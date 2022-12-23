# Issue 5340: NTL "context"s can be restored at the wrong time, leading to randomly-wrong answers

Issue created by migration from https://trac.sagemath.org/ticket/5340

Original creator: cwitty

Original creation time: 2009-02-22 20:03:58

Assignee: cwitty

I should have a fix for this very soon.


---

Comment by cwitty created at 2009-02-22 20:04:22

Changing status from new to assigned.


---

Comment by cwitty created at 2009-02-22 20:46:56

The problem is that `__dealloc__` can happen at "random" times (whenever the garbage collector happens to trigger), so it must not have global side-effects.

To the reviewer: Note that the NTL documentation explicitly says you don't need to have the correct context when you destroy an object:

```
Note, however, that if a GF2E object is created under one modulus 
and then used in any way (except destroyed) under another, 
program behavior is not predictable.
```

Essentially identical language occurs in the documentation for lzz_pE, lzz_p, ZZ_pE, and ZZ_p.

I fixed 9 potential instances of the problem, but only added a doctest for one of them; you'll understand why when you see how hard it is to doctest.

All doctests pass.

This is based on sage-3.3 + ReST patches, but I think it would probably apply without the ReST patches just fine.


---

Attachment


---

Comment by mabshoff created at 2009-02-24 20:30:04

Positive review. I did valgrind all of the Sage 3.3 doctests + this patch (while testing gsw's libSingular work) and no issue popped up. It also passes doctests on top of the ReST patches.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-24 20:30:23

Resolution: fixed


---

Comment by mabshoff created at 2009-02-24 20:30:23

Merged in Sage 3.4.alpha0.

Cheers,

Michael
