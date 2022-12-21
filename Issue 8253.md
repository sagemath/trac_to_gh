# Issue 8253: search_src (etc.) bug

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2010-02-12 22:22:10

Assignee: tbd

In Sage 4.3.2:

```
search_src('is', 'prime', 'field', ignore_case=True)
Traceback (most recent call last):
...
TypeError: search() takes at most 3 arguments (4 given)
```

This is because of a bug in sage.misc.sagedoc: when calling re.search, flags like re.MULTILINE and re.IGNORECASE should be combined using bit-wise or, not by passing them as separate entries in a list.  The attached patch fixes this.


---

Attachment


---

Comment by mpatel created at 2010-02-16 21:38:16

I noticed another `*flags` nearby.  Should we make it `flags`?


---

Comment by jhpalmieri created at 2010-02-17 20:57:35

Yes.  Here's a new patch, rebased against 4.3.3.alpha0.


---

Comment by jhpalmieri created at 2010-02-17 20:57:35

Changing status from new to needs_review.


---

Attachment


---

Comment by mpatel created at 2010-02-18 02:00:36

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-18 22:05:09

Merged [trac_8253-search.v2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8253/trac_8253-search.v2.patch).


---

Comment by mvngu created at 2010-02-18 22:05:09

Resolution: fixed
