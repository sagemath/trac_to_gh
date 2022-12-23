# Issue 6803: Implement symbolic Kronecker delta and also make current signum (sgn) symbolic

Issue created by migration from https://trac.sagemath.org/ticket/6803

Original creator: gmhossain

Original creation time: 2009-08-22 11:34:45

We should have a symbolic Kronecker delta in Sage.

Also, current implementation of signum (sgn) function 
returns wrong answer for symbolic input.

```
sage: sgn(x)
1
sage: sgn(-x)
1
```


So we should make sgn() symbolic aware. Given, implementation of 
these functions in new symbolics should be very similar to the existing generalized function *Dirac delta* and *Heaviside*, I am putting them together here. 

Also, ticket #777 should be closed down as Sign is already in Sage
and this ticket will further enhance it.


---

Attachment


---

Comment by kcrisman created at 2009-09-23 02:42:17

Overall this is good, and should get positive review.  However, there is a doctest failure (very typical when one adds a new symbolic function in line 204 of symbolic/random_tests.py, with random_expr().  This should be easy to fix.


---

Comment by kcrisman created at 2009-11-10 15:58:15

I have attached the patch, but with the random test fixed as a reviewer patch.  Apply only this patch.


---

Comment by kcrisman created at 2009-11-10 15:58:15

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2009-11-10 15:58:36

Based on 4.2.1.alpha0, apply only this patch.


---

Comment by kcrisman created at 2009-11-10 15:58:50

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by mhansen created at 2009-11-17 07:27:19

I had to add a small patch to the doctest for sage.quadratic_forms.extras.sgn to make sure that the doctest was actually doctesting that function.


---

Comment by mhansen created at 2009-11-17 07:27:19

Resolution: fixed


---

Comment by kcrisman created at 2009-11-17 14:18:33

Replying to [comment:5 mhansen]:
> I had to add a small patch to the doctest for sage.quadratic_forms.extras.sgn to make sure that the doctest was actually doctesting that function.

Can you post that here, or at least the code in braces - just for posterity?


---

Comment by mvngu created at 2009-12-09 03:34:00

apply after previous


---

Attachment

Replying to [comment:6 kcrisman]:
> Can you post that here, or at least the code in braces - just for posterity?  

mhansen's patch is contained in `trac_6803-sgn.patch`
