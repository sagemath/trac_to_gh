# Issue 2953: gcc 4.3/Itanium: fix givaro 3.2.10.rc3 build

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-04-19 02:20:34

Assignee: mabshoff

On Itanium with gcc 4.3 we need to add climits to gmp++.h. The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0/alpha6/givaro-3.2.10.rc3.p1.spkg

fixes that.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-04-19 02:21:57

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-19 02:21:57

The difference between this and the previous spkg is the attached patched. The fix should also go into LinBox upstream.

Cheers,

Michael


---

Comment by was created at 2008-04-19 04:59:37

This works on a wide range of architectures where I tested it, and of course the change itself looks good. positive review.


---

Comment by mabshoff created at 2008-04-19 05:06:36

Merged in Sage 3.0.alpha6


---

Comment by mabshoff created at 2008-04-19 05:06:36

Resolution: fixed
