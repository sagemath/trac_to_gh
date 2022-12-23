# Issue 257: restart needed after segfault

Issue created by migration from https://trac.sagemath.org/ticket/257

Original creator: boothby

Original creation time: 2007-02-10 06:33:51

Assignee: boothby

Following a null pointer gives the user an oh-so-friendly message.  Then (s)he has to use the mouse to restart the notebook manually.

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


---

Comment by boothby created at 2007-03-22 20:01:56

Resolution: fixed
