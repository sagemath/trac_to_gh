# Issue 3186: fix 64 bit OSX build support for numpy

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-13 13:48:57

Assignee: mabshoff

We need to create a fake gcc injecting "-m64" in the argument list since otherwise the conftest will fail.

Spkg is coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-13 13:49:04

Changing status from new to assigned.


---

Attachment


---

Attachment


---

Attachment

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha1/numpy-20080104-1.0.4.p4.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-19 04:01:34

Merged in Sage 3.0.2.alpha1


---

Comment by mabshoff created at 2008-05-19 04:01:34

Resolution: fixed
