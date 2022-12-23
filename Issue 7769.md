# Issue 7769: delete some rst files

Issue created by migration from https://trac.sagemath.org/ticket/7769

Original creator: jhpalmieri

Original creation time: 2009-12-26 16:11:44

Assignee: mvngu

This is a follow-up to #7466, and it may also be related to #7764.  In order to get rid of some of the warnings when building the reference manual: delete (by hand) everything in the directory SAGE_ROOT/devel/sage/doc/en/reference/sage/server/ *except* for

```
trac/trac.rst
wiki/moin.rst
```

None of the files in this directory are tracked by Mercurial, so we have to delete them by hand, as far as I can tell, therefore there is no patch file.

(This was given a positive review as part of #7466, but this part was never merged, so I'm giving it a positive review again.)




---

Comment by jhpalmieri created at 2009-12-26 16:11:49

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-12-26 16:11:55

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 20:41:11

Resolution: fixed
