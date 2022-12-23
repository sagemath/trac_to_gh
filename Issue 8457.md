# Issue 8457: Yet more annoying warnings when building the reference manual

Issue created by migration from https://trac.sagemath.org/ticket/8457

Original creator: mpatel

Original creation time: 2010-03-06 10:10:37

Assignee: mvngu

CC:  jhpalmieri mvngu

Mostly of this sort:

```
categories/examples/finite_semigroups.rst:6: (WARNING/2) error while formatting signature for sage.categories.examples.finite_semigroups.LeftRegularBand.Element.wrapped_class.center: arg is not a module, class, method, function, traceback, frame, or code object
```

This may happen because `wrapped_class = str` is [an alias of] a builtin.


---

Attachment

Skip builtins.  Depends on #7448.


---

Comment by mpatel created at 2010-03-06 14:44:13

The attached patch appears to be enough for builtins, if we're willing to skip them.

Note: It clashes with the first at #8452.


---

Attachment

Rebased vs. #8452.


---

Comment by mpatel created at 2010-03-09 11:54:24

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-03-09 22:18:42

I think this is okay: I don't see a problem with skipping builtins.


---

Comment by jhpalmieri created at 2010-03-09 22:18:42

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-11 04:46:48

Resolution: fixed


---

Comment by mvngu created at 2010-03-11 04:46:48

Merged [trac_8457-doc_skip_builtins.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8457/trac_8457-doc_skip_builtins.2.patch).
