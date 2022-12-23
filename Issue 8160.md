# Issue 8160: add 'text' option to sphinxify

Issue created by migration from https://trac.sagemath.org/ticket/8160

Original creator: jhpalmieri

Original creation time: 2010-02-03 02:20:23

Assignee: was

CC:  mpatel

This patch adds a 'text' option to sphinxify: use `sphinxify(s, format='text')` or `sphinxify(s, format='html')`, where format is optional with default value 'html'.  The intended use is in sage.misc.sagedoc for producing docstrings from the command line.  I'll create another ticket for that.


---

Attachment

apply to sagenb repo


---

Comment by jhpalmieri created at 2010-02-03 02:33:09

Changing status from new to needs_review.


---

Attachment

Rebased vs. #8102.  Apply only this patch.  sagenb repo.


---

Comment by mpatel created at 2010-02-03 04:57:40

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-03 04:57:40

I've attached a version rebased against #8102 --- it seemed a bit easier than the opposite.  Positive review for the first patch, at least.


---

Comment by mpatel created at 2010-02-05 00:37:35

Resolution: fixed
