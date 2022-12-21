# Issue 9783: list_plot should accept dictionaries

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2010-08-23 01:53:27

Assignee: jason, was

Keywords: list_plot, plotting, dictionaries

If I give the following dictionary to `list_plot`, it seems very obvious what I want it to do:

```
{67: 1770, 52: 2735, 37: 3135, 22: 3365, 72: 1560, 57: 2550, 42: 3020,
27: 3295, 62: 1960, 47: 2880}
```

...especially since list_plot plots functions with a finite domain, and dictionaries in Python are called "mapping types"! We should make `list_plot` be able to deal with dictionaries with numeric keys and values.


---

Attachment


---

Comment by ddrake created at 2010-08-24 07:02:48

Patch up, please review. One decision I'd like feedback on is sorting the resulting list -- I made it so that it only sorts the list when `plotjoined=True`, but maybe it would be fine to always sort the list?


---

Comment by ddrake created at 2010-08-24 07:02:48

Changing status from new to needs_review.


---

Comment by jason created at 2010-09-05 03:06:31

Changing status from needs_review to positive_review.


---

Comment by jason created at 2010-09-05 03:06:31

Looks good to me.  I agree with only sorting when plotjoined=True.


---

Comment by mpatel created at 2010-09-15 10:40:38

Resolution: fixed
