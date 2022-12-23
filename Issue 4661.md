# Issue 4661: clean up module_list.py

Issue created by migration from https://trac.sagemath.org/ticket/4661

Original creator: craigcitro

Original creation time: 2008-11-30 09:00:21

Assignee: craigcitro

There were a few duplicate entries in  `module_list.py`, which didn't cause any trouble, but caused sage to build some extensions (like `sage/structure/sage_object.pyx`) multiple times during the build. The attached patch alphabetizes the module list, and removes duplicates.


---

Attachment

I just posted Craig's patch that he gave to me off-trac. I did nuke the build directory and a sage -ba followed by a -t -long passed, so positive review.

Some commented out extensions might have to be nuked, but that ought to get taken care of via the followup ticket #4663.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 10:11:33

Resolution: fixed


---

Comment by mabshoff created at 2008-11-30 10:11:33

Merged in Sage 3.2.1.rc1
