# Issue 1106: speed up dense matrix comparison

Issue created by migration from https://trac.sagemath.org/ticket/1106

Original creator: malb

Original creation time: 2007-11-05 12:22:36

Assignee: was

The general implementation right now is:

```
cdef int _cmp_c_impl(self, Element right) except -2:
    return cmp(self._list(), right._list())
```

which has a huge memory overhead. This should be optimised. Also, Matrix_modn_dense should have a faster special cmp method.


---

Attachment


---

Comment by mhansen created at 2007-12-22 17:39:06

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-22 17:39:06

Changing assignee from was to mhansen.


---

Comment by rlm created at 2007-12-22 18:08:35

merged in 2.9.1 rc0


---

Comment by rlm created at 2007-12-22 18:08:35

Resolution: fixed
