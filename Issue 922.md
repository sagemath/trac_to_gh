# Issue 922: bug in prime_powers

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-18 18:35:31

Assignee: somebody

Inconsistent types:


```
sage: vv = prime_powers(10)
sage: type(vv[0])
<type 'int'>
sage: type(vv[1])
<type 'sage.rings.integer.Integer'>
```


Freebie for bug day on Saturday :-)


---

Comment by robertwb created at 2007-10-20 19:21:49

Changing status from new to assigned.


---

Comment by robertwb created at 2007-10-20 19:21:49

Changing assignee from somebody to robertwb.


---

Attachment


---

Comment by was created at 2007-10-21 00:55:34

Resolution: fixed
