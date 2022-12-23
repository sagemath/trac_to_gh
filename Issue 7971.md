# Issue 7971: Change all occurrences of "method" to "algorithm" in coding/code_bounds.py

Issue created by migration from https://trac.sagemath.org/ticket/7971

Original creator: rbeezer

Original creation time: 2010-01-18 04:37:28

Assignee: wdj

CC:  wdj

This is a follow-on to #6094.  More places where the keyword argument "method=" should be changed to "algorithm=".


---

Comment by rbeezer created at 2010-01-18 05:41:10

This patch will build, and the tests in sage/coding all pass.  But I don't have Guava installed, which is needed for most of the affected doctests.

David - maybe you can run the optional tests as part of a review?


---

Attachment


---

Comment by rbeezer created at 2010-01-18 05:45:08

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-01-18 06:52:08

Passes all doctests on Sage 4.3.1.rc0 with or without the patch. To run the optional doctests that require Guava: After applying the patch, install the optional Guava package by installing the package [gap_packages-4.4.10_6.spkg](http://www.sagemath.org/packages/optional/gap_packages-4.4.10_6.spkg). Running doctest on "sage/coding/code_bounds.py" with the options

```
-t -long -optional
```

results in all doctests passed. Positive review.


---

Comment by mvngu created at 2010-01-18 06:52:08

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-01-18 21:21:31

This needs work (deprecation warnings) and so should just be handled as part of #6094.  

I've marked this as "needs work" but should be marked some form of invalid.


---

Comment by rbeezer created at 2010-01-18 21:21:31

Changing status from positive_review to needs_work.


---

Comment by jsrn created at 2010-11-02 14:02:22

The currently newest uploaded patch for Trac #6094 -- needing a positive review -- handles all these cases, so this Trac should just be closed.


---

Comment by rlm created at 2010-11-09 11:06:03

Resolution: duplicate
