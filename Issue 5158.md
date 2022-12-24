# Issue 5158: [with patch, needs review] bug in symbolic factorial

archive/issues_005158.json:
```json
{
    "body": "Assignee: whuss\n\n\n```\nsage: factorial(x)^2\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n...\n\nTypeError: unable to make sense of Maxima expression 'x!^2' in Sage\n```\n\n\nThe attached patch fixes this.\n\nCheers,\n\nWilfried\n\nIssue created by migration from https://trac.sagemath.org/ticket/5158\n\n",
    "created_at": "2009-02-02T13:52:16Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs review] bug in symbolic factorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5158",
    "user": "whuss"
}
```
Assignee: whuss


```
sage: factorial(x)^2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

...

TypeError: unable to make sense of Maxima expression 'x!^2' in Sage
```


The attached patch fixes this.

Cheers,

Wilfried

Issue created by migration from https://trac.sagemath.org/ticket/5158





---

archive/issue_comments_039514.json:
```json
{
    "body": "Attachment [factorial_bug.patch](tarball://root/attachments/some-uuid/ticket5158/factorial_bug.patch) by mabshoff created at 2009-02-02 14:59:29",
    "created_at": "2009-02-02T14:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5158#issuecomment-39514",
    "user": "mabshoff"
}
```

Attachment [factorial_bug.patch](tarball://root/attachments/some-uuid/ticket5158/factorial_bug.patch) by mabshoff created at 2009-02-02 14:59:29



---

archive/issue_comments_039515.json:
```json
{
    "body": "Code looks good; doctests pass.\n\nPositive review.",
    "created_at": "2009-02-05T06:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5158#issuecomment-39515",
    "user": "cwitty"
}
```

Code looks good; doctests pass.

Positive review.



---

archive/issue_comments_039516.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-05T11:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5158#issuecomment-39516",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039517.json:
```json
{
    "body": "Merged in Sage 3.3.alpha6.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-05T11:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5158",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5158#issuecomment-39517",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha6.

Cheers,

Michael
