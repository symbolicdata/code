import unittest

class TestTemplatesSOL(unittest.TestCase):
    """
    Tests for the different templates to extract the solution from the
    output of the computer algebra systems.

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """

    def test_FA_Q_dp_Singular_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Singular output on a FA_Q_dp-instance, i.e. the
        computation of a Groebner basis over the free algebra.

        The module consists of two functions:
        1.) extractSolution(outpString)
        2.) convertFromLetterplace(inpPoly):
        
        We test both functions here. The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by Singular.
        2.1) Giving a string where nothing needs to be replaced (1 as
             solution e.g.)
        2.2) Polynomial with "-" at the front
        2.3) Polynomial with multiple monomials
        2.4) Polynomial with alternating + and - signs.
        """
        from comp.FA_Q_dp.Singular.template_sol import extractSolution
        from comp.FA_Q_dp.Singular.template_sol import convertFromLetterplace
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "x(1)" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<FA_Q_dp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</FA_Q_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        singularOutput = """                     SINGULAR                                 /
 A Computer Algebra System for Polynomial Computations       /   version 3-1-7
                                                           0<
 by: W. Decker, G.-M. Greuel, G. Pfister, H. Schoenemann     \   Aug 2013
FB Mathematik der Universitaet, D-67653 Kaiserslautern        \
// ** loaded /Applications/Singular/3-1-7/LIB/freegb.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/bfun.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/presolve.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/elim.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/poly.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/ring.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/primdec.lib (3-1-7-0,Jan_2014)
// ** loaded /Applications/Singular/3-1-7/LIB/absfact.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/triang.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/random.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/matrix.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/general.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/inout.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/nctools.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/dmodapp.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/sing.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/gkdim.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/dmod.lib (3-1-7-1,jan_2014)
// ** loaded /Applications/Singular/3-1-7/LIB/control.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/homolog.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/deform.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/gmssing.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/linalg.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/qhmoduli.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/rinvar.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/zeroset.lib (3-1-7-0,Sep_2013)
// ** loaded /Applications/Singular/3-1-7/LIB/primitiv.lib (3-1-7-0,Sep_2013)
[3:15]2(5)s(4)s(5)s(6)sss3(8)s(9)s(12)s(16)s(18)s(21)s(27)s(30)s(37)s4(48)s(55)s(64)s(73)s(82)--s(92)s(101)s(110)s(119)s(129)s(139)s(151)-s(164)s(178)s(193)s(208)s(223)-s(237)s(252)--s(265)-s(275)----5-----------------------------------------------------------------------(200)---------------------------------------------------------------------6-------------------------------(100)------------------------------------------------7----------------------------------------------------
(S:34)----------------------------------
product criterion:825 chain criterion:110
shift V criterion:3755
=====Solution Begin=====
x2(1)*x1(2)+4*x1(1)*x2(2)-3*x1(1)*x1(2),x2(1)*x2(2)-4*x1(1)*x3(2)+54*x1(1)*x2(2)-40*x1(1)*x1(2),x3(1)*x3(2)-9*x3(1)*x2(2)+2*x1(1)*x4(2)+x1(1)*x1(2),17*x4(1)*x2(2)-41*x1(1)*x4(2)-20*x1(1)*x3(2)+270*x1(1)*x2(2)-200*x1(1)*x1(2),17*x4(1)*x3(2)+204*x4(1)*x1(2)-153*x3(1)*x4(2)+68*x3(1)*x2(2)+697*x3(1)*x1(2)+414*x1(1)*x4(2)+260*x1(1)*x3(2)-3527*x1(1)*x2(2)+2600*x1(1)*x1(2),17*x4(1)*x4(2)-1042*x1(1)*x4(2)-602*x1(1)*x3(2)+6597*x1(1)*x2(2)-4983*x1(1)*x1(2),4*x1(1)*x3(2)*x1(3)-64*x1(1)*x1(2)*x3(3)+1044*x1(1)*x1(2)*x2(3)-735*x1(1)*x1(2)*x1(3),2*x1(1)*x3(2)*x2(3)+8*x1(1)*x2(2)*x3(3)-546*x1(1)*x1(2)*x3(3)+7071*x1(1)*x1(2)*x2(3)-5220*x1(1)*x1(2)*x1(3),306*x3(1)*x2(2)*x3(3)+68*x3(1)*x1(2)*x4(3)-11016*x3(1)*x1(2)*x3(3)+148716*x3(1)*x1(2)*x2(3)-110126*x3(1)*x1(2)*x1(3)+816*x1(1)*x4(2)*x1(3)-612*x1(1)*x3(2)*x4(3)-1088*x1(1)*x2(2)*x3(3)+3132*x1(1)*x1(2)*x4(3)+120590*x1(1)*x1(2)*x3(3)-1712846*x1(1)*x1(2)*x2(3)+1239815*x1(1)*x1(2)*x1(3),4945294458*x3(1)*x2(2)*x4(3)-11590928206*x3(1)*x1(2)*x4(3)-16154463546*x3(1)*x1(2)*x3(3)+292437150876*x3(1)*x1(2)*x2(3)-220005283238*x3(1)*x1(2)*x1(3)+1136470308*x1(1)*x4(2)*x1(3)-2875259808*x1(1)*x3(2)*x4(3)+25990312050*x1(1)*x2(2)*x4(3)-293454954050*x1(1)*x2(2)*x3(3)-37682827965*x1(1)*x1(2)*x4(3)+16792204874504*x1(1)*x1(2)*x3(3)-215661366909620*x1(1)*x1(2)*x2(3)+159500235636143*x1(1)*x1(2)*x1(3),168140011572*x3(1)*x4(2)*x1(3)-2016140964916*x3(1)*x1(2)*x4(3)-1263283387704*x3(1)*x1(2)*x3(3)+13710091274100*x3(1)*x1(2)*x2(3)-11177637711968*x3(1)*x1(2)*x1(3)-2456678073810*x1(1)*x4(2)*x1(3)-988966678500*x1(1)*x3(2)*x4(3)+13446943729218*x1(1)*x2(2)*x4(3)-136417952624228*x1(1)*x2(2)*x3(3)-849620756475*x1(1)*x1(2)*x4(3)+7763955728363828*x1(1)*x1(2)*x3(3)-99574514167841120*x1(1)*x1(2)*x2(3)+73663405211507060*x1(1)*x1(2)*x1(3),154037*x4(1)*x1(2)*x1(3)-1285965*x1(1)*x4(2)*x1(3)-839188*x1(1)*x3(2)*x4(3)+9196218*x1(1)*x2(2)*x4(3)-85464304*x1(1)*x2(2)*x3(3)-6756349*x1(1)*x1(2)*x4(3)+4878039136*x1(1)*x1(2)*x3(3)-62608070032*x1(1)*x1(2)*x2(3)+46309301943*x1(1)*x1(2)*x1(3),616148*x4(1)*x1(2)*x2(3)-3486394*x1(1)*x4(2)*x1(3)-2517564*x1(1)*x3(2)*x4(3)+27588654*x1(1)*x2(2)*x4(3)-256392912*x1(1)*x2(2)*x3(3)-20269047*x1(1)*x1(2)*x4(3)+14637016928*x1(1)*x1(2)*x3(3)-187861722636*x1(1)*x1(2)*x2(3)+138955677794*x1(1)*x1(2)*x1(3),1232296*x4(1)*x1(2)*x3(3)+8744562*x1(1)*x4(2)*x1(3)-839188*x1(1)*x3(2)*x4(3)+9196218*x1(1)*x2(2)*x4(3)-84014544*x1(1)*x2(2)*x3(3)-8548295*x1(1)*x1(2)*x4(3)+4876077696*x1(1)*x1(2)*x3(3)-62595544532*x1(1)*x1(2)*x2(3)+46300152998*x1(1)*x1(2)*x1(3),11849*x4(1)*x1(2)*x4(3)+689112*x1(1)*x2(2)*x3(3)-717869*x1(1)*x1(2)*x4(3)-39847742*x1(1)*x1(2)*x3(3)+510679730*x1(1)*x1(2)*x2(3)-377804060*x1(1)*x1(2)*x1(3),x1(1)*x1(2)*x1(3)*x1(4),x1(1)*x1(2)*x1(3)*x2(4),x1(1)*x1(2)*x1(3)*x3(4),x1(1)*x1(2)*x1(3)*x4(4),x1(1)*x1(2)*x2(3)*x3(4),x1(1)*x1(2)*x2(3)*x4(4),x1(1)*x1(2)*x3(3)*x4(4),x1(1)*x1(2)*x4(3)*x1(4),x1(1)*x2(2)*x3(3)*x1(4),x1(1)*x2(2)*x3(3)*x2(4),x1(1)*x2(2)*x3(3)*x4(4),x1(1)*x2(2)*x4(3)*x1(4),x3(1)*x1(2)*x1(3)*x1(4),x3(1)*x1(2)*x1(3)*x2(4),x3(1)*x1(2)*x1(3)*x3(4),x3(1)*x1(2)*x1(3)*x4(4),x3(1)*x1(2)*x2(3)*x3(4),x3(1)*x1(2)*x2(3)*x4(4),x3(1)*x1(2)*x3(3)*x4(4),x3(1)*x1(2)*x4(3)*x1(4)
=====Solution End=====

$Bye.
real 1.58
user 1.52
sys 0.04"""
        try:
            tempRes = extractSolution(singularOutput)
        except:
            self.fail("Could not parse valid Singular output string")
        expectedOutp = """<?xml version="1.0" ?>
<FA_Q_dp_SOL>
  <basis>
    <polynomial>x2*x1+4*x1*x2-3*x1*x1</polynomial>
    <polynomial>x2*x2-4*x1*x3+54*x1*x2-40*x1*x1</polynomial>
    <polynomial>x3*x3-9*x3*x2+2*x1*x4+x1*x1</polynomial>
    <polynomial>17*x4*x2-41*x1*x4-20*x1*x3+270*x1*x2-200*x1*x1</polynomial>
    <polynomial>17*x4*x3+204*x4*x1-153*x3*x4+68*x3*x2+697*x3*x1+414*x1*x4+260*x1*x3-3527*x1*x2+2600*x1*x1</polynomial>
    <polynomial>17*x4*x4-1042*x1*x4-602*x1*x3+6597*x1*x2-4983*x1*x1</polynomial>
    <polynomial>4*x1*x3*x1-64*x1*x1*x3+1044*x1*x1*x2-735*x1*x1*x1</polynomial>
    <polynomial>2*x1*x3*x2+8*x1*x2*x3-546*x1*x1*x3+7071*x1*x1*x2-5220*x1*x1*x1</polynomial>
    <polynomial>306*x3*x2*x3+68*x3*x1*x4-11016*x3*x1*x3+148716*x3*x1*x2-110126*x3*x1*x1+816*x1*x4*x1-612*x1*x3*x4-1088*x1*x2*x3+3132*x1*x1*x4+120590*x1*x1*x3-1712846*x1*x1*x2+1239815*x1*x1*x1</polynomial>
    <polynomial>4945294458*x3*x2*x4-11590928206*x3*x1*x4-16154463546*x3*x1*x3+292437150876*x3*x1*x2-220005283238*x3*x1*x1+1136470308*x1*x4*x1-2875259808*x1*x3*x4+25990312050*x1*x2*x4-293454954050*x1*x2*x3-37682827965*x1*x1*x4+16792204874504*x1*x1*x3-215661366909620*x1*x1*x2+159500235636143*x1*x1*x1</polynomial>
    <polynomial>168140011572*x3*x4*x1-2016140964916*x3*x1*x4-1263283387704*x3*x1*x3+13710091274100*x3*x1*x2-11177637711968*x3*x1*x1-2456678073810*x1*x4*x1-988966678500*x1*x3*x4+13446943729218*x1*x2*x4-136417952624228*x1*x2*x3-849620756475*x1*x1*x4+7763955728363828*x1*x1*x3-99574514167841120*x1*x1*x2+73663405211507060*x1*x1*x1</polynomial>
    <polynomial>154037*x4*x1*x1-1285965*x1*x4*x1-839188*x1*x3*x4+9196218*x1*x2*x4-85464304*x1*x2*x3-6756349*x1*x1*x4+4878039136*x1*x1*x3-62608070032*x1*x1*x2+46309301943*x1*x1*x1</polynomial>
    <polynomial>616148*x4*x1*x2-3486394*x1*x4*x1-2517564*x1*x3*x4+27588654*x1*x2*x4-256392912*x1*x2*x3-20269047*x1*x1*x4+14637016928*x1*x1*x3-187861722636*x1*x1*x2+138955677794*x1*x1*x1</polynomial>
    <polynomial>1232296*x4*x1*x3+8744562*x1*x4*x1-839188*x1*x3*x4+9196218*x1*x2*x4-84014544*x1*x2*x3-8548295*x1*x1*x4+4876077696*x1*x1*x3-62595544532*x1*x1*x2+46300152998*x1*x1*x1</polynomial>
    <polynomial>11849*x4*x1*x4+689112*x1*x2*x3-717869*x1*x1*x4-39847742*x1*x1*x3+510679730*x1*x1*x2-377804060*x1*x1*x1</polynomial>
    <polynomial>x1*x1*x1*x1</polynomial>
    <polynomial>x1*x1*x1*x2</polynomial>
    <polynomial>x1*x1*x1*x3</polynomial>
    <polynomial>x1*x1*x1*x4</polynomial>
    <polynomial>x1*x1*x2*x3</polynomial>
    <polynomial>x1*x1*x2*x4</polynomial>
    <polynomial>x1*x1*x3*x4</polynomial>
    <polynomial>x1*x1*x4*x1</polynomial>
    <polynomial>x1*x2*x3*x1</polynomial>
    <polynomial>x1*x2*x3*x2</polynomial>
    <polynomial>x1*x2*x3*x4</polynomial>
    <polynomial>x1*x2*x4*x1</polynomial>
    <polynomial>x3*x1*x1*x1</polynomial>
    <polynomial>x3*x1*x1*x2</polynomial>
    <polynomial>x3*x1*x1*x3</polynomial>
    <polynomial>x3*x1*x1*x4</polynomial>
    <polynomial>x3*x1*x2*x3</polynomial>
    <polynomial>x3*x1*x2*x4</polynomial>
    <polynomial>x3*x1*x3*x4</polynomial>
    <polynomial>x3*x1*x4*x1</polynomial>
  </basis>
</FA_Q_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for Singular output parse.")
        #2.1.a)
        self.assertEqual("1", convertFromLetterplace("1"), "Could not \
parse a single number")
        self.assertEqual("-1", convertFromLetterplace("-1"), "Could not \
parse a negative number")
        #2.2)
        self.assertEqual("-x", convertFromLetterplace("-x(1)"), "Could \
not parse a polynomial with negative sign.")
        #2.3)
        self.assertEqual("x*y*x + z*y",
                         convertFromLetterplace("x(1)*y(2)*x(3) + \
z(1)*y(2)"),
                         "Could not parse a polynomial consisting of \
multiple monomials")
        #2.4
        self.assertEqual("x*y*z + z - z*y +x*y - y",
                         convertFromLetterplace("x(1)*y(2)*z(3) + z(1) \
- z(1)*y(2) +x(1)*y(2) - y(1)"),
                         "Could not parse polynomial with alternating signs")


    def test_FA_Q_dp_Magma_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Magma output on a FA_Q_dp-instance, i.e. the
        computation of a Groebner basis over the free algebra.

        We test both functions here. The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by Magma.
        """
        from comp.FA_Q_dp.Magma.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "[x1]" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<FA_Q_dp_SOL>
  <basis>
    <polynomial>x1</polynomial>
  </basis>
</FA_Q_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2b)
        magmaOutput ="""Magma V2.19-2     Tue Aug 12 2014 19:33:57 on emmy     [Seed = 3154493372]
Type ? for help.  Type <Ctrl>-D to quit.
=====Solution Begin=====
[
    u^3*v*u*v^2*u^3*v*u*v^2 - 1,
    u*v^11*u*V - v*U^13,
    u*v^12*U - v*U^12*V,
    U*V^11*U*v - V*u^13,
    U*V^12*u - V*u^12*v,
    u*v^10*u*V - v*U^12,
    u*v^11*U - v*U^11*V,
    U*V^10*U*v - V*u^12,
    U*V^11*u - V*u^11*v,
    u*v^9*u*V - v*U^11,
    u*v^10*U - v*U^10*V,
    U*V^9*U*v - V*u^11,
    U*V^10*u - V*u^10*v,
    u*v^8*u*V - v*U^10,
    u*v^9*U - v*U^9*V,
    U*V^8*U*v - V*u^10,
    U*V^9*u - V*u^9*v,
    u*v^7*u*V - v*U^9,
    u*v^8*U - v*U^8*V,
    U*V^7*U*v - V*u^9,
    U*V^8*u - V*u^8*v,
    u*v^6*u*V - v*U^8,
    u*v^7*U - v*U^7*V,
    U*V^6*U*v - V*u^8,
    U*V^7*u - V*u^7*v,
    u*v^5*u*V - v*U^7,
    u*v^6*U - v*U^6*V,
    U*V^5*U*v - V*u^7,
    U*V^6*u - V*u^6*v,
    u*v^4*u*V - v*U^6,
    u*v^5*U - v*U^5*V,
    U*V^4*U*v - V*u^6,
    U*V^5*u - V*u^5*v,
    u*v^3*u*V - v*U^5,
    u*v^4*U - v*U^4*V,
    U*V^3*U*v - V*u^5,
    U*V^4*u - V*u^4*v,
    u*v^2*u*V - v*U^4,
    u*v^3*U - v*U^3*V,
    U*V^2*U*v - V*u^4,
    U*V^3*u - V*u^3*v,
    u*v*u*V - v*U^3,
    u*v^2*U - v*U^2*V,
    U*V*U*v - V*u^3,
    U*V^2*u - V*u^2*v,
    V^2*u*V - U*v,
    u^2*V - v*U^2,
    u*v*U - v*U*V,
    u*V*u - V*u*V,
    u*V*U - v*u*V,
    u*V^2 - v^2*U,
    v*U*v - V*u*V,
    U*v*u - V*U*v,
    U*v^2 - V^2*u,
    U*v*U - V*u*V,
    U^2*v - V*u^2,
    U*V*u - V*u*v,
    u*U - 1,
    v*V - 1,
    U*u - 1,
    V*v - 1
]
=====Solution End=====

Total time: 0.380 seconds, Total memory usage: 11.03MB
real 0.41
user 0.31
sys 0.10"""
        try:
            tempRes = extractSolution(magmaOutput)
        except:
            self.fail("Could not parse valid Magma output string")
        expectedOutp = """<?xml version="1.0" ?>
<FA_Q_dp_SOL>
  <basis>
    <polynomial>u^3*v*u*v^2*u^3*v*u*v^2 - 1</polynomial>
    <polynomial>u*v^11*u*V - v*U^13</polynomial>
    <polynomial>u*v^12*U - v*U^12*V</polynomial>
    <polynomial>U*V^11*U*v - V*u^13</polynomial>
    <polynomial>U*V^12*u - V*u^12*v</polynomial>
    <polynomial>u*v^10*u*V - v*U^12</polynomial>
    <polynomial>u*v^11*U - v*U^11*V</polynomial>
    <polynomial>U*V^10*U*v - V*u^12</polynomial>
    <polynomial>U*V^11*u - V*u^11*v</polynomial>
    <polynomial>u*v^9*u*V - v*U^11</polynomial>
    <polynomial>u*v^10*U - v*U^10*V</polynomial>
    <polynomial>U*V^9*U*v - V*u^11</polynomial>
    <polynomial>U*V^10*u - V*u^10*v</polynomial>
    <polynomial>u*v^8*u*V - v*U^10</polynomial>
    <polynomial>u*v^9*U - v*U^9*V</polynomial>
    <polynomial>U*V^8*U*v - V*u^10</polynomial>
    <polynomial>U*V^9*u - V*u^9*v</polynomial>
    <polynomial>u*v^7*u*V - v*U^9</polynomial>
    <polynomial>u*v^8*U - v*U^8*V</polynomial>
    <polynomial>U*V^7*U*v - V*u^9</polynomial>
    <polynomial>U*V^8*u - V*u^8*v</polynomial>
    <polynomial>u*v^6*u*V - v*U^8</polynomial>
    <polynomial>u*v^7*U - v*U^7*V</polynomial>
    <polynomial>U*V^6*U*v - V*u^8</polynomial>
    <polynomial>U*V^7*u - V*u^7*v</polynomial>
    <polynomial>u*v^5*u*V - v*U^7</polynomial>
    <polynomial>u*v^6*U - v*U^6*V</polynomial>
    <polynomial>U*V^5*U*v - V*u^7</polynomial>
    <polynomial>U*V^6*u - V*u^6*v</polynomial>
    <polynomial>u*v^4*u*V - v*U^6</polynomial>
    <polynomial>u*v^5*U - v*U^5*V</polynomial>
    <polynomial>U*V^4*U*v - V*u^6</polynomial>
    <polynomial>U*V^5*u - V*u^5*v</polynomial>
    <polynomial>u*v^3*u*V - v*U^5</polynomial>
    <polynomial>u*v^4*U - v*U^4*V</polynomial>
    <polynomial>U*V^3*U*v - V*u^5</polynomial>
    <polynomial>U*V^4*u - V*u^4*v</polynomial>
    <polynomial>u*v^2*u*V - v*U^4</polynomial>
    <polynomial>u*v^3*U - v*U^3*V</polynomial>
    <polynomial>U*V^2*U*v - V*u^4</polynomial>
    <polynomial>U*V^3*u - V*u^3*v</polynomial>
    <polynomial>u*v*u*V - v*U^3</polynomial>
    <polynomial>u*v^2*U - v*U^2*V</polynomial>
    <polynomial>U*V*U*v - V*u^3</polynomial>
    <polynomial>U*V^2*u - V*u^2*v</polynomial>
    <polynomial>V^2*u*V - U*v</polynomial>
    <polynomial>u^2*V - v*U^2</polynomial>
    <polynomial>u*v*U - v*U*V</polynomial>
    <polynomial>u*V*u - V*u*V</polynomial>
    <polynomial>u*V*U - v*u*V</polynomial>
    <polynomial>u*V^2 - v^2*U</polynomial>
    <polynomial>v*U*v - V*u*V</polynomial>
    <polynomial>U*v*u - V*U*v</polynomial>
    <polynomial>U*v^2 - V^2*u</polynomial>
    <polynomial>U*v*U - V*u*V</polynomial>
    <polynomial>U^2*v - V*u^2</polynomial>
    <polynomial>U*V*u - V*u*v</polynomial>
    <polynomial>u*U - 1</polynomial>
    <polynomial>v*V - 1</polynomial>
    <polynomial>U*u - 1</polynomial>
    <polynomial>V*v - 1</polynomial>
  </basis>
</FA_Q_dp_SOL>
"""
        print tempRes
        print expectedOutp
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for Magma output parse.")


    def test_FA_Q_dp_GAP_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the GAP output on a FA_Q_dp-instance, i.e. the
        computation of a Groebner basis over the free algebra.

        We test both functions here. The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by GAP.
        """
        from comp.FA_Q_dp.GAP.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "x1" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<FA_Q_dp_SOL>
  <basis>
    <polynomial>x1</polynomial>
  </basis>
</FA_Q_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        gapOutput = """
 Libs used:  gmp
 Loading the library and packages ...
 Components: trans 1.0, prim 2.1, small* 1.0, id* 1.0
 Packages:   AClib 1.2, Alnuth 3.0.0, AtlasRep 1.5.0, AutPGrp 1.6, 
             CRISP 1.3.8, Cryst 4.1.12, CrystCat 1.1.6, CTblLib 1.2.2, 
             FactInt 1.5.3, FGA 1.2.0, GAPDoc 1.5.1, IRREDSOL 1.2.4, 
             LAGUNA 3.6.4, Polenta 1.3.2, Polycyclic 2.11, RadiRoot 2.7, 
             ResClasses 3.3.2, Sophus 1.23, SpinSym 1.5, TomLib 1.2.4
 Try '?help' for help. See also  '?copyright' and  '?authors'
gap> true
gap> gap> gap> Rationals
gap> <algebra-with-one over Rationals, with 4 generators>
gap> [ (1)*x4, (1)*x3, (1)*x2, (1)*x1 ]
gap> (1)*x4
gap> (1)*x3
gap> (1)*x2
gap> (1)*x1
gap> [ 1, 1, 1, 1 ]
gap> > > > > > > > [ (1)*(x2*x1)^2+(-1)*x2*x1^2*x2+(-1)*x1*x2^2*x1+(1)*(x1*x2)^2, 
  (1)*x2*x1*x3*x1+(-1)*x2*x1^2*x3+(-1)*x1*x2*x3*x1+(1)*x1*x2*x1*x3, 
  (1)*x2*x1*x4*x1+(-1)*x2*x1^2*x4+(-1)*x1*x2*x4*x1+(1)*x1*x2*x1*x4, 
  (1)*x2*x1*x3*x2+(-1)*x2*x1*x2*x3+(-1)*x1*x2*x3*x2+(1)*x1*x2^2*x3, 
  (1)*x2*x1*x4*x2+(-1)*x2*x1*x2*x4+(-1)*x1*x2*x4*x2+(1)*x1*x2^2*x4, 
  (1)*x2*x1*x4*x3+(-1)*x2*x1*x3*x4+(-1)*x1*x2*x4*x3+(1)*x1*x2*x3*x4, 
  (1)*x3*x1*x2*x1+(-1)*x3*x1^2*x2+(-1)*x1*x3*x2*x1+(1)*x1*x3*x1*x2, 
  (1)*(x3*x1)^2+(-1)*x3*x1^2*x3+(-1)*x1*x3^2*x1+(1)*(x1*x3)^2, 
  (1)*x3*x1*x4*x1+(-1)*x3*x1^2*x4+(-1)*x1*x3*x4*x1+(1)*x1*x3*x1*x4, 
  (1)*x3*x1*x3*x2+(-1)*x3*x1*x2*x3+(-1)*x1*x3^2*x2+(1)*x1*x3*x2*x3, 
  (1)*x3*x1*x4*x2+(-1)*x3*x1*x2*x4+(-1)*x1*x3*x4*x2+(1)*x1*x3*x2*x4, 
  (1)*x3*x1*x4*x3+(-1)*x3*x1*x3*x4+(-1)*x1*x3*x4*x3+(1)*x1*x3^2*x4, 
  (1)*x4*x1*x2*x1+(-1)*x4*x1^2*x2+(-1)*x1*x4*x2*x1+(1)*x1*x4*x1*x2, 
  (1)*x4*x1*x3*x1+(-1)*x4*x1^2*x3+(-1)*x1*x4*x3*x1+(1)*x1*x4*x1*x3, 
  (1)*(x4*x1)^2+(-1)*x4*x1^2*x4+(-1)*x1*x4^2*x1+(1)*(x1*x4)^2, 
  (1)*x4*x1*x3*x2+(-1)*x4*x1*x2*x3+(-1)*x1*x4*x3*x2+(1)*x1*x4*x2*x3, 
  (1)*x4*x1*x4*x2+(-1)*x4*x1*x2*x4+(-1)*x1*x4^2*x2+(1)*x1*x4*x2*x4, 
  (1)*x4*x1*x4*x3+(-1)*x4*x1*x3*x4+(-1)*x1*x4^2*x3+(1)*x1*x4*x3*x4, 
  (1)*x3*x2^2*x1+(-1)*x3*x2*x1*x2+(-1)*x2*x3*x2*x1+(1)*x2*x3*x1*x2, 
  (1)*x3*x2*x3*x1+(-1)*x3*x2*x1*x3+(-1)*x2*x3^2*x1+(1)*x2*x3*x1*x3, 
  (1)*x3*x2*x4*x1+(-1)*x3*x2*x1*x4+(-1)*x2*x3*x4*x1+(1)*x2*x3*x1*x4, 
  (1)*(x3*x2)^2+(-1)*x3*x2^2*x3+(-1)*x2*x3^2*x2+(1)*(x2*x3)^2, 
  (1)*x3*x2*x4*x2+(-1)*x3*x2^2*x4+(-1)*x2*x3*x4*x2+(1)*x2*x3*x2*x4, 
  (1)*x3*x2*x4*x3+(-1)*x3*x2*x3*x4+(-1)*x2*x3*x4*x3+(1)*x2*x3^2*x4, 
  (1)*x4*x2^2*x1+(-1)*x4*x2*x1*x2+(-1)*x2*x4*x2*x1+(1)*x2*x4*x1*x2, 
  (1)*x4*x2*x3*x1+(-1)*x4*x2*x1*x3+(-1)*x2*x4*x3*x1+(1)*x2*x4*x1*x3, 
  (1)*x4*x2*x4*x1+(-1)*x4*x2*x1*x4+(-1)*x2*x4^2*x1+(1)*x2*x4*x1*x4, 
  (1)*x4*x2*x3*x2+(-1)*x4*x2^2*x3+(-1)*x2*x4*x3*x2+(1)*x2*x4*x2*x3, 
  (1)*(x4*x2)^2+(-1)*x4*x2^2*x4+(-1)*x2*x4^2*x2+(1)*(x2*x4)^2, 
  (1)*x4*x2*x4*x3+(-1)*x4*x2*x3*x4+(-1)*x2*x4^2*x3+(1)*x2*x4*x3*x4, 
  (1)*x4*x3*x2*x1+(-1)*x4*x3*x1*x2+(-1)*x3*x4*x2*x1+(1)*x3*x4*x1*x2, 
  (1)*x4*x3^2*x1+(-1)*x4*x3*x1*x3+(-1)*x3*x4*x3*x1+(1)*x3*x4*x1*x3, 
  (1)*x4*x3*x4*x1+(-1)*x4*x3*x1*x4+(-1)*x3*x4^2*x1+(1)*x3*x4*x1*x4, 
  (1)*x4*x3^2*x2+(-1)*x4*x3*x2*x3+(-1)*x3*x4*x3*x2+(1)*x3*x4*x2*x3, 
  (1)*x4*x3*x4*x2+(-1)*x4*x3*x2*x4+(-1)*x3*x4^2*x2+(1)*x3*x4*x2*x4, 
  (1)*(x4*x3)^2+(-1)*x4*x3^2*x4+(-1)*x3*x4^2*x3+(1)*(x3*x4)^2, 
  (1)*x2*x1^2*x2*x1+(-1)*x2*x1^3*x2+(-1)*(x1*x2)^2*x1+(1)*x1*x2*x1^2*x2, 
  (1)*x2*x1^2*x3*x1+(-1)*x2*x1^3*x3+(-1)*x1*x2*x1*x3*x1+(1)*x1*x2*x1^2*x3, 
  (1)*x2*x1^2*x4*x1+(-1)*x2*x1^3*x4+(-1)*x1*x2*x1*x4*x1+(1)*x1*x2*x1^2*x4, 
  (1)*x2*x1^2*x3*x2+(-1)*x2*x1^2*x2*x3+(-1)*x1*x2*x1*x3*x2+(1)*(x1*x2)^2*x3, 
  (1)*x2*x1^2*x4*x2+(-1)*x2*x1^2*x2*x4+(-1)*x1*x2*x1*x4*x2+(1)*(x1*x2)^2*x4, 
  (1)*x2*x1^2*x4*x3+(-1)*x2*x1^2*x3*x4+(-1)*x1*x2*x1*x4*x3+(1)*x1*x2*x1*x3*x4,
  (1)*x2*x1*x2^2*x1+(-1)*(x2*x1)^2*x2+(-1)*x1*x2^3*x1+(1)*x1*x2^2*x1*x2, 
  (1)*x2*x1*x2*x3*x1+(-1)*(x2*x1)^2*x3+(-1)*x1*x2^2*x3*x1+(1)*x1*x2^2*x1*x3, 
  (1)*x2*x1*x2*x4*x1+(-1)*(x2*x1)^2*x4+(-1)*x1*x2^2*x4*x1+(1)*x1*x2^2*x1*x4, 
  (1)*x2*x1*x2*x3*x2+(-1)*x2*x1*x2^2*x3+(-1)*x1*x2^2*x3*x2+(1)*x1*x2^3*x3, 
  (1)*x2*x1*x2*x4*x2+(-1)*x2*x1*x2^2*x4+(-1)*x1*x2^2*x4*x2+(1)*x1*x2^3*x4, 
  (1)*x2*x1*x2*x4*x3+(-1)*x2*x1*x2*x3*x4+(-1)*x1*x2^2*x4*x3+(1)*x1*x2^2*x3*x4,
  (1)*x2*x1*x3*x2*x1+(-1)*x2*x1*x3*x1*x2+(-1)*x1*x2*x3*x2*x1+(
    1)*x1*x2*x3*x1*x2, (1)*x2*x1*x3^2*x1+(-1)*x2*(x1*x3)^2+(
    -1)*x1*x2*x3^2*x1+(1)*x1*x2*x3*x1*x3, 
  (1)*x2*x1*x3*x4*x1+(-1)*x2*x1*x3*x1*x4+(-1)*x1*x2*x3*x4*x1+(
    1)*x1*x2*x3*x1*x4, (1)*x2*x1*x3^2*x2+(-1)*x2*x1*x3*x2*x3+(
    -1)*x1*x2*x3^2*x2+(1)*x1*(x2*x3)^2, 
  (1)*x2*x1*x3*x4*x2+(-1)*x2*x1*x3*x2*x4+(-1)*x1*x2*x3*x4*x2+(
    1)*x1*x2*x3*x2*x4, (1)*x2*x1*x3*x4*x3+(-1)*x2*x1*x3^2*x4+(
    -1)*x1*x2*x3*x4*x3+(1)*x1*x2*x3^2*x4, 
  (1)*x2*x1*x4*x2*x1+(-1)*x2*x1*x4*x1*x2+(-1)*x1*x2*x4*x2*x1+(
    1)*x1*x2*x4*x1*x2, (1)*x2*x1*x4*x3*x1+(-1)*x2*x1*x4*x1*x3+(
    -1)*x1*x2*x4*x3*x1+(1)*x1*x2*x4*x1*x3, 
  (1)*x2*x1*x4^2*x1+(-1)*x2*(x1*x4)^2+(-1)*x1*x2*x4^2*x1+(1)*x1*x2*x4*x1*x4, 
  (1)*x2*x1*x4*x3*x2+(-1)*x2*x1*x4*x2*x3+(-1)*x1*x2*x4*x3*x2+(
    1)*x1*x2*x4*x2*x3, (1)*x2*x1*x4^2*x2+(-1)*x2*x1*x4*x2*x4+(
    -1)*x1*x2*x4^2*x2+(1)*x1*(x2*x4)^2, 
  (1)*x2*x1*x4^2*x3+(-1)*x2*x1*x4*x3*x4+(-1)*x1*x2*x4^2*x3+(1)*x1*x2*x4*x3*x4,
  (1)*x3*x1^2*x2*x1+(-1)*x3*x1^3*x2+(-1)*x1*x3*x1*x2*x1+(1)*x1*x3*x1^2*x2, 
  (1)*x3*x1^2*x3*x1+(-1)*x3*x1^3*x3+(-1)*(x1*x3)^2*x1+(1)*x1*x3*x1^2*x3, 
  (1)*x3*x1^2*x4*x1+(-1)*x3*x1^3*x4+(-1)*x1*x3*x1*x4*x1+(1)*x1*x3*x1^2*x4, 
  (1)*x3*x1^2*x3*x2+(-1)*x3*x1^2*x2*x3+(-1)*(x1*x3)^2*x2+(1)*x1*x3*x1*x2*x3, 
  (1)*x3*x1^2*x4*x2+(-1)*x3*x1^2*x2*x4+(-1)*x1*x3*x1*x4*x2+(1)*x1*x3*x1*x2*x4,
  (1)*x3*x1^2*x4*x3+(-1)*x3*x1^2*x3*x4+(-1)*x1*x3*x1*x4*x3+(1)*(x1*x3)^2*x4, 
  (1)*x3*x1*x2^2*x1+(-1)*x3*(x1*x2)^2+(-1)*x1*x3*x2^2*x1+(1)*x1*x3*x2*x1*x2, 
  (1)*x3*x1*x2*x3*x1+(-1)*x3*x1*x2*x1*x3+(-1)*x1*x3*x2*x3*x1+(
    1)*x1*x3*x2*x1*x3, (1)*x3*x1*x2*x4*x1+(-1)*x3*x1*x2*x1*x4+(
    -1)*x1*x3*x2*x4*x1+(1)*x1*x3*x2*x1*x4, 
  (1)*x3*x1*x2*x3*x2+(-1)*x3*x1*x2^2*x3+(-1)*x1*(x3*x2)^2+(1)*x1*x3*x2^2*x3, 
  (1)*x3*x1*x2*x4*x2+(-1)*x3*x1*x2^2*x4+(-1)*x1*x3*x2*x4*x2+(1)*x1*x3*x2^2*x4,
  (1)*x3*x1*x2*x4*x3+(-1)*x3*x1*x2*x3*x4+(-1)*x1*x3*x2*x4*x3+(
    1)*x1*x3*x2*x3*x4, (1)*x3*x1*x3*x2*x1+(-1)*(x3*x1)^2*x2+(
    -1)*x1*x3^2*x2*x1+(1)*x1*x3^2*x1*x2, (1)*x3*x1*x3^2*x1+(-1)*(x3*x1)^2*x3+(
    -1)*x1*x3^3*x1+(1)*x1*x3^2*x1*x3, (1)*x3*x1*x3*x4*x1+(-1)*(x3*x1)^2*x4+(
    -1)*x1*x3^2*x4*x1+(1)*x1*x3^2*x1*x4, 
  (1)*x3*x1*x3^2*x2+(-1)*x3*x1*x3*x2*x3+(-1)*x1*x3^3*x2+(1)*x1*x3^2*x2*x3, 
  (1)*x3*x1*x3*x4*x2+(-1)*x3*x1*x3*x2*x4+(-1)*x1*x3^2*x4*x2+(1)*x1*x3^2*x2*x4,
  (1)*x3*x1*x3*x4*x3+(-1)*x3*x1*x3^2*x4+(-1)*x1*x3^2*x4*x3+(1)*x1*x3^3*x4, 
  (1)*x3*x1*x4*x2*x1+(-1)*x3*x1*x4*x1*x2+(-1)*x1*x3*x4*x2*x1+(
    1)*x1*x3*x4*x1*x2, (1)*x3*x1*x4*x3*x1+(-1)*x3*x1*x4*x1*x3+(
    -1)*x1*x3*x4*x3*x1+(1)*x1*x3*x4*x1*x3, 
  (1)*x3*x1*x4^2*x1+(-1)*x3*(x1*x4)^2+(-1)*x1*x3*x4^2*x1+(1)*x1*x3*x4*x1*x4, 
  (1)*x3*x1*x4*x3*x2+(-1)*x3*x1*x4*x2*x3+(-1)*x1*x3*x4*x3*x2+(
    1)*x1*x3*x4*x2*x3, (1)*x3*x1*x4^2*x2+(-1)*x3*x1*x4*x2*x4+(
    -1)*x1*x3*x4^2*x2+(1)*x1*x3*x4*x2*x4, 
  (1)*x3*x1*x4^2*x3+(-1)*x3*x1*x4*x3*x4+(-1)*x1*x3*x4^2*x3+(1)*x1*(x3*x4)^2, 
  (1)*x4*x1^2*x2*x1+(-1)*x4*x1^3*x2+(-1)*x1*x4*x1*x2*x1+(1)*x1*x4*x1^2*x2, 
  (1)*x4*x1^2*x3*x1+(-1)*x4*x1^3*x3+(-1)*x1*x4*x1*x3*x1+(1)*x1*x4*x1^2*x3, 
  (1)*x4*x1^2*x4*x1+(-1)*x4*x1^3*x4+(-1)*(x1*x4)^2*x1+(1)*x1*x4*x1^2*x4, 
  (1)*x4*x1^2*x3*x2+(-1)*x4*x1^2*x2*x3+(-1)*x1*x4*x1*x3*x2+(1)*x1*x4*x1*x2*x3,
  (1)*x4*x1^2*x4*x2+(-1)*x4*x1^2*x2*x4+(-1)*(x1*x4)^2*x2+(1)*x1*x4*x1*x2*x4, 
  (1)*x4*x1^2*x4*x3+(-1)*x4*x1^2*x3*x4+(-1)*(x1*x4)^2*x3+(1)*x1*x4*x1*x3*x4, 
  (1)*x4*x1*x2^2*x1+(-1)*x4*(x1*x2)^2+(-1)*x1*x4*x2^2*x1+(1)*x1*x4*x2*x1*x2, 
  (1)*x4*x1*x2*x3*x1+(-1)*x4*x1*x2*x1*x3+(-1)*x1*x4*x2*x3*x1+(
    1)*x1*x4*x2*x1*x3, (1)*x4*x1*x2*x4*x1+(-1)*x4*x1*x2*x1*x4+(
    -1)*x1*x4*x2*x4*x1+(1)*x1*x4*x2*x1*x4, 
  (1)*x4*x1*x2*x3*x2+(-1)*x4*x1*x2^2*x3+(-1)*x1*x4*x2*x3*x2+(1)*x1*x4*x2^2*x3,
  (1)*x4*x1*x2*x4*x2+(-1)*x4*x1*x2^2*x4+(-1)*x1*(x4*x2)^2+(1)*x1*x4*x2^2*x4, 
  (1)*x4*x1*x2*x4*x3+(-1)*x4*x1*x2*x3*x4+(-1)*x1*x4*x2*x4*x3+(
    1)*x1*x4*x2*x3*x4, (1)*x4*x1*x3*x2*x1+(-1)*x4*x1*x3*x1*x2+(
    -1)*x1*x4*x3*x2*x1+(1)*x1*x4*x3*x1*x2, 
  (1)*x4*x1*x3^2*x1+(-1)*x4*(x1*x3)^2+(-1)*x1*x4*x3^2*x1+(1)*x1*x4*x3*x1*x3, 
  (1)*x4*x1*x3*x4*x1+(-1)*x4*x1*x3*x1*x4+(-1)*x1*x4*x3*x4*x1+(
    1)*x1*x4*x3*x1*x4, (1)*x4*x1*x3^2*x2+(-1)*x4*x1*x3*x2*x3+(
    -1)*x1*x4*x3^2*x2+(1)*x1*x4*x3*x2*x3, 
  (1)*x4*x1*x3*x4*x2+(-1)*x4*x1*x3*x2*x4+(-1)*x1*x4*x3*x4*x2+(
    1)*x1*x4*x3*x2*x4, (1)*x4*x1*x3*x4*x3+(-1)*x4*x1*x3^2*x4+(
    -1)*x1*(x4*x3)^2+(1)*x1*x4*x3^2*x4, (1)*x4*x1*x4*x2*x1+(-1)*(x4*x1)^2*x2+(
    -1)*x1*x4^2*x2*x1+(1)*x1*x4^2*x1*x2, 
  (1)*x4*x1*x4*x3*x1+(-1)*(x4*x1)^2*x3+(-1)*x1*x4^2*x3*x1+(1)*x1*x4^2*x1*x3, 
  (1)*x4*x1*x4^2*x1+(-1)*(x4*x1)^2*x4+(-1)*x1*x4^3*x1+(1)*x1*x4^2*x1*x4, 
  (1)*x4*x1*x4*x3*x2+(-1)*x4*x1*x4*x2*x3+(-1)*x1*x4^2*x3*x2+(1)*x1*x4^2*x2*x3,
  (1)*x4*x1*x4^2*x2+(-1)*x4*x1*x4*x2*x4+(-1)*x1*x4^3*x2+(1)*x1*x4^2*x2*x4, 
  (1)*x4*x1*x4^2*x3+(-1)*x4*x1*x4*x3*x4+(-1)*x1*x4^3*x3+(1)*x1*x4^2*x3*x4, 
  (1)*x3*(x2*x1)^2+(-1)*x3*x2*x1^2*x2+(-1)*x2*x3*x1*x2*x1+(1)*x2*x3*x1^2*x2, 
  (1)*x3*x2*x1*x3*x1+(-1)*x3*x2*x1^2*x3+(-1)*x2*(x3*x1)^2+(1)*x2*x3*x1^2*x3, 
  (1)*x3*x2*x1*x4*x1+(-1)*x3*x2*x1^2*x4+(-1)*x2*x3*x1*x4*x1+(1)*x2*x3*x1^2*x4,
  (1)*x3*x2*x1*x3*x2+(-1)*x3*x2*x1*x2*x3+(-1)*x2*x3*x1*x3*x2+(
    1)*x2*x3*x1*x2*x3, (1)*x3*x2*x1*x4*x2+(-1)*x3*x2*x1*x2*x4+(
    -1)*x2*x3*x1*x4*x2+(1)*x2*x3*x1*x2*x4, 
  (1)*x3*x2*x1*x4*x3+(-1)*x3*x2*x1*x3*x4+(-1)*x2*x3*x1*x4*x3+(
    1)*x2*x3*x1*x3*x4, (1)*x3*x2^3*x1+(-1)*x3*x2^2*x1*x2+(-1)*x2*x3*x2^2*x1+(
    1)*x2*x3*x2*x1*x2, (1)*x3*x2^2*x3*x1+(-1)*x3*x2^2*x1*x3+(
    -1)*(x2*x3)^2*x1+(1)*x2*x3*x2*x1*x3, 
  (1)*x3*x2^2*x4*x1+(-1)*x3*x2^2*x1*x4+(-1)*x2*x3*x2*x4*x1+(1)*x2*x3*x2*x1*x4,
  (1)*x3*x2^2*x3*x2+(-1)*x3*x2^3*x3+(-1)*(x2*x3)^2*x2+(1)*x2*x3*x2^2*x3, 
  (1)*x3*x2^2*x4*x2+(-1)*x3*x2^3*x4+(-1)*x2*x3*x2*x4*x2+(1)*x2*x3*x2^2*x4, 
  (1)*x3*x2^2*x4*x3+(-1)*x3*x2^2*x3*x4+(-1)*x2*x3*x2*x4*x3+(1)*(x2*x3)^2*x4, 
  (1)*(x3*x2)^2*x1+(-1)*x3*x2*x3*x1*x2+(-1)*x2*x3^2*x2*x1+(1)*x2*x3^2*x1*x2, 
  (1)*x3*x2*x3^2*x1+(-1)*x3*x2*x3*x1*x3+(-1)*x2*x3^3*x1+(1)*x2*x3^2*x1*x3, 
  (1)*x3*x2*x3*x4*x1+(-1)*x3*x2*x3*x1*x4+(-1)*x2*x3^2*x4*x1+(1)*x2*x3^2*x1*x4,
  (1)*x3*x2*x3^2*x2+(-1)*(x3*x2)^2*x3+(-1)*x2*x3^3*x2+(1)*x2*x3^2*x2*x3, 
  (1)*x3*x2*x3*x4*x2+(-1)*(x3*x2)^2*x4+(-1)*x2*x3^2*x4*x2+(1)*x2*x3^2*x2*x4, 
  (1)*x3*x2*x3*x4*x3+(-1)*x3*x2*x3^2*x4+(-1)*x2*x3^2*x4*x3+(1)*x2*x3^3*x4, 
  (1)*x3*x2*x4*x2*x1+(-1)*x3*x2*x4*x1*x2+(-1)*x2*x3*x4*x2*x1+(
    1)*x2*x3*x4*x1*x2, (1)*x3*x2*x4*x3*x1+(-1)*x3*x2*x4*x1*x3+(
    -1)*x2*x3*x4*x3*x1+(1)*x2*x3*x4*x1*x3, 
  (1)*x3*x2*x4^2*x1+(-1)*x3*x2*x4*x1*x4+(-1)*x2*x3*x4^2*x1+(1)*x2*x3*x4*x1*x4,
  (1)*x3*x2*x4*x3*x2+(-1)*x3*x2*x4*x2*x3+(-1)*x2*x3*x4*x3*x2+(
    1)*x2*x3*x4*x2*x3, (1)*x3*x2*x4^2*x2+(-1)*x3*(x2*x4)^2+(
    -1)*x2*x3*x4^2*x2+(1)*x2*x3*x4*x2*x4, 
  (1)*x3*x2*x4^2*x3+(-1)*x3*x2*x4*x3*x4+(-1)*x2*x3*x4^2*x3+(1)*x2*(x3*x4)^2, 
  (1)*x4*(x2*x1)^2+(-1)*x4*x2*x1^2*x2+(-1)*x2*x4*x1*x2*x1+(1)*x2*x4*x1^2*x2, 
  (1)*x4*x2*x1*x3*x1+(-1)*x4*x2*x1^2*x3+(-1)*x2*x4*x1*x3*x1+(1)*x2*x4*x1^2*x3,
  (1)*x4*x2*x1*x4*x1+(-1)*x4*x2*x1^2*x4+(-1)*x2*(x4*x1)^2+(1)*x2*x4*x1^2*x4, 
  (1)*x4*x2*x1*x3*x2+(-1)*x4*x2*x1*x2*x3+(-1)*x2*x4*x1*x3*x2+(
    1)*x2*x4*x1*x2*x3, (1)*x4*x2*x1*x4*x2+(-1)*x4*x2*x1*x2*x4+(
    -1)*x2*x4*x1*x4*x2+(1)*x2*x4*x1*x2*x4, 
  (1)*x4*x2*x1*x4*x3+(-1)*x4*x2*x1*x3*x4+(-1)*x2*x4*x1*x4*x3+(
    1)*x2*x4*x1*x3*x4, (1)*x4*x2^3*x1+(-1)*x4*x2^2*x1*x2+(-1)*x2*x4*x2^2*x1+(
    1)*x2*x4*x2*x1*x2, (1)*x4*x2^2*x3*x1+(-1)*x4*x2^2*x1*x3+(
    -1)*x2*x4*x2*x3*x1+(1)*x2*x4*x2*x1*x3, 
  (1)*x4*x2^2*x4*x1+(-1)*x4*x2^2*x1*x4+(-1)*(x2*x4)^2*x1+(1)*x2*x4*x2*x1*x4, 
  (1)*x4*x2^2*x3*x2+(-1)*x4*x2^3*x3+(-1)*x2*x4*x2*x3*x2+(1)*x2*x4*x2^2*x3, 
  (1)*x4*x2^2*x4*x2+(-1)*x4*x2^3*x4+(-1)*(x2*x4)^2*x2+(1)*x2*x4*x2^2*x4, 
  (1)*x4*x2^2*x4*x3+(-1)*x4*x2^2*x3*x4+(-1)*(x2*x4)^2*x3+(1)*x2*x4*x2*x3*x4, 
  (1)*x4*x2*x3*x2*x1+(-1)*x4*x2*x3*x1*x2+(-1)*x2*x4*x3*x2*x1+(
    1)*x2*x4*x3*x1*x2, (1)*x4*x2*x3^2*x1+(-1)*x4*x2*x3*x1*x3+(
    -1)*x2*x4*x3^2*x1+(1)*x2*x4*x3*x1*x3, 
  (1)*x4*x2*x3*x4*x1+(-1)*x4*x2*x3*x1*x4+(-1)*x2*x4*x3*x4*x1+(
    1)*x2*x4*x3*x1*x4, (1)*x4*x2*x3^2*x2+(-1)*x4*(x2*x3)^2+(
    -1)*x2*x4*x3^2*x2+(1)*x2*x4*x3*x2*x3, 
  (1)*x4*x2*x3*x4*x2+(-1)*x4*x2*x3*x2*x4+(-1)*x2*x4*x3*x4*x2+(
    1)*x2*x4*x3*x2*x4, (1)*x4*x2*x3*x4*x3+(-1)*x4*x2*x3^2*x4+(
    -1)*x2*(x4*x3)^2+(1)*x2*x4*x3^2*x4, (1)*(x4*x2)^2*x1+(-1)*x4*x2*x4*x1*x2+(
    -1)*x2*x4^2*x2*x1+(1)*x2*x4^2*x1*x2, 
  (1)*x4*x2*x4*x3*x1+(-1)*x4*x2*x4*x1*x3+(-1)*x2*x4^2*x3*x1+(1)*x2*x4^2*x1*x3,
  (1)*x4*x2*x4^2*x1+(-1)*x4*x2*x4*x1*x4+(-1)*x2*x4^3*x1+(1)*x2*x4^2*x1*x4, 
  (1)*x4*x2*x4*x3*x2+(-1)*(x4*x2)^2*x3+(-1)*x2*x4^2*x3*x2+(1)*x2*x4^2*x2*x3, 
  (1)*x4*x2*x4^2*x2+(-1)*(x4*x2)^2*x4+(-1)*x2*x4^3*x2+(1)*x2*x4^2*x2*x4, 
  (1)*x4*x2*x4^2*x3+(-1)*x4*x2*x4*x3*x4+(-1)*x2*x4^3*x3+(1)*x2*x4^2*x3*x4, 
  (1)*x4*x3*x1*x2*x1+(-1)*x4*x3*x1^2*x2+(-1)*x3*x4*x1*x2*x1+(1)*x3*x4*x1^2*x2,
  (1)*x4*(x3*x1)^2+(-1)*x4*x3*x1^2*x3+(-1)*x3*x4*x1*x3*x1+(1)*x3*x4*x1^2*x3, 
  (1)*x4*x3*x1*x4*x1+(-1)*x4*x3*x1^2*x4+(-1)*x3*(x4*x1)^2+(1)*x3*x4*x1^2*x4, 
  (1)*x4*x3*x1*x3*x2+(-1)*x4*x3*x1*x2*x3+(-1)*x3*x4*x1*x3*x2+(
    1)*x3*x4*x1*x2*x3, (1)*x4*x3*x1*x4*x2+(-1)*x4*x3*x1*x2*x4+(
    -1)*x3*x4*x1*x4*x2+(1)*x3*x4*x1*x2*x4, 
  (1)*x4*x3*x1*x4*x3+(-1)*x4*x3*x1*x3*x4+(-1)*x3*x4*x1*x4*x3+(
    1)*x3*x4*x1*x3*x4, (1)*x4*x3*x2^2*x1+(-1)*x4*x3*x2*x1*x2+(
    -1)*x3*x4*x2^2*x1+(1)*x3*x4*x2*x1*x2, 
  (1)*x4*x3*x2*x3*x1+(-1)*x4*x3*x2*x1*x3+(-1)*x3*x4*x2*x3*x1+(
    1)*x3*x4*x2*x1*x3, (1)*x4*x3*x2*x4*x1+(-1)*x4*x3*x2*x1*x4+(
    -1)*x3*x4*x2*x4*x1+(1)*x3*x4*x2*x1*x4, 
  (1)*x4*(x3*x2)^2+(-1)*x4*x3*x2^2*x3+(-1)*x3*x4*x2*x3*x2+(1)*x3*x4*x2^2*x3, 
  (1)*x4*x3*x2*x4*x2+(-1)*x4*x3*x2^2*x4+(-1)*x3*(x4*x2)^2+(1)*x3*x4*x2^2*x4, 
  (1)*x4*x3*x2*x4*x3+(-1)*x4*x3*x2*x3*x4+(-1)*x3*x4*x2*x4*x3+(
    1)*x3*x4*x2*x3*x4, (1)*x4*x3^2*x2*x1+(-1)*x4*x3^2*x1*x2+(
    -1)*x3*x4*x3*x2*x1+(1)*x3*x4*x3*x1*x2, (1)*x4*x3^3*x1+(-1)*x4*x3^2*x1*x3+(
    -1)*x3*x4*x3^2*x1+(1)*x3*x4*x3*x1*x3, 
  (1)*x4*x3^2*x4*x1+(-1)*x4*x3^2*x1*x4+(-1)*(x3*x4)^2*x1+(1)*x3*x4*x3*x1*x4, 
  (1)*x4*x3^3*x2+(-1)*x4*x3^2*x2*x3+(-1)*x3*x4*x3^2*x2+(1)*x3*x4*x3*x2*x3, 
  (1)*x4*x3^2*x4*x2+(-1)*x4*x3^2*x2*x4+(-1)*(x3*x4)^2*x2+(1)*x3*x4*x3*x2*x4, 
  (1)*x4*x3^2*x4*x3+(-1)*x4*x3^3*x4+(-1)*(x3*x4)^2*x3+(1)*x3*x4*x3^2*x4, 
  (1)*x4*x3*x4*x2*x1+(-1)*x4*x3*x4*x1*x2+(-1)*x3*x4^2*x2*x1+(1)*x3*x4^2*x1*x2,
  (1)*(x4*x3)^2*x1+(-1)*x4*x3*x4*x1*x3+(-1)*x3*x4^2*x3*x1+(1)*x3*x4^2*x1*x3, 
  (1)*x4*x3*x4^2*x1+(-1)*x4*x3*x4*x1*x4+(-1)*x3*x4^3*x1+(1)*x3*x4^2*x1*x4, 
  (1)*(x4*x3)^2*x2+(-1)*x4*x3*x4*x2*x3+(-1)*x3*x4^2*x3*x2+(1)*x3*x4^2*x2*x3, 
  (1)*x4*x3*x4^2*x2+(-1)*x4*x3*x4*x2*x4+(-1)*x3*x4^3*x2+(1)*x3*x4^2*x2*x4, 
  (1)*x4*x3*x4^2*x3+(-1)*(x4*x3)^2*x4+(-1)*x3*x4^3*x3+(1)*x3*x4^2*x3*x4, 
  (1)*x2*x1^3*x2*x1+(-1)*x2*x1^4*x2+(-1)*(x1*x2*x1)^2+(1)*x1*x2*x1^3*x2, 
  (1)*x2*x1^3*x3*x1+(-1)*x2*x1^4*x3+(-1)*x1*x2*x1^2*x3*x1+(1)*x1*x2*x1^3*x3, 
  (1)*x2*x1^3*x4*x1+(-1)*x2*x1^4*x4+(-1)*x1*x2*x1^2*x4*x1+(1)*x1*x2*x1^3*x4, 
  (1)*x2*x1^3*x3*x2+(-1)*x2*x1^3*x2*x3+(-1)*x1*x2*x1^2*x3*x2+(
    1)*x1*x2*x1^2*x2*x3, (1)*x2*x1^3*x4*x2+(-1)*x2*x1^3*x2*x4+(
    -1)*x1*x2*x1^2*x4*x2+(1)*x1*x2*x1^2*x2*x4, 
  (1)*x2*x1^3*x4*x3+(-1)*x2*x1^3*x3*x4+(-1)*x1*x2*x1^2*x4*x3+(
    1)*x1*x2*x1^2*x3*x4, (1)*x2*x1^2*x2^2*x1+(-1)*x2*x1*(x1*x2)^2+(
    -1)*(x1*x2)^2*x2*x1+(1)*(x1*x2)^3, 
  (1)*x2*x1^2*x2*x3*x1+(-1)*x2*x1^2*x2*x1*x3+(-1)*(x1*x2)^2*x3*x1+(
    1)*(x1*x2)^2*x1*x3, (1)*x2*x1^2*x2*x4*x1+(-1)*x2*x1^2*x2*x1*x4+(
    -1)*(x1*x2)^2*x4*x1+(1)*(x1*x2)^2*x1*x4, 
  (1)*x2*x1^2*x2*x3*x2+(-1)*x2*x1^2*x2^2*x3+(-1)*(x1*x2)^2*x3*x2+(
    1)*(x1*x2)^2*x2*x3, (1)*x2*x1^2*x2*x4*x2+(-1)*x2*x1^2*x2^2*x4+(
    -1)*(x1*x2)^2*x4*x2+(1)*(x1*x2)^2*x2*x4, 
  (1)*x2*x1^2*x2*x4*x3+(-1)*x2*x1^2*x2*x3*x4+(-1)*(x1*x2)^2*x4*x3+(
    1)*(x1*x2)^2*x3*x4, (1)*x2*x1^2*x3*x2*x1+(-1)*x2*x1^2*x3*x1*x2+(
    -1)*x1*x2*x1*x3*x2*x1+(1)*x1*x2*x1*x3*x1*x2, 
  (1)*x2*x1^2*x3^2*x1+(-1)*x2*x1*(x1*x3)^2+(-1)*x1*x2*x1*x3^2*x1+(
    1)*x1*x2*(x1*x3)^2, (1)*x2*x1^2*x3*x4*x1+(-1)*x2*x1^2*x3*x1*x4+(
    -1)*x1*x2*x1*x3*x4*x1+(1)*x1*x2*x1*x3*x1*x4, 
  (1)*x2*x1^2*x3^2*x2+(-1)*x2*x1^2*x3*x2*x3+(-1)*x1*x2*x1*x3^2*x2+(
    1)*x1*x2*x1*x3*x2*x3, (1)*x2*x1^2*x3*x4*x2+(-1)*x2*x1^2*x3*x2*x4+(
    -1)*x1*x2*x1*x3*x4*x2+(1)*x1*x2*x1*x3*x2*x4, 
  (1)*x2*x1^2*x3*x4*x3+(-1)*x2*x1^2*x3^2*x4+(-1)*x1*x2*x1*x3*x4*x3+(
    1)*x1*x2*x1*x3^2*x4, (1)*x2*x1^2*x4*x2*x1+(-1)*x2*x1^2*x4*x1*x2+(
    -1)*x1*x2*x1*x4*x2*x1+(1)*x1*x2*x1*x4*x1*x2, 
  (1)*x2*x1^2*x4*x3*x1+(-1)*x2*x1^2*x4*x1*x3+(-1)*x1*x2*x1*x4*x3*x1+(
    1)*x1*x2*x1*x4*x1*x3, (1)*x2*x1^2*x4^2*x1+(-1)*x2*x1*(x1*x4)^2+(
    -1)*x1*x2*x1*x4^2*x1+(1)*x1*x2*(x1*x4)^2, 
  (1)*x2*x1^2*x4*x3*x2+(-1)*x2*x1^2*x4*x2*x3+(-1)*x1*x2*x1*x4*x3*x2+(
    1)*x1*x2*x1*x4*x2*x3, (1)*x2*x1^2*x4^2*x2+(-1)*x2*x1^2*x4*x2*x4+(
    -1)*x1*x2*x1*x4^2*x2+(1)*x1*x2*x1*x4*x2*x4, 
  (1)*x2*x1^2*x4^2*x3+(-1)*x2*x1^2*x4*x3*x4+(-1)*x1*x2*x1*x4^2*x3+(
    1)*x1*x2*x1*x4*x3*x4, (1)*(x2*x1)^3+(-1)*(x2*x1)^2*x1*x2+(
    -1)*x1*x2*(x2*x1)^2+(1)*x1*x2^2*x1^2*x2, 
  (1)*(x2*x1)^2*x3*x1+(-1)*(x2*x1)^2*x1*x3+(-1)*x1*x2^2*x1*x3*x1+(
    1)*x1*x2^2*x1^2*x3, (1)*(x2*x1)^2*x4*x1+(-1)*(x2*x1)^2*x1*x4+(
    -1)*x1*x2^2*x1*x4*x1+(1)*x1*x2^2*x1^2*x4, 
  (1)*(x2*x1)^2*x3*x2+(-1)*(x2*x1)^2*x2*x3+(-1)*x1*x2^2*x1*x3*x2+(
    1)*x1*x2^2*x1*x2*x3, (1)*(x2*x1)^2*x4*x2+(-1)*(x2*x1)^2*x2*x4+(
    -1)*x1*x2^2*x1*x4*x2+(1)*x1*x2^2*x1*x2*x4, 
  (1)*(x2*x1)^2*x4*x3+(-1)*(x2*x1)^2*x3*x4+(-1)*x1*x2^2*x1*x4*x3+(
    1)*x1*x2^2*x1*x3*x4, (1)*x2*x1*x2^3*x1+(-1)*(x2*x1*x2)^2+(-1)*x1*x2^4*x1+(
    1)*x1*x2^3*x1*x2, (1)*x2*x1*x2^2*x3*x1+(-1)*x2*x1*x2^2*x1*x3+(
    -1)*x1*x2^3*x3*x1+(1)*x1*x2^3*x1*x3, 
  (1)*x2*x1*x2^2*x4*x1+(-1)*x2*x1*x2^2*x1*x4+(-1)*x1*x2^3*x4*x1+(
    1)*x1*x2^3*x1*x4, (1)*x2*x1*x2^2*x3*x2+(-1)*x2*x1*x2^3*x3+(
    -1)*x1*x2^3*x3*x2+(1)*x1*x2^4*x3, 
  (1)*x2*x1*x2^2*x4*x2+(-1)*x2*x1*x2^3*x4+(-1)*x1*x2^3*x4*x2+(1)*x1*x2^4*x4, 
  (1)*x2*x1*x2^2*x4*x3+(-1)*x2*x1*x2^2*x3*x4+(-1)*x1*x2^3*x4*x3+(
    1)*x1*x2^3*x3*x4, (1)*x2*x1*x2*x3*x2*x1+(-1)*x2*x1*x2*x3*x1*x2+(
    -1)*x1*x2^2*x3*x2*x1+(1)*x1*x2^2*x3*x1*x2, 
  (1)*x2*x1*x2*x3^2*x1+(-1)*x2*x1*x2*x3*x1*x3+(-1)*x1*x2^2*x3^2*x1+(
    1)*x1*x2^2*x3*x1*x3, (1)*x2*x1*x2*x3*x4*x1+(-1)*x2*x1*x2*x3*x1*x4+(
    -1)*x1*x2^2*x3*x4*x1+(1)*x1*x2^2*x3*x1*x4, 
  (1)*x2*x1*x2*x3^2*x2+(-1)*x2*x1*(x2*x3)^2+(-1)*x1*x2^2*x3^2*x2+(
    1)*x1*x2*(x2*x3)^2, (1)*x2*x1*x2*x3*x4*x2+(-1)*x2*x1*x2*x3*x2*x4+(
    -1)*x1*x2^2*x3*x4*x2+(1)*x1*x2^2*x3*x2*x4, 
  (1)*x2*x1*x2*x3*x4*x3+(-1)*x2*x1*x2*x3^2*x4+(-1)*x1*x2^2*x3*x4*x3+(
    1)*x1*x2^2*x3^2*x4, (1)*x2*x1*x2*x4*x2*x1+(-1)*x2*x1*x2*x4*x1*x2+(
    -1)*x1*x2^2*x4*x2*x1+(1)*x1*x2^2*x4*x1*x2, 
  (1)*x2*x1*x2*x4*x3*x1+(-1)*x2*x1*x2*x4*x1*x3+(-1)*x1*x2^2*x4*x3*x1+(
    1)*x1*x2^2*x4*x1*x3, (1)*x2*x1*x2*x4^2*x1+(-1)*x2*x1*x2*x4*x1*x4+(
    -1)*x1*x2^2*x4^2*x1+(1)*x1*x2^2*x4*x1*x4, 
  (1)*x2*x1*x2*x4*x3*x2+(-1)*x2*x1*x2*x4*x2*x3+(-1)*x1*x2^2*x4*x3*x2+(
    1)*x1*x2^2*x4*x2*x3, (1)*x2*x1*x2*x4^2*x2+(-1)*x2*x1*(x2*x4)^2+(
    -1)*x1*x2^2*x4^2*x2+(1)*x1*x2*(x2*x4)^2, 
  (1)*x2*x1*x2*x4^2*x3+(-1)*x2*x1*x2*x4*x3*x4+(-1)*x1*x2^2*x4^2*x3+(
    1)*x1*x2^2*x4*x3*x4, (1)*x2*x1*x3*x1*x2*x1+(-1)*x2*x1*x3*x1^2*x2+(
    -1)*x1*x2*x3*x1*x2*x1+(1)*x1*x2*x3*x1^2*x2, 
  (1)*x2*(x1*x3)^2*x1+(-1)*x2*x1*x3*x1^2*x3+(-1)*x1*x2*(x3*x1)^2+(
    1)*x1*x2*x3*x1^2*x3, (1)*x2*x1*x3*x1*x4*x1+(-1)*x2*x1*x3*x1^2*x4+(
    -1)*x1*x2*x3*x1*x4*x1+(1)*x1*x2*x3*x1^2*x4, 
  (1)*x2*(x1*x3)^2*x2+(-1)*x2*x1*x3*x1*x2*x3+(-1)*x1*x2*x3*x1*x3*x2+(
    1)*(x1*x2*x3)^2, (1)*x2*x1*x3*x1*x4*x2+(-1)*x2*x1*x3*x1*x2*x4+(
    -1)*x1*x2*x3*x1*x4*x2+(1)*x1*x2*x3*x1*x2*x4, 
  (1)*x2*x1*x3*x1*x4*x3+(-1)*x2*(x1*x3)^2*x4+(-1)*x1*x2*x3*x1*x4*x3+(
    1)*x1*x2*x3*x1*x3*x4, (1)*x2*x1*x3*x2^2*x1+(-1)*x2*x1*x3*x2*x1*x2+(
    -1)*x1*x2*x3*x2^2*x1+(1)*x1*x2*x3*x2*x1*x2, 
  (1)*x2*x1*x3*x2*x3*x1+(-1)*(x2*x1*x3)^2+(-1)*x1*(x2*x3)^2*x1+(
    1)*x1*x2*x3*x2*x1*x3, (1)*x2*x1*x3*x2*x4*x1+(-1)*x2*x1*x3*x2*x1*x4+(
    -1)*x1*x2*x3*x2*x4*x1+(1)*x1*x2*x3*x2*x1*x4, 
  (1)*x2*x1*(x3*x2)^2+(-1)*x2*x1*x3*x2^2*x3+(-1)*x1*(x2*x3)^2*x2+(
    1)*x1*x2*x3*x2^2*x3, (1)*x2*x1*x3*x2*x4*x2+(-1)*x2*x1*x3*x2^2*x4+(
    -1)*x1*x2*x3*x2*x4*x2+(1)*x1*x2*x3*x2^2*x4, 
  (1)*x2*x1*x3*x2*x4*x3+(-1)*x2*x1*x3*x2*x3*x4+(-1)*x1*x2*x3*x2*x4*x3+(
    1)*x1*(x2*x3)^2*x4, (1)*x2*x1*x3^2*x2*x1+(-1)*x2*x1*x3^2*x1*x2+(
    -1)*x1*x2*x3^2*x2*x1+(1)*x1*x2*x3^2*x1*x2, 
  (1)*x2*x1*x3^3*x1+(-1)*x2*x1*x3^2*x1*x3+(-1)*x1*x2*x3^3*x1+(
    1)*x1*x2*x3^2*x1*x3, (1)*x2*x1*x3^2*x4*x1+(-1)*x2*x1*x3^2*x1*x4+(
    -1)*x1*x2*x3^2*x4*x1+(1)*x1*x2*x3^2*x1*x4, 
  (1)*x2*x1*x3^3*x2+(-1)*x2*x1*x3^2*x2*x3+(-1)*x1*x2*x3^3*x2+(
    1)*x1*x2*x3^2*x2*x3, (1)*x2*x1*x3^2*x4*x2+(-1)*x2*x1*x3^2*x2*x4+(
    -1)*x1*x2*x3^2*x4*x2+(1)*x1*x2*x3^2*x2*x4, 
  (1)*x2*x1*x3^2*x4*x3+(-1)*x2*x1*x3^3*x4+(-1)*x1*x2*x3^2*x4*x3+(
    1)*x1*x2*x3^3*x4, (1)*x2*x1*x3*x4*x2*x1+(-1)*x2*x1*x3*x4*x1*x2+(
    -1)*x1*x2*x3*x4*x2*x1+(1)*x1*x2*x3*x4*x1*x2, 
  (1)*x2*x1*x3*x4*x3*x1+(-1)*x2*x1*x3*x4*x1*x3+(-1)*x1*x2*x3*x4*x3*x1+(
    1)*x1*x2*x3*x4*x1*x3, (1)*x2*x1*x3*x4^2*x1+(-1)*x2*x1*x3*x4*x1*x4+(
    -1)*x1*x2*x3*x4^2*x1+(1)*x1*x2*x3*x4*x1*x4, 
  (1)*x2*x1*x3*x4*x3*x2+(-1)*x2*x1*x3*x4*x2*x3+(-1)*x1*x2*x3*x4*x3*x2+(
    1)*x1*x2*x3*x4*x2*x3, (1)*x2*x1*x3*x4^2*x2+(-1)*x2*x1*x3*x4*x2*x4+(
    -1)*x1*x2*x3*x4^2*x2+(1)*x1*x2*x3*x4*x2*x4, 
  (1)*x2*x1*x3*x4^2*x3+(-1)*x2*x1*(x3*x4)^2+(-1)*x1*x2*x3*x4^2*x3+(
    1)*x1*x2*(x3*x4)^2, (1)*x2*x1*x4*x1*x2*x1+(-1)*x2*x1*x4*x1^2*x2+(
    -1)*x1*x2*x4*x1*x2*x1+(1)*x1*x2*x4*x1^2*x2, 
  (1)*x2*x1*x4*x1*x3*x1+(-1)*x2*x1*x4*x1^2*x3+(-1)*x1*x2*x4*x1*x3*x1+(
    1)*x1*x2*x4*x1^2*x3, (1)*x2*(x1*x4)^2*x1+(-1)*x2*x1*x4*x1^2*x4+(
    -1)*x1*x2*(x4*x1)^2+(1)*x1*x2*x4*x1^2*x4, 
  (1)*x2*x1*x4*x1*x3*x2+(-1)*x2*x1*x4*x1*x2*x3+(-1)*x1*x2*x4*x1*x3*x2+(
    1)*x1*x2*x4*x1*x2*x3, (1)*x2*(x1*x4)^2*x2+(-1)*x2*x1*x4*x1*x2*x4+(
    -1)*x1*x2*x4*x1*x4*x2+(1)*(x1*x2*x4)^2, 
  (1)*x2*(x1*x4)^2*x3+(-1)*x2*x1*x4*x1*x3*x4+(-1)*x1*x2*x4*x1*x4*x3+(
    1)*x1*x2*x4*x1*x3*x4, (1)*x2*x1*x4*x2^2*x1+(-1)*x2*x1*x4*x2*x1*x2+(
    -1)*x1*x2*x4*x2^2*x1+(1)*x1*x2*x4*x2*x1*x2, 
  (1)*x2*x1*x4*x2*x3*x1+(-1)*x2*x1*x4*x2*x1*x3+(-1)*x1*x2*x4*x2*x3*x1+(
    1)*x1*x2*x4*x2*x1*x3, (1)*x2*x1*x4*x2*x4*x1+(-1)*(x2*x1*x4)^2+(
    -1)*x1*(x2*x4)^2*x1+(1)*x1*x2*x4*x2*x1*x4, 
  (1)*x2*x1*x4*x2*x3*x2+(-1)*x2*x1*x4*x2^2*x3+(-1)*x1*x2*x4*x2*x3*x2+(
    1)*x1*x2*x4*x2^2*x3, (1)*x2*x1*(x4*x2)^2+(-1)*x2*x1*x4*x2^2*x4+(
    -1)*x1*(x2*x4)^2*x2+(1)*x1*x2*x4*x2^2*x4, 
  (1)*x2*x1*x4*x2*x4*x3+(-1)*x2*x1*x4*x2*x3*x4+(-1)*x1*(x2*x4)^2*x3+(
    1)*x1*x2*x4*x2*x3*x4, (1)*x2*x1*x4*x3*x2*x1+(-1)*x2*x1*x4*x3*x1*x2+(
    -1)*x1*x2*x4*x3*x2*x1+(1)*x1*x2*x4*x3*x1*x2, 
  (1)*x2*x1*x4*x3^2*x1+(-1)*x2*x1*x4*x3*x1*x3+(-1)*x1*x2*x4*x3^2*x1+(
    1)*x1*x2*x4*x3*x1*x3, (1)*x2*x1*x4*x3*x4*x1+(-1)*x2*x1*x4*x3*x1*x4+(
    -1)*x1*x2*x4*x3*x4*x1+(1)*x1*x2*x4*x3*x1*x4, 
  (1)*x2*x1*x4*x3^2*x2+(-1)*x2*x1*x4*x3*x2*x3+(-1)*x1*x2*x4*x3^2*x2+(
    1)*x1*x2*x4*x3*x2*x3, (1)*x2*x1*x4*x3*x4*x2+(-1)*x2*x1*x4*x3*x2*x4+(
    -1)*x1*x2*x4*x3*x4*x2+(1)*x1*x2*x4*x3*x2*x4, 
  (1)*x2*x1*(x4*x3)^2+(-1)*x2*x1*x4*x3^2*x4+(-1)*x1*x2*(x4*x3)^2+(
    1)*x1*x2*x4*x3^2*x4, (1)*x2*x1*x4^2*x2*x1+(-1)*x2*x1*x4^2*x1*x2+(
    -1)*x1*x2*x4^2*x2*x1+(1)*x1*x2*x4^2*x1*x2, 
  (1)*x2*x1*x4^2*x3*x1+(-1)*x2*x1*x4^2*x1*x3+(-1)*x1*x2*x4^2*x3*x1+(
    1)*x1*x2*x4^2*x1*x3, (1)*x2*x1*x4^3*x1+(-1)*x2*x1*x4^2*x1*x4+(
    -1)*x1*x2*x4^3*x1+(1)*x1*x2*x4^2*x1*x4, 
  (1)*x2*x1*x4^2*x3*x2+(-1)*x2*x1*x4^2*x2*x3+(-1)*x1*x2*x4^2*x3*x2+(
    1)*x1*x2*x4^2*x2*x3, (1)*x2*x1*x4^3*x2+(-1)*x2*x1*x4^2*x2*x4+(
    -1)*x1*x2*x4^3*x2+(1)*x1*x2*x4^2*x2*x4, 
  (1)*x2*x1*x4^3*x3+(-1)*x2*x1*x4^2*x3*x4+(-1)*x1*x2*x4^3*x3+(
    1)*x1*x2*x4^2*x3*x4, (1)*x3*x1^3*x2*x1+(-1)*x3*x1^4*x2+(
    -1)*x1*x3*x1^2*x2*x1+(1)*x1*x3*x1^3*x2, 
  (1)*x3*x1^3*x3*x1+(-1)*x3*x1^4*x3+(-1)*(x1*x3*x1)^2+(1)*x1*x3*x1^3*x3, 
  (1)*x3*x1^3*x4*x1+(-1)*x3*x1^4*x4+(-1)*x1*x3*x1^2*x4*x1+(1)*x1*x3*x1^3*x4, 
  (1)*x3*x1^3*x3*x2+(-1)*x3*x1^3*x2*x3+(-1)*x1*x3*x1^2*x3*x2+(
    1)*x1*x3*x1^2*x2*x3, (1)*x3*x1^3*x4*x2+(-1)*x3*x1^3*x2*x4+(
    -1)*x1*x3*x1^2*x4*x2+(1)*x1*x3*x1^2*x2*x4, 
  (1)*x3*x1^3*x4*x3+(-1)*x3*x1^3*x3*x4+(-1)*x1*x3*x1^2*x4*x3+(
    1)*x1*x3*x1^2*x3*x4, (1)*x3*x1^2*x2^2*x1+(-1)*x3*x1*(x1*x2)^2+(
    -1)*x1*x3*x1*x2^2*x1+(1)*x1*x3*(x1*x2)^2, 
  (1)*x3*x1^2*x2*x3*x1+(-1)*x3*x1^2*x2*x1*x3+(-1)*x1*x3*x1*x2*x3*x1+(
    1)*x1*x3*x1*x2*x1*x3, (1)*x3*x1^2*x2*x4*x1+(-1)*x3*x1^2*x2*x1*x4+(
    -1)*x1*x3*x1*x2*x4*x1+(1)*x1*x3*x1*x2*x1*x4, 
  (1)*x3*x1^2*x2*x3*x2+(-1)*x3*x1^2*x2^2*x3+(-1)*x1*x3*x1*x2*x3*x2+(
    1)*x1*x3*x1*x2^2*x3, (1)*x3*x1^2*x2*x4*x2+(-1)*x3*x1^2*x2^2*x4+(
    -1)*x1*x3*x1*x2*x4*x2+(1)*x1*x3*x1*x2^2*x4, 
  (1)*x3*x1^2*x2*x4*x3+(-1)*x3*x1^2*x2*x3*x4+(-1)*x1*x3*x1*x2*x4*x3+(
    1)*x1*x3*x1*x2*x3*x4, (1)*x3*x1^2*x3*x2*x1+(-1)*x3*x1^2*x3*x1*x2+(
    -1)*(x1*x3)^2*x2*x1+(1)*(x1*x3)^2*x1*x2, 
  (1)*x3*x1^2*x3^2*x1+(-1)*x3*x1*(x1*x3)^2+(-1)*(x1*x3)^2*x3*x1+(1)*(x1*x3)^3,
  (1)*x3*x1^2*x3*x4*x1+(-1)*x3*x1^2*x3*x1*x4+(-1)*(x1*x3)^2*x4*x1+(
    1)*(x1*x3)^2*x1*x4, (1)*x3*x1^2*x3^2*x2+(-1)*x3*x1^2*x3*x2*x3+(
    -1)*(x1*x3)^2*x3*x2+(1)*(x1*x3)^2*x2*x3, 
  (1)*x3*x1^2*x3*x4*x2+(-1)*x3*x1^2*x3*x2*x4+(-1)*(x1*x3)^2*x4*x2+(
    1)*(x1*x3)^2*x2*x4, (1)*x3*x1^2*x3*x4*x3+(-1)*x3*x1^2*x3^2*x4+(
    -1)*(x1*x3)^2*x4*x3+(1)*(x1*x3)^2*x3*x4, 
  (1)*x3*x1^2*x4*x2*x1+(-1)*x3*x1^2*x4*x1*x2+(-1)*x1*x3*x1*x4*x2*x1+(
    1)*x1*x3*x1*x4*x1*x2, (1)*x3*x1^2*x4*x3*x1+(-1)*x3*x1^2*x4*x1*x3+(
    -1)*x1*x3*x1*x4*x3*x1+(1)*x1*x3*x1*x4*x1*x3, 
  (1)*x3*x1^2*x4^2*x1+(-1)*x3*x1*(x1*x4)^2+(-1)*x1*x3*x1*x4^2*x1+(
    1)*x1*x3*(x1*x4)^2, (1)*x3*x1^2*x4*x3*x2+(-1)*x3*x1^2*x4*x2*x3+(
    -1)*x1*x3*x1*x4*x3*x2+(1)*x1*x3*x1*x4*x2*x3, 
  (1)*x3*x1^2*x4^2*x2+(-1)*x3*x1^2*x4*x2*x4+(-1)*x1*x3*x1*x4^2*x2+(
    1)*x1*x3*x1*x4*x2*x4, (1)*x3*x1^2*x4^2*x3+(-1)*x3*x1^2*x4*x3*x4+(
    -1)*x1*x3*x1*x4^2*x3+(1)*x1*x3*x1*x4*x3*x4, 
  (1)*x3*(x1*x2)^2*x1+(-1)*x3*x1*x2*x1^2*x2+(-1)*x1*x3*(x2*x1)^2+(
    1)*x1*x3*x2*x1^2*x2, (1)*x3*x1*x2*x1*x3*x1+(-1)*x3*x1*x2*x1^2*x3+(
    -1)*x1*x3*x2*x1*x3*x1+(1)*x1*x3*x2*x1^2*x3, 
  (1)*x3*x1*x2*x1*x4*x1+(-1)*x3*x1*x2*x1^2*x4+(-1)*x1*x3*x2*x1*x4*x1+(
    1)*x1*x3*x2*x1^2*x4, (1)*x3*x1*x2*x1*x3*x2+(-1)*x3*(x1*x2)^2*x3+(
    -1)*(x1*x3*x2)^2+(1)*x1*x3*x2*x1*x2*x3, 
  (1)*x3*x1*x2*x1*x4*x2+(-1)*x3*(x1*x2)^2*x4+(-1)*x1*x3*x2*x1*x4*x2+(
    1)*x1*x3*x2*x1*x2*x4, (1)*x3*x1*x2*x1*x4*x3+(-1)*x3*x1*x2*x1*x3*x4+(
    -1)*x1*x3*x2*x1*x4*x3+(1)*x1*x3*x2*x1*x3*x4, 
  (1)*x3*x1*x2^3*x1+(-1)*x3*x1*x2^2*x1*x2+(-1)*x1*x3*x2^3*x1+(
    1)*x1*x3*x2^2*x1*x2, (1)*x3*x1*x2^2*x3*x1+(-1)*x3*x1*x2^2*x1*x3+(
    -1)*x1*x3*x2^2*x3*x1+(1)*x1*x3*x2^2*x1*x3, 
  (1)*x3*x1*x2^2*x4*x1+(-1)*x3*x1*x2^2*x1*x4+(-1)*x1*x3*x2^2*x4*x1+(
    1)*x1*x3*x2^2*x1*x4, (1)*x3*x1*x2^2*x3*x2+(-1)*x3*x1*x2^3*x3+(
    -1)*x1*x3*x2^2*x3*x2+(1)*x1*x3*x2^3*x3, 
  (1)*x3*x1*x2^2*x4*x2+(-1)*x3*x1*x2^3*x4+(-1)*x1*x3*x2^2*x4*x2+(
    1)*x1*x3*x2^3*x4, (1)*x3*x1*x2^2*x4*x3+(-1)*x3*x1*x2^2*x3*x4+(
    -1)*x1*x3*x2^2*x4*x3+(1)*x1*x3*x2^2*x3*x4, 
  (1)*x3*x1*x2*x3*x2*x1+(-1)*(x3*x1*x2)^2+(-1)*x1*(x3*x2)^2*x1+(
    1)*x1*x3*x2*x3*x1*x2, (1)*x3*x1*x2*x3^2*x1+(-1)*x3*x1*x2*x3*x1*x3+(
    -1)*x1*x3*x2*x3^2*x1+(1)*x1*x3*x2*x3*x1*x3, 
  (1)*x3*x1*x2*x3*x4*x1+(-1)*x3*x1*x2*x3*x1*x4+(-1)*x1*x3*x2*x3*x4*x1+(
    1)*x1*x3*x2*x3*x1*x4, (1)*x3*x1*x2*x3^2*x2+(-1)*x3*x1*(x2*x3)^2+(
    -1)*x1*x3*x2*x3^2*x2+(1)*x1*(x3*x2)^2*x3, 
  (1)*x3*x1*x2*x3*x4*x2+(-1)*x3*x1*x2*x3*x2*x4+(-1)*x1*x3*x2*x3*x4*x2+(
    1)*x1*(x3*x2)^2*x4, (1)*x3*x1*x2*x3*x4*x3+(-1)*x3*x1*x2*x3^2*x4+(
    -1)*x1*x3*x2*x3*x4*x3+(1)*x1*x3*x2*x3^2*x4, 
  (1)*x3*x1*x2*x4*x2*x1+(-1)*x3*x1*x2*x4*x1*x2+(-1)*x1*x3*x2*x4*x2*x1+(
    1)*x1*x3*x2*x4*x1*x2, (1)*x3*x1*x2*x4*x3*x1+(-1)*x3*x1*x2*x4*x1*x3+(
    -1)*x1*x3*x2*x4*x3*x1+(1)*x1*x3*x2*x4*x1*x3, 
  (1)*x3*x1*x2*x4^2*x1+(-1)*x3*x1*x2*x4*x1*x4+(-1)*x1*x3*x2*x4^2*x1+(
    1)*x1*x3*x2*x4*x1*x4, (1)*x3*x1*x2*x4*x3*x2+(-1)*x3*x1*x2*x4*x2*x3+(
    -1)*x1*x3*x2*x4*x3*x2+(1)*x1*x3*x2*x4*x2*x3, 
  (1)*x3*x1*x2*x4^2*x2+(-1)*x3*x1*(x2*x4)^2+(-1)*x1*x3*x2*x4^2*x2+(
    1)*x1*x3*(x2*x4)^2, (1)*x3*x1*x2*x4^2*x3+(-1)*x3*x1*x2*x4*x3*x4+(
    -1)*x1*x3*x2*x4^2*x3+(1)*x1*x3*x2*x4*x3*x4, 
  (1)*(x3*x1)^2*x2*x1+(-1)*(x3*x1)^2*x1*x2+(-1)*x1*x3^2*x1*x2*x1+(
    1)*x1*x3^2*x1^2*x2, (1)*(x3*x1)^3+(-1)*(x3*x1)^2*x1*x3+(
    -1)*x1*x3*(x3*x1)^2+(1)*x1*x3^2*x1^2*x3, 
  (1)*(x3*x1)^2*x4*x1+(-1)*(x3*x1)^2*x1*x4+(-1)*x1*x3^2*x1*x4*x1+(
    1)*x1*x3^2*x1^2*x4, (1)*(x3*x1)^2*x3*x2+(-1)*(x3*x1)^2*x2*x3+(
    -1)*x1*x3^2*x1*x3*x2+(1)*x1*x3^2*x1*x2*x3, 
  (1)*(x3*x1)^2*x4*x2+(-1)*(x3*x1)^2*x2*x4+(-1)*x1*x3^2*x1*x4*x2+(
    1)*x1*x3^2*x1*x2*x4, (1)*(x3*x1)^2*x4*x3+(-1)*(x3*x1)^2*x3*x4+(
    -1)*x1*x3^2*x1*x4*x3+(1)*x1*x3^2*x1*x3*x4, 
  (1)*x3*x1*x3*x2^2*x1+(-1)*x3*x1*x3*x2*x1*x2+(-1)*x1*x3^2*x2^2*x1+(
    1)*x1*x3^2*x2*x1*x2, (1)*x3*x1*x3*x2*x3*x1+(-1)*x3*x1*x3*x2*x1*x3+(
    -1)*x1*x3^2*x2*x3*x1+(1)*x1*x3^2*x2*x1*x3, 
  (1)*x3*x1*x3*x2*x4*x1+(-1)*x3*x1*x3*x2*x1*x4+(-1)*x1*x3^2*x2*x4*x1+(
    1)*x1*x3^2*x2*x1*x4, (1)*x3*x1*(x3*x2)^2+(-1)*x3*x1*x3*x2^2*x3+(
    -1)*x1*x3*(x3*x2)^2+(1)*x1*x3^2*x2^2*x3, 
  (1)*x3*x1*x3*x2*x4*x2+(-1)*x3*x1*x3*x2^2*x4+(-1)*x1*x3^2*x2*x4*x2+(
    1)*x1*x3^2*x2^2*x4, (1)*x3*x1*x3*x2*x4*x3+(-1)*x3*x1*x3*x2*x3*x4+(
    -1)*x1*x3^2*x2*x4*x3+(1)*x1*x3^2*x2*x3*x4, 
  (1)*x3*x1*x3^2*x2*x1+(-1)*x3*x1*x3^2*x1*x2+(-1)*x1*x3^3*x2*x1+(
    1)*x1*x3^3*x1*x2, (1)*x3*x1*x3^3*x1+(-1)*(x3*x1*x3)^2+(-1)*x1*x3^4*x1+(
    1)*x1*x3^3*x1*x3, (1)*x3*x1*x3^2*x4*x1+(-1)*x3*x1*x3^2*x1*x4+(
    -1)*x1*x3^3*x4*x1+(1)*x1*x3^3*x1*x4, 
  (1)*x3*x1*x3^3*x2+(-1)*x3*x1*x3^2*x2*x3+(-1)*x1*x3^4*x2+(1)*x1*x3^3*x2*x3, 
  (1)*x3*x1*x3^2*x4*x2+(-1)*x3*x1*x3^2*x2*x4+(-1)*x1*x3^3*x4*x2+(
    1)*x1*x3^3*x2*x4, (1)*x3*x1*x3^2*x4*x3+(-1)*x3*x1*x3^3*x4+(
    -1)*x1*x3^3*x4*x3+(1)*x1*x3^4*x4, 
  (1)*x3*x1*x3*x4*x2*x1+(-1)*x3*x1*x3*x4*x1*x2+(-1)*x1*x3^2*x4*x2*x1+(
    1)*x1*x3^2*x4*x1*x2, (1)*x3*x1*x3*x4*x3*x1+(-1)*x3*x1*x3*x4*x1*x3+(
    -1)*x1*x3^2*x4*x3*x1+(1)*x1*x3^2*x4*x1*x3, 
  (1)*x3*x1*x3*x4^2*x1+(-1)*x3*x1*x3*x4*x1*x4+(-1)*x1*x3^2*x4^2*x1+(
    1)*x1*x3^2*x4*x1*x4, (1)*x3*x1*x3*x4*x3*x2+(-1)*x3*x1*x3*x4*x2*x3+(
    -1)*x1*x3^2*x4*x3*x2+(1)*x1*x3^2*x4*x2*x3, 
  (1)*x3*x1*x3*x4^2*x2+(-1)*x3*x1*x3*x4*x2*x4+(-1)*x1*x3^2*x4^2*x2+(
    1)*x1*x3^2*x4*x2*x4, (1)*x3*x1*x3*x4^2*x3+(-1)*x3*x1*(x3*x4)^2+(
    -1)*x1*x3^2*x4^2*x3+(1)*x1*x3*(x3*x4)^2, 
  (1)*x3*x1*x4*x1*x2*x1+(-1)*x3*x1*x4*x1^2*x2+(-1)*x1*x3*x4*x1*x2*x1+(
    1)*x1*x3*x4*x1^2*x2, (1)*x3*x1*x4*x1*x3*x1+(-1)*x3*x1*x4*x1^2*x3+(
    -1)*x1*x3*x4*x1*x3*x1+(1)*x1*x3*x4*x1^2*x3, 
  (1)*x3*(x1*x4)^2*x1+(-1)*x3*x1*x4*x1^2*x4+(-1)*x1*x3*(x4*x1)^2+(
    1)*x1*x3*x4*x1^2*x4, (1)*x3*x1*x4*x1*x3*x2+(-1)*x3*x1*x4*x1*x2*x3+(
    -1)*x1*x3*x4*x1*x3*x2+(1)*x1*x3*x4*x1*x2*x3, 
  (1)*x3*(x1*x4)^2*x2+(-1)*x3*x1*x4*x1*x2*x4+(-1)*x1*x3*x4*x1*x4*x2+(
    1)*x1*x3*x4*x1*x2*x4, (1)*x3*(x1*x4)^2*x3+(-1)*x3*x1*x4*x1*x3*x4+(
    -1)*x1*x3*x4*x1*x4*x3+(1)*(x1*x3*x4)^2, 
  (1)*x3*x1*x4*x2^2*x1+(-1)*x3*x1*x4*x2*x1*x2+(-1)*x1*x3*x4*x2^2*x1+(
    1)*x1*x3*x4*x2*x1*x2, (1)*x3*x1*x4*x2*x3*x1+(-1)*x3*x1*x4*x2*x1*x3+(
    -1)*x1*x3*x4*x2*x3*x1+(1)*x1*x3*x4*x2*x1*x3, 
  (1)*x3*x1*x4*x2*x4*x1+(-1)*x3*x1*x4*x2*x1*x4+(-1)*x1*x3*x4*x2*x4*x1+(
    1)*x1*x3*x4*x2*x1*x4, (1)*x3*x1*x4*x2*x3*x2+(-1)*x3*x1*x4*x2^2*x3+(
    -1)*x1*x3*x4*x2*x3*x2+(1)*x1*x3*x4*x2^2*x3, 
  (1)*x3*x1*(x4*x2)^2+(-1)*x3*x1*x4*x2^2*x4+(-1)*x1*x3*(x4*x2)^2+(
    1)*x1*x3*x4*x2^2*x4, (1)*x3*x1*x4*x2*x4*x3+(-1)*x3*x1*x4*x2*x3*x4+(
    -1)*x1*x3*x4*x2*x4*x3+(1)*x1*x3*x4*x2*x3*x4, 
  (1)*x3*x1*x4*x3*x2*x1+(-1)*x3*x1*x4*x3*x1*x2+(-1)*x1*x3*x4*x3*x2*x1+(
    1)*x1*x3*x4*x3*x1*x2, (1)*x3*x1*x4*x3^2*x1+(-1)*x3*x1*x4*x3*x1*x3+(
    -1)*x1*x3*x4*x3^2*x1+(1)*x1*x3*x4*x3*x1*x3, 
  (1)*x3*x1*x4*x3*x4*x1+(-1)*(x3*x1*x4)^2+(-1)*x1*(x3*x4)^2*x1+(
    1)*x1*x3*x4*x3*x1*x4, (1)*x3*x1*x4*x3^2*x2+(-1)*x3*x1*x4*x3*x2*x3+(
    -1)*x1*x3*x4*x3^2*x2+(1)*x1*x3*x4*x3*x2*x3, 
  (1)*x3*x1*x4*x3*x4*x2+(-1)*x3*x1*x4*x3*x2*x4+(-1)*x1*(x3*x4)^2*x2+(
    1)*x1*x3*x4*x3*x2*x4, (1)*x3*x1*(x4*x3)^2+(-1)*x3*x1*x4*x3^2*x4+(
    -1)*x1*(x3*x4)^2*x3+(1)*x1*x3*x4*x3^2*x4, 
  (1)*x3*x1*x4^2*x2*x1+(-1)*x3*x1*x4^2*x1*x2+(-1)*x1*x3*x4^2*x2*x1+(
    1)*x1*x3*x4^2*x1*x2, (1)*x3*x1*x4^2*x3*x1+(-1)*x3*x1*x4^2*x1*x3+(
    -1)*x1*x3*x4^2*x3*x1+(1)*x1*x3*x4^2*x1*x3, 
  (1)*x3*x1*x4^3*x1+(-1)*x3*x1*x4^2*x1*x4+(-1)*x1*x3*x4^3*x1+(
    1)*x1*x3*x4^2*x1*x4, (1)*x3*x1*x4^2*x3*x2+(-1)*x3*x1*x4^2*x2*x3+(
    -1)*x1*x3*x4^2*x3*x2+(1)*x1*x3*x4^2*x2*x3, 
  (1)*x3*x1*x4^3*x2+(-1)*x3*x1*x4^2*x2*x4+(-1)*x1*x3*x4^3*x2+(
    1)*x1*x3*x4^2*x2*x4, (1)*x3*x1*x4^3*x3+(-1)*x3*x1*x4^2*x3*x4+(
    -1)*x1*x3*x4^3*x3+(1)*x1*x3*x4^2*x3*x4, 
  (1)*x4*x1^3*x2*x1+(-1)*x4*x1^4*x2+(-1)*x1*x4*x1^2*x2*x1+(1)*x1*x4*x1^3*x2, 
  (1)*x4*x1^3*x3*x1+(-1)*x4*x1^4*x3+(-1)*x1*x4*x1^2*x3*x1+(1)*x1*x4*x1^3*x3, 
  (1)*x4*x1^3*x4*x1+(-1)*x4*x1^4*x4+(-1)*(x1*x4*x1)^2+(1)*x1*x4*x1^3*x4, 
  (1)*x4*x1^3*x3*x2+(-1)*x4*x1^3*x2*x3+(-1)*x1*x4*x1^2*x3*x2+(
    1)*x1*x4*x1^2*x2*x3, (1)*x4*x1^3*x4*x2+(-1)*x4*x1^3*x2*x4+(
    -1)*x1*x4*x1^2*x4*x2+(1)*x1*x4*x1^2*x2*x4, 
  (1)*x4*x1^3*x4*x3+(-1)*x4*x1^3*x3*x4+(-1)*x1*x4*x1^2*x4*x3+(
    1)*x1*x4*x1^2*x3*x4, (1)*x4*x1^2*x2^2*x1+(-1)*x4*x1*(x1*x2)^2+(
    -1)*x1*x4*x1*x2^2*x1+(1)*x1*x4*(x1*x2)^2, 
  (1)*x4*x1^2*x2*x3*x1+(-1)*x4*x1^2*x2*x1*x3+(-1)*x1*x4*x1*x2*x3*x1+(
    1)*x1*x4*x1*x2*x1*x3, (1)*x4*x1^2*x2*x4*x1+(-1)*x4*x1^2*x2*x1*x4+(
    -1)*x1*x4*x1*x2*x4*x1+(1)*x1*x4*x1*x2*x1*x4, 
  (1)*x4*x1^2*x2*x3*x2+(-1)*x4*x1^2*x2^2*x3+(-1)*x1*x4*x1*x2*x3*x2+(
    1)*x1*x4*x1*x2^2*x3, (1)*x4*x1^2*x2*x4*x2+(-1)*x4*x1^2*x2^2*x4+(
    -1)*x1*x4*x1*x2*x4*x2+(1)*x1*x4*x1*x2^2*x4, 
  (1)*x4*x1^2*x2*x4*x3+(-1)*x4*x1^2*x2*x3*x4+(-1)*x1*x4*x1*x2*x4*x3+(
    1)*x1*x4*x1*x2*x3*x4, (1)*x4*x1^2*x3*x2*x1+(-1)*x4*x1^2*x3*x1*x2+(
    -1)*x1*x4*x1*x3*x2*x1+(1)*x1*x4*x1*x3*x1*x2, 
  (1)*x4*x1^2*x3^2*x1+(-1)*x4*x1*(x1*x3)^2+(-1)*x1*x4*x1*x3^2*x1+(
    1)*x1*x4*(x1*x3)^2, (1)*x4*x1^2*x3*x4*x1+(-1)*x4*x1^2*x3*x1*x4+(
    -1)*x1*x4*x1*x3*x4*x1+(1)*x1*x4*x1*x3*x1*x4, 
  (1)*x4*x1^2*x3^2*x2+(-1)*x4*x1^2*x3*x2*x3+(-1)*x1*x4*x1*x3^2*x2+(
    1)*x1*x4*x1*x3*x2*x3, (1)*x4*x1^2*x3*x4*x2+(-1)*x4*x1^2*x3*x2*x4+(
    -1)*x1*x4*x1*x3*x4*x2+(1)*x1*x4*x1*x3*x2*x4, 
  (1)*x4*x1^2*x3*x4*x3+(-1)*x4*x1^2*x3^2*x4+(-1)*x1*x4*x1*x3*x4*x3+(
    1)*x1*x4*x1*x3^2*x4, (1)*x4*x1^2*x4*x2*x1+(-1)*x4*x1^2*x4*x1*x2+(
    -1)*(x1*x4)^2*x2*x1+(1)*(x1*x4)^2*x1*x2, 
  (1)*x4*x1^2*x4*x3*x1+(-1)*x4*x1^2*x4*x1*x3+(-1)*(x1*x4)^2*x3*x1+(
    1)*(x1*x4)^2*x1*x3, (1)*x4*x1^2*x4^2*x1+(-1)*x4*x1*(x1*x4)^2+(
    -1)*(x1*x4)^2*x4*x1+(1)*(x1*x4)^3, 
  (1)*x4*x1^2*x4*x3*x2+(-1)*x4*x1^2*x4*x2*x3+(-1)*(x1*x4)^2*x3*x2+(
    1)*(x1*x4)^2*x2*x3, (1)*x4*x1^2*x4^2*x2+(-1)*x4*x1^2*x4*x2*x4+(
    -1)*(x1*x4)^2*x4*x2+(1)*(x1*x4)^2*x2*x4, 
  (1)*x4*x1^2*x4^2*x3+(-1)*x4*x1^2*x4*x3*x4+(-1)*(x1*x4)^2*x4*x3+(
    1)*(x1*x4)^2*x3*x4, (1)*x4*(x1*x2)^2*x1+(-1)*x4*x1*x2*x1^2*x2+(
    -1)*x1*x4*(x2*x1)^2+(1)*x1*x4*x2*x1^2*x2, 
  (1)*x4*x1*x2*x1*x3*x1+(-1)*x4*x1*x2*x1^2*x3+(-1)*x1*x4*x2*x1*x3*x1+(
    1)*x1*x4*x2*x1^2*x3, (1)*x4*x1*x2*x1*x4*x1+(-1)*x4*x1*x2*x1^2*x4+(
    -1)*x1*x4*x2*x1*x4*x1+(1)*x1*x4*x2*x1^2*x4, 
  (1)*x4*x1*x2*x1*x3*x2+(-1)*x4*(x1*x2)^2*x3+(-1)*x1*x4*x2*x1*x3*x2+(
    1)*x1*x4*x2*x1*x2*x3, (1)*x4*x1*x2*x1*x4*x2+(-1)*x4*(x1*x2)^2*x4+(
    -1)*(x1*x4*x2)^2+(1)*x1*x4*x2*x1*x2*x4, 
  (1)*x4*x1*x2*x1*x4*x3+(-1)*x4*x1*x2*x1*x3*x4+(-1)*x1*x4*x2*x1*x4*x3+(
    1)*x1*x4*x2*x1*x3*x4, (1)*x4*x1*x2^3*x1+(-1)*x4*x1*x2^2*x1*x2+(
    -1)*x1*x4*x2^3*x1+(1)*x1*x4*x2^2*x1*x2, 
  (1)*x4*x1*x2^2*x3*x1+(-1)*x4*x1*x2^2*x1*x3+(-1)*x1*x4*x2^2*x3*x1+(
    1)*x1*x4*x2^2*x1*x3, (1)*x4*x1*x2^2*x4*x1+(-1)*x4*x1*x2^2*x1*x4+(
    -1)*x1*x4*x2^2*x4*x1+(1)*x1*x4*x2^2*x1*x4, 
  (1)*x4*x1*x2^2*x3*x2+(-1)*x4*x1*x2^3*x3+(-1)*x1*x4*x2^2*x3*x2+(
    1)*x1*x4*x2^3*x3, (1)*x4*x1*x2^2*x4*x2+(-1)*x4*x1*x2^3*x4+(
    -1)*x1*x4*x2^2*x4*x2+(1)*x1*x4*x2^3*x4, 
  (1)*x4*x1*x2^2*x4*x3+(-1)*x4*x1*x2^2*x3*x4+(-1)*x1*x4*x2^2*x4*x3+(
    1)*x1*x4*x2^2*x3*x4, (1)*x4*x1*x2*x3*x2*x1+(-1)*x4*x1*x2*x3*x1*x2+(
    -1)*x1*x4*x2*x3*x2*x1+(1)*x1*x4*x2*x3*x1*x2, 
  (1)*x4*x1*x2*x3^2*x1+(-1)*x4*x1*x2*x3*x1*x3+(-1)*x1*x4*x2*x3^2*x1+(
    1)*x1*x4*x2*x3*x1*x3, (1)*x4*x1*x2*x3*x4*x1+(-1)*x4*x1*x2*x3*x1*x4+(
    -1)*x1*x4*x2*x3*x4*x1+(1)*x1*x4*x2*x3*x1*x4, 
  (1)*x4*x1*x2*x3^2*x2+(-1)*x4*x1*(x2*x3)^2+(-1)*x1*x4*x2*x3^2*x2+(
    1)*x1*x4*(x2*x3)^2, (1)*x4*x1*x2*x3*x4*x2+(-1)*x4*x1*x2*x3*x2*x4+(
    -1)*x1*x4*x2*x3*x4*x2+(1)*x1*x4*x2*x3*x2*x4, 
  (1)*x4*x1*x2*x3*x4*x3+(-1)*x4*x1*x2*x3^2*x4+(-1)*x1*x4*x2*x3*x4*x3+(
    1)*x1*x4*x2*x3^2*x4, (1)*x4*x1*x2*x4*x2*x1+(-1)*(x4*x1*x2)^2+(
    -1)*x1*(x4*x2)^2*x1+(1)*x1*x4*x2*x4*x1*x2, 
  (1)*x4*x1*x2*x4*x3*x1+(-1)*x4*x1*x2*x4*x1*x3+(-1)*x1*x4*x2*x4*x3*x1+(
    1)*x1*x4*x2*x4*x1*x3, (1)*x4*x1*x2*x4^2*x1+(-1)*x4*x1*x2*x4*x1*x4+(
    -1)*x1*x4*x2*x4^2*x1+(1)*x1*x4*x2*x4*x1*x4, 
  (1)*x4*x1*x2*x4*x3*x2+(-1)*x4*x1*x2*x4*x2*x3+(-1)*x1*x4*x2*x4*x3*x2+(
    1)*x1*(x4*x2)^2*x3, (1)*x4*x1*x2*x4^2*x2+(-1)*x4*x1*(x2*x4)^2+(
    -1)*x1*x4*x2*x4^2*x2+(1)*x1*(x4*x2)^2*x4, 
  (1)*x4*x1*x2*x4^2*x3+(-1)*x4*x1*x2*x4*x3*x4+(-1)*x1*x4*x2*x4^2*x3+(
    1)*x1*x4*x2*x4*x3*x4, (1)*x4*x1*x3*x1*x2*x1+(-1)*x4*x1*x3*x1^2*x2+(
    -1)*x1*x4*x3*x1*x2*x1+(1)*x1*x4*x3*x1^2*x2, 
  (1)*x4*(x1*x3)^2*x1+(-1)*x4*x1*x3*x1^2*x3+(-1)*x1*x4*(x3*x1)^2+(
    1)*x1*x4*x3*x1^2*x3, (1)*x4*x1*x3*x1*x4*x1+(-1)*x4*x1*x3*x1^2*x4+(
    -1)*x1*x4*x3*x1*x4*x1+(1)*x1*x4*x3*x1^2*x4, 
  (1)*x4*(x1*x3)^2*x2+(-1)*x4*x1*x3*x1*x2*x3+(-1)*x1*x4*x3*x1*x3*x2+(
    1)*x1*x4*x3*x1*x2*x3, (1)*x4*x1*x3*x1*x4*x2+(-1)*x4*x1*x3*x1*x2*x4+(
    -1)*x1*x4*x3*x1*x4*x2+(1)*x1*x4*x3*x1*x2*x4, 
  (1)*x4*x1*x3*x1*x4*x3+(-1)*x4*(x1*x3)^2*x4+(-1)*(x1*x4*x3)^2+(
    1)*x1*x4*x3*x1*x3*x4, (1)*x4*x1*x3*x2^2*x1+(-1)*x4*x1*x3*x2*x1*x2+(
    -1)*x1*x4*x3*x2^2*x1+(1)*x1*x4*x3*x2*x1*x2, 
  (1)*x4*x1*x3*x2*x3*x1+(-1)*x4*x1*x3*x2*x1*x3+(-1)*x1*x4*x3*x2*x3*x1+(
    1)*x1*x4*x3*x2*x1*x3, (1)*x4*x1*x3*x2*x4*x1+(-1)*x4*x1*x3*x2*x1*x4+(
    -1)*x1*x4*x3*x2*x4*x1+(1)*x1*x4*x3*x2*x1*x4, 
  (1)*x4*x1*(x3*x2)^2+(-1)*x4*x1*x3*x2^2*x3+(-1)*x1*x4*(x3*x2)^2+(
    1)*x1*x4*x3*x2^2*x3, (1)*x4*x1*x3*x2*x4*x2+(-1)*x4*x1*x3*x2^2*x4+(
    -1)*x1*x4*x3*x2*x4*x2+(1)*x1*x4*x3*x2^2*x4, 
  (1)*x4*x1*x3*x2*x4*x3+(-1)*x4*x1*x3*x2*x3*x4+(-1)*x1*x4*x3*x2*x4*x3+(
    1)*x1*x4*x3*x2*x3*x4, (1)*x4*x1*x3^2*x2*x1+(-1)*x4*x1*x3^2*x1*x2+(
    -1)*x1*x4*x3^2*x2*x1+(1)*x1*x4*x3^2*x1*x2, 
  (1)*x4*x1*x3^3*x1+(-1)*x4*x1*x3^2*x1*x3+(-1)*x1*x4*x3^3*x1+(
    1)*x1*x4*x3^2*x1*x3, (1)*x4*x1*x3^2*x4*x1+(-1)*x4*x1*x3^2*x1*x4+(
    -1)*x1*x4*x3^2*x4*x1+(1)*x1*x4*x3^2*x1*x4, 
  (1)*x4*x1*x3^3*x2+(-1)*x4*x1*x3^2*x2*x3+(-1)*x1*x4*x3^3*x2+(
    1)*x1*x4*x3^2*x2*x3, (1)*x4*x1*x3^2*x4*x2+(-1)*x4*x1*x3^2*x2*x4+(
    -1)*x1*x4*x3^2*x4*x2+(1)*x1*x4*x3^2*x2*x4, 
  (1)*x4*x1*x3^2*x4*x3+(-1)*x4*x1*x3^3*x4+(-1)*x1*x4*x3^2*x4*x3+(
    1)*x1*x4*x3^3*x4, (1)*x4*x1*x3*x4*x2*x1+(-1)*x4*x1*x3*x4*x1*x2+(
    -1)*x1*x4*x3*x4*x2*x1+(1)*x1*x4*x3*x4*x1*x2, 
  (1)*x4*x1*x3*x4*x3*x1+(-1)*(x4*x1*x3)^2+(-1)*x1*(x4*x3)^2*x1+(
    1)*x1*x4*x3*x4*x1*x3, (1)*x4*x1*x3*x4^2*x1+(-1)*x4*x1*x3*x4*x1*x4+(
    -1)*x1*x4*x3*x4^2*x1+(1)*x1*x4*x3*x4*x1*x4, 
  (1)*x4*x1*x3*x4*x3*x2+(-1)*x4*x1*x3*x4*x2*x3+(-1)*x1*(x4*x3)^2*x2+(
    1)*x1*x4*x3*x4*x2*x3, (1)*x4*x1*x3*x4^2*x2+(-1)*x4*x1*x3*x4*x2*x4+(
    -1)*x1*x4*x3*x4^2*x2+(1)*x1*x4*x3*x4*x2*x4, 
  (1)*x4*x1*x3*x4^2*x3+(-1)*x4*x1*(x3*x4)^2+(-1)*x1*x4*x3*x4^2*x3+(
    1)*x1*(x4*x3)^2*x4, (1)*(x4*x1)^2*x2*x1+(-1)*(x4*x1)^2*x1*x2+(
    -1)*x1*x4^2*x1*x2*x1+(1)*x1*x4^2*x1^2*x2, 
  (1)*(x4*x1)^2*x3*x1+(-1)*(x4*x1)^2*x1*x3+(-1)*x1*x4^2*x1*x3*x1+(
    1)*x1*x4^2*x1^2*x3, (1)*(x4*x1)^3+(-1)*(x4*x1)^2*x1*x4+(
    -1)*x1*x4*(x4*x1)^2+(1)*x1*x4^2*x1^2*x4, 
  (1)*(x4*x1)^2*x3*x2+(-1)*(x4*x1)^2*x2*x3+(-1)*x1*x4^2*x1*x3*x2+(
    1)*x1*x4^2*x1*x2*x3, (1)*(x4*x1)^2*x4*x2+(-1)*(x4*x1)^2*x2*x4+(
    -1)*x1*x4^2*x1*x4*x2+(1)*x1*x4^2*x1*x2*x4, 
  (1)*(x4*x1)^2*x4*x3+(-1)*(x4*x1)^2*x3*x4+(-1)*x1*x4^2*x1*x4*x3+(
    1)*x1*x4^2*x1*x3*x4, (1)*x4*x1*x4*x2^2*x1+(-1)*x4*x1*x4*x2*x1*x2+(
    -1)*x1*x4^2*x2^2*x1+(1)*x1*x4^2*x2*x1*x2, 
  (1)*x4*x1*x4*x2*x3*x1+(-1)*x4*x1*x4*x2*x1*x3+(-1)*x1*x4^2*x2*x3*x1+(
    1)*x1*x4^2*x2*x1*x3, (1)*x4*x1*x4*x2*x4*x1+(-1)*x4*x1*x4*x2*x1*x4+(
    -1)*x1*x4^2*x2*x4*x1+(1)*x1*x4^2*x2*x1*x4, 
  (1)*x4*x1*x4*x2*x3*x2+(-1)*x4*x1*x4*x2^2*x3+(-1)*x1*x4^2*x2*x3*x2+(
    1)*x1*x4^2*x2^2*x3, (1)*x4*x1*(x4*x2)^2+(-1)*x4*x1*x4*x2^2*x4+(
    -1)*x1*x4*(x4*x2)^2+(1)*x1*x4^2*x2^2*x4, 
  (1)*x4*x1*x4*x2*x4*x3+(-1)*x4*x1*x4*x2*x3*x4+(-1)*x1*x4^2*x2*x4*x3+(
    1)*x1*x4^2*x2*x3*x4, (1)*x4*x1*x4*x3*x2*x1+(-1)*x4*x1*x4*x3*x1*x2+(
    -1)*x1*x4^2*x3*x2*x1+(1)*x1*x4^2*x3*x1*x2, 
  (1)*x4*x1*x4*x3^2*x1+(-1)*x4*x1*x4*x3*x1*x3+(-1)*x1*x4^2*x3^2*x1+(
    1)*x1*x4^2*x3*x1*x3, (1)*x4*x1*x4*x3*x4*x1+(-1)*x4*x1*x4*x3*x1*x4+(
    -1)*x1*x4^2*x3*x4*x1+(1)*x1*x4^2*x3*x1*x4, 
  (1)*x4*x1*x4*x3^2*x2+(-1)*x4*x1*x4*x3*x2*x3+(-1)*x1*x4^2*x3^2*x2+(
    1)*x1*x4^2*x3*x2*x3, (1)*x4*x1*x4*x3*x4*x2+(-1)*x4*x1*x4*x3*x2*x4+(
    -1)*x1*x4^2*x3*x4*x2+(1)*x1*x4^2*x3*x2*x4, 
  (1)*x4*x1*(x4*x3)^2+(-1)*x4*x1*x4*x3^2*x4+(-1)*x1*x4*(x4*x3)^2+(
    1)*x1*x4^2*x3^2*x4, (1)*x4*x1*x4^2*x2*x1+(-1)*x4*x1*x4^2*x1*x2+(
    -1)*x1*x4^3*x2*x1+(1)*x1*x4^3*x1*x2, 
  (1)*x4*x1*x4^2*x3*x1+(-1)*x4*x1*x4^2*x1*x3+(-1)*x1*x4^3*x3*x1+(
    1)*x1*x4^3*x1*x3, (1)*x4*x1*x4^3*x1+(-1)*(x4*x1*x4)^2+(-1)*x1*x4^4*x1+(
    1)*x1*x4^3*x1*x4, (1)*x4*x1*x4^2*x3*x2+(-1)*x4*x1*x4^2*x2*x3+(
    -1)*x1*x4^3*x3*x2+(1)*x1*x4^3*x2*x3, 
  (1)*x4*x1*x4^3*x2+(-1)*x4*x1*x4^2*x2*x4+(-1)*x1*x4^4*x2+(1)*x1*x4^3*x2*x4, 
  (1)*x4*x1*x4^3*x3+(-1)*x4*x1*x4^2*x3*x4+(-1)*x1*x4^4*x3+(1)*x1*x4^3*x3*x4, 
  (1)*x3*x2*x1^2*x2*x1+(-1)*x3*x2*x1^3*x2+(-1)*x2*x3*x1^2*x2*x1+(
    1)*x2*x3*x1^3*x2, (1)*x3*x2*x1^2*x3*x1+(-1)*x3*x2*x1^3*x3+(
    -1)*x2*x3*x1^2*x3*x1+(1)*x2*x3*x1^3*x3, 
  (1)*x3*x2*x1^2*x4*x1+(-1)*x3*x2*x1^3*x4+(-1)*x2*x3*x1^2*x4*x1+(
    1)*x2*x3*x1^3*x4, (1)*x3*x2*x1^2*x3*x2+(-1)*x3*x2*x1^2*x2*x3+(
    -1)*x2*x3*x1^2*x3*x2+(1)*x2*x3*x1^2*x2*x3, 
  (1)*x3*x2*x1^2*x4*x2+(-1)*x3*x2*x1^2*x2*x4+(-1)*x2*x3*x1^2*x4*x2+(
    1)*x2*x3*x1^2*x2*x4, (1)*x3*x2*x1^2*x4*x3+(-1)*x3*x2*x1^2*x3*x4+(
    -1)*x2*x3*x1^2*x4*x3+(1)*x2*x3*x1^2*x3*x4, 
  (1)*x3*x2*x1*x2^2*x1+(-1)*x3*(x2*x1)^2*x2+(-1)*x2*x3*x1*x2^2*x1+(
    1)*x2*x3*(x1*x2)^2, (1)*x3*x2*x1*x2*x3*x1+(-1)*x3*(x2*x1)^2*x3+(
    -1)*(x2*x3*x1)^2+(1)*x2*x3*x1*x2*x1*x3, 
  (1)*x3*x2*x1*x2*x4*x1+(-1)*x3*(x2*x1)^2*x4+(-1)*x2*x3*x1*x2*x4*x1+(
    1)*x2*x3*x1*x2*x1*x4, (1)*x3*x2*x1*x2*x3*x2+(-1)*x3*x2*x1*x2^2*x3+(
    -1)*x2*x3*x1*x2*x3*x2+(1)*x2*x3*x1*x2^2*x3, 
  (1)*x3*x2*x1*x2*x4*x2+(-1)*x3*x2*x1*x2^2*x4+(-1)*x2*x3*x1*x2*x4*x2+(
    1)*x2*x3*x1*x2^2*x4, (1)*x3*x2*x1*x2*x4*x3+(-1)*x3*x2*x1*x2*x3*x4+(
    -1)*x2*x3*x1*x2*x4*x3+(1)*x2*x3*x1*x2*x3*x4, 
  (1)*(x3*x2*x1)^2+(-1)*x3*x2*x1*x3*x1*x2+(-1)*x2*x3*x1*x3*x2*x1+(
    1)*x2*(x3*x1)^2*x2, (1)*x3*x2*x1*x3^2*x1+(-1)*x3*x2*(x1*x3)^2+(
    -1)*x2*x3*x1*x3^2*x1+(1)*x2*(x3*x1)^2*x3, 
  (1)*x3*x2*x1*x3*x4*x1+(-1)*x3*x2*x1*x3*x1*x4+(-1)*x2*x3*x1*x3*x4*x1+(
    1)*x2*(x3*x1)^2*x4, (1)*x3*x2*x1*x3^2*x2+(-1)*x3*x2*x1*x3*x2*x3+(
    -1)*x2*x3*x1*x3^2*x2+(1)*x2*x3*x1*x3*x2*x3, 
  (1)*x3*x2*x1*x3*x4*x2+(-1)*x3*x2*x1*x3*x2*x4+(-1)*x2*x3*x1*x3*x4*x2+(
    1)*x2*x3*x1*x3*x2*x4, (1)*x3*x2*x1*x3*x4*x3+(-1)*x3*x2*x1*x3^2*x4+(
    -1)*x2*x3*x1*x3*x4*x3+(1)*x2*x3*x1*x3^2*x4, 
  (1)*x3*x2*x1*x4*x2*x1+(-1)*x3*x2*x1*x4*x1*x2+(-1)*x2*x3*x1*x4*x2*x1+(
    1)*x2*x3*x1*x4*x1*x2, (1)*x3*x2*x1*x4*x3*x1+(-1)*x3*x2*x1*x4*x1*x3+(
    -1)*x2*x3*x1*x4*x3*x1+(1)*x2*x3*x1*x4*x1*x3, 
  (1)*x3*x2*x1*x4^2*x1+(-1)*x3*x2*(x1*x4)^2+(-1)*x2*x3*x1*x4^2*x1+(
    1)*x2*x3*(x1*x4)^2, (1)*x3*x2*x1*x4*x3*x2+(-1)*x3*x2*x1*x4*x2*x3+(
    -1)*x2*x3*x1*x4*x3*x2+(1)*x2*x3*x1*x4*x2*x3, 
  (1)*x3*x2*x1*x4^2*x2+(-1)*x3*x2*x1*x4*x2*x4+(-1)*x2*x3*x1*x4^2*x2+(
    1)*x2*x3*x1*x4*x2*x4, (1)*x3*x2*x1*x4^2*x3+(-1)*x3*x2*x1*x4*x3*x4+(
    -1)*x2*x3*x1*x4^2*x3+(1)*x2*x3*x1*x4*x3*x4, 
  (1)*x3*x2*(x2*x1)^2+(-1)*x3*x2^2*x1^2*x2+(-1)*x2*x3*(x2*x1)^2+(
    1)*x2*x3*x2*x1^2*x2, (1)*x3*x2^2*x1*x3*x1+(-1)*x3*x2^2*x1^2*x3+(
    -1)*x2*x3*x2*x1*x3*x1+(1)*x2*x3*x2*x1^2*x3, 
  (1)*x3*x2^2*x1*x4*x1+(-1)*x3*x2^2*x1^2*x4+(-1)*x2*x3*x2*x1*x4*x1+(
    1)*x2*x3*x2*x1^2*x4, (1)*x3*x2^2*x1*x3*x2+(-1)*x3*x2^2*x1*x2*x3+(
    -1)*x2*x3*x2*x1*x3*x2+(1)*x2*x3*x2*x1*x2*x3, 
  (1)*x3*x2^2*x1*x4*x2+(-1)*x3*x2^2*x1*x2*x4+(-1)*x2*x3*x2*x1*x4*x2+(
    1)*x2*x3*x2*x1*x2*x4, (1)*x3*x2^2*x1*x4*x3+(-1)*x3*x2^2*x1*x3*x4+(
    -1)*x2*x3*x2*x1*x4*x3+(1)*x2*x3*x2*x1*x3*x4, 
  (1)*x3*x2^4*x1+(-1)*x3*x2^3*x1*x2+(-1)*x2*x3*x2^3*x1+(1)*x2*x3*x2^2*x1*x2, 
  (1)*x3*x2^3*x3*x1+(-1)*x3*x2^3*x1*x3+(-1)*x2*x3*x2^2*x3*x1+(
    1)*x2*x3*x2^2*x1*x3, (1)*x3*x2^3*x4*x1+(-1)*x3*x2^3*x1*x4+(
    -1)*x2*x3*x2^2*x4*x1+(1)*x2*x3*x2^2*x1*x4, 
  (1)*x3*x2^3*x3*x2+(-1)*x3*x2^4*x3+(-1)*(x2*x3*x2)^2+(1)*x2*x3*x2^3*x3, 
  (1)*x3*x2^3*x4*x2+(-1)*x3*x2^4*x4+(-1)*x2*x3*x2^2*x4*x2+(1)*x2*x3*x2^3*x4, 
  (1)*x3*x2^3*x4*x3+(-1)*x3*x2^3*x3*x4+(-1)*x2*x3*x2^2*x4*x3+(
    1)*x2*x3*x2^2*x3*x4, (1)*x3*x2^2*x3*x2*x1+(-1)*x3*x2^2*x3*x1*x2+(
    -1)*(x2*x3)^2*x2*x1+(1)*(x2*x3)^2*x1*x2, 
  (1)*x3*x2^2*x3^2*x1+(-1)*x3*x2^2*x3*x1*x3+(-1)*(x2*x3)^2*x3*x1+(
    1)*(x2*x3)^2*x1*x3, (1)*x3*x2^2*x3*x4*x1+(-1)*x3*x2^2*x3*x1*x4+(
    -1)*(x2*x3)^2*x4*x1+(1)*(x2*x3)^2*x1*x4, 
  (1)*x3*x2^2*x3^2*x2+(-1)*x3*x2*(x2*x3)^2+(-1)*(x2*x3)^2*x3*x2+(1)*(x2*x3)^3,
  (1)*x3*x2^2*x3*x4*x2+(-1)*x3*x2^2*x3*x2*x4+(-1)*(x2*x3)^2*x4*x2+(
    1)*(x2*x3)^2*x2*x4, (1)*x3*x2^2*x3*x4*x3+(-1)*x3*x2^2*x3^2*x4+(
    -1)*(x2*x3)^2*x4*x3+(1)*(x2*x3)^2*x3*x4, 
  (1)*x3*x2^2*x4*x2*x1+(-1)*x3*x2^2*x4*x1*x2+(-1)*x2*x3*x2*x4*x2*x1+(
    1)*x2*x3*x2*x4*x1*x2, (1)*x3*x2^2*x4*x3*x1+(-1)*x3*x2^2*x4*x1*x3+(
    -1)*x2*x3*x2*x4*x3*x1+(1)*x2*x3*x2*x4*x1*x3, 
  (1)*x3*x2^2*x4^2*x1+(-1)*x3*x2^2*x4*x1*x4+(-1)*x2*x3*x2*x4^2*x1+(
    1)*x2*x3*x2*x4*x1*x4, (1)*x3*x2^2*x4*x3*x2+(-1)*x3*x2^2*x4*x2*x3+(
    -1)*x2*x3*x2*x4*x3*x2+(1)*x2*x3*x2*x4*x2*x3, 
  (1)*x3*x2^2*x4^2*x2+(-1)*x3*x2*(x2*x4)^2+(-1)*x2*x3*x2*x4^2*x2+(
    1)*x2*x3*(x2*x4)^2, (1)*x3*x2^2*x4^2*x3+(-1)*x3*x2^2*x4*x3*x4+(
    -1)*x2*x3*x2*x4^2*x3+(1)*x2*x3*x2*x4*x3*x4, 
  (1)*x3*x2*x3*x1*x2*x1+(-1)*x3*x2*x3*x1^2*x2+(-1)*x2*x3^2*x1*x2*x1+(
    1)*x2*x3^2*x1^2*x2, (1)*x3*x2*(x3*x1)^2+(-1)*x3*x2*x3*x1^2*x3+(
    -1)*x2*x3*(x3*x1)^2+(1)*x2*x3^2*x1^2*x3, 
  (1)*x3*x2*x3*x1*x4*x1+(-1)*x3*x2*x3*x1^2*x4+(-1)*x2*x3^2*x1*x4*x1+(
    1)*x2*x3^2*x1^2*x4, (1)*x3*x2*x3*x1*x3*x2+(-1)*x3*x2*x3*x1*x2*x3+(
    -1)*x2*x3^2*x1*x3*x2+(1)*x2*x3^2*x1*x2*x3, 
  (1)*x3*x2*x3*x1*x4*x2+(-1)*x3*x2*x3*x1*x2*x4+(-1)*x2*x3^2*x1*x4*x2+(
    1)*x2*x3^2*x1*x2*x4, (1)*x3*x2*x3*x1*x4*x3+(-1)*x3*x2*x3*x1*x3*x4+(
    -1)*x2*x3^2*x1*x4*x3+(1)*x2*x3^2*x1*x3*x4, 
  (1)*(x3*x2)^2*x2*x1+(-1)*(x3*x2)^2*x1*x2+(-1)*x2*x3^2*x2^2*x1+(
    1)*x2*x3^2*x2*x1*x2, (1)*(x3*x2)^2*x3*x1+(-1)*(x3*x2)^2*x1*x3+(
    -1)*x2*x3^2*x2*x3*x1+(1)*x2*x3^2*x2*x1*x3, 
  (1)*(x3*x2)^2*x4*x1+(-1)*(x3*x2)^2*x1*x4+(-1)*x2*x3^2*x2*x4*x1+(
    1)*x2*x3^2*x2*x1*x4, (1)*(x3*x2)^3+(-1)*(x3*x2)^2*x2*x3+(
    -1)*x2*x3*(x3*x2)^2+(1)*x2*x3^2*x2^2*x3, 
  (1)*(x3*x2)^2*x4*x2+(-1)*(x3*x2)^2*x2*x4+(-1)*x2*x3^2*x2*x4*x2+(
    1)*x2*x3^2*x2^2*x4, (1)*(x3*x2)^2*x4*x3+(-1)*(x3*x2)^2*x3*x4+(
    -1)*x2*x3^2*x2*x4*x3+(1)*x2*x3^2*x2*x3*x4, 
  (1)*x3*x2*x3^2*x2*x1+(-1)*x3*x2*x3^2*x1*x2+(-1)*x2*x3^3*x2*x1+(
    1)*x2*x3^3*x1*x2, (1)*x3*x2*x3^3*x1+(-1)*x3*x2*x3^2*x1*x3+(
    -1)*x2*x3^4*x1+(1)*x2*x3^3*x1*x3, 
  (1)*x3*x2*x3^2*x4*x1+(-1)*x3*x2*x3^2*x1*x4+(-1)*x2*x3^3*x4*x1+(
    1)*x2*x3^3*x1*x4, (1)*x3*x2*x3^3*x2+(-1)*(x3*x2*x3)^2+(-1)*x2*x3^4*x2+(
    1)*x2*x3^3*x2*x3, (1)*x3*x2*x3^2*x4*x2+(-1)*x3*x2*x3^2*x2*x4+(
    -1)*x2*x3^3*x4*x2+(1)*x2*x3^3*x2*x4, 
  (1)*x3*x2*x3^2*x4*x3+(-1)*x3*x2*x3^3*x4+(-1)*x2*x3^3*x4*x3+(1)*x2*x3^4*x4, 
  (1)*x3*x2*x3*x4*x2*x1+(-1)*x3*x2*x3*x4*x1*x2+(-1)*x2*x3^2*x4*x2*x1+(
    1)*x2*x3^2*x4*x1*x2, (1)*x3*x2*x3*x4*x3*x1+(-1)*x3*x2*x3*x4*x1*x3+(
    -1)*x2*x3^2*x4*x3*x1+(1)*x2*x3^2*x4*x1*x3, 
  (1)*x3*x2*x3*x4^2*x1+(-1)*x3*x2*x3*x4*x1*x4+(-1)*x2*x3^2*x4^2*x1+(
    1)*x2*x3^2*x4*x1*x4, (1)*x3*x2*x3*x4*x3*x2+(-1)*x3*x2*x3*x4*x2*x3+(
    -1)*x2*x3^2*x4*x3*x2+(1)*x2*x3^2*x4*x2*x3, 
  (1)*x3*x2*x3*x4^2*x2+(-1)*x3*x2*x3*x4*x2*x4+(-1)*x2*x3^2*x4^2*x2+(
    1)*x2*x3^2*x4*x2*x4, (1)*x3*x2*x3*x4^2*x3+(-1)*x3*x2*(x3*x4)^2+(
    -1)*x2*x3^2*x4^2*x3+(1)*x2*x3*(x3*x4)^2, 
  (1)*x3*x2*x4*x1*x2*x1+(-1)*x3*x2*x4*x1^2*x2+(-1)*x2*x3*x4*x1*x2*x1+(
    1)*x2*x3*x4*x1^2*x2, (1)*x3*x2*x4*x1*x3*x1+(-1)*x3*x2*x4*x1^2*x3+(
    -1)*x2*x3*x4*x1*x3*x1+(1)*x2*x3*x4*x1^2*x3, 
  (1)*x3*x2*(x4*x1)^2+(-1)*x3*x2*x4*x1^2*x4+(-1)*x2*x3*(x4*x1)^2+(
    1)*x2*x3*x4*x1^2*x4, (1)*x3*x2*x4*x1*x3*x2+(-1)*x3*x2*x4*x1*x2*x3+(
    -1)*x2*x3*x4*x1*x3*x2+(1)*x2*x3*x4*x1*x2*x3, 
  (1)*x3*x2*x4*x1*x4*x2+(-1)*x3*x2*x4*x1*x2*x4+(-1)*x2*x3*x4*x1*x4*x2+(
    1)*x2*x3*x4*x1*x2*x4, (1)*x3*x2*x4*x1*x4*x3+(-1)*x3*x2*x4*x1*x3*x4+(
    -1)*x2*x3*x4*x1*x4*x3+(1)*x2*x3*x4*x1*x3*x4, 
  (1)*x3*x2*x4*x2^2*x1+(-1)*x3*x2*x4*x2*x1*x2+(-1)*x2*x3*x4*x2^2*x1+(
    1)*x2*x3*x4*x2*x1*x2, (1)*x3*x2*x4*x2*x3*x1+(-1)*x3*x2*x4*x2*x1*x3+(
    -1)*x2*x3*x4*x2*x3*x1+(1)*x2*x3*x4*x2*x1*x3, 
  (1)*x3*(x2*x4)^2*x1+(-1)*x3*x2*x4*x2*x1*x4+(-1)*x2*x3*x4*x2*x4*x1+(
    1)*x2*x3*x4*x2*x1*x4, (1)*x3*x2*x4*x2*x3*x2+(-1)*x3*x2*x4*x2^2*x3+(
    -1)*x2*x3*x4*x2*x3*x2+(1)*x2*x3*x4*x2^2*x3, 
  (1)*x3*(x2*x4)^2*x2+(-1)*x3*x2*x4*x2^2*x4+(-1)*x2*x3*(x4*x2)^2+(
    1)*x2*x3*x4*x2^2*x4, (1)*x3*(x2*x4)^2*x3+(-1)*x3*x2*x4*x2*x3*x4+(
    -1)*x2*x3*x4*x2*x4*x3+(1)*(x2*x3*x4)^2, 
  (1)*x3*x2*x4*x3*x2*x1+(-1)*x3*x2*x4*x3*x1*x2+(-1)*x2*x3*x4*x3*x2*x1+(
    1)*x2*x3*x4*x3*x1*x2, (1)*x3*x2*x4*x3^2*x1+(-1)*x3*x2*x4*x3*x1*x3+(
    -1)*x2*x3*x4*x3^2*x1+(1)*x2*x3*x4*x3*x1*x3, 
  (1)*x3*x2*x4*x3*x4*x1+(-1)*x3*x2*x4*x3*x1*x4+(-1)*x2*(x3*x4)^2*x1+(
    1)*x2*x3*x4*x3*x1*x4, (1)*x3*x2*x4*x3^2*x2+(-1)*x3*x2*x4*x3*x2*x3+(
    -1)*x2*x3*x4*x3^2*x2+(1)*x2*x3*x4*x3*x2*x3, 
  (1)*x3*x2*x4*x3*x4*x2+(-1)*(x3*x2*x4)^2+(-1)*x2*(x3*x4)^2*x2+(
    1)*x2*x3*x4*x3*x2*x4, (1)*x3*x2*(x4*x3)^2+(-1)*x3*x2*x4*x3^2*x4+(
    -1)*x2*(x3*x4)^2*x3+(1)*x2*x3*x4*x3^2*x4, 
  (1)*x3*x2*x4^2*x2*x1+(-1)*x3*x2*x4^2*x1*x2+(-1)*x2*x3*x4^2*x2*x1+(
    1)*x2*x3*x4^2*x1*x2, (1)*x3*x2*x4^2*x3*x1+(-1)*x3*x2*x4^2*x1*x3+(
    -1)*x2*x3*x4^2*x3*x1+(1)*x2*x3*x4^2*x1*x3, 
  (1)*x3*x2*x4^3*x1+(-1)*x3*x2*x4^2*x1*x4+(-1)*x2*x3*x4^3*x1+(
    1)*x2*x3*x4^2*x1*x4, (1)*x3*x2*x4^2*x3*x2+(-1)*x3*x2*x4^2*x2*x3+(
    -1)*x2*x3*x4^2*x3*x2+(1)*x2*x3*x4^2*x2*x3, 
  (1)*x3*x2*x4^3*x2+(-1)*x3*x2*x4^2*x2*x4+(-1)*x2*x3*x4^3*x2+(
    1)*x2*x3*x4^2*x2*x4, (1)*x3*x2*x4^3*x3+(-1)*x3*x2*x4^2*x3*x4+(
    -1)*x2*x3*x4^3*x3+(1)*x2*x3*x4^2*x3*x4, 
  (1)*x4*x2*x1^2*x2*x1+(-1)*x4*x2*x1^3*x2+(-1)*x2*x4*x1^2*x2*x1+(
    1)*x2*x4*x1^3*x2, (1)*x4*x2*x1^2*x3*x1+(-1)*x4*x2*x1^3*x3+(
    -1)*x2*x4*x1^2*x3*x1+(1)*x2*x4*x1^3*x3, 
  (1)*x4*x2*x1^2*x4*x1+(-1)*x4*x2*x1^3*x4+(-1)*x2*x4*x1^2*x4*x1+(
    1)*x2*x4*x1^3*x4, (1)*x4*x2*x1^2*x3*x2+(-1)*x4*x2*x1^2*x2*x3+(
    -1)*x2*x4*x1^2*x3*x2+(1)*x2*x4*x1^2*x2*x3, 
  (1)*x4*x2*x1^2*x4*x2+(-1)*x4*x2*x1^2*x2*x4+(-1)*x2*x4*x1^2*x4*x2+(
    1)*x2*x4*x1^2*x2*x4, (1)*x4*x2*x1^2*x4*x3+(-1)*x4*x2*x1^2*x3*x4+(
    -1)*x2*x4*x1^2*x4*x3+(1)*x2*x4*x1^2*x3*x4, 
  (1)*x4*x2*x1*x2^2*x1+(-1)*x4*(x2*x1)^2*x2+(-1)*x2*x4*x1*x2^2*x1+(
    1)*x2*x4*(x1*x2)^2, (1)*x4*x2*x1*x2*x3*x1+(-1)*x4*(x2*x1)^2*x3+(
    -1)*x2*x4*x1*x2*x3*x1+(1)*x2*x4*x1*x2*x1*x3, 
  (1)*x4*x2*x1*x2*x4*x1+(-1)*x4*(x2*x1)^2*x4+(-1)*(x2*x4*x1)^2+(
    1)*x2*x4*x1*x2*x1*x4, (1)*x4*x2*x1*x2*x3*x2+(-1)*x4*x2*x1*x2^2*x3+(
    -1)*x2*x4*x1*x2*x3*x2+(1)*x2*x4*x1*x2^2*x3, 
  (1)*x4*x2*x1*x2*x4*x2+(-1)*x4*x2*x1*x2^2*x4+(-1)*x2*x4*x1*x2*x4*x2+(
    1)*x2*x4*x1*x2^2*x4, (1)*x4*x2*x1*x2*x4*x3+(-1)*x4*x2*x1*x2*x3*x4+(
    -1)*x2*x4*x1*x2*x4*x3+(1)*x2*x4*x1*x2*x3*x4, 
  (1)*x4*x2*x1*x3*x2*x1+(-1)*x4*x2*x1*x3*x1*x2+(-1)*x2*x4*x1*x3*x2*x1+(
    1)*x2*x4*x1*x3*x1*x2, (1)*x4*x2*x1*x3^2*x1+(-1)*x4*x2*(x1*x3)^2+(
    -1)*x2*x4*x1*x3^2*x1+(1)*x2*x4*(x1*x3)^2, 
  (1)*x4*x2*x1*x3*x4*x1+(-1)*x4*x2*x1*x3*x1*x4+(-1)*x2*x4*x1*x3*x4*x1+(
    1)*x2*x4*x1*x3*x1*x4, (1)*x4*x2*x1*x3^2*x2+(-1)*x4*x2*x1*x3*x2*x3+(
    -1)*x2*x4*x1*x3^2*x2+(1)*x2*x4*x1*x3*x2*x3, 
  (1)*x4*x2*x1*x3*x4*x2+(-1)*x4*x2*x1*x3*x2*x4+(-1)*x2*x4*x1*x3*x4*x2+(
    1)*x2*x4*x1*x3*x2*x4, (1)*x4*x2*x1*x3*x4*x3+(-1)*x4*x2*x1*x3^2*x4+(
    -1)*x2*x4*x1*x3*x4*x3+(1)*x2*x4*x1*x3^2*x4, 
  (1)*(x4*x2*x1)^2+(-1)*x4*x2*x1*x4*x1*x2+(-1)*x2*x4*x1*x4*x2*x1+(
    1)*x2*(x4*x1)^2*x2, (1)*x4*x2*x1*x4*x3*x1+(-1)*x4*x2*x1*x4*x1*x3+(
    -1)*x2*x4*x1*x4*x3*x1+(1)*x2*(x4*x1)^2*x3, 
  (1)*x4*x2*x1*x4^2*x1+(-1)*x4*x2*(x1*x4)^2+(-1)*x2*x4*x1*x4^2*x1+(
    1)*x2*(x4*x1)^2*x4, (1)*x4*x2*x1*x4*x3*x2+(-1)*x4*x2*x1*x4*x2*x3+(
    -1)*x2*x4*x1*x4*x3*x2+(1)*x2*x4*x1*x4*x2*x3, 
  (1)*x4*x2*x1*x4^2*x2+(-1)*x4*x2*x1*x4*x2*x4+(-1)*x2*x4*x1*x4^2*x2+(
    1)*x2*x4*x1*x4*x2*x4, (1)*x4*x2*x1*x4^2*x3+(-1)*x4*x2*x1*x4*x3*x4+(
    -1)*x2*x4*x1*x4^2*x3+(1)*x2*x4*x1*x4*x3*x4, 
  (1)*x4*x2*(x2*x1)^2+(-1)*x4*x2^2*x1^2*x2+(-1)*x2*x4*(x2*x1)^2+(
    1)*x2*x4*x2*x1^2*x2, (1)*x4*x2^2*x1*x3*x1+(-1)*x4*x2^2*x1^2*x3+(
    -1)*x2*x4*x2*x1*x3*x1+(1)*x2*x4*x2*x1^2*x3, 
  (1)*x4*x2^2*x1*x4*x1+(-1)*x4*x2^2*x1^2*x4+(-1)*x2*x4*x2*x1*x4*x1+(
    1)*x2*x4*x2*x1^2*x4, (1)*x4*x2^2*x1*x3*x2+(-1)*x4*x2^2*x1*x2*x3+(
    -1)*x2*x4*x2*x1*x3*x2+(1)*x2*x4*x2*x1*x2*x3, 
  (1)*x4*x2^2*x1*x4*x2+(-1)*x4*x2^2*x1*x2*x4+(-1)*x2*x4*x2*x1*x4*x2+(
    1)*x2*x4*x2*x1*x2*x4, (1)*x4*x2^2*x1*x4*x3+(-1)*x4*x2^2*x1*x3*x4+(
    -1)*x2*x4*x2*x1*x4*x3+(1)*x2*x4*x2*x1*x3*x4, 
  (1)*x4*x2^4*x1+(-1)*x4*x2^3*x1*x2+(-1)*x2*x4*x2^3*x1+(1)*x2*x4*x2^2*x1*x2, 
  (1)*x4*x2^3*x3*x1+(-1)*x4*x2^3*x1*x3+(-1)*x2*x4*x2^2*x3*x1+(
    1)*x2*x4*x2^2*x1*x3, (1)*x4*x2^3*x4*x1+(-1)*x4*x2^3*x1*x4+(
    -1)*x2*x4*x2^2*x4*x1+(1)*x2*x4*x2^2*x1*x4, 
  (1)*x4*x2^3*x3*x2+(-1)*x4*x2^4*x3+(-1)*x2*x4*x2^2*x3*x2+(1)*x2*x4*x2^3*x3, 
  (1)*x4*x2^3*x4*x2+(-1)*x4*x2^4*x4+(-1)*(x2*x4*x2)^2+(1)*x2*x4*x2^3*x4, 
  (1)*x4*x2^3*x4*x3+(-1)*x4*x2^3*x3*x4+(-1)*x2*x4*x2^2*x4*x3+(
    1)*x2*x4*x2^2*x3*x4, (1)*x4*x2^2*x3*x2*x1+(-1)*x4*x2^2*x3*x1*x2+(
    -1)*x2*x4*x2*x3*x2*x1+(1)*x2*x4*x2*x3*x1*x2, 
  (1)*x4*x2^2*x3^2*x1+(-1)*x4*x2^2*x3*x1*x3+(-1)*x2*x4*x2*x3^2*x1+(
    1)*x2*x4*x2*x3*x1*x3, (1)*x4*x2^2*x3*x4*x1+(-1)*x4*x2^2*x3*x1*x4+(
    -1)*x2*x4*x2*x3*x4*x1+(1)*x2*x4*x2*x3*x1*x4, 
  (1)*x4*x2^2*x3^2*x2+(-1)*x4*x2*(x2*x3)^2+(-1)*x2*x4*x2*x3^2*x2+(
    1)*x2*x4*(x2*x3)^2, (1)*x4*x2^2*x3*x4*x2+(-1)*x4*x2^2*x3*x2*x4+(
    -1)*x2*x4*x2*x3*x4*x2+(1)*x2*x4*x2*x3*x2*x4, 
  (1)*x4*x2^2*x3*x4*x3+(-1)*x4*x2^2*x3^2*x4+(-1)*x2*x4*x2*x3*x4*x3+(
    1)*x2*x4*x2*x3^2*x4, (1)*x4*x2^2*x4*x2*x1+(-1)*x4*x2^2*x4*x1*x2+(
    -1)*(x2*x4)^2*x2*x1+(1)*(x2*x4)^2*x1*x2, 
  (1)*x4*x2^2*x4*x3*x1+(-1)*x4*x2^2*x4*x1*x3+(-1)*(x2*x4)^2*x3*x1+(
    1)*(x2*x4)^2*x1*x3, (1)*x4*x2^2*x4^2*x1+(-1)*x4*x2^2*x4*x1*x4+(
    -1)*(x2*x4)^2*x4*x1+(1)*(x2*x4)^2*x1*x4, 
  (1)*x4*x2^2*x4*x3*x2+(-1)*x4*x2^2*x4*x2*x3+(-1)*(x2*x4)^2*x3*x2+(
    1)*(x2*x4)^2*x2*x3, (1)*x4*x2^2*x4^2*x2+(-1)*x4*x2*(x2*x4)^2+(
    -1)*(x2*x4)^2*x4*x2+(1)*(x2*x4)^3, 
  (1)*x4*x2^2*x4^2*x3+(-1)*x4*x2^2*x4*x3*x4+(-1)*(x2*x4)^2*x4*x3+(
    1)*(x2*x4)^2*x3*x4, (1)*x4*x2*x3*x1*x2*x1+(-1)*x4*x2*x3*x1^2*x2+(
    -1)*x2*x4*x3*x1*x2*x1+(1)*x2*x4*x3*x1^2*x2, 
  (1)*x4*x2*(x3*x1)^2+(-1)*x4*x2*x3*x1^2*x3+(-1)*x2*x4*(x3*x1)^2+(
    1)*x2*x4*x3*x1^2*x3, (1)*x4*x2*x3*x1*x4*x1+(-1)*x4*x2*x3*x1^2*x4+(
    -1)*x2*x4*x3*x1*x4*x1+(1)*x2*x4*x3*x1^2*x4, 
  (1)*x4*x2*x3*x1*x3*x2+(-1)*x4*x2*x3*x1*x2*x3+(-1)*x2*x4*x3*x1*x3*x2+(
    1)*x2*x4*x3*x1*x2*x3, (1)*x4*x2*x3*x1*x4*x2+(-1)*x4*x2*x3*x1*x2*x4+(
    -1)*x2*x4*x3*x1*x4*x2+(1)*x2*x4*x3*x1*x2*x4, 
  (1)*x4*x2*x3*x1*x4*x3+(-1)*x4*x2*x3*x1*x3*x4+(-1)*x2*x4*x3*x1*x4*x3+(
    1)*x2*x4*x3*x1*x3*x4, (1)*x4*x2*x3*x2^2*x1+(-1)*x4*x2*x3*x2*x1*x2+(
    -1)*x2*x4*x3*x2^2*x1+(1)*x2*x4*x3*x2*x1*x2, 
  (1)*x4*(x2*x3)^2*x1+(-1)*x4*x2*x3*x2*x1*x3+(-1)*x2*x4*x3*x2*x3*x1+(
    1)*x2*x4*x3*x2*x1*x3, (1)*x4*x2*x3*x2*x4*x1+(-1)*x4*x2*x3*x2*x1*x4+(
    -1)*x2*x4*x3*x2*x4*x1+(1)*x2*x4*x3*x2*x1*x4, 
  (1)*x4*(x2*x3)^2*x2+(-1)*x4*x2*x3*x2^2*x3+(-1)*x2*x4*(x3*x2)^2+(
    1)*x2*x4*x3*x2^2*x3, (1)*x4*x2*x3*x2*x4*x2+(-1)*x4*x2*x3*x2^2*x4+(
    -1)*x2*x4*x3*x2*x4*x2+(1)*x2*x4*x3*x2^2*x4, 
  (1)*x4*x2*x3*x2*x4*x3+(-1)*x4*(x2*x3)^2*x4+(-1)*(x2*x4*x3)^2+(
    1)*x2*x4*x3*x2*x3*x4, (1)*x4*x2*x3^2*x2*x1+(-1)*x4*x2*x3^2*x1*x2+(
    -1)*x2*x4*x3^2*x2*x1+(1)*x2*x4*x3^2*x1*x2, 
  (1)*x4*x2*x3^3*x1+(-1)*x4*x2*x3^2*x1*x3+(-1)*x2*x4*x3^3*x1+(
    1)*x2*x4*x3^2*x1*x3, (1)*x4*x2*x3^2*x4*x1+(-1)*x4*x2*x3^2*x1*x4+(
    -1)*x2*x4*x3^2*x4*x1+(1)*x2*x4*x3^2*x1*x4, 
  (1)*x4*x2*x3^3*x2+(-1)*x4*x2*x3^2*x2*x3+(-1)*x2*x4*x3^3*x2+(
    1)*x2*x4*x3^2*x2*x3, (1)*x4*x2*x3^2*x4*x2+(-1)*x4*x2*x3^2*x2*x4+(
    -1)*x2*x4*x3^2*x4*x2+(1)*x2*x4*x3^2*x2*x4, 
  (1)*x4*x2*x3^2*x4*x3+(-1)*x4*x2*x3^3*x4+(-1)*x2*x4*x3^2*x4*x3+(
    1)*x2*x4*x3^3*x4, (1)*x4*x2*x3*x4*x2*x1+(-1)*x4*x2*x3*x4*x1*x2+(
    -1)*x2*x4*x3*x4*x2*x1+(1)*x2*x4*x3*x4*x1*x2, 
  (1)*x4*x2*x3*x4*x3*x1+(-1)*x4*x2*x3*x4*x1*x3+(-1)*x2*(x4*x3)^2*x1+(
    1)*x2*x4*x3*x4*x1*x3, (1)*x4*x2*x3*x4^2*x1+(-1)*x4*x2*x3*x4*x1*x4+(
    -1)*x2*x4*x3*x4^2*x1+(1)*x2*x4*x3*x4*x1*x4, 
  (1)*x4*x2*x3*x4*x3*x2+(-1)*(x4*x2*x3)^2+(-1)*x2*(x4*x3)^2*x2+(
    1)*x2*x4*x3*x4*x2*x3, (1)*x4*x2*x3*x4^2*x2+(-1)*x4*x2*x3*x4*x2*x4+(
    -1)*x2*x4*x3*x4^2*x2+(1)*x2*x4*x3*x4*x2*x4, 
  (1)*x4*x2*x3*x4^2*x3+(-1)*x4*x2*(x3*x4)^2+(-1)*x2*x4*x3*x4^2*x3+(
    1)*x2*(x4*x3)^2*x4, (1)*x4*x2*x4*x1*x2*x1+(-1)*x4*x2*x4*x1^2*x2+(
    -1)*x2*x4^2*x1*x2*x1+(1)*x2*x4^2*x1^2*x2, 
  (1)*x4*x2*x4*x1*x3*x1+(-1)*x4*x2*x4*x1^2*x3+(-1)*x2*x4^2*x1*x3*x1+(
    1)*x2*x4^2*x1^2*x3, (1)*x4*x2*(x4*x1)^2+(-1)*x4*x2*x4*x1^2*x4+(
    -1)*x2*x4*(x4*x1)^2+(1)*x2*x4^2*x1^2*x4, 
  (1)*x4*x2*x4*x1*x3*x2+(-1)*x4*x2*x4*x1*x2*x3+(-1)*x2*x4^2*x1*x3*x2+(
    1)*x2*x4^2*x1*x2*x3, (1)*x4*x2*x4*x1*x4*x2+(-1)*x4*x2*x4*x1*x2*x4+(
    -1)*x2*x4^2*x1*x4*x2+(1)*x2*x4^2*x1*x2*x4, 
  (1)*x4*x2*x4*x1*x4*x3+(-1)*x4*x2*x4*x1*x3*x4+(-1)*x2*x4^2*x1*x4*x3+(
    1)*x2*x4^2*x1*x3*x4, (1)*(x4*x2)^2*x2*x1+(-1)*(x4*x2)^2*x1*x2+(
    -1)*x2*x4^2*x2^2*x1+(1)*x2*x4^2*x2*x1*x2, 
  (1)*(x4*x2)^2*x3*x1+(-1)*(x4*x2)^2*x1*x3+(-1)*x2*x4^2*x2*x3*x1+(
    1)*x2*x4^2*x2*x1*x3, (1)*(x4*x2)^2*x4*x1+(-1)*(x4*x2)^2*x1*x4+(
    -1)*x2*x4^2*x2*x4*x1+(1)*x2*x4^2*x2*x1*x4, 
  (1)*(x4*x2)^2*x3*x2+(-1)*(x4*x2)^2*x2*x3+(-1)*x2*x4^2*x2*x3*x2+(
    1)*x2*x4^2*x2^2*x3, (1)*(x4*x2)^3+(-1)*(x4*x2)^2*x2*x4+(
    -1)*x2*x4*(x4*x2)^2+(1)*x2*x4^2*x2^2*x4, 
  (1)*(x4*x2)^2*x4*x3+(-1)*(x4*x2)^2*x3*x4+(-1)*x2*x4^2*x2*x4*x3+(
    1)*x2*x4^2*x2*x3*x4, (1)*x4*x2*x4*x3*x2*x1+(-1)*x4*x2*x4*x3*x1*x2+(
    -1)*x2*x4^2*x3*x2*x1+(1)*x2*x4^2*x3*x1*x2, 
  (1)*x4*x2*x4*x3^2*x1+(-1)*x4*x2*x4*x3*x1*x3+(-1)*x2*x4^2*x3^2*x1+(
    1)*x2*x4^2*x3*x1*x3, (1)*x4*x2*x4*x3*x4*x1+(-1)*x4*x2*x4*x3*x1*x4+(
    -1)*x2*x4^2*x3*x4*x1+(1)*x2*x4^2*x3*x1*x4, 
  (1)*x4*x2*x4*x3^2*x2+(-1)*x4*x2*x4*x3*x2*x3+(-1)*x2*x4^2*x3^2*x2+(
    1)*x2*x4^2*x3*x2*x3, (1)*x4*x2*x4*x3*x4*x2+(-1)*x4*x2*x4*x3*x2*x4+(
    -1)*x2*x4^2*x3*x4*x2+(1)*x2*x4^2*x3*x2*x4, 
  (1)*x4*x2*(x4*x3)^2+(-1)*x4*x2*x4*x3^2*x4+(-1)*x2*x4*(x4*x3)^2+(
    1)*x2*x4^2*x3^2*x4, (1)*x4*x2*x4^2*x2*x1+(-1)*x4*x2*x4^2*x1*x2+(
    -1)*x2*x4^3*x2*x1+(1)*x2*x4^3*x1*x2, 
  (1)*x4*x2*x4^2*x3*x1+(-1)*x4*x2*x4^2*x1*x3+(-1)*x2*x4^3*x3*x1+(
    1)*x2*x4^3*x1*x3, (1)*x4*x2*x4^3*x1+(-1)*x4*x2*x4^2*x1*x4+(
    -1)*x2*x4^4*x1+(1)*x2*x4^3*x1*x4, 
  (1)*x4*x2*x4^2*x3*x2+(-1)*x4*x2*x4^2*x2*x3+(-1)*x2*x4^3*x3*x2+(
    1)*x2*x4^3*x2*x3, (1)*x4*x2*x4^3*x2+(-1)*(x4*x2*x4)^2+(-1)*x2*x4^4*x2+(
    1)*x2*x4^3*x2*x4, (1)*x4*x2*x4^3*x3+(-1)*x4*x2*x4^2*x3*x4+(
    -1)*x2*x4^4*x3+(1)*x2*x4^3*x3*x4, 
  (1)*x4*x3*x1^2*x2*x1+(-1)*x4*x3*x1^3*x2+(-1)*x3*x4*x1^2*x2*x1+(
    1)*x3*x4*x1^3*x2, (1)*x4*x3*x1^2*x3*x1+(-1)*x4*x3*x1^3*x3+(
    -1)*x3*x4*x1^2*x3*x1+(1)*x3*x4*x1^3*x3, 
  (1)*x4*x3*x1^2*x4*x1+(-1)*x4*x3*x1^3*x4+(-1)*x3*x4*x1^2*x4*x1+(
    1)*x3*x4*x1^3*x4, (1)*x4*x3*x1^2*x3*x2+(-1)*x4*x3*x1^2*x2*x3+(
    -1)*x3*x4*x1^2*x3*x2+(1)*x3*x4*x1^2*x2*x3, 
  (1)*x4*x3*x1^2*x4*x2+(-1)*x4*x3*x1^2*x2*x4+(-1)*x3*x4*x1^2*x4*x2+(
    1)*x3*x4*x1^2*x2*x4, (1)*x4*x3*x1^2*x4*x3+(-1)*x4*x3*x1^2*x3*x4+(
[...]
  [ 
      [ [ 4, 3, 3, 4, 4, 4, 2 ], [ 4, 3, 3, 4, 4, 2, 4 ], 
          [ 3, 4, 3, 4, 4, 4, 2 ], [ 3, 4, 3, 4, 4, 2, 4 ] ], 
      [ 1, -1, -1, 1 ] ], 
  [ 
      [ [ 4, 3, 3, 4, 4, 4, 3 ], [ 4, 3, 3, 4, 4, 3, 4 ], 
          [ 3, 4, 3, 4, 4, 4, 3 ], [ 3, 4, 3, 4, 4, 3, 4 ] ], 
      [ 1, -1, -1, 1 ] ], 
  [ 
      [ [ 4, 3, 4, 4, 4, 4, 1 ], [ 4, 3, 4, 4, 4, 1, 4 ], 
          [ 3, 4, 4, 4, 4, 4, 1 ], [ 3, 4, 4, 4, 4, 1, 4 ] ], 
      [ 1, -1, -1, 1 ] ], 
  [ 
      [ [ 4, 3, 4, 4, 4, 4, 2 ], [ 4, 3, 4, 4, 4, 2, 4 ], 
          [ 3, 4, 4, 4, 4, 4, 2 ], [ 3, 4, 4, 4, 4, 2, 4 ] ], 
      [ 1, -1, -1, 1 ] ], 
  [ 
      [ [ 4, 3, 4, 4, 4, 4, 3 ], [ 4, 3, 4, 4, 4, 3, 4 ], 
          [ 3, 4, 4, 4, 4, 4, 3 ], [ 3, 4, 4, 4, 4, 3, 4 ] ], 
      [ 1, -1, -1, 1 ] ] ]
gap> gap> =====Solution Begin=====
gap>  x3x4x3x4 - x3x4^2x3 - x4x3^2x4 + x4x3x4x3 
 x3x4x2x4 - x3x4^2x2 - x4x3x2x4 + x4x3x4x2 
 x3x4x2x3 - x3x4x3x2 - x4x3x2x3 + x4x3^2x2 
 x3x4x1x4 - x3x4^2x1 - x4x3x1x4 + x4x3x4x1 
 x3x4x1x3 - x3x4x3x1 - x4x3x1x3 + x4x3^2x1 
 x3x4x1x2 - x3x4x2x1 - x4x3x1x2 + x4x3x2x1 
 x2x4x3x4 - x2x4^2x3 - x4x2x3x4 + x4x2x4x3 
 x2x4x2x4 - x2x4^2x2 - x4x2^2x4 + x4x2x4x2 
 x2x4x2x3 - x2x4x3x2 - x4x2^2x3 + x4x2x3x2 
 x2x4x1x4 - x2x4^2x1 - x4x2x1x4 + x4x2x4x1 
 x2x4x1x3 - x2x4x3x1 - x4x2x1x3 + x4x2x3x1 
 x2x4x1x2 - x2x4x2x1 - x4x2x1x2 + x4x2^2x1 
 x2x3^2x4 - x2x3x4x3 - x3x2x3x4 + x3x2x4x3 
 x2x3x2x4 - x2x3x4x2 - x3x2^2x4 + x3x2x4x2 
 x2x3x2x3 - x2x3^2x2 - x3x2^2x3 + x3x2x3x2 
 x2x3x1x4 - x2x3x4x1 - x3x2x1x4 + x3x2x4x1 
 x2x3x1x3 - x2x3^2x1 - x3x2x1x3 + x3x2x3x1 
 x2x3x1x2 - x2x3x2x1 - x3x2x1x2 + x3x2^2x1 
 x1x4x3x4 - x1x4^2x3 - x4x1x3x4 + x4x1x4x3 
 x1x4x2x4 - x1x4^2x2 - x4x1x2x4 + x4x1x4x2 
 x1x4x2x3 - x1x4x3x2 - x4x1x2x3 + x4x1x3x2 
 x1x4x1x4 - x1x4^2x1 - x4x1^2x4 + x4x1x4x1 
 x1x4x1x3 - x1x4x3x1 - x4x1^2x3 + x4x1x3x1 
 x1x4x1x2 - x1x4x2x1 - x4x1^2x2 + x4x1x2x1 
 x1x3^2x4 - x1x3x4x3 - x3x1x3x4 + x3x1x4x3 
 x1x3x2x4 - x1x3x4x2 - x3x1x2x4 + x3x1x4x2 
 x1x3x2x3 - x1x3^2x2 - x3x1x2x3 + x3x1x3x2 
 x1x3x1x4 - x1x3x4x1 - x3x1^2x4 + x3x1x4x1 
 x1x3x1x3 - x1x3^2x1 - x3x1^2x3 + x3x1x3x1 
 x1x3x1x2 - x1x3x2x1 - x3x1^2x2 + x3x1x2x1 
 x1x2x3x4 - x1x2x4x3 - x2x1x3x4 + x2x1x4x3 
 x1x2^2x4 - x1x2x4x2 - x2x1x2x4 + x2x1x4x2 
 x1x2^2x3 - x1x2x3x2 - x2x1x2x3 + x2x1x3x2 
 x1x2x1x4 - x1x2x4x1 - x2x1^2x4 + x2x1x4x1 
 x1x2x1x3 - x1x2x3x1 - x2x1^2x3 + x2x1x3x1 
 x1x2x1x2 - x1x2^2x1 - x2x1^2x2 + x2x1x2x1 
 x3x4^2x3x4 - x3x4^3x3 - x4x3x4x3x4 + x4x3x4^2x3 
 x3x4^2x2x4 - x3x4^3x2 - x4x3x4x2x4 + x4x3x4^2x2 
 x3x4^2x2x3 - x3x4^2x3x2 - x4x3x4x2x3 + x4x3x4x3x2 
 x3x4^2x1x4 - x3x4^3x1 - x4x3x4x1x4 + x4x3x4^2x1 
 x3x4^2x1x3 - x3x4^2x3x1 - x4x3x4x1x3 + x4x3x4x3x1 
 x3x4^2x1x2 - x3x4^2x2x1 - x4x3x4x1x2 + x4x3x4x2x1 
 x3x4x3^2x4 - x3x4x3x4x3 - x4x3^3x4 + x4x3^2x4x3 
 x3x4x3x2x4 - x3x4x3x4x2 - x4x3^2x2x4 + x4x3^2x4x2 
 x3x4x3x2x3 - x3x4x3^2x2 - x4x3^2x2x3 + x4x3^3x2 
 x3x4x3x1x4 - x3x4x3x4x1 - x4x3^2x1x4 + x4x3^2x4x1 
 x3x4x3x1x3 - x3x4x3^2x1 - x4x3^2x1x3 + x4x3^3x1 
 x3x4x3x1x2 - x3x4x3x2x1 - x4x3^2x1x2 + x4x3^2x2x1 
 x3x4x2^2x4 - x3x4x2x4x2 - x4x3x2^2x4 + x4x3x2x4x2 
 x3x4x2^2x3 - x3x4x2x3x2 - x4x3x2^2x3 + x4x3x2x3x2 
 x3x4x2x1x4 - x3x4x2x4x1 - x4x3x2x1x4 + x4x3x2x4x1 
 x3x4x2x1x3 - x3x4x2x3x1 - x4x3x2x1x3 + x4x3x2x3x1 
 x3x4x2x1x2 - x3x4x2^2x1 - x4x3x2x1x2 + x4x3x2^2x1 
 x3x4x1^2x4 - x3x4x1x4x1 - x4x3x1^2x4 + x4x3x1x4x1 
 x3x4x1^2x3 - x3x4x1x3x1 - x4x3x1^2x3 + x4x3x1x3x1 
 x3x4x1^2x2 - x3x4x1x2x1 - x4x3x1^2x2 + x4x3x1x2x1 
 x2x4^2x3x4 - x2x4^3x3 - x4x2x4x3x4 + x4x2x4^2x3 
 x2x4^2x2x4 - x2x4^3x2 - x4x2x4x2x4 + x4x2x4^2x2 
 x2x4^2x2x3 - x2x4^2x3x2 - x4x2x4x2x3 + x4x2x4x3x2 
 x2x4^2x1x4 - x2x4^3x1 - x4x2x4x1x4 + x4x2x4^2x1 
 x2x4^2x1x3 - x2x4^2x3x1 - x4x2x4x1x3 + x4x2x4x3x1 
 x2x4^2x1x2 - x2x4^2x2x1 - x4x2x4x1x2 + x4x2x4x2x1 
 x2x4x3^2x4 - x2x4x3x4x3 - x4x2x3^2x4 + x4x2x3x4x3 
 x2x4x3x2x4 - x2x4x3x4x2 - x4x2x3x2x4 + x4x2x3x4x2 
 x2x4x3x2x3 - x2x4x3^2x2 - x4x2x3x2x3 + x4x2x3^2x2 
 x2x4x3x1x4 - x2x4x3x4x1 - x4x2x3x1x4 + x4x2x3x4x1 
 x2x4x3x1x3 - x2x4x3^2x1 - x4x2x3x1x3 + x4x2x3^2x1 
 x2x4x3x1x2 - x2x4x3x2x1 - x4x2x3x1x2 + x4x2x3x2x1 
 x2x4x2^2x4 - x2x4x2x4x2 - x4x2^3x4 + x4x2^2x4x2 
 x2x4x2^2x3 - x2x4x2x3x2 - x4x2^3x3 + x4x2^2x3x2 
 x2x4x2x1x4 - x2x4x2x4x1 - x4x2^2x1x4 + x4x2^2x4x1 
 x2x4x2x1x3 - x2x4x2x3x1 - x4x2^2x1x3 + x4x2^2x3x1 
 x2x4x2x1x2 - x2x4x2^2x1 - x4x2^2x1x2 + x4x2^3x1 
 x2x4x1^2x4 - x2x4x1x4x1 - x4x2x1^2x4 + x4x2x1x4x1 
 x2x4x1^2x3 - x2x4x1x3x1 - x4x2x1^2x3 + x4x2x1x3x1 
 x2x4x1^2x2 - x2x4x1x2x1 - x4x2x1^2x2 + x4x2x1x2x1 
 x2x3^3x4 - x2x3^2x4x3 - x3x2x3^2x4 + x3x2x3x4x3 
 x2x3^2x2x4 - x2x3^2x4x2 - x3x2x3x2x4 + x3x2x3x4x2 
 x2x3^2x2x3 - x2x3^3x2 - x3x2x3x2x3 + x3x2x3^2x2 
 x2x3^2x1x4 - x2x3^2x4x1 - x3x2x3x1x4 + x3x2x3x4x1 
 x2x3^2x1x3 - x2x3^3x1 - x3x2x3x1x3 + x3x2x3^2x1 
 x2x3^2x1x2 - x2x3^2x2x1 - x3x2x3x1x2 + x3x2x3x2x1 
 x2x3x2^2x4 - x2x3x2x4x2 - x3x2^3x4 + x3x2^2x4x2 
 x2x3x2^2x3 - x2x3x2x3x2 - x3x2^3x3 + x3x2^2x3x2 
 x2x3x2x1x4 - x2x3x2x4x1 - x3x2^2x1x4 + x3x2^2x4x1 
 x2x3x2x1x3 - x2x3x2x3x1 - x3x2^2x1x3 + x3x2^2x3x1 
 x2x3x2x1x2 - x2x3x2^2x1 - x3x2^2x1x2 + x3x2^3x1 
 x2x3x1^2x4 - x2x3x1x4x1 - x3x2x1^2x4 + x3x2x1x4x1 
 x2x3x1^2x3 - x2x3x1x3x1 - x3x2x1^2x3 + x3x2x1x3x1 
 x2x3x1^2x2 - x2x3x1x2x1 - x3x2x1^2x2 + x3x2x1x2x1 
 x1x4^2x3x4 - x1x4^3x3 - x4x1x4x3x4 + x4x1x4^2x3 
 x1x4^2x2x4 - x1x4^3x2 - x4x1x4x2x4 + x4x1x4^2x2 
 x1x4^2x2x3 - x1x4^2x3x2 - x4x1x4x2x3 + x4x1x4x3x2 
 x1x4^2x1x4 - x1x4^3x1 - x4x1x4x1x4 + x4x1x4^2x1 
 x1x4^2x1x3 - x1x4^2x3x1 - x4x1x4x1x3 + x4x1x4x3x1 
 x1x4^2x1x2 - x1x4^2x2x1 - x4x1x4x1x2 + x4x1x4x2x1 
 x1x4x3^2x4 - x1x4x3x4x3 - x4x1x3^2x4 + x4x1x3x4x3 
 x1x4x3x2x4 - x1x4x3x4x2 - x4x1x3x2x4 + x4x1x3x4x2 
 x1x4x3x2x3 - x1x4x3^2x2 - x4x1x3x2x3 + x4x1x3^2x2 
 x1x4x3x1x4 - x1x4x3x4x1 - x4x1x3x1x4 + x4x1x3x4x1 
 x1x4x3x1x3 - x1x4x3^2x1 - x4x1x3x1x3 + x4x1x3^2x1 
 x1x4x3x1x2 - x1x4x3x2x1 - x4x1x3x1x2 + x4x1x3x2x1 
 x1x4x2^2x4 - x1x4x2x4x2 - x4x1x2^2x4 + x4x1x2x4x2 
 x1x4x2^2x3 - x1x4x2x3x2 - x4x1x2^2x3 + x4x1x2x3x2 
 x1x4x2x1x4 - x1x4x2x4x1 - x4x1x2x1x4 + x4x1x2x4x1 
 x1x4x2x1x3 - x1x4x2x3x1 - x4x1x2x1x3 + x4x1x2x3x1 
 x1x4x2x1x2 - x1x4x2^2x1 - x4x1x2x1x2 + x4x1x2^2x1 
 x1x4x1^2x4 - x1x4x1x4x1 - x4x1^3x4 + x4x1^2x4x1 
 x1x4x1^2x3 - x1x4x1x3x1 - x4x1^3x3 + x4x1^2x3x1 
 x1x4x1^2x2 - x1x4x1x2x1 - x4x1^3x2 + x4x1^2x2x1 
 x1x3^3x4 - x1x3^2x4x3 - x3x1x3^2x4 + x3x1x3x4x3 
 x1x3^2x2x4 - x1x3^2x4x2 - x3x1x3x2x4 + x3x1x3x4x2 
 x1x3^2x2x3 - x1x3^3x2 - x3x1x3x2x3 + x3x1x3^2x2 
 x1x3^2x1x4 - x1x3^2x4x1 - x3x1x3x1x4 + x3x1x3x4x1 
 x1x3^2x1x3 - x1x3^3x1 - x3x1x3x1x3 + x3x1x3^2x1 
 x1x3^2x1x2 - x1x3^2x2x1 - x3x1x3x1x2 + x3x1x3x2x1 
 x1x3x2^2x4 - x1x3x2x4x2 - x3x1x2^2x4 + x3x1x2x4x2 
 x1x3x2^2x3 - x1x3x2x3x2 - x3x1x2^2x3 + x3x1x2x3x2 
 x1x3x2x1x4 - x1x3x2x4x1 - x3x1x2x1x4 + x3x1x2x4x1 
 x1x3x2x1x3 - x1x3x2x3x1 - x3x1x2x1x3 + x3x1x2x3x1 
 x1x3x2x1x2 - x1x3x2^2x1 - x3x1x2x1x2 + x3x1x2^2x1 
 x1x3x1^2x4 - x1x3x1x4x1 - x3x1^3x4 + x3x1^2x4x1 
 x1x3x1^2x3 - x1x3x1x3x1 - x3x1^3x3 + x3x1^2x3x1 
 x1x3x1^2x2 - x1x3x1x2x1 - x3x1^3x2 + x3x1^2x2x1 
 x1x2^3x4 - x1x2^2x4x2 - x2x1x2^2x4 + x2x1x2x4x2 
 x1x2^3x3 - x1x2^2x3x2 - x2x1x2^2x3 + x2x1x2x3x2 
 x1x2^2x1x4 - x1x2^2x4x1 - x2x1x2x1x4 + x2x1x2x4x1 
 x1x2^2x1x3 - x1x2^2x3x1 - x2x1x2x1x3 + x2x1x2x3x1 
 x1x2^2x1x2 - x1x2^3x1 - x2x1x2x1x2 + x2x1x2^2x1 
 x1x2x1^2x4 - x1x2x1x4x1 - x2x1^3x4 + x2x1^2x4x1 
 x1x2x1^2x3 - x1x2x1x3x1 - x2x1^3x3 + x2x1^2x3x1 
 x1x2x1^2x2 - x1x2x1x2x1 - x2x1^3x2 + x2x1^2x2x1 
 x3x4^3x3x4 - x3x4^4x3 - x4x3x4^2x3x4 + x4x3x4^3x3 
 x3x4^3x2x4 - x3x4^4x2 - x4x3x4^2x2x4 + x4x3x4^3x2 
 x3x4^3x2x3 - x3x4^3x3x2 - x4x3x4^2x2x3 + x4x3x4^2x3x2 
 x3x4^3x1x4 - x3x4^4x1 - x4x3x4^2x1x4 + x4x3x4^3x1 
 x3x4^3x1x3 - x3x4^3x3x1 - x4x3x4^2x1x3 + x4x3x4^2x3x1 
 x3x4^3x1x2 - x3x4^3x2x1 - x4x3x4^2x1x2 + x4x3x4^2x2x1 
 x3x4^2x3^2x4 - x3x4^2x3x4x3 - x4x3x4x3^2x4 + x4x3x4x3x4x3 
 x3x4^2x3x2x4 - x3x4^2x3x4x2 - x4x3x4x3x2x4 + x4x3x4x3x4x2 
 x3x4^2x3x2x3 - x3x4^2x3^2x2 - x4x3x4x3x2x3 + x4x3x4x3^2x2 
 x3x4^2x3x1x4 - x3x4^2x3x4x1 - x4x3x4x3x1x4 + x4x3x4x3x4x1 
 x3x4^2x3x1x3 - x3x4^2x3^2x1 - x4x3x4x3x1x3 + x4x3x4x3^2x1 
 x3x4^2x3x1x2 - x3x4^2x3x2x1 - x4x3x4x3x1x2 + x4x3x4x3x2x1 
 x3x4^2x2^2x4 - x3x4^2x2x4x2 - x4x3x4x2^2x4 + x4x3x4x2x4x2 
 x3x4^2x2^2x3 - x3x4^2x2x3x2 - x4x3x4x2^2x3 + x4x3x4x2x3x2 
 x3x4^2x2x1x4 - x3x4^2x2x4x1 - x4x3x4x2x1x4 + x4x3x4x2x4x1 
 x3x4^2x2x1x3 - x3x4^2x2x3x1 - x4x3x4x2x1x3 + x4x3x4x2x3x1 
 x3x4^2x2x1x2 - x3x4^2x2^2x1 - x4x3x4x2x1x2 + x4x3x4x2^2x1 
 x3x4^2x1^2x4 - x3x4^2x1x4x1 - x4x3x4x1^2x4 + x4x3x4x1x4x1 
 x3x4^2x1^2x3 - x3x4^2x1x3x1 - x4x3x4x1^2x3 + x4x3x4x1x3x1 
 x3x4^2x1^2x2 - x3x4^2x1x2x1 - x4x3x4x1^2x2 + x4x3x4x1x2x1 
 x3x4x3^3x4 - x3x4x3^2x4x3 - x4x3^4x4 + x4x3^3x4x3 
 x3x4x3^2x2x4 - x3x4x3^2x4x2 - x4x3^3x2x4 + x4x3^3x4x2 
 x3x4x3^2x2x3 - x3x4x3^3x2 - x4x3^3x2x3 + x4x3^4x2 
 x3x4x3^2x1x4 - x3x4x3^2x4x1 - x4x3^3x1x4 + x4x3^3x4x1 
 x3x4x3^2x1x3 - x3x4x3^3x1 - x4x3^3x1x3 + x4x3^4x1 
 x3x4x3^2x1x2 - x3x4x3^2x2x1 - x4x3^3x1x2 + x4x3^3x2x1 
 x3x4x3x2^2x4 - x3x4x3x2x4x2 - x4x3^2x2^2x4 + x4x3^2x2x4x2 
 x3x4x3x2^2x3 - x3x4x3x2x3x2 - x4x3^2x2^2x3 + x4x3^2x2x3x2 
 x3x4x3x2x1x4 - x3x4x3x2x4x1 - x4x3^2x2x1x4 + x4x3^2x2x4x1 
 x3x4x3x2x1x3 - x3x4x3x2x3x1 - x4x3^2x2x1x3 + x4x3^2x2x3x1 
 x3x4x3x2x1x2 - x3x4x3x2^2x1 - x4x3^2x2x1x2 + x4x3^2x2^2x1 
 x3x4x3x1^2x4 - x3x4x3x1x4x1 - x4x3^2x1^2x4 + x4x3^2x1x4x1 
 x3x4x3x1^2x3 - x3x4x3x1x3x1 - x4x3^2x1^2x3 + x4x3^2x1x3x1 
 x3x4x3x1^2x2 - x3x4x3x1x2x1 - x4x3^2x1^2x2 + x4x3^2x1x2x1 
 x3x4x2^3x4 - x3x4x2^2x4x2 - x4x3x2^3x4 + x4x3x2^2x4x2 
 x3x4x2^3x3 - x3x4x2^2x3x2 - x4x3x2^3x3 + x4x3x2^2x3x2 
 x3x4x2^2x1x4 - x3x4x2^2x4x1 - x4x3x2^2x1x4 + x4x3x2^2x4x1 
 x3x4x2^2x1x3 - x3x4x2^2x3x1 - x4x3x2^2x1x3 + x4x3x2^2x3x1 
 x3x4x2^2x1x2 - x3x4x2^3x1 - x4x3x2^2x1x2 + x4x3x2^3x1 
 x3x4x2x1^2x4 - x3x4x2x1x4x1 - x4x3x2x1^2x4 + x4x3x2x1x4x1 
 x3x4x2x1^2x3 - x3x4x2x1x3x1 - x4x3x2x1^2x3 + x4x3x2x1x3x1 
 x3x4x2x1^2x2 - x3x4x2x1x2x1 - x4x3x2x1^2x2 + x4x3x2x1x2x1 
 x3x4x1^3x4 - x3x4x1^2x4x1 - x4x3x1^3x4 + x4x3x1^2x4x1 
 x3x4x1^3x3 - x3x4x1^2x3x1 - x4x3x1^3x3 + x4x3x1^2x3x1 
 x3x4x1^3x2 - x3x4x1^2x2x1 - x4x3x1^3x2 + x4x3x1^2x2x1 
 x2x4^3x3x4 - x2x4^4x3 - x4x2x4^2x3x4 + x4x2x4^3x3 
 x2x4^3x2x4 - x2x4^4x2 - x4x2x4^2x2x4 + x4x2x4^3x2 
 x2x4^3x2x3 - x2x4^3x3x2 - x4x2x4^2x2x3 + x4x2x4^2x3x2 
 x2x4^3x1x4 - x2x4^4x1 - x4x2x4^2x1x4 + x4x2x4^3x1 
 x2x4^3x1x3 - x2x4^3x3x1 - x4x2x4^2x1x3 + x4x2x4^2x3x1 
 x2x4^3x1x2 - x2x4^3x2x1 - x4x2x4^2x1x2 + x4x2x4^2x2x1 
 x2x4^2x3^2x4 - x2x4^2x3x4x3 - x4x2x4x3^2x4 + x4x2x4x3x4x3 
 x2x4^2x3x2x4 - x2x4^2x3x4x2 - x4x2x4x3x2x4 + x4x2x4x3x4x2 
 x2x4^2x3x2x3 - x2x4^2x3^2x2 - x4x2x4x3x2x3 + x4x2x4x3^2x2 
 x2x4^2x3x1x4 - x2x4^2x3x4x1 - x4x2x4x3x1x4 + x4x2x4x3x4x1 
 x2x4^2x3x1x3 - x2x4^2x3^2x1 - x4x2x4x3x1x3 + x4x2x4x3^2x1 
 x2x4^2x3x1x2 - x2x4^2x3x2x1 - x4x2x4x3x1x2 + x4x2x4x3x2x1 
 x2x4^2x2^2x4 - x2x4^2x2x4x2 - x4x2x4x2^2x4 + x4x2x4x2x4x2 
 x2x4^2x2^2x3 - x2x4^2x2x3x2 - x4x2x4x2^2x3 + x4x2x4x2x3x2 
 x2x4^2x2x1x4 - x2x4^2x2x4x1 - x4x2x4x2x1x4 + x4x2x4x2x4x1 
 x2x4^2x2x1x3 - x2x4^2x2x3x1 - x4x2x4x2x1x3 + x4x2x4x2x3x1 
 x2x4^2x2x1x2 - x2x4^2x2^2x1 - x4x2x4x2x1x2 + x4x2x4x2^2x1 
 x2x4^2x1^2x4 - x2x4^2x1x4x1 - x4x2x4x1^2x4 + x4x2x4x1x4x1 
 x2x4^2x1^2x3 - x2x4^2x1x3x1 - x4x2x4x1^2x3 + x4x2x4x1x3x1 
 x2x4^2x1^2x2 - x2x4^2x1x2x1 - x4x2x4x1^2x2 + x4x2x4x1x2x1 
 x2x4x3^3x4 - x2x4x3^2x4x3 - x4x2x3^3x4 + x4x2x3^2x4x3 
 x2x4x3^2x2x4 - x2x4x3^2x4x2 - x4x2x3^2x2x4 + x4x2x3^2x4x2 
 x2x4x3^2x2x3 - x2x4x3^3x2 - x4x2x3^2x2x3 + x4x2x3^3x2 
 x2x4x3^2x1x4 - x2x4x3^2x4x1 - x4x2x3^2x1x4 + x4x2x3^2x4x1 
 x2x4x3^2x1x3 - x2x4x3^3x1 - x4x2x3^2x1x3 + x4x2x3^3x1 
 x2x4x3^2x1x2 - x2x4x3^2x2x1 - x4x2x3^2x1x2 + x4x2x3^2x2x1 
 x2x4x3x2^2x4 - x2x4x3x2x4x2 - x4x2x3x2^2x4 + x4x2x3x2x4x2 
 x2x4x3x2^2x3 - x2x4x3x2x3x2 - x4x2x3x2^2x3 + x4x2x3x2x3x2 
 x2x4x3x2x1x4 - x2x4x3x2x4x1 - x4x2x3x2x1x4 + x4x2x3x2x4x1 
 x2x4x3x2x1x3 - x2x4x3x2x3x1 - x4x2x3x2x1x3 + x4x2x3x2x3x1 
 x2x4x3x2x1x2 - x2x4x3x2^2x1 - x4x2x3x2x1x2 + x4x2x3x2^2x1 
 x2x4x3x1^2x4 - x2x4x3x1x4x1 - x4x2x3x1^2x4 + x4x2x3x1x4x1 
 x2x4x3x1^2x3 - x2x4x3x1x3x1 - x4x2x3x1^2x3 + x4x2x3x1x3x1 
 x2x4x3x1^2x2 - x2x4x3x1x2x1 - x4x2x3x1^2x2 + x4x2x3x1x2x1 
 x2x4x2^3x4 - x2x4x2^2x4x2 - x4x2^4x4 + x4x2^3x4x2 
 x2x4x2^3x3 - x2x4x2^2x3x2 - x4x2^4x3 + x4x2^3x3x2 
 x2x4x2^2x1x4 - x2x4x2^2x4x1 - x4x2^3x1x4 + x4x2^3x4x1 
 x2x4x2^2x1x3 - x2x4x2^2x3x1 - x4x2^3x1x3 + x4x2^3x3x1 
 x2x4x2^2x1x2 - x2x4x2^3x1 - x4x2^3x1x2 + x4x2^4x1 
 x2x4x2x1^2x4 - x2x4x2x1x4x1 - x4x2^2x1^2x4 + x4x2^2x1x4x1 
 x2x4x2x1^2x3 - x2x4x2x1x3x1 - x4x2^2x1^2x3 + x4x2^2x1x3x1 
 x2x4x2x1^2x2 - x2x4x2x1x2x1 - x4x2^2x1^2x2 + x4x2^2x1x2x1 
 x2x4x1^3x4 - x2x4x1^2x4x1 - x4x2x1^3x4 + x4x2x1^2x4x1 
 x2x4x1^3x3 - x2x4x1^2x3x1 - x4x2x1^3x3 + x4x2x1^2x3x1 
 x2x4x1^3x2 - x2x4x1^2x2x1 - x4x2x1^3x2 + x4x2x1^2x2x1 
 x2x3^4x4 - x2x3^3x4x3 - x3x2x3^3x4 + x3x2x3^2x4x3 
 x2x3^3x2x4 - x2x3^3x4x2 - x3x2x3^2x2x4 + x3x2x3^2x4x2 
 x2x3^3x2x3 - x2x3^4x2 - x3x2x3^2x2x3 + x3x2x3^3x2 
 x2x3^3x1x4 - x2x3^3x4x1 - x3x2x3^2x1x4 + x3x2x3^2x4x1 
 x2x3^3x1x3 - x2x3^4x1 - x3x2x3^2x1x3 + x3x2x3^3x1 
 x2x3^3x1x2 - x2x3^3x2x1 - x3x2x3^2x1x2 + x3x2x3^2x2x1 
 x2x3^2x2^2x4 - x2x3^2x2x4x2 - x3x2x3x2^2x4 + x3x2x3x2x4x2 
 x2x3^2x2^2x3 - x2x3^2x2x3x2 - x3x2x3x2^2x3 + x3x2x3x2x3x2 
 x2x3^2x2x1x4 - x2x3^2x2x4x1 - x3x2x3x2x1x4 + x3x2x3x2x4x1 
 x2x3^2x2x1x3 - x2x3^2x2x3x1 - x3x2x3x2x1x3 + x3x2x3x2x3x1 
 x2x3^2x2x1x2 - x2x3^2x2^2x1 - x3x2x3x2x1x2 + x3x2x3x2^2x1 
 x2x3^2x1^2x4 - x2x3^2x1x4x1 - x3x2x3x1^2x4 + x3x2x3x1x4x1 
 x2x3^2x1^2x3 - x2x3^2x1x3x1 - x3x2x3x1^2x3 + x3x2x3x1x3x1 
 x2x3^2x1^2x2 - x2x3^2x1x2x1 - x3x2x3x1^2x2 + x3x2x3x1x2x1 
 x2x3x2^3x4 - x2x3x2^2x4x2 - x3x2^4x4 + x3x2^3x4x2 
 x2x3x2^3x3 - x2x3x2^2x3x2 - x3x2^4x3 + x3x2^3x3x2 
 x2x3x2^2x1x4 - x2x3x2^2x4x1 - x3x2^3x1x4 + x3x2^3x4x1 
 x2x3x2^2x1x3 - x2x3x2^2x3x1 - x3x2^3x1x3 + x3x2^3x3x1 
 x2x3x2^2x1x2 - x2x3x2^3x1 - x3x2^3x1x2 + x3x2^4x1 
 x2x3x2x1^2x4 - x2x3x2x1x4x1 - x3x2^2x1^2x4 + x3x2^2x1x4x1 
 x2x3x2x1^2x3 - x2x3x2x1x3x1 - x3x2^2x1^2x3 + x3x2^2x1x3x1 
 x2x3x2x1^2x2 - x2x3x2x1x2x1 - x3x2^2x1^2x2 + x3x2^2x1x2x1 
 x2x3x1^3x4 - x2x3x1^2x4x1 - x3x2x1^3x4 + x3x2x1^2x4x1 
 x2x3x1^3x3 - x2x3x1^2x3x1 - x3x2x1^3x3 + x3x2x1^2x3x1 
 x2x3x1^3x2 - x2x3x1^2x2x1 - x3x2x1^3x2 + x3x2x1^2x2x1 
 x1x4^3x3x4 - x1x4^4x3 - x4x1x4^2x3x4 + x4x1x4^3x3 
 x1x4^3x2x4 - x1x4^4x2 - x4x1x4^2x2x4 + x4x1x4^3x2 
 x1x4^3x2x3 - x1x4^3x3x2 - x4x1x4^2x2x3 + x4x1x4^2x3x2 
 x1x4^3x1x4 - x1x4^4x1 - x4x1x4^2x1x4 + x4x1x4^3x1 
 x1x4^3x1x3 - x1x4^3x3x1 - x4x1x4^2x1x3 + x4x1x4^2x3x1 
 x1x4^3x1x2 - x1x4^3x2x1 - x4x1x4^2x1x2 + x4x1x4^2x2x1 
 x1x4^2x3^2x4 - x1x4^2x3x4x3 - x4x1x4x3^2x4 + x4x1x4x3x4x3 
 x1x4^2x3x2x4 - x1x4^2x3x4x2 - x4x1x4x3x2x4 + x4x1x4x3x4x2 
 x1x4^2x3x2x3 - x1x4^2x3^2x2 - x4x1x4x3x2x3 + x4x1x4x3^2x2 
 x1x4^2x3x1x4 - x1x4^2x3x4x1 - x4x1x4x3x1x4 + x4x1x4x3x4x1 
 x1x4^2x3x1x3 - x1x4^2x3^2x1 - x4x1x4x3x1x3 + x4x1x4x3^2x1 
 x1x4^2x3x1x2 - x1x4^2x3x2x1 - x4x1x4x3x1x2 + x4x1x4x3x2x1 
 x1x4^2x2^2x4 - x1x4^2x2x4x2 - x4x1x4x2^2x4 + x4x1x4x2x4x2 
 x1x4^2x2^2x3 - x1x4^2x2x3x2 - x4x1x4x2^2x3 + x4x1x4x2x3x2 
 x1x4^2x2x1x4 - x1x4^2x2x4x1 - x4x1x4x2x1x4 + x4x1x4x2x4x1 
 x1x4^2x2x1x3 - x1x4^2x2x3x1 - x4x1x4x2x1x3 + x4x1x4x2x3x1 
 x1x4^2x2x1x2 - x1x4^2x2^2x1 - x4x1x4x2x1x2 + x4x1x4x2^2x1 
 x1x4^2x1^2x4 - x1x4^2x1x4x1 - x4x1x4x1^2x4 + x4x1x4x1x4x1 
 x1x4^2x1^2x3 - x1x4^2x1x3x1 - x4x1x4x1^2x3 + x4x1x4x1x3x1 
 x1x4^2x1^2x2 - x1x4^2x1x2x1 - x4x1x4x1^2x2 + x4x1x4x1x2x1 
 x1x4x3^3x4 - x1x4x3^2x4x3 - x4x1x3^3x4 + x4x1x3^2x4x3 
 x1x4x3^2x2x4 - x1x4x3^2x4x2 - x4x1x3^2x2x4 + x4x1x3^2x4x2 
 x1x4x3^2x2x3 - x1x4x3^3x2 - x4x1x3^2x2x3 + x4x1x3^3x2 
 x1x4x3^2x1x4 - x1x4x3^2x4x1 - x4x1x3^2x1x4 + x4x1x3^2x4x1 
 x1x4x3^2x1x3 - x1x4x3^3x1 - x4x1x3^2x1x3 + x4x1x3^3x1 
 x1x4x3^2x1x2 - x1x4x3^2x2x1 - x4x1x3^2x1x2 + x4x1x3^2x2x1 
 x1x4x3x2^2x4 - x1x4x3x2x4x2 - x4x1x3x2^2x4 + x4x1x3x2x4x2 
 x1x4x3x2^2x3 - x1x4x3x2x3x2 - x4x1x3x2^2x3 + x4x1x3x2x3x2 
 x1x4x3x2x1x4 - x1x4x3x2x4x1 - x4x1x3x2x1x4 + x4x1x3x2x4x1 
 x1x4x3x2x1x3 - x1x4x3x2x3x1 - x4x1x3x2x1x3 + x4x1x3x2x3x1 
 x1x4x3x2x1x2 - x1x4x3x2^2x1 - x4x1x3x2x1x2 + x4x1x3x2^2x1 
 x1x4x3x1^2x4 - x1x4x3x1x4x1 - x4x1x3x1^2x4 + x4x1x3x1x4x1 
 x1x4x3x1^2x3 - x1x4x3x1x3x1 - x4x1x3x1^2x3 + x4x1x3x1x3x1 
 x1x4x3x1^2x2 - x1x4x3x1x2x1 - x4x1x3x1^2x2 + x4x1x3x1x2x1 
 x1x4x2^3x4 - x1x4x2^2x4x2 - x4x1x2^3x4 + x4x1x2^2x4x2 
 x1x4x2^3x3 - x1x4x2^2x3x2 - x4x1x2^3x3 + x4x1x2^2x3x2 
 x1x4x2^2x1x4 - x1x4x2^2x4x1 - x4x1x2^2x1x4 + x4x1x2^2x4x1 
 x1x4x2^2x1x3 - x1x4x2^2x3x1 - x4x1x2^2x1x3 + x4x1x2^2x3x1 
 x1x4x2^2x1x2 - x1x4x2^3x1 - x4x1x2^2x1x2 + x4x1x2^3x1 
 x1x4x2x1^2x4 - x1x4x2x1x4x1 - x4x1x2x1^2x4 + x4x1x2x1x4x1 
 x1x4x2x1^2x3 - x1x4x2x1x3x1 - x4x1x2x1^2x3 + x4x1x2x1x3x1 
 x1x4x2x1^2x2 - x1x4x2x1x2x1 - x4x1x2x1^2x2 + x4x1x2x1x2x1 
 x1x4x1^3x4 - x1x4x1^2x4x1 - x4x1^4x4 + x4x1^3x4x1 
 x1x4x1^3x3 - x1x4x1^2x3x1 - x4x1^4x3 + x4x1^3x3x1 
 x1x4x1^3x2 - x1x4x1^2x2x1 - x4x1^4x2 + x4x1^3x2x1 
 x1x3^4x4 - x1x3^3x4x3 - x3x1x3^3x4 + x3x1x3^2x4x3 
 x1x3^3x2x4 - x1x3^3x4x2 - x3x1x3^2x2x4 + x3x1x3^2x4x2 
 x1x3^3x2x3 - x1x3^4x2 - x3x1x3^2x2x3 + x3x1x3^3x2 
 x1x3^3x1x4 - x1x3^3x4x1 - x3x1x3^2x1x4 + x3x1x3^2x4x1 
 x1x3^3x1x3 - x1x3^4x1 - x3x1x3^2x1x3 + x3x1x3^3x1 
 x1x3^3x1x2 - x1x3^3x2x1 - x3x1x3^2x1x2 + x3x1x3^2x2x1 
 x1x3^2x2^2x4 - x1x3^2x2x4x2 - x3x1x3x2^2x4 + x3x1x3x2x4x2 
 x1x3^2x2^2x3 - x1x3^2x2x3x2 - x3x1x3x2^2x3 + x3x1x3x2x3x2 
 x1x3^2x2x1x4 - x1x3^2x2x4x1 - x3x1x3x2x1x4 + x3x1x3x2x4x1 
 x1x3^2x2x1x3 - x1x3^2x2x3x1 - x3x1x3x2x1x3 + x3x1x3x2x3x1 
 x1x3^2x2x1x2 - x1x3^2x2^2x1 - x3x1x3x2x1x2 + x3x1x3x2^2x1 
 x1x3^2x1^2x4 - x1x3^2x1x4x1 - x3x1x3x1^2x4 + x3x1x3x1x4x1 
 x1x3^2x1^2x3 - x1x3^2x1x3x1 - x3x1x3x1^2x3 + x3x1x3x1x3x1 
 x1x3^2x1^2x2 - x1x3^2x1x2x1 - x3x1x3x1^2x2 + x3x1x3x1x2x1 
 x1x3x2^3x4 - x1x3x2^2x4x2 - x3x1x2^3x4 + x3x1x2^2x4x2 
 x1x3x2^3x3 - x1x3x2^2x3x2 - x3x1x2^3x3 + x3x1x2^2x3x2 
 x1x3x2^2x1x4 - x1x3x2^2x4x1 - x3x1x2^2x1x4 + x3x1x2^2x4x1 
 x1x3x2^2x1x3 - x1x3x2^2x3x1 - x3x1x2^2x1x3 + x3x1x2^2x3x1 
 x1x3x2^2x1x2 - x1x3x2^3x1 - x3x1x2^2x1x2 + x3x1x2^3x1 
 x1x3x2x1^2x4 - x1x3x2x1x4x1 - x3x1x2x1^2x4 + x3x1x2x1x4x1 
 x1x3x2x1^2x3 - x1x3x2x1x3x1 - x3x1x2x1^2x3 + x3x1x2x1x3x1 
 x1x3x2x1^2x2 - x1x3x2x1x2x1 - x3x1x2x1^2x2 + x3x1x2x1x2x1 
 x1x3x1^3x4 - x1x3x1^2x4x1 - x3x1^4x4 + x3x1^3x4x1 
 x1x3x1^3x3 - x1x3x1^2x3x1 - x3x1^4x3 + x3x1^3x3x1 
 x1x3x1^3x2 - x1x3x1^2x2x1 - x3x1^4x2 + x3x1^3x2x1 
 x1x2^4x4 - x1x2^3x4x2 - x2x1x2^3x4 + x2x1x2^2x4x2 
 x1x2^4x3 - x1x2^3x3x2 - x2x1x2^3x3 + x2x1x2^2x3x2 
 x1x2^3x1x4 - x1x2^3x4x1 - x2x1x2^2x1x4 + x2x1x2^2x4x1 
 x1x2^3x1x3 - x1x2^3x3x1 - x2x1x2^2x1x3 + x2x1x2^2x3x1 
 x1x2^3x1x2 - x1x2^4x1 - x2x1x2^2x1x2 + x2x1x2^3x1 
 x1x2^2x1^2x4 - x1x2^2x1x4x1 - x2x1x2x1^2x4 + x2x1x2x1x4x1 
 x1x2^2x1^2x3 - x1x2^2x1x3x1 - x2x1x2x1^2x3 + x2x1x2x1x3x1 
 x1x2^2x1^2x2 - x1x2^2x1x2x1 - x2x1x2x1^2x2 + x2x1x2x1x2x1 
 x1x2x1^3x4 - x1x2x1^2x4x1 - x2x1^4x4 + x2x1^3x4x1 
 x1x2x1^3x3 - x1x2x1^2x3x1 - x2x1^4x3 + x2x1^3x3x1 
 x1x2x1^3x2 - x1x2x1^2x2x1 - x2x1^4x2 + x2x1^3x2x1 
 x3x4^4x3x4 - x3x4^5x3 - x4x3x4^3x3x4 + x4x3x4^4x3 
 x3x4^4x2x4 - x3x4^5x2 - x4x3x4^3x2x4 + x4x3x4^4x2 
 x3x4^4x2x3 - x3x4^4x3x2 - x4x3x4^3x2x3 + x4x3x4^3x3x2 
 x3x4^4x1x4 - x3x4^5x1 - x4x3x4^3x1x4 + x4x3x4^4x1 
 x3x4^4x1x3 - x3x4^4x3x1 - x4x3x4^3x1x3 + x4x3x4^3x3x1 
 x3x4^4x1x2 - x3x4^4x2x1 - x4x3x4^3x1x2 + x4x3x4^3x2x1 
 x3x4^3x3^2x4 - x3x4^3x3x4x3 - x4x3x4^2x3^2x4 + x4x3x4^2x3x4x3 
 x3x4^3x3x2x4 - x3x4^3x3x4x2 - x4x3x4^2x3x2x4 + x4x3x4^2x3x4x2 
 x3x4^3x3x2x3 - x3x4^3x3^2x2 - x4x3x4^2x3x2x3 + x4x3x4^2x3^2x2 
 x3x4^3x3x1x4 - x3x4^3x3x4x1 - x4x3x4^2x3x1x4 + x4x3x4^2x3x4x1 
 x3x4^3x3x1x3 - x3x4^3x3^2x1 - x4x3x4^2x3x1x3 + x4x3x4^2x3^2x1 
 x3x4^3x3x1x2 - x3x4^3x3x2x1 - x4x3x4^2x3x1x2 + x4x3x4^2x3x2x1 
 x3x4^3x2^2x4 - x3x4^3x2x4x2 - x4x3x4^2x2^2x4 + x4x3x4^2x2x4x2 
 x3x4^3x2^2x3 - x3x4^3x2x3x2 - x4x3x4^2x2^2x3 + x4x3x4^2x2x3x2 
 x3x4^3x2x1x4 - x3x4^3x2x4x1 - x4x3x4^2x2x1x4 + x4x3x4^2x2x4x1 
 x3x4^3x2x1x3 - x3x4^3x2x3x1 - x4x3x4^2x2x1x3 + x4x3x4^2x2x3x1 
 x3x4^3x2x1x2 - x3x4^3x2^2x1 - x4x3x4^2x2x1x2 + x4x3x4^2x2^2x1 
 x3x4^3x1^2x4 - x3x4^3x1x4x1 - x4x3x4^2x1^2x4 + x4x3x4^2x1x4x1 
 x3x4^3x1^2x3 - x3x4^3x1x3x1 - x4x3x4^2x1^2x3 + x4x3x4^2x1x3x1 
 x3x4^3x1^2x2 - x3x4^3x1x2x1 - x4x3x4^2x1^2x2 + x4x3x4^2x1x2x1 
 x3x4^2x3^3x4 - x3x4^2x3^2x4x3 - x4x3x4x3^3x4 + x4x3x4x3^2x4x3 
 x3x4^2x3^2x2x4 - x3x4^2x3^2x4x2 - x4x3x4x3^2x2x4 + x4x3x4x3^2x4x2 
 x3x4^2x3^2x2x3 - x3x4^2x3^3x2 - x4x3x4x3^2x2x3 + x4x3x4x3^3x2 
 x3x4^2x3^2x1x4 - x3x4^2x3^2x4x1 - x4x3x4x3^2x1x4 + x4x3x4x3^2x4x1 
 x3x4^2x3^2x1x3 - x3x4^2x3^3x1 - x4x3x4x3^2x1x3 + x4x3x4x3^3x1 
 x3x4^2x3^2x1x2 - x3x4^2x3^2x2x1 - x4x3x4x3^2x1x2 + x4x3x4x3^2x2x1 
 x3x4^2x3x2^2x4 - x3x4^2x3x2x4x2 - x4x3x4x3x2^2x4 + x4x3x4x3x2x4x2 
 x3x4^2x3x2^2x3 - x3x4^2x3x2x3x2 - x4x3x4x3x2^2x3 + x4x3x4x3x2x3x2 
 x3x4^2x3x2x1x4 - x3x4^2x3x2x4x1 - x4x3x4x3x2x1x4 + x4x3x4x3x2x4x1 
 x3x4^2x3x2x1x3 - x3x4^2x3x2x3x1 - x4x3x4x3x2x1x3 + x4x3x4x3x2x3x1 
 x3x4^2x3x2x1x2 - x3x4^2x3x2^2x1 - x4x3x4x3x2x1x2 + x4x3x4x3x2^2x1 
 x3x4^2x3x1^2x4 - x3x4^2x3x1x4x1 - x4x3x4x3x1^2x4 + x4x3x4x3x1x4x1 
 x3x4^2x3x1^2x3 - x3x4^2x3x1x3x1 - x4x3x4x3x1^2x3 + x4x3x4x3x1x3x1 
 x3x4^2x3x1^2x2 - x3x4^2x3x1x2x1 - x4x3x4x3x1^2x2 + x4x3x4x3x1x2x1 
 x3x4^2x2^3x4 - x3x4^2x2^2x4x2 - x4x3x4x2^3x4 + x4x3x4x2^2x4x2 
 x3x4^2x2^3x3 - x3x4^2x2^2x3x2 - x4x3x4x2^3x3 + x4x3x4x2^2x3x2 
 x3x4^2x2^2x1x4 - x3x4^2x2^2x4x1 - x4x3x4x2^2x1x4 + x4x3x4x2^2x4x1 
 x3x4^2x2^2x1x3 - x3x4^2x2^2x3x1 - x4x3x4x2^2x1x3 + x4x3x4x2^2x3x1 
 x3x4^2x2^2x1x2 - x3x4^2x2^3x1 - x4x3x4x2^2x1x2 + x4x3x4x2^3x1 
 x3x4^2x2x1^2x4 - x3x4^2x2x1x4x1 - x4x3x4x2x1^2x4 + x4x3x4x2x1x4x1 
 x3x4^2x2x1^2x3 - x3x4^2x2x1x3x1 - x4x3x4x2x1^2x3 + x4x3x4x2x1x3x1 
 x3x4^2x2x1^2x2 - x3x4^2x2x1x2x1 - x4x3x4x2x1^2x2 + x4x3x4x2x1x2x1 
 x3x4^2x1^3x4 - x3x4^2x1^2x4x1 - x4x3x4x1^3x4 + x4x3x4x1^2x4x1 
 x3x4^2x1^3x3 - x3x4^2x1^2x3x1 - x4x3x4x1^3x3 + x4x3x4x1^2x3x1 
 x3x4^2x1^3x2 - x3x4^2x1^2x2x1 - x4x3x4x1^3x2 + x4x3x4x1^2x2x1 
 x3x4x3^4x4 - x3x4x3^3x4x3 - x4x3^5x4 + x4x3^4x4x3 
 x3x4x3^3x2x4 - x3x4x3^3x4x2 - x4x3^4x2x4 + x4x3^4x4x2 
 x3x4x3^3x2x3 - x3x4x3^4x2 - x4x3^4x2x3 + x4x3^5x2 
 x3x4x3^3x1x4 - x3x4x3^3x4x1 - x4x3^4x1x4 + x4x3^4x4x1 
 x3x4x3^3x1x3 - x3x4x3^4x1 - x4x3^4x1x3 + x4x3^5x1 
 x3x4x3^3x1x2 - x3x4x3^3x2x1 - x4x3^4x1x2 + x4x3^4x2x1 
 x3x4x3^2x2^2x4 - x3x4x3^2x2x4x2 - x4x3^3x2^2x4 + x4x3^3x2x4x2 
 x3x4x3^2x2^2x3 - x3x4x3^2x2x3x2 - x4x3^3x2^2x3 + x4x3^3x2x3x2 
 x3x4x3^2x2x1x4 - x3x4x3^2x2x4x1 - x4x3^3x2x1x4 + x4x3^3x2x4x1 
 x3x4x3^2x2x1x3 - x3x4x3^2x2x3x1 - x4x3^3x2x1x3 + x4x3^3x2x3x1 
 x3x4x3^2x2x1x2 - x3x4x3^2x2^2x1 - x4x3^3x2x1x2 + x4x3^3x2^2x1 
 x3x4x3^2x1^2x4 - x3x4x3^2x1x4x1 - x4x3^3x1^2x4 + x4x3^3x1x4x1 
 x3x4x3^2x1^2x3 - x3x4x3^2x1x3x1 - x4x3^3x1^2x3 + x4x3^3x1x3x1 
 x3x4x3^2x1^2x2 - x3x4x3^2x1x2x1 - x4x3^3x1^2x2 + x4x3^3x1x2x1 
 x3x4x3x2^3x4 - x3x4x3x2^2x4x2 - x4x3^2x2^3x4 + x4x3^2x2^2x4x2 
 x3x4x3x2^3x3 - x3x4x3x2^2x3x2 - x4x3^2x2^3x3 + x4x3^2x2^2x3x2 
 x3x4x3x2^2x1x4 - x3x4x3x2^2x4x1 - x4x3^2x2^2x1x4 + x4x3^2x2^2x4x1 
 x3x4x3x2^2x1x3 - x3x4x3x2^2x3x1 - x4x3^2x2^2x1x3 + x4x3^2x2^2x3x1 
 x3x4x3x2^2x1x2 - x3x4x3x2^3x1 - x4x3^2x2^2x1x2 + x4x3^2x2^3x1 
 x3x4x3x2x1^2x4 - x3x4x3x2x1x4x1 - x4x3^2x2x1^2x4 + x4x3^2x2x1x4x1 
 x3x4x3x2x1^2x3 - x3x4x3x2x1x3x1 - x4x3^2x2x1^2x3 + x4x3^2x2x1x3x1 
 x3x4x3x2x1^2x2 - x3x4x3x2x1x2x1 - x4x3^2x2x1^2x2 + x4x3^2x2x1x2x1 
 x3x4x3x1^3x4 - x3x4x3x1^2x4x1 - x4x3^2x1^3x4 + x4x3^2x1^2x4x1 
 x3x4x3x1^3x3 - x3x4x3x1^2x3x1 - x4x3^2x1^3x3 + x4x3^2x1^2x3x1 
 x3x4x3x1^3x2 - x3x4x3x1^2x2x1 - x4x3^2x1^3x2 + x4x3^2x1^2x2x1 
 x3x4x2^4x4 - x3x4x2^3x4x2 - x4x3x2^4x4 + x4x3x2^3x4x2 
 x3x4x2^4x3 - x3x4x2^3x3x2 - x4x3x2^4x3 + x4x3x2^3x3x2 
 x3x4x2^3x1x4 - x3x4x2^3x4x1 - x4x3x2^3x1x4 + x4x3x2^3x4x1 
 x3x4x2^3x1x3 - x3x4x2^3x3x1 - x4x3x2^3x1x3 + x4x3x2^3x3x1 
 x3x4x2^3x1x2 - x3x4x2^4x1 - x4x3x2^3x1x2 + x4x3x2^4x1 
 x3x4x2^2x1^2x4 - x3x4x2^2x1x4x1 - x4x3x2^2x1^2x4 + x4x3x2^2x1x4x1 
 x3x4x2^2x1^2x3 - x3x4x2^2x1x3x1 - x4x3x2^2x1^2x3 + x4x3x2^2x1x3x1 
 x3x4x2^2x1^2x2 - x3x4x2^2x1x2x1 - x4x3x2^2x1^2x2 + x4x3x2^2x1x2x1 
 x3x4x2x1^3x4 - x3x4x2x1^2x4x1 - x4x3x2x1^3x4 + x4x3x2x1^2x4x1 
 x3x4x2x1^3x3 - x3x4x2x1^2x3x1 - x4x3x2x1^3x3 + x4x3x2x1^2x3x1 
 x3x4x2x1^3x2 - x3x4x2x1^2x2x1 - x4x3x2x1^3x2 + x4x3x2x1^2x2x1 
 x3x4x1^4x4 - x3x4x1^3x4x1 - x4x3x1^4x4 + x4x3x1^3x4x1 
 x3x4x1^4x3 - x3x4x1^3x3x1 - x4x3x1^4x3 + x4x3x1^3x3x1 
 x3x4x1^4x2 - x3x4x1^3x2x1 - x4x3x1^4x2 + x4x3x1^3x2x1 
 x2x4^4x3x4 - x2x4^5x3 - x4x2x4^3x3x4 + x4x2x4^4x3 
 x2x4^4x2x4 - x2x4^5x2 - x4x2x4^3x2x4 + x4x2x4^4x2 
 x2x4^4x2x3 - x2x4^4x3x2 - x4x2x4^3x2x3 + x4x2x4^3x3x2 
 x2x4^4x1x4 - x2x4^5x1 - x4x2x4^3x1x4 + x4x2x4^4x1 
 x2x4^4x1x3 - x2x4^4x3x1 - x4x2x4^3x1x3 + x4x2x4^3x3x1 
 x2x4^4x1x2 - x2x4^4x2x1 - x4x2x4^3x1x2 + x4x2x4^3x2x1 
 x2x4^3x3^2x4 - x2x4^3x3x4x3 - x4x2x4^2x3^2x4 + x4x2x4^2x3x4x3 
 x2x4^3x3x2x4 - x2x4^3x3x4x2 - x4x2x4^2x3x2x4 + x4x2x4^2x3x4x2 
 x2x4^3x3x2x3 - x2x4^3x3^2x2 - x4x2x4^2x3x2x3 + x4x2x4^2x3^2x2 
 x2x4^3x3x1x4 - x2x4^3x3x4x1 - x4x2x4^2x3x1x4 + x4x2x4^2x3x4x1 
 x2x4^3x3x1x3 - x2x4^3x3^2x1 - x4x2x4^2x3x1x3 + x4x2x4^2x3^2x1 
 x2x4^3x3x1x2 - x2x4^3x3x2x1 - x4x2x4^2x3x1x2 + x4x2x4^2x3x2x1 
 x2x4^3x2^2x4 - x2x4^3x2x4x2 - x4x2x4^2x2^2x4 + x4x2x4^2x2x4x2 
 x2x4^3x2^2x3 - x2x4^3x2x3x2 - x4x2x4^2x2^2x3 + x4x2x4^2x2x3x2 
 x2x4^3x2x1x4 - x2x4^3x2x4x1 - x4x2x4^2x2x1x4 + x4x2x4^2x2x4x1 
 x2x4^3x2x1x3 - x2x4^3x2x3x1 - x4x2x4^2x2x1x3 + x4x2x4^2x2x3x1 
 x2x4^3x2x1x2 - x2x4^3x2^2x1 - x4x2x4^2x2x1x2 + x4x2x4^2x2^2x1 
 x2x4^3x1^2x4 - x2x4^3x1x4x1 - x4x2x4^2x1^2x4 + x4x2x4^2x1x4x1 
 x2x4^3x1^2x3 - x2x4^3x1x3x1 - x4x2x4^2x1^2x3 + x4x2x4^2x1x3x1 
 x2x4^3x1^2x2 - x2x4^3x1x2x1 - x4x2x4^2x1^2x2 + x4x2x4^2x1x2x1 
 x2x4^2x3^3x4 - x2x4^2x3^2x4x3 - x4x2x4x3^3x4 + x4x2x4x3^2x4x3 
 x2x4^2x3^2x2x4 - x2x4^2x3^2x4x2 - x4x2x4x3^2x2x4 + x4x2x4x3^2x4x2 
 x2x4^2x3^2x2x3 - x2x4^2x3^3x2 - x4x2x4x3^2x2x3 + x4x2x4x3^3x2 
 x2x4^2x3^2x1x4 - x2x4^2x3^2x4x1 - x4x2x4x3^2x1x4 + x4x2x4x3^2x4x1 
 x2x4^2x3^2x1x3 - x2x4^2x3^3x1 - x4x2x4x3^2x1x3 + x4x2x4x3^3x1 
 x2x4^2x3^2x1x2 - x2x4^2x3^2x2x1 - x4x2x4x3^2x1x2 + x4x2x4x3^2x2x1 
 x2x4^2x3x2^2x4 - x2x4^2x3x2x4x2 - x4x2x4x3x2^2x4 + x4x2x4x3x2x4x2 
 x2x4^2x3x2^2x3 - x2x4^2x3x2x3x2 - x4x2x4x3x2^2x3 + x4x2x4x3x2x3x2 
 x2x4^2x3x2x1x4 - x2x4^2x3x2x4x1 - x4x2x4x3x2x1x4 + x4x2x4x3x2x4x1 
 x2x4^2x3x2x1x3 - x2x4^2x3x2x3x1 - x4x2x4x3x2x1x3 + x4x2x4x3x2x3x1 
 x2x4^2x3x2x1x2 - x2x4^2x3x2^2x1 - x4x2x4x3x2x1x2 + x4x2x4x3x2^2x1 
 x2x4^2x3x1^2x4 - x2x4^2x3x1x4x1 - x4x2x4x3x1^2x4 + x4x2x4x3x1x4x1 
 x2x4^2x3x1^2x3 - x2x4^2x3x1x3x1 - x4x2x4x3x1^2x3 + x4x2x4x3x1x3x1 
 x2x4^2x3x1^2x2 - x2x4^2x3x1x2x1 - x4x2x4x3x1^2x2 + x4x2x4x3x1x2x1 
 x2x4^2x2^3x4 - x2x4^2x2^2x4x2 - x4x2x4x2^3x4 + x4x2x4x2^2x4x2 
 x2x4^2x2^3x3 - x2x4^2x2^2x3x2 - x4x2x4x2^3x3 + x4x2x4x2^2x3x2 
 x2x4^2x2^2x1x4 - x2x4^2x2^2x4x1 - x4x2x4x2^2x1x4 + x4x2x4x2^2x4x1 
 x2x4^2x2^2x1x3 - x2x4^2x2^2x3x1 - x4x2x4x2^2x1x3 + x4x2x4x2^2x3x1 
 x2x4^2x2^2x1x2 - x2x4^2x2^3x1 - x4x2x4x2^2x1x2 + x4x2x4x2^3x1 
 x2x4^2x2x1^2x4 - x2x4^2x2x1x4x1 - x4x2x4x2x1^2x4 + x4x2x4x2x1x4x1 
 x2x4^2x2x1^2x3 - x2x4^2x2x1x3x1 - x4x2x4x2x1^2x3 + x4x2x4x2x1x3x1 
 x2x4^2x2x1^2x2 - x2x4^2x2x1x2x1 - x4x2x4x2x1^2x2 + x4x2x4x2x1x2x1 
 x2x4^2x1^3x4 - x2x4^2x1^2x4x1 - x4x2x4x1^3x4 + x4x2x4x1^2x4x1 
 x2x4^2x1^3x3 - x2x4^2x1^2x3x1 - x4x2x4x1^3x3 + x4x2x4x1^2x3x1 
 x2x4^2x1^3x2 - x2x4^2x1^2x2x1 - x4x2x4x1^3x2 + x4x2x4x1^2x2x1 
 x2x4x3^4x4 - x2x4x3^3x4x3 - x4x2x3^4x4 + x4x2x3^3x4x3 
 x2x4x3^3x2x4 - x2x4x3^3x4x2 - x4x2x3^3x2x4 + x4x2x3^3x4x2 
 x2x4x3^3x2x3 - x2x4x3^4x2 - x4x2x3^3x2x3 + x4x2x3^4x2 
 x2x4x3^3x1x4 - x2x4x3^3x4x1 - x4x2x3^3x1x4 + x4x2x3^3x4x1 
 x2x4x3^3x1x3 - x2x4x3^4x1 - x4x2x3^3x1x3 + x4x2x3^4x1 
 x2x4x3^3x1x2 - x2x4x3^3x2x1 - x4x2x3^3x1x2 + x4x2x3^3x2x1 
 x2x4x3^2x2^2x4 - x2x4x3^2x2x4x2 - x4x2x3^2x2^2x4 + x4x2x3^2x2x4x2 
 x2x4x3^2x2^2x3 - x2x4x3^2x2x3x2 - x4x2x3^2x2^2x3 + x4x2x3^2x2x3x2 
 x2x4x3^2x2x1x4 - x2x4x3^2x2x4x1 - x4x2x3^2x2x1x4 + x4x2x3^2x2x4x1 
 x2x4x3^2x2x1x3 - x2x4x3^2x2x3x1 - x4x2x3^2x2x1x3 + x4x2x3^2x2x3x1 
 x2x4x3^2x2x1x2 - x2x4x3^2x2^2x1 - x4x2x3^2x2x1x2 + x4x2x3^2x2^2x1 
 x2x4x3^2x1^2x4 - x2x4x3^2x1x4x1 - x4x2x3^2x1^2x4 + x4x2x3^2x1x4x1 
 x2x4x3^2x1^2x3 - x2x4x3^2x1x3x1 - x4x2x3^2x1^2x3 + x4x2x3^2x1x3x1 
 x2x4x3^2x1^2x2 - x2x4x3^2x1x2x1 - x4x2x3^2x1^2x2 + x4x2x3^2x1x2x1 
 x2x4x3x2^3x4 - x2x4x3x2^2x4x2 - x4x2x3x2^3x4 + x4x2x3x2^2x4x2 
 x2x4x3x2^3x3 - x2x4x3x2^2x3x2 - x4x2x3x2^3x3 + x4x2x3x2^2x3x2 
 x2x4x3x2^2x1x4 - x2x4x3x2^2x4x1 - x4x2x3x2^2x1x4 + x4x2x3x2^2x4x1 
 x2x4x3x2^2x1x3 - x2x4x3x2^2x3x1 - x4x2x3x2^2x1x3 + x4x2x3x2^2x3x1 
 x2x4x3x2^2x1x2 - x2x4x3x2^3x1 - x4x2x3x2^2x1x2 + x4x2x3x2^3x1 
 x2x4x3x2x1^2x4 - x2x4x3x2x1x4x1 - x4x2x3x2x1^2x4 + x4x2x3x2x1x4x1 
 x2x4x3x2x1^2x3 - x2x4x3x2x1x3x1 - x4x2x3x2x1^2x3 + x4x2x3x2x1x3x1 
 x2x4x3x2x1^2x2 - x2x4x3x2x1x2x1 - x4x2x3x2x1^2x2 + x4x2x3x2x1x2x1 
 x2x4x3x1^3x4 - x2x4x3x1^2x4x1 - x4x2x3x1^3x4 + x4x2x3x1^2x4x1 
 x2x4x3x1^3x3 - x2x4x3x1^2x3x1 - x4x2x3x1^3x3 + x4x2x3x1^2x3x1 
 x2x4x3x1^3x2 - x2x4x3x1^2x2x1 - x4x2x3x1^3x2 + x4x2x3x1^2x2x1 
 x2x4x2^4x4 - x2x4x2^3x4x2 - x4x2^5x4 + x4x2^4x4x2 
 x2x4x2^4x3 - x2x4x2^3x3x2 - x4x2^5x3 + x4x2^4x3x2 
 x2x4x2^3x1x4 - x2x4x2^3x4x1 - x4x2^4x1x4 + x4x2^4x4x1 
 x2x4x2^3x1x3 - x2x4x2^3x3x1 - x4x2^4x1x3 + x4x2^4x3x1 
 x2x4x2^3x1x2 - x2x4x2^4x1 - x4x2^4x1x2 + x4x2^5x1 
 x2x4x2^2x1^2x4 - x2x4x2^2x1x4x1 - x4x2^3x1^2x4 + x4x2^3x1x4x1 
 x2x4x2^2x1^2x3 - x2x4x2^2x1x3x1 - x4x2^3x1^2x3 + x4x2^3x1x3x1 
 x2x4x2^2x1^2x2 - x2x4x2^2x1x2x1 - x4x2^3x1^2x2 + x4x2^3x1x2x1 
 x2x4x2x1^3x4 - x2x4x2x1^2x4x1 - x4x2^2x1^3x4 + x4x2^2x1^2x4x1 
 x2x4x2x1^3x3 - x2x4x2x1^2x3x1 - x4x2^2x1^3x3 + x4x2^2x1^2x3x1 
 x2x4x2x1^3x2 - x2x4x2x1^2x2x1 - x4x2^2x1^3x2 + x4x2^2x1^2x2x1 
 x2x4x1^4x4 - x2x4x1^3x4x1 - x4x2x1^4x4 + x4x2x1^3x4x1 
 x2x4x1^4x3 - x2x4x1^3x3x1 - x4x2x1^4x3 + x4x2x1^3x3x1 
 x2x4x1^4x2 - x2x4x1^3x2x1 - x4x2x1^4x2 + x4x2x1^3x2x1 
 x2x3^5x4 - x2x3^4x4x3 - x3x2x3^4x4 + x3x2x3^3x4x3 
 x2x3^4x2x4 - x2x3^4x4x2 - x3x2x3^3x2x4 + x3x2x3^3x4x2 
 x2x3^4x2x3 - x2x3^5x2 - x3x2x3^3x2x3 + x3x2x3^4x2 
 x2x3^4x1x4 - x2x3^4x4x1 - x3x2x3^3x1x4 + x3x2x3^3x4x1 
 x2x3^4x1x3 - x2x3^5x1 - x3x2x3^3x1x3 + x3x2x3^4x1 
 x2x3^4x1x2 - x2x3^4x2x1 - x3x2x3^3x1x2 + x3x2x3^3x2x1 
 x2x3^3x2^2x4 - x2x3^3x2x4x2 - x3x2x3^2x2^2x4 + x3x2x3^2x2x4x2 
 x2x3^3x2^2x3 - x2x3^3x2x3x2 - x3x2x3^2x2^2x3 + x3x2x3^2x2x3x2 
 x2x3^3x2x1x4 - x2x3^3x2x4x1 - x3x2x3^2x2x1x4 + x3x2x3^2x2x4x1 
 x2x3^3x2x1x3 - x2x3^3x2x3x1 - x3x2x3^2x2x1x3 + x3x2x3^2x2x3x1 
 x2x3^3x2x1x2 - x2x3^3x2^2x1 - x3x2x3^2x2x1x2 + x3x2x3^2x2^2x1 
 x2x3^3x1^2x4 - x2x3^3x1x4x1 - x3x2x3^2x1^2x4 + x3x2x3^2x1x4x1 
 x2x3^3x1^2x3 - x2x3^3x1x3x1 - x3x2x3^2x1^2x3 + x3x2x3^2x1x3x1 
 x2x3^3x1^2x2 - x2x3^3x1x2x1 - x3x2x3^2x1^2x2 + x3x2x3^2x1x2x1 
 x2x3^2x2^3x4 - x2x3^2x2^2x4x2 - x3x2x3x2^3x4 + x3x2x3x2^2x4x2 
 x2x3^2x2^3x3 - x2x3^2x2^2x3x2 - x3x2x3x2^3x3 + x3x2x3x2^2x3x2 
 x2x3^2x2^2x1x4 - x2x3^2x2^2x4x1 - x3x2x3x2^2x1x4 + x3x2x3x2^2x4x1 
 x2x3^2x2^2x1x3 - x2x3^2x2^2x3x1 - x3x2x3x2^2x1x3 + x3x2x3x2^2x3x1 
 x2x3^2x2^2x1x2 - x2x3^2x2^3x1 - x3x2x3x2^2x1x2 + x3x2x3x2^3x1 
 x2x3^2x2x1^2x4 - x2x3^2x2x1x4x1 - x3x2x3x2x1^2x4 + x3x2x3x2x1x4x1 
 x2x3^2x2x1^2x3 - x2x3^2x2x1x3x1 - x3x2x3x2x1^2x3 + x3x2x3x2x1x3x1 
 x2x3^2x2x1^2x2 - x2x3^2x2x1x2x1 - x3x2x3x2x1^2x2 + x3x2x3x2x1x2x1 
 x2x3^2x1^3x4 - x2x3^2x1^2x4x1 - x3x2x3x1^3x4 + x3x2x3x1^2x4x1 
 x2x3^2x1^3x3 - x2x3^2x1^2x3x1 - x3x2x3x1^3x3 + x3x2x3x1^2x3x1 
 x2x3^2x1^3x2 - x2x3^2x1^2x2x1 - x3x2x3x1^3x2 + x3x2x3x1^2x2x1 
 x2x3x2^4x4 - x2x3x2^3x4x2 - x3x2^5x4 + x3x2^4x4x2 
 x2x3x2^4x3 - x2x3x2^3x3x2 - x3x2^5x3 + x3x2^4x3x2 
 x2x3x2^3x1x4 - x2x3x2^3x4x1 - x3x2^4x1x4 + x3x2^4x4x1 
 x2x3x2^3x1x3 - x2x3x2^3x3x1 - x3x2^4x1x3 + x3x2^4x3x1 
 x2x3x2^3x1x2 - x2x3x2^4x1 - x3x2^4x1x2 + x3x2^5x1 
 x2x3x2^2x1^2x4 - x2x3x2^2x1x4x1 - x3x2^3x1^2x4 + x3x2^3x1x4x1 
 x2x3x2^2x1^2x3 - x2x3x2^2x1x3x1 - x3x2^3x1^2x3 + x3x2^3x1x3x1 
 x2x3x2^2x1^2x2 - x2x3x2^2x1x2x1 - x3x2^3x1^2x2 + x3x2^3x1x2x1 
 x2x3x2x1^3x4 - x2x3x2x1^2x4x1 - x3x2^2x1^3x4 + x3x2^2x1^2x4x1 
 x2x3x2x1^3x3 - x2x3x2x1^2x3x1 - x3x2^2x1^3x3 + x3x2^2x1^2x3x1 
 x2x3x2x1^3x2 - x2x3x2x1^2x2x1 - x3x2^2x1^3x2 + x3x2^2x1^2x2x1 
 x2x3x1^4x4 - x2x3x1^3x4x1 - x3x2x1^4x4 + x3x2x1^3x4x1 
 x2x3x1^4x3 - x2x3x1^3x3x1 - x3x2x1^4x3 + x3x2x1^3x3x1 
 x2x3x1^4x2 - x2x3x1^3x2x1 - x3x2x1^4x2 + x3x2x1^3x2x1 
 x1x4^4x3x4 - x1x4^5x3 - x4x1x4^3x3x4 + x4x1x4^4x3 
 x1x4^4x2x4 - x1x4^5x2 - x4x1x4^3x2x4 + x4x1x4^4x2 
 x1x4^4x2x3 - x1x4^4x3x2 - x4x1x4^3x2x3 + x4x1x4^3x3x2 
 x1x4^4x1x4 - x1x4^5x1 - x4x1x4^3x1x4 + x4x1x4^4x1 
 x1x4^4x1x3 - x1x4^4x3x1 - x4x1x4^3x1x3 + x4x1x4^3x3x1 
 x1x4^4x1x2 - x1x4^4x2x1 - x4x1x4^3x1x2 + x4x1x4^3x2x1 
 x1x4^3x3^2x4 - x1x4^3x3x4x3 - x4x1x4^2x3^2x4 + x4x1x4^2x3x4x3 
 x1x4^3x3x2x4 - x1x4^3x3x4x2 - x4x1x4^2x3x2x4 + x4x1x4^2x3x4x2 
 x1x4^3x3x2x3 - x1x4^3x3^2x2 - x4x1x4^2x3x2x3 + x4x1x4^2x3^2x2 
 x1x4^3x3x1x4 - x1x4^3x3x4x1 - x4x1x4^2x3x1x4 + x4x1x4^2x3x4x1 
 x1x4^3x3x1x3 - x1x4^3x3^2x1 - x4x1x4^2x3x1x3 + x4x1x4^2x3^2x1 
 x1x4^3x3x1x2 - x1x4^3x3x2x1 - x4x1x4^2x3x1x2 + x4x1x4^2x3x2x1 
 x1x4^3x2^2x4 - x1x4^3x2x4x2 - x4x1x4^2x2^2x4 + x4x1x4^2x2x4x2 
 x1x4^3x2^2x3 - x1x4^3x2x3x2 - x4x1x4^2x2^2x3 + x4x1x4^2x2x3x2 
 x1x4^3x2x1x4 - x1x4^3x2x4x1 - x4x1x4^2x2x1x4 + x4x1x4^2x2x4x1 
 x1x4^3x2x1x3 - x1x4^3x2x3x1 - x4x1x4^2x2x1x3 + x4x1x4^2x2x3x1 
 x1x4^3x2x1x2 - x1x4^3x2^2x1 - x4x1x4^2x2x1x2 + x4x1x4^2x2^2x1 
 x1x4^3x1^2x4 - x1x4^3x1x4x1 - x4x1x4^2x1^2x4 + x4x1x4^2x1x4x1 
 x1x4^3x1^2x3 - x1x4^3x1x3x1 - x4x1x4^2x1^2x3 + x4x1x4^2x1x3x1 
 x1x4^3x1^2x2 - x1x4^3x1x2x1 - x4x1x4^2x1^2x2 + x4x1x4^2x1x2x1 
 x1x4^2x3^3x4 - x1x4^2x3^2x4x3 - x4x1x4x3^3x4 + x4x1x4x3^2x4x3 
 x1x4^2x3^2x2x4 - x1x4^2x3^2x4x2 - x4x1x4x3^2x2x4 + x4x1x4x3^2x4x2 
 x1x4^2x3^2x2x3 - x1x4^2x3^3x2 - x4x1x4x3^2x2x3 + x4x1x4x3^3x2 
 x1x4^2x3^2x1x4 - x1x4^2x3^2x4x1 - x4x1x4x3^2x1x4 + x4x1x4x3^2x4x1 
 x1x4^2x3^2x1x3 - x1x4^2x3^3x1 - x4x1x4x3^2x1x3 + x4x1x4x3^3x1 
 x1x4^2x3^2x1x2 - x1x4^2x3^2x2x1 - x4x1x4x3^2x1x2 + x4x1x4x3^2x2x1 
 x1x4^2x3x2^2x4 - x1x4^2x3x2x4x2 - x4x1x4x3x2^2x4 + x4x1x4x3x2x4x2 
 x1x4^2x3x2^2x3 - x1x4^2x3x2x3x2 - x4x1x4x3x2^2x3 + x4x1x4x3x2x3x2 
 x1x4^2x3x2x1x4 - x1x4^2x3x2x4x1 - x4x1x4x3x2x1x4 + x4x1x4x3x2x4x1 
 x1x4^2x3x2x1x3 - x1x4^2x3x2x3x1 - x4x1x4x3x2x1x3 + x4x1x4x3x2x3x1 
 x1x4^2x3x2x1x2 - x1x4^2x3x2^2x1 - x4x1x4x3x2x1x2 + x4x1x4x3x2^2x1 
 x1x4^2x3x1^2x4 - x1x4^2x3x1x4x1 - x4x1x4x3x1^2x4 + x4x1x4x3x1x4x1 
 x1x4^2x3x1^2x3 - x1x4^2x3x1x3x1 - x4x1x4x3x1^2x3 + x4x1x4x3x1x3x1 
 x1x4^2x3x1^2x2 - x1x4^2x3x1x2x1 - x4x1x4x3x1^2x2 + x4x1x4x3x1x2x1 
 x1x4^2x2^3x4 - x1x4^2x2^2x4x2 - x4x1x4x2^3x4 + x4x1x4x2^2x4x2 
 x1x4^2x2^3x3 - x1x4^2x2^2x3x2 - x4x1x4x2^3x3 + x4x1x4x2^2x3x2 
 x1x4^2x2^2x1x4 - x1x4^2x2^2x4x1 - x4x1x4x2^2x1x4 + x4x1x4x2^2x4x1 
 x1x4^2x2^2x1x3 - x1x4^2x2^2x3x1 - x4x1x4x2^2x1x3 + x4x1x4x2^2x3x1 
 x1x4^2x2^2x1x2 - x1x4^2x2^3x1 - x4x1x4x2^2x1x2 + x4x1x4x2^3x1 
 x1x4^2x2x1^2x4 - x1x4^2x2x1x4x1 - x4x1x4x2x1^2x4 + x4x1x4x2x1x4x1 
 x1x4^2x2x1^2x3 - x1x4^2x2x1x3x1 - x4x1x4x2x1^2x3 + x4x1x4x2x1x3x1 
 x1x4^2x2x1^2x2 - x1x4^2x2x1x2x1 - x4x1x4x2x1^2x2 + x4x1x4x2x1x2x1 
 x1x4^2x1^3x4 - x1x4^2x1^2x4x1 - x4x1x4x1^3x4 + x4x1x4x1^2x4x1 
 x1x4^2x1^3x3 - x1x4^2x1^2x3x1 - x4x1x4x1^3x3 + x4x1x4x1^2x3x1 
 x1x4^2x1^3x2 - x1x4^2x1^2x2x1 - x4x1x4x1^3x2 + x4x1x4x1^2x2x1 
 x1x4x3^4x4 - x1x4x3^3x4x3 - x4x1x3^4x4 + x4x1x3^3x4x3 
 x1x4x3^3x2x4 - x1x4x3^3x4x2 - x4x1x3^3x2x4 + x4x1x3^3x4x2 
 x1x4x3^3x2x3 - x1x4x3^4x2 - x4x1x3^3x2x3 + x4x1x3^4x2 
 x1x4x3^3x1x4 - x1x4x3^3x4x1 - x4x1x3^3x1x4 + x4x1x3^3x4x1 
 x1x4x3^3x1x3 - x1x4x3^4x1 - x4x1x3^3x1x3 + x4x1x3^4x1 
 x1x4x3^3x1x2 - x1x4x3^3x2x1 - x4x1x3^3x1x2 + x4x1x3^3x2x1 
 x1x4x3^2x2^2x4 - x1x4x3^2x2x4x2 - x4x1x3^2x2^2x4 + x4x1x3^2x2x4x2 
 x1x4x3^2x2^2x3 - x1x4x3^2x2x3x2 - x4x1x3^2x2^2x3 + x4x1x3^2x2x3x2 
 x1x4x3^2x2x1x4 - x1x4x3^2x2x4x1 - x4x1x3^2x2x1x4 + x4x1x3^2x2x4x1 
 x1x4x3^2x2x1x3 - x1x4x3^2x2x3x1 - x4x1x3^2x2x1x3 + x4x1x3^2x2x3x1 
 x1x4x3^2x2x1x2 - x1x4x3^2x2^2x1 - x4x1x3^2x2x1x2 + x4x1x3^2x2^2x1 
 x1x4x3^2x1^2x4 - x1x4x3^2x1x4x1 - x4x1x3^2x1^2x4 + x4x1x3^2x1x4x1 
 x1x4x3^2x1^2x3 - x1x4x3^2x1x3x1 - x4x1x3^2x1^2x3 + x4x1x3^2x1x3x1 
 x1x4x3^2x1^2x2 - x1x4x3^2x1x2x1 - x4x1x3^2x1^2x2 + x4x1x3^2x1x2x1 
 x1x4x3x2^3x4 - x1x4x3x2^2x4x2 - x4x1x3x2^3x4 + x4x1x3x2^2x4x2 
 x1x4x3x2^3x3 - x1x4x3x2^2x3x2 - x4x1x3x2^3x3 + x4x1x3x2^2x3x2 
 x1x4x3x2^2x1x4 - x1x4x3x2^2x4x1 - x4x1x3x2^2x1x4 + x4x1x3x2^2x4x1 
 x1x4x3x2^2x1x3 - x1x4x3x2^2x3x1 - x4x1x3x2^2x1x3 + x4x1x3x2^2x3x1 
 x1x4x3x2^2x1x2 - x1x4x3x2^3x1 - x4x1x3x2^2x1x2 + x4x1x3x2^3x1 
 x1x4x3x2x1^2x4 - x1x4x3x2x1x4x1 - x4x1x3x2x1^2x4 + x4x1x3x2x1x4x1 
 x1x4x3x2x1^2x3 - x1x4x3x2x1x3x1 - x4x1x3x2x1^2x3 + x4x1x3x2x1x3x1 
 x1x4x3x2x1^2x2 - x1x4x3x2x1x2x1 - x4x1x3x2x1^2x2 + x4x1x3x2x1x2x1 
 x1x4x3x1^3x4 - x1x4x3x1^2x4x1 - x4x1x3x1^3x4 + x4x1x3x1^2x4x1 
 x1x4x3x1^3x3 - x1x4x3x1^2x3x1 - x4x1x3x1^3x3 + x4x1x3x1^2x3x1 
 x1x4x3x1^3x2 - x1x4x3x1^2x2x1 - x4x1x3x1^3x2 + x4x1x3x1^2x2x1 
 x1x4x2^4x4 - x1x4x2^3x4x2 - x4x1x2^4x4 + x4x1x2^3x4x2 
 x1x4x2^4x3 - x1x4x2^3x3x2 - x4x1x2^4x3 + x4x1x2^3x3x2 
 x1x4x2^3x1x4 - x1x4x2^3x4x1 - x4x1x2^3x1x4 + x4x1x2^3x4x1 
 x1x4x2^3x1x3 - x1x4x2^3x3x1 - x4x1x2^3x1x3 + x4x1x2^3x3x1 
 x1x4x2^3x1x2 - x1x4x2^4x1 - x4x1x2^3x1x2 + x4x1x2^4x1 
 x1x4x2^2x1^2x4 - x1x4x2^2x1x4x1 - x4x1x2^2x1^2x4 + x4x1x2^2x1x4x1 
 x1x4x2^2x1^2x3 - x1x4x2^2x1x3x1 - x4x1x2^2x1^2x3 + x4x1x2^2x1x3x1 
 x1x4x2^2x1^2x2 - x1x4x2^2x1x2x1 - x4x1x2^2x1^2x2 + x4x1x2^2x1x2x1 
 x1x4x2x1^3x4 - x1x4x2x1^2x4x1 - x4x1x2x1^3x4 + x4x1x2x1^2x4x1 
 x1x4x2x1^3x3 - x1x4x2x1^2x3x1 - x4x1x2x1^3x3 + x4x1x2x1^2x3x1 
 x1x4x2x1^3x2 - x1x4x2x1^2x2x1 - x4x1x2x1^3x2 + x4x1x2x1^2x2x1 
 x1x4x1^4x4 - x1x4x1^3x4x1 - x4x1^5x4 + x4x1^4x4x1 
 x1x4x1^4x3 - x1x4x1^3x3x1 - x4x1^5x3 + x4x1^4x3x1 
 x1x4x1^4x2 - x1x4x1^3x2x1 - x4x1^5x2 + x4x1^4x2x1 
 x1x3^5x4 - x1x3^4x4x3 - x3x1x3^4x4 + x3x1x3^3x4x3 
 x1x3^4x2x4 - x1x3^4x4x2 - x3x1x3^3x2x4 + x3x1x3^3x4x2 
 x1x3^4x2x3 - x1x3^5x2 - x3x1x3^3x2x3 + x3x1x3^4x2 
 x1x3^4x1x4 - x1x3^4x4x1 - x3x1x3^3x1x4 + x3x1x3^3x4x1 
 x1x3^4x1x3 - x1x3^5x1 - x3x1x3^3x1x3 + x3x1x3^4x1 
 x1x3^4x1x2 - x1x3^4x2x1 - x3x1x3^3x1x2 + x3x1x3^3x2x1 
 x1x3^3x2^2x4 - x1x3^3x2x4x2 - x3x1x3^2x2^2x4 + x3x1x3^2x2x4x2 
 x1x3^3x2^2x3 - x1x3^3x2x3x2 - x3x1x3^2x2^2x3 + x3x1x3^2x2x3x2 
 x1x3^3x2x1x4 - x1x3^3x2x4x1 - x3x1x3^2x2x1x4 + x3x1x3^2x2x4x1 
 x1x3^3x2x1x3 - x1x3^3x2x3x1 - x3x1x3^2x2x1x3 + x3x1x3^2x2x3x1 
 x1x3^3x2x1x2 - x1x3^3x2^2x1 - x3x1x3^2x2x1x2 + x3x1x3^2x2^2x1 
 x1x3^3x1^2x4 - x1x3^3x1x4x1 - x3x1x3^2x1^2x4 + x3x1x3^2x1x4x1 
 x1x3^3x1^2x3 - x1x3^3x1x3x1 - x3x1x3^2x1^2x3 + x3x1x3^2x1x3x1 
 x1x3^3x1^2x2 - x1x3^3x1x2x1 - x3x1x3^2x1^2x2 + x3x1x3^2x1x2x1 
 x1x3^2x2^3x4 - x1x3^2x2^2x4x2 - x3x1x3x2^3x4 + x3x1x3x2^2x4x2 
 x1x3^2x2^3x3 - x1x3^2x2^2x3x2 - x3x1x3x2^3x3 + x3x1x3x2^2x3x2 
 x1x3^2x2^2x1x4 - x1x3^2x2^2x4x1 - x3x1x3x2^2x1x4 + x3x1x3x2^2x4x1 
 x1x3^2x2^2x1x3 - x1x3^2x2^2x3x1 - x3x1x3x2^2x1x3 + x3x1x3x2^2x3x1 
 x1x3^2x2^2x1x2 - x1x3^2x2^3x1 - x3x1x3x2^2x1x2 + x3x1x3x2^3x1 
 x1x3^2x2x1^2x4 - x1x3^2x2x1x4x1 - x3x1x3x2x1^2x4 + x3x1x3x2x1x4x1 
 x1x3^2x2x1^2x3 - x1x3^2x2x1x3x1 - x3x1x3x2x1^2x3 + x3x1x3x2x1x3x1 
 x1x3^2x2x1^2x2 - x1x3^2x2x1x2x1 - x3x1x3x2x1^2x2 + x3x1x3x2x1x2x1 
 x1x3^2x1^3x4 - x1x3^2x1^2x4x1 - x3x1x3x1^3x4 + x3x1x3x1^2x4x1 
 x1x3^2x1^3x3 - x1x3^2x1^2x3x1 - x3x1x3x1^3x3 + x3x1x3x1^2x3x1 
 x1x3^2x1^3x2 - x1x3^2x1^2x2x1 - x3x1x3x1^3x2 + x3x1x3x1^2x2x1 
 x1x3x2^4x4 - x1x3x2^3x4x2 - x3x1x2^4x4 + x3x1x2^3x4x2 
 x1x3x2^4x3 - x1x3x2^3x3x2 - x3x1x2^4x3 + x3x1x2^3x3x2 
 x1x3x2^3x1x4 - x1x3x2^3x4x1 - x3x1x2^3x1x4 + x3x1x2^3x4x1 
 x1x3x2^3x1x3 - x1x3x2^3x3x1 - x3x1x2^3x1x3 + x3x1x2^3x3x1 
 x1x3x2^3x1x2 - x1x3x2^4x1 - x3x1x2^3x1x2 + x3x1x2^4x1 
 x1x3x2^2x1^2x4 - x1x3x2^2x1x4x1 - x3x1x2^2x1^2x4 + x3x1x2^2x1x4x1 
 x1x3x2^2x1^2x3 - x1x3x2^2x1x3x1 - x3x1x2^2x1^2x3 + x3x1x2^2x1x3x1 
 x1x3x2^2x1^2x2 - x1x3x2^2x1x2x1 - x3x1x2^2x1^2x2 + x3x1x2^2x1x2x1 
 x1x3x2x1^3x4 - x1x3x2x1^2x4x1 - x3x1x2x1^3x4 + x3x1x2x1^2x4x1 
 x1x3x2x1^3x3 - x1x3x2x1^2x3x1 - x3x1x2x1^3x3 + x3x1x2x1^2x3x1 
 x1x3x2x1^3x2 - x1x3x2x1^2x2x1 - x3x1x2x1^3x2 + x3x1x2x1^2x2x1 
 x1x3x1^4x4 - x1x3x1^3x4x1 - x3x1^5x4 + x3x1^4x4x1 
 x1x3x1^4x3 - x1x3x1^3x3x1 - x3x1^5x3 + x3x1^4x3x1 
 x1x3x1^4x2 - x1x3x1^3x2x1 - x3x1^5x2 + x3x1^4x2x1 
 x1x2^5x4 - x1x2^4x4x2 - x2x1x2^4x4 + x2x1x2^3x4x2 
 x1x2^5x3 - x1x2^4x3x2 - x2x1x2^4x3 + x2x1x2^3x3x2 
 x1x2^4x1x4 - x1x2^4x4x1 - x2x1x2^3x1x4 + x2x1x2^3x4x1 
 x1x2^4x1x3 - x1x2^4x3x1 - x2x1x2^3x1x3 + x2x1x2^3x3x1 
 x1x2^4x1x2 - x1x2^5x1 - x2x1x2^3x1x2 + x2x1x2^4x1 
 x1x2^3x1^2x4 - x1x2^3x1x4x1 - x2x1x2^2x1^2x4 + x2x1x2^2x1x4x1 
 x1x2^3x1^2x3 - x1x2^3x1x3x1 - x2x1x2^2x1^2x3 + x2x1x2^2x1x3x1 
 x1x2^3x1^2x2 - x1x2^3x1x2x1 - x2x1x2^2x1^2x2 + x2x1x2^2x1x2x1 
 x1x2^2x1^3x4 - x1x2^2x1^2x4x1 - x2x1x2x1^3x4 + x2x1x2x1^2x4x1 
 x1x2^2x1^3x3 - x1x2^2x1^2x3x1 - x2x1x2x1^3x3 + x2x1x2x1^2x3x1 
 x1x2^2x1^3x2 - x1x2^2x1^2x2x1 - x2x1x2x1^3x2 + x2x1x2x1^2x2x1 
 x1x2x1^4x4 - x1x2x1^3x4x1 - x2x1^5x4 + x2x1^4x4x1 
 x1x2x1^4x3 - x1x2x1^3x3x1 - x2x1^5x3 + x2x1^4x3x1 
 x1x2x1^4x2 - x1x2x1^3x2x1 - x2x1^5x2 + x2x1^4x2x1 
gap> =====Solution End=====
gap> 672
gap> > real 30.33
user 30.09
sys 0.23
"""
        try:
            tempRes = extractSolution(gapOutput)
        except:
            self.fail("Could not parse valid Singular output string")
        expectedOutp = """<?xml version="1.0" ?>
<FA_Q_dp_SOL>
  <basis>
    <polynomial>x3x4x3x4 - x3x4^2x3 - x4x3^2x4 + x4x3x4x3</polynomial>
    <polynomial>x3x4x2x4 - x3x4^2x2 - x4x3x2x4 + x4x3x4x2</polynomial>
    <polynomial>x3x4x2x3 - x3x4x3x2 - x4x3x2x3 + x4x3^2x2</polynomial>
    <polynomial>x3x4x1x4 - x3x4^2x1 - x4x3x1x4 + x4x3x4x1</polynomial>
    <polynomial>x3x4x1x3 - x3x4x3x1 - x4x3x1x3 + x4x3^2x1</polynomial>
    <polynomial>x3x4x1x2 - x3x4x2x1 - x4x3x1x2 + x4x3x2x1</polynomial>
    <polynomial>x2x4x3x4 - x2x4^2x3 - x4x2x3x4 + x4x2x4x3</polynomial>
    <polynomial>x2x4x2x4 - x2x4^2x2 - x4x2^2x4 + x4x2x4x2</polynomial>
    <polynomial>x2x4x2x3 - x2x4x3x2 - x4x2^2x3 + x4x2x3x2</polynomial>
    <polynomial>x2x4x1x4 - x2x4^2x1 - x4x2x1x4 + x4x2x4x1</polynomial>
    <polynomial>x2x4x1x3 - x2x4x3x1 - x4x2x1x3 + x4x2x3x1</polynomial>
    <polynomial>x2x4x1x2 - x2x4x2x1 - x4x2x1x2 + x4x2^2x1</polynomial>
    <polynomial>x2x3^2x4 - x2x3x4x3 - x3x2x3x4 + x3x2x4x3</polynomial>
    <polynomial>x2x3x2x4 - x2x3x4x2 - x3x2^2x4 + x3x2x4x2</polynomial>
    <polynomial>x2x3x2x3 - x2x3^2x2 - x3x2^2x3 + x3x2x3x2</polynomial>
    <polynomial>x2x3x1x4 - x2x3x4x1 - x3x2x1x4 + x3x2x4x1</polynomial>
    <polynomial>x2x3x1x3 - x2x3^2x1 - x3x2x1x3 + x3x2x3x1</polynomial>
    <polynomial>x2x3x1x2 - x2x3x2x1 - x3x2x1x2 + x3x2^2x1</polynomial>
    <polynomial>x1x4x3x4 - x1x4^2x3 - x4x1x3x4 + x4x1x4x3</polynomial>
    <polynomial>x1x4x2x4 - x1x4^2x2 - x4x1x2x4 + x4x1x4x2</polynomial>
    <polynomial>x1x4x2x3 - x1x4x3x2 - x4x1x2x3 + x4x1x3x2</polynomial>
    <polynomial>x1x4x1x4 - x1x4^2x1 - x4x1^2x4 + x4x1x4x1</polynomial>
    <polynomial>x1x4x1x3 - x1x4x3x1 - x4x1^2x3 + x4x1x3x1</polynomial>
    <polynomial>x1x4x1x2 - x1x4x2x1 - x4x1^2x2 + x4x1x2x1</polynomial>
    <polynomial>x1x3^2x4 - x1x3x4x3 - x3x1x3x4 + x3x1x4x3</polynomial>
    <polynomial>x1x3x2x4 - x1x3x4x2 - x3x1x2x4 + x3x1x4x2</polynomial>
    <polynomial>x1x3x2x3 - x1x3^2x2 - x3x1x2x3 + x3x1x3x2</polynomial>
    <polynomial>x1x3x1x4 - x1x3x4x1 - x3x1^2x4 + x3x1x4x1</polynomial>
    <polynomial>x1x3x1x3 - x1x3^2x1 - x3x1^2x3 + x3x1x3x1</polynomial>
    <polynomial>x1x3x1x2 - x1x3x2x1 - x3x1^2x2 + x3x1x2x1</polynomial>
    <polynomial>x1x2x3x4 - x1x2x4x3 - x2x1x3x4 + x2x1x4x3</polynomial>
    <polynomial>x1x2^2x4 - x1x2x4x2 - x2x1x2x4 + x2x1x4x2</polynomial>
    <polynomial>x1x2^2x3 - x1x2x3x2 - x2x1x2x3 + x2x1x3x2</polynomial>
    <polynomial>x1x2x1x4 - x1x2x4x1 - x2x1^2x4 + x2x1x4x1</polynomial>
    <polynomial>x1x2x1x3 - x1x2x3x1 - x2x1^2x3 + x2x1x3x1</polynomial>
    <polynomial>x1x2x1x2 - x1x2^2x1 - x2x1^2x2 + x2x1x2x1</polynomial>
    <polynomial>x3x4^2x3x4 - x3x4^3x3 - x4x3x4x3x4 + x4x3x4^2x3</polynomial>
    <polynomial>x3x4^2x2x4 - x3x4^3x2 - x4x3x4x2x4 + x4x3x4^2x2</polynomial>
    <polynomial>x3x4^2x2x3 - x3x4^2x3x2 - x4x3x4x2x3 + x4x3x4x3x2</polynomial>
    <polynomial>x3x4^2x1x4 - x3x4^3x1 - x4x3x4x1x4 + x4x3x4^2x1</polynomial>
    <polynomial>x3x4^2x1x3 - x3x4^2x3x1 - x4x3x4x1x3 + x4x3x4x3x1</polynomial>
    <polynomial>x3x4^2x1x2 - x3x4^2x2x1 - x4x3x4x1x2 + x4x3x4x2x1</polynomial>
    <polynomial>x3x4x3^2x4 - x3x4x3x4x3 - x4x3^3x4 + x4x3^2x4x3</polynomial>
    <polynomial>x3x4x3x2x4 - x3x4x3x4x2 - x4x3^2x2x4 + x4x3^2x4x2</polynomial>
    <polynomial>x3x4x3x2x3 - x3x4x3^2x2 - x4x3^2x2x3 + x4x3^3x2</polynomial>
    <polynomial>x3x4x3x1x4 - x3x4x3x4x1 - x4x3^2x1x4 + x4x3^2x4x1</polynomial>
    <polynomial>x3x4x3x1x3 - x3x4x3^2x1 - x4x3^2x1x3 + x4x3^3x1</polynomial>
    <polynomial>x3x4x3x1x2 - x3x4x3x2x1 - x4x3^2x1x2 + x4x3^2x2x1</polynomial>
    <polynomial>x3x4x2^2x4 - x3x4x2x4x2 - x4x3x2^2x4 + x4x3x2x4x2</polynomial>
    <polynomial>x3x4x2^2x3 - x3x4x2x3x2 - x4x3x2^2x3 + x4x3x2x3x2</polynomial>
    <polynomial>x3x4x2x1x4 - x3x4x2x4x1 - x4x3x2x1x4 + x4x3x2x4x1</polynomial>
    <polynomial>x3x4x2x1x3 - x3x4x2x3x1 - x4x3x2x1x3 + x4x3x2x3x1</polynomial>
    <polynomial>x3x4x2x1x2 - x3x4x2^2x1 - x4x3x2x1x2 + x4x3x2^2x1</polynomial>
    <polynomial>x3x4x1^2x4 - x3x4x1x4x1 - x4x3x1^2x4 + x4x3x1x4x1</polynomial>
    <polynomial>x3x4x1^2x3 - x3x4x1x3x1 - x4x3x1^2x3 + x4x3x1x3x1</polynomial>
    <polynomial>x3x4x1^2x2 - x3x4x1x2x1 - x4x3x1^2x2 + x4x3x1x2x1</polynomial>
    <polynomial>x2x4^2x3x4 - x2x4^3x3 - x4x2x4x3x4 + x4x2x4^2x3</polynomial>
    <polynomial>x2x4^2x2x4 - x2x4^3x2 - x4x2x4x2x4 + x4x2x4^2x2</polynomial>
    <polynomial>x2x4^2x2x3 - x2x4^2x3x2 - x4x2x4x2x3 + x4x2x4x3x2</polynomial>
    <polynomial>x2x4^2x1x4 - x2x4^3x1 - x4x2x4x1x4 + x4x2x4^2x1</polynomial>
    <polynomial>x2x4^2x1x3 - x2x4^2x3x1 - x4x2x4x1x3 + x4x2x4x3x1</polynomial>
    <polynomial>x2x4^2x1x2 - x2x4^2x2x1 - x4x2x4x1x2 + x4x2x4x2x1</polynomial>
    <polynomial>x2x4x3^2x4 - x2x4x3x4x3 - x4x2x3^2x4 + x4x2x3x4x3</polynomial>
    <polynomial>x2x4x3x2x4 - x2x4x3x4x2 - x4x2x3x2x4 + x4x2x3x4x2</polynomial>
    <polynomial>x2x4x3x2x3 - x2x4x3^2x2 - x4x2x3x2x3 + x4x2x3^2x2</polynomial>
    <polynomial>x2x4x3x1x4 - x2x4x3x4x1 - x4x2x3x1x4 + x4x2x3x4x1</polynomial>
    <polynomial>x2x4x3x1x3 - x2x4x3^2x1 - x4x2x3x1x3 + x4x2x3^2x1</polynomial>
    <polynomial>x2x4x3x1x2 - x2x4x3x2x1 - x4x2x3x1x2 + x4x2x3x2x1</polynomial>
    <polynomial>x2x4x2^2x4 - x2x4x2x4x2 - x4x2^3x4 + x4x2^2x4x2</polynomial>
    <polynomial>x2x4x2^2x3 - x2x4x2x3x2 - x4x2^3x3 + x4x2^2x3x2</polynomial>
    <polynomial>x2x4x2x1x4 - x2x4x2x4x1 - x4x2^2x1x4 + x4x2^2x4x1</polynomial>
    <polynomial>x2x4x2x1x3 - x2x4x2x3x1 - x4x2^2x1x3 + x4x2^2x3x1</polynomial>
    <polynomial>x2x4x2x1x2 - x2x4x2^2x1 - x4x2^2x1x2 + x4x2^3x1</polynomial>
    <polynomial>x2x4x1^2x4 - x2x4x1x4x1 - x4x2x1^2x4 + x4x2x1x4x1</polynomial>
    <polynomial>x2x4x1^2x3 - x2x4x1x3x1 - x4x2x1^2x3 + x4x2x1x3x1</polynomial>
    <polynomial>x2x4x1^2x2 - x2x4x1x2x1 - x4x2x1^2x2 + x4x2x1x2x1</polynomial>
    <polynomial>x2x3^3x4 - x2x3^2x4x3 - x3x2x3^2x4 + x3x2x3x4x3</polynomial>
    <polynomial>x2x3^2x2x4 - x2x3^2x4x2 - x3x2x3x2x4 + x3x2x3x4x2</polynomial>
    <polynomial>x2x3^2x2x3 - x2x3^3x2 - x3x2x3x2x3 + x3x2x3^2x2</polynomial>
    <polynomial>x2x3^2x1x4 - x2x3^2x4x1 - x3x2x3x1x4 + x3x2x3x4x1</polynomial>
    <polynomial>x2x3^2x1x3 - x2x3^3x1 - x3x2x3x1x3 + x3x2x3^2x1</polynomial>
    <polynomial>x2x3^2x1x2 - x2x3^2x2x1 - x3x2x3x1x2 + x3x2x3x2x1</polynomial>
    <polynomial>x2x3x2^2x4 - x2x3x2x4x2 - x3x2^3x4 + x3x2^2x4x2</polynomial>
    <polynomial>x2x3x2^2x3 - x2x3x2x3x2 - x3x2^3x3 + x3x2^2x3x2</polynomial>
    <polynomial>x2x3x2x1x4 - x2x3x2x4x1 - x3x2^2x1x4 + x3x2^2x4x1</polynomial>
    <polynomial>x2x3x2x1x3 - x2x3x2x3x1 - x3x2^2x1x3 + x3x2^2x3x1</polynomial>
    <polynomial>x2x3x2x1x2 - x2x3x2^2x1 - x3x2^2x1x2 + x3x2^3x1</polynomial>
    <polynomial>x2x3x1^2x4 - x2x3x1x4x1 - x3x2x1^2x4 + x3x2x1x4x1</polynomial>
    <polynomial>x2x3x1^2x3 - x2x3x1x3x1 - x3x2x1^2x3 + x3x2x1x3x1</polynomial>
    <polynomial>x2x3x1^2x2 - x2x3x1x2x1 - x3x2x1^2x2 + x3x2x1x2x1</polynomial>
    <polynomial>x1x4^2x3x4 - x1x4^3x3 - x4x1x4x3x4 + x4x1x4^2x3</polynomial>
    <polynomial>x1x4^2x2x4 - x1x4^3x2 - x4x1x4x2x4 + x4x1x4^2x2</polynomial>
    <polynomial>x1x4^2x2x3 - x1x4^2x3x2 - x4x1x4x2x3 + x4x1x4x3x2</polynomial>
    <polynomial>x1x4^2x1x4 - x1x4^3x1 - x4x1x4x1x4 + x4x1x4^2x1</polynomial>
    <polynomial>x1x4^2x1x3 - x1x4^2x3x1 - x4x1x4x1x3 + x4x1x4x3x1</polynomial>
    <polynomial>x1x4^2x1x2 - x1x4^2x2x1 - x4x1x4x1x2 + x4x1x4x2x1</polynomial>
    <polynomial>x1x4x3^2x4 - x1x4x3x4x3 - x4x1x3^2x4 + x4x1x3x4x3</polynomial>
    <polynomial>x1x4x3x2x4 - x1x4x3x4x2 - x4x1x3x2x4 + x4x1x3x4x2</polynomial>
    <polynomial>x1x4x3x2x3 - x1x4x3^2x2 - x4x1x3x2x3 + x4x1x3^2x2</polynomial>
    <polynomial>x1x4x3x1x4 - x1x4x3x4x1 - x4x1x3x1x4 + x4x1x3x4x1</polynomial>
    <polynomial>x1x4x3x1x3 - x1x4x3^2x1 - x4x1x3x1x3 + x4x1x3^2x1</polynomial>
    <polynomial>x1x4x3x1x2 - x1x4x3x2x1 - x4x1x3x1x2 + x4x1x3x2x1</polynomial>
    <polynomial>x1x4x2^2x4 - x1x4x2x4x2 - x4x1x2^2x4 + x4x1x2x4x2</polynomial>
    <polynomial>x1x4x2^2x3 - x1x4x2x3x2 - x4x1x2^2x3 + x4x1x2x3x2</polynomial>
    <polynomial>x1x4x2x1x4 - x1x4x2x4x1 - x4x1x2x1x4 + x4x1x2x4x1</polynomial>
    <polynomial>x1x4x2x1x3 - x1x4x2x3x1 - x4x1x2x1x3 + x4x1x2x3x1</polynomial>
    <polynomial>x1x4x2x1x2 - x1x4x2^2x1 - x4x1x2x1x2 + x4x1x2^2x1</polynomial>
    <polynomial>x1x4x1^2x4 - x1x4x1x4x1 - x4x1^3x4 + x4x1^2x4x1</polynomial>
    <polynomial>x1x4x1^2x3 - x1x4x1x3x1 - x4x1^3x3 + x4x1^2x3x1</polynomial>
    <polynomial>x1x4x1^2x2 - x1x4x1x2x1 - x4x1^3x2 + x4x1^2x2x1</polynomial>
    <polynomial>x1x3^3x4 - x1x3^2x4x3 - x3x1x3^2x4 + x3x1x3x4x3</polynomial>
    <polynomial>x1x3^2x2x4 - x1x3^2x4x2 - x3x1x3x2x4 + x3x1x3x4x2</polynomial>
    <polynomial>x1x3^2x2x3 - x1x3^3x2 - x3x1x3x2x3 + x3x1x3^2x2</polynomial>
    <polynomial>x1x3^2x1x4 - x1x3^2x4x1 - x3x1x3x1x4 + x3x1x3x4x1</polynomial>
    <polynomial>x1x3^2x1x3 - x1x3^3x1 - x3x1x3x1x3 + x3x1x3^2x1</polynomial>
    <polynomial>x1x3^2x1x2 - x1x3^2x2x1 - x3x1x3x1x2 + x3x1x3x2x1</polynomial>
    <polynomial>x1x3x2^2x4 - x1x3x2x4x2 - x3x1x2^2x4 + x3x1x2x4x2</polynomial>
    <polynomial>x1x3x2^2x3 - x1x3x2x3x2 - x3x1x2^2x3 + x3x1x2x3x2</polynomial>
    <polynomial>x1x3x2x1x4 - x1x3x2x4x1 - x3x1x2x1x4 + x3x1x2x4x1</polynomial>
    <polynomial>x1x3x2x1x3 - x1x3x2x3x1 - x3x1x2x1x3 + x3x1x2x3x1</polynomial>
    <polynomial>x1x3x2x1x2 - x1x3x2^2x1 - x3x1x2x1x2 + x3x1x2^2x1</polynomial>
    <polynomial>x1x3x1^2x4 - x1x3x1x4x1 - x3x1^3x4 + x3x1^2x4x1</polynomial>
    <polynomial>x1x3x1^2x3 - x1x3x1x3x1 - x3x1^3x3 + x3x1^2x3x1</polynomial>
    <polynomial>x1x3x1^2x2 - x1x3x1x2x1 - x3x1^3x2 + x3x1^2x2x1</polynomial>
    <polynomial>x1x2^3x4 - x1x2^2x4x2 - x2x1x2^2x4 + x2x1x2x4x2</polynomial>
    <polynomial>x1x2^3x3 - x1x2^2x3x2 - x2x1x2^2x3 + x2x1x2x3x2</polynomial>
    <polynomial>x1x2^2x1x4 - x1x2^2x4x1 - x2x1x2x1x4 + x2x1x2x4x1</polynomial>
    <polynomial>x1x2^2x1x3 - x1x2^2x3x1 - x2x1x2x1x3 + x2x1x2x3x1</polynomial>
    <polynomial>x1x2^2x1x2 - x1x2^3x1 - x2x1x2x1x2 + x2x1x2^2x1</polynomial>
    <polynomial>x1x2x1^2x4 - x1x2x1x4x1 - x2x1^3x4 + x2x1^2x4x1</polynomial>
    <polynomial>x1x2x1^2x3 - x1x2x1x3x1 - x2x1^3x3 + x2x1^2x3x1</polynomial>
    <polynomial>x1x2x1^2x2 - x1x2x1x2x1 - x2x1^3x2 + x2x1^2x2x1</polynomial>
    <polynomial>x3x4^3x3x4 - x3x4^4x3 - x4x3x4^2x3x4 + x4x3x4^3x3</polynomial>
    <polynomial>x3x4^3x2x4 - x3x4^4x2 - x4x3x4^2x2x4 + x4x3x4^3x2</polynomial>
    <polynomial>x3x4^3x2x3 - x3x4^3x3x2 - x4x3x4^2x2x3 + x4x3x4^2x3x2</polynomial>
    <polynomial>x3x4^3x1x4 - x3x4^4x1 - x4x3x4^2x1x4 + x4x3x4^3x1</polynomial>
    <polynomial>x3x4^3x1x3 - x3x4^3x3x1 - x4x3x4^2x1x3 + x4x3x4^2x3x1</polynomial>
    <polynomial>x3x4^3x1x2 - x3x4^3x2x1 - x4x3x4^2x1x2 + x4x3x4^2x2x1</polynomial>
    <polynomial>x3x4^2x3^2x4 - x3x4^2x3x4x3 - x4x3x4x3^2x4 + x4x3x4x3x4x3</polynomial>
    <polynomial>x3x4^2x3x2x4 - x3x4^2x3x4x2 - x4x3x4x3x2x4 + x4x3x4x3x4x2</polynomial>
    <polynomial>x3x4^2x3x2x3 - x3x4^2x3^2x2 - x4x3x4x3x2x3 + x4x3x4x3^2x2</polynomial>
    <polynomial>x3x4^2x3x1x4 - x3x4^2x3x4x1 - x4x3x4x3x1x4 + x4x3x4x3x4x1</polynomial>
    <polynomial>x3x4^2x3x1x3 - x3x4^2x3^2x1 - x4x3x4x3x1x3 + x4x3x4x3^2x1</polynomial>
    <polynomial>x3x4^2x3x1x2 - x3x4^2x3x2x1 - x4x3x4x3x1x2 + x4x3x4x3x2x1</polynomial>
    <polynomial>x3x4^2x2^2x4 - x3x4^2x2x4x2 - x4x3x4x2^2x4 + x4x3x4x2x4x2</polynomial>
    <polynomial>x3x4^2x2^2x3 - x3x4^2x2x3x2 - x4x3x4x2^2x3 + x4x3x4x2x3x2</polynomial>
    <polynomial>x3x4^2x2x1x4 - x3x4^2x2x4x1 - x4x3x4x2x1x4 + x4x3x4x2x4x1</polynomial>
    <polynomial>x3x4^2x2x1x3 - x3x4^2x2x3x1 - x4x3x4x2x1x3 + x4x3x4x2x3x1</polynomial>
    <polynomial>x3x4^2x2x1x2 - x3x4^2x2^2x1 - x4x3x4x2x1x2 + x4x3x4x2^2x1</polynomial>
    <polynomial>x3x4^2x1^2x4 - x3x4^2x1x4x1 - x4x3x4x1^2x4 + x4x3x4x1x4x1</polynomial>
    <polynomial>x3x4^2x1^2x3 - x3x4^2x1x3x1 - x4x3x4x1^2x3 + x4x3x4x1x3x1</polynomial>
    <polynomial>x3x4^2x1^2x2 - x3x4^2x1x2x1 - x4x3x4x1^2x2 + x4x3x4x1x2x1</polynomial>
    <polynomial>x3x4x3^3x4 - x3x4x3^2x4x3 - x4x3^4x4 + x4x3^3x4x3</polynomial>
    <polynomial>x3x4x3^2x2x4 - x3x4x3^2x4x2 - x4x3^3x2x4 + x4x3^3x4x2</polynomial>
    <polynomial>x3x4x3^2x2x3 - x3x4x3^3x2 - x4x3^3x2x3 + x4x3^4x2</polynomial>
    <polynomial>x3x4x3^2x1x4 - x3x4x3^2x4x1 - x4x3^3x1x4 + x4x3^3x4x1</polynomial>
    <polynomial>x3x4x3^2x1x3 - x3x4x3^3x1 - x4x3^3x1x3 + x4x3^4x1</polynomial>
    <polynomial>x3x4x3^2x1x2 - x3x4x3^2x2x1 - x4x3^3x1x2 + x4x3^3x2x1</polynomial>
    <polynomial>x3x4x3x2^2x4 - x3x4x3x2x4x2 - x4x3^2x2^2x4 + x4x3^2x2x4x2</polynomial>
    <polynomial>x3x4x3x2^2x3 - x3x4x3x2x3x2 - x4x3^2x2^2x3 + x4x3^2x2x3x2</polynomial>
    <polynomial>x3x4x3x2x1x4 - x3x4x3x2x4x1 - x4x3^2x2x1x4 + x4x3^2x2x4x1</polynomial>
    <polynomial>x3x4x3x2x1x3 - x3x4x3x2x3x1 - x4x3^2x2x1x3 + x4x3^2x2x3x1</polynomial>
    <polynomial>x3x4x3x2x1x2 - x3x4x3x2^2x1 - x4x3^2x2x1x2 + x4x3^2x2^2x1</polynomial>
    <polynomial>x3x4x3x1^2x4 - x3x4x3x1x4x1 - x4x3^2x1^2x4 + x4x3^2x1x4x1</polynomial>
    <polynomial>x3x4x3x1^2x3 - x3x4x3x1x3x1 - x4x3^2x1^2x3 + x4x3^2x1x3x1</polynomial>
    <polynomial>x3x4x3x1^2x2 - x3x4x3x1x2x1 - x4x3^2x1^2x2 + x4x3^2x1x2x1</polynomial>
    <polynomial>x3x4x2^3x4 - x3x4x2^2x4x2 - x4x3x2^3x4 + x4x3x2^2x4x2</polynomial>
    <polynomial>x3x4x2^3x3 - x3x4x2^2x3x2 - x4x3x2^3x3 + x4x3x2^2x3x2</polynomial>
    <polynomial>x3x4x2^2x1x4 - x3x4x2^2x4x1 - x4x3x2^2x1x4 + x4x3x2^2x4x1</polynomial>
    <polynomial>x3x4x2^2x1x3 - x3x4x2^2x3x1 - x4x3x2^2x1x3 + x4x3x2^2x3x1</polynomial>
    <polynomial>x3x4x2^2x1x2 - x3x4x2^3x1 - x4x3x2^2x1x2 + x4x3x2^3x1</polynomial>
    <polynomial>x3x4x2x1^2x4 - x3x4x2x1x4x1 - x4x3x2x1^2x4 + x4x3x2x1x4x1</polynomial>
    <polynomial>x3x4x2x1^2x3 - x3x4x2x1x3x1 - x4x3x2x1^2x3 + x4x3x2x1x3x1</polynomial>
    <polynomial>x3x4x2x1^2x2 - x3x4x2x1x2x1 - x4x3x2x1^2x2 + x4x3x2x1x2x1</polynomial>
    <polynomial>x3x4x1^3x4 - x3x4x1^2x4x1 - x4x3x1^3x4 + x4x3x1^2x4x1</polynomial>
    <polynomial>x3x4x1^3x3 - x3x4x1^2x3x1 - x4x3x1^3x3 + x4x3x1^2x3x1</polynomial>
    <polynomial>x3x4x1^3x2 - x3x4x1^2x2x1 - x4x3x1^3x2 + x4x3x1^2x2x1</polynomial>
    <polynomial>x2x4^3x3x4 - x2x4^4x3 - x4x2x4^2x3x4 + x4x2x4^3x3</polynomial>
    <polynomial>x2x4^3x2x4 - x2x4^4x2 - x4x2x4^2x2x4 + x4x2x4^3x2</polynomial>
    <polynomial>x2x4^3x2x3 - x2x4^3x3x2 - x4x2x4^2x2x3 + x4x2x4^2x3x2</polynomial>
    <polynomial>x2x4^3x1x4 - x2x4^4x1 - x4x2x4^2x1x4 + x4x2x4^3x1</polynomial>
    <polynomial>x2x4^3x1x3 - x2x4^3x3x1 - x4x2x4^2x1x3 + x4x2x4^2x3x1</polynomial>
    <polynomial>x2x4^3x1x2 - x2x4^3x2x1 - x4x2x4^2x1x2 + x4x2x4^2x2x1</polynomial>
    <polynomial>x2x4^2x3^2x4 - x2x4^2x3x4x3 - x4x2x4x3^2x4 + x4x2x4x3x4x3</polynomial>
    <polynomial>x2x4^2x3x2x4 - x2x4^2x3x4x2 - x4x2x4x3x2x4 + x4x2x4x3x4x2</polynomial>
    <polynomial>x2x4^2x3x2x3 - x2x4^2x3^2x2 - x4x2x4x3x2x3 + x4x2x4x3^2x2</polynomial>
    <polynomial>x2x4^2x3x1x4 - x2x4^2x3x4x1 - x4x2x4x3x1x4 + x4x2x4x3x4x1</polynomial>
    <polynomial>x2x4^2x3x1x3 - x2x4^2x3^2x1 - x4x2x4x3x1x3 + x4x2x4x3^2x1</polynomial>
    <polynomial>x2x4^2x3x1x2 - x2x4^2x3x2x1 - x4x2x4x3x1x2 + x4x2x4x3x2x1</polynomial>
    <polynomial>x2x4^2x2^2x4 - x2x4^2x2x4x2 - x4x2x4x2^2x4 + x4x2x4x2x4x2</polynomial>
    <polynomial>x2x4^2x2^2x3 - x2x4^2x2x3x2 - x4x2x4x2^2x3 + x4x2x4x2x3x2</polynomial>
    <polynomial>x2x4^2x2x1x4 - x2x4^2x2x4x1 - x4x2x4x2x1x4 + x4x2x4x2x4x1</polynomial>
    <polynomial>x2x4^2x2x1x3 - x2x4^2x2x3x1 - x4x2x4x2x1x3 + x4x2x4x2x3x1</polynomial>
    <polynomial>x2x4^2x2x1x2 - x2x4^2x2^2x1 - x4x2x4x2x1x2 + x4x2x4x2^2x1</polynomial>
    <polynomial>x2x4^2x1^2x4 - x2x4^2x1x4x1 - x4x2x4x1^2x4 + x4x2x4x1x4x1</polynomial>
    <polynomial>x2x4^2x1^2x3 - x2x4^2x1x3x1 - x4x2x4x1^2x3 + x4x2x4x1x3x1</polynomial>
    <polynomial>x2x4^2x1^2x2 - x2x4^2x1x2x1 - x4x2x4x1^2x2 + x4x2x4x1x2x1</polynomial>
    <polynomial>x2x4x3^3x4 - x2x4x3^2x4x3 - x4x2x3^3x4 + x4x2x3^2x4x3</polynomial>
    <polynomial>x2x4x3^2x2x4 - x2x4x3^2x4x2 - x4x2x3^2x2x4 + x4x2x3^2x4x2</polynomial>
    <polynomial>x2x4x3^2x2x3 - x2x4x3^3x2 - x4x2x3^2x2x3 + x4x2x3^3x2</polynomial>
    <polynomial>x2x4x3^2x1x4 - x2x4x3^2x4x1 - x4x2x3^2x1x4 + x4x2x3^2x4x1</polynomial>
    <polynomial>x2x4x3^2x1x3 - x2x4x3^3x1 - x4x2x3^2x1x3 + x4x2x3^3x1</polynomial>
    <polynomial>x2x4x3^2x1x2 - x2x4x3^2x2x1 - x4x2x3^2x1x2 + x4x2x3^2x2x1</polynomial>
    <polynomial>x2x4x3x2^2x4 - x2x4x3x2x4x2 - x4x2x3x2^2x4 + x4x2x3x2x4x2</polynomial>
    <polynomial>x2x4x3x2^2x3 - x2x4x3x2x3x2 - x4x2x3x2^2x3 + x4x2x3x2x3x2</polynomial>
    <polynomial>x2x4x3x2x1x4 - x2x4x3x2x4x1 - x4x2x3x2x1x4 + x4x2x3x2x4x1</polynomial>
    <polynomial>x2x4x3x2x1x3 - x2x4x3x2x3x1 - x4x2x3x2x1x3 + x4x2x3x2x3x1</polynomial>
    <polynomial>x2x4x3x2x1x2 - x2x4x3x2^2x1 - x4x2x3x2x1x2 + x4x2x3x2^2x1</polynomial>
    <polynomial>x2x4x3x1^2x4 - x2x4x3x1x4x1 - x4x2x3x1^2x4 + x4x2x3x1x4x1</polynomial>
    <polynomial>x2x4x3x1^2x3 - x2x4x3x1x3x1 - x4x2x3x1^2x3 + x4x2x3x1x3x1</polynomial>
    <polynomial>x2x4x3x1^2x2 - x2x4x3x1x2x1 - x4x2x3x1^2x2 + x4x2x3x1x2x1</polynomial>
    <polynomial>x2x4x2^3x4 - x2x4x2^2x4x2 - x4x2^4x4 + x4x2^3x4x2</polynomial>
    <polynomial>x2x4x2^3x3 - x2x4x2^2x3x2 - x4x2^4x3 + x4x2^3x3x2</polynomial>
    <polynomial>x2x4x2^2x1x4 - x2x4x2^2x4x1 - x4x2^3x1x4 + x4x2^3x4x1</polynomial>
    <polynomial>x2x4x2^2x1x3 - x2x4x2^2x3x1 - x4x2^3x1x3 + x4x2^3x3x1</polynomial>
    <polynomial>x2x4x2^2x1x2 - x2x4x2^3x1 - x4x2^3x1x2 + x4x2^4x1</polynomial>
    <polynomial>x2x4x2x1^2x4 - x2x4x2x1x4x1 - x4x2^2x1^2x4 + x4x2^2x1x4x1</polynomial>
    <polynomial>x2x4x2x1^2x3 - x2x4x2x1x3x1 - x4x2^2x1^2x3 + x4x2^2x1x3x1</polynomial>
    <polynomial>x2x4x2x1^2x2 - x2x4x2x1x2x1 - x4x2^2x1^2x2 + x4x2^2x1x2x1</polynomial>
    <polynomial>x2x4x1^3x4 - x2x4x1^2x4x1 - x4x2x1^3x4 + x4x2x1^2x4x1</polynomial>
    <polynomial>x2x4x1^3x3 - x2x4x1^2x3x1 - x4x2x1^3x3 + x4x2x1^2x3x1</polynomial>
    <polynomial>x2x4x1^3x2 - x2x4x1^2x2x1 - x4x2x1^3x2 + x4x2x1^2x2x1</polynomial>
    <polynomial>x2x3^4x4 - x2x3^3x4x3 - x3x2x3^3x4 + x3x2x3^2x4x3</polynomial>
    <polynomial>x2x3^3x2x4 - x2x3^3x4x2 - x3x2x3^2x2x4 + x3x2x3^2x4x2</polynomial>
    <polynomial>x2x3^3x2x3 - x2x3^4x2 - x3x2x3^2x2x3 + x3x2x3^3x2</polynomial>
    <polynomial>x2x3^3x1x4 - x2x3^3x4x1 - x3x2x3^2x1x4 + x3x2x3^2x4x1</polynomial>
    <polynomial>x2x3^3x1x3 - x2x3^4x1 - x3x2x3^2x1x3 + x3x2x3^3x1</polynomial>
    <polynomial>x2x3^3x1x2 - x2x3^3x2x1 - x3x2x3^2x1x2 + x3x2x3^2x2x1</polynomial>
    <polynomial>x2x3^2x2^2x4 - x2x3^2x2x4x2 - x3x2x3x2^2x4 + x3x2x3x2x4x2</polynomial>
    <polynomial>x2x3^2x2^2x3 - x2x3^2x2x3x2 - x3x2x3x2^2x3 + x3x2x3x2x3x2</polynomial>
    <polynomial>x2x3^2x2x1x4 - x2x3^2x2x4x1 - x3x2x3x2x1x4 + x3x2x3x2x4x1</polynomial>
    <polynomial>x2x3^2x2x1x3 - x2x3^2x2x3x1 - x3x2x3x2x1x3 + x3x2x3x2x3x1</polynomial>
    <polynomial>x2x3^2x2x1x2 - x2x3^2x2^2x1 - x3x2x3x2x1x2 + x3x2x3x2^2x1</polynomial>
    <polynomial>x2x3^2x1^2x4 - x2x3^2x1x4x1 - x3x2x3x1^2x4 + x3x2x3x1x4x1</polynomial>
    <polynomial>x2x3^2x1^2x3 - x2x3^2x1x3x1 - x3x2x3x1^2x3 + x3x2x3x1x3x1</polynomial>
    <polynomial>x2x3^2x1^2x2 - x2x3^2x1x2x1 - x3x2x3x1^2x2 + x3x2x3x1x2x1</polynomial>
    <polynomial>x2x3x2^3x4 - x2x3x2^2x4x2 - x3x2^4x4 + x3x2^3x4x2</polynomial>
    <polynomial>x2x3x2^3x3 - x2x3x2^2x3x2 - x3x2^4x3 + x3x2^3x3x2</polynomial>
    <polynomial>x2x3x2^2x1x4 - x2x3x2^2x4x1 - x3x2^3x1x4 + x3x2^3x4x1</polynomial>
    <polynomial>x2x3x2^2x1x3 - x2x3x2^2x3x1 - x3x2^3x1x3 + x3x2^3x3x1</polynomial>
    <polynomial>x2x3x2^2x1x2 - x2x3x2^3x1 - x3x2^3x1x2 + x3x2^4x1</polynomial>
    <polynomial>x2x3x2x1^2x4 - x2x3x2x1x4x1 - x3x2^2x1^2x4 + x3x2^2x1x4x1</polynomial>
    <polynomial>x2x3x2x1^2x3 - x2x3x2x1x3x1 - x3x2^2x1^2x3 + x3x2^2x1x3x1</polynomial>
    <polynomial>x2x3x2x1^2x2 - x2x3x2x1x2x1 - x3x2^2x1^2x2 + x3x2^2x1x2x1</polynomial>
    <polynomial>x2x3x1^3x4 - x2x3x1^2x4x1 - x3x2x1^3x4 + x3x2x1^2x4x1</polynomial>
    <polynomial>x2x3x1^3x3 - x2x3x1^2x3x1 - x3x2x1^3x3 + x3x2x1^2x3x1</polynomial>
    <polynomial>x2x3x1^3x2 - x2x3x1^2x2x1 - x3x2x1^3x2 + x3x2x1^2x2x1</polynomial>
    <polynomial>x1x4^3x3x4 - x1x4^4x3 - x4x1x4^2x3x4 + x4x1x4^3x3</polynomial>
    <polynomial>x1x4^3x2x4 - x1x4^4x2 - x4x1x4^2x2x4 + x4x1x4^3x2</polynomial>
    <polynomial>x1x4^3x2x3 - x1x4^3x3x2 - x4x1x4^2x2x3 + x4x1x4^2x3x2</polynomial>
    <polynomial>x1x4^3x1x4 - x1x4^4x1 - x4x1x4^2x1x4 + x4x1x4^3x1</polynomial>
    <polynomial>x1x4^3x1x3 - x1x4^3x3x1 - x4x1x4^2x1x3 + x4x1x4^2x3x1</polynomial>
    <polynomial>x1x4^3x1x2 - x1x4^3x2x1 - x4x1x4^2x1x2 + x4x1x4^2x2x1</polynomial>
    <polynomial>x1x4^2x3^2x4 - x1x4^2x3x4x3 - x4x1x4x3^2x4 + x4x1x4x3x4x3</polynomial>
    <polynomial>x1x4^2x3x2x4 - x1x4^2x3x4x2 - x4x1x4x3x2x4 + x4x1x4x3x4x2</polynomial>
    <polynomial>x1x4^2x3x2x3 - x1x4^2x3^2x2 - x4x1x4x3x2x3 + x4x1x4x3^2x2</polynomial>
    <polynomial>x1x4^2x3x1x4 - x1x4^2x3x4x1 - x4x1x4x3x1x4 + x4x1x4x3x4x1</polynomial>
    <polynomial>x1x4^2x3x1x3 - x1x4^2x3^2x1 - x4x1x4x3x1x3 + x4x1x4x3^2x1</polynomial>
    <polynomial>x1x4^2x3x1x2 - x1x4^2x3x2x1 - x4x1x4x3x1x2 + x4x1x4x3x2x1</polynomial>
    <polynomial>x1x4^2x2^2x4 - x1x4^2x2x4x2 - x4x1x4x2^2x4 + x4x1x4x2x4x2</polynomial>
    <polynomial>x1x4^2x2^2x3 - x1x4^2x2x3x2 - x4x1x4x2^2x3 + x4x1x4x2x3x2</polynomial>
    <polynomial>x1x4^2x2x1x4 - x1x4^2x2x4x1 - x4x1x4x2x1x4 + x4x1x4x2x4x1</polynomial>
    <polynomial>x1x4^2x2x1x3 - x1x4^2x2x3x1 - x4x1x4x2x1x3 + x4x1x4x2x3x1</polynomial>
    <polynomial>x1x4^2x2x1x2 - x1x4^2x2^2x1 - x4x1x4x2x1x2 + x4x1x4x2^2x1</polynomial>
    <polynomial>x1x4^2x1^2x4 - x1x4^2x1x4x1 - x4x1x4x1^2x4 + x4x1x4x1x4x1</polynomial>
    <polynomial>x1x4^2x1^2x3 - x1x4^2x1x3x1 - x4x1x4x1^2x3 + x4x1x4x1x3x1</polynomial>
    <polynomial>x1x4^2x1^2x2 - x1x4^2x1x2x1 - x4x1x4x1^2x2 + x4x1x4x1x2x1</polynomial>
    <polynomial>x1x4x3^3x4 - x1x4x3^2x4x3 - x4x1x3^3x4 + x4x1x3^2x4x3</polynomial>
    <polynomial>x1x4x3^2x2x4 - x1x4x3^2x4x2 - x4x1x3^2x2x4 + x4x1x3^2x4x2</polynomial>
    <polynomial>x1x4x3^2x2x3 - x1x4x3^3x2 - x4x1x3^2x2x3 + x4x1x3^3x2</polynomial>
    <polynomial>x1x4x3^2x1x4 - x1x4x3^2x4x1 - x4x1x3^2x1x4 + x4x1x3^2x4x1</polynomial>
    <polynomial>x1x4x3^2x1x3 - x1x4x3^3x1 - x4x1x3^2x1x3 + x4x1x3^3x1</polynomial>
    <polynomial>x1x4x3^2x1x2 - x1x4x3^2x2x1 - x4x1x3^2x1x2 + x4x1x3^2x2x1</polynomial>
    <polynomial>x1x4x3x2^2x4 - x1x4x3x2x4x2 - x4x1x3x2^2x4 + x4x1x3x2x4x2</polynomial>
    <polynomial>x1x4x3x2^2x3 - x1x4x3x2x3x2 - x4x1x3x2^2x3 + x4x1x3x2x3x2</polynomial>
    <polynomial>x1x4x3x2x1x4 - x1x4x3x2x4x1 - x4x1x3x2x1x4 + x4x1x3x2x4x1</polynomial>
    <polynomial>x1x4x3x2x1x3 - x1x4x3x2x3x1 - x4x1x3x2x1x3 + x4x1x3x2x3x1</polynomial>
    <polynomial>x1x4x3x2x1x2 - x1x4x3x2^2x1 - x4x1x3x2x1x2 + x4x1x3x2^2x1</polynomial>
    <polynomial>x1x4x3x1^2x4 - x1x4x3x1x4x1 - x4x1x3x1^2x4 + x4x1x3x1x4x1</polynomial>
    <polynomial>x1x4x3x1^2x3 - x1x4x3x1x3x1 - x4x1x3x1^2x3 + x4x1x3x1x3x1</polynomial>
    <polynomial>x1x4x3x1^2x2 - x1x4x3x1x2x1 - x4x1x3x1^2x2 + x4x1x3x1x2x1</polynomial>
    <polynomial>x1x4x2^3x4 - x1x4x2^2x4x2 - x4x1x2^3x4 + x4x1x2^2x4x2</polynomial>
    <polynomial>x1x4x2^3x3 - x1x4x2^2x3x2 - x4x1x2^3x3 + x4x1x2^2x3x2</polynomial>
    <polynomial>x1x4x2^2x1x4 - x1x4x2^2x4x1 - x4x1x2^2x1x4 + x4x1x2^2x4x1</polynomial>
    <polynomial>x1x4x2^2x1x3 - x1x4x2^2x3x1 - x4x1x2^2x1x3 + x4x1x2^2x3x1</polynomial>
    <polynomial>x1x4x2^2x1x2 - x1x4x2^3x1 - x4x1x2^2x1x2 + x4x1x2^3x1</polynomial>
    <polynomial>x1x4x2x1^2x4 - x1x4x2x1x4x1 - x4x1x2x1^2x4 + x4x1x2x1x4x1</polynomial>
    <polynomial>x1x4x2x1^2x3 - x1x4x2x1x3x1 - x4x1x2x1^2x3 + x4x1x2x1x3x1</polynomial>
    <polynomial>x1x4x2x1^2x2 - x1x4x2x1x2x1 - x4x1x2x1^2x2 + x4x1x2x1x2x1</polynomial>
    <polynomial>x1x4x1^3x4 - x1x4x1^2x4x1 - x4x1^4x4 + x4x1^3x4x1</polynomial>
    <polynomial>x1x4x1^3x3 - x1x4x1^2x3x1 - x4x1^4x3 + x4x1^3x3x1</polynomial>
    <polynomial>x1x4x1^3x2 - x1x4x1^2x2x1 - x4x1^4x2 + x4x1^3x2x1</polynomial>
    <polynomial>x1x3^4x4 - x1x3^3x4x3 - x3x1x3^3x4 + x3x1x3^2x4x3</polynomial>
    <polynomial>x1x3^3x2x4 - x1x3^3x4x2 - x3x1x3^2x2x4 + x3x1x3^2x4x2</polynomial>
    <polynomial>x1x3^3x2x3 - x1x3^4x2 - x3x1x3^2x2x3 + x3x1x3^3x2</polynomial>
    <polynomial>x1x3^3x1x4 - x1x3^3x4x1 - x3x1x3^2x1x4 + x3x1x3^2x4x1</polynomial>
    <polynomial>x1x3^3x1x3 - x1x3^4x1 - x3x1x3^2x1x3 + x3x1x3^3x1</polynomial>
    <polynomial>x1x3^3x1x2 - x1x3^3x2x1 - x3x1x3^2x1x2 + x3x1x3^2x2x1</polynomial>
    <polynomial>x1x3^2x2^2x4 - x1x3^2x2x4x2 - x3x1x3x2^2x4 + x3x1x3x2x4x2</polynomial>
    <polynomial>x1x3^2x2^2x3 - x1x3^2x2x3x2 - x3x1x3x2^2x3 + x3x1x3x2x3x2</polynomial>
    <polynomial>x1x3^2x2x1x4 - x1x3^2x2x4x1 - x3x1x3x2x1x4 + x3x1x3x2x4x1</polynomial>
    <polynomial>x1x3^2x2x1x3 - x1x3^2x2x3x1 - x3x1x3x2x1x3 + x3x1x3x2x3x1</polynomial>
    <polynomial>x1x3^2x2x1x2 - x1x3^2x2^2x1 - x3x1x3x2x1x2 + x3x1x3x2^2x1</polynomial>
    <polynomial>x1x3^2x1^2x4 - x1x3^2x1x4x1 - x3x1x3x1^2x4 + x3x1x3x1x4x1</polynomial>
    <polynomial>x1x3^2x1^2x3 - x1x3^2x1x3x1 - x3x1x3x1^2x3 + x3x1x3x1x3x1</polynomial>
    <polynomial>x1x3^2x1^2x2 - x1x3^2x1x2x1 - x3x1x3x1^2x2 + x3x1x3x1x2x1</polynomial>
    <polynomial>x1x3x2^3x4 - x1x3x2^2x4x2 - x3x1x2^3x4 + x3x1x2^2x4x2</polynomial>
    <polynomial>x1x3x2^3x3 - x1x3x2^2x3x2 - x3x1x2^3x3 + x3x1x2^2x3x2</polynomial>
    <polynomial>x1x3x2^2x1x4 - x1x3x2^2x4x1 - x3x1x2^2x1x4 + x3x1x2^2x4x1</polynomial>
    <polynomial>x1x3x2^2x1x3 - x1x3x2^2x3x1 - x3x1x2^2x1x3 + x3x1x2^2x3x1</polynomial>
    <polynomial>x1x3x2^2x1x2 - x1x3x2^3x1 - x3x1x2^2x1x2 + x3x1x2^3x1</polynomial>
    <polynomial>x1x3x2x1^2x4 - x1x3x2x1x4x1 - x3x1x2x1^2x4 + x3x1x2x1x4x1</polynomial>
    <polynomial>x1x3x2x1^2x3 - x1x3x2x1x3x1 - x3x1x2x1^2x3 + x3x1x2x1x3x1</polynomial>
    <polynomial>x1x3x2x1^2x2 - x1x3x2x1x2x1 - x3x1x2x1^2x2 + x3x1x2x1x2x1</polynomial>
    <polynomial>x1x3x1^3x4 - x1x3x1^2x4x1 - x3x1^4x4 + x3x1^3x4x1</polynomial>
    <polynomial>x1x3x1^3x3 - x1x3x1^2x3x1 - x3x1^4x3 + x3x1^3x3x1</polynomial>
    <polynomial>x1x3x1^3x2 - x1x3x1^2x2x1 - x3x1^4x2 + x3x1^3x2x1</polynomial>
    <polynomial>x1x2^4x4 - x1x2^3x4x2 - x2x1x2^3x4 + x2x1x2^2x4x2</polynomial>
    <polynomial>x1x2^4x3 - x1x2^3x3x2 - x2x1x2^3x3 + x2x1x2^2x3x2</polynomial>
    <polynomial>x1x2^3x1x4 - x1x2^3x4x1 - x2x1x2^2x1x4 + x2x1x2^2x4x1</polynomial>
    <polynomial>x1x2^3x1x3 - x1x2^3x3x1 - x2x1x2^2x1x3 + x2x1x2^2x3x1</polynomial>
    <polynomial>x1x2^3x1x2 - x1x2^4x1 - x2x1x2^2x1x2 + x2x1x2^3x1</polynomial>
    <polynomial>x1x2^2x1^2x4 - x1x2^2x1x4x1 - x2x1x2x1^2x4 + x2x1x2x1x4x1</polynomial>
    <polynomial>x1x2^2x1^2x3 - x1x2^2x1x3x1 - x2x1x2x1^2x3 + x2x1x2x1x3x1</polynomial>
    <polynomial>x1x2^2x1^2x2 - x1x2^2x1x2x1 - x2x1x2x1^2x2 + x2x1x2x1x2x1</polynomial>
    <polynomial>x1x2x1^3x4 - x1x2x1^2x4x1 - x2x1^4x4 + x2x1^3x4x1</polynomial>
    <polynomial>x1x2x1^3x3 - x1x2x1^2x3x1 - x2x1^4x3 + x2x1^3x3x1</polynomial>
    <polynomial>x1x2x1^3x2 - x1x2x1^2x2x1 - x2x1^4x2 + x2x1^3x2x1</polynomial>
    <polynomial>x3x4^4x3x4 - x3x4^5x3 - x4x3x4^3x3x4 + x4x3x4^4x3</polynomial>
    <polynomial>x3x4^4x2x4 - x3x4^5x2 - x4x3x4^3x2x4 + x4x3x4^4x2</polynomial>
    <polynomial>x3x4^4x2x3 - x3x4^4x3x2 - x4x3x4^3x2x3 + x4x3x4^3x3x2</polynomial>
    <polynomial>x3x4^4x1x4 - x3x4^5x1 - x4x3x4^3x1x4 + x4x3x4^4x1</polynomial>
    <polynomial>x3x4^4x1x3 - x3x4^4x3x1 - x4x3x4^3x1x3 + x4x3x4^3x3x1</polynomial>
    <polynomial>x3x4^4x1x2 - x3x4^4x2x1 - x4x3x4^3x1x2 + x4x3x4^3x2x1</polynomial>
    <polynomial>x3x4^3x3^2x4 - x3x4^3x3x4x3 - x4x3x4^2x3^2x4 + x4x3x4^2x3x4x3</polynomial>
    <polynomial>x3x4^3x3x2x4 - x3x4^3x3x4x2 - x4x3x4^2x3x2x4 + x4x3x4^2x3x4x2</polynomial>
    <polynomial>x3x4^3x3x2x3 - x3x4^3x3^2x2 - x4x3x4^2x3x2x3 + x4x3x4^2x3^2x2</polynomial>
    <polynomial>x3x4^3x3x1x4 - x3x4^3x3x4x1 - x4x3x4^2x3x1x4 + x4x3x4^2x3x4x1</polynomial>
    <polynomial>x3x4^3x3x1x3 - x3x4^3x3^2x1 - x4x3x4^2x3x1x3 + x4x3x4^2x3^2x1</polynomial>
    <polynomial>x3x4^3x3x1x2 - x3x4^3x3x2x1 - x4x3x4^2x3x1x2 + x4x3x4^2x3x2x1</polynomial>
    <polynomial>x3x4^3x2^2x4 - x3x4^3x2x4x2 - x4x3x4^2x2^2x4 + x4x3x4^2x2x4x2</polynomial>
    <polynomial>x3x4^3x2^2x3 - x3x4^3x2x3x2 - x4x3x4^2x2^2x3 + x4x3x4^2x2x3x2</polynomial>
    <polynomial>x3x4^3x2x1x4 - x3x4^3x2x4x1 - x4x3x4^2x2x1x4 + x4x3x4^2x2x4x1</polynomial>
    <polynomial>x3x4^3x2x1x3 - x3x4^3x2x3x1 - x4x3x4^2x2x1x3 + x4x3x4^2x2x3x1</polynomial>
    <polynomial>x3x4^3x2x1x2 - x3x4^3x2^2x1 - x4x3x4^2x2x1x2 + x4x3x4^2x2^2x1</polynomial>
    <polynomial>x3x4^3x1^2x4 - x3x4^3x1x4x1 - x4x3x4^2x1^2x4 + x4x3x4^2x1x4x1</polynomial>
    <polynomial>x3x4^3x1^2x3 - x3x4^3x1x3x1 - x4x3x4^2x1^2x3 + x4x3x4^2x1x3x1</polynomial>
    <polynomial>x3x4^3x1^2x2 - x3x4^3x1x2x1 - x4x3x4^2x1^2x2 + x4x3x4^2x1x2x1</polynomial>
    <polynomial>x3x4^2x3^3x4 - x3x4^2x3^2x4x3 - x4x3x4x3^3x4 + x4x3x4x3^2x4x3</polynomial>
    <polynomial>x3x4^2x3^2x2x4 - x3x4^2x3^2x4x2 - x4x3x4x3^2x2x4 + x4x3x4x3^2x4x2</polynomial>
    <polynomial>x3x4^2x3^2x2x3 - x3x4^2x3^3x2 - x4x3x4x3^2x2x3 + x4x3x4x3^3x2</polynomial>
    <polynomial>x3x4^2x3^2x1x4 - x3x4^2x3^2x4x1 - x4x3x4x3^2x1x4 + x4x3x4x3^2x4x1</polynomial>
    <polynomial>x3x4^2x3^2x1x3 - x3x4^2x3^3x1 - x4x3x4x3^2x1x3 + x4x3x4x3^3x1</polynomial>
    <polynomial>x3x4^2x3^2x1x2 - x3x4^2x3^2x2x1 - x4x3x4x3^2x1x2 + x4x3x4x3^2x2x1</polynomial>
    <polynomial>x3x4^2x3x2^2x4 - x3x4^2x3x2x4x2 - x4x3x4x3x2^2x4 + x4x3x4x3x2x4x2</polynomial>
    <polynomial>x3x4^2x3x2^2x3 - x3x4^2x3x2x3x2 - x4x3x4x3x2^2x3 + x4x3x4x3x2x3x2</polynomial>
    <polynomial>x3x4^2x3x2x1x4 - x3x4^2x3x2x4x1 - x4x3x4x3x2x1x4 + x4x3x4x3x2x4x1</polynomial>
    <polynomial>x3x4^2x3x2x1x3 - x3x4^2x3x2x3x1 - x4x3x4x3x2x1x3 + x4x3x4x3x2x3x1</polynomial>
    <polynomial>x3x4^2x3x2x1x2 - x3x4^2x3x2^2x1 - x4x3x4x3x2x1x2 + x4x3x4x3x2^2x1</polynomial>
    <polynomial>x3x4^2x3x1^2x4 - x3x4^2x3x1x4x1 - x4x3x4x3x1^2x4 + x4x3x4x3x1x4x1</polynomial>
    <polynomial>x3x4^2x3x1^2x3 - x3x4^2x3x1x3x1 - x4x3x4x3x1^2x3 + x4x3x4x3x1x3x1</polynomial>
    <polynomial>x3x4^2x3x1^2x2 - x3x4^2x3x1x2x1 - x4x3x4x3x1^2x2 + x4x3x4x3x1x2x1</polynomial>
    <polynomial>x3x4^2x2^3x4 - x3x4^2x2^2x4x2 - x4x3x4x2^3x4 + x4x3x4x2^2x4x2</polynomial>
    <polynomial>x3x4^2x2^3x3 - x3x4^2x2^2x3x2 - x4x3x4x2^3x3 + x4x3x4x2^2x3x2</polynomial>
    <polynomial>x3x4^2x2^2x1x4 - x3x4^2x2^2x4x1 - x4x3x4x2^2x1x4 + x4x3x4x2^2x4x1</polynomial>
    <polynomial>x3x4^2x2^2x1x3 - x3x4^2x2^2x3x1 - x4x3x4x2^2x1x3 + x4x3x4x2^2x3x1</polynomial>
    <polynomial>x3x4^2x2^2x1x2 - x3x4^2x2^3x1 - x4x3x4x2^2x1x2 + x4x3x4x2^3x1</polynomial>
    <polynomial>x3x4^2x2x1^2x4 - x3x4^2x2x1x4x1 - x4x3x4x2x1^2x4 + x4x3x4x2x1x4x1</polynomial>
    <polynomial>x3x4^2x2x1^2x3 - x3x4^2x2x1x3x1 - x4x3x4x2x1^2x3 + x4x3x4x2x1x3x1</polynomial>
    <polynomial>x3x4^2x2x1^2x2 - x3x4^2x2x1x2x1 - x4x3x4x2x1^2x2 + x4x3x4x2x1x2x1</polynomial>
    <polynomial>x3x4^2x1^3x4 - x3x4^2x1^2x4x1 - x4x3x4x1^3x4 + x4x3x4x1^2x4x1</polynomial>
    <polynomial>x3x4^2x1^3x3 - x3x4^2x1^2x3x1 - x4x3x4x1^3x3 + x4x3x4x1^2x3x1</polynomial>
    <polynomial>x3x4^2x1^3x2 - x3x4^2x1^2x2x1 - x4x3x4x1^3x2 + x4x3x4x1^2x2x1</polynomial>
    <polynomial>x3x4x3^4x4 - x3x4x3^3x4x3 - x4x3^5x4 + x4x3^4x4x3</polynomial>
    <polynomial>x3x4x3^3x2x4 - x3x4x3^3x4x2 - x4x3^4x2x4 + x4x3^4x4x2</polynomial>
    <polynomial>x3x4x3^3x2x3 - x3x4x3^4x2 - x4x3^4x2x3 + x4x3^5x2</polynomial>
    <polynomial>x3x4x3^3x1x4 - x3x4x3^3x4x1 - x4x3^4x1x4 + x4x3^4x4x1</polynomial>
    <polynomial>x3x4x3^3x1x3 - x3x4x3^4x1 - x4x3^4x1x3 + x4x3^5x1</polynomial>
    <polynomial>x3x4x3^3x1x2 - x3x4x3^3x2x1 - x4x3^4x1x2 + x4x3^4x2x1</polynomial>
    <polynomial>x3x4x3^2x2^2x4 - x3x4x3^2x2x4x2 - x4x3^3x2^2x4 + x4x3^3x2x4x2</polynomial>
    <polynomial>x3x4x3^2x2^2x3 - x3x4x3^2x2x3x2 - x4x3^3x2^2x3 + x4x3^3x2x3x2</polynomial>
    <polynomial>x3x4x3^2x2x1x4 - x3x4x3^2x2x4x1 - x4x3^3x2x1x4 + x4x3^3x2x4x1</polynomial>
    <polynomial>x3x4x3^2x2x1x3 - x3x4x3^2x2x3x1 - x4x3^3x2x1x3 + x4x3^3x2x3x1</polynomial>
    <polynomial>x3x4x3^2x2x1x2 - x3x4x3^2x2^2x1 - x4x3^3x2x1x2 + x4x3^3x2^2x1</polynomial>
    <polynomial>x3x4x3^2x1^2x4 - x3x4x3^2x1x4x1 - x4x3^3x1^2x4 + x4x3^3x1x4x1</polynomial>
    <polynomial>x3x4x3^2x1^2x3 - x3x4x3^2x1x3x1 - x4x3^3x1^2x3 + x4x3^3x1x3x1</polynomial>
    <polynomial>x3x4x3^2x1^2x2 - x3x4x3^2x1x2x1 - x4x3^3x1^2x2 + x4x3^3x1x2x1</polynomial>
    <polynomial>x3x4x3x2^3x4 - x3x4x3x2^2x4x2 - x4x3^2x2^3x4 + x4x3^2x2^2x4x2</polynomial>
    <polynomial>x3x4x3x2^3x3 - x3x4x3x2^2x3x2 - x4x3^2x2^3x3 + x4x3^2x2^2x3x2</polynomial>
    <polynomial>x3x4x3x2^2x1x4 - x3x4x3x2^2x4x1 - x4x3^2x2^2x1x4 + x4x3^2x2^2x4x1</polynomial>
    <polynomial>x3x4x3x2^2x1x3 - x3x4x3x2^2x3x1 - x4x3^2x2^2x1x3 + x4x3^2x2^2x3x1</polynomial>
    <polynomial>x3x4x3x2^2x1x2 - x3x4x3x2^3x1 - x4x3^2x2^2x1x2 + x4x3^2x2^3x1</polynomial>
    <polynomial>x3x4x3x2x1^2x4 - x3x4x3x2x1x4x1 - x4x3^2x2x1^2x4 + x4x3^2x2x1x4x1</polynomial>
    <polynomial>x3x4x3x2x1^2x3 - x3x4x3x2x1x3x1 - x4x3^2x2x1^2x3 + x4x3^2x2x1x3x1</polynomial>
    <polynomial>x3x4x3x2x1^2x2 - x3x4x3x2x1x2x1 - x4x3^2x2x1^2x2 + x4x3^2x2x1x2x1</polynomial>
    <polynomial>x3x4x3x1^3x4 - x3x4x3x1^2x4x1 - x4x3^2x1^3x4 + x4x3^2x1^2x4x1</polynomial>
    <polynomial>x3x4x3x1^3x3 - x3x4x3x1^2x3x1 - x4x3^2x1^3x3 + x4x3^2x1^2x3x1</polynomial>
    <polynomial>x3x4x3x1^3x2 - x3x4x3x1^2x2x1 - x4x3^2x1^3x2 + x4x3^2x1^2x2x1</polynomial>
    <polynomial>x3x4x2^4x4 - x3x4x2^3x4x2 - x4x3x2^4x4 + x4x3x2^3x4x2</polynomial>
    <polynomial>x3x4x2^4x3 - x3x4x2^3x3x2 - x4x3x2^4x3 + x4x3x2^3x3x2</polynomial>
    <polynomial>x3x4x2^3x1x4 - x3x4x2^3x4x1 - x4x3x2^3x1x4 + x4x3x2^3x4x1</polynomial>
    <polynomial>x3x4x2^3x1x3 - x3x4x2^3x3x1 - x4x3x2^3x1x3 + x4x3x2^3x3x1</polynomial>
    <polynomial>x3x4x2^3x1x2 - x3x4x2^4x1 - x4x3x2^3x1x2 + x4x3x2^4x1</polynomial>
    <polynomial>x3x4x2^2x1^2x4 - x3x4x2^2x1x4x1 - x4x3x2^2x1^2x4 + x4x3x2^2x1x4x1</polynomial>
    <polynomial>x3x4x2^2x1^2x3 - x3x4x2^2x1x3x1 - x4x3x2^2x1^2x3 + x4x3x2^2x1x3x1</polynomial>
    <polynomial>x3x4x2^2x1^2x2 - x3x4x2^2x1x2x1 - x4x3x2^2x1^2x2 + x4x3x2^2x1x2x1</polynomial>
    <polynomial>x3x4x2x1^3x4 - x3x4x2x1^2x4x1 - x4x3x2x1^3x4 + x4x3x2x1^2x4x1</polynomial>
    <polynomial>x3x4x2x1^3x3 - x3x4x2x1^2x3x1 - x4x3x2x1^3x3 + x4x3x2x1^2x3x1</polynomial>
    <polynomial>x3x4x2x1^3x2 - x3x4x2x1^2x2x1 - x4x3x2x1^3x2 + x4x3x2x1^2x2x1</polynomial>
    <polynomial>x3x4x1^4x4 - x3x4x1^3x4x1 - x4x3x1^4x4 + x4x3x1^3x4x1</polynomial>
    <polynomial>x3x4x1^4x3 - x3x4x1^3x3x1 - x4x3x1^4x3 + x4x3x1^3x3x1</polynomial>
    <polynomial>x3x4x1^4x2 - x3x4x1^3x2x1 - x4x3x1^4x2 + x4x3x1^3x2x1</polynomial>
    <polynomial>x2x4^4x3x4 - x2x4^5x3 - x4x2x4^3x3x4 + x4x2x4^4x3</polynomial>
    <polynomial>x2x4^4x2x4 - x2x4^5x2 - x4x2x4^3x2x4 + x4x2x4^4x2</polynomial>
    <polynomial>x2x4^4x2x3 - x2x4^4x3x2 - x4x2x4^3x2x3 + x4x2x4^3x3x2</polynomial>
    <polynomial>x2x4^4x1x4 - x2x4^5x1 - x4x2x4^3x1x4 + x4x2x4^4x1</polynomial>
    <polynomial>x2x4^4x1x3 - x2x4^4x3x1 - x4x2x4^3x1x3 + x4x2x4^3x3x1</polynomial>
    <polynomial>x2x4^4x1x2 - x2x4^4x2x1 - x4x2x4^3x1x2 + x4x2x4^3x2x1</polynomial>
    <polynomial>x2x4^3x3^2x4 - x2x4^3x3x4x3 - x4x2x4^2x3^2x4 + x4x2x4^2x3x4x3</polynomial>
    <polynomial>x2x4^3x3x2x4 - x2x4^3x3x4x2 - x4x2x4^2x3x2x4 + x4x2x4^2x3x4x2</polynomial>
    <polynomial>x2x4^3x3x2x3 - x2x4^3x3^2x2 - x4x2x4^2x3x2x3 + x4x2x4^2x3^2x2</polynomial>
    <polynomial>x2x4^3x3x1x4 - x2x4^3x3x4x1 - x4x2x4^2x3x1x4 + x4x2x4^2x3x4x1</polynomial>
    <polynomial>x2x4^3x3x1x3 - x2x4^3x3^2x1 - x4x2x4^2x3x1x3 + x4x2x4^2x3^2x1</polynomial>
    <polynomial>x2x4^3x3x1x2 - x2x4^3x3x2x1 - x4x2x4^2x3x1x2 + x4x2x4^2x3x2x1</polynomial>
    <polynomial>x2x4^3x2^2x4 - x2x4^3x2x4x2 - x4x2x4^2x2^2x4 + x4x2x4^2x2x4x2</polynomial>
    <polynomial>x2x4^3x2^2x3 - x2x4^3x2x3x2 - x4x2x4^2x2^2x3 + x4x2x4^2x2x3x2</polynomial>
    <polynomial>x2x4^3x2x1x4 - x2x4^3x2x4x1 - x4x2x4^2x2x1x4 + x4x2x4^2x2x4x1</polynomial>
    <polynomial>x2x4^3x2x1x3 - x2x4^3x2x3x1 - x4x2x4^2x2x1x3 + x4x2x4^2x2x3x1</polynomial>
    <polynomial>x2x4^3x2x1x2 - x2x4^3x2^2x1 - x4x2x4^2x2x1x2 + x4x2x4^2x2^2x1</polynomial>
    <polynomial>x2x4^3x1^2x4 - x2x4^3x1x4x1 - x4x2x4^2x1^2x4 + x4x2x4^2x1x4x1</polynomial>
    <polynomial>x2x4^3x1^2x3 - x2x4^3x1x3x1 - x4x2x4^2x1^2x3 + x4x2x4^2x1x3x1</polynomial>
    <polynomial>x2x4^3x1^2x2 - x2x4^3x1x2x1 - x4x2x4^2x1^2x2 + x4x2x4^2x1x2x1</polynomial>
    <polynomial>x2x4^2x3^3x4 - x2x4^2x3^2x4x3 - x4x2x4x3^3x4 + x4x2x4x3^2x4x3</polynomial>
    <polynomial>x2x4^2x3^2x2x4 - x2x4^2x3^2x4x2 - x4x2x4x3^2x2x4 + x4x2x4x3^2x4x2</polynomial>
    <polynomial>x2x4^2x3^2x2x3 - x2x4^2x3^3x2 - x4x2x4x3^2x2x3 + x4x2x4x3^3x2</polynomial>
    <polynomial>x2x4^2x3^2x1x4 - x2x4^2x3^2x4x1 - x4x2x4x3^2x1x4 + x4x2x4x3^2x4x1</polynomial>
    <polynomial>x2x4^2x3^2x1x3 - x2x4^2x3^3x1 - x4x2x4x3^2x1x3 + x4x2x4x3^3x1</polynomial>
    <polynomial>x2x4^2x3^2x1x2 - x2x4^2x3^2x2x1 - x4x2x4x3^2x1x2 + x4x2x4x3^2x2x1</polynomial>
    <polynomial>x2x4^2x3x2^2x4 - x2x4^2x3x2x4x2 - x4x2x4x3x2^2x4 + x4x2x4x3x2x4x2</polynomial>
    <polynomial>x2x4^2x3x2^2x3 - x2x4^2x3x2x3x2 - x4x2x4x3x2^2x3 + x4x2x4x3x2x3x2</polynomial>
    <polynomial>x2x4^2x3x2x1x4 - x2x4^2x3x2x4x1 - x4x2x4x3x2x1x4 + x4x2x4x3x2x4x1</polynomial>
    <polynomial>x2x4^2x3x2x1x3 - x2x4^2x3x2x3x1 - x4x2x4x3x2x1x3 + x4x2x4x3x2x3x1</polynomial>
    <polynomial>x2x4^2x3x2x1x2 - x2x4^2x3x2^2x1 - x4x2x4x3x2x1x2 + x4x2x4x3x2^2x1</polynomial>
    <polynomial>x2x4^2x3x1^2x4 - x2x4^2x3x1x4x1 - x4x2x4x3x1^2x4 + x4x2x4x3x1x4x1</polynomial>
    <polynomial>x2x4^2x3x1^2x3 - x2x4^2x3x1x3x1 - x4x2x4x3x1^2x3 + x4x2x4x3x1x3x1</polynomial>
    <polynomial>x2x4^2x3x1^2x2 - x2x4^2x3x1x2x1 - x4x2x4x3x1^2x2 + x4x2x4x3x1x2x1</polynomial>
    <polynomial>x2x4^2x2^3x4 - x2x4^2x2^2x4x2 - x4x2x4x2^3x4 + x4x2x4x2^2x4x2</polynomial>
    <polynomial>x2x4^2x2^3x3 - x2x4^2x2^2x3x2 - x4x2x4x2^3x3 + x4x2x4x2^2x3x2</polynomial>
    <polynomial>x2x4^2x2^2x1x4 - x2x4^2x2^2x4x1 - x4x2x4x2^2x1x4 + x4x2x4x2^2x4x1</polynomial>
    <polynomial>x2x4^2x2^2x1x3 - x2x4^2x2^2x3x1 - x4x2x4x2^2x1x3 + x4x2x4x2^2x3x1</polynomial>
    <polynomial>x2x4^2x2^2x1x2 - x2x4^2x2^3x1 - x4x2x4x2^2x1x2 + x4x2x4x2^3x1</polynomial>
    <polynomial>x2x4^2x2x1^2x4 - x2x4^2x2x1x4x1 - x4x2x4x2x1^2x4 + x4x2x4x2x1x4x1</polynomial>
    <polynomial>x2x4^2x2x1^2x3 - x2x4^2x2x1x3x1 - x4x2x4x2x1^2x3 + x4x2x4x2x1x3x1</polynomial>
    <polynomial>x2x4^2x2x1^2x2 - x2x4^2x2x1x2x1 - x4x2x4x2x1^2x2 + x4x2x4x2x1x2x1</polynomial>
    <polynomial>x2x4^2x1^3x4 - x2x4^2x1^2x4x1 - x4x2x4x1^3x4 + x4x2x4x1^2x4x1</polynomial>
    <polynomial>x2x4^2x1^3x3 - x2x4^2x1^2x3x1 - x4x2x4x1^3x3 + x4x2x4x1^2x3x1</polynomial>
    <polynomial>x2x4^2x1^3x2 - x2x4^2x1^2x2x1 - x4x2x4x1^3x2 + x4x2x4x1^2x2x1</polynomial>
    <polynomial>x2x4x3^4x4 - x2x4x3^3x4x3 - x4x2x3^4x4 + x4x2x3^3x4x3</polynomial>
    <polynomial>x2x4x3^3x2x4 - x2x4x3^3x4x2 - x4x2x3^3x2x4 + x4x2x3^3x4x2</polynomial>
    <polynomial>x2x4x3^3x2x3 - x2x4x3^4x2 - x4x2x3^3x2x3 + x4x2x3^4x2</polynomial>
    <polynomial>x2x4x3^3x1x4 - x2x4x3^3x4x1 - x4x2x3^3x1x4 + x4x2x3^3x4x1</polynomial>
    <polynomial>x2x4x3^3x1x3 - x2x4x3^4x1 - x4x2x3^3x1x3 + x4x2x3^4x1</polynomial>
    <polynomial>x2x4x3^3x1x2 - x2x4x3^3x2x1 - x4x2x3^3x1x2 + x4x2x3^3x2x1</polynomial>
    <polynomial>x2x4x3^2x2^2x4 - x2x4x3^2x2x4x2 - x4x2x3^2x2^2x4 + x4x2x3^2x2x4x2</polynomial>
    <polynomial>x2x4x3^2x2^2x3 - x2x4x3^2x2x3x2 - x4x2x3^2x2^2x3 + x4x2x3^2x2x3x2</polynomial>
    <polynomial>x2x4x3^2x2x1x4 - x2x4x3^2x2x4x1 - x4x2x3^2x2x1x4 + x4x2x3^2x2x4x1</polynomial>
    <polynomial>x2x4x3^2x2x1x3 - x2x4x3^2x2x3x1 - x4x2x3^2x2x1x3 + x4x2x3^2x2x3x1</polynomial>
    <polynomial>x2x4x3^2x2x1x2 - x2x4x3^2x2^2x1 - x4x2x3^2x2x1x2 + x4x2x3^2x2^2x1</polynomial>
    <polynomial>x2x4x3^2x1^2x4 - x2x4x3^2x1x4x1 - x4x2x3^2x1^2x4 + x4x2x3^2x1x4x1</polynomial>
    <polynomial>x2x4x3^2x1^2x3 - x2x4x3^2x1x3x1 - x4x2x3^2x1^2x3 + x4x2x3^2x1x3x1</polynomial>
    <polynomial>x2x4x3^2x1^2x2 - x2x4x3^2x1x2x1 - x4x2x3^2x1^2x2 + x4x2x3^2x1x2x1</polynomial>
    <polynomial>x2x4x3x2^3x4 - x2x4x3x2^2x4x2 - x4x2x3x2^3x4 + x4x2x3x2^2x4x2</polynomial>
    <polynomial>x2x4x3x2^3x3 - x2x4x3x2^2x3x2 - x4x2x3x2^3x3 + x4x2x3x2^2x3x2</polynomial>
    <polynomial>x2x4x3x2^2x1x4 - x2x4x3x2^2x4x1 - x4x2x3x2^2x1x4 + x4x2x3x2^2x4x1</polynomial>
    <polynomial>x2x4x3x2^2x1x3 - x2x4x3x2^2x3x1 - x4x2x3x2^2x1x3 + x4x2x3x2^2x3x1</polynomial>
    <polynomial>x2x4x3x2^2x1x2 - x2x4x3x2^3x1 - x4x2x3x2^2x1x2 + x4x2x3x2^3x1</polynomial>
    <polynomial>x2x4x3x2x1^2x4 - x2x4x3x2x1x4x1 - x4x2x3x2x1^2x4 + x4x2x3x2x1x4x1</polynomial>
    <polynomial>x2x4x3x2x1^2x3 - x2x4x3x2x1x3x1 - x4x2x3x2x1^2x3 + x4x2x3x2x1x3x1</polynomial>
    <polynomial>x2x4x3x2x1^2x2 - x2x4x3x2x1x2x1 - x4x2x3x2x1^2x2 + x4x2x3x2x1x2x1</polynomial>
    <polynomial>x2x4x3x1^3x4 - x2x4x3x1^2x4x1 - x4x2x3x1^3x4 + x4x2x3x1^2x4x1</polynomial>
    <polynomial>x2x4x3x1^3x3 - x2x4x3x1^2x3x1 - x4x2x3x1^3x3 + x4x2x3x1^2x3x1</polynomial>
    <polynomial>x2x4x3x1^3x2 - x2x4x3x1^2x2x1 - x4x2x3x1^3x2 + x4x2x3x1^2x2x1</polynomial>
    <polynomial>x2x4x2^4x4 - x2x4x2^3x4x2 - x4x2^5x4 + x4x2^4x4x2</polynomial>
    <polynomial>x2x4x2^4x3 - x2x4x2^3x3x2 - x4x2^5x3 + x4x2^4x3x2</polynomial>
    <polynomial>x2x4x2^3x1x4 - x2x4x2^3x4x1 - x4x2^4x1x4 + x4x2^4x4x1</polynomial>
    <polynomial>x2x4x2^3x1x3 - x2x4x2^3x3x1 - x4x2^4x1x3 + x4x2^4x3x1</polynomial>
    <polynomial>x2x4x2^3x1x2 - x2x4x2^4x1 - x4x2^4x1x2 + x4x2^5x1</polynomial>
    <polynomial>x2x4x2^2x1^2x4 - x2x4x2^2x1x4x1 - x4x2^3x1^2x4 + x4x2^3x1x4x1</polynomial>
    <polynomial>x2x4x2^2x1^2x3 - x2x4x2^2x1x3x1 - x4x2^3x1^2x3 + x4x2^3x1x3x1</polynomial>
    <polynomial>x2x4x2^2x1^2x2 - x2x4x2^2x1x2x1 - x4x2^3x1^2x2 + x4x2^3x1x2x1</polynomial>
    <polynomial>x2x4x2x1^3x4 - x2x4x2x1^2x4x1 - x4x2^2x1^3x4 + x4x2^2x1^2x4x1</polynomial>
    <polynomial>x2x4x2x1^3x3 - x2x4x2x1^2x3x1 - x4x2^2x1^3x3 + x4x2^2x1^2x3x1</polynomial>
    <polynomial>x2x4x2x1^3x2 - x2x4x2x1^2x2x1 - x4x2^2x1^3x2 + x4x2^2x1^2x2x1</polynomial>
    <polynomial>x2x4x1^4x4 - x2x4x1^3x4x1 - x4x2x1^4x4 + x4x2x1^3x4x1</polynomial>
    <polynomial>x2x4x1^4x3 - x2x4x1^3x3x1 - x4x2x1^4x3 + x4x2x1^3x3x1</polynomial>
    <polynomial>x2x4x1^4x2 - x2x4x1^3x2x1 - x4x2x1^4x2 + x4x2x1^3x2x1</polynomial>
    <polynomial>x2x3^5x4 - x2x3^4x4x3 - x3x2x3^4x4 + x3x2x3^3x4x3</polynomial>
    <polynomial>x2x3^4x2x4 - x2x3^4x4x2 - x3x2x3^3x2x4 + x3x2x3^3x4x2</polynomial>
    <polynomial>x2x3^4x2x3 - x2x3^5x2 - x3x2x3^3x2x3 + x3x2x3^4x2</polynomial>
    <polynomial>x2x3^4x1x4 - x2x3^4x4x1 - x3x2x3^3x1x4 + x3x2x3^3x4x1</polynomial>
    <polynomial>x2x3^4x1x3 - x2x3^5x1 - x3x2x3^3x1x3 + x3x2x3^4x1</polynomial>
    <polynomial>x2x3^4x1x2 - x2x3^4x2x1 - x3x2x3^3x1x2 + x3x2x3^3x2x1</polynomial>
    <polynomial>x2x3^3x2^2x4 - x2x3^3x2x4x2 - x3x2x3^2x2^2x4 + x3x2x3^2x2x4x2</polynomial>
    <polynomial>x2x3^3x2^2x3 - x2x3^3x2x3x2 - x3x2x3^2x2^2x3 + x3x2x3^2x2x3x2</polynomial>
    <polynomial>x2x3^3x2x1x4 - x2x3^3x2x4x1 - x3x2x3^2x2x1x4 + x3x2x3^2x2x4x1</polynomial>
    <polynomial>x2x3^3x2x1x3 - x2x3^3x2x3x1 - x3x2x3^2x2x1x3 + x3x2x3^2x2x3x1</polynomial>
    <polynomial>x2x3^3x2x1x2 - x2x3^3x2^2x1 - x3x2x3^2x2x1x2 + x3x2x3^2x2^2x1</polynomial>
    <polynomial>x2x3^3x1^2x4 - x2x3^3x1x4x1 - x3x2x3^2x1^2x4 + x3x2x3^2x1x4x1</polynomial>
    <polynomial>x2x3^3x1^2x3 - x2x3^3x1x3x1 - x3x2x3^2x1^2x3 + x3x2x3^2x1x3x1</polynomial>
    <polynomial>x2x3^3x1^2x2 - x2x3^3x1x2x1 - x3x2x3^2x1^2x2 + x3x2x3^2x1x2x1</polynomial>
    <polynomial>x2x3^2x2^3x4 - x2x3^2x2^2x4x2 - x3x2x3x2^3x4 + x3x2x3x2^2x4x2</polynomial>
    <polynomial>x2x3^2x2^3x3 - x2x3^2x2^2x3x2 - x3x2x3x2^3x3 + x3x2x3x2^2x3x2</polynomial>
    <polynomial>x2x3^2x2^2x1x4 - x2x3^2x2^2x4x1 - x3x2x3x2^2x1x4 + x3x2x3x2^2x4x1</polynomial>
    <polynomial>x2x3^2x2^2x1x3 - x2x3^2x2^2x3x1 - x3x2x3x2^2x1x3 + x3x2x3x2^2x3x1</polynomial>
    <polynomial>x2x3^2x2^2x1x2 - x2x3^2x2^3x1 - x3x2x3x2^2x1x2 + x3x2x3x2^3x1</polynomial>
    <polynomial>x2x3^2x2x1^2x4 - x2x3^2x2x1x4x1 - x3x2x3x2x1^2x4 + x3x2x3x2x1x4x1</polynomial>
    <polynomial>x2x3^2x2x1^2x3 - x2x3^2x2x1x3x1 - x3x2x3x2x1^2x3 + x3x2x3x2x1x3x1</polynomial>
    <polynomial>x2x3^2x2x1^2x2 - x2x3^2x2x1x2x1 - x3x2x3x2x1^2x2 + x3x2x3x2x1x2x1</polynomial>
    <polynomial>x2x3^2x1^3x4 - x2x3^2x1^2x4x1 - x3x2x3x1^3x4 + x3x2x3x1^2x4x1</polynomial>
    <polynomial>x2x3^2x1^3x3 - x2x3^2x1^2x3x1 - x3x2x3x1^3x3 + x3x2x3x1^2x3x1</polynomial>
    <polynomial>x2x3^2x1^3x2 - x2x3^2x1^2x2x1 - x3x2x3x1^3x2 + x3x2x3x1^2x2x1</polynomial>
    <polynomial>x2x3x2^4x4 - x2x3x2^3x4x2 - x3x2^5x4 + x3x2^4x4x2</polynomial>
    <polynomial>x2x3x2^4x3 - x2x3x2^3x3x2 - x3x2^5x3 + x3x2^4x3x2</polynomial>
    <polynomial>x2x3x2^3x1x4 - x2x3x2^3x4x1 - x3x2^4x1x4 + x3x2^4x4x1</polynomial>
    <polynomial>x2x3x2^3x1x3 - x2x3x2^3x3x1 - x3x2^4x1x3 + x3x2^4x3x1</polynomial>
    <polynomial>x2x3x2^3x1x2 - x2x3x2^4x1 - x3x2^4x1x2 + x3x2^5x1</polynomial>
    <polynomial>x2x3x2^2x1^2x4 - x2x3x2^2x1x4x1 - x3x2^3x1^2x4 + x3x2^3x1x4x1</polynomial>
    <polynomial>x2x3x2^2x1^2x3 - x2x3x2^2x1x3x1 - x3x2^3x1^2x3 + x3x2^3x1x3x1</polynomial>
    <polynomial>x2x3x2^2x1^2x2 - x2x3x2^2x1x2x1 - x3x2^3x1^2x2 + x3x2^3x1x2x1</polynomial>
    <polynomial>x2x3x2x1^3x4 - x2x3x2x1^2x4x1 - x3x2^2x1^3x4 + x3x2^2x1^2x4x1</polynomial>
    <polynomial>x2x3x2x1^3x3 - x2x3x2x1^2x3x1 - x3x2^2x1^3x3 + x3x2^2x1^2x3x1</polynomial>
    <polynomial>x2x3x2x1^3x2 - x2x3x2x1^2x2x1 - x3x2^2x1^3x2 + x3x2^2x1^2x2x1</polynomial>
    <polynomial>x2x3x1^4x4 - x2x3x1^3x4x1 - x3x2x1^4x4 + x3x2x1^3x4x1</polynomial>
    <polynomial>x2x3x1^4x3 - x2x3x1^3x3x1 - x3x2x1^4x3 + x3x2x1^3x3x1</polynomial>
    <polynomial>x2x3x1^4x2 - x2x3x1^3x2x1 - x3x2x1^4x2 + x3x2x1^3x2x1</polynomial>
    <polynomial>x1x4^4x3x4 - x1x4^5x3 - x4x1x4^3x3x4 + x4x1x4^4x3</polynomial>
    <polynomial>x1x4^4x2x4 - x1x4^5x2 - x4x1x4^3x2x4 + x4x1x4^4x2</polynomial>
    <polynomial>x1x4^4x2x3 - x1x4^4x3x2 - x4x1x4^3x2x3 + x4x1x4^3x3x2</polynomial>
    <polynomial>x1x4^4x1x4 - x1x4^5x1 - x4x1x4^3x1x4 + x4x1x4^4x1</polynomial>
    <polynomial>x1x4^4x1x3 - x1x4^4x3x1 - x4x1x4^3x1x3 + x4x1x4^3x3x1</polynomial>
    <polynomial>x1x4^4x1x2 - x1x4^4x2x1 - x4x1x4^3x1x2 + x4x1x4^3x2x1</polynomial>
    <polynomial>x1x4^3x3^2x4 - x1x4^3x3x4x3 - x4x1x4^2x3^2x4 + x4x1x4^2x3x4x3</polynomial>
    <polynomial>x1x4^3x3x2x4 - x1x4^3x3x4x2 - x4x1x4^2x3x2x4 + x4x1x4^2x3x4x2</polynomial>
    <polynomial>x1x4^3x3x2x3 - x1x4^3x3^2x2 - x4x1x4^2x3x2x3 + x4x1x4^2x3^2x2</polynomial>
    <polynomial>x1x4^3x3x1x4 - x1x4^3x3x4x1 - x4x1x4^2x3x1x4 + x4x1x4^2x3x4x1</polynomial>
    <polynomial>x1x4^3x3x1x3 - x1x4^3x3^2x1 - x4x1x4^2x3x1x3 + x4x1x4^2x3^2x1</polynomial>
    <polynomial>x1x4^3x3x1x2 - x1x4^3x3x2x1 - x4x1x4^2x3x1x2 + x4x1x4^2x3x2x1</polynomial>
    <polynomial>x1x4^3x2^2x4 - x1x4^3x2x4x2 - x4x1x4^2x2^2x4 + x4x1x4^2x2x4x2</polynomial>
    <polynomial>x1x4^3x2^2x3 - x1x4^3x2x3x2 - x4x1x4^2x2^2x3 + x4x1x4^2x2x3x2</polynomial>
    <polynomial>x1x4^3x2x1x4 - x1x4^3x2x4x1 - x4x1x4^2x2x1x4 + x4x1x4^2x2x4x1</polynomial>
    <polynomial>x1x4^3x2x1x3 - x1x4^3x2x3x1 - x4x1x4^2x2x1x3 + x4x1x4^2x2x3x1</polynomial>
    <polynomial>x1x4^3x2x1x2 - x1x4^3x2^2x1 - x4x1x4^2x2x1x2 + x4x1x4^2x2^2x1</polynomial>
    <polynomial>x1x4^3x1^2x4 - x1x4^3x1x4x1 - x4x1x4^2x1^2x4 + x4x1x4^2x1x4x1</polynomial>
    <polynomial>x1x4^3x1^2x3 - x1x4^3x1x3x1 - x4x1x4^2x1^2x3 + x4x1x4^2x1x3x1</polynomial>
    <polynomial>x1x4^3x1^2x2 - x1x4^3x1x2x1 - x4x1x4^2x1^2x2 + x4x1x4^2x1x2x1</polynomial>
    <polynomial>x1x4^2x3^3x4 - x1x4^2x3^2x4x3 - x4x1x4x3^3x4 + x4x1x4x3^2x4x3</polynomial>
    <polynomial>x1x4^2x3^2x2x4 - x1x4^2x3^2x4x2 - x4x1x4x3^2x2x4 + x4x1x4x3^2x4x2</polynomial>
    <polynomial>x1x4^2x3^2x2x3 - x1x4^2x3^3x2 - x4x1x4x3^2x2x3 + x4x1x4x3^3x2</polynomial>
    <polynomial>x1x4^2x3^2x1x4 - x1x4^2x3^2x4x1 - x4x1x4x3^2x1x4 + x4x1x4x3^2x4x1</polynomial>
    <polynomial>x1x4^2x3^2x1x3 - x1x4^2x3^3x1 - x4x1x4x3^2x1x3 + x4x1x4x3^3x1</polynomial>
    <polynomial>x1x4^2x3^2x1x2 - x1x4^2x3^2x2x1 - x4x1x4x3^2x1x2 + x4x1x4x3^2x2x1</polynomial>
    <polynomial>x1x4^2x3x2^2x4 - x1x4^2x3x2x4x2 - x4x1x4x3x2^2x4 + x4x1x4x3x2x4x2</polynomial>
    <polynomial>x1x4^2x3x2^2x3 - x1x4^2x3x2x3x2 - x4x1x4x3x2^2x3 + x4x1x4x3x2x3x2</polynomial>
    <polynomial>x1x4^2x3x2x1x4 - x1x4^2x3x2x4x1 - x4x1x4x3x2x1x4 + x4x1x4x3x2x4x1</polynomial>
    <polynomial>x1x4^2x3x2x1x3 - x1x4^2x3x2x3x1 - x4x1x4x3x2x1x3 + x4x1x4x3x2x3x1</polynomial>
    <polynomial>x1x4^2x3x2x1x2 - x1x4^2x3x2^2x1 - x4x1x4x3x2x1x2 + x4x1x4x3x2^2x1</polynomial>
    <polynomial>x1x4^2x3x1^2x4 - x1x4^2x3x1x4x1 - x4x1x4x3x1^2x4 + x4x1x4x3x1x4x1</polynomial>
    <polynomial>x1x4^2x3x1^2x3 - x1x4^2x3x1x3x1 - x4x1x4x3x1^2x3 + x4x1x4x3x1x3x1</polynomial>
    <polynomial>x1x4^2x3x1^2x2 - x1x4^2x3x1x2x1 - x4x1x4x3x1^2x2 + x4x1x4x3x1x2x1</polynomial>
    <polynomial>x1x4^2x2^3x4 - x1x4^2x2^2x4x2 - x4x1x4x2^3x4 + x4x1x4x2^2x4x2</polynomial>
    <polynomial>x1x4^2x2^3x3 - x1x4^2x2^2x3x2 - x4x1x4x2^3x3 + x4x1x4x2^2x3x2</polynomial>
    <polynomial>x1x4^2x2^2x1x4 - x1x4^2x2^2x4x1 - x4x1x4x2^2x1x4 + x4x1x4x2^2x4x1</polynomial>
    <polynomial>x1x4^2x2^2x1x3 - x1x4^2x2^2x3x1 - x4x1x4x2^2x1x3 + x4x1x4x2^2x3x1</polynomial>
    <polynomial>x1x4^2x2^2x1x2 - x1x4^2x2^3x1 - x4x1x4x2^2x1x2 + x4x1x4x2^3x1</polynomial>
    <polynomial>x1x4^2x2x1^2x4 - x1x4^2x2x1x4x1 - x4x1x4x2x1^2x4 + x4x1x4x2x1x4x1</polynomial>
    <polynomial>x1x4^2x2x1^2x3 - x1x4^2x2x1x3x1 - x4x1x4x2x1^2x3 + x4x1x4x2x1x3x1</polynomial>
    <polynomial>x1x4^2x2x1^2x2 - x1x4^2x2x1x2x1 - x4x1x4x2x1^2x2 + x4x1x4x2x1x2x1</polynomial>
    <polynomial>x1x4^2x1^3x4 - x1x4^2x1^2x4x1 - x4x1x4x1^3x4 + x4x1x4x1^2x4x1</polynomial>
    <polynomial>x1x4^2x1^3x3 - x1x4^2x1^2x3x1 - x4x1x4x1^3x3 + x4x1x4x1^2x3x1</polynomial>
    <polynomial>x1x4^2x1^3x2 - x1x4^2x1^2x2x1 - x4x1x4x1^3x2 + x4x1x4x1^2x2x1</polynomial>
    <polynomial>x1x4x3^4x4 - x1x4x3^3x4x3 - x4x1x3^4x4 + x4x1x3^3x4x3</polynomial>
    <polynomial>x1x4x3^3x2x4 - x1x4x3^3x4x2 - x4x1x3^3x2x4 + x4x1x3^3x4x2</polynomial>
    <polynomial>x1x4x3^3x2x3 - x1x4x3^4x2 - x4x1x3^3x2x3 + x4x1x3^4x2</polynomial>
    <polynomial>x1x4x3^3x1x4 - x1x4x3^3x4x1 - x4x1x3^3x1x4 + x4x1x3^3x4x1</polynomial>
    <polynomial>x1x4x3^3x1x3 - x1x4x3^4x1 - x4x1x3^3x1x3 + x4x1x3^4x1</polynomial>
    <polynomial>x1x4x3^3x1x2 - x1x4x3^3x2x1 - x4x1x3^3x1x2 + x4x1x3^3x2x1</polynomial>
    <polynomial>x1x4x3^2x2^2x4 - x1x4x3^2x2x4x2 - x4x1x3^2x2^2x4 + x4x1x3^2x2x4x2</polynomial>
    <polynomial>x1x4x3^2x2^2x3 - x1x4x3^2x2x3x2 - x4x1x3^2x2^2x3 + x4x1x3^2x2x3x2</polynomial>
    <polynomial>x1x4x3^2x2x1x4 - x1x4x3^2x2x4x1 - x4x1x3^2x2x1x4 + x4x1x3^2x2x4x1</polynomial>
    <polynomial>x1x4x3^2x2x1x3 - x1x4x3^2x2x3x1 - x4x1x3^2x2x1x3 + x4x1x3^2x2x3x1</polynomial>
    <polynomial>x1x4x3^2x2x1x2 - x1x4x3^2x2^2x1 - x4x1x3^2x2x1x2 + x4x1x3^2x2^2x1</polynomial>
    <polynomial>x1x4x3^2x1^2x4 - x1x4x3^2x1x4x1 - x4x1x3^2x1^2x4 + x4x1x3^2x1x4x1</polynomial>
    <polynomial>x1x4x3^2x1^2x3 - x1x4x3^2x1x3x1 - x4x1x3^2x1^2x3 + x4x1x3^2x1x3x1</polynomial>
    <polynomial>x1x4x3^2x1^2x2 - x1x4x3^2x1x2x1 - x4x1x3^2x1^2x2 + x4x1x3^2x1x2x1</polynomial>
    <polynomial>x1x4x3x2^3x4 - x1x4x3x2^2x4x2 - x4x1x3x2^3x4 + x4x1x3x2^2x4x2</polynomial>
    <polynomial>x1x4x3x2^3x3 - x1x4x3x2^2x3x2 - x4x1x3x2^3x3 + x4x1x3x2^2x3x2</polynomial>
    <polynomial>x1x4x3x2^2x1x4 - x1x4x3x2^2x4x1 - x4x1x3x2^2x1x4 + x4x1x3x2^2x4x1</polynomial>
    <polynomial>x1x4x3x2^2x1x3 - x1x4x3x2^2x3x1 - x4x1x3x2^2x1x3 + x4x1x3x2^2x3x1</polynomial>
    <polynomial>x1x4x3x2^2x1x2 - x1x4x3x2^3x1 - x4x1x3x2^2x1x2 + x4x1x3x2^3x1</polynomial>
    <polynomial>x1x4x3x2x1^2x4 - x1x4x3x2x1x4x1 - x4x1x3x2x1^2x4 + x4x1x3x2x1x4x1</polynomial>
    <polynomial>x1x4x3x2x1^2x3 - x1x4x3x2x1x3x1 - x4x1x3x2x1^2x3 + x4x1x3x2x1x3x1</polynomial>
    <polynomial>x1x4x3x2x1^2x2 - x1x4x3x2x1x2x1 - x4x1x3x2x1^2x2 + x4x1x3x2x1x2x1</polynomial>
    <polynomial>x1x4x3x1^3x4 - x1x4x3x1^2x4x1 - x4x1x3x1^3x4 + x4x1x3x1^2x4x1</polynomial>
    <polynomial>x1x4x3x1^3x3 - x1x4x3x1^2x3x1 - x4x1x3x1^3x3 + x4x1x3x1^2x3x1</polynomial>
    <polynomial>x1x4x3x1^3x2 - x1x4x3x1^2x2x1 - x4x1x3x1^3x2 + x4x1x3x1^2x2x1</polynomial>
    <polynomial>x1x4x2^4x4 - x1x4x2^3x4x2 - x4x1x2^4x4 + x4x1x2^3x4x2</polynomial>
    <polynomial>x1x4x2^4x3 - x1x4x2^3x3x2 - x4x1x2^4x3 + x4x1x2^3x3x2</polynomial>
    <polynomial>x1x4x2^3x1x4 - x1x4x2^3x4x1 - x4x1x2^3x1x4 + x4x1x2^3x4x1</polynomial>
    <polynomial>x1x4x2^3x1x3 - x1x4x2^3x3x1 - x4x1x2^3x1x3 + x4x1x2^3x3x1</polynomial>
    <polynomial>x1x4x2^3x1x2 - x1x4x2^4x1 - x4x1x2^3x1x2 + x4x1x2^4x1</polynomial>
    <polynomial>x1x4x2^2x1^2x4 - x1x4x2^2x1x4x1 - x4x1x2^2x1^2x4 + x4x1x2^2x1x4x1</polynomial>
    <polynomial>x1x4x2^2x1^2x3 - x1x4x2^2x1x3x1 - x4x1x2^2x1^2x3 + x4x1x2^2x1x3x1</polynomial>
    <polynomial>x1x4x2^2x1^2x2 - x1x4x2^2x1x2x1 - x4x1x2^2x1^2x2 + x4x1x2^2x1x2x1</polynomial>
    <polynomial>x1x4x2x1^3x4 - x1x4x2x1^2x4x1 - x4x1x2x1^3x4 + x4x1x2x1^2x4x1</polynomial>
    <polynomial>x1x4x2x1^3x3 - x1x4x2x1^2x3x1 - x4x1x2x1^3x3 + x4x1x2x1^2x3x1</polynomial>
    <polynomial>x1x4x2x1^3x2 - x1x4x2x1^2x2x1 - x4x1x2x1^3x2 + x4x1x2x1^2x2x1</polynomial>
    <polynomial>x1x4x1^4x4 - x1x4x1^3x4x1 - x4x1^5x4 + x4x1^4x4x1</polynomial>
    <polynomial>x1x4x1^4x3 - x1x4x1^3x3x1 - x4x1^5x3 + x4x1^4x3x1</polynomial>
    <polynomial>x1x4x1^4x2 - x1x4x1^3x2x1 - x4x1^5x2 + x4x1^4x2x1</polynomial>
    <polynomial>x1x3^5x4 - x1x3^4x4x3 - x3x1x3^4x4 + x3x1x3^3x4x3</polynomial>
    <polynomial>x1x3^4x2x4 - x1x3^4x4x2 - x3x1x3^3x2x4 + x3x1x3^3x4x2</polynomial>
    <polynomial>x1x3^4x2x3 - x1x3^5x2 - x3x1x3^3x2x3 + x3x1x3^4x2</polynomial>
    <polynomial>x1x3^4x1x4 - x1x3^4x4x1 - x3x1x3^3x1x4 + x3x1x3^3x4x1</polynomial>
    <polynomial>x1x3^4x1x3 - x1x3^5x1 - x3x1x3^3x1x3 + x3x1x3^4x1</polynomial>
    <polynomial>x1x3^4x1x2 - x1x3^4x2x1 - x3x1x3^3x1x2 + x3x1x3^3x2x1</polynomial>
    <polynomial>x1x3^3x2^2x4 - x1x3^3x2x4x2 - x3x1x3^2x2^2x4 + x3x1x3^2x2x4x2</polynomial>
    <polynomial>x1x3^3x2^2x3 - x1x3^3x2x3x2 - x3x1x3^2x2^2x3 + x3x1x3^2x2x3x2</polynomial>
    <polynomial>x1x3^3x2x1x4 - x1x3^3x2x4x1 - x3x1x3^2x2x1x4 + x3x1x3^2x2x4x1</polynomial>
    <polynomial>x1x3^3x2x1x3 - x1x3^3x2x3x1 - x3x1x3^2x2x1x3 + x3x1x3^2x2x3x1</polynomial>
    <polynomial>x1x3^3x2x1x2 - x1x3^3x2^2x1 - x3x1x3^2x2x1x2 + x3x1x3^2x2^2x1</polynomial>
    <polynomial>x1x3^3x1^2x4 - x1x3^3x1x4x1 - x3x1x3^2x1^2x4 + x3x1x3^2x1x4x1</polynomial>
    <polynomial>x1x3^3x1^2x3 - x1x3^3x1x3x1 - x3x1x3^2x1^2x3 + x3x1x3^2x1x3x1</polynomial>
    <polynomial>x1x3^3x1^2x2 - x1x3^3x1x2x1 - x3x1x3^2x1^2x2 + x3x1x3^2x1x2x1</polynomial>
    <polynomial>x1x3^2x2^3x4 - x1x3^2x2^2x4x2 - x3x1x3x2^3x4 + x3x1x3x2^2x4x2</polynomial>
    <polynomial>x1x3^2x2^3x3 - x1x3^2x2^2x3x2 - x3x1x3x2^3x3 + x3x1x3x2^2x3x2</polynomial>
    <polynomial>x1x3^2x2^2x1x4 - x1x3^2x2^2x4x1 - x3x1x3x2^2x1x4 + x3x1x3x2^2x4x1</polynomial>
    <polynomial>x1x3^2x2^2x1x3 - x1x3^2x2^2x3x1 - x3x1x3x2^2x1x3 + x3x1x3x2^2x3x1</polynomial>
    <polynomial>x1x3^2x2^2x1x2 - x1x3^2x2^3x1 - x3x1x3x2^2x1x2 + x3x1x3x2^3x1</polynomial>
    <polynomial>x1x3^2x2x1^2x4 - x1x3^2x2x1x4x1 - x3x1x3x2x1^2x4 + x3x1x3x2x1x4x1</polynomial>
    <polynomial>x1x3^2x2x1^2x3 - x1x3^2x2x1x3x1 - x3x1x3x2x1^2x3 + x3x1x3x2x1x3x1</polynomial>
    <polynomial>x1x3^2x2x1^2x2 - x1x3^2x2x1x2x1 - x3x1x3x2x1^2x2 + x3x1x3x2x1x2x1</polynomial>
    <polynomial>x1x3^2x1^3x4 - x1x3^2x1^2x4x1 - x3x1x3x1^3x4 + x3x1x3x1^2x4x1</polynomial>
    <polynomial>x1x3^2x1^3x3 - x1x3^2x1^2x3x1 - x3x1x3x1^3x3 + x3x1x3x1^2x3x1</polynomial>
    <polynomial>x1x3^2x1^3x2 - x1x3^2x1^2x2x1 - x3x1x3x1^3x2 + x3x1x3x1^2x2x1</polynomial>
    <polynomial>x1x3x2^4x4 - x1x3x2^3x4x2 - x3x1x2^4x4 + x3x1x2^3x4x2</polynomial>
    <polynomial>x1x3x2^4x3 - x1x3x2^3x3x2 - x3x1x2^4x3 + x3x1x2^3x3x2</polynomial>
    <polynomial>x1x3x2^3x1x4 - x1x3x2^3x4x1 - x3x1x2^3x1x4 + x3x1x2^3x4x1</polynomial>
    <polynomial>x1x3x2^3x1x3 - x1x3x2^3x3x1 - x3x1x2^3x1x3 + x3x1x2^3x3x1</polynomial>
    <polynomial>x1x3x2^3x1x2 - x1x3x2^4x1 - x3x1x2^3x1x2 + x3x1x2^4x1</polynomial>
    <polynomial>x1x3x2^2x1^2x4 - x1x3x2^2x1x4x1 - x3x1x2^2x1^2x4 + x3x1x2^2x1x4x1</polynomial>
    <polynomial>x1x3x2^2x1^2x3 - x1x3x2^2x1x3x1 - x3x1x2^2x1^2x3 + x3x1x2^2x1x3x1</polynomial>
    <polynomial>x1x3x2^2x1^2x2 - x1x3x2^2x1x2x1 - x3x1x2^2x1^2x2 + x3x1x2^2x1x2x1</polynomial>
    <polynomial>x1x3x2x1^3x4 - x1x3x2x1^2x4x1 - x3x1x2x1^3x4 + x3x1x2x1^2x4x1</polynomial>
    <polynomial>x1x3x2x1^3x3 - x1x3x2x1^2x3x1 - x3x1x2x1^3x3 + x3x1x2x1^2x3x1</polynomial>
    <polynomial>x1x3x2x1^3x2 - x1x3x2x1^2x2x1 - x3x1x2x1^3x2 + x3x1x2x1^2x2x1</polynomial>
    <polynomial>x1x3x1^4x4 - x1x3x1^3x4x1 - x3x1^5x4 + x3x1^4x4x1</polynomial>
    <polynomial>x1x3x1^4x3 - x1x3x1^3x3x1 - x3x1^5x3 + x3x1^4x3x1</polynomial>
    <polynomial>x1x3x1^4x2 - x1x3x1^3x2x1 - x3x1^5x2 + x3x1^4x2x1</polynomial>
    <polynomial>x1x2^5x4 - x1x2^4x4x2 - x2x1x2^4x4 + x2x1x2^3x4x2</polynomial>
    <polynomial>x1x2^5x3 - x1x2^4x3x2 - x2x1x2^4x3 + x2x1x2^3x3x2</polynomial>
    <polynomial>x1x2^4x1x4 - x1x2^4x4x1 - x2x1x2^3x1x4 + x2x1x2^3x4x1</polynomial>
    <polynomial>x1x2^4x1x3 - x1x2^4x3x1 - x2x1x2^3x1x3 + x2x1x2^3x3x1</polynomial>
    <polynomial>x1x2^4x1x2 - x1x2^5x1 - x2x1x2^3x1x2 + x2x1x2^4x1</polynomial>
    <polynomial>x1x2^3x1^2x4 - x1x2^3x1x4x1 - x2x1x2^2x1^2x4 + x2x1x2^2x1x4x1</polynomial>
    <polynomial>x1x2^3x1^2x3 - x1x2^3x1x3x1 - x2x1x2^2x1^2x3 + x2x1x2^2x1x3x1</polynomial>
    <polynomial>x1x2^3x1^2x2 - x1x2^3x1x2x1 - x2x1x2^2x1^2x2 + x2x1x2^2x1x2x1</polynomial>
    <polynomial>x1x2^2x1^3x4 - x1x2^2x1^2x4x1 - x2x1x2x1^3x4 + x2x1x2x1^2x4x1</polynomial>
    <polynomial>x1x2^2x1^3x3 - x1x2^2x1^2x3x1 - x2x1x2x1^3x3 + x2x1x2x1^2x3x1</polynomial>
    <polynomial>x1x2^2x1^3x2 - x1x2^2x1^2x2x1 - x2x1x2x1^3x2 + x2x1x2x1^2x2x1</polynomial>
    <polynomial>x1x2x1^4x4 - x1x2x1^3x4x1 - x2x1^5x4 + x2x1^4x4x1</polynomial>
    <polynomial>x1x2x1^4x3 - x1x2x1^3x3x1 - x2x1^5x3 + x2x1^4x3x1</polynomial>
    <polynomial>x1x2x1^4x2 - x1x2x1^3x2x1 - x2x1^5x2 + x2x1^4x2x1</polynomial>
  </basis>
</FA_Q_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for GAP output parse.")

    def test_GB_Z_lp_Singular_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Singular output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by Singular.
        """
        from comp.GB_Z_lp.Singular.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "x" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        singularOutput = """                     SINGULAR                                 /
 A Computer Algebra System for Polynomial Computations       /   version 3-1-7
                                                           0<
 by: W. Decker, G.-M. Greuel, G. Pfister, H. Schoenemann     \   Aug 2013
FB Mathematik der Universitaet, D-67653 Kaiserslautern        \
=====Solution Begin=====
58773123072f19-47869056f13-45657f7+f,
80621568ef13+44928ef7-ef,
4245696e2f7-91e2f+8707129344f17-12130560f11+256f5,
7e4f-15489792e2f11+836e2f5+20155392f15-27648f9,
2916e7+2414448e5f4+3159e3f2+2916ef6-4e,
162362880df7-3480df-1143072e8-262763676e6f4-23078868624e4f8-1139670e4f2-162596889e2f6+1568e2+641079684f10+107184f4,
374647680def6-8030de+1512742068e7f3+3183187248e5f7+567486e5f-248372973e3f5+1267588116ef9+114395ef3,
1134de2+10077696df10-41040df4-312012e6f+12072240e4f5+38475e2f3-102060f7-28f,
36d2f+7776de4f2+279936de2f6+24de2-279936e4f5-1080e2f3-f,
261d2e-3779136de5f+74218032de3f5-2671849152def9+114372def3-20412e7+2671849152e3f8-320517e3f2+7514532ef6+28e,
20d3+15552d2e4f+4752de2f2-5d+1728e4f-15552e2f5-20f3,
4c-3240d2ef2-3240de3f-324e5+45ef2,
b+432c3de-648c2d3-36c2d+648d3f2-1296d2e2f-432de4+36e2f,
2af+2be+2cd+f,
2ae+2bd+c2+e+f2,
2ad+2bc+d+2ef,
a2+a+2bf+2ce+d2
=====Solution End=====

$Bye.
real 0.00
user 0.00
sys 0.00"""
        try:
            tempRes = extractSolution(singularOutput)
        except:
            self.fail("Could not parse valid Singular output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>58773123072f19-47869056f13-45657f7+f</polynomial>
    <polynomial>80621568ef13+44928ef7-ef</polynomial>
    <polynomial>4245696e2f7-91e2f+8707129344f17-12130560f11+256f5</polynomial>
    <polynomial>7e4f-15489792e2f11+836e2f5+20155392f15-27648f9</polynomial>
    <polynomial>2916e7+2414448e5f4+3159e3f2+2916ef6-4e</polynomial>
    <polynomial>162362880df7-3480df-1143072e8-262763676e6f4-23078868624e4f8-1139670e4f2-162596889e2f6+1568e2+641079684f10+107184f4</polynomial>
    <polynomial>374647680def6-8030de+1512742068e7f3+3183187248e5f7+567486e5f-248372973e3f5+1267588116ef9+114395ef3</polynomial>
    <polynomial>1134de2+10077696df10-41040df4-312012e6f+12072240e4f5+38475e2f3-102060f7-28f</polynomial>
    <polynomial>36d2f+7776de4f2+279936de2f6+24de2-279936e4f5-1080e2f3-f</polynomial>
    <polynomial>261d2e-3779136de5f+74218032de3f5-2671849152def9+114372def3-20412e7+2671849152e3f8-320517e3f2+7514532ef6+28e</polynomial>
    <polynomial>20d3+15552d2e4f+4752de2f2-5d+1728e4f-15552e2f5-20f3</polynomial>
    <polynomial>4c-3240d2ef2-3240de3f-324e5+45ef2</polynomial>
    <polynomial>b+432c3de-648c2d3-36c2d+648d3f2-1296d2e2f-432de4+36e2f</polynomial>
    <polynomial>2af+2be+2cd+f</polynomial>
    <polynomial>2ae+2bd+c2+e+f2</polynomial>
    <polynomial>2ad+2bc+d+2ef</polynomial>
    <polynomial>a2+a+2bf+2ce+d2</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for Singular output parse.")


    def test_GB_Z_lp_Risa_Asir_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Risa/Asir output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by Risa/Asir.
        """
        from comp.GB_Z_lp.Risa_Asir.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "[x]" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        risaasirOutput = """=====Solution Begin=====
[z^5-t^4,t^3*y^2+2*t^2*z^2*y+(-t^6+2*t^3+t-1)*z^4,-t*z*y^2-2*z^3*y+t^8-2*t^5-t^3+t^2,-z^3*y^2-2*t^3*y+(t^7-2*t^4-t^2+t)*z^2,-2*t^2*y^3-z^2*y^2+(2*t^5-4*t^2+6)*z^4*y+(-4*t^8+t^7+8*t^5-2*t^4+4*t^3-5*t^2+t)*z,-z*y^3+(t^7-2*t^4+3*t^2+t)*y+(-2*t^6+4*t^3+2*t-2)*z^2,-2*t*y^5-z*y^2+(2*t^11-8*t^8+20*t^6+12*t^5-40*t^3-8*t^2+10*t+20)*z^3*y-8*t^14+32*t^11-48*t^8+t^7+32*t^5+6*t^4-9*t^2+t,y^8+8*t*y^3-16*z^2*y^2+(8*t^16-48*t^13+56*t^11+120*t^10-224*t^8-160*t^7+56*t^6+336*t^5+112*t^4-112*t^3-224*t^2-24*t+56)*z^4*y+(-t^24+8*t^21-20*t^19-28*t^18+120*t^16+56*t^15-14*t^14-300*t^13-70*t^12+56*t^11+400*t^10+84*t^9-84*t^8-268*t^7-84*t^6+56*t^5+63*t^4+36*t^3-46*t^2+12*t-1)*z,(-t^3+1)*x+y^6+(6*t^13-24*t^10+20*t^8+36*t^7-40*t^5-24*t^4+6*t^3+20*t^2+6*t+1)*y+(-t^17+6*t^14-9*t^12-15*t^11+36*t^9+20*t^8+5*t^7-54*t^6-15*t^5-10*t^4+36*t^3+11*t^2+5*t-9)*z^2,(y+t^2*z^2)*x+y^7+(20*t^2+6*t+1)*y^2+(-t^17+6*t^14-21*t^12-15*t^11+84*t^9+20*t^8-35*t^7-126*t^6-15*t^5+70*t^4+84*t^3-t^2+5*t-9)*z^2*y+(6*t^16-36*t^13+14*t^11+90*t^10-56*t^8-120*t^7-14*t^6+64*t^5+84*t^4+27*t^3-16*t^2-30*t+7)*z^4,-x^2+2*y^7+(41*t^2+13*t+1)*y^2+(-2*t^17+12*t^14-42*t^12-30*t^11+168*t^9+40*t^8-70*t^7-252*t^6-30*t^5+140*t^4+168*t^3-2*t^2+12*t-16)*z^2*y+(12*t^16-72*t^13+28*t^11+180*t^10-112*t^8-240*t^7-28*t^6+127*t^5+167*t^4+55*t^3-30*t^2-58*t+15)*z^4]
=====Solution End=====
0
"""
        try:
            tempRes = extractSolution(risaasirOutput)
        except:
            self.fail("Could not parse valid Risa/Asir output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>z^5-t^4</polynomial>
    <polynomial>t^3*y^2+2*t^2*z^2*y+(-t^6+2*t^3+t-1)*z^4</polynomial>
    <polynomial>-t*z*y^2-2*z^3*y+t^8-2*t^5-t^3+t^2</polynomial>
    <polynomial>-z^3*y^2-2*t^3*y+(t^7-2*t^4-t^2+t)*z^2</polynomial>
    <polynomial>-2*t^2*y^3-z^2*y^2+(2*t^5-4*t^2+6)*z^4*y+(-4*t^8+t^7+8*t^5-2*t^4+4*t^3-5*t^2+t)*z</polynomial>
    <polynomial>-z*y^3+(t^7-2*t^4+3*t^2+t)*y+(-2*t^6+4*t^3+2*t-2)*z^2</polynomial>
    <polynomial>-2*t*y^5-z*y^2+(2*t^11-8*t^8+20*t^6+12*t^5-40*t^3-8*t^2+10*t+20)*z^3*y-8*t^14+32*t^11-48*t^8+t^7+32*t^5+6*t^4-9*t^2+t</polynomial>
    <polynomial>y^8+8*t*y^3-16*z^2*y^2+(8*t^16-48*t^13+56*t^11+120*t^10-224*t^8-160*t^7+56*t^6+336*t^5+112*t^4-112*t^3-224*t^2-24*t+56)*z^4*y+(-t^24+8*t^21-20*t^19-28*t^18+120*t^16+56*t^15-14*t^14-300*t^13-70*t^12+56*t^11+400*t^10+84*t^9-84*t^8-268*t^7-84*t^6+56*t^5+63*t^4+36*t^3-46*t^2+12*t-1)*z</polynomial>
    <polynomial>(-t^3+1)*x+y^6+(6*t^13-24*t^10+20*t^8+36*t^7-40*t^5-24*t^4+6*t^3+20*t^2+6*t+1)*y+(-t^17+6*t^14-9*t^12-15*t^11+36*t^9+20*t^8+5*t^7-54*t^6-15*t^5-10*t^4+36*t^3+11*t^2+5*t-9)*z^2</polynomial>
    <polynomial>(y+t^2*z^2)*x+y^7+(20*t^2+6*t+1)*y^2+(-t^17+6*t^14-21*t^12-15*t^11+84*t^9+20*t^8-35*t^7-126*t^6-15*t^5+70*t^4+84*t^3-t^2+5*t-9)*z^2*y+(6*t^16-36*t^13+14*t^11+90*t^10-56*t^8-120*t^7-14*t^6+64*t^5+84*t^4+27*t^3-16*t^2-30*t+7)*z^4</polynomial>
    <polynomial>-x^2+2*y^7+(41*t^2+13*t+1)*y^2+(-2*t^17+12*t^14-42*t^12-30*t^11+168*t^9+40*t^8-70*t^7-252*t^6-30*t^5+140*t^4+168*t^3-2*t^2+12*t-16)*z^2*y+(12*t^16-72*t^13+28*t^11+180*t^10-112*t^8-240*t^7-28*t^6+127*t^5+167*t^4+55*t^3-30*t^2-58*t+15)*z^4</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        print expectedOutp
        print tempRes
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for Risa/Asir output parse.")

    def test_GB_Z_lp_REDUCE_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the REDUCE output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by REDUCE.
        """
        from comp.GB_Z_lp.REDUCE.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "5: {x}" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        reduceOutput = """Reduce (Free CSL version), 27-Apr-10 ...

1: 
2: 
3: 
4: 
=====Solution Begin=====$

5: 
{x1 + x2,x2**2 + x3*x4,x3**2*x4**2}$

6: 
=====Solution End=====$

7: """
        try:
            tempRes = extractSolution(reduceOutput)
        except:
            self.fail("Could not parse valid REDUCE output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>x1 + x2</polynomial>
    <polynomial>x2^2 + x3*x4</polynomial>
    <polynomial>x3^2*x4^2</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        print expectedOutp
        print tempRes
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for REDUCE output parse.")

    def test_GB_Z_lp_Maple_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Maple output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by Maple.
        """
        from comp.GB_Z_lp.Maple.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "printxyz() [x]" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        mapleOutput = """    |\^/|     Maple 17 (X86 64 LINUX)
._|\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple Inc. 2013
 \  MAPLE  /  All rights reserved. Maple is a trademark of
 <____ ____>  Waterloo Maple Inc.
      |       Type ? for help.
> with(Groebner):
> Ideal := {x1+x2,x3*x4-x2*x1,x1*x2*x3*x4}:
> ordering := plex(x1,x2,x3,x4):
> B := Basis(Ideal, ordering):
memory used=2.6MB, alloc=32.3MB, time=0.33
> printf("=====Solution Begin=====");
=====Solution Begin=====> printf("%a\n",B);
[x3^2*x4^2, x2^2+x3*x4, x1+x2]
> printf("=====Solution End=====");
=====Solution End=====> quit;"""
        try:
            tempRes = extractSolution(mapleOutput)
        except:
            self.fail("Could not parse valid Maple output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>x3^2*x4^2</polynomial>
    <polynomial>x2^2+x3*x4</polynomial>
    <polynomial>x1+x2</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        print expectedOutp
        print tempRes
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for Maple output parse.")

    def test_GB_Z_lp_Magma_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Magma output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by Magma.
        """
        from comp.GB_Z_lp.Magma.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "[x]" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        magmaOutput = """Magma V2.19-2     Tue Aug 19 2014 15:18:53 on emmy     [Seed = 2419100951]
Type ? for help.  Type <Ctrl>-D to quit.
=====Solution Begin=====
[
    x1 + x2,
    x2^2 + x3*x4,
    x3^2*x4^2
]
=====Solution End=====
"""
        try:
            tempRes = extractSolution(magmaOutput)
        except:
            self.fail("Could not parse valid Magma output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>x1 + x2</polynomial>
    <polynomial>x2^2 + x3*x4</polynomial>
    <polynomial>x3^2*x4^2</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        print expectedOutp
        print tempRes
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for Magma output parse.")

    def test_GB_Z_lp_GAP_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the GAP output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by GAP.
        """
        from comp.GB_Z_lp.GAP.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "gap> [x]" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        gapOutput = """ Libs used:  gmp, readline
 Loading the library and packages ...
 Components: trans 1.0, prim 2.1, small* 1.0, id* 1.0
 Packages:   AClib 1.2, Alnuth 3.0.0, AtlasRep 1.5.0, AutPGrp 1.5, 
             CRISP 1.3.7, Cryst 4.1.12, CrystCat 1.1.6, CTblLib 1.2.2, 
             FactInt 1.5.3, FGA 1.2.0, GAPDoc 1.5.1, IO 4.2, IRREDSOL 1.2.3, 
             LAGUNA 3.6.4, Polenta 1.3.1, Polycyclic 2.11, RadiRoot 2.6, 
             ResClasses 3.3.2, Sophus 1.23, SpinSym 1.5, TomLib 1.2.4
 Try '?help' for help. See also  '?copyright' and  '?authors'
gap> Rationals
gap> Rationals[x1,x2,x3,x4]
gap> x1
gap> x2
gap> x3
gap> x4
gap> <two-sided ideal in Rationals[x1,x2,x3,x4], (3 generators)>
gap> MonomialLexOrdering()
gap> [ x3^2*x4^2, x2^2+x3*x4, x1+x2 ]
gap> =====Solution Begin=====
gap> [ x3^2*x4^2, x2^2+x3*x4, x1+x2 ]
gap> =====Solution End=====
"""
        try:
            tempRes = extractSolution(gapOutput)
        except:
            self.fail("Could not parse valid GAP output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Z_lp_SOL>
  <basis>
    <polynomial>x3^2*x4^2</polynomial>
    <polynomial>x2^2+x3*x4</polynomial>
    <polynomial>x1+x2</polynomial>
  </basis>
</GB_Z_lp_SOL>
"""
        print expectedOutp
        print tempRes
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for GAP output parse.")

    def test_GB_Fp_dp_GAP_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the GAP output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by GAP.
        """
        from comp.GB_Fp_dp.GAP.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "gap> [x]" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        gapOutput = """Libs used:  gmp, readline
 Loading the library and packages ...
 Components: trans 1.0, prim 2.1, small* 1.0, id* 1.0
 Packages:   AClib 1.2, Alnuth 3.0.0, AtlasRep 1.5.0, AutPGrp 1.5, 
             CRISP 1.3.7, Cryst 4.1.12, CrystCat 1.1.6, CTblLib 1.2.2, 
             FactInt 1.5.3, FGA 1.2.0, GAPDoc 1.5.1, IO 4.2, IRREDSOL 1.2.3, 
             LAGUNA 3.6.4, Polenta 1.3.1, Polycyclic 2.11, RadiRoot 2.6, 
             ResClasses 3.3.2, Sophus 1.23, SpinSym 1.5, TomLib 1.2.4
 Try '?help' for help. See also  '?copyright' and  '?authors'
gap> GF(5)
gap> GF(5)[x1,x2,x3,x4]
gap> x1
gap> x2
gap> x3
gap> x4
gap> <two-sided ideal in GF(5)[x1,x2,x3,x4], (3 generators)>
gap> MonomialGrlexOrdering()
gap> [ x1+x2, x2^2+x3*x4, x3^2*x4^2 ]
gap> =====Solution Begin=====
gap> [ x1+x2, x2^2+x3*x4, x3^2*x4^2 ]
gap> =====Solution End=====
"""
        try:
            tempRes = extractSolution(gapOutput)
        except:
            self.fail("Could not parse valid GAP output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>x1+x2</polynomial>
    <polynomial>x2^2+x3*x4</polynomial>
    <polynomial>x3^2*x4^2</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for GAP output parse.")

    def test_GB_Fp_dp_Magma_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Magma output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by Magma.
        """
        from comp.GB_Fp_dp.Magma.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "[x]" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        magmaOutput = """Magma V2.19-2     Tue Aug 19 2014 16:43:06 on emmy     [Seed = 3429694951]
Type ? for help.  Type <Ctrl>-D to quit.
=====Solution Begin=====
[
    x1 + x2,
    x2^2 + x3*x4,
    x3^2*x4^2
]
=====Solution End=====
"""
        try:
            tempRes = extractSolution(magmaOutput)
        except:
            self.fail("Could not parse valid Magma output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>x1 + x2</polynomial>
    <polynomial>x2^2 + x3*x4</polynomial>
    <polynomial>x3^2*x4^2</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for Magma output parse.")

    def test_GB_Fp_dp_Maple_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Maple output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by Maple.
        """
        from comp.GB_Fp_dp.Maple.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "print fask;d [x]" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        mapleOutput = """    |\^/|     Maple 17 (X86 64 LINUX)
._|\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple Inc. 2013
 \  MAPLE  /  All rights reserved. Maple is a trademark of
 <____ ____>  Waterloo Maple Inc.
      |       Type ? for help.
> with(Groebner):
> Ideal := {x1+x2,x3*x4-x2*x1,x1*x2*x3*x4} mod 5:
> ordering := grlex(x1,x2,x3,x4):
> B := Basis(Ideal, ordering):
> printf("=====Solution Begin=====");
=====Solution Begin=====> printf("%a\n",B);
[x1+x2, 4*x2^2-x3*x4, x3^2*x4^2]
> printf("=====Solution End=====");
=====Solution End=====> quit;
memory used=2.0MB, alloc=8.3MB, time=0.23
"""
        try:
            tempRes = extractSolution(mapleOutput)
        except:
            self.fail("Could not parse valid Maple output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>x1+x2</polynomial>
    <polynomial>4*x2^2-x3*x4</polynomial>
    <polynomial>x3^2*x4^2</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for Maple output parse.")

    def test_GB_Fp_dp_REDUCE_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the REDUCE output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by REDUCE.
        """
        from comp.GB_Fp_dp.REDUCE.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "7: $ {x}$" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        reduceOutput = """Reduce (Free CSL version), 27-Apr-10 ...

1: 
2: 
3: 
4: 
5: 
6: 
=====Solution Begin=====$

7: 
{x**3*y**3 + x*y*z**3*t + 4*y**2*z**3*t + x*y**2*z + x*t**3 + 4*z**2*t**2 + x*t 
+ 4*y*t + 4*x + 4*y,
x*z**2*t**3 + 4*x**2*t**2 + 4*x*z**2 + 4*y*z**2,
z**2*t**4 + 4*x*y*z**3 + 4*x*t**3 + 4*z**2*t,
x**3*y*t + x*z*t**3 + 4*z**3*t**2 + x*z*t + 4*x*z + 4*y*z,
x**3*t**2 + 4*z*t**4 + x*y*z**2 + z*t,
x**2*t**3 + 4*z**4,
x*y*t**3 + 4*x*z**2*t**2 + z**4 + x**2*t + 4*x**2 + 3*x*y + 4*y**2,
x*z**4 + 4*x**3 + 4*x**2*y + 4*z,
x*t**4 + 4*x*t + 4*y*t + 4*z**2,
y*z**4 + x**3*t + 4*z*t**3 + 4*x**2*y + 4*x*y**2 + z,
y*t**4 + 4*z**2*t**3 + 4*x*y**2*z + x*t**2 + 4*y*t + z**2,
z**5 + 4*t**4,
z**4*t + 4*x**2*t + 4*x*y*t + 4*x*z**2,
t**5 + 4*x*y*z*t + 4*x*z**3 + 4*t**2,
x**4 + x**3*y + 4*z**3*t + x*z,
x**2*z + 4*t}$

8: 
=====Solution End=====$

9: 
"""
        try:
            tempRes = extractSolution(reduceOutput)
        except:
            self.fail("Could not parse valid REDUCE output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>x^3*y^3 + x*y*z^3*t + 4*y^2*z^3*t + x*y^2*z + x*t^3 + 4*z^2*t^2 + x*t 
+ 4*y*t + 4*x + 4*y</polynomial>
    <polynomial>x*z^2*t^3 + 4*x^2*t^2 + 4*x*z^2 + 4*y*z^2</polynomial>
    <polynomial>z^2*t^4 + 4*x*y*z^3 + 4*x*t^3 + 4*z^2*t</polynomial>
    <polynomial>x^3*y*t + x*z*t^3 + 4*z^3*t^2 + x*z*t + 4*x*z + 4*y*z</polynomial>
    <polynomial>x^3*t^2 + 4*z*t^4 + x*y*z^2 + z*t</polynomial>
    <polynomial>x^2*t^3 + 4*z^4</polynomial>
    <polynomial>x*y*t^3 + 4*x*z^2*t^2 + z^4 + x^2*t + 4*x^2 + 3*x*y + 4*y^2</polynomial>
    <polynomial>x*z^4 + 4*x^3 + 4*x^2*y + 4*z</polynomial>
    <polynomial>x*t^4 + 4*x*t + 4*y*t + 4*z^2</polynomial>
    <polynomial>y*z^4 + x^3*t + 4*z*t^3 + 4*x^2*y + 4*x*y^2 + z</polynomial>
    <polynomial>y*t^4 + 4*z^2*t^3 + 4*x*y^2*z + x*t^2 + 4*y*t + z^2</polynomial>
    <polynomial>z^5 + 4*t^4</polynomial>
    <polynomial>z^4*t + 4*x^2*t + 4*x*y*t + 4*x*z^2</polynomial>
    <polynomial>t^5 + 4*x*y*z*t + 4*x*z^3 + 4*t^2</polynomial>
    <polynomial>x^4 + x^3*y + 4*z^3*t + x*z</polynomial>
    <polynomial>x^2*z + 4*t</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for REDUCE output parse.")

    def test_GB_Fp_dp_Risa_Asir_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Risa/Asir output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by Risa/Asir.
        """
        from comp.GB_Fp_dp.Risa_Asir.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "[x]" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        risaasirOutput = """=====Solution Begin=====
[z*x^2+4*t,x^4+y*x^3+z*x+4*t*z^3,(4*t*z*y+4*z^3)*x+t^5+4*t^2,4*t*x^2+(4*t*y+4*z^2)*x+t*z^4,z^5+4*t^4,(4*z*y^2+t^2)*x+(t^4+4*t)*y+(4*t^3+1)*z^2,t*x^3+4*y*x^2+4*y^2*x+z^4*y+(4*t^3+1)*z,(t^4+4*t)*x+4*t*y+4*z^2,4*x^3+4*y*x^2+z^4*x+4*z,(t+4)*x^2+((t^3+3)*y+4*t^2*z^2)*x+4*y^2+z^4,t^3*x^2+4*z^4,t^2*x^3+z^2*y*x+(4*t^4+t)*z,t*y*x^3+(t^3+t+4)*z*x+4*z*y+4*t^2*z^3,(4*z^3*y+4*t^3)*x+(t^4+4*t)*z^2,4*t^2*x^2+(t^3+4)*z^2*x+4*z^2*y,y^3*x^3+(z*y^2+t*z^3*y+t^3+t+4)*x+4*t*z^3*y^2+(4*t+4)*y+4*t^2*z^2]
=====Solution End=====
0
"""
        try:
            tempRes = extractSolution(risaasirOutput)
        except:
            self.fail("Could not parse valid Risa/Asir output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>z*x^2+4*t</polynomial>
    <polynomial>x^4+y*x^3+z*x+4*t*z^3</polynomial>
    <polynomial>(4*t*z*y+4*z^3)*x+t^5+4*t^2</polynomial>
    <polynomial>4*t*x^2+(4*t*y+4*z^2)*x+t*z^4</polynomial>
    <polynomial>z^5+4*t^4</polynomial>
    <polynomial>(4*z*y^2+t^2)*x+(t^4+4*t)*y+(4*t^3+1)*z^2</polynomial>
    <polynomial>t*x^3+4*y*x^2+4*y^2*x+z^4*y+(4*t^3+1)*z</polynomial>
    <polynomial>(t^4+4*t)*x+4*t*y+4*z^2</polynomial>
    <polynomial>4*x^3+4*y*x^2+z^4*x+4*z</polynomial>
    <polynomial>(t+4)*x^2+((t^3+3)*y+4*t^2*z^2)*x+4*y^2+z^4</polynomial>
    <polynomial>t^3*x^2+4*z^4</polynomial>
    <polynomial>t^2*x^3+z^2*y*x+(4*t^4+t)*z</polynomial>
    <polynomial>t*y*x^3+(t^3+t+4)*z*x+4*z*y+4*t^2*z^3</polynomial>
    <polynomial>(4*z^3*y+4*t^3)*x+(t^4+4*t)*z^2</polynomial>
    <polynomial>4*t^2*x^2+(t^3+4)*z^2*x+4*z^2*y</polynomial>
    <polynomial>y^3*x^3+(z*y^2+t*z^3*y+t^3+t+4)*x+4*t*z^3*y^2+(4*t+4)*y+4*t^2*z^2</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for Risa/Asir output parse.")

    def test_GB_Fp_dp_Singular_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Singular output on a GB_Z_lp-instance, i.e. the
        computation of a Groebner basis in a commutative polynomial ring

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by Singular.
        """
        from comp.GB_Fp_dp.Singular.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("abc123" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with no solution in \
between begin and end tag.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "x" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>x</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b
        singularOutput = """                     SINGULAR                                 /  Development
 A Computer Algebra System for Polynomial Computations       /   version 4.0.0
                                                           0<
 by: W. Decker, G.-M. Greuel, G. Pfister, H. Schoenemann     \   Dec 2013
FB Mathematik der Universitaet, D-67653 Kaiserslautern        \
=====Solution Begin=====
x3^2*x4^2,
x2^2+x3*x4,
x1+x2
=====Solution End=====

$Bye.
"""
        try:
            tempRes = extractSolution(singularOutput)
        except:
            self.fail("Could not parse valid Singular output string")
        expectedOutp = """<?xml version="1.0" ?>
<GB_Fp_dp_SOL>
  <basis>
    <polynomial>x3^2*x4^2</polynomial>
    <polynomial>x2^2+x3*x4</polynomial>
    <polynomial>x1+x2</polynomial>
  </basis>
</GB_Fp_dp_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "Output strings did not \
match for Singular output parse.")

    def test_SOL_R_poly_sys_Singular_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Singular output on a SOL_R_poly_sys-instance, i.e. finding
        real solutions to a given polynomial system of equations

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.2.) extractSolution on valid inputs
        1.2.a) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.b) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.c) Solution given really by Singular.
        """
        from comp.SOL_R_poly_sys.Singular.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n blabliblup")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("woahahaha\n" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr +" " +solEndStr)
        except:
            self.fail("1.2.a: Could parse a string with no solution in \
between begin and end tag, which is valid if no real solutions \
exist.")
        expectedOutp = """<?xml version="1.0" ?>
<SOL_R_poly_sys_SOL>
  <solutions/>
</SOL_R_poly_sys_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.b)
        try:
            tempRes = extractSolution(solBeginStr + "x1=0" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag")
        expectedOutp = """<?xml version="1.0" ?>
<SOL_R_poly_sys_SOL>
  <solutions>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>0</value>
      </equal>
    </solution>
  </solutions>
</SOL_R_poly_sys_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.b)")
        #1.2.c)
        singularOutput = """                     SINGULAR                                 /
 A Computer Algebra System for Polynomial Computations       /   version 4.0.1
                                                           0<
 by: W. Decker, G.-M. Greuel, G. Pfister, H. Schoenemann     \   Sep 2014
FB Mathematik der Universitaet, D-67653 Kaiserslautern        \
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/solve.lib (4.0.0.0,Jun_2013)
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/triang.lib (4.0.0.0,Jun_2013)
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/elim.lib (4.0.0.1,Jan_2014)
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/ring.lib (4.0.0.0,Jun_2013)
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/primdec.lib (4.0.0.0,Jun_2013)
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/absfact.lib (4.0.0.0,Jun_2013)
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/matrix.lib (4.0.0.0,Jun_2013)
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/nctools.lib (4.0.0.0,Jun_2013)
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/random.lib (4.0.0.0,Jun_2013)
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/poly.lib (4.0.0.0,Jun_2013)
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/inout.lib (4.0.0.0,Jun_2013)
// ** loaded /Applications/Singular/4-0-1/bin/../share/singular/LIB/general.lib (4.0.0.1,Jan_2014)

// 'solve' created a ring, in which a list SOL of numbers (the complex solutions)
// is stored.
// To access the list of complex solutions, type (if the name R was assigned
// to the return value):
        setring R; SOL; 
=====Solution Begin=====
x1=0, x2=0, x3=1, x4=0
x1=0, x2=1, x3=0, x4=0
x1=0.68043737, x2=-0.33314102, x3=0.68043737, x4=-0.33314102
x1=-0.33314102, x2=0.68043737, x3=0.68043737, x4=-0.33314102
x1=0.58740105, x2=-0.32748, x3=0.58740105, x4=0.58740105
x1=-0.32748, x2=0.58740105, x3=0.58740105, x4=0.58740105
x1=0.68043737, x2=-0.33314102, x3=-0.33314102, x4=0.68043737
x1=-0.33314102, x2=0.68043737, x3=-0.33314102, x4=0.68043737
x1=-2.87938524, x2=-2.87938524, x3=-2.87938524, x4=-2.87938524
x1=-0.65270364, x2=-0.65270364, x3=-0.65270364, x4=-0.65270364
x1=0.58740105, x2=0.58740105, x3=0.58740105, x4=-0.32748
x1=0.53208889, x2=0.53208889, x3=0.53208889, x4=0.53208889
x1=0.68043737, x2=0.68043737, x3=-0.33314102, x4=-0.33314102
x1=0.58740105, x2=0.58740105, x3=-0.32748, x4=0.58740105
x1=-0.33314102, x2=-0.33314102, x3=0.68043737, x4=0.68043737
x1=1, x2=0, x3=0, x4=0
x1=0, x2=0, x3=0, x4=1
=====Solution End=====
$Bye.
real 0.10
user 0.10
sys 0.00"""
        try:
            tempRes = extractSolution(singularOutput)
        except:
            self.fail("Could not accept a regular Singular output (1.2.c)")
        expectedOutp = """<?xml version="1.0" ?>
<SOL_R_poly_sys_SOL>
  <solutions>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>0</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>0</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>1</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>0</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>0</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>1</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>0</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>0</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>0.68043737</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>-0.33314102</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>0.68043737</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>-0.33314102</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>-0.33314102</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>0.68043737</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>0.68043737</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>-0.33314102</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>0.58740105</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>-0.32748</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>0.58740105</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>0.58740105</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>-0.32748</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>0.58740105</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>0.58740105</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>0.58740105</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>0.68043737</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>-0.33314102</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>-0.33314102</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>0.68043737</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>-0.33314102</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>0.68043737</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>-0.33314102</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>0.68043737</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>-2.87938524</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>-2.87938524</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>-2.87938524</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>-2.87938524</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>-0.65270364</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>-0.65270364</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>-0.65270364</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>-0.65270364</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>0.58740105</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>0.58740105</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>0.58740105</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>-0.32748</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>0.53208889</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>0.53208889</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>0.53208889</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>0.53208889</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>0.68043737</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>0.68043737</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>-0.33314102</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>-0.33314102</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>0.58740105</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>0.58740105</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>-0.32748</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>0.58740105</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>-0.33314102</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>-0.33314102</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>0.68043737</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>0.68043737</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>1</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>0</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>0</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>0</value>
      </equal>
    </solution>
    <solution>
      <equal>
        <varName>x1</varName>
        <value>0</value>
      </equal>
      <equal>
        <varName>x2</varName>
        <value>0</value>
      </equal>
      <equal>
        <varName>x3</varName>
        <value>0</value>
      </equal>
      <equal>
        <varName>x4</varName>
        <value>1</value>
      </equal>
    </solution>
  </solutions>
</SOL_R_poly_sys_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.c)")

    def test_SOL_R_poly_sys_Z3_Sol(self):
        """
        Here, we are testing the template to extract the solution from
        the Z3 output on a SOL_R_poly_sys-instance, i.e. finding
        real solutions to a given polynomial system of equations

        The covered test cases are:
        1.1.) extractSolution on invalid inputs
        1.1.a) Wrong datatype
        1.1.b) String without the "=====Solution Begin=====" and
               "=====Solution End=====" tags.
        1.1.c) String with the "=====Solution Begin=====" tag, but not
               with the "=====Solution End=====" tag
        1.1.d) String with the "=====Solution End=====" tag, but not
               with the "=====Solution Begin=====" tag
        1.1.e) String with both the "=====Solution Begin=====" and the
               "=====Solution End=====" tag, but with whitespace in
               between.
        1.2.) extractSolution on valid inputs
        1.2.a) String with The solution right after "=====Solution
               Begin=====" tag, and ending right at "=====Solution
               End====="
        1.2.b) Solution given really by Z3.
        """
        from comp.SOL_R_poly_sys.Z3.template_sol import extractSolution
        testPassed = 1
        solBeginStr = "=====Solution Begin====="
        solEndStr   = "=====Solution End====="
        #1.1.a)
        try:
            extractSolution(1)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("I was able to try to extract a solution from an \
int.")
        #1.1.b)
        try:
            extractSolution("abc123")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Invalid solution string did not cause \
exception")
        #1.1.c)
        try:
            extractSolution(solBeginStr + "\n\n blabliblup")
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with begin, but not with \
end tag.")
        #1.1.d)
        try:
            extractSolution("woahahaha\n" + solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("Could parse a string with end, but not with \
begin tag")
        #1.1.e)
        try:
            tempRes = extractSolution(solBeginStr +" " +solEndStr)
            testPassed = 0
        except:
            pass
        if not testPassed:
            self.fail("1.2.a: Could parse a string with no solution in \
between begin and end tag, which is valid if no real solutions \
exist.")
        #1.2.a)
        try:
            tempRes = extractSolution(solBeginStr + "sat" + solEndStr)
        except:
            self.fail("Could not accept a solution with no whitespace \
between the begin and the end tag (1.2a)")
        expectedOutp = """<?xml version="1.0" ?>
<SOL_R_poly_sys_SOL>
  <satisfiable>1</satisfiable>
</SOL_R_poly_sys_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.a)")
        #1.2.c)
        z3Output = """=====Solution Begin=====
sat
=====Solution End====="""
        try:
            tempRes = extractSolution(z3Output)
        except:
            self.fail("Could not accept a regular Singular output (1.2.b)")
        expectedOutp = """<?xml version="1.0" ?>
<SOL_R_poly_sys_SOL>
  <satisfiable>1</satisfiable>
</SOL_R_poly_sys_SOL>
"""
        self.assertEqual(tempRes,expectedOutp, "XML string did not \
match for 1.2.b)")
    
if __name__=="__main__":
    unittest.main()
