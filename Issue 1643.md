# Issue 1643: Fortran.spkg: If SAGE_FORTRAN is set do not copy the binary to sage_fortran.bin

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-30 18:56:17

Assignee: mabshoff

We shouldn't copy the binary named in `SAGE_FORTRAN` to `sage_fortran.bin` since it seems to break gfortran. Some times it seems to assume the position of libgfortran.so to be relative to the invoking executable and then breaks things will break. Just make the script `sage_fortran` call

```/bin/bash
value of SAGE_FORTRAN $*
```

That way a bdist is also less likely to break if the version of the fortran compiler is slightly different. It will also result in a slightly smaller Sage install, which is also a good thing.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 10:24:08

Changing status from new to assigned.


---

Comment by jkantor created at 2008-01-04 09:16:58

Hopefully this fixes that problem. In case that SAGE_FORTRAN is a valid path
the sage_fortran wrapper directly calls that as opposed to calling sage_fortran.bin which is symlinked to sage_fortran. 

(note I didn't change the case where g95 doesn't work but we find something without the users specifying a valid SAGE_FORTRAN, maybe I should change that too)

Also, i tested that which produces a correctly function sage_fortran, but didn't build anything with it yet so that should be done.

http://sage.math.washington.edu/home/jkantor/spkgs/fortran-20071120.p2.spkg


---

Comment by mabshoff created at 2008-01-04 10:44:12

Merged in 2.9.2.rc0


---

Comment by mabshoff created at 2008-01-04 10:44:12

Resolution: fixed
