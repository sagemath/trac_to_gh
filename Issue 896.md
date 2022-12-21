# Issue 896: remove obsolte comment in matrix_modn_dense.pyx

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-10-14 14:15:59

Assignee: was

Around line 923:

```
    # TODO: TEMPORARILY DISABLED due to bug on 64-bit sage.math:
    #  A = matrix(Integers(389),4,range(16)); A._echelon_strassen(4)
    # *** glibc detected *** free(): invalid next size (fast): 0x0000000000fb15e0 ***
    # due to error in set_to memcpy on 64-bit
    cdef matrix_window_c(self, Py_ssize_t row, Py_ssize_t col,
                        Py_ssize_t nrows, Py_ssize_t ncols):
```

I ran 

```
A = matrix(Integers(389),4,range(16)); A._echelon_strassen(4)
```

under valgrind on sage.math and nothing turned up. So I believe this comment should be removed.

Cheers,

Michael


---

Attachment


---

Comment by was created at 2007-10-19 01:13:39

Thanks.  That bug was fixed about a year ago.  Good.


---

Comment by was created at 2007-10-19 01:14:18

Resolution: fixed
