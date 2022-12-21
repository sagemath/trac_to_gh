# Issue 6407: Multiplication-by-n method on elliptic curve formal groups should use the double-and-add algorithm

Issue created by migration from Trac.

Original creator: hlaw

Original creation time: 2009-06-25 14:39:58

Assignee: hlaw

Keywords: formal group elliptic curve

Currently `EllipticCurveFormalGroup.mult_by_n()` is implemented simply by applying the group law to itself _n_ times (except when working over a field of characteristic zero, in which case a fast algorithm is used).  This linear algorithm should be replaced with the logarithmic double-and-add algorithm (i.e. the additive version of the standard square-and-multiply algorithm).


---

Comment by hlaw created at 2009-06-25 14:41:45

Changing status from new to assigned.


---

Attachment


---

Attachment


---

Comment by boothby created at 2009-07-17 23:25:30

hlaw's implementation of the double-and-add algorithm resulted in a wasted doubling at the end -- potentially expensive.  My part2 patch is a slight improvement.


---

Comment by rlm created at 2009-07-21 19:17:20

Looks good to me.


---

Comment by mvngu created at 2009-07-23 08:18:24

Resolution: fixed
