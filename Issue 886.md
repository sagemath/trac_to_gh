# Issue 886: 2.8.7-alpha0: doctest failure in rings/integer_mod.pyx (expecting wrong type)

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-10-13 20:25:31

Assignee: failure

A trivial doctest failure.  On sage.math:

```
File "integer_mod.pyx", line 460:
    sage: type(a.polynomial())
Expected:
    <class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_dense_mod_p'>
Got:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
```



---

Attachment

The obvious fix.


---

Comment by was created at 2007-10-14 22:56:18

Resolution: fixed
