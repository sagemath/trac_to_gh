# Issue 5183: issues with elementary_divisors for sparse integer matrices

archive/issues_005183.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @loefflerd\n\nKeywords: elementary_divisor, sparse, dense\n\nTwo things: \n\n1. the conventions for elementary_divisors are different in Pari's implementation (called in matrix_integer_dense.pyx) compared to the generic PID implementation (in matrix2.pyx):\n\n```\nsage: mat = matrix(ZZ, 3, 2, [1, 0, 0, 1, 0, 0], sparse=True)\nsage: mat.elementary_divisors()\n[1, 1]\nsage: mat.dense_matrix().elementary_divisors()\n[1, 1, 0]\n```\n\n\n2. if the elementary divisors of a sparse matrix are not all 0 or 1 (at least I think that's the issue), I get an error:\n\n```\nsage: mat = matrix(ZZ, 3, 2, range(6), sparse=True)\nsage: sage: mat.elementary_divisors()                    \n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n...\nTypeError: unable to coerce <class 'sage.rings.ideal.Ideal_pid'> to an integer\n```\n\nI get the same error for `mat.smith_form()`.  This is a problem with the Smith normal form stuff in matrix2.pyx, I think.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5183\n\n",
    "created_at": "2009-02-04T23:51:15Z",
    "labels": [
        "component: linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "issues with elementary_divisors for sparse integer matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5183",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @williamstein

CC:  @loefflerd

Keywords: elementary_divisor, sparse, dense

Two things: 

1. the conventions for elementary_divisors are different in Pari's implementation (called in matrix_integer_dense.pyx) compared to the generic PID implementation (in matrix2.pyx):

```
sage: mat = matrix(ZZ, 3, 2, [1, 0, 0, 1, 0, 0], sparse=True)
sage: mat.elementary_divisors()
[1, 1]
sage: mat.dense_matrix().elementary_divisors()
[1, 1, 0]
```


2. if the elementary divisors of a sparse matrix are not all 0 or 1 (at least I think that's the issue), I get an error:

```
sage: mat = matrix(ZZ, 3, 2, range(6), sparse=True)
sage: sage: mat.elementary_divisors()                    
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
...
TypeError: unable to coerce <class 'sage.rings.ideal.Ideal_pid'> to an integer
```

I get the same error for `mat.smith_form()`.  This is a problem with the Smith normal form stuff in matrix2.pyx, I think.


Issue created by migration from https://trac.sagemath.org/ticket/5183





---

archive/issue_comments_039670.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-02-20T00:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5183#issuecomment-39670",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: worksforme



---

archive/issue_comments_039671.json:
```json
{
    "body": "These two examples seem to work now, so I think we can close this.",
    "created_at": "2010-02-20T00:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5183#issuecomment-39671",
    "user": "https://github.com/jhpalmieri"
}
```

These two examples seem to work now, so I think we can close this.



---

archive/issue_events_005437.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2010-02-20T00:49:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5183",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5183#event-5437"
}
```
