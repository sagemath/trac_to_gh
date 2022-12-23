# Issue 2595: rubiks and polymake both have a cube binary

Issue created by migration from https://trac.sagemath.org/ticket/2595

Original creator: mabshoff

Original creation time: 2008-03-19 12:44:32

Assignee: mabshoff

When one installs the optional polymake.spkg the cube doctest fails since somehow polymake's cube is in $PATH before rubik's cube:

```
./local/bin/cube
./local/polymake/bin/cube
```


I would suggest changing the name of the binary from rubiks.spkg.

Cheers,

Michael



---

Comment by mabshoff created at 2008-03-19 12:45:32

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-03-21 12:27:25

trivial patch to rename the binary in DikSolver


---

Attachment


---

Comment by gfurnish created at 2008-03-21 12:29:13

Looks good


---

Comment by mabshoff created at 2008-03-21 12:36:25

Resolution: fixed


---

Comment by mabshoff created at 2008-03-21 12:36:25

Merged in Sage 2.11.alpha1. The corresponding fix to the makefile of rubiks.spkg will be in #2287.
