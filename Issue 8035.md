# Issue 8035: make SageTeX able to detect version mismatches

Issue created by migration from https://trac.sagemath.org/ticket/8035

Original creator: ddrake

Original creation time: 2010-01-22 00:49:53

Assignee: tbd

CC:  jhpalmieri

Keywords: sagetex

In comment:21:ticket:7617, John Palmieri suggested that SageTeX detect version mismatches between the Python module (installed in Sage) and the LaTeX style file. We should implement this.

One difficulty is that people have lots of old sagetex.sty files around, and whatever mechanism we use would need to work with those.


---

Comment by ddrake created at 2012-01-16 07:00:03

This is fixed by the spkg at #12267. This ticket should be closed if the spkg there is merged.


---

Comment by ddrake created at 2012-05-25 03:42:47

Changing status from new to needs_review.


---

Comment by ddrake created at 2012-05-25 03:43:08

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2012-05-25 03:46:00

Hmm, I forget how to close tickets. Release manager, please close this.


---

Comment by jdemeyer created at 2012-06-02 13:26:17

Resolution: duplicate
