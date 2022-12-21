# Issue 2764: apply Minh Nguyen's patches to hg_doc

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-04-01 22:14:30

Assignee: tba




---

Comment by mhansen created at 2008-04-01 22:21:02

Give credit to Minh Nguyen for these.


---

Comment by mhansen created at 2008-04-01 22:21:02

Changing status from new to assigned.


---

Comment by mhansen created at 2008-04-01 22:21:02

Changing assignee from tba to mhansen.


---

Comment by mabshoff created at 2008-04-02 04:58:46

This patch is wrong since some of the patch needs to be applied to the Sage repo. Some of the TeX files are overwritten on doc rebuild, so patching them is counterproductive.

Cheers,

Michael


---

Attachment

I'm 99.9% sure that the patch is correct as is.  If you can give me a specific instance of something that's in the wrong place and where it should go, I'll stand corrected.


---

Comment by mabshoff created at 2008-04-02 19:34:22

Sorry mahnsen, you are correct. The patch looks good and does patch TeX files that are *not* overwritten.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-02 19:36:13

Merged in Sage 3.0.alpha1


---

Comment by mabshoff created at 2008-04-02 19:36:13

Resolution: fixed
