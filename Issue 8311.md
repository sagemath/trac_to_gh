# Issue 8311: elliptic curve random point hangs when group is trivial

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2010-02-20 12:06:17

Assignee: cremona

CC:  schilly

Keywords: random point

As reported:

```
E = EllipticCurve(GF(3), [0,0,0,2,2])
E.random_element()
```

Hangs since

```
sage: E.rational_points()
[(0 : 1 : 0)]
```

so unless the point at infinity is picked (probability 1/(q+1)=1/4) no point will be found.

This can only happen for q=2,3,4 (try Hasse_bounds(q)) so these cases need separate treatment.

Patch coming up.



---

Attachment

applies to 4.3.3.alpha1


---

Comment by cremona created at 2010-02-20 13:49:21

Patch attached.  I needed to make a few side adjustments to avoid infinite recursions, since enumerating points is sometimes done via first finding the group generators, which in turn uses random points....


---

Comment by cremona created at 2010-02-20 13:49:21

Changing status from new to needs_review.


---

Comment by schilly created at 2010-02-20 13:58:29

thx, tried the patch, works. i'll seek for some feedback from the original reporter.


---

Comment by wuthrich created at 2010-03-05 18:25:40

Replaces the previous patch


---

Attachment

I changed a few tabulators to spaces. Other than that the patch is fine. And I started testing now.


---

Comment by cremona created at 2010-03-08 21:15:06

Replying to [comment:4 wuthrich]:
> I changed a few tabulators to spaces. Other than that the patch is fine. And I started testing now.
Thanks, sorry about the tabs.


---

Comment by wuthrich created at 2010-03-09 19:59:42

Changing status from needs_review to positive_review.


---

Comment by wuthrich created at 2010-03-09 19:59:42

Sorry about the delay. I still do not know why I can use the trac only from home and not from my office. 

The tests passed (except the once that are reported and present in the current .alpha)


---

Comment by mvngu created at 2010-03-11 04:45:47

Merged [trac_8311_random_point_2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8311/trac_8311_random_point_2.patch).


---

Comment by mvngu created at 2010-03-11 04:45:47

Resolution: fixed


---

Comment by jdemeyer created at 2014-09-09 15:07:19

Much better fix at #16951.
