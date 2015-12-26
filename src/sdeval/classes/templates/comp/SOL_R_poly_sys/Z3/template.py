"""
This is the template for the computation problem of finding real solutions of a polynomial system of equations.
It creates code for an SMT solver like Z3.

.. moduleauthor:: Albert Heinle <albert.heinle@googlemail.com>
"""

#--------------------------------------------------
#---------------The template-----------------------
#--------------------------------------------------

def generateCode(vars, basis):
    """
    The main function generating the SMT2 code for the computation of
    the real solution of a polynomial system of equations.

    :param         vars: A list of variables used in the IntPS-System
    :type          vars: list
    :param        basis: The polynomials forming a basis of the IntPS-System. This input will not be checked whether
                         there are polynomials using variables not in the list of variables.
    :type         basis: list
    """
    result = ""
    for v in vars:
        result+="(declare-const %s Real)\n" % v
    for b in basis:
        result+=polyIntoLispStyle(b)
        result+="\n"
    result += """
(echo "=====Solution Begin=====")
(check-sat)
(echo "=====Solution End=====")
(exit)
"""
    return result

#--------------------------------------------------
#----------------Help Functions--------------------
#--------------------------------------------------
def polyIntoLispStyle(poly):
    result = "(assert (= "
    if "+" in poly:
        polySplit = filter(lambda x: x!= '', poly.split("+"))
        result += "(+ "
        for ms in polySplit:
            result += evalPlusFreePart(ms) + " "
        result += ")"
    else:
        result += evalPlusFreePart(poly)
    return result + " 0))"

def evalPlusFreePart(s):
    result = ""
    if "-" in s:
        ssplit = filter(lambda x: x!='',s.split("-"))
        if len(ssplit)<=1:
            result += "(- 0" + getMonomialRep(ssplit[0]) + ")"
        else:
            result += "(- "
            for ms in ssplit:
                result += getMonomialRep(ms) + " "
            result += ")"
    else:
        result = getMonomialRep(s)
    return result

def getMonomialRep(s):
    result = ""
    if "*" in s:
        result +="(* "
        mons = s.split("*")
        for ms in mons:
            if "^" in ms:
                msSplit = ms.split("^")
                result += " ".join(msSplit[0].strip() for i in range(int(msSplit[1])))
                result += " "
            else:
                result += ms.strip() + " "
        result +=")"
    else:
        if "^" in s:
            ssplit = s.split("^")
            result += "(* "
            result += " ".join([ssplit[0].strip() for i in range (int(ssplit[1]))])
            result += ")"
        else:
            result = s.strip()
    return result
            
