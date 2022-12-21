# Issue 1494: bug coercing from maximal order of cyclotomic field into cyclotomic field

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-13 22:08:23

Assignee: somebody


```
sage: K.<z> = CyclotomicField(7)
sage: O = K.maximal_order()
sage: K(O.1)
Traceback (most recent call last):
...
TypeError: Cannot coerce element into this number field
```



---

Attachment


---

Comment by robertwb created at 2007-12-15 07:47:04

I am wary of this patch, but will look into it more.


---

Attachment


---

Comment by cwitty created at 2007-12-15 08:17:56

Looks OK to me.  The new doctest passes (after applying the trivial patch in trac-1494-fixdoctest.patch).


---

Comment by robertwb created at 2007-12-15 08:39:41

I was worried if there was some special reason we were calling _coerce_from_other_number_field here previously, but it looks OK. 

This will probably be revised when coercion is flushed throughout the system anyways.


---

Comment by mabshoff created at 2007-12-15 09:42:45

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 09:42:45

Resolution: fixed
