# Issue 5387: [with patch, needs review] a few changes to the installation guide

Issue created by migration from https://trac.sagemath.org/ticket/5387

Original creator: jhpalmieri

Original creation time: 2009-02-26 18:29:41

Assignee: jhpalmieri

At least one thing in the installation guide (a table) disappeared in the ReST conversion, and I've changed a few other things: how to build the documentation, a broken link, etc.



---

Attachment


---

Comment by jhpalmieri created at 2009-02-26 18:31:17

By the way, for the list of software, I just copied it from the old installation guide; I didn't check it for accuracy or omissions.


---

Comment by wdj created at 2009-02-26 21:36:20

Isn't the current list of software is on the wiki at
http://wiki.sagemath.org/standard_packages_available_for_SAGE?
The list you have in the patch and that list from the wiki don't
agree.


---

Comment by jhpalmieri created at 2009-02-26 22:15:51

I think the current list is actually in [http://sagemath.org/packages/standard/](http://sagemath.org/packages/standard/) or $SAGE_ROOT/spkg/installed, and the list there doesn't match the one in the installation guide or the one on the wiki.

Anyway, here's a patch (apply on top of the old one) with a new list.


---

Comment by jhpalmieri created at 2009-02-26 22:16:25

apply on top of other patch


---

Attachment

Applies cleanly to sage-3.4.alpha0 using hg_sage.apply (*not* hg_doc). Compiles cleanly and without error.

Excellent job - thanks for making this patch!


---

Comment by mabshoff created at 2009-02-28 16:27:04

Merged both patches in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-28 16:27:04

Resolution: fixed


---

Comment by mvngu created at 2009-03-01 04:34:42

reviewer fixes for above patches


---

Comment by mvngu created at 2009-03-01 04:37:40

Changing status from closed to reopened.


---

Comment by mvngu created at 2009-03-01 04:37:40

Changing keywords from "" to "installation guide".


---

Attachment

The patch *trac_5387_reviewer-fixes.patch* fixes some typos found in the patches by jhpalmieri.


---

Comment by mvngu created at 2009-03-01 04:37:40

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-03-01 04:41:20

Do not reopen ticket that I have closed. Open a followup ticket - this is otherwise a giant mess.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 04:41:20

Resolution: fixed


---

Comment by mabshoff created at 2009-03-01 04:45:11

To keep things simple: Merged trac_5387_reviewer-fixes.patch in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mvngu created at 2009-03-01 04:47:27

Replying to [comment:8 mabshoff]:
> To keep things simple: Merged trac_5387_reviewer-fixes.patch in Sage 3.4.rc0.
Sorry about this, Michael. I'll keep your advice in mind.
