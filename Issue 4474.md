# Issue 4474: A hack in preparsing files is dangerous/confusing

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-09 03:16:04

Assignee: cwitty

There is a dangerous hack in preparser.py. Given input file:

```
load a.sage
load b.py
```

   
Then b.py will be loaded while the file is being *parsed*, and *before* a.sage is loaded.  That would be very confusing.  See the related #4473 and apply that patch before working on this.


---

Comment by aapitzsch created at 2014-05-01 08:36:20

The hack has been removed in #7514.


---

Comment by aapitzsch created at 2014-05-01 08:36:20

Changing status from new to needs_review.


---

Comment by ncohen created at 2014-05-05 11:43:05

You must set it to positive_review in this case.


---

Comment by ncohen created at 2014-05-05 11:43:05

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-05-06 15:15:25

Resolution: duplicate
