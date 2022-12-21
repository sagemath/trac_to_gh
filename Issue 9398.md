# Issue 9398: Sage meddles with soft rlimits

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2010-06-30 22:11:44

Assignee: jason

Sage currently removes any soft resource limits set. If those limits are set, it's probably with good reason, so it would be better if it kept limits in place

```
sh-3.2$ ulimit -S -v 1000000
sh-3.2$ ulimit -v
1000000
sh-3.2$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: import os
sage: os.system("ulimit -v")
unlimited
0
```

| Sage Version 4.4.4, Release Date: 2010-06-23                       |
| Type notebook() for the GUI, and license() for information.        |


---

Comment by nbruin created at 2010-06-30 22:13:42

change all.py to not touch rlimits


---

Comment by nbruin created at 2010-06-30 22:14:07

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2010-06-30 22:18:00

I can't remember why this was added to Sage in 2005, so... positive review.


---

Comment by was created at 2010-06-30 22:18:00

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 08:26:24

Resolution: fixed
