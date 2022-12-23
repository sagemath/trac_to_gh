# Issue 6133: [with patch, needs review] remove pbuild files in devel/sage

Issue created by migration from https://trac.sagemath.org/ticket/6133

Original creator: craigcitro

Original creation time: 2009-05-26 18:31:22

Assignee: craigcitro

CC:  mhansen

Three pbuild files still live in `devel/sage`, but are clearly out of date and need to be removed. The patch just removes all three.


---

Comment by craigcitro created at 2009-05-26 23:11:45

New patch -- cleans up `MANIFEST.in`, too.


---

Comment by was created at 2009-05-28 07:20:50

No hurry, so this should go in 4.0.1.  But I also read it, and it's a positive review.


---

Comment by mhansen created at 2009-05-28 07:47:40

I get these failures when applying:


```
applying trac-6133.patch
unable to find 'build.py' for patching
1 out of 1 hunks FAILED -- saving rejects to file build.py.rej
unable to find 'clib.py' for patching
1 out of 1 hunks FAILED -- saving rejects to file clib.py.rej
unable to find 'sagebuild.py' for patching
1 out of 1 hunks FAILED -- saving rejects to file sagebuild.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac-6133.patch

```



---

Attachment


---

Comment by craigcitro created at 2009-05-28 08:26:58

I was stupid -- the patch file had two copies of the same patch appended to one another. This works.


---

Comment by mhansen created at 2009-05-28 19:59:15

Resolution: fixed


---

Comment by mhansen created at 2009-05-28 19:59:15

The new patch works.

Merged in 4.0.rc2.
