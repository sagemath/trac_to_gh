# Issue 2167: Echelon form of symbolic matrices does not work

Issue created by migration from https://trac.sagemath.org/ticket/2167

Original creator: moretti

Original creation time: 2008-02-15 00:28:45

Assignee: was


```
You sage: M = Matrix([[1,0],[x,4]])
sage: M

[1 0]
[x 4]
sage: type(M)
<type 'sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense'>
sage: M.echelon_form()

[1 0]
[0 1]
```



---

Comment by moretti created at 2008-02-15 00:35:25

Resolution: invalid


---

Comment by moretti created at 2008-02-15 00:35:25

Sorry, I realized I was giving the wrong input. It appears to be implemented.
