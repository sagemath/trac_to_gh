# Issue 8494: docstring f or digits() should mention its inverse

Issue created by migration from https://trac.sagemath.org/ticket/8494

Original creator: ddrake

Original creation time: 2010-03-11 05:40:42

Assignee: mvngu

One can use the `digits()` method to go from an integer to a list of digits, but it would be nice if the docstring explained how to do the inverse:

```
Z(x.digits(base), base)
```



---

Comment by ddrake created at 2010-03-11 07:01:02

I took the liberty of fixing up some of the ReST formatting, and also removed a comment that says "s = 2003^100300000" crashes Sage, because it doesn't anymore. (On my machine, at any rate.)


---

Comment by ddrake created at 2010-03-11 07:01:02

Changing status from new to needs_review.


---

Attachment

Added a bit about `balanced_sum`; note that Sphinx won't do the hyperlink properly until we add `sage.misc.misc_c` to the reference manual.


---

Comment by mvngu created at 2010-03-12 05:58:33

Looks good to go into Sage 4.3.4.rc0.


---

Comment by mvngu created at 2010-03-12 05:58:33

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-14 08:25:50

Resolution: fixed
