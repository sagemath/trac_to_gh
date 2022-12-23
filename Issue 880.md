# Issue 880: 2.8.7-alpha0: many segfaults when running doctests on 32-bit x86 Linux

Issue created by migration from https://trac.sagemath.org/ticket/880

Original creator: cwitty

Original creation time: 2007-10-13 19:08:48

Assignee: failure

On my laptop, many of the doctests crash with SIGSEGV.
Here's one example:

```
sage -t  devel/sage-main/sage/categories/category_types.py  

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [1.0 s]
```


My laptop is 32-bit x86 Debian testing.  I think probably Jaap Spies is seeing the same thing on Fedora 7 (his report on the mailing list doesn't have enough detail to be positive).


---

Attachment


---

Comment by cwitty created at 2007-10-13 21:47:42

There was a copy-and-paste error that ended up reading uninitialized local variables, causing crashes on some machines.  Remove this incorrect, redundant code.


---

Comment by was created at 2007-10-14 22:55:12

Resolution: fixed
