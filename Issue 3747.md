# Issue 3747: incorrect power in modular arithmetic

archive/issues_003747.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R = Integers(17^5)\nsage: R(17)^5\n1419857\n```\n\n\nThe answer should be zero.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3747\n\n",
    "created_at": "2008-07-30T14:14:21Z",
    "labels": [
        "basic arithmetic",
        "blocker",
        "bug"
    ],
    "title": "incorrect power in modular arithmetic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3747",
    "user": "dmharvey"
}
```
Assignee: somebody


```
sage: R = Integers(17^5)
sage: R(17)^5
1419857
```


The answer should be zero.


Issue created by migration from https://trac.sagemath.org/ticket/3747





---

archive/issue_comments_026614.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-07-30T14:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3747#issuecomment-26614",
    "user": "dmharvey"
}
```

Attachment



---

archive/issue_comments_026615.json:
```json
{
    "body": "looks good!",
    "created_at": "2008-07-30T14:37:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3747#issuecomment-26615",
    "user": "was"
}
```

looks good!



---

archive/issue_comments_026616.json:
```json
{
    "body": "Looks good to me too.  I note that only the 32-bit code had this bug, not the 64-bit code.",
    "created_at": "2008-07-30T23:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3747#issuecomment-26616",
    "user": "cremona"
}
```

Looks good to me too.  I note that only the 32-bit code had this bug, not the 64-bit code.



---

archive/issue_comments_026617.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-30T23:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3747#issuecomment-26617",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026618.json:
```json
{
    "body": "Merged in Sage 3.1.alpha0",
    "created_at": "2008-07-30T23:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3747",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3747#issuecomment-26618",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha0
