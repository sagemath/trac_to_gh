# Issue 3196: fix 64 bit OSX build support for R

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-13 15:40:32

Assignee: mabshoff

spkg coming up. One issue is that OSX 10.5 does not have a 64 bit libiconv, so that support is disabled.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-13 16:54:58

Changing status from new to assigned.


---

Attachment

The updated spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.3/alpha0/r-2.6.1.p16.spkg

Compile tested on Linux, 32 and 64 bit OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-28 13:19:29

Merged in Sage 3.0.3.alpha0


---

Comment by mabshoff created at 2008-05-28 13:19:29

Resolution: fixed
