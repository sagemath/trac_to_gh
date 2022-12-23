# Issue 6526: remove naive suffix trees

Issue created by migration from https://trac.sagemath.org/ticket/6526

Original creator: rlm

Original creation time: 2009-07-13 19:12:33

Assignee: mhansen

CC:  saliola

This is one of the obstructions to switching the graph backends over to Cython by default.

To quote Franco:

```
But all the doctest failures occur in the NaiveSuffixTreeClass, which
is a naive implementation. This code was only intended for testing
purposes, so I think it is fine to delete it (delete both
NaiveSuffixTree and NaiveSuffixTreeClass). I am pretty certain it is
not used anywhere else (it should not be, if it is), because it is a
very slow implementation (hence, the name naive).
```



---

Comment by rlm created at 2009-07-13 19:12:47

This will be based on #6519.


---

Comment by rlm created at 2009-07-14 16:05:03

based on #6519


---

Attachment


---

Comment by saliola created at 2009-07-16 23:47:10

Positive review.


---

Comment by mvngu created at 2009-07-18 14:50:06

Resolution: fixed
