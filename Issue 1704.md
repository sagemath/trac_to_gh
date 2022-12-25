# Issue 1704: [with patch, with positive review] replace _DivPolyContext by _multiply_point

archive/issues_001704.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis patch replaces the `_DivPolyContext` class with a new function `_multiply_point`. The main downside of the original `_DivPolyContext` is that it's very recursive, and I started overflowing python's stack for some large problems I needed to play with. The new function is not recursive, and also turns out to be slightly faster.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1704\n\n",
    "closed_at": "2008-01-21T05:52:54Z",
    "created_at": "2008-01-06T23:19:41Z",
    "labels": [
        "component: algebraic geometry"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with patch, with positive review] replace _DivPolyContext by _multiply_point",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1704",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein

This patch replaces the `_DivPolyContext` class with a new function `_multiply_point`. The main downside of the original `_DivPolyContext` is that it's very recursive, and I started overflowing python's stack for some large problems I needed to play with. The new function is not recursive, and also turns out to be slightly faster.


Issue created by migration from https://trac.sagemath.org/ticket/1704





---

archive/issue_comments_010767.json:
```json
{
    "body": "Attachment [multiply_point.hg](tarball://root/attachments/some-uuid/ticket1704/multiply_point.hg) by dmharvey created at 2008-01-06 23:20:24",
    "created_at": "2008-01-06T23:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1704#issuecomment-10767",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Attachment [multiply_point.hg](tarball://root/attachments/some-uuid/ticket1704/multiply_point.hg) by dmharvey created at 2008-01-06 23:20:24



---

archive/issue_comments_010768.json:
```json
{
    "body": "I can't speak to mathematical correctness, but the patch looks good to me.  Apply.",
    "created_at": "2008-01-20T06:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1704#issuecomment-10768",
    "user": "https://github.com/ncalexan"
}
```

I can't speak to mathematical correctness, but the patch looks good to me.  Apply.



---

archive/issue_events_004160.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-21T05:52:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1704",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1704#event-4160"
}
```



---

archive/issue_comments_010769.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T05:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1704#issuecomment-10769",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010770.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T05:52:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1704",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1704#issuecomment-10770",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1
