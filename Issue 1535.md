# Issue 1535: jmol meshes are always smoothed

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2007-12-16 07:37:19

Assignee: was

This is great for surfaces and spheres, but makes things like platonic solids turn out very poorly. 

This should probably be handled at the IndexFaceSet level, where non-smooth vertices should be unique. 


---

Comment by robertwb created at 2007-12-16 07:37:23

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2007-12-16 07:37:23

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-01-04 11:05:55

The bundle was merged via #1665 in 2.9.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-04 11:05:55

Resolution: fixed
