# Issue 7000: Move Sphinx-ify on-the-fly code to another module

Issue created by migration from https://trac.sagemath.org/ticket/7000

Original creator: mpatel

Original creation time: 2009-09-23 09:25:49

Assignee: tba

CC:  jhpalmieri

The code for running docstrings through Sphinx on-demand could be useful in other contexts:

 * Command-line (cf. 6820).
 * Notebook reST editor (cf. [The List](http://wiki.sagemath.org/SageUsability)).

Currently, the code lives in `cell.py`, but it would be easier to mantain and extend in `sage.misc`, say.


---

Comment by was created at 2009-09-30 08:16:35

Resolution: fixed


---

Comment by was created at 2009-09-30 08:16:35

This is now down as part of the notebook refactoring.  It's in sagenb.misc.sphinxify.
