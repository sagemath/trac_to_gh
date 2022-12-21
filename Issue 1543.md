# Issue 1543: rpy build fails if "tail -1" doesn't work

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2007-12-17 02:56:50

Assignee: craigcitro

Again, the title says it all -- on some systems (like mine), tail -1 produces an error (since this is supposedly "deprecated" behavior), recommending that the user use tail -n 1 instead. rpy fails after that; fixing this, everything works fine. I've added one more file to the patches/ directory, and one more line to the spkg-install (namely, copying that file over). 


---

Attachment


---

Comment by craigcitro created at 2007-12-17 02:58:35

Changing status from new to assigned.


---

Attachment

As mabshoff pointed out, this spkg name should probably get updated, since changes were made, and so I've added rpy-1.0.1.p0.spkg ... I'm also putting up a new patch for 1542, which will know about this new filename. (It has to appear in the r spkg-install, so these two should be handled simultaneously.)


---

Comment by rlm created at 2007-12-18 02:04:50

Resolution: fixed


---

Comment by rlm created at 2007-12-18 02:04:50

Merged in 2.9.1.alpha1
