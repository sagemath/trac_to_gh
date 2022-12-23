# Issue 4828: [with patch, needs review] Sage 3.2.2.rc2: Fix documentation build issues

Issue created by migration from https://trac.sagemath.org/ticket/4828

Original creator: mabshoff

Original creation time: 2008-12-19 06:34:10

Assignee: mabshoff

There are two issues: 

 * In sage/sage/combinat/ranker.py "Thiéry" is used without the proper encoding, so change it to "Thiery" since that is consistent with the other spellings
 * in doc/ref/files we still include the old word.tex file which no longer exists, so delete that line. The new words documentation will be in 3.3.

Cheers,

Michael


---

Attachment


---

Attachment

I had to delete the patchlevel.tex hunk to get the doc patch to apply, but otherwise looks good, positive review.


---

Comment by mabshoff created at 2008-12-19 07:07:47

Resolution: fixed


---

Comment by mabshoff created at 2008-12-19 07:07:47

Merged both patches in Sage 3.2.2.rc2
