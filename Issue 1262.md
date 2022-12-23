# Issue 1262: "make check" needs to depend on all

Issue created by migration from https://trac.sagemath.org/ticket/1262

Original creator: mabshoff

Original creation time: 2007-11-25 05:44:16

Assignee: was

If you run "make check" on a sage installation that hasn't been compiled all the doctests fail one by one. Make check depend on all to fix this.

Cheers,

Michaek


---

Comment by was created at 2007-11-25 05:56:27

OK, I fixed this by modifying SAGE_ROOT/makefile slightly.


---

Comment by was created at 2007-11-25 05:56:27

Resolution: fixed
