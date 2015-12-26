"""
This is the template for the computation problem of computing a Groebner basis of an
ideal in a free algebra over QQ in the computeralgebra system GAP.

.. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
"""

#--------------------------------------------------
#---------------The template-----------------------
#--------------------------------------------------

def generateCode(vars, basis, uptoDeg):
    """
    The main function generating the GAP code for the computation of
    the Groebner basis given the input variables.

    :param         vars: A list of variables used in the FreeAlgebra-System
    :type          vars: list
    :param        basis: The polynomials forming a basis of the FreeAlgebra-System. This input will not be checked whether
                         there are polynomials using variables not in the list of variables.
    :type         basis: list
    :param      uptoDeg: The uptoDeg Entry.
    :type       uptoDeg: unsigned int
    """
    rev = vars
    rev.reverse()
    result = "\
LoadPackage(\"GBNP\",\"0\",false);\n\
SetInfoLevel(InfoGBNP,1);\n\
SetInfoLevel(InfoGBNPTime,1);\n\
F := Rationals;\n\
A := FreeAssociativeAlgebraWithOne(F,%s);\n\
g :=GeneratorsOfAlgebraWithOne(A);\n\
%s;\n\
weights := [%s];\n\
KI_gp := [%s];\n\
KI_np :=GP2NPList(KI_gp);\n\
GB :=SGrobnerTrunc(KI_np,%i,weights);\n\
GBNP.ConfigPrint(%s);\n\
PrintNPList(GB);\n\
Length(GB);\n\
quit;\
" % (",".join(str("\""+v+"\"") for v in rev),
     "\n".join((rev)[i] + " := g["+str(i+1)+"];" for i in range(len(vars))),
     ",".join("1" for v in vars),
     ",".join(basis),
     uptoDeg,
     ",".join(str("\""+v+"\"") for v in rev)
     )
    return result

#--------------------------------------------------
#----------------Help Functions--------------------
#--------------------------------------------------
