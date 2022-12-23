# Issue 2828: get doctest coverage for combinat/ to 100%

Issue created by migration from https://trac.sagemath.org/ticket/2828

Original creator: mhansen

Original creation time: 2008-04-06 10:09:16

Assignee: mhansen

CC:  sage-combinat




---

Comment by mhansen created at 2008-04-06 10:15:16

Changing status from new to assigned.


---

Comment by mhansen created at 2008-04-06 10:16:16

Ignore lint.patch.  2828.patch is the one to be reviewed.


---

Attachment

Note that this patch is based against 3.0.alpha2.


---

Comment by malb created at 2008-04-06 13:14:57

*Review*
 * patch applies cleanly
 * patch looks good but I'm not an expert on the subject matter
 * coverage is indeed 100% as advertised
 * doctests pass
 * some small issues are:
   * some "possibly wrong"s are reported, see `trac_2828_fixes.patch`
   * one typo, see `trac_2828_fixes.patch`
   * a couple of classes don't have `loads(dumps(s))` doctests
 * However, this shouldn't stop the patch from being applied. 
 * I say apply asap, don't let this big patch bitrot.

I provide a partial fix for the issues mentioned above. The patch does not fix all issues because I ran out of steam.


---

Attachment

Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-06 14:09:32

Resolution: fixed
