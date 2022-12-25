# Issue 8021: ref manual for 4.3.1: error when building (Undefined control sequence \cross)

archive/issues_008021.json:
```json
{
    "body": "Assignee: mvngu\n\nIn several places in the Sage code, \"\\cross\" is used, and one of those instances causes an error when building the reference manual.  This is not a standard LaTeX command, and I think \"\\times\" is what is intended, so this patch makes that change.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8021\n\n",
    "closed_at": "2010-01-23T16:58:37Z",
    "created_at": "2010-01-21T06:26:45Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.2",
    "title": "ref manual for 4.3.1: error when building (Undefined control sequence \\cross)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8021",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: mvngu

In several places in the Sage code, "\cross" is used, and one of those instances causes an error when building the reference manual.  This is not a standard LaTeX command, and I think "\times" is what is intended, so this patch makes that change.

Issue created by migration from https://trac.sagemath.org/ticket/8021





---

archive/issue_comments_069965.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-21T06:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8021#issuecomment-69965",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069966.json:
```json
{
    "body": "Attachment [trac_8021-times.patch](tarball://root/attachments/some-uuid/ticket8021/trac_8021-times.patch) by @jhpalmieri created at 2010-01-21 06:30:23",
    "created_at": "2010-01-21T06:30:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8021#issuecomment-69966",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_8021-times.patch](tarball://root/attachments/some-uuid/ticket8021/trac_8021-times.patch) by @jhpalmieri created at 2010-01-21 06:30:23



---

archive/issue_comments_069967.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-22T02:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8021#issuecomment-69967",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069968.json:
```json
{
    "body": "This allows the HTML version of the reference manual to build without errors.",
    "created_at": "2010-01-22T02:37:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8021#issuecomment-69968",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This allows the HTML version of the reference manual to build without errors.



---

archive/issue_comments_069969.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-23T16:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8021",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8021#issuecomment-69969",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_019217.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-01-23T16:58:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8021",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8021#event-19217"
}
```
