# Issue 2273: matrix exponentials

archive/issues_002273.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout\n\nRight now, thanks to #2049, we can (have Maxima) compute the exponential of a symbolic matrix:\n\n\n```\nsage: var('t')\nsage: A = Matrix(SR, [[t, 0], [0, t]])\nsage: A.exp()\n[e^t   0]\n[  0 e^t]\n```\n\n\nThis is great, but it would also be nice to have this for numerical matrices.  On a related note, the following is perplexing (to me):\n\n\n```\nsage: A=Matrix(RDF,[[1,-2],[2,-1]])\nsage: exp(A)\n...\n<type 'exceptions.TypeError'>: cannot coerce type '<type 'sage.matrix.matrix_real_double_dense.Matrix_real_double_dense'>' into a SymbolicExpression.\nsage: exp(1.0*A)\n...\n<type 'exceptions.TypeError'>: cannot coerce type '<type 'sage.matrix.matrix_real_double_dense.Matrix_real_double_dense'>' into a SymbolicExpression.\nsage: exp(pi/(3*sqrt(3))*A)\n[ 1 -1]\n[ 1  0]\n```\n\n\nYes folks, the last one works (and gives the right answer, btw).  Weird.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2273\n\n",
    "created_at": "2008-02-23T01:46:16Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "matrix exponentials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2273",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

CC:  @jasongrout

Right now, thanks to #2049, we can (have Maxima) compute the exponential of a symbolic matrix:


```
sage: var('t')
sage: A = Matrix(SR, [[t, 0], [0, t]])
sage: A.exp()
[e^t   0]
[  0 e^t]
```


This is great, but it would also be nice to have this for numerical matrices.  On a related note, the following is perplexing (to me):


```
sage: A=Matrix(RDF,[[1,-2],[2,-1]])
sage: exp(A)
...
<type 'exceptions.TypeError'>: cannot coerce type '<type 'sage.matrix.matrix_real_double_dense.Matrix_real_double_dense'>' into a SymbolicExpression.
sage: exp(1.0*A)
...
<type 'exceptions.TypeError'>: cannot coerce type '<type 'sage.matrix.matrix_real_double_dense.Matrix_real_double_dense'>' into a SymbolicExpression.
sage: exp(pi/(3*sqrt(3))*A)
[ 1 -1]
[ 1  0]
```


Yes folks, the last one works (and gives the right answer, btw).  Weird.


Issue created by migration from https://trac.sagemath.org/ticket/2273





---

archive/issue_comments_015039.json:
```json
{
    "body": "Now that we have the Jordan canonical form (#874) we could use it to compute the matrix exponential.",
    "created_at": "2008-02-28T20:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2273#issuecomment-15039",
    "user": "https://github.com/pdenapo"
}
```

Now that we have the Jordan canonical form (#874) we could use it to compute the matrix exponential.



---

archive/issue_comments_015040.json:
```json
{
    "body": "For implementing this using the Jordan canonical form, being able to compute that canonical form is not enough, we would need to compute the Jordan basis as well (see #2615)",
    "created_at": "2008-03-20T14:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2273#issuecomment-15040",
    "user": "https://github.com/pdenapo"
}
```

For implementing this using the Jordan canonical form, being able to compute that canonical form is not enough, we would need to compute the Jordan basis as well (see #2615)



---

archive/issue_comments_015041.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-07T04:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2273#issuecomment-15041",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015042.json:
```json
{
    "body": "#4733 implements this, though it could be done better, maybe, with the Jordan form code.",
    "created_at": "2008-12-07T04:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2273#issuecomment-15042",
    "user": "https://github.com/jasongrout"
}
```

#4733 implements this, though it could be done better, maybe, with the Jordan form code.



---

archive/issue_comments_015043.json:
```json
{
    "body": "Changing assignee from @williamstein to @jasongrout.",
    "created_at": "2008-12-07T04:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2273#issuecomment-15043",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @williamstein to @jasongrout.



---

archive/issue_comments_015044.json:
```json
{
    "body": "I agree that this is a duplicate of #4733 and since there is a patch there I am closing this as a dupe.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-07T04:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2273#issuecomment-15044",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I agree that this is a duplicate of #4733 and since there is a patch there I am closing this as a dupe.

Cheers,

Michael



---

archive/issue_comments_015045.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-12-07T04:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2273",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2273#issuecomment-15045",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: duplicate
