# Issue 9442: reference manual issues for 4.5.alpha4

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-07-06 22:41:15

Assignee: mvngu

The attached patch fixes the two warnings when building the ref manual in Sage 4.5.alpha4:

```
/Applications/sage_builds/sage-4.5.alpha4/devel/sage/doc/en/reference/graphs.rst:4: (WARNING/2) toctree references unknown document u'sage/graphs/pq_trees.py'
/Applications/sage_builds/sage-4.5.alpha4/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.py:docstring of sage.schemes.elliptic_curves.sha_tate.Sha.bound_kato:12: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
```




---

Attachment


---

Comment by mpatel created at 2010-07-07 02:39:04

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-07-07 02:39:18

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-07-08 19:09:31

Resolution: fixed
