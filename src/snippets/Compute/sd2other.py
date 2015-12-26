#!/usr/bin/env python
# encoding: utf-8
#Author: Michael Brickenstein
# (c) 2007 by
#Mathematisches Forschungsinstitut Oberwolfach gGmbH
#Created 30.1.2007

import lxml.etree as et
from optparse import OptionParser
from os.path import basename
from copy import copy
from string import Template
from exceptions import NotImplementedError
MAGMA="magma"
STD="std"
SLIMGB="slimgb"
SLIMGBTEST="slimgbtest"
COCOA4="cocoa4"
COCOA5="cocoa5"
ASIR="asir"
ALL="all"
DP="dp"
LP="lp"
all_formats=[]
really_all_formats=[ALL]
converters=dict()
def register_converter(name,converter,in_all=True):
  converters[name]=converter
  if in_all:
    all_formats.append(name)
  really_all_formats.append(name)
parser=OptionParser()
parser.add_option("--output-dir",
                  action="store", type="string",dest="output_dir", default=".",
                  help="output directory")

parser.add_option("--asir-gr-dir",
                  action="store", type="string",dest="asir_gr_dir", default="/users/urmel/alggeom/bulygin/asir/OpenXM_contrib2/asir2000/lib",
                  help="directory of asir contrib libs")




parser.add_option("--ordering",
                  action="store", dest="ordering", type="choice",
                  choices=[DP,LP],default=DP,
                  help="select monomial ordering")

parser.add_option("--char", action="store", type="int",dest="char", default=0,
                  help="characteristic")

singular_out_template=Template("""
  ring MYRINGNAME=$char,($vars_str),$ordering;
  ideal MYIDEALNAME=$polys_str;
  timer=1;
  option(prot);
  $alg(MYIDEALNAME);
  memory(2);
  exit;
  """)

singular_test_template=Template("""
    LIB "tst.lib";
    tst_init();
    ring MYRINGNAME=$char,($vars_str),$ordering;
    ideal MYIDEALNAME=$polys_str;
    option(redSB);
    $alg(MYIDEALNAME);
    kill MYRINGNAME;
    tst_status(1);exit;
    """)

magma_out_template=Template("""MYFIELDNAME:=$field;
  MYRINGNAME< $vars_str >:=PolynomialRing(MYFIELDNAME,$nvars,"$ordering");
  MYIDEALNAME:=ideal< MYRINGNAME | $polys_str
  >;
  GroebnerBasis(MYIDEALNAME);
  exit;
  """)

cocoa_out_template=Template("""
Use R ::= $field[$vars_str],$ordering;
I := Ideal($polys_str);
$alg(I);
""")

asir_out_template_char0=Template("""
load("$contrib/gr");
MYIDEALNAME=[$polys_str];

T0=time()$$
gr(MYIDEALNAME,[$vars_str],0);
T1=time()$$
T1[0]-T0[0];
T1[2]*4;
""")


asir_out_template_modp=Template("""
load("$contrib/gr");
MYIDEALNAME=[$polys_str];

T0=time()$$
gr_mod(MYIDEALNAME,[$vars_str],0,$char);
T1=time()$$
T1[0]-T0[0];
""")
def asir_converter(ordering,char,**kwds):
  if ordering!=DP:
    raise NotImplementedError
  kwds["contrib"]=opts.asir_gr_dir
  kwds["char"]=char
  if char>0:
    asir_out_template=asir_out_template_modp
  else:
    asir_out_template=asir_out_template_char0
  return asir_out_template.substitute(kwds)
def cocoa_converter(alg):
  def converter(char,ordering,polys_str,vars,**kwds):
    if len(vars)>26:
       print repr(vars)
       raise NotImplementedError
    if char!=0:
      field="Z/("+str(char)+")"
    else:
      field="Q"
    #TODO: first translate in neutral symbols
    ordering_table={LP:"Lex",DP:"DegRevLex"}
    kwds=copy(kwds)
    old_vars=vars
    vars=[chr(ord("a")+i) for i in xrange(0,len(vars))]
    kwds["vars"]=vars
    kwds["vars_str"]=", ".join(vars)
    intermediate_vars=[chr(1)+str(i)+chr(2) for i in xrange(len(vars))]
    vars_table_final=dict([(intermediate_vars[i],vars[i]) for i in xrange(len(vars))])
    vars_table_intermediate=dict([(old_vars[i],intermediate_vars[i]) for i in xrange(len(vars))])
    vars_sorted=reversed(sorted(old_vars,key=len))
    
    for v in vars_sorted:
      polys_str=polys_str.replace(v,vars_table_intermediate[v])
    for v in intermediate_vars:
      polys_str=polys_str.replace(v,vars_table_final[v])
    kwds["ordering"]=ordering_table[ordering]
    kwds["alg"]=alg
    kwds["polys_str"]=polys_str
    kwds["field"]=field
    return cocoa_out_template.substitute(kwds)
  return converter

def singular_converter(alg):
  def converter(**kwds):
    kwds=copy(kwds)
    kwds["alg"]=alg
    return singular_out_template.substitute(kwds)
  return converter
 
def singular_test_converter(alg):
  def converter(**kwds):
    kwds=copy(kwds)
    kwds["alg"]=alg
    return singular_test_template.substitute(kwds)
  return converter
def magma_converter(vars,vars_str,char,polys_str,ordering,**kwds):
  ordering_table={LP:"lex",DP:"grevlex"}
  ordering=ordering_table[ordering]
  if char>0:
    field="FiniteField("+str(char)+")"
  else:
    field="RationalField()"
  return magma_out_template.substitute(dict(ordering=ordering,field=field,polys_str=polys_str,vars_str=vars_str,nvars=len(vars)))

for a in [STD,SLIMGB]:
  register_converter(a,singular_converter(a))
register_converter(SLIMGBTEST,singular_test_converter("slimgb"))
register_converter(MAGMA,magma_converter)
for (n,a) in [(COCOA4,"GBasis"),(COCOA5,"GBasis5")]:
  register_converter(n,cocoa_converter(a),in_all=False)
register_converter(ASIR,asir_converter,in_all=False)
parser.add_option("-f", "--format",
                  action="store", dest="format", type="choice",
                  choices=really_all_formats,default=STD,
                  help="select format from SING/PB")
if __name__=='__main__':
  (opts,args)=parser.parse_args()
  opts.output_dir=opts.output_dir+"/"
  for a in args:
    base=basename(a).replace(".xml","")
    tree=et.parse(a)
    root=tree.getroot()
    basis=root.find("basis")
    #homog=root.find("isHomog").text
    homog=0
    polys=basis.findall("poly")
    vars=root.find("vars").text
    vars=vars.replace("]","")
    vars=vars.replace("[","")
    vars=vars.split(" ")
    vars=[v.strip() for v in vars]
    
    if int(homog):
      homog_suffix="_HOMOG"
    else:
      homog_suffix=""
    polys_str=",\n".join((p.text for p in polys))
  
    format=opts.format
    if format==ALL:
      format=all_formats
    else:
      format=[format]
    for f in format:
      out=open(opts.output_dir+base+homog_suffix+"_"+str(opts.char)+"_"+str(opts.ordering)+"."+f,"w")
      out.write(converters[f](vars=vars,nvars=len(vars),vars_str=", ".join(vars), polys=polys,homog=homog,polys_str=polys_str,char=opts.char,ordering=opts.ordering))  
      out.close()
