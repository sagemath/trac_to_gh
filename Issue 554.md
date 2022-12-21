# Issue 554: the calculus roots command is totally stupid.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-01 17:25:30

Assignee: was

Consider this below -- the output doesn't make any sense at all:

```
sage: var('x')
sage: f = x^(1/9) + (2^(8/9) - 2^(1/9))*(x - 1) - x^(8/9)
sage: f
(2^(8/9) - 2^(1/9))*(x - 1) - x^(8/9) + x^(1/9)
sage: f.roots()
[((x^(8/9) - x^(1/9) + 2^(8/9) - 2^(1/9))/(2^(8/9) - 2^(1/9)), 1)]
```




---

Comment by mhansen created at 2007-11-03 19:53:39

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2007-11-03 19:53:39

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2007-11-03 20:03:42

Resolution: fixed
