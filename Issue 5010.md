# Issue 5010: [with patch, needs review] Solaris 10: rings/real_double.pyx doctests failure: nan vs. NaN

archive/issues_005010.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe are seeing the following doctest failure:\n\n```\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-fulvia/devel/sage/sage/rings/real_double.pyx\", line 1311:\n    sage: RDF(0).log()\nExpected:\n    -inf\nGot:\n    -Infinity\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-fulvia/devel/sage/sage/rings/real_double.pyx\", line 1313:\n    sage: RDF(-1).log()\nExpected:\n    nan\nGot:\n    -NaN\n```\nThis is because we are using the C library instead of RDF to create inf and nan.\n\nNote that this is a different issue than #672.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5010\n\n",
    "created_at": "2009-01-18T06:39:47Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] Solaris 10: rings/real_double.pyx doctests failure: nan vs. NaN",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

We are seeing the following doctest failure:

```
**********************************************************************
File "/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-fulvia/devel/sage/sage/rings/real_double.pyx", line 1311:
    sage: RDF(0).log()
Expected:
    -inf
Got:
    -Infinity
**********************************************************************
File "/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-fulvia/devel/sage/sage/rings/real_double.pyx", line 1313:
    sage: RDF(-1).log()
Expected:
    nan
Got:
    -NaN
```
This is because we are using the C library instead of RDF to create inf and nan.

Note that this is a different issue than #672.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5010





---

archive/issue_comments_038120.json:
```json
{
    "body": "Attachment [trac_5010_real_double_NaN.patch](tarball://root/attachments/some-uuid/ticket5010/trac_5010_real_double_NaN.patch) by mabshoff created at 2009-01-18 06:43:07",
    "created_at": "2009-01-18T06:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5010#issuecomment-38120",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5010_real_double_NaN.patch](tarball://root/attachments/some-uuid/ticket5010/trac_5010_real_double_NaN.patch) by mabshoff created at 2009-01-18 06:43:07



---

archive/issue_comments_038121.json:
```json
{
    "body": "This looks good.",
    "created_at": "2009-01-18T12:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5010#issuecomment-38121",
    "user": "https://github.com/craigcitro"
}
```

This looks good.



---

archive/issue_comments_038122.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T13:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5010#issuecomment-38122",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011577.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-18T13:57:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5010",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5010#event-11577"
}
```



---

archive/issue_comments_038123.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-18T13:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5010#issuecomment-38123",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0
