# Issue 5661: implement numerical_diff and generalize numerical_integral

Issue created by migration from https://trac.sagemath.org/ticket/5661

Original creator: ncalexan

Original creation time: 2009-04-01 21:31:26

Assignee: jkantor

CC:  jkantor

Keywords: numerical integration differentiation

sage does not differentiate numerically at this time; a `numerical_diff` similar to Maple's `fdiff` would have helped me implement Riemann theta functions.

sage's `numerical_integral` uses GSL, which means it only handles RDF.  Weak!


---

Comment by was created at 2009-04-02 15:21:17

Pari can do arbitrary precision numerical integration.  It would be cool if you could make a version of numerical_integral that uses PARI instead, and is hence arbitrary precision.    It would likely be a lot lot slower than the GSL-based numerical_integral, though.


---

Comment by fredrik.johansson created at 2009-04-02 20:46:05

Arbitrary-precision integration and differentiation is also available in mpmath.


---

Comment by was created at 2009-04-02 23:17:10

> Arbitrary-precision integration and differentiation is also available in mpmath. 

Cool.  And in case people don't know, mpmath is in Sage.

```
sage: import sympy.mpmath
sage: sympy.mpmath.
Display all 206 possibilities? (y or n)
```

