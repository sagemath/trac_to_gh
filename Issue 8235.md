# Issue 8235: fix another doctest in base.pyx

Issue created by migration from Trac.

Original creator: wcauchois

Original creation time: 2010-02-11 00:40:23

Assignee: AlexGhitza

This ticket is related to #7985. There's another doctest in base.pyx (on line 1308) that uses the output of texture_set(), which is inconsistent across machines since the order of Texture objects in a set is not well defined. This should be a trivial fix.


---

Comment by wcauchois created at 2010-02-11 01:10:31

based on sage 4.3.1


---

Attachment

Its not terribly pretty, but this should fix it.


---

Comment by wcauchois created at 2010-02-11 01:10:51

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-11 10:06:08

Changing priority from major to minor.


---

Comment by mpatel created at 2010-02-11 10:06:08

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 10:06:08

Changing component from algebra to graphics.


---

Comment by mpatel created at 2010-02-11 10:09:47

Running `sage -t  plot/plot3d/base.pyx` 10 or so times in succession yields no failures.  Positive review.

Please remember to set / update the relevant ticket fields.

Thanks!


---

Comment by mpatel created at 2010-02-11 15:04:07

Resolution: fixed
