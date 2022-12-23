# Issue 5010: [with patch, needs review] Solaris 10: rings/real_double.pyx doctests failure: nan vs. NaN

archive/issues_005010.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe are seeing the following doctest failure:\n\n```\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-fulvia/devel/sage/sage/rings/real_double.pyx\", line 1311:\n    sage: RDF(0).log()\nExpected:\n    -inf\nGot:\n    -Infinity\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.3.final/sage-3.2.3.final-fulvia/devel/sage/sage/rings/real_double.pyx\", line 1313:\n    sage: RDF(-1).log()\nExpected:\n    nan\nGot:\n    -NaN\n```\n\nThis is because we are using the C library instead of RDF to create inf and nan.\n\nNote that this is a different issue than #672.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5010\n\n",
    "created_at": "2009-01-18T06:39:47Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Solaris 10: rings/real_double.pyx doctests failure: nan vs. NaN",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5010",
    "user": "mabshoff"
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

archive/issue_comments_038192.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-18T06:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5010#issuecomment-38192",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_038193.json:
```json
{
    "body": "This looks good.",
    "created_at": "2009-01-18T12:35:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5010#issuecomment-38193",
    "user": "craigcitro"
}
```

This looks good.



---

archive/issue_comments_038194.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T13:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5010#issuecomment-38194",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038195.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-18T13:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5010",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5010#issuecomment-38195",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0
