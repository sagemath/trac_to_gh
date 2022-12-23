# Issue 725: memleak in initialization of diagonal Matrix_integer_dense objects

Issue created by migration from https://trac.sagemath.org/ticket/725

Original creator: burcin

Original creation time: 2007-09-21 02:34:04

Assignee: was

For the diagonal case, the `__init__` function of `Matrix_integer_dense` contains the following code:


```
            self._zero_out_matrix()
            j = 0
            for i from 0 <= i < self._nrows:
                mpz_init_set(self._entries[j], x.value)
                j = j + self._nrows + 1
            self._initialized = True
```


as the _zero_out_matrix function calls mpz_init on self.entries, we should use mpz_set instead of mpz_init_set.

Attached patch fixes this.

The valgrind output of this error is similar to that of #621, but the example on that ticket uses a different code path. So this is not related.


---

Attachment


---

Comment by burcin created at 2007-09-21 02:36:24

Changing assignee from was to burcin.


---

Comment by burcin created at 2007-09-21 02:36:24

Changing status from new to assigned.


---

Comment by was created at 2007-09-21 02:45:27

great work!


---

Comment by was created at 2007-09-21 02:45:27

Resolution: fixed
