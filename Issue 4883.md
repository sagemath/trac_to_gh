# Issue 4883: possible memory leak in sage.matrix.matrix_integer_dense

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2008-12-27 00:52:38

Assignee: mabshoff


```
    def __dealloc__(self):
        """
        Frees all the memory allocated for this matrix. 
        EXAMPLE:
            sage: a = Matrix(ZZ,2,[1,2,3,4])
            sage: del a        
        """
        cdef Py_ssize_t i
        if self._initialized:
            for i from 0 <= i < (self._nrows * self._ncols):
                mpz_clear(self._entries[i])
            sage_free(self._entries)
            sage_free(self._matrix)
```


It is possible that `_initialized` is not set but `_matrix` and `_entries` are allocated.

Error paths in `__new__` and `__init__` should also be revised, since if one raises an error in these functions python still calls `__dealloc__` for the cleanup. 

From the `__init__` function:

```
        elif isinstance(entries, (int,long)) or is_Element(entries):
            try:
                x = ZZ(entries)
            except TypeError:
                self._initialized = False
                raise TypeError, "unable to coerce entry to an integer"
```



---

Comment by malb created at 2009-01-25 19:01:24

Changing status from new to assigned.


---

Comment by malb created at 2009-01-25 19:01:24

Changing assignee from mabshoff to malb.
