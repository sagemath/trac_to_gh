# Issue 9684: Make use of _tidy_model() optional

Issue created by migration from Trac.

Original creator: arminstraub

Original creation time: 2010-08-04 05:14:25

Assignee: cremona

CC:  cturner beankao

Keywords: local_data

Currently, local_data() after running Tate's algorithm always also calls _tidy_model().  The attached patch makes this behaviour optional by introducing a parameter tidy.  This functionality is needed for the implementation of ticket #9320.


```
sage: E = EllipticCurve([2, 1, 0, -2, -1])
sage: E.local_data(ZZ.ideal(2), algorithm="generic").minimal_model()
Elliptic Curve defined by y^2 = x^3 - x^2 - 3*x + 2 over Rational Field
sage: E.local_data(ZZ.ideal(2), algorithm="generic").minimal_model(tidy=False)
Elliptic Curve defined by y^2 + 2*x*y + 2*y = x^3 + x^2 - 4*x - 2 over Rational Field
```


Since Pari also does this "tidying", the patch needs to add the parameter algorithm to various functions.


---

Attachment


---

Comment by arminstraub created at 2010-08-04 05:19:14

Changing status from new to needs_review.


---

Comment by cremona created at 2010-08-11 19:49:56

I will review this.  I'm afraid that I coined the phrase "tidy model", which I now regret.  It would be better, and consistent with other usage, to call this operation *reducing* the model.  Minimization and reduction are different things and so should be implemented independently.


---

Attachment

Apply after previous


---

Comment by cremona created at 2010-08-12 20:09:12

The first patch is fine, applies to 4.5.3.alpha0 and tests pass.

I added a second patch which **only** changes "tidy" to "reduce" as appropriate, which I think is better terminology.  If the original poster is happy with that, please mark the ticket "positive review".  If not, I'll still give the first patch a positive review.

For the future, there is an addition reduction step not yet implemented but useful (only non-trivial over number fields):  scale by [u,0,0,0] where u is a unit chosen so that the discriminant is in a sense minimal (minimal height modulo 12th powers of units).  But that is for another day.


---

Comment by arminstraub created at 2010-08-13 00:29:54

Changing status from needs_review to positive_review.


---

Comment by arminstraub created at 2010-08-13 00:29:54

Thank you for the review!

Yes, I'm happy with this renaming.  Even though we did enjoy your earlier terminology at the Sage Days ;)


---

Comment by cremona created at 2010-08-13 08:38:10

Thanks.

Release manager:  please apply both patches.


---

Comment by mpatel created at 2010-09-15 11:38:05

Resolution: fixed
