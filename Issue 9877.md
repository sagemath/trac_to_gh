# Issue 9877: symbolic zeta(1) should return unsigned infinity

Issue created by migration from https://trac.sagemath.org/ticket/9878

Original creator: burcin

Original creation time: 2010-09-09 08:19:55

Assignee: burcin

Keywords: pynac

After exposing the symbolic zeta function at the top level in #8864, we get:


```
sage: zeta(1)
zeta(1)
```


We should return unsigned infinity in this case.

See also #5739.


---

Attachment

With the new pynac package at #9201, we have:


```
sage: zeta(1)
Infinity
```


attachment:trac_9878-zeta_infinity.patch adds doctests for this change.

The pynac package includes patches for #9394, #9834, #9879, #9881, #9900 as well as this ticket. See the ticket description of #9901 for the list (and order) of patches associated to the new version.


---

Comment by burcin created at 2010-09-12 12:15:07

Changing status from new to needs_review.


---

Comment by burcin created at 2010-09-12 12:26:33

Replying to [comment:1 burcin]:
> With the new pynac package at #9201, we have:

at #9901. Sorry for the noise.


---

Comment by kcrisman created at 2010-09-22 18:00:28

With #9901, positive review.  Do not merge until #9901 also has positive review and is merged.


---

Comment by kcrisman created at 2010-09-22 18:00:28

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-10-06 03:20:07

Resolution: fixed
