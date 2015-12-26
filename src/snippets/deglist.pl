##################################
#
# author: graebe
# createdAt: 2006-03-03
# lastUpdate: 2013-08-25

# purpose: compute theDegreeList and theLengthsList using MuPAD. 
# Save the output of this script as in.txt and run it with MuPAD as
# 'mupkern <in.txt >out.txt'

# remark: obsolete in SymbolicData v.3, since degree list and lengths list
# depend on the base ring of the polynomials. These result are valid only for
# the flat ideals associated with the polynomial systems.

use strict;
use XML::DOM;

my $parser=new XML::DOM::Parser;
print("Pref::echo(FALSE):Pref::prompt(FALSE):\n");
map action($_), @ARGV;
print("quit;\n");

# === end main ===

sub action {
  my $fn=shift;
  my $doc=$parser->parsefile($fn) or die;
  my $vars=getTagValue($doc,"vars");
  my @l;
  map push(@l,getValue($_)), $doc->getElementsByTagName("poly");
  my $polys=join(",\n",@l);
  print <<EOT;
vars:=[$vars]:
polys:=[$polys]:
dlist:=sort(map(polys,degree)):
llist:=sort(map(polys,nops)):
print(NoNL,"<Result filename=\\"$fn\\" dlist=\\"".expr2text(dlist)
       ."\\" llist=\\"".expr2text(llist)."\\"/>\n");
EOT
}

sub getTagValue {
  my ($doc,$tag)=@_;
  map { return getValue($_); } $doc->getElementsByTagName($tag);
  return;
}

sub getValue {
  my $node=shift;
  local $_=$node->toString(1);
  s/^\s*<[^>]*?>\s*//s;
  s/\s*<\/[^>]*?>\s*$//s;
  return $_;
}
