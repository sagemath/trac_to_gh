# Issue 6653: Add --no-pdf-links option for doc/html/index.html builder.

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-07-29 08:39:16

Assignee: tba

CC:  schilly

The top-level `index.html` for Sage documentation now includes links to the corresponding PDF files (cf. #4460).  However, it can be useful to suppress these links.  Building on #6187, this ticket adds an option `--no-pdf-links` to `sage -docbuild`.

See #4460 for some history and an earlier version.


---

Comment by mpatel created at 2009-07-29 09:13:10

Depends on #6187.


---

Attachment


---

Comment by jhpalmieri created at 2009-11-19 21:50:05

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2009-11-19 21:51:55

Looks good to me: running "sage -docbuild website html --no-pdf-links" turns the links off, and then running "sage -docbuild website html" turns them back on again.


---

Comment by mhansen created at 2009-11-29 04:45:17

Resolution: fixed
