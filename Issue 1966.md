# Issue 1966: [with spkgs,patch ] inline_fortran broke on OSX

Issue created by migration from Trac.

Original creator: jkantor

Original creation time: 2008-01-29 07:09:15

Assignee: mabshoff

Probably around the upgrade to 1.0.4 the inline_fortran command broke on osx.

The following spkg fixes it

http://sage.math.washington.edu/home/jkantor/spkgs/numpy-20080104-1.0.4.p2.spkg

also I changed the inline_fortran.py file so the inline_fortran doctests is no longer optional (it was optional when fortran wasn't required, but now it is, so there is no reason for it to be optional).

http://sage.math.washington.edu/home/jkantor/spkgs/inline_fortran.patch



---

Comment by mabshoff created at 2008-01-30 08:30:25

Builds and testall passes with scipy* rebuild on Linux and OSX. `testall` passes.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-30 08:31:25

Resolution: fixed


---

Comment by mabshoff created at 2008-01-30 08:31:25

Merged in Sage 2.10.1.rc3
