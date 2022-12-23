# Issue 4520: segfault in cyclotomic matrices

Issue created by migration from https://trac.sagemath.org/ticket/4520

Original creator: robertwb

Original creation time: 2008-11-14 06:52:59

Assignee: was

CC:  craigcitro


```
sage: M = matrix(CyclotomicField(5), 5, 2, 5)


------------------------------------------------------------
Unhandled SIGBUS: A bus error occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```



---

Comment by robertwb created at 2008-11-14 06:58:57

It was a missing check.


---

Comment by craigcitro created at 2008-11-14 07:09:08

If you add a doctest, I'll give this a positive review.


---

Attachment


---

Comment by robertwb created at 2008-11-14 07:19:52

Of course :) I've uploaded a new patch.


---

Comment by craigcitro created at 2008-11-14 07:21:10

Looks good.


---

Comment by mabshoff created at 2008-11-14 17:19:13

Merged in Sage 3.2.rc1


---

Comment by mabshoff created at 2008-11-14 17:19:13

Resolution: fixed
