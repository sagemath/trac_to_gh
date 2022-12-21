# Issue 4201: add .options and .reset to plot functions

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-09-26 17:08:06

Assignee: was

CC:  boothby




---

Comment by mhansen created at 2008-09-26 20:07:53

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2008-09-26 20:07:53

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-26 20:08:32

Note that this patch is on top of #4099.


---

Comment by mabshoff created at 2008-09-26 20:12:27

A couple spelling problems:

 * defualt options 
 * decorator whcich renames

Cheers,

Michael


---

Attachment

What spelling problems?  I don't see any ;-)


---

Comment by jason created at 2008-09-26 22:30:22

This does not apply cleanly to alpha1.  For example, the plot_slope_field patch in alpha1 causes a reject.


---

Attachment

Apply instead of previous patch


---

Comment by jason created at 2008-09-26 22:35:48

trac_4201-rebased.patch is rebased against 3.1.3alpha1; apply it instead of the first patch.


---

Comment by jason created at 2008-09-26 22:39:45

This could make #4154 easy now.


---

Comment by jason created at 2008-09-26 22:42:15

The code looks reasonable, the rebased patch applies cleanly, it seems to work as advertised, and it solves the problem in a very elegant fashion.  Oh, and doctests in plot/*.py pass.

Positive review.


---

Comment by jason created at 2008-09-26 23:04:43

the third patch above adds a docstring for the reset function.  Apply it on top of the second patch.


---

Comment by jason created at 2008-09-26 23:21:09

The trac_4207-options-doc-defaults.patch adds a defaults() method to get the default options and also modifies the reset() and defaults() docstrings to reflect the options of the current function instead of the vague general decorator docstring.


---

Comment by jason created at 2008-09-26 23:22:15

Positive review for the rebased original patch.  There probably ought to be a review of my patches.  Mike, do you want to review them?


---

Attachment


---

Attachment

I just indented the examples on Jason's patches.  +1 to them.  Apply only the last three patches.


---

Comment by mabshoff created at 2008-09-27 04:24:52

Merged the last three patches in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-27 04:24:52

Resolution: fixed
