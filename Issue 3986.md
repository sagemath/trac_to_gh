# Issue 3986: notebook -- a doc browser bug

Issue created by migration from https://trac.sagemath.org/ticket/3986

Original creator: was

Original creation time: 2008-08-29 04:58:19

Assignee: boothby

1. Go to any interactive help sheet in the notebook.

2. Go the very very bottom cell, below the text.

3. Press shift enter.

4. I get this traceback in the server log:

```
...
	    cell.evaluate(username = self.username)
	exceptions.AttributeError: TextCell instance has no attribute 'evaluate'
```


It's bad form getting tracebacks in the server log, though everything continues
to work fine.   The fix is to figure out why a text cell is having evaluate called
on it.  Is the bottom cell somehow incorrectly set to be a text cell?


---

Comment by mpatel created at 2009-08-10 09:42:35

Is this still a problem?


---

Comment by mpatel created at 2009-10-15 18:15:33

Changing status from new to needs_info.


---

Comment by timdumol created at 2010-01-19 11:19:51

This doesn't seem to be a problem in sagenb-0.6.


---

Comment by timdumol created at 2010-01-19 11:19:51

Resolution: invalid
