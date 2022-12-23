# Issue 8189: hg.py: fix some docstrings

Issue created by migration from https://trac.sagemath.org/ticket/8189

Original creator: jhpalmieri

Original creation time: 2010-02-05 04:54:39

Assignee: mvngu

In hg.py, strings like `ssh://[user`@`]host[:port]/[path]` appear in docstrings, and Sphinx turns them into active links in the html documentation (which are obviously broken), and Sphinx produces warnings when producing the latex/pdf documentation:

```
.../devel/sage/doc/en/reference/sage/misc/hg.rst:: WARNING: unusable reference target found: ssh://[user@]host[:port]/[path
```

This patch puts these links into double backquotes, fixing both of these issues.



---

Comment by jhpalmieri created at 2010-02-05 04:55:30

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-02-05 06:12:27

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-11 15:07:05

Resolution: fixed
