# Issue 8167: Use LaTeX-friendly Unicode characters in SageNB docstrings

Issue created by migration from https://trac.sagemath.org/ticket/8167

Original creator: mpatel

Original creation time: 2010-02-03 09:23:05

Assignee: was

CC:  mvngu robert.marik jhpalmieri

In order to build the PDF reference manual --- with the current settings in `doc/common/conf.py` --- we need replace several Unicode characters introduced at #7249.


---

Comment by mpatel created at 2010-02-03 09:27:16

Replace some Unicode characters.  sagenb repo.


---

Attachment


---

Comment by mpatel created at 2010-02-03 09:30:54

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-02-03 09:30:54

Small-scale tests with the patch show promise.  I'm attempting to build the full PDF manual now.


---

Comment by mpatel created at 2010-02-03 09:30:54

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-03 09:41:11

It builds!


---

Comment by jhpalmieri created at 2010-02-04 16:00:05

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-02-04 16:00:05

Builds for me, too -- if I install sagenb-0.7.3, building the PDF documentation fails before the patch, succeeds afterward.


---

Comment by mpatel created at 2010-02-05 00:36:13

Resolution: fixed
