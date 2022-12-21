# Issue 2187: [with patch, needs review] improve refman autogeneration; add and rewrite much reference manual text

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-02-17 05:35:37

Assignee: tba

I have two patches.  One, for hg_doc, improves the consistency between the formatting of module docstrings, class docstrings, and function docstrings.  The main effect of this is that "AUTHORS:" blocks are now specially translated in class docstrings, to match the behavior of module and function docstrings.

The other patch, for hg_sage, adds and rewrites a fair bit of text: fixing typos, adding LaTeX formatting, etc.

I also snuck in a bugfix: `IntegerMod_gmp` and `IntegerMod_int` had an `__index__` method, so that values could be used as array indices; but the method was missing from `IntegerMod_int64`.


---

Attachment


---

Attachment

Both patches looks good to me, they apply cleanly -> positive review.


---

Comment by mabshoff created at 2008-02-17 13:04:56

Resolution: fixed


---

Comment by mabshoff created at 2008-02-17 13:04:56

Merged in Sage 2.10.2.alpha1
