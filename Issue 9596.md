# Issue 9596: is_totally_positive should give proven output

Issue created by migration from https://trac.sagemath.org/ticket/9596

Original creator: mstreng

Original creation time: 2010-07-25 12:45:28

Assignee: davidloeffler

CC:  mstreng

Keywords: real_embeddings is_totally_positive algebraic real numbers proven output

The number field function `real_embeddings` gives embeddings into finite precision real numbers, hence cannot be used for functions whose values are supposed to be proven (like `is_totally_positive`).

A patch for this ticket should correct the usage of `real_embeddings` and give `real_embeddings` a warning in the documentation string.

For more info, see

 * [http://groups.google.com/group/sage-nt/browse_thread/thread/fb34ad5be1bbe5fd](http://groups.google.com/group/sage-nt/browse_thread/thread/fb34ad5be1bbe5fd) and
 * [http://groups.google.com/group/sage-nt/browse_thread/thread/ce2a4b9555618f99/fbed7f10a944af48](http://groups.google.com/group/sage-nt/browse_thread/thread/ce2a4b9555618f99/fbed7f10a944af48)


```
sage: a = 30122754096401; b = 21300003689580
sage: (a/b)^2 > 2
True
sage: K.<sqrt2> = QuadraticField(2)
sage: (a/b+sqrt2).is_totally_positive()
False
```

Both should be `True`.

I'm creating a patch right now.


---

Attachment


---

Comment by mstreng created at 2010-07-30 12:14:55

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-09-22 09:55:01

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-09-22 09:55:01

Changes look sensible, and all doctests in `sage/rings/number_field` pass. Positive review.


---

Comment by mpatel created at 2010-09-29 04:23:26

Resolution: fixed
