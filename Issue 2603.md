# Issue 2603: implement solution_space_right and solution_space_left for solving under-determined linear systems

Issue created by migration from https://trac.sagemath.org/ticket/2603

Original creator: ncalexan

Original creation time: 2008-03-19 19:33:02

Assignee: was

CC:  ncalexan

Keywords: linear system under determined solution space solve

With respect to #2581, which generalizes `solve_left` and `solve_right`, Nick Alexander asked:

Is there any hope for a `solution_space_right` that handles under-determined systems?

William Stein replied:

Not in this patch. Make a trac ticket and somebody will get to it.

It would be nice if this was gotten to :)

To be a little more clear, as of 2.10.4 the following does not work:


```
sage: sage: matrix(ZZ, 3, 1, [0, 1, 2]).solve_right(vector(ZZ, [3, 2, 1]))
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/Users/ncalexan/sage-2.10.3.rc3/devel/sage-gensolve/sage/schemes/hyperelliptic_curves/<ipython console> in <module>()

/Users/ncalexan/sage-2.10.3.rc3/devel/sage-gensolve/sage/schemes/hyperelliptic_curves/matrix_integer_dense.pyx in sage.matrix.matrix_integer_dense.Matrix_integer_dense.solve_right()

<type 'exceptions.ValueError'>: self must be of full rank.
```



---

Comment by was created at 2008-03-19 19:42:07

I don't even understand what you're asking for now!
I think #2581 resolves this problem:

```
sage: matrix(ZZ, 3, 1, [0, 1, 2]).solve_right(vector(ZZ, [3, 2, 1]))
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/matrix2.pyx in sage.matrix.matrix2.Matrix.solve_right()

/Users/was/matrix2.pyx in sage.matrix.matrix2.Matrix._solve_right_general()

<type 'exceptions.ValueError'>: matrix equation has no solutions
sage: matrix(ZZ, 3, 1, [6,4,2]).solve_right(vector(ZZ, [3, 2, 1]))
(1/2)
```


The exception above is *correct*.  

It's likely this ticket can be closed.


---

Comment by ncalexan created at 2008-03-19 19:49:11

I'm glad #2581 addresses that particular problem, but asking for a solution space for general matrix equations is still reasonable.  A trivial example might be


```
sage: zero_matrix(3, 2).solution_space_right(zero_matrix(3, 1))
```


which should yield a full matrix space (matrices of size 2 by 1).
