# Issue 1507: [with patch] plotting -- document how to use pylab / matlab style plotting from sage

Issue created by migration from https://trac.sagemath.org/ticket/1507

Original creator: was

Original creation time: 2007-12-14 17:53:05

Assignee: was




---

Comment by was created at 2007-12-14 17:53:50

this is *only* a documentation addition -- no code, so should be easy to referee.


---

Attachment


---

Comment by was created at 2007-12-14 17:59:38

If the second hunk fails, no problem.  That's not relevant.  Only the first big
hunk is.


---

Comment by cwitty created at 2007-12-15 06:36:58

Looks good to me.  

To apply: Attempt to apply the patch as usual.  Ignore the error message:

```
Hunk #2 FAILED at 127
1 out of 2 hunks FAILED -- saving rejects to file sage/plot/plot.py.rej
abort: patch failed to apply
```


Then do `hg_sage.ci()`, to check in the half-applied patch.


---

Comment by mabshoff created at 2007-12-15 06:47:58

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 06:47:58

Merged in 2.9.rc0.
