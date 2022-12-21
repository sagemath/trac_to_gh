# Issue 1742: [with spkg] Build ntl with debug info

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-01-10 06:22:40

Assignee: mabshoff

NTL is currently build without debug symbols. This makes debugging or valgrinding harder and forces me to rebuild NTL manually. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/ntl-5.4.1.p10.spkg

adds debug flags to the appropriate CFLAGS and CXXFLAGS.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-10 06:28:11

Resolution: fixed


---

Comment by mabshoff created at 2008-01-10 06:28:11

Merged in Sage 2.10.alpha1.
