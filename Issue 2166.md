# Issue 2166: [with patch] Sage 2.10.2.alpha0: matrix/matrix_symbolic_dense.pyx doctest failure

Issue created by migration from https://trac.sagemath.org/ticket/2166

Original creator: mabshoff

Original creation time: 2008-02-15 00:11:39

Assignee: failure


```
sage -t  devel/sage-main/sage/matrix/matrix_symbolic_dense.pyx
**********************************************************************
File "matrix_symbolic_dense.pyx", line 177:
    sage: hash(m)
Expected:
    1653238849131003967
Got:
    -8735270519673468630
**********************************************************************
File "matrix_symbolic_dense.pyx", line 180:
    sage: m.__hash__()
Expected:
    1653238849131003967
Got:
    -8735270519673468630
**********************************************************************
File "matrix_symbolic_dense.pyx", line 183:
    sage: hash(maxima(m))
Expected:
    1653238849131003967
Got:
    -8735270519673468630
**********************************************************************
1 items had failures:
   3 of   4 in __main__.example_10
***Test Failed*** 3 failures.
For whitespace errors, see the file .doctest_matrix_symbolic_dense.pyx
         [16.6 s]
exit code: 256

----------------------------------------------------------------------
```



---

Attachment

Looks good to me.


---

Comment by mabshoff created at 2008-02-15 00:25:38

Resolution: fixed


---

Comment by mabshoff created at 2008-02-15 00:25:38

Merged in Sage 2.10.2.alpha0
