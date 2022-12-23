# Issue 3193: fix 64 bit OSX build support for twisted

Issue created by migration from https://trac.sagemath.org/ticket/3193

Original creator: mabshoff

Original creation time: 2008-05-13 14:51:37

Assignee: mabshoff

This is slightly trickier - see ToDo in http://wiki.sagemath.org/osx64 - but spkg is coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-13 14:51:43

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-05-28 10:02:28

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/twisted-8.0.1.p0.spkg

provides 64 bit OSX build support. Build tested on Linux and 32 & 64 bit OSX. It is required to merge the updated python.spkg from #3318 for 64 bit OSX for this spkg to work.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-28 13:19:19

Resolution: fixed


---

Comment by mabshoff created at 2008-05-28 13:19:19

Merged in Sage 3.0.3.alpha0
