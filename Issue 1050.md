# Issue 1050: update optional valgrind+omega spkg to r7070 (or later)

Issue created by migration from https://trac.sagemath.org/ticket/1050

Original creator: mabshoff

Original creation time: 2007-11-01 04:48:39

Assignee: was

From the r7069/r7070 commit log message:

```
Merged the MASSIF2 branch to the trunk.  Main changes:

- ms_main.c: completely overhauled.

- massif/tests/*:  lots of them now.

- massif/perf/:  added.

- massif/hp2ps:  removed.  No longer used.

- vg_regtest: renamed the previously unused "posttest" notion to "post".
  Using it for checking ms_print's output.

Although the code has changed dramatically, as has the form of the tool's
output, the information presented in the output is basically the same,
although it's now (hopefully) much more useful.  So the tool name is
unchanged.
```

I should also add a spkg-check script to run the test suite, we are after all running code from the development branch.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-01 04:49:31

Changing component from algebraic geometry to packages.


---

Comment by mabshoff created at 2007-11-01 04:49:31

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2007-11-01 04:49:37

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-11-01 04:49:37

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-25 20:33:51

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha2/valgrind_3.3.0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-25 20:39:38

Resolution: fixed


---

Comment by mabshoff created at 2008-01-25 20:39:38

Merged in the optional spkg repo and mirrored out.
