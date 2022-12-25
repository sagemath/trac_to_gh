# Issue 919: creation of p-adic rings uses O(n^2) memory

archive/issues_000919.json:
```json
{
    "body": "Assignee: @roed314\n\nKeywords: padics\n\nUpon creation, p-adic rings currently cache powers of p from 0 up to their precision cap.  This uses O(n^2) space, and is very unfriendly to someone who wants to use a capped relative ring with very high precision in order to never run into the precision cap.\n\nIssue created by migration from https://trac.sagemath.org/ticket/919\n\n",
    "created_at": "2007-10-18T14:51:33Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.8",
    "title": "creation of p-adic rings uses O(n^2) memory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/919",
    "user": "https://github.com/roed314"
}
```
Assignee: @roed314

Keywords: padics

Upon creation, p-adic rings currently cache powers of p from 0 up to their precision cap.  This uses O(n^2) space, and is very unfriendly to someone who wants to use a capped relative ring with very high precision in order to never run into the precision cap.

Issue created by migration from https://trac.sagemath.org/ticket/919





---

archive/issue_comments_005616.json:
```json
{
    "body": "Fixes the problem, adds some functionality for padic extensions",
    "created_at": "2007-10-19T22:09:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/919#issuecomment-5616",
    "user": "https://github.com/roed314"
}
```

Fixes the problem, adds some functionality for padic extensions



---

archive/issue_comments_005617.json:
```json
{
    "body": "Attachment [padic_framework.hg](tarball://root/attachments/some-uuid/ticket919/padic_framework.hg) by @roed314 created at 2007-10-19 22:09:53",
    "created_at": "2007-10-19T22:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/919#issuecomment-5617",
    "user": "https://github.com/roed314"
}
```

Attachment [padic_framework.hg](tarball://root/attachments/some-uuid/ticket919/padic_framework.hg) by @roed314 created at 2007-10-19 22:09:53



---

archive/issue_comments_005618.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-20T18:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/919#issuecomment-5618",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_005619.json:
```json
{
    "body": "I've applied this.",
    "created_at": "2007-10-20T18:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/919#issuecomment-5619",
    "user": "https://github.com/williamstein"
}
```

I've applied this.



---

archive/issue_events_001039.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2007-10-20T18:00:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/919",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/919#event-1039"
}
```
