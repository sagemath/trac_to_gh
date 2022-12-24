# Issue 5944: fix a nasty pynac bug in exp

archive/issues_005944.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @mwhansen\n\n\n```\nsage: t = var('t', ns=1)\nsage: a = (-2*t).exp(); a\ne^(-2*t)\nsage: b = (-t).exp(); b\ne^(-t)\nsage: a - b\n0\nsage: a\ne^(-t)\nsage: b\ne^(-t)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5944\n\n",
    "created_at": "2009-04-29T22:59:30Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "fix a nasty pynac bug in exp",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5944",
    "user": "@williamstein"
}
```
Assignee: @burcin

CC:  @mwhansen


```
sage: t = var('t', ns=1)
sage: a = (-2*t).exp(); a
e^(-2*t)
sage: b = (-t).exp(); b
e^(-t)
sage: a - b
0
sage: a
e^(-t)
sage: b
e^(-t)
```


Issue created by migration from https://trac.sagemath.org/ticket/5944





---

archive/issue_comments_046995.json:
```json
{
    "body": "add doctests for the fix",
    "created_at": "2009-05-05T23:20:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5944#issuecomment-46995",
    "user": "@burcin"
}
```

add doctests for the fix



---

archive/issue_comments_046996.json:
```json
{
    "body": "Attachment [trac_5944-doctest.patch](tarball://root/attachments/some-uuid/ticket5944/trac_5944-doctest.patch) by @burcin created at 2009-05-05 23:22:20\n\nThe package for pynac 0.1.6 at #5777 has a fix for this. Attached patch adds doctests.",
    "created_at": "2009-05-05T23:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5944#issuecomment-46996",
    "user": "@burcin"
}
```

Attachment [trac_5944-doctest.patch](tarball://root/attachments/some-uuid/ticket5944/trac_5944-doctest.patch) by @burcin created at 2009-05-05 23:22:20

The package for pynac 0.1.6 at #5777 has a fix for this. Attached patch adds doctests.



---

archive/issue_comments_046997.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-05T23:22:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5944#issuecomment-46997",
    "user": "@burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046998.json:
```json
{
    "body": "Positive review due to symbolics getting a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T23:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5944#issuecomment-46998",
    "user": "mabshoff"
}
```

Positive review due to symbolics getting a positive review.

Cheers,

Michael



---

archive/issue_comments_046999.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-20T23:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5944#issuecomment-46999",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_047000.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-20T23:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5944",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5944#issuecomment-47000",
    "user": "mabshoff"
}
```

Resolution: fixed
