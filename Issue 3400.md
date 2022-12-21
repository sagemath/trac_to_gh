# Issue 3400: Elements of GL(n,R) should coerce properly to matrices

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-06-11 16:23:08

Assignee: robertwb

CC:  alexghitza

For example:


```
sage: M = Matrix(GF(2), [This is the Trac macro *1,1,1,1* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,1,1,1-macro))
sage: G = GL(4,2)
sage: N = G.0
sage: M
[1 1 1 1]
sage: N

[1 1 0 0]
[0 1 0 0]
[0 0 1 0]
[0 0 0 1]
sage: M*N
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/rlmill/sage-3.0.2/<ipython console> in <module>()

/Users/rlmill/sage-3.0.2/element.pyx in sage.structure.element.Matrix.__mul__ (sage/structure/element.c:11352)()

/Users/rlmill/sage-3.0.2/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5301)()

TypeError: unsupported operand parent(s) for '*': 'Full MatrixSpace of 1 by 4 dense matrices over Finite Field of size 2' and 'General Linear Group of degree 4 over Finite Field of size 2'
sage: M*N.matrix()
[1 0 1 1]
```



---

Comment by mhansen created at 2008-09-19 06:55:26

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-19 06:55:26

Changing assignee from robertwb to mhansen.


---

Comment by robertwb created at 2010-01-17 11:09:21

Changing status from new to needs_review.


---

Attachment


---

Comment by rbeezer created at 2010-01-18 05:09:09

Passes all tests and works as advertised.  Positive review.


---

Comment by rbeezer created at 2010-01-18 05:09:09

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-01-18 22:43:01

Resolution: fixed
