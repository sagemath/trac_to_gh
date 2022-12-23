# Issue 4143: injvar() docstring should be the same as inject_variables()

Issue created by migration from https://trac.sagemath.org/ticket/4143

Original creator: schilly

Original creation time: 2008-09-18 10:23:39

Assignee: tbd

The `injvar()` command has no docstring. Maybe depreciate it and use the docstring of `inject_variables()` ?


```
R = PolynomialRing( GF(Integer(2)), ['a%s'%i for i in range(Integer(93))] + ['b%s'%i for i in range(Integer(84))], order='degrevlex' )

R.injvar?
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in method injvar of sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular object at 0xb1c32414>
Namespace:      Interactive
Docstring:
    <no docstring>
Class Docstring:
    <attribute '__doc__' of 'builtin_function_or_method' objects>
```




---

Comment by malb created at 2008-09-18 10:43:16

> There should be one-- and preferably only one --obvious way to do it.
(http://www.python.org/dev/peps/pep-0020/)

I vote for deprecation of `injvar`.


---

Attachment

This patch deprecates injvar.


---

Comment by robertwb created at 2008-12-12 01:42:12

I agree with deprecating this, and the patch looks good to me.


---

Comment by mabshoff created at 2008-12-12 06:32:13

Resolution: fixed


---

Comment by mabshoff created at 2008-12-12 06:32:13

Merged in Sage 3.2.2.alpha2
