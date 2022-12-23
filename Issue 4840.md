# Issue 4840: FLINT: call the stack cleanup function at exit

Issue created by migration from https://trac.sagemath.org/ticket/4840

Original creator: mabshoff

Original creation time: 2008-12-20 22:11:53

Assignee: was

CC:  burcin

FLINT uses its own memory pool. In order to clean up Sage's valgrind log call  flint_stack_cleanup() right before unloading FLINT.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-20 22:12:07

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-20 22:12:07

Changing component from linear algebra to memleak.


---

Comment by mabshoff created at 2008-12-20 22:12:07

Changing assignee from was to mabshoff.


---

Comment by burcin created at 2009-01-23 08:10:43

Changing status from assigned to new.


---

Comment by burcin created at 2009-01-23 08:10:43

attachment:trac_4840-flint_free.patch should fix this.


---

Comment by burcin created at 2009-01-23 08:10:43

Changing assignee from mabshoff to burcin.


---

Comment by mhansen created at 2009-01-24 02:39:18

Looks good to me.


---

Comment by mabshoff created at 2009-01-24 14:09:05

This patch does not apply to my tree? I am also curious why this is a git style patch considering that the history is messed up anyway with git style patches:

```
mabshoff@geom:/scratch/mabshoff/sage-3.3.alpha2/devel/sage$ hg import trac_4840-flint_free.patch 
applying trac_4840-flint_free.patch
unable to find 'sage/libs/flint/flint.pxi' for patching
1 out of 1 hunks FAILED -- saving rejects to file sage/libs/flint/flint.pxi.rej
sage/libs/flint/flint.pxi: No such file or directory
abort: patch failed to apply
```

What is going on here? Does this depend on something else?

Cheers,

Michael


---

Attachment

New patch fixes merge failure.


---

Comment by mabshoff created at 2009-01-24 17:45:49

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 17:45:49

Merged in Sage 3.3.alpha2
