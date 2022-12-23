# Issue 5164: NTL.spkg: Set SHAREDFALGS to -fnocommon on Darwin

Issue created by migration from https://trac.sagemath.org/ticket/5164

Original creator: mabshoff

Original creation time: 2009-02-03 05:00:34

Assignee: mabshoff

In #5161 I removed some global SHAREDFLAGS setting from sage-env. NTL on Darwin needs -fnocommon to work around some linker stupidity.

spkg coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 05:00:40

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-03 18:04:53

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha5/ntl-5.4.2.p6.spkg

fixes the problem.

Cheers,

Michael


---

Comment by jsp created at 2009-02-03 19:51:09

No issues with building on other OSes Fedora 9, Fedora 10 and Ubuntu 8.10, 32 bits

Jaap


---

Comment by mabshoff created at 2009-02-03 19:55:03

Merged in Sage 3.3.alpha5.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-03 19:55:03

Resolution: fixed
