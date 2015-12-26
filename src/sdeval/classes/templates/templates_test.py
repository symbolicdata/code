import unittest

class TestTemplates(unittest.TestCase):
    """
    Tests for the different templates to generate code for different Computer algebra systems.

    .. moduleauthor:: Albert Heinle <albert.heinle@uwaterloo.ca>
    """

    def test_FA_Q_DP_GAP(self):
        """
        This test checks the template FA_Q_DP for GAP.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.FA_Q_dp.GAP.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        uptoDeg = 10;
        expectedString = """LoadPackage("GBNP","0",false);
SetInfoLevel(InfoGBNP,1);
SetInfoLevel(InfoGBNPTime,1);
F := Rationals;
A := FreeAssociativeAlgebraWithOne(F,"x4","x3","x2","x1");
g :=GeneratorsOfAlgebraWithOne(A);
x4 := g[1];
x3 := g[2];
x2 := g[3];
x1 := g[4];
weights := [1,1,1,1];
KI_gp := [x1+x2,x3*x4-x2*x1,x1*x2*x3*x4];
KI_np :=GP2NPList(KI_gp);
GB :=SGrobnerTrunc(KI_np,10,weights);
GBNP.ConfigPrint("x4","x3","x2","x1");
Print("=====Solution Begin=====");
PrintNPList(GB);
Print("=====Solution End=====");
Length(GB);
quit;"""
        output = generateCode(vars,basis,uptoDeg)
        print output
        print expectedString
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_FA_Q_DP_Singular(self):
        """
        This test checks the template FA_Q_DP for Singular.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.FA_Q_dp.Singular.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        uptoDeg = 10;
        expectedString = """LIB "freegb.lib";
ring r = 0,(x1,x2,x3,x4),dp;
int d = 10;
def R = makeLetterplaceRing(d);
 setring(R);
ideal I = x1(1)+x2(1),
x3(1)*x4(2)-x2(1)*x1(2),
x1(1)*x2(2)*x3(3)*x4(4);
option(prot);
option(redTail);
option(redSB);
ideal J = letplaceGBasis(I);
print("=====Solution Begin=====");
print (J, "%s");
print(\"=====Solution End=====\");$;"""
        output = generateCode(vars,basis,uptoDeg)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_FA_Q_DP_Magma(self):
        """
        This test checks the template FA_Q_DP for Magma.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.FA_Q_dp.Magma.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        uptoDeg = 10;
        expectedString = """F := RationalField();
A<x1,x2,x3,x4> := FreeAlgebra(F,4);
B := [x1+x2,
x3*x4-x2*x1,
x1*x2*x3*x4];
print "=====Solution Begin=====";
GroebnerBasis(B,10);
print "=====Solution End=====";
quit;"""
        output = generateCode(vars,basis,uptoDeg)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_FP_DP_GAP(self):
        """
        This test checks the template GB_Fp_dp for GAP.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Fp_dp.GAP.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        characteristic = 5
        expectedString = """F := GaloisField(5);
PR := PolynomialRing(F,["x1","x2","x3","x4"]);
x1:= IndeterminatesOfPolynomialRing(PR)[1];
x2:= IndeterminatesOfPolynomialRing(PR)[2];
x3:= IndeterminatesOfPolynomialRing(PR)[3];
x4:= IndeterminatesOfPolynomialRing(PR)[4];
I:= Ideal(PR,[x1+x2,x3*x4-x2*x1,x1*x2*x3*x4]);
ord := MonomialGrlexOrdering(x1,x2,x3,x4);
B := GroebnerBasis(I,ord);
Print("=====Solution Begin=====");
B;
Print("=====Solution End=====");
quit;"""
        output = generateCode(vars,basis,characteristic)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_FP_DP_Singular(self):
        """
        This test checks the template GB_Fp_dp for Singular.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Fp_dp.Singular.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        characteristic = 5
        expectedString = """ring R = 5,(x1,x2,x3,x4),lp;
ideal I = x1+x2,
x3*x4-x2*x1,
x1*x2*x3*x4;
ideal J = std(I);
print("=====Solution Begin=====");
print(J);
print("=====Solution End=====");
$"""
        output = generateCode(vars,basis,characteristic)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_FP_DP_Magma(self):
        """
        This test checks the template GB_Fp_dp for Magma.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Fp_dp.Magma.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        characteristic = 5
        expectedString = """F := FiniteField(5);
P<x1,x2,x3,x4> := PolynomialRing(F,4);
I := ideal<P | x1+x2,x3*x4-x2*x1,x1*x2*x3*x4>;
B := GroebnerBasis(I);
print "=====Solution Begin=====";
B;
print "=====Solution End=====";
quit;"""
        output = generateCode(vars,basis,characteristic)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_FP_DP_Maple(self):
        """
        This test checks the template GB_Fp_dp for Maple.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Fp_dp.Maple.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        characteristic = 5
        expectedString = r"""with(Groebner):
Ideal := {x1+x2,x3*x4-x2*x1,x1*x2*x3*x4} mod 5:
ordering := grlex(x1,x2,x3,x4):
B := Basis(Ideal, ordering):
printf("=====Solution Begin=====");
printf("%a\n",B);
printf("=====Solution End=====");
quit;"""
        output = generateCode(vars,basis,characteristic)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Z_lp_Maple(self):
        """
        This test checks the template GB_Z_lp for Maple.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Z_lp.Maple.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        expectedString = r"""with(Groebner):
Ideal := {x1+x2,x3*x4-x2*x1,x1*x2*x3*x4}:
ordering := plex(x1,x2,x3,x4):
B := Basis(Ideal, ordering):
printf("=====Solution Begin=====");
printf("%a\n",B);
printf("=====Solution End=====");
quit;"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Z_lp_Singular(self):
        """
        This test checks the template GB_Z_lp for Singular.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Z_lp.Singular.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        expectedString = """ring R = 0,(x1,x2,x3,x4),lp;
ideal I = x1+x2,
x3*x4-x2*x1,
x1*x2*x3*x4;
ideal J = std(I);
print("=====Solution Begin=====");
print(J);
print("=====Solution End=====");
$"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Z_lp_Magma(self):
        """
        This test checks the template GB_Z_lp for Magma.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Z_lp.Magma.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        expectedString = """F := RationalField();
P<x1,x2,x3,x4> := PolynomialRing(F,4);
I := ideal<P | x1+x2,x3*x4-x2*x1,x1*x2*x3*x4>;
B := GroebnerBasis(I);
print "=====Solution Begin=====";
B;
print "=====Solution End=====";
quit;"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Z_LP_GAP(self):
        """
        This test checks the template GB_Z_lp for GAP.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Z_lp.GAP.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        expectedString = """F := Rationals;
PR := PolynomialRing(F,["x1","x2","x3","x4"]);
x1:= IndeterminatesOfPolynomialRing(PR)[1];
x2:= IndeterminatesOfPolynomialRing(PR)[2];
x3:= IndeterminatesOfPolynomialRing(PR)[3];
x4:= IndeterminatesOfPolynomialRing(PR)[4];
I:= Ideal(PR,[x1+x2,x3*x4-x2*x1,x1*x2*x3*x4]);
ord := MonomialLexOrdering(x1,x2,x3,x4);
B := GroebnerBasis(I,ord);
Print("=====Solution Begin=====");
B;
Print("=====Solution End=====");
quit;"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Z_LP_REDUCE(self):
        """
        This test checks the template GB_Z_lp for REDUCE.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Z_lp.REDUCE.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1+x2','x3*x4-x2*x1','x1*x2*x3*x4']
        expectedString = """load_package groebner;
off nat;
torder({x1,x2,x3,x4}, lex)$
write "=====Solution Begin=====";
groebner{x1+x2,x3*x4-x2*x1,x1*x2*x3*x4};
write "=====Solution End=====";
quit;"""
        output = generateCode(vars,basis)
        print output
        print expectedString
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Z_LP_RISA_ASIR(self):
        """
        This test checks the template GB_Z_lp for Risa/Asir.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Z_lp.Risa_Asir.template import generateCode
        vars = ['x','y','z','t']
        basis=['x^10-t', 'x^8-z', 'x^31-x^6-x-y']
        expectedString = """load("gr")$
B=[x^10-t, x^8-z, x^31-x^6-x-y]$
print("=====Solution Begin=====");
print(gr(B,[x,y,z,t],2));
print("=====Solution End=====");"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Fp_dp_RISA_ASIR(self):
        """
        This test checks the template GB_Fp_dp for Risa/Asir.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Fp_dp.Risa_Asir.template import generateCode
        vars = ['x','y','z','t']
        basis=['x^10-t', 'x^8-z', 'x^31-x^6-x-y']
        characteristic=5;
        expectedString = """load("gr")$
B=[x^10-t, x^8-z, x^31-x^6-x-y]$
print("=====Solution Begin=====");
print(gr_mod(B,[x,y,z,t],1,5));
print("=====Solution End=====");
"""
        output = generateCode(vars,basis,characteristic)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_GB_Fp_dp_REDUCE(self):
        """
        This test checks the template GB_Fp_dp for REDUCE.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.GB_Fp_dp.REDUCE.template import generateCode
        vars = ['x','y','z','t']
        basis=['x^10-t', 'x^8-z', 'x^31-x^6-x-y']
        characteristic=5;
        expectedString = """on modular$
off nat;
setmod 5$
load_package groebner;
torder({x,y,z,t}, gradlex)$
write "=====Solution Begin=====";
groebner{x^10-t, x^8-z, x^31-x^6-x-y};
write "=====Solution End=====";
quit;"""
        output = generateCode(vars,basis,characteristic)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_SOL_R_poly_sys_Singular(self):
        """
        This test checks the template SOL_R_poly_sys for Singular.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.SOL_R_poly_sys.Singular.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1^3+x2^2+x3^2+x4^2-1',
               'x2^3+x1^2+x3^2+x4^2-1',
               'x3^3+x1^2+x2^2+x4^2-1',
               'x4^3+x1^2+x2^2+x3^2-1']
        expectedString = """LIB "solve.lib";
ring R = 0,(x1,x2,x3,x4),lp;
ideal I = x1^3+x2^2+x3^2+x4^2-1,
x2^3+x1^2+x3^2+x4^2-1,
x3^3+x1^2+x2^2+x4^2-1,
x4^3+x1^2+x2^2+x3^2-1;
int i; int j;
int isRealSolution;
string tempString;
def AC = solve(I,"nodisplay");
setring(AC);
print("=====Solution Begin=====");
if (defined(SOL))
{
  for (i = 1; i<= size(SOL); i++)
  {
    isRealSolution = 1;
    for (j=1; j<= size(SOL[i]);j++)
    {
      if (impart(SOL[i][j])!=0)
      {
        isRealSolution = 0;
        break;
      }
    }
    if (isRealSolution)
    {
      tempString = "";
      for (j=1; j<= size(SOL[i]);j++)
      {
        tempString =tempString+ string(var(j)) + "=" + string(SOL[i][j]);
        if (j!= size(SOL[i])){tempString = tempString + ", ";}
      }
      print(tempString);
    }
  }
  print("=====Solution End=====");
}
else
{
  print("An error occurred. Maybe the ideal was not zero-dimensional.");
}
$"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")

    def test_SOL_R_poly_sys_Z3(self):
        """
        This test checks the template SOL_R_poly_sys for Z3.

        The covered test cases are:
        1. Create executable string and check for correctness
        """
        #1
        from comp.SOL_R_poly_sys.Z3.template import generateCode
        vars = ['x1','x2','x3','x4']
        basis=['x1^3+x2^2+x3^2+x4^2-1',
               'x2^3+x1^2+x3^2+x4^2-1',
               'x3^3+x1^2+x2^2+x4^2-1',
               'x4^3+x1^2+x2^2+x3^2-1']
        expectedString = """(declare-const x1 Real)
(declare-const x2 Real)
(declare-const x3 Real)
(declare-const x4 Real)
(assert (= (+ (* x1 x1 x1) (* x2 x2) (* x3 x3) (- (* x4 x4) 1 ) ) 0))
(assert (= (+ (* x2 x2 x2) (* x1 x1) (* x3 x3) (- (* x4 x4) 1 ) ) 0))
(assert (= (+ (* x3 x3 x3) (* x1 x1) (* x2 x2) (- (* x4 x4) 1 ) ) 0))
(assert (= (+ (* x4 x4 x4) (* x1 x1) (* x2 x2) (- (* x3 x3) 1 ) ) 0))

(echo "=====Solution Begin=====")
(check-sat)
(echo "=====Solution End=====")
(exit)
"""
        output = generateCode(vars,basis)
        self.assertEqual(expectedString,output,
                         "Output string was different from what we expected.")
        
if __name__=="__main__":
    unittest.main()
