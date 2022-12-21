# Issue 6011: Bring plot/arrow.py to 100% coverage

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-05-09 02:45:35

Assignee: mabshoff

Bring plot/arrow.py to 100% coverage


---

Attachment

Also adds tiny plot3d enhancement (original doctest only tested Graphics.plot3d).

Please see [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.  Yet.


---

Comment by kcrisman created at 2009-05-09 02:49:05

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-05-09 02:49:05

Changing assignee from mabshoff to kcrisman.


---

Comment by kcrisman created at 2009-05-09 02:52:03

Changing component from doctest to documentation.


---

Attachment

reviewer patch; add consistency to the whole module


---

Comment by mvngu created at 2009-05-09 04:18:55

REFEREE REPORT



The patch `trac_6011.patch` applies OK against the "post-final" version sage-3.4.2, all doctests pass with the options `-t -long`, and the doctest coverage is now 100% as claimed. Note that `sage/plot/arrow.py` is not included in the reference manual, so you can't search for it in order to view the documentation for `sage/plot/arrow.py`.



The patch adds some trivial inconsistencies in how "two-dimensional" and "three-dimensional" are abbreviated. These and other inconsistencies are fixed in the reviewer patch `trac_6011-reviewer.patch`. Apart from the issue of consistency throughout the whole module, positive review for kcrisman's patch. Only my patch needs to be reviewed.


---

Comment by mabshoff created at 2009-05-11 09:02:40

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-11 09:02:40

Resolution: fixed
