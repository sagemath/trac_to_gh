# Issue 2104: missing dependency: lcalc on mpfr

archive/issues_002104.json:
```json
{
    "body": "Assignee: mabshoff\n\nlcalc seems to link against mpfr, but doesn't depend on it in the spkg/standard/deps.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2104\n\n",
    "created_at": "2008-02-08T08:27:26Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "missing dependency: lcalc on mpfr",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2104",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

lcalc seems to link against mpfr, but doesn't depend on it in the spkg/standard/deps.

Issue created by migration from https://trac.sagemath.org/ticket/2104





---

archive/issue_comments_013690.json:
```json
{
    "body": "Attachment [deps.patch](tarball://root/attachments/some-uuid/ticket2104/deps.patch) by @timabbott created at 2008-02-08 22:24:14",
    "created_at": "2008-02-08T22:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2104#issuecomment-13690",
    "user": "https://github.com/timabbott"
}
```

Attachment [deps.patch](tarball://root/attachments/some-uuid/ticket2104/deps.patch) by @timabbott created at 2008-02-08 22:24:14



---

archive/issue_comments_013691.json:
```json
{
    "body": "Patch looks good to me and fixes a real bug that we just don't hit due to luck. \n\nCheers,\n\nMichael",
    "created_at": "2008-02-10T01:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2104#issuecomment-13691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me and fixes a real bug that we just don't hit due to luck. 

Cheers,

Michael



---

archive/issue_events_002264.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-10T01:46:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2104",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2104#event-2264"
}
```



---

archive/issue_comments_013692.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-10T01:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2104#issuecomment-13692",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_013693.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha0",
    "created_at": "2008-02-10T01:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2104",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2104#issuecomment-13693",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.alpha0
