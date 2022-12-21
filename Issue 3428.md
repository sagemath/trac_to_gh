# Issue 3428: [with patch, needs review] univariate polynomial quo_rem 0 trouble

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-06-15 19:34:54

Assignee: somebody

Attached patch fixes this:


```
sage: R.<x> = ZZ[]
sage: 0//(2*x)
---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)

...
/home/burcin/work/sage/sage-3.0.2/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.quo_rem (sage/rings/polynomial/polynomial_integer_dense_ntl.cpp:4638)()

ArithmeticError: division not exact in Z[x] (consider coercing to Q[x] first) 
```



---

Comment by burcin created at 2008-06-15 19:35:38

univariate poly quo_rem zero handling fix


---

Comment by craigcitro created at 2008-06-15 21:55:42

Changing keywords from "" to "editor_craigcitro".


---

Attachment


---

Comment by burcin created at 2008-06-17 19:41:13

This won't be necessary when #2357 is merged. I suggest we resolve this with `wontfix`.


---

Comment by burcin created at 2008-06-17 19:41:13

Resolution: fixed


---

Comment by craigcitro created at 2008-06-17 22:37:04

Resolution changed from fixed to 


---

Comment by craigcitro created at 2008-06-17 22:37:04

Changing status from closed to reopened.


---

Comment by craigcitro created at 2008-06-17 22:37:04

However, we're not going to kill the NTL interface, so this should still be fixed.


---

Comment by craigcitro created at 2008-06-19 20:20:21

Looks good. I added one additional doctest to make sure that the exact failure reported is now doctested. 

Review by craigcitro and ncalexan.


---

Comment by craigcitro created at 2008-06-19 20:20:50

apply after Burcin's patch


---

Comment by mabshoff created at 2008-06-23 10:00:53

Resolution: fixed


---

Attachment

Merged in Sage 3.0.4.alpha0
