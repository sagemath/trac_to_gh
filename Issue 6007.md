# Issue 6007: Bring plot/primitive.py to 100% coverage

Issue created by migration from https://trac.sagemath.org/ticket/6007

Original creator: kcrisman

Original creation time: 2009-05-08 16:43:54

Assignee: mabshoff

Bring plot/primitive.py to 100% coverage.


---

Attachment


---

Comment by kcrisman created at 2009-05-08 16:45:31

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-05-08 16:45:31

Please see [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for explanation of why there is no loads(dumps()) test.


---

Comment by kcrisman created at 2009-05-08 16:45:31

Changing assignee from mabshoff to kcrisman.


---

Comment by kcrisman created at 2009-05-09 02:51:18

Changing component from doctest to documentation.


---

Comment by mvngu created at 2009-05-09 03:22:41

reviewer patch; add consistency to the whole module


---

Attachment

REFEREE REPORT



The patch `trac_6007.patch` applies fine against the "post-final" version sage-3.4.2, all doctests pass with the options `-t -long`, and the doctest coverage is 100% as claimed. The reference manual built OK, but note that `sage/plot/primitive.py` is not included in the reference manual, so you can't search for the module in it.



On the side of pedantry, the patch introduces a trivial inconsistency in how "two-dimensional" and "three-dimensional" are abbreviated. So all such references in the module `sage/plot/primitive.py` now follow the forms `2D` and `3D`. Apart from this trivial issue of inconsistency which is fixed in `trac_6007-reviewer.patch`, positive review for kcrisman's patch. Only my patch needs to be reviewed.


---

Comment by jhpalmieri created at 2009-05-09 20:35:25

> Only my patch needs to be reviewed.

Looks good.


---

Comment by mabshoff created at 2009-05-11 08:40:42

Resolution: fixed


---

Comment by mabshoff created at 2009-05-11 08:40:42

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
