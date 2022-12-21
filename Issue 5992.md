# Issue 5992: [with spkg, needs review] Set stack size in Maxima.spkg to 32kb for clisp

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-05-06 05:26:28

Assignee: mabshoff

clisp needs a stack larger than many systems provide, i.e. 8kb. If the stacksize isn't raised Maxima can randomly fail to build.

The spkg at 

  http://sage.math.washington.edu/home/mabshoff/release-cycles-3.4.2/post-final/maxima-5.16.3.p2.spkg

fixes that issue.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-06 05:26:37

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-05-06 06:27:23

Resolution: fixed


---

Comment by mabshoff created at 2009-05-06 06:27:23

Merged in Sage 3.4.2.

Cheers,

Michael
