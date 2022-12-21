# Issue 1406: bug in coercion of multivariate polynomials (possibly libsingular related)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-06 04:00:21

Assignee: somebody

Reducing a polynomial to the libsingular polynomials to GF(p^n) is buggy as the following examples all illustrate. 


```
sage: R.<x,y> = QQ[]
sage: S.<xx,yy> = GF(5)[]
sage: S(5*x*y + x + 17*y)
0*xx*yy + xx + 2*yy
sage: R.<x,y> = ZZ[]
sage: S.<xx,yy> = GF(5)[]
sage: R.<x,y> = ZZ[]
sage: S.<xx,yy> = GF(25,'a')[]
sage: S(5*x*y + x + 17*y)
0*xx*yy + xx + 2*yy
sage: type(S(5*x*y + x + 17*y))
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
sage: R.<x,y> = ZZ[]
sage: S.<xx,yy> = Integers(5)[]
sage: S(5*x*y + x + 17*y)
xx + 2*yy
```



---

Comment by mhansen created at 2007-12-06 06:12:44

I have a fix for this, but it causes a segfault in the testing of multi_polynomial_ideal.py .

--Mike


---

Comment by mhansen created at 2007-12-06 06:12:44

Changing assignee from somebody to mhansen.


---

Comment by mhansen created at 2007-12-06 06:12:44

Changing status from new to assigned.


---

Attachment


---

Attachment

This is a -- I think -- better version of the 1406.patch that mhansen attached -- use it instead.


---

Comment by was created at 2007-12-06 16:00:48

Bonus -- my patch doesn't cause segfaults in multi_polynomial_ideal.py... I think.


---

Comment by mhansen created at 2007-12-06 19:48:30

Actually, it turns out that that segfault was there all along (with or without the patch).  See #1409 .


---

Comment by mabshoff created at 2007-12-06 20:46:27

Ok, looks good to me, merging William's patch.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-06 20:48:03

Merged in 2.9.alpha1.


---

Comment by mabshoff created at 2007-12-06 20:48:03

Resolution: fixed
