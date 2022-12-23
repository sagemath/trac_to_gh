# Issue 3008: first cell in notebook is undeletable

Issue created by migration from https://trac.sagemath.org/ticket/3008

Original creator: mhampton

Original creation time: 2008-04-23 18:44:30

Assignee: somebody

The top cell in a notebook worksheet cannot be deleted by backspace.  A workaround is ctrl-backspace from the next cell, but that is annoyingly indirect.  I have tried this on both Safari and Firefox on OS X, but not other platforms.


---

Attachment

This patch:

```
Fix trac #3008 -- Fix delete first cell bug. Also:
  2. Make deleting/merging cells via control-backspace feel slightly snappier
  3. Improve the documentation in js.py for the join_cell function.
```



---

Comment by mhampton created at 2008-05-11 12:10:39

The attached patch works for me, looks good.  Positive review.


---

Comment by mabshoff created at 2008-05-11 12:21:47

Resolution: fixed


---

Comment by mabshoff created at 2008-05-11 12:21:47

Merged in Sage 3.0.2.alpha0
