# Issue 5369: [with patch, needs review] Optimize transpose for matrix_integer_dense and matrix_rational_dense

Issue created by migration from https://trac.sagemath.org/ticket/5369

Original creator: ylchapuy

Original creation time: 2009-02-25 10:00:02

Assignee: was

CC:  rbeezer

Keywords: transpose

matrix_integer_dense and matrix_rational_dense don't have any optimize transpose functions, so add it.


---

Attachment

I did only one ticket for both as they are both gmp based.

I mostly copied the logic used in the __copy__ function (by the way I also simplified the __copy__ function in matrix_rational_dense.pyx)

timings (wall time) for

```
m=identity_matrix(3000);
time m2=m.transpose(); m3=m.antitranspose();
```

* sage 3-3: 15.44
* with #5345: 3.38
* with this patch: 2.01


---

Attachment

Looks good.  I updated the patch to the new docstring format in 3.4.

Apply only trac-5369-transpose-gmp-matrix.2.patch


---

Comment by mabshoff created at 2009-02-28 21:04:29

Resolution: fixed


---

Comment by mabshoff created at 2009-02-28 21:04:29

Merged trac-5369-transpose-gmp-matrix.2.patch in Sage 3.4.rc0.

Cheers,

Michael
