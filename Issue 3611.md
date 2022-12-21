# Issue 3611: sympow: make it use $CC instead of cc

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-07-08 17:42:57

Assignee: mabshoff

Make sympow default to $CC[=gcc] instead of cc since that can cause trouble by picking up another compiler

Cheers,

Michael



---

Comment by mabshoff created at 2008-07-08 17:43:03

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-29 15:16:56

An spkg which picks the default gcc from $PATH is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.6/final/sympow-1.018.1.p5.spkg

Cheers,

Michael


---

Comment by was created at 2008-07-29 15:24:51

Looks safe enough.


---

Comment by mabshoff created at 2008-07-29 15:33:11

Resolution: fixed


---

Comment by mabshoff created at 2008-07-29 15:33:11

Merged in Sage 3.0.6.final
