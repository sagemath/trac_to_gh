# Issue 6009: Bring plot/text.py to 100%

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-05-08 19:14:56

Assignee: mabshoff

Bring plot/text.py to 100%.


---

Attachment


---

Comment by kcrisman created at 2009-05-08 19:25:51

See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.


---

Comment by kcrisman created at 2009-05-08 19:25:51

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-05-08 19:25:51

Changing assignee from mabshoff to kcrisman.


---

Comment by kcrisman created at 2009-05-09 02:51:40

Changing component from doctest to documentation.


---

Comment by mvngu created at 2009-05-09 02:54:47

reviewer patch: fix typos, add consistency to the whole module


---

Attachment

REFEREE REPORT



The patch `trac_6009.patch` applies OK against the "post-final" sage-3.4.2, all doctests pass with the options `-t -long`. The reference manual built fine, but note that `sage/plot/text.py` is not included in the reference manual so don't be surprised when you can't search for `sage/plot/text.py` in the reference manual. The doctest coverage for `sage/plot/text.py` is 100% as claimed.



However, I notice that the patch introduces some typos and inconsistencies into the module `sage/plot/text.py`. These are fixed in the reviewer patch `trac_6009-reviewer.patch`. Apart from these issues, positive review for kcrisman's patch. Only my patch needs to be reviewed.


---

Comment by jhpalmieri created at 2009-05-09 20:34:37

Reviewer patch looks good.


---

Comment by mabshoff created at 2009-05-11 08:52:14

Changing component from documentation to doctest.


---

Comment by mabshoff created at 2009-05-11 08:52:14

Resolution: fixed


---

Comment by mabshoff created at 2009-05-11 08:52:14

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
