# Issue 5354: [with patch, needs review] stop paying attention to <stdlib.h> RAND_MAX (should fix problems on Solaris)

archive/issues_005354.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe randstate framework always provides 31-bit random numbers regardless of platform, so RAND_MAX should be ignored.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5354\n\n",
    "created_at": "2009-02-24T02:21:00Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] stop paying attention to <stdlib.h> RAND_MAX (should fix problems on Solaris)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5354",
    "user": "cwitty"
}
```
Assignee: mabshoff

The randstate framework always provides 31-bit random numbers regardless of platform, so RAND_MAX should be ignored.

Issue created by migration from https://trac.sagemath.org/ticket/5354





---

archive/issue_comments_041252.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-02-24T02:21:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5354#issuecomment-41252",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_041253.json:
```json
{
    "body": "Nice. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T07:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5354#issuecomment-41253",
    "user": "mabshoff"
}
```

Nice. Positive review.

Cheers,

Michael



---

archive/issue_comments_041254.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T19:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5354#issuecomment-41254",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041255.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T19:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5354#issuecomment-41255",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael
