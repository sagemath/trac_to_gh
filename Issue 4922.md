# Issue 4922: convert sage.monoids.* docstrings to Sphinx

Issue created by migration from https://trac.sagemath.org/ticket/4922

Original creator: mhansen

Original creation time: 2009-01-01 22:54:39

Assignee: tba




---

Attachment


---

Comment by jhpalmieri created at 2009-02-09 21:22:31

Looks good.  One tiny change: 

sage/monoids/free_monoid.py, line 156: change ``i`th` to ``i`-th`.

(This is in a function whose name starts with double underscores, so it isn't even in the reference manual.  Just in case we add such things to the reference manual eventually, though...)

After this change, positive review.


---

Comment by mabshoff created at 2009-02-24 18:45:38

Resolution: fixed


---

Attachment

Merged in Sage 3.4.alpha0.

Cheers,

Michael
