# Issue 1605: conversion of sage vectors to magma vectors not implemented.

Issue created by migration from https://trac.sagemath.org/ticket/1605

Original creator: was

Original creation time: 2007-12-27 02:45:23

Assignee: was


```
sage: v = vector([1,2,3])
sage: magma(v)
boom ...

IN:_sage_[2] := (1, 2, 3);
OUT:
>> _sage_[2] := (1, 2, 3);
                ^
Runtime error in elt< ... >: No permutation group context in which to create cycle

```



---

Attachment

add support for converting vectors to magma


---

Comment by burcin created at 2008-05-12 15:14:17

Changing assignee from was to burcin.


---

Comment by burcin created at 2008-05-12 15:14:17

attachment:1605-sage_vectors_to_magma.patch adds support for converting vectors to Magma.


---

Comment by burcin created at 2008-05-12 15:14:17

Changing status from new to assigned.


---

Comment by mhansen created at 2008-05-24 21:17:46

Looks good to me.


---

Comment by mabshoff created at 2008-05-25 04:11:58

Merged in Sage 3.0.3.alpha0


---

Comment by mabshoff created at 2008-05-25 04:11:58

Resolution: fixed
