# Issue 7244: Implement dicyclic groups as permutation groups

Issue created by migration from https://trac.sagemath.org/ticket/7244

Original creator: rbeezer

Original creation time: 2009-10-19 04:48:24

Assignee: joyner

CC:  wdj

Keywords: dicyclic

The dicyclic groups are nonabelian groups of order 4n, n> 2.

With these added, it will be possible to easily construct every subgroup of order 8 and 12 as a permutation group, and then every subgroup of size 15 or less will be easy to construct.

Discussion originated at:

http://groups.google.com/group/sage-devel/browse_thread/thread/df6697653527006c


---

Comment by rbeezer created at 2009-10-19 05:06:52

Changing status from new to needs_review.


---

Comment by rbeezer created at 2009-10-19 05:06:52

Dicyclic groups are implemented as a new class in the named permutation groups collection.

The "quaternion group" is implemented by simply forming the dicyclic group of order 8.  The intent is that this small group is a good one for students to contrast with the other four groups of this order.


---

Comment by kcrisman created at 2009-10-21 16:06:20

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2009-10-21 16:06:20

There's a typo in line 495, and these groups are sufficiently unusual that some reference to online documentation of them would be useful.   I realize these are fairly trivial comments, my apologies.


---

Attachment


---

Comment by rbeezer created at 2009-10-22 02:38:01

Karl-Dieter,

Thanks for the comments.  I've replaced the patch with a new one addressing your comments.

If you test building the docs will you see if you get the warning


```
/doc/en/reference/sage/groups/perm_gps/permgroup_named.rst:: document isn't included in any toctree
```


This file really needs a workover, and probably shouldn't be in the docs as-is, but I'm not sure if the warning was there before, or if I've induced it.

Thanks,
Rob


---

Comment by rbeezer created at 2009-10-22 02:38:01

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2009-10-25 00:44:53

passes sage -testall (on ubuntu 9.04 32 but running under vmware under mac 10.6) and does what it claims.

Thanks Rob!


---

Comment by wdj created at 2009-10-25 00:44:53

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2009-10-26 04:20:50

Release manager:  please obsolete #7151 when this gets merged.  Thanks!


---

Comment by mhansen created at 2009-10-31 16:37:53

Resolution: fixed
