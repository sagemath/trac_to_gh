# Issue 8138: Single-column index in PDF documentation

Issue created by migration from https://trac.sagemath.org/ticket/8138

Original creator: mpatel

Original creation time: 2010-01-31 09:45:31

Assignee: mvngu

CC:  jhpalmieri

Sphinx's LaTeX and PDF builders output two-column indexes / indices, but the badness is high.


---

Comment by mpatel created at 2010-01-31 10:03:44

One-column indexes for PDF ref. manual.  Depends on #8036's "utfx8" patch.


---

Attachment


---

Comment by mpatel created at 2010-01-31 10:06:50

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-31 10:07:33

The patch depends on #8036's "utf8x" patch, but rebasing should be easy.


---

Comment by mpatel created at 2010-01-31 10:08:31

The patch is adapted from [these examples](http://www.latex-community.org/forum/viewtopic.php?f=4&t=1735).


---

Comment by jhpalmieri created at 2010-01-31 16:59:21

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-01-31 16:59:21

Wow, the index looks _terrible_ before applying this patch, much better afterwards.  This adds 51 pages to the reference manual, but that's just a little over 1% of its total length, so I'm not concerned by that. 

One small error: you need an "r" before the triple quotes; otherwise the latex file says "enewenvironment" instead of "\renewenvironment".  I added it to the patch.


---

Attachment

apply instead of other patch


---

Comment by mpatel created at 2010-02-11 14:53:37

Resolution: fixed
