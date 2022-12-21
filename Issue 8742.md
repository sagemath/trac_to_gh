# Issue 8742: Lazy format strings

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2010-04-21 19:50:06

Assignee: hivert

CC:  nthiery

Keywords: lazy format strings

The class `LazyFormat` allows to create format strings which calls their argument's `__repr__` only if needed. Otherwise it behaves as usual format string.

This is useful tor speeding up tests suites. 


---

Comment by hivert created at 2010-04-21 19:53:35

Changing status from new to needs_review.


---

Comment by hivert created at 2010-04-21 22:04:34

I forgot to add the doc in the reference manual, I just reuploaded a version with it.


---

Attachment

The former patch made sphinx to raise a warning. This is now fixed.


---

Comment by hivert created at 2010-05-12 17:37:58

Changing status from needs_review to positive_review.


---

Attachment

This is an extract from a private mail from Nicolas Thiéry:

```
 - trac_8742-lazy_format-fh.patch
   trac_8742-lazy_format-review-nt.patch

   Si mon patch de review est ok et les tests passent, c'est tout bon!
```

Translation: If my review patch is ok and if the tests pass, this is all good.

I'm ok with Nicolas review patch. I Put a positive review.


---

Comment by mhansen created at 2010-06-05 21:50:02

Resolution: fixed
