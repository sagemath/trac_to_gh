# Issue 5492: implement sage -bt

Issue created by migration from https://trac.sagemath.org/ticket/5492

Original creator: AlexGhitza

Original creation time: 2009-03-11 22:54:04

Assignee: was

Keywords: build test

This was requested by Mike Stillman at Sage Days 14, and sounds like a good idea to me:  have


```
sage -bt <filename(s)>
```


as a shortcut for the current


```
sage -b
sage -t <filename(s)>
```




---

Comment by jdemeyer created at 2010-10-15 07:33:47

Patch for sage-scripts


---

Attachment


---

Comment by jdemeyer created at 2010-10-15 07:40:31

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-10-18 11:00:16

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-10-18 11:00:16

Applies cleanly to sage-4.6.alpha3.  I tried it out with various combinations of options and it looks good.


---

Comment by jdemeyer created at 2010-11-01 10:05:00

Resolution: fixed
