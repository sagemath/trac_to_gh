# Issue 9620: conflicting branch cut conventions

Issue created by migration from Trac.

Original creator: rbk

Original creation time: 2010-07-28 07:55:46

Assignee: AlexGhitza

CC:  jdemeyer

For multi-valued complex functions, the choice of principal values and where complex branch cuts are continuous is a matter of convention but there is a clear predominant convention which has been advocated by Kahan, can be found in Guy Steele's CLTL2 (chapter 12.5.3) and is implemented in most Lisp dialects, in the C99 standard, the upcoming C++0x standard, the CLN library, Mathematica, Maple, Sage's CDF, MPMath, and many others.

However, some libraries disagree with the predominant convention for branch cuts of inverse trigonometric and hyperbolic functions.

Unfortunately for Sage, Pari is one of the systems that disagree. This leads to surprising results that are difficult to explain to new users, like this fine example:

```
  sage: acosh(-1.0-0.00001*I) - acosh(CDF(-1,-0.0000001))
  -0.00347850806404590 + 6.27970680439127*I
```


It turns out that all of Pari's branch cuts of inverse trigonometric and hyperbolic functions are somehow affected.

Luckily we don't disagree about roots and the logarithm any more. :-)

* asin: The asin() function is not continuous as the cut is approached coming around the finite endpoint of the cuts in a counter clockwise direction.

* acos: Pari picks an unconventional principal branch in the left complex plain.

* atan: The atan() function is not continous as the cut is appraoched coming around the finite endpoint of the cut along the negative imaginary axis in a counter clockwise direction.

* asinh: The asinh() function is not continuous as the cut is approached coming around the finite endpoint of the cuts in a counter clockwise direction.

* acosh: Pari picks an unconventional principal branch in the lower complex plain.

* atanh: The atan() function is not continous as the cut is appraoched coming around the finite endpoint of the cut along the positive real axis in a counter clockwise direction.

Applying the attached patch to Pari 2.3.5 in Sage 4.5.1 makes the implementations in sage.libs.mpmath, sage.libs.pari, and sage.rings.complex_double return the same values within numerical accuracy.


---

Attachment


---

Comment by rbk created at 2010-07-28 19:53:40

Reported upstream as http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1084.


---

Comment by jdemeyer created at 2010-12-09 21:44:10

See #10430


---

Comment by jdemeyer created at 2010-12-10 22:07:42

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2010-12-15 10:26:55

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-12-15 10:26:55

Richard B. Kreckel wrote in an email:

So, back to the review:

I've checked that it works fine now. The results of pari(re+im*I).f() are compatible with f(CDF(re,im)) and mpmath.f(re+I*im) in the entire complex plain, where f is any of asin, acos, atan, asinh, acosh, and atanh.

thank you
   -richy.


---

Comment by jdemeyer created at 2010-12-24 17:36:02

Resolution: duplicate
