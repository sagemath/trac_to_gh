# Issue 3469: Something funny with free modules

archive/issues_003469.json:
```json
{
    "body": "Assignee: was\n\nCC:  jason\n\n\n```\nsage: W = (ZZ^2).span([(1/2,1/2), (0,1)]); W\nFree module of degree 2 and rank 2 over Integer Ring\nEchelon basis matrix:\n[1/2 1/2]\n[  0   1]\nsage: V = (ZZ^2).span([(1/2,1/2), (0,2)]); V\nFree module of degree 2 and rank 2 over Integer Ring\nEchelon basis matrix:\n[1/2 1/2]\n[  0   2]\nsage: W(V.gen(0))\nTraceback (most recent call last):\n...\nTypeError: no coercion of this rational to integer\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3469\n\n",
    "created_at": "2008-06-19T07:29:53Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Something funny with free modules",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3469",
    "user": "robertwb"
}
```
Assignee: was

CC:  jason


```
sage: W = (ZZ^2).span([(1/2,1/2), (0,1)]); W
Free module of degree 2 and rank 2 over Integer Ring
Echelon basis matrix:
[1/2 1/2]
[  0   1]
sage: V = (ZZ^2).span([(1/2,1/2), (0,2)]); V
Free module of degree 2 and rank 2 over Integer Ring
Echelon basis matrix:
[1/2 1/2]
[  0   2]
sage: W(V.gen(0))
Traceback (most recent call last):
...
TypeError: no coercion of this rational to integer
```


Issue created by migration from https://trac.sagemath.org/ticket/3469





---

archive/issue_comments_024461.json:
```json
{
    "body": "Also\n\n```\nsage: type(V.gen())\n<type 'sage.modules.vector_rational_dense.Vector_rational_dense'>\nsage: type(V([1,2]))\n<type 'sage.modules.vector_integer_dense.Vector_integer_dense'>\n```\n",
    "created_at": "2008-06-19T07:38:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3469#issuecomment-24461",
    "user": "robertwb"
}
```

Also

```
sage: type(V.gen())
<type 'sage.modules.vector_rational_dense.Vector_rational_dense'>
sage: type(V([1,2]))
<type 'sage.modules.vector_integer_dense.Vector_integer_dense'>
```




---

archive/issue_comments_024462.json:
```json
{
    "body": "This seems to be the real issue: \n\n```\nsage: V([1/2,1/2])\nTraceback (most recent call last):\n...\nTypeError: no coercion of this rational to integer\n```\n",
    "created_at": "2008-06-19T07:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3469#issuecomment-24462",
    "user": "robertwb"
}
```

This seems to be the real issue: 

```
sage: V([1/2,1/2])
Traceback (most recent call last):
...
TypeError: no coercion of this rational to integer
```




---

archive/issue_comments_024463.json:
```json
{
    "body": "Seems to work now.",
    "created_at": "2010-01-18T05:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3469#issuecomment-24463",
    "user": "boothby"
}
```

Seems to work now.



---

archive/issue_comments_024464.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-01-18T05:00:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3469#issuecomment-24464",
    "user": "boothby"
}
```

Resolution: worksforme
