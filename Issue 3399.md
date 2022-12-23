# Issue 3399: [with patch, needs review] sage build scripts should be moved to devel

Issue created by migration from https://trac.sagemath.org/ticket/3399

Original creator: gfurnish

Original creation time: 2008-06-11 15:00:38

Assignee: gfurnish

The sage build files that use pbuild should be moved to the devel repo while the pbuild files should stay in extcode.


---

Comment by gfurnish created at 2008-06-11 15:03:33

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-06-11 20:50:19

Good in principle, but as discussed with you in person this does not work as is due to circular dependency issues.

Cheers,

Michael


---

Comment by craigcitro created at 2008-06-20 05:02:45

Changing keywords from "" to "editor_mabshoff".


---

Attachment


---

Attachment


---

Attachment

Please remove the old patches, apply the new patches, and rereview.  This patch also adds documentation on how to add files to pbuild: see devel/sage/sagebuild.py


---

Comment by mabshoff created at 2008-07-06 09:05:29

Patch looks good to me and applies cleanly. Positive review. We might have to think about names and locations of those files in the long term, but for now this does the right thing.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 09:05:41

Resolution: fixed


---

Comment by mabshoff created at 2008-07-06 09:05:41

Merged in Sage 3.0.4.alpha2
