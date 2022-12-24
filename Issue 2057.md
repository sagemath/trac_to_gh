# Issue 2057: followup to #1983 -- 0^0 for 0 a rational

archive/issues_002057.json:
```json
{
    "body": "Assignee: somebody\n\nBefore patch:\n\n```\n\nsage: (0/1) ^ (0/1)\n\n---------------------------------------------------------------------------\n<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)\n\n/home/was/<ipython console> in <module>()\n\n/home/was/rational.pyx in sage.rings.rational.Rational.__pow__()\n\n<type 'exceptions.ArithmeticError'>: 0^0 is undefined.\n```\n\n\nAfter patch:\n\n```\nsage: (0/1) ^ (0/1)\n1\nsage: type(_)\n<type 'sage.rings.rational.Rational'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2057\n\n",
    "created_at": "2008-02-05T15:25:10Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "followup to #1983 -- 0^0 for 0 a rational",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2057",
    "user": "was"
}
```
Assignee: somebody

Before patch:

```

sage: (0/1) ^ (0/1)

---------------------------------------------------------------------------
<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)

/home/was/<ipython console> in <module>()

/home/was/rational.pyx in sage.rings.rational.Rational.__pow__()

<type 'exceptions.ArithmeticError'>: 0^0 is undefined.
```


After patch:

```
sage: (0/1) ^ (0/1)
1
sage: type(_)
<type 'sage.rings.rational.Rational'>
```


Issue created by migration from https://trac.sagemath.org/ticket/2057





---

archive/issue_comments_013314.json:
```json
{
    "body": "Attachment [trac-2057-zero_to_zero.patch](tarball://root/attachments/some-uuid/ticket2057/trac-2057-zero_to_zero.patch) by was created at 2008-02-05 15:27:42",
    "created_at": "2008-02-05T15:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2057#issuecomment-13314",
    "user": "was"
}
```

Attachment [trac-2057-zero_to_zero.patch](tarball://root/attachments/some-uuid/ticket2057/trac-2057-zero_to_zero.patch) by was created at 2008-02-05 15:27:42



---

archive/issue_comments_013315.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-02-06T04:03:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2057#issuecomment-13315",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_013316.json:
```json
{
    "body": "Merged in Sage 2.l0.2.alpha0",
    "created_at": "2008-02-07T05:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2057#issuecomment-13316",
    "user": "mabshoff"
}
```

Merged in Sage 2.l0.2.alpha0



---

archive/issue_comments_013317.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-07T05:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2057#issuecomment-13317",
    "user": "mabshoff"
}
```

Resolution: fixed
