# Issue 5446: [with patch, needs review] RealIntervalField creates non-unique RealFields

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-03-06 02:16:10

Assignee: somebody

`real_mpfi.pyx` uses the wrong function to create `RealField`s, so it creates new ones instead of using the previously-cached ones.

Fixed in the attached patch.



---

Attachment

Yep, this looks good. Out of curiousity, is there a reason `RIF` itself isn't unique (or just "no one's gotten around to it")?


---

Comment by mabshoff created at 2009-03-23 20:35:14

Resolution: fixed


---

Comment by mabshoff created at 2009-03-23 20:35:14

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
