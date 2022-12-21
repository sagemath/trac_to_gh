# Issue 5543: [with patch, needs review] RealIntervalField parents are not unique

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2009-03-17 06:14:11

Assignee: somebody

Note that the attached patch has an apparently-spurious chunk that adds a single space to rings/polynomial/real_roots.pyx.  This is to force a recompilation for that file (to work around a bug in the dependency tracker); otherwise you end up with a broken Sage because the real_roots module won't load.  (I'll report the dependency tracker bug as a separate ticket in a minute.)


---

Attachment


---

Comment by mabshoff created at 2009-04-13 02:39:34

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 02:39:34

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
