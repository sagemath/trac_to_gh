# Issue 6667: bug in newton_polygon() for p-adic polynomials

Issue created by migration from https://trac.sagemath.org/ticket/6667

Original creator: AlexGhitza

Original creation time: 2009-08-03 08:00:58

Assignee: roed

Keywords: newton polygon

This is as simple as I can make it at the moment:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: K = Qp(2, prec=5)
sage: P.<x> = K[]
sage: f = P(x^4 + 2^3*x^3 + 2^13*x^2 + 2^21*x + 2^37)
sage: f.newton_polygon()
[(0, 37), (1, 21), (2, 13), (3, 3), (4, 0)]
```

| Sage Version 4.1.1.rc0, Release Date: 2009-07-29                   |
| Type notebook() for the GUI, and license() for information.        |
This is wrong, as it's not convex (the point (2,13) should not be there).  Indeed, note that the sequence of Newton slopes is not non-increasing:


```
sage: f.newton_slopes()
[16, 8, 10, 3]
```


This should be [16, 9, 9, 3].


---

Comment by roed created at 2009-08-04 01:56:40

I'm probably not going to be able to take a look at this until August 20 or so.  If someone else wants to fix it, feel free.  :-)


---

Comment by roed created at 2009-11-27 04:36:50

This is fixed in the new p-adic polynomial code, which is in progress.


---

Comment by chapoton created at 2013-08-23 09:24:00

Still there in 5.12.beta2


---

Attachment

here is a quick patch that should fix the problem

I have not been careful concerning the precision of the coefficients

Needs review !


---

Comment by chapoton created at 2013-08-23 10:16:54

Changing status from new to needs_review.


---

Comment by chapoton created at 2013-08-25 07:20:32

bot is happy, is there somebody out there for a review ?


---

Comment by caruso created at 2013-08-27 08:13:03

Here is a patch taking in account precision issues (see discussion in ticket #14828).

-----

For the bot: apply only [attachment:trac_6667_caruso.patch]


---

Comment by chapoton created at 2013-08-27 08:22:29

your patch does not apply on a clean 5.12.beta3


---

Attachment

Sorry. I was working with an older version of Sage. It should be fixed now.


---

Attachment

here is a review patch, with only minor changes to your code

in my opinion, it would be good to add examples for the two other raise statements.


---

Comment by caruso created at 2013-08-27 20:26:21

Replying to [comment:10 chapoton]:
> here is a review patch, with only minor changes to your code

Thanks!

> in my opinion, it would be good to add examples for the two other raise statements.

Actually, I believe that they can't occur but it seemed to be really safer to check them anyway. (I added a comment in the code to mention that.)

I also corrected another bug: the valuation of the coefficients are not the values in the list `self._valadded` but these values augmented by `self._valbase` (as far as I understand David's code). As a consequence, the computation was wrong when the gcd of all coefficients was not 1. I added a doctest to check this issue.

Apply only [attachment:trac_6667_caruso_revised.patch] (it includes your review).


---

Attachment


---

Comment by chapoton created at 2013-08-29 07:43:34

apply only trac_6667_caruso_revised.patch


---

Comment by chapoton created at 2013-08-29 07:45:53

apply only trac_6667_caruso_revised.patch


---

Comment by chapoton created at 2013-09-15 11:22:59

ok, good to me. Positive review


---

Comment by chapoton created at 2013-09-15 11:22:59

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-10-01 07:17:35

Resolution: fixed
