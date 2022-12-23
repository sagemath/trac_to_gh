# Issue 8901: negative integers in IntegerVectors()

Issue created by migration from https://trac.sagemath.org/ticket/8901

Original creator: ecurry

Original creation time: 2010-05-06 01:14:18

Assignee: sage-combinat

CC:  sdenton

Keywords: integer, vector

IntegerVectors() seems to only include vectors with positive integer entries:

```
sage: [-1,4] in IntegerVectors()
False
```


Can the class be changed to include vectors with some/all negative integer entries as well, or create a new, larger class for all integer vectors (since I can imagine that having a class for positive integer vectors would be useful in some applications)?

Thanks,
Eva


---

Comment by ecurry created at 2010-05-06 14:00:55

Changing priority from minor to major.


---

Comment by ecurry created at 2010-05-06 14:00:55

Changing assignee from sage-combinat to ecurry.


---

Comment by ecurry created at 2010-05-06 14:00:55

Status: Eva will look into funding for a Sage Days at Acadia where updating IntegerVectors can be one of the focuses.


---

Comment by tscrim created at 2012-05-09 22:30:15

This is not a bug, but instead a misnomer. I've updated the doc-strings to warn the users about this and created a Ticket #12932 to ask for the new class.


---

Comment by tscrim created at 2012-05-09 22:35:08

Changing status from new to needs_review.


---

Comment by tscrim created at 2012-05-09 22:35:08

Changing priority from major to minor.


---

Comment by sdenton created at 2012-05-09 22:42:02

Changing status from needs_review to positive_review.


---

Comment by sdenton created at 2012-05-09 22:42:02

Changing keywords from "integer, vector" to "integer, vector, days38".


---

Comment by sdenton created at 2012-05-09 22:45:04

Positive review assuming doc tests pass.


---

Comment by jdemeyer created at 2012-05-11 11:39:37

The formatting of the documentation should be like

```
Entries are non-negative::
```

with the double colon at the end.


---

Comment by jdemeyer created at 2012-05-11 11:39:37

Changing status from positive_review to needs_work.


---

Comment by tscrim created at 2012-05-11 13:54:50

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2012-05-11 13:54:50

Changed formatting of doc-string. Now consistent with the rest of the file.


---

Comment by sdenton created at 2012-05-15 16:27:38

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-05-18 14:55:22

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-05-18 14:55:22

There is a further problem with the documentation formatting: the list of AUTHORS should be indented like

```
AUTHORS:

 * bla bla bla
 * bla bla bla
   bla bla bla
```

as opposed to

```
AUTHORS:

 * bla bla bla
 * bla bla bla
 bla bla bla
```



---

Comment by tscrim created at 2012-05-19 16:13:36

Changing status from needs_work to needs_review.


---

Attachment

Corrected.


---

Comment by jdemeyer created at 2012-05-22 08:46:00

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-05-23 21:31:16

Resolution: fixed
