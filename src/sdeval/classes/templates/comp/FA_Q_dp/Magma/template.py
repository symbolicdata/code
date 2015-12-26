"""
This is the template for the computation problem of computing a Groebner basis of an
ideal in a free algebra over QQ in the computeralgebra system Magma.

.. moduleauthor:: Albert Heinle <albert.heinle@rwth-aachen.de>
"""

#--------------------------------------------------
#---------------The template-----------------------
#--------------------------------------------------

def generateCode(vars, basis, uptoDeg):
    """
    The main function generating the Magma code for the computation of
    the Groebner basis given the input variables.

    :param         vars: A list of variables used in the FreeAlgebra-System
    :type          vars: list
    :param        basis: The polynomials forming a basis of the FreeAlgebra-System. This input will not be checked whether
                         there are polynomials using variables not in the list of variables.
    :type         basis: list
    :param      uptoDeg: The uptoDeg Entry.
    :type       uptoDeg: unsigned int
    """
    result = "\
F := RationalField();\n\
A<%s> := FreeAlgebra(F,%i);\n\
B := [%s];\n\
GroebnerBasis(B,%i);\n\
quit;" % (",".join(vars), len(vars), ",\n".join(basis), uptoDeg)
    return result

#--------------------------------------------------
#----------------Help Functions--------------------
#--------------------------------------------------
