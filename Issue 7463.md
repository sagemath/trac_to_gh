# Issue 7463: document memory management for the magma interface

Issue created by migration from https://trac.sagemath.org/ticket/7463

Original creator: was

Original creation time: 2009-11-14 18:55:29

Assignee: was

Add documentation to magma.py explaining memory management for this interface. 

The attached patch will -- if tested using 

```
cd devel/sage/sage/interfaces/
sage -t --only_optional=magma magma.py
```

have doctest failures.  This isn't because of this patch.  See #7462. 


---

Attachment


---

Comment by was created at 2009-11-14 18:56:09

Changing status from new to needs_review.


---

Comment by GeorgSWeber created at 2009-11-14 20:40:52

Changing status from needs_review to positive_review.


---

Comment by GeorgSWeber created at 2009-11-14 20:40:52

I couldn't resist to review this right on the spot. What should I say? I even tested the html documentation, and everything seems to be just perfect.


---

Comment by mhansen created at 2009-11-17 06:01:57

Resolution: fixed
