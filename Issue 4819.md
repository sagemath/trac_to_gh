# Issue 4819: [with spkg, needs review] update Cython to 0.10.3

Issue created by migration from https://trac.sagemath.org/ticket/4819

Original creator: robertwb

Original creation time: 2008-12-17 09:52:47

Assignee: mabshoff

This is a followup to #4798. As #4639 didn't involve any more changes to Cython, I'm now officially releasing 0.10.3. One other fix involving buffers made it into this release, which shouldn't affect us yet but I did a sage -ba and it built and runs fine (didn't do another testall). 

Package up in the usual place: http://sage.math.washington.edu/home/robertwb/cython/


---

Comment by mabshoff created at 2008-12-17 10:02:51

Yep, looks good to me. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-17 10:51:50

Resolution: fixed


---

Comment by mabshoff created at 2008-12-17 10:51:50

Merged in Sage 3.2.2.rc1
