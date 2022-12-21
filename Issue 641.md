# Issue 641: from sage.all import * for spyx files/cython notebook cells

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-09-12 04:48:59

Assignee: boothby

In spyx files, and cython blocks of the notebook, all names in sage.all are available (one doesn't need to import Integer, et al.) 

This means that miss-spelled/non-existent names will not be caught at compile time though. 



---

Comment by robertwb created at 2007-09-12 04:51:10

Changing assignee from boothby to robertwb.


---

Comment by robertwb created at 2007-09-12 04:51:10

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2007-09-15 21:04:59

Resolution: fixed


---

Comment by was created at 2007-09-15 21:04:59

This is frickin' awesome.  In sage-2.8.4.3.  Done.
