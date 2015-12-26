class FA_Q_dp_SOL():
    """
    This class represents the solution of the Groebner basis calculation with respect
    to the degree-lexicographic ordering, given generators of an ideal in the free algebra.

    The solution is represented by a list of generators of the ideal. In our case,
    we provide a list of strings, each representing a generator.

    .. moduleauthor:: Albert Heinle <aheinle@uwaterloo.ca>
    """

    def __init__(self, basis, originalGenerators=[],variables=[], upToDeg=0):
        """
        The constructor of the FA_Q_dp_SOL class. It consumes a parameter basis,
        which is a list of strings, where each string represents an element of the
        groebner basis of the original ideal.

        Optionally, also the original generators, the variable list and the degree,
        up to which the generators were calculated, is provided.

        :param basis: A list of strings, representing the calculated Groebner Basis
        :type  basis: list of str
        :param originalGenerators: A list of strings, representing the original generators
                                   of the considered ideal. If not specified, empty list.
        :type  originalGenerators: list of str
        :param variables: A list of strings, representing the variables that appear in the
                     free algebra. If not specified, empty list.
        :type variables: list of str
        :param upToDeg: Represents the degree, up to which the Groebner basis was calculated.
                        If not specified, zero.
        :type  upToDeg: int
        :raises TypeError: In case, one of the inputs were not of correct type
        """
        #Input Check
        if ((type(basis)!=list) or (type(originalGenerators)!=list) or
            (type(variables)!=list) or (type(upToDeg)!=int)):
            raise TypeError("One of the input parameters of FA_Q_dp_SOL did not have the correct type")

        for i in basis:
            if type(i) != str:
                raise TypeError("The elements in the parameter basis were not of type string")
        for i in originalGenerators:
            if type(i) != str:
                raise TypeError("The elements in the parameter originalGenerators were not of type string")
        for i in variables:
            if type(i) != str:
                raise TypeError("The elements in the parameter variables were not of type string")
        #Input Check Done
        self.__basis = basis
        self.__originalGenerators = originalGenerators
        self.__vars = variables
        self.__upToDeg = upToDeg

    def getBasis(self):
        """
        Getter for the internal variable basis

        :returns: The calculated Groebner basis
        :rtype: list of str
        """
        return self.__basis

    def getOriginalGenerators(self):
        """
        Returns the list of original generators of the ideal, if existent.

        :returns: either [], or a list of strings representing the original generators
        :rtype:   list of str
        """
        return self.__originalGenerators

    def getVars(self):
        """
        Returns the list of variables, if provided. Empty list otherwise

        :returns: either [], or a list of strings representing the occurring variables
        :rtype:   list of str
        """
        return self.__vars

    def getUpToDeg(self):
        """
        Returns the degree, up to which the Groebner basis was calculated, if provided. Empty list otherwise.

        :returns: either [], or a list of strings representing the occurring variables
        :rtype:   list of string
        """
        return self.__upToDeg

    def __str__(self):
        """
        Returns the string representation of the solution of the calculation.

        It will have the following form::
          ====================
          The Calculated Groebner basis is:
          <element 1>,
          <element 2>,
          ...
          ====================
          Optional Information, if provided
          --------------------
          The original list of generators was:
          <element 1>,
          <element 2>,
          ...

          The set of variables is:
          <var1>, <var2>, <var3>, ...

          The degree, up to which the Groebner basis was calculated is: <deg>
          ====================
          
        
        :returns: String representation of the instance class FA_Q_dp_SOL
        :rtype:   str
        """
        result = """====================
The Calculated Groebner basis is:
%s

====================
Optional Information, if provided
--------------------
The original list of generators was:
%s

The set of variables is:
%s

The degree, up to which the Groebner basis was calculated is: %i
====================
""" % (",\n".join(v for v in self.__basis), ",\n".join(v for v in self.__originalGenerators),
       ", ".join(v for v in self.__vars), self.__upToDeg)
        return result
