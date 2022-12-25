# Issue 810: [with patch] gens_reduced for general ideals

archive/issues_000810.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt's annoying that number field ideals have a `gens_reduced()` method, but ideals of ZZ do not. This patch fixes this by adding a `gens_reduced()` method to the base ideal class, whose default implementation just calls `gens()`.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/810\n\n",
    "closed_at": "2007-10-04T15:15:23Z",
    "created_at": "2007-10-03T16:39:57Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.6",
    "title": "[with patch] gens_reduced for general ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/810",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein

It's annoying that number field ideals have a `gens_reduced()` method, but ideals of ZZ do not. This patch fixes this by adding a `gens_reduced()` method to the base ideal class, whose default implementation just calls `gens()`.


Issue created by migration from https://trac.sagemath.org/ticket/810





---

archive/issue_comments_004887.json:
```json
{
    "body": "Attachment [gens-reduced.hg](tarball://root/attachments/some-uuid/ticket810/gens-reduced.hg) by dmharvey created at 2007-10-03 16:40:10",
    "created_at": "2007-10-03T16:40:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/810#issuecomment-4887",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [gens-reduced.hg](tarball://root/attachments/some-uuid/ticket810/gens-reduced.hg) by dmharvey created at 2007-10-03 16:40:10



---

archive/issue_comments_004888.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-04T15:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/810#issuecomment-4888",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_002278.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-04T15:15:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/810",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/810#event-2278"
}
```
