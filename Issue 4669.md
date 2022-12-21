# Issue 4669: CDF matrices need complex doctests (see matrix/matrix_complex_double_dense.pyx)

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-12-01 15:31:59

Assignee: was


```
> What is really confusing me is that the docstring for
> matrix_complex_double_dense.pyx
> (presumably *complex* matrices) is more or less the same as the docstring for
> matrix_real_double_dense.pyx at
> http://www.sagemath.org/hg/sage-main/file/8b1d19463fc4/sage/matrix/matrix_real_double_dense.pyx
> In other words, there are no examples of *complex* matrices in the
> docstring for
> matrix_complex_double_dense.pyx, which seems odd.
```




---

Comment by jason created at 2008-12-01 16:04:32

Changing status from new to assigned.


---

Comment by jason created at 2008-12-01 16:04:32

Changing assignee from was to jason.


---

Attachment


---

Comment by was created at 2008-12-06 22:13:06

THANKS!!


---

Comment by mabshoff created at 2008-12-07 09:59:42

Merged in Sage 3.2.2.alpha1


---

Comment by mabshoff created at 2008-12-07 09:59:42

Resolution: fixed
