# Issue 1040: bug in new ring extension constructor

archive/issues_001040.json:
```json
{
    "body": "Assignee: was\n\nNow that we allow notation such as\n\n```\nQQ[2^(1/3)]\n```\n\nto create a number field, the following is totally wrong and\nneeds to be fixed ASAP:\n\n\n```\nsage: K.<a> = QQ[2^(1/3)]\nsage: K\nUnivariate Polynomial Ring in a over Rational Field\nsage: parent(a)\nUnivariate Polynomial Ring in a over Rational Field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1040\n\n",
    "created_at": "2007-10-31T18:14:03Z",
    "labels": [
        "number theory",
        "critical",
        "bug"
    ],
    "title": "bug in new ring extension constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1040",
    "user": "was"
}
```
Assignee: was

Now that we allow notation such as

```
QQ[2^(1/3)]
```

to create a number field, the following is totally wrong and
needs to be fixed ASAP:


```
sage: K.<a> = QQ[2^(1/3)]
sage: K
Univariate Polynomial Ring in a over Rational Field
sage: parent(a)
Univariate Polynomial Ring in a over Rational Field
```


Issue created by migration from https://trac.sagemath.org/ticket/1040





---

archive/issue_comments_006342.json:
```json
{
    "body": "More:\n\nThis is because the preparser is written stupidly in this case:\n\n\n```\nsage: K.<a> = QQ[2^(1/3)]\nsage: preparse('K.<a> = QQ[2^(1/3)]')\n'K = QQ[\"a\"]; (a,) = K._first_ngens(Integer(1))'\n```\n\n\nI think this is what *should* happen:\n\n```\nsage: K.<a> = QQ[2^(1/3)]\nsage: preparse('K.<a> = QQ[2^(1/3)]')\n'K = QQ[\"2^(1/3)\"]; (a,) = K._first_ngens(Integer(1))'\n```\n\n\nThe previous behavior should only happen in the case when nothing is between brackets, as a sort of short cut:\n\n```\nsage: K.<a> = QQ[2^(1/3)]\nsage: preparse('K.<a> = QQ[]')\n'K = QQ[\"a\"]; (a,) = K._first_ngens(Integer(1))'\n```\n",
    "created_at": "2007-11-01T07:20:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1040#issuecomment-6342",
    "user": "was"
}
```

More:

This is because the preparser is written stupidly in this case:


```
sage: K.<a> = QQ[2^(1/3)]
sage: preparse('K.<a> = QQ[2^(1/3)]')
'K = QQ["a"]; (a,) = K._first_ngens(Integer(1))'
```


I think this is what *should* happen:

```
sage: K.<a> = QQ[2^(1/3)]
sage: preparse('K.<a> = QQ[2^(1/3)]')
'K = QQ["2^(1/3)"]; (a,) = K._first_ngens(Integer(1))'
```


The previous behavior should only happen in the case when nothing is between brackets, as a sort of short cut:

```
sage: K.<a> = QQ[2^(1/3)]
sage: preparse('K.<a> = QQ[]')
'K = QQ["a"]; (a,) = K._first_ngens(Integer(1))'
```




---

archive/issue_comments_006343.json:
```json
{
    "body": "Changing assignee from was to ncalexan.",
    "created_at": "2007-11-03T20:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1040#issuecomment-6343",
    "user": "ncalexan"
}
```

Changing assignee from was to ncalexan.



---

archive/issue_comments_006344.json:
```json
{
    "body": "Attachment [1040-ncalexan-2.hg](tarball://root/attachments/some-uuid/ticket1040/1040-ncalexan-2.hg) by ncalexan created at 2007-11-03 23:36:39",
    "created_at": "2007-11-03T23:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1040#issuecomment-6344",
    "user": "ncalexan"
}
```

Attachment [1040-ncalexan-2.hg](tarball://root/attachments/some-uuid/ticket1040/1040-ncalexan-2.hg) by ncalexan created at 2007-11-03 23:36:39



---

archive/issue_comments_006345.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-03T23:43:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1040",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1040#issuecomment-6345",
    "user": "was"
}
```

Resolution: fixed
