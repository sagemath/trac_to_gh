# Issue 3526: notebook -- change favicon to the new one seen at the new sagemath.org web site

Issue created by migration from https://trac.sagemath.org/ticket/3526

Original creator: TimothyClemans

Original creation time: 2008-06-28 09:01:55

Assignee: boothby




---

Comment by TimothyClemans created at 2008-06-28 09:04:37

Changing keywords from "" to "editor_wstein".


---

Comment by TimothyClemans created at 2008-06-28 09:07:53

Changing assignee from boothby to TimothyClemans.


---

Comment by TimothyClemans created at 2008-06-28 09:07:53

Changing status from new to assigned.


---

Comment by TimothyClemans created at 2008-06-28 09:07:53

Changing priority from major to trivial.


---

Comment by mabshoff created at 2008-07-06 02:18:39

This patch is basically empty since favicon.ico is binary and not in the patch:

```
cat trac_3526_extcode-3526.patch 
# HG changeset patch
# User Timothy Clemans <timothy.clemans@gmail.com>
# Date 1214643704 25200
# Node ID c6d839efcf8a7730a04e74399930ffab23651a5f
# Parent  c3d96fbf0f19bf8b2c0c1c5188943ba54829f947
#3526

diff -r c3d96fbf0f19 -r c6d839efcf8a notebook/images/favicon.ico
Binary file notebook/images/favicon.ico has changed
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 02:23:47

From http://developer.mozilla.org/en/docs/Mercurial_FAQ#How_can_I_diff_and_patch_files.3F:

 * If you are changing binary files or renaming files you may want to use git style patches with hg diff -g to retain that sort of information in the patch.
 * If you have a git style patch with renames and/or binary changes you can use hg import --no-commit to apply the patch to your tree or use hg qimport to import the patch to mq. 

Cheers,

Michael


---

Attachment


---

Attachment

Patch looks good to me, positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 02:38:43

Resolution: fixed


---

Comment by mabshoff created at 2008-07-06 02:38:43

Merged in Sage 3.0.4.alpha2
