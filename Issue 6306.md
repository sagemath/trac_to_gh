# Issue 6306: [with patch, needs review] fix some reference manual issues for 4.0.2

Issue created by migration from https://trac.sagemath.org/ticket/6306

Original creator: jhpalmieri

Original creation time: 2009-06-16 02:06:05

Assignee: jhpalmieri

The attached patch should fix several of the reference manual warnings for 4.0.2.  There is still one outstanding -- sage/misc/misc.py -- but I can't figure that one out.



---

Attachment


---

Comment by mvngu created at 2009-06-16 23:15:48

Looks good. Applied OK against Sage 4.0.2.rc2. Although with the patch at #6297, I still see about 5 warnings when building the reference manual.


---

Comment by craigcitro created at 2009-06-18 00:07:40

Resolution: fixed
