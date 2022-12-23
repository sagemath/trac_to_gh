# Issue 1741: [with spkg] Build zlib with debug info

Issue created by migration from https://trac.sagemath.org/ticket/1741

Original creator: mabshoff

Original creation time: 2008-01-10 05:54:59

Assignee: mabshoff

I have been looking for various problems in zlib that valgrind exposed. Since we do not build with debug info I need to rebuild zlib manually, so fix this in the spkg. An updated spkg with this trivial fix is at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10/alpha1/zlib-1.2.3.p3.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-10 06:28:06

Merged in Sage 2.10.alpha1.


---

Comment by mabshoff created at 2008-01-10 06:28:06

Resolution: fixed
