# Issue 1502: calculus -- bug in argument ordering for formal functions

archive/issues_001502.json:
```json
{
    "body": "Assignee: was\n\nThis is wrong:\n\n\n```\nsage: f = function('Gamma', var('z'), var('w')); f\nGamma(z, w)\nsage: f(2)\nGamma(z, 2)\nsage: f(2,5)\nGamma(5, 2)\n```\n\n\nIt should be\n\n\n```\nsage: f = function('Gamma', var('z'), var('w')); f\nGamma(z, w)\nsage: f(2)\nGamma(2, w)\nsage: f(2,5)\nGamma(2, 5)\n```\n\n\nNote that this works:\n\n\n```\nsage: f(z,w) = function('Gamma'); f\n(z, w) |--> Gamma(z, w)\nsage: f(2)\nGamma(2, w)\nsage: f(2,5)\nGamma(2, 5)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1502\n\n",
    "created_at": "2007-12-14T05:41:19Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "calculus -- bug in argument ordering for formal functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1502",
    "user": "was"
}
```
Assignee: was

This is wrong:


```
sage: f = function('Gamma', var('z'), var('w')); f
Gamma(z, w)
sage: f(2)
Gamma(z, 2)
sage: f(2,5)
Gamma(5, 2)
```


It should be


```
sage: f = function('Gamma', var('z'), var('w')); f
Gamma(z, w)
sage: f(2)
Gamma(2, w)
sage: f(2,5)
Gamma(2, 5)
```


Note that this works:


```
sage: f(z,w) = function('Gamma'); f
(z, w) |--> Gamma(z, w)
sage: f(2)
Gamma(2, w)
sage: f(2,5)
Gamma(2, 5)
```


Issue created by migration from https://trac.sagemath.org/ticket/1502





---

archive/issue_comments_009627.json:
```json
{
    "body": "Attachment [1502.patch](tarball://root/attachments/some-uuid/ticket1502/1502.patch) by mhansen created at 2007-12-14 06:42:08",
    "created_at": "2007-12-14T06:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9627",
    "user": "mhansen"
}
```

Attachment [1502.patch](tarball://root/attachments/some-uuid/ticket1502/1502.patch) by mhansen created at 2007-12-14 06:42:08



---

archive/issue_comments_009628.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-14T06:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9628",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009629.json:
```json
{
    "body": "Apply after #553 .",
    "created_at": "2007-12-14T06:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9629",
    "user": "mhansen"
}
```

Apply after #553 .



---

archive/issue_comments_009630.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-12-14T06:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9630",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_009631.json:
```json
{
    "body": "Was reviewed this positively in IRC during BD7. \n\nCheers,\n\nMichael",
    "created_at": "2007-12-15T11:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9631",
    "user": "mabshoff"
}
```

Was reviewed this positively in IRC during BD7. 

Cheers,

Michael



---

archive/issue_comments_009632.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T11:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9632",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_009633.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T12:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9633",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009634.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T12:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1502",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1502#issuecomment-9634",
    "user": "mabshoff"
}
```

Merged in 2.9.rc0.
