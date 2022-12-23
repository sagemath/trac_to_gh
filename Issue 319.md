# Issue 319: can't divide matrix over QQ by a rational

archive/issues_000319.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: Matrix(QQ, 2, 2, [1, 1, 1, 1]) / 2\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/dmharvey/sage-2.2/<ipython console> in <module>()\n\n/home/dmharvey/sage-2.2/element.pyx in element.RingElement.__div__()\n\n/home/dmharvey/sage-2.2/element.pyx in element.bin_op_c()\n\n<type 'exceptions.TypeError'>: unsupported operand parent(s) for '/': 'Full MatrixSpace of 2 by 2 dense matrices over Rational Field' and 'Integer Ring'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/319\n\n",
    "created_at": "2007-03-12T05:16:04Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "can't divide matrix over QQ by a rational",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/319",
    "user": "dmharvey"
}
```
Assignee: somebody


```
sage: Matrix(QQ, 2, 2, [1, 1, 1, 1]) / 2
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/dmharvey/sage-2.2/<ipython console> in <module>()

/home/dmharvey/sage-2.2/element.pyx in element.RingElement.__div__()

/home/dmharvey/sage-2.2/element.pyx in element.bin_op_c()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '/': 'Full MatrixSpace of 2 by 2 dense matrices over Rational Field' and 'Integer Ring'
```



Issue created by migration from https://trac.sagemath.org/ticket/319





---

archive/issue_comments_001519.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T17:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/319#issuecomment-1519",
    "user": "dmharvey"
}
```

Resolution: fixed



---

archive/issue_comments_001520.json:
```json
{
    "body": "this is apparently fixed at least as of 2.8",
    "created_at": "2007-08-18T17:13:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/319",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/319#issuecomment-1520",
    "user": "dmharvey"
}
```

this is apparently fixed at least as of 2.8
