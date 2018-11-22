"""
This is the template for the computation problem of computing a Groebner basis of an
ideal in a free algebra over QQ in the computeralgebra system Singular.

.. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
"""

#--------------------------------------------------
#---------------The template-----------------------
#--------------------------------------------------

def generateCode(vars, basis, uptoDeg):
    """
    The main function generating the Singular code for the computation of
    the Groebner basis given the input variables.

    :param         vars: A list of variables used in the FreeAlgebras-System
    :type          vars: list
    :param        basis: The polynomials forming a basis of the FreeAlgebras-System. This input will not be checked whether
                         there are polynomials using variables not in the list of variables.
    :type         basis: list
    :param      uptoDeg: The uptoDeg Entry.
    :type       uptoDeg: unsigned int
    """
    result = ""
    result += "LIB \"freegb.lib\";\n"
    result += "ring r = 0,(%s),dp;\n" % ",".join(vars)
    result += "int upToDeg = %i;\n" % uptoDeg
    result += "def R = makeLetterplaceRing(upToDeg);\nsetring(R);\n"
    result += "ideal Id = %s;\n" % ",\n".join(v for v in basis)
    result += "option(prot);\noption(redTail);\noption(redSB);\n"
    result += "ideal IdSTD = std(Id);\n"
    result += "print(\"=====Solution Begin=====\");\n"
    result += "print (IdSTD, \"%s\");\n"
    result += "print (varstr(r), \"%s\");\n"
    result += "print (upToDeg, \"%s\");\n"
    result += "print (Id, \"%s\");\n"
    result += "print(\"=====Solution End=====\");"
    result += "$;"
    return result
