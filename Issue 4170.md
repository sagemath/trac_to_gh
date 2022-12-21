# Issue 4170: symbolic ring does not accept python longs

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-09-23 01:10:30

Assignee: burcin

The easy fix is to add it to the big list in `_coerce_impl` at sage.calculus.calculus.py:481. Because


```
sage: ZZ.has_coerce_map_from(long)
True
sage: SR.has_coerce_map_from(ZZ)
True
```


This should be handled in the new model, but symbolics are being changed anyways. 


---

Attachment


---

Comment by mabshoff created at 2008-09-23 01:17:34

Looks good to me. Assuming this passes doctests positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-23 01:51:33

Merged in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-23 01:51:33

Resolution: fixed
