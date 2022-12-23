# Issue 3169: matrix augment and stack should take vectors

archive/issues_003169.json:
```json
{
    "body": "Assignee: was\n\nCC:  slelievre\n\nIt would be nice if these worked:\n\n\n```\nsage: m=matrix(3,range(9))\nsage: v=vector([-1,-2,-3])\nsage: m.augment(v)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/grout/<ipython console> in <module>()\n\n/home/grout/matrix1.pyx in sage.matrix.matrix1.Matrix.augment (sage/matrix/matrix1.c:7099)()\n\n<type 'exceptions.TypeError'>: Argument 'other' has incorrect type (expected sage.matrix.matrix1.Matrix, got sage.modules.vector_integer_dense.Vector_integer_dense)\nsage: m.stack(v)\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/home/grout/<ipython console> in <module>()\n\n/home/grout/matrix_integer_dense.pyx in sage.matrix.matrix_integer_dense.Matrix_integer_dense.stack (sage/matrix/matrix_integer_dense.c:24661)()\n\n<type 'exceptions.AttributeError'>: 'sage.modules.vector_integer_dense.Vector_integer_d' object has no attribute 'ncols'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3169\n\n",
    "created_at": "2008-05-12T22:21:56Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "title": "matrix augment and stack should take vectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3169",
    "user": "jason"
}
```
Assignee: was

CC:  slelievre

It would be nice if these worked:


```
sage: m=matrix(3,range(9))
sage: v=vector([-1,-2,-3])
sage: m.augment(v)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/matrix1.pyx in sage.matrix.matrix1.Matrix.augment (sage/matrix/matrix1.c:7099)()

<type 'exceptions.TypeError'>: Argument 'other' has incorrect type (expected sage.matrix.matrix1.Matrix, got sage.modules.vector_integer_dense.Vector_integer_dense)
sage: m.stack(v)
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/matrix_integer_dense.pyx in sage.matrix.matrix_integer_dense.Matrix_integer_dense.stack (sage/matrix/matrix_integer_dense.c:24661)()

<type 'exceptions.AttributeError'>: 'sage.modules.vector_integer_dense.Vector_integer_d' object has no attribute 'ncols'
```


Issue created by migration from https://trac.sagemath.org/ticket/3169





---

archive/issue_comments_021959.json:
```json
{
    "body": "Attachment",
    "created_at": "2013-08-13T15:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3169#issuecomment-21959",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_021960.json:
```json
{
    "body": "Implemented in #10424 and #10974.\n\nThe following now works, making this ticket obsolete.\n\n```\nsage: m = matrix(3, range(9))\nsage: m\n[0 1 2]\n[3 4 5]\n[6 7 8]\nsage: v = vector([-1, -2, -3])\nsage: m.augment(v)\n[ 0  1  2 -1]\n[ 3  4  5 -2]\n[ 6  7  8 -3]\nsage: m.stack(v)\n[ 0  1  2]\n[ 3  4  5]\n[ 6  7  8]\n[-1 -2 -3]\n```\n\n\nI am marking this ticket as duplicate/invalid/wontfix.",
    "created_at": "2018-04-20T14:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3169#issuecomment-21960",
    "user": "slelievre"
}
```

Implemented in #10424 and #10974.

The following now works, making this ticket obsolete.

```
sage: m = matrix(3, range(9))
sage: m
[0 1 2]
[3 4 5]
[6 7 8]
sage: v = vector([-1, -2, -3])
sage: m.augment(v)
[ 0  1  2 -1]
[ 3  4  5 -2]
[ 6  7  8 -3]
sage: m.stack(v)
[ 0  1  2]
[ 3  4  5]
[ 6  7  8]
[-1 -2 -3]
```


I am marking this ticket as duplicate/invalid/wontfix.



---

archive/issue_comments_021961.json:
```json
{
    "body": "Changing keywords from \"\" to \"augment\".",
    "created_at": "2018-04-20T14:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3169#issuecomment-21961",
    "user": "slelievre"
}
```

Changing keywords from "" to "augment".



---

archive/issue_comments_021962.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2018-04-20T14:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3169#issuecomment-21962",
    "user": "slelievre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_021963.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-04-21T04:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3169#issuecomment-21963",
    "user": "tscrim"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_021964.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3169#issuecomment-21964",
    "user": "vdelecroix"
}
```

Resolution: wontfix



---

archive/issue_comments_021965.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3169",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3169#issuecomment-21965",
    "user": "vdelecroix"
}
```

closing positively reviewed duplicates
