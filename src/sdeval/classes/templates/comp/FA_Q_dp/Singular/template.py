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

    :param         vars: A list of variables used in the FreeAlgebra-System
    :type          vars: list
    :param        basis: The polynomials forming a basis of the FreeAlgebra-System. This input will not be checked whether
                         there are polynomials using variables not in the list of variables.
    :type         basis: list
    :param      uptoDeg: The uptoDeg Entry.
    :type       uptoDeg: unsigned int
    """
    result = ""
    result += "LIB \"freegb.lib\";\n"
    result += "ring r = 0,(%s),dp;\n" % ",".join(vars)
    result += "int d = %i;\n" % uptoDeg
    result += "def R = makeLetterplaceRing(d);\n setring(R);\n"
    result += "ideal I = %s;\n" % ",\n".join(FAPolyToSingularStyle(v,vars) for v in basis)
    result += "option(prot);\noption(redTail);\noption(redSB);\n"
    result += "ideal J = letplaceGBasis(I);\n"
    result += "print (\">>Output Start\");\n"
    result += "print (J, \"%s\");\n"
    result += "print (\"<<Output End\");$"
    return result

#--------------------------------------------------
#----------------Help Functions--------------------
#--------------------------------------------------

def FAPolyToSingularStyle(poly,variables):
        """
        Input: A Polynomial (Freealgebra) in the MAGMA-Style, and the variables
               in the corresponding free algebra
        Output: A Polynomial in the Letterplace Style (with their positions as
                arguments)
        :param      poly: The polynomial given in MAGMA-Style
        :type       poly: string
        :param variables: A list containing the occurring variables.
        :type  variables: list
        """
        result = ""
        plusSplit = poly.split("+")
        for p in plusSplit:
            minusSplit = p.split("-")
            for ms in minusSplit:
                monomials = ms.split("*")
                i = 1
                for m in monomials:
                    if m.strip() not in variables: #Coefficient
                        result += m+"*"
                        continue
                    m = m.strip()+"("+str(i)+")"
                    result += m.strip()+"*"
                    i=i+1
                result = result[:-1] #one * too much
                result += "-"
            result = result[:-1]
            result += "+"
        result = result[:-1]
        return result
