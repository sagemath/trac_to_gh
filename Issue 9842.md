# Issue 9842: modular/overconvergent/weightspace.py uses Maxima because of symbolic variables

Issue created by migration from https://trac.sagemath.org/ticket/9843

Original creator: AlexGhitza

Original creation time: 2010-08-31 22:09:56

Assignee: craigcitro

CC:  davidloeffler

This is in the top-level docstring of the file:


```
sage: L = Qp(17).extension(x^2 - 17, names='a'); L.rename('L')
sage: 
Exiting Sage (CPU time 0m0.94s, Wall time 0m25.72s).
Exiting spawned Maxima process.
```


Patch on its way.


---

Comment by AlexGhitza created at 2010-08-31 22:14:16

OK, I have a patch but I'm getting a trac error when trying to attach it (no space left on device).


---

Comment by mhansen created at 2010-08-31 23:08:43

Test post.


---

Comment by AlexGhitza created at 2010-09-01 02:43:28

Changing priority from major to minor.


---

Attachment


---

Comment by AlexGhitza created at 2010-09-01 02:43:28

Changing status from new to needs_review.


---

Comment by davidloeffler created at 2010-09-22 09:01:43

Looks fine to me.


---

Comment by davidloeffler created at 2010-09-22 09:01:43

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 09:11:55

Resolution: fixed
