# Issue 6259: [with patch, needs review] Fix spurious file creation in sage/server/support.py

Issue created by migration from https://trac.sagemath.org/ticket/6259

Original creator: craigcitro

Original creation time: 2009-06-11 09:40:40

Assignee: boothby

CC:  mhansen ncalexan

The file above generates a file in the current directory when running doctests on it; the attached patch just moves that to an appropriate temp directory. (That is, it switches the doctest, not the actual code.) 

I'm adding two people to the cc in the hopes that someone can give this a three-second glance.


---

Comment by ncalexan created at 2009-06-11 16:59:37

When using this on the server, are the temp files properly cleaned up?  But this addresses the problem for now.


---

Attachment


---

Comment by craigcitro created at 2009-06-12 07:55:15

Resolution: fixed


---

Comment by craigcitro created at 2009-06-18 10:25:01

Somehow this patch got dropped between `alpha0` and `rc3`. I've added it back in `rc3`.
