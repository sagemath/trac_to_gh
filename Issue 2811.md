# Issue 2811: make check is broken due to #2746

Issue created by migration from https://trac.sagemath.org/ticket/2811

Original creator: mabshoff

Original creation time: 2008-04-05 18:10:14

Assignee: mabshoff


```
SAGE build/upgrade complete!
. local/bin/sage-env && sage-maketest
/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 3: [: argument expected
mkdir: `': No such file or directory
/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 11: /test.log: Permission denied
/scratch/mabshoff/release-cycle/sage-3.0.alpha2/local/bin/sage-maketest: line 12: /test.log: Permission denied
tee: /test.log: Permission denied
Testing of examples currently not implemented.
Testing SAGE documentation
Testing SAGE tutorial
tee: /test.log: Permission denied
sage -t  devel/doc/tut/tut.tex                              Testing SAGE programming guide
tee: /test.log: Permission denied
sage -t  devel/doc/prog/prog.tex
```



---

Attachment


---

Comment by mabshoff created at 2008-04-07 01:27:56

This patch needs some additional fixes to the main makefile which are not up here since the file isn't under revision control.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-07 01:28:03

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-04-07 01:30:19

Good


---

Comment by mabshoff created at 2008-04-07 01:33:28

Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-07 01:33:28

Resolution: fixed
