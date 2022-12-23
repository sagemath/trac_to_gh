# Issue 2179: [with patch] implementation mpoly factoring with coefficients in ZZ

Issue created by migration from https://trac.sagemath.org/ticket/2179

Original creator: jbmohler

Original creation time: 2008-02-16 20:45:54

Assignee: was

CC:  ncalexan

Here's a pure python implementation of an algorithm to factor polynomials over ZZ using kronecker's trick (specializing a variable to a large prime reduces you to a poly of fewer variables).  Note that this also fills in an implementation of factoring over ZZ[x,y] --- we don't have any implementation at all for this currently.  It's also faster than singular (over QQ) for some cases.

Here's an example with my favorite trouble-maker for singular.

this patch:

```
sage: R.<p10,g0,g1,g2,g3,g4,X1,X2>=ZZ[]
sage: t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1
sage: time t.factor()
CPU times: user 0.11 s, sys: 0.00 s, total: 0.12 s
Wall time: 0.12
(-1) * (p10^8*X2 - 1) * (p10^8*X1 - 1) * (p10^18*X1*X2 - 1) * (p10^32*X2^4 + p10^24*X2^3 + p10^16*X2^2 + p10^8*X2 + 1) * (p10^32*X1^4 + p10^24*X1^3 + p10^16*X1^2 + p10^8*X1 + 1) * (p10^72*X1^4*X2^4 + p10^54*X1^3*X2^3 + p10^36*X1^2*X2^2 + p10^18*X1*X2 + 1)
```


singular:

```
sage: R.<p10,g0,g1,g2,g3,g4,X1,X2>=QQ[]
sage: t=-p10^170*X1^10*X2^10+p10^130*X1^10*X2^5+p10^130*X1^5*X2^10-p10^90*X1^5*X2^5+p10^80*X1^5*X2^5-p10^40*X1^5-p10^40*X2^5+1
sage: time t.factor()
CPU times: <longer than I wanted to wait>
```




---

Attachment


---

Comment by jbmohler created at 2008-02-16 20:57:13

Changing assignee from was to malb.


---

Comment by jbmohler created at 2008-02-16 20:57:13

Changing component from algebraic geometry to commutative algebra.


---

Comment by ncalexan created at 2008-02-18 19:44:23

I am no expert on factoring algorithms, but this does seem to fill a needed hole, is reasonably implemented, and has some rudimentary doctests.

I say apply.

Isn't this whole area going to be addressed soon anyway, so that this code will likely be reviewed and enhanced shortly?


---

Comment by was created at 2008-02-19 14:51:53

REVIEW:

This absolutely should not be applied for the simple reason that the file `sage/rings/polynomial/multi_polynomial_factor.py`
introduces 7 new functions that have 0 docstrings and 0 doctests, and essentially 0 documentation.  My understanding, which I want to push very hard, is that no new code should go into Sage that reduces the overall doctest coverage score. 

Joel -- can you add doctests and docstrings for every single function `multi_polynomial_factor.py`?    I do that with *all* new code I write for Sage.


---

Comment by jbmohler created at 2008-02-25 17:26:19

I'm reviewing my own code today.  Expect a new patch to be submitted as of later today.  I just thought I'd mention that here in case someone was looking at this code today.


---

Comment by jbmohler created at 2008-02-27 02:18:12

I'm retracting this for the moment.  As expected, once I started looking at this code I found so many ways to improve it and totally got sucked in again and want to make it better.


---

Comment by malb created at 2008-03-28 11:44:52

Changing assignee from malb to jbmohler.


---

Comment by was created at 2008-04-01 05:12:53

Here is what Magma does, for the record:
   http://magma.maths.usyd.edu.au/magma/htmlhelp/text315.htm

And for GCD:
   http://magma.maths.usyd.edu.au/magma/htmlhelp/text314.htm#1994


---

Comment by craigcitro created at 2008-06-20 04:41:57

Changing keywords from "" to "editor_wstein".


---

Comment by burcin created at 2008-07-04 17:32:55

Joel says he has an improved patch with various additional tricks to filter easy factors. I will wait for an updated patch to review this.


---

Comment by malb created at 2009-01-22 23:08:15

Changing type from defect to enhancement.


---

Comment by mmezzarobba created at 2015-04-13 16:24:02

Related: #17840


---

Comment by jdemeyer created at 2015-05-24 09:48:41

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2015-06-19 08:38:11

Resolution: fixed
