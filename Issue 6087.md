# Issue 6087: graph automorphism group segfaults on invalid input

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-05-19 21:38:06

Assignee: rlm

CC:  rlm mjo

Even though the input is invalid (the partition isn't a valid partition), I think segfaulting is considered a bug:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: g=graphs.CubeGraph(3)
sage: 
sage: g.relabel()
sage: g.automorphism_group(partition=[[0,1,2],[3,4,5]])
| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```




---

Attachment

Patch adding a doctest for the correct behavior


---

Comment by mjo created at 2011-12-15 15:10:51

Changing status from new to needs_review.


---

Comment by mjo created at 2011-12-15 15:10:51

This is fixed now, so I've added a doctest for it.


---

Comment by jason created at 2011-12-16 16:26:43

Looks great; passes tests on the file.  Thanks!


---

Comment by jason created at 2011-12-16 16:26:43

Changing status from needs_review to positive_review.


---

Comment by jason created at 2011-12-16 16:27:43

Can you add your name to the Author field?


---

Comment by jdemeyer created at 2011-12-17 09:12:29

Resolution: fixed
