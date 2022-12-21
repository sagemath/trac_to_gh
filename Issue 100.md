# Issue 100: sage doctest system -- when it tests a pyrex file it still describes it as a .py file

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-30 21:47:46

Assignee: was

Example:

```
File "element.py", line 507:
    sage: f.mod( (x - y, y - z) )
Exception raised:
    Traceback (most recent call last):
```



---

Comment by was created at 2007-01-13 02:19:31

fixed


---

Comment by was created at 2007-01-13 02:19:31

Resolution: fixed
