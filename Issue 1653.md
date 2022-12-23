# Issue 1653: Bug raising an integer to a float  (probably really easy to fix in integer.pyx!)

archive/issues_001653.json:
```json
{
    "body": "Assignee: somebody\n\nThis is a bug:\n\n\n```\nsage: 2^float(3.1)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/integer.pyx in sage.rings.integer.Integer.__pow__()\n\n<type 'exceptions.TypeError'>: exponent (=3.1) must be an integer.\nCoerce your numbers to real or complex numbers first.\n\nNote:\nsage: int(2)^float(3.1)\n8.574187700290345\nsage: (2/1)^float(3.1)\n8.574187700290345\n```\n\n\nNote that\n\nIssue created by migration from https://trac.sagemath.org/ticket/1653\n\n",
    "created_at": "2008-01-02T06:29:41Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Bug raising an integer to a float  (probably really easy to fix in integer.pyx!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1653",
    "user": "was"
}
```
Assignee: somebody

This is a bug:


```
sage: 2^float(3.1)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/integer.pyx in sage.rings.integer.Integer.__pow__()

<type 'exceptions.TypeError'>: exponent (=3.1) must be an integer.
Coerce your numbers to real or complex numbers first.

Note:
sage: int(2)^float(3.1)
8.574187700290345
sage: (2/1)^float(3.1)
8.574187700290345
```


Note that

Issue created by migration from https://trac.sagemath.org/ticket/1653





---

archive/issue_comments_010523.json:
```json
{
    "body": "Changing assignee from somebody to dmharvey.",
    "created_at": "2008-01-02T18:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1653#issuecomment-10523",
    "user": "dmharvey"
}
```

Changing assignee from somebody to dmharvey.



---

archive/issue_comments_010524.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-02T18:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1653#issuecomment-10524",
    "user": "dmharvey"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010525.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-02T22:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1653#issuecomment-10525",
    "user": "dmharvey"
}
```

Attachment



---

archive/issue_comments_010526.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-20T03:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1653#issuecomment-10526",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010527.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha0",
    "created_at": "2008-01-20T03:16:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1653",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1653#issuecomment-10527",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha0
