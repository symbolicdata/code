"""
This is the template for the computation problem of finding real solutions of a polynomial system of equations.
It creates code for the computer algebra system Singular.

.. moduleauthor:: Albert Heinle <albert.heinle@googlemail.com>
"""

#--------------------------------------------------
#---------------The template-----------------------
#--------------------------------------------------

def generateCode(vars, basis):
    """
    The main function generating the Singular code for the computation of
    the real solutions of a polynomial systems of equations.

    :param         vars: A list of variables used in the IntPS-System
    :type          vars: list
    :param        basis: The polynomials forming a basis of the IntPS-System. This input will not be checked whether
                         there are polynomials using variables not in the list of variables.
    :type         basis: list
    """
    result = """LIB "solve.lib";
ring R = 0,(%s),lp;
ideal I = %s;
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
$""" % (",".join(vars),",\n".join(basis))
    return result

#--------------------------------------------------
#----------------Help Functions--------------------
#--------------------------------------------------
