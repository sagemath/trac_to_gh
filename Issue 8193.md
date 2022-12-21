# Issue 8193: Enumeration of points on plane curves over finite fields is very inefficient

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2010-02-05 12:29:54

Assignee: AlexGhitza

The title says all!  The code in sage/schemes/plane_curves/projective_curve.py for finding all points on a plane curve over a finite field just enumerates all point in `P^2` and tests every one, which is less than optimal.

A patch to improve this is on its way.



---

Comment by cremona created at 2010-02-05 14:17:28

Changing status from new to needs_review.


---

Comment by cremona created at 2010-02-05 14:17:28

The patch does the enumeration in a more efficient way.


---

Attachment

applies to 4.3.2


---

Comment by cremona created at 2010-02-07 15:40:06

In view of #8197 I have deleted "check=False" twice.  Otherwise unchanged.


---

Comment by roed created at 2010-02-09 22:47:24

I'm testing now...


---

Comment by roed created at 2010-02-11 08:49:30

Looks good, passes all doctests.


---

Comment by roed created at 2010-02-11 08:49:30

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:05:18

Resolution: fixed


---

Comment by cturner created at 2010-03-03 10:51:52

A bug has been found in this patch - a new ticket #8428 has been opened and a patch to fix this is in progress.
