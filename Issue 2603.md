# Issue 2603: implement solution_space_right and solution_space_left for solving under-determined linear systems

archive/issues_002603.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan\n\nKeywords: linear system under determined solution space solve\n\nWith respect to #2581, which generalizes `solve_left` and `solve_right`, Nick Alexander asked:\n\nIs there any hope for a `solution_space_right` that handles under-determined systems?\n\nWilliam Stein replied:\n\nNot in this patch. Make a trac ticket and somebody will get to it.\n\nIt would be nice if this was gotten to :)\n\nTo be a little more clear, as of 2.10.4 the following does not work:\n\n```\nsage: sage: matrix(ZZ, 3, 1, [0, 1, 2]).solve_right(vector(ZZ, [3, 2, 1]))\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/Users/ncalexan/sage-2.10.3.rc3/devel/sage-gensolve/sage/schemes/hyperelliptic_curves/<ipython console> in <module>()\n\n/Users/ncalexan/sage-2.10.3.rc3/devel/sage-gensolve/sage/schemes/hyperelliptic_curves/matrix_integer_dense.pyx in sage.matrix.matrix_integer_dense.Matrix_integer_dense.solve_right()\n\n<type 'exceptions.ValueError'>: self must be of full rank.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2603\n\n",
    "created_at": "2008-03-19T19:33:02Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "implement solution_space_right and solution_space_left for solving under-determined linear systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2603",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @ncalexan

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

Issue created by migration from https://trac.sagemath.org/ticket/2603





---

archive/issue_comments_017769.json:
```json
{
    "body": "I don't even understand what you're asking for now!\nI think #2581 resolves this problem:\n\n```\nsage: matrix(ZZ, 3, 1, [0, 1, 2]).solve_right(vector(ZZ, [3, 2, 1]))\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/matrix2.pyx in sage.matrix.matrix2.Matrix.solve_right()\n\n/Users/was/matrix2.pyx in sage.matrix.matrix2.Matrix._solve_right_general()\n\n<type 'exceptions.ValueError'>: matrix equation has no solutions\nsage: matrix(ZZ, 3, 1, [6,4,2]).solve_right(vector(ZZ, [3, 2, 1]))\n(1/2)\n```\n\nThe exception above is *correct*.  \n\nIt's likely this ticket can be closed.",
    "created_at": "2008-03-19T19:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2603#issuecomment-17769",
    "user": "https://github.com/williamstein"
}
```

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

archive/issue_comments_017770.json:
```json
{
    "body": "I'm glad #2581 addresses that particular problem, but asking for a solution space for general matrix equations is still reasonable.  A trivial example might be\n\n```\nsage: zero_matrix(3, 2).solution_space_right(zero_matrix(3, 1))\n```\n\nwhich should yield a full matrix space (matrices of size 2 by 1).",
    "created_at": "2008-03-19T19:49:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2603",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2603#issuecomment-17770",
    "user": "https://github.com/ncalexan"
}
```

I'm glad #2581 addresses that particular problem, but asking for a solution space for general matrix equations is still reasonable.  A trivial example might be

```
sage: zero_matrix(3, 2).solution_space_right(zero_matrix(3, 1))
```

which should yield a full matrix space (matrices of size 2 by 1).
