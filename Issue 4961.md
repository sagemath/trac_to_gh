# Issue 4961: sage/modules/vector_modn_sparse_c.pxi: allocate_c_vector_modint can leak memory in case of failure

Issue created by migration from https://trac.sagemath.org/ticket/4961

Original creator: mabshoff

Original creation time: 2009-01-10 09:55:59

Assignee: craigcitro

Look at

```
cdef int allocate_c_vector_modint(c_vector_modint* v, Py_ssize_t num_nonzero) except -1:
    """
    Allocate memory for a c_vector_modint -- most user code won't call this.
    """
    v.entries = <int*>sage_malloc(num_nonzero*sizeof(int))
    if v.entries == NULL:
        raise MemoryError, "Error allocating memory"
    v.positions = <Py_ssize_t*>sage_malloc(num_nonzero*sizeof(Py_ssize_t))
    if v.positions == NULL:
        raise MemoryError, "Error allocating memory"
    return 0
```


When the allocation for positions fails we will leak entries.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-01-23 16:20:24

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-24 13:17:21

Resolution: fixed


---

Comment by mabshoff created at 2009-01-24 13:17:21

Merged in Sage 3.3.alpha2
