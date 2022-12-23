# Issue 459: TypeError: unsupported operand parent(s) for '*': 'Polynomial Ring in u, v over Integer Ring'

Issue created by migration from https://trac.sagemath.org/ticket/459

Original creator: mhansen

Original creation time: 2007-08-19 14:26:12

Assignee: somebody


Here we go:

**********************************************************************
File "constructor.py", line 82:
   sage: EllipticCurve(R, [1,1])
Exception raised:
   Traceback (most recent call last):
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/
doctest.py", line 1212, in __run
       compileflags, 1) in test.globs
     File "<doctest __main__.example_1[10]>", line 1, in <module>
       EllipticCurve(R, [Integer(1),Integer(1)])###line 82:
   sage: EllipticCurve(R, [1,1])
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-
packages/sage/schemes/elliptic_curves/constructor.py", line 112, in
EllipticCurve
       return ell_generic.EllipticCurve_generic(x, y)
     File "/tmp/Work2/sage-2.8.1/sage-2.8.1/local/lib/python2.5/site-
packages/sage/schemes/elliptic_curves/ell_generic.py", line 98, in
__init__
       - (x**3 + a2*x**2*z + a4*x*z**2 + a6*z**3)
     File "element.pyx", line 1365, in element.RingElement.__mul__
     File "coerce.pyx", line 219, in
coerce.CoercionModel_cache_maps.bin_op_c
   TypeError: unsupported operand parent(s) for '*': 'Polynomial Ring
in u, v over Integer Ring' and 'Polynomial Ring in x, y, z over
Polynomial Ring in u, v over Integer Ring'
**********************************************************************

Cheers,

Michael



---

Comment by was created at 2007-08-19 18:44:37

Resolution: fixed


---

Attachment
