# Issue 3085: [with patch, needs *really* easy review] identity matrix docs

archive/issues_003085.json:
```json
{
    "body": "Assignee: was\n\nThe docs for identity matrix contain a \"\\t\", so the string should be a raw string so \\t doesn't expand to a tab.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3085\n\n",
    "created_at": "2008-05-02T22:08:38Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs *really* easy review] identity matrix docs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3085",
    "user": "jason"
}
```
Assignee: was

The docs for identity matrix contain a "\t", so the string should be a raw string so \t doesn't expand to a tab.

Issue created by migration from https://trac.sagemath.org/ticket/3085





---

archive/issue_comments_021302.json:
```json
{
    "body": "Attachment [identity-matrix.patch](tarball://root/attachments/some-uuid/ticket3085/identity-matrix.patch) by jason created at 2008-05-02 22:09:00",
    "created_at": "2008-05-02T22:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3085#issuecomment-21302",
    "user": "jason"
}
```

Attachment [identity-matrix.patch](tarball://root/attachments/some-uuid/ticket3085/identity-matrix.patch) by jason created at 2008-05-02 22:09:00



---

archive/issue_comments_021303.json:
```json
{
    "body": "Credit goes to Geoff Tims for reporting this.",
    "created_at": "2008-05-02T22:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3085#issuecomment-21303",
    "user": "jason"
}
```

Credit goes to Geoff Tims for reporting this.



---

archive/issue_comments_021304.json:
```json
{
    "body": "uh, in the interest of full disclosure, I didn't doctest this, but I did sage -br and check the docs to make sure they look better.",
    "created_at": "2008-05-02T22:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3085#issuecomment-21304",
    "user": "jason"
}
```

uh, in the interest of full disclosure, I didn't doctest this, but I did sage -br and check the docs to make sure they look better.



---

archive/issue_comments_021305.json:
```json
{
    "body": "After looking at the patch I am convinced it will not harm anybody when we merge this in 3.0.1.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-03T04:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3085#issuecomment-21305",
    "user": "mabshoff"
}
```

After looking at the patch I am convinced it will not harm anybody when we merge this in 3.0.1.

Cheers,

Michael



---

archive/issue_comments_021306.json:
```json
{
    "body": "Merged in Sage 3.0.1.final",
    "created_at": "2008-05-03T13:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3085#issuecomment-21306",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.final



---

archive/issue_comments_021307.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-03T13:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3085#issuecomment-21307",
    "user": "mabshoff"
}
```

Resolution: fixed
