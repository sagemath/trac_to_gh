# Issue 2121: move libecm wrapper from interfaces to libs

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-02-09 01:32:52

Assignee: was

...yeah...


---

Comment by rlm created at 2008-05-23 00:59:07

Patch is here:

http://sage.math.washington.edu/home/rlmill/trac-2121-libecm.patch

Passes all tests except for known issues in sage-3.0.2.rc0.


---

Attachment

this is rlm's patch, but properly attached ;)


---

Comment by mabshoff created at 2008-05-23 01:12:08

Patch looks good to me. It just moves the file and updates setup.py properly. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-23 01:13:01

Resolution: fixed


---

Comment by mabshoff created at 2008-05-23 01:13:01

Merged in Sage 3.0.2.rc0
