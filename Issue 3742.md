# Issue 3742: [with spkg, needs review] Fortran.spkg: Detect the location of gfortran properly

Issue created by migration from https://trac.sagemath.org/ticket/3742

Original creator: mabshoff

Original creation time: 2008-07-29 17:01:17

Assignee: mabshoff

For the cases when we do not provide a binary Fortran compiler we determine the location of libgfortran relative to the gfortran binary. But many installs link gfortran into $PATH somewhere, so we end up linking against a non-existent libgfortran.so. The updated spkg follows any potential gfortran link, so the issue is fixed. This has been observed on iras. The spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/final/fortran-20071120.p5.spkg

Cheers,

Michael



---

Comment by mabshoff created at 2008-07-29 17:01:28

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-29 17:04:18

Resolution: fixed


---

Comment by mabshoff created at 2008-07-29 17:04:18

Merged in Sage 3.0.6.final
