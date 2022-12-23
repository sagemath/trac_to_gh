# Issue 4686: Documentation for eta products

Issue created by migration from https://trac.sagemath.org/ticket/4686

Original creator: davidloeffler

Original creation time: 2008-12-03 10:20:01

Assignee: davidloeffler

When I wrote the eta products code I didn't know how to add it to the reference manual. Here is the requisite patch, together with a patch to the code itself correcting LaTeX errors in the docstrings.


---

Attachment


---

Attachment

Here are two patches (one each for the hg_sage and hg_doc repositories).


---

Comment by davidloeffler created at 2008-12-03 10:23:12

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-03 10:26:13

Patch looks good to me. One tiny spelling issue I can take care when applying the patch:

```
Grobner basis
```

is missing an "e".

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-04 15:37:16

Merged both patches in Sage 3.2.2.alpha0


---

Comment by mabshoff created at 2008-12-04 15:37:16

Resolution: fixed
