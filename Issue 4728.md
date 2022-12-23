# Issue 4728: .roots() is inconsistent between polynomials and symbolic polynomials

Issue created by migration from https://trac.sagemath.org/ticket/4728

Original creator: ncalexan

Original creation time: 2008-12-06 19:55:25

Assignee: malb

Keywords: roots symbolic polynomial

The lack of multiplicities= keyword and the failure to try to convert to a polynomial first irritates me.  Actually, the default symbolic 'x' irritates me most of all, but I don't intend to open a ticket for that.


```
sage: (var('x') - 1).roots()
[(1, 1)]
sage: (var('x') - 1).roots(QQbar)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2816, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2790, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/96844/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in roots(self, x, explicit_solutions)
   3077         if x is None:
   3078             x = self.default_variable()
-> 3079         S, mul = self.solve(x, multiplicities=True, explicit_solutions=explicit_solutions)
   3080         if len(mul) == 0 and explicit_solutions:
   3081             raise RuntimeError, "no explicit roots found"

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in solve(self, x, multiplicities, explicit_solutions)
   3103         """
   3104         x = var(x)
-> 3105         return (self == 0).solve(x, multiplicities=multiplicities, explicit_solutions=explicit_solutions)
   3106 
   3107     def find_root(self, a, b, var=None, xtol=10e-13, rtol=4.5e-16, maxiter=100, full_output=False):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/equations.pyc in solve(self, x, multiplicities, solution_dict, explicit_solutions)
   1021         from sage.calculus.calculus import SymbolicVariable, SymbolicFunction, SymbolicFunctionEvaluation
   1022         if not isinstance(x,(SymbolicVariable,SymbolicFunction,SymbolicFunctionEvaluation)):
-> 1023             raise TypeError, "%s is not a valid variable."%x
   1024 
   1025         m = self._maxima_()

TypeError: not all arguments converted during string formatting
sage: (var('x')^2 - 1).roots(CC)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2816, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2791, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (592, 0))

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/96844/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in roots(self, x, explicit_solutions)
   3077         if x is None:
   3078             x = self.default_variable()
-> 3079         S, mul = self.solve(x, multiplicities=True, explicit_solutions=explicit_solutions)
   3080         if len(mul) == 0 and explicit_solutions:
   3081             raise RuntimeError, "no explicit roots found"

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in solve(self, x, multiplicities, explicit_solutions)
   3102             [z == e^(2*I*pi/5), z == e^(4*I*pi/5), z == e^(-(4*I*pi/5)), z == e^(-(2*I*pi/5)), z == 1]        
   3103         """
-> 3104         x = var(x)
   3105         return (self == 0).solve(x, multiplicities=multiplicities, explicit_solutions=explicit_solutions)
   3106 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in var(s, create)
   5467         return tuple([var(x.strip()) for x in s.split(',')])
   5468     elif ' ' in s:
-> 5469         return tuple([var(x.strip()) for x in s.split()])
   5470     try:
   5471         v = _vars[s]

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in var(s, create)
   5476             raise ValueError, "the variable '%s' has not been defined"%var
   5477         pass
-> 5478     v = SymbolicVariable(s)
   5479     _vars[s] = v
   5480     _syms[s] = v

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __init__(self, name)
   5301             raise ValueError, "variable name must be nonempty"
   5302         elif not is_python_identifier.match(name):
-> 5303             raise ValueError, "variable name is not a valid Python identifier"
   5304 
   5305     def __hash__(self):

ValueError: variable name is not a valid Python identifier
sage: (var('x')^2 - 1).roots(CC, multiplicities=False)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/96844/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

TypeError: roots() got an unexpected keyword argument 'multiplicities'
sage: (QQ['x'].0^2 - 1).roots(CC, multiplicities=False)
[-1.00000000000000, 1.00000000000000]
```



---

Comment by ncalexan created at 2009-01-22 09:47:52

It's not perfect, but it's more in line with the polynomial .roots() method.

My least favourite thing is that giving one keyword argument must remain the variable, to maintain backwards compatability.


---

Attachment


---

Comment by malb created at 2009-01-22 19:44:41

The only issue I see is:


```
multiplicities -- bool (default True); when True, return 
multiplicities 
```


should be


```
multiplicities -- bool (default True); when True, return 
                  multiplicities 
```



---

Comment by jason created at 2009-01-28 17:54:37

apply on top of previous patch


---

Attachment

positive review.  I've posted a small patch for the docs to correct the problem malb pointed out.  All tests pass in calculus.py.


---

Comment by mabshoff created at 2009-01-29 00:26:55

Resolution: fixed


---

Comment by mabshoff created at 2009-01-29 00:26:55

Merged both patches in Sage 3.3.alpha3.

Cheers,

Michael
