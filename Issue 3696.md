# Issue 3696: [with spkg, needs review] Fix gmp.spkg build issue on Solaris

Issue created by migration from https://trac.sagemath.org/ticket/3696

Original creator: mabshoff

Original creation time: 2008-07-21 19:07:54

Assignee: mabshoff

Due to bashisms on Solaris gmp fails to build. This is fixed by using "/usr/bin/env bash" instead of "/bin/sh" in spkg/install. That is the only change to 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/alpha1/gmp-4.2.2.p1.fake.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-21 19:14:40

Merged in Sage 3.0.6.rc0


---

Comment by mabshoff created at 2008-07-21 19:14:40

Resolution: fixed
