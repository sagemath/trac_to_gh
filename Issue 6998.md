# Issue 6998: wrong error for powerseries sqrt

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-09-22 23:19:05

Assignee: somebody


```
sage: R.<x> = QQ[[]]
sage: (x^10/2).sqrt()
Traceback (click to the left for traceback)
...
ValueError: power series does not have a square root since it has odd
valuation.
```



---

Comment by robertwb created at 2009-09-22 23:19:16

Changing component from basic arithmetic to algebra.


---

Comment by robertwb created at 2009-09-22 23:19:16

Changing assignee from somebody to tbd.


---

Comment by mhansen created at 2009-09-24 06:12:15

Changing assignee from tbd to mhansen.


---

Comment by mhansen created at 2009-09-24 06:12:15

Changing status from new to assigned.


---

Attachment


---

Comment by awebb created at 2009-10-06 08:50:26

The patch works as advertised so I give it a positive review. The doc also builds correctly.

Adam


---

Comment by mhansen created at 2009-10-15 09:35:11

Resolution: fixed
