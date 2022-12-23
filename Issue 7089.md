# Issue 7089: refactor SAGE_ROOT/makefile

Issue created by migration from https://trac.sagemath.org/ticket/7089

Original creator: ddrake

Original creation time: 2009-10-01 03:39:26

Assignee: tbd

I've been editing the root makefile while working on a couple tickets, and I have a deep urge to refactor repetitive, boilerplate code. In SAGE_ROOT/makefile, there are many sequences of commands that are repeated in multiple targets.

The attached patch puts the repetitive bits into variables that can easily be customized later by editing only one thing in the makefile, instead of multiple things.

I'd also like to consider removing the "install" and "gmp" targets in the makefile. I suspect no one ever uses them.


---

Comment by ddrake created at 2009-10-01 03:39:46

unified diff for SAGE_ROOT/makefile


---

Comment by ddrake created at 2009-10-01 03:41:52

Changing status from new to assigned.


---

Comment by ddrake created at 2009-10-01 03:41:52

Changing keywords from "" to "makefile".


---

Attachment


---

Comment by ddrake created at 2009-10-01 03:41:52

Changing assignee from tbd to ddrake.


---

Comment by timdumol created at 2009-10-01 04:48:24

Patch applies, and the tests run properly. Positive review.


---

Comment by mhansen created at 2009-10-16 09:02:23

Resolution: fixed
