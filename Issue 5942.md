# Issue 5942: bug in RealIntervalField printing

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-04-29 22:05:36

Assignee: somebody

CC:  cwitty mhansen

This seems bad to me...

```
sage: p=RealIntervalField(4)(pi)
sage: p.str(style='brackets')
'[3.00 .. 3.25]'
sage: p
4.?
```



---

Comment by ylchapuy created at 2009-11-26 02:45:12

should be closed with won't fix. It's a design choice.


---

Comment by AlexGhitza created at 2010-01-02 03:20:33

Mike, I'm ccing you as this should apparently be closed.


---

Comment by mhansen created at 2010-01-02 03:21:44

Resolution: invalid
