# Issue 4224: small error in new question-mark interval printing

Issue created by migration from https://trac.sagemath.org/ticket/4224

Original creator: cwitty

Original creation time: 2008-09-30 19:09:41

Assignee: cwitty

CC:  jason

Some intervals were printing incorrectly in question-mark style (the printed result didn't always include the lower bound of the interval), as reported here: http://groups.google.com/group/sage-support/browse_thread/thread/844cde94499c42a1#

(Thanks to Pong for reporting the problem, and Jason Grout for bringing it to my attention!)

It turns out that this is a single-character fix: I had RNDN (round-to-nearest) where I needed RNDD (round-down).  Unfortunately, lots of doctests recorded incorrect printing, so the actual patch is almost entirely doctest fixes.

This patch against 3.1.2 passes -testall.  I hand-checked several (but not all) of the doctest changes against .str(style='brackets').


---

Attachment


---

Comment by mabshoff created at 2008-10-01 10:38:40

Carl, 

I observed the following failure on a Core2 Quad running Solaris:

```
sage -t  devel/sage/sage/rings/qqbar.py                     
**********************************************************************
File "/home/mabshoff/build-3.1.3.alpha0/sage-3.1.3.alpha0-fulvia/tmp/qqbar.py", line 3770:
    sage: cp.complex_roots(30, 1)
Expected:
    [1.189207115002721?,
     -1.189207115002721?,
     1.189207115002721?*I,
     -1.189207115002721?*I]
Got:
    [1.189207115002721?, -1.1892071150027211?, 1.189207115002721?*I, -1.189207115002721?*I]
**********************************************************************
```

Could this be related to this issue? I am reviewing the patch and will see what is going on on Solaris once I build 3.1.3 on it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-01 11:30:26

Patch is good and passes doctests. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-01 11:30:39

Resolution: fixed


---

Comment by mabshoff created at 2008-10-01 11:30:39

Merged in Sage 3.1.3.alpha3


---

Comment by jason created at 2008-10-01 16:40:09

I also looked at this patch, for the record, and it looked reasonable.  I did not have time to apply it and check it, though.
