# Issue 2248: [with patch, needs trivial review] sage-2.10.2.alpha2: multi_polynomial.pyx doctest failure

archive/issues_002248.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nsage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx\n**********************************************************************\nFile \"multi_polynomial.pyx\", line 256:\n    sage: R(S.0)\nExpected:\n    BROKEN -- FIX ME\nGot:\n    p\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2248\n\n",
    "created_at": "2008-02-21T19:01:42Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "[with patch, needs trivial review] sage-2.10.2.alpha2: multi_polynomial.pyx doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2248",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: failure


```
sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial.pyx
**********************************************************************
File "multi_polynomial.pyx", line 256:
    sage: R(S.0)
Expected:
    BROKEN -- FIX ME
Got:
    p
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/2248





---

archive/issue_comments_014868.json:
```json
{
    "body": "fixed the failure as suggested by William",
    "created_at": "2008-02-21T19:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2248#issuecomment-14868",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

fixed the failure as suggested by William



---

archive/issue_comments_014869.json:
```json
{
    "body": "Attachment [trac_2248.patch](tarball://root/attachments/some-uuid/ticket2248/trac_2248.patch) by @williamstein created at 2008-02-21 19:21:23",
    "created_at": "2008-02-21T19:21:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2248#issuecomment-14869",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_2248.patch](tarball://root/attachments/some-uuid/ticket2248/trac_2248.patch) by @williamstein created at 2008-02-21 19:21:23



---

archive/issue_events_002418.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-21T19:23:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2248",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2248#event-2418"
}
```



---

archive/issue_comments_014870.json:
```json
{
    "body": "Merged in Sage 2.10.2.rc0",
    "created_at": "2008-02-21T19:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2248#issuecomment-14870",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.rc0



---

archive/issue_comments_014871.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T19:23:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2248#issuecomment-14871",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
