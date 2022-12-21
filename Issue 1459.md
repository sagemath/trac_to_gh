# Issue 1459: [with patch] make notebook ?? behavior like command line behavior

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2007-12-11 10:43:44

Assignee: mhansen

On the command-line, if a class docstring is not found, then the one from __init__ is used.  This does not happen in the notebook.


---

Attachment

This fixes doctest formatting.


---

Attachment

You should make sure to run doctests (no pun intended):

```
**********************************************************************
File "sageinspect.py", line 404:
    sage: sage_getdoc(None)
Expected:
    ''
Got:
    'x.__init__(...) initializes x; see x.__class__.__doc__ for signature'
**********************************************************************
```



---

Comment by mabshoff created at 2007-12-22 15:17:44

mhansen also speculates that the patch above should also fix #1565.

Cheers,

Michael


---

Comment by rlm created at 2007-12-22 18:16:20

Resolution: fixed


---

Comment by rlm created at 2007-12-22 18:16:20

merged in 2.9.1 rc0

added
`if obj is None: return ''`
