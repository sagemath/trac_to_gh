# Issue 6212: make sage -upgrade check that there are no applied hg queue patches

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-06-04 20:40:01

Assignee: tbd

CC:  jason jthurber

Keywords: sage upgrade applied hg queue

It would be nice if sage -upgrade aborted if are applied hg queue patches, in the same way it aborts if there are local changes.


---

Comment by ncalexan created at 2009-06-04 20:40:29

Even better:


```
[1:38pm] jason-: you have patches that are applied using mercurial queues.  Do you want to pop all of the patches? [y/n]
[1:38pm] jason-: yes would pop and continue the upgrae
[1:39pm] jason-: no would quit the upgrade
```



---

Comment by chapoton created at 2014-03-14 16:44:26

Changing status from new to needs_review.


---

Comment by chapoton created at 2014-03-14 16:44:26

we have switched to git, this is obsolete


---

Comment by mmezzarobba created at 2014-03-15 13:33:35

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-19 04:35:53

Resolution: wontfix
