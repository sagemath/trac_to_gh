# Issue 2929: [with spkg, needs review] gcc 4.3: fix gmp.spkg

Issue created by migration from https://trac.sagemath.org/ticket/2929

Original creator: mabshoff

Original creation time: 2008-04-15 05:52:53

Assignee: mabshoff

The gmp.spkg fails to build on gcc 4.3 [at least we cannot link properly against it] due to some changes to the inline handling as well as missing std::FILE issues. The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha5/gmp-4.2.1.p14.spkg

fixes that by slightly patching gmp-h.in.

To test build gmp, then FLINT for example since gmp by itself builds fine ;) - imagine my excitement debugging the problem. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-15 05:53:01

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-04-15 05:56:22

works for me.


---

Comment by mabshoff created at 2008-04-15 06:08:19

Resolution: fixed


---

Comment by mabshoff created at 2008-04-15 06:08:19

Merged in Sage 3.0.alpha5
