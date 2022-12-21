# Issue 4962: sage/modules/vector_modn_sparse_c.pxi: init_c_vector_modint leaks leak memory in case of OverflowError

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-10 10:01:20

Assignee: craigcitro

Look at:

```
cdef int init_c_vector_modint(c_vector_modint* v, int p, Py_ssize_t degree,
                              Py_ssize_t num_nonzero) except -1:
    """
    Initialize a c_vector_modint.
    """
    if (allocate_c_vector_modint(v, num_nonzero) == -1):
        raise MemoryError, "Error allocating memory for sparse vector."
    if p > 46340:
        raise OverflowError, "The prime must be <= 46340."
    v.num_nonzero = num_nonzero
    v.degree = degree
    v.p = p
    return 0
```

On OverflowError v is leaked. Switching check and allocation will fix the problem.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-01-23 16:19:35

Positive review even though the author did not fix it as I suggested :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 13:17:30

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 13:17:30

Resolution: fixed
