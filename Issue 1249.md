# Issue 1249: [with patch] fixes bug in graph plotting with partitions

Issue created by migration from https://trac.sagemath.org/ticket/1249

Original creator: rlm

Original creation time: 2007-11-23 18:56:47

Assignee: mhansen

Keywords: graphs




---

Attachment

Looks good to me: the example in the doctests fails before the patch and succeeds after the patch.  There is one caveat: I think the call to D.show() in the first doctest chunk was supposed to be D.plot().

But IMHO good enough to apply, anyway.


---

Comment by mabshoff created at 2007-12-01 19:30:13

`<mhansen-962> mabshoff: I think http://trac.sagemath.org/sage_trac/ticket/1249 is okay.`


---

Comment by mabshoff created at 2007-12-01 19:53:02

Merged in 2.8.15.alpha1.


---

Comment by mabshoff created at 2007-12-01 19:53:02

Resolution: fixed
