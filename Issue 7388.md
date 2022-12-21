# Issue 7388: upgrade ratpoints to 2.1.3

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-11-04 19:16:32

Assignee: tbd




---

Comment by rlm created at 2009-11-04 19:20:54

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2009-12-09 01:01:22

You seem to have left in a directory src-2.1.2 for no reason:

```
wstein`@`sage:~/build/sage-4.3.alpha1/spkg/optional/ratpoints-2.1.3$ ls
spkg-install  SPKG.txt  src  src-2.1.2
```


Otherwise this looks fine.


---

Comment by was created at 2009-12-09 01:01:22

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2009-12-09 01:10:47

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2009-12-09 01:10:47

New spkg is up, same location.


---

Comment by cremona created at 2009-12-30 17:44:50

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2009-12-30 17:44:50

Changing keywords from "" to "ratpoints".


---

Comment by cremona created at 2009-12-30 17:44:50

Looks fine to me too.  I installed it on 4.3 and tested sage/libs/ratpoints.pyx.


---

Comment by mhansen created at 2010-01-03 22:27:17

Resolution: fixed
