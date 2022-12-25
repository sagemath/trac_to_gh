# Issue 1016: [with patch] add max_level argument to flatten

archive/issues_001016.json:
```json
{
    "body": "Assignee: cwitty\n\nCurrently flatten will only flatten a list all the way.  This patch adds a max_level argument that will only flatten up to a certain depth.  See the new doctests for examples.\n\nThis patch makes flatten a little slower because of bookkeeping.  However, if that's a problem, we can split the function into code paths depending on whether max_level is passed or not.  In this case, this version of flatten should run faster than the original version since a.pop(i) is slower than a[i:i+1]=[] (at least on my computer).\n\nI import sys to get sys.maxint.  Is that the proper way to get the maximum integer?\n\nAlso, I found in testing this patch that Python has some very low and depressing limits on the number of levels in nested lists!\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1016\n\n",
    "created_at": "2007-10-28T02:00:13Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "[with patch] add max_level argument to flatten",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1016",
    "user": "https://github.com/jasongrout"
}
```
Assignee: cwitty

Currently flatten will only flatten a list all the way.  This patch adds a max_level argument that will only flatten up to a certain depth.  See the new doctests for examples.

This patch makes flatten a little slower because of bookkeeping.  However, if that's a problem, we can split the function into code paths depending on whether max_level is passed or not.  In this case, this version of flatten should run faster than the original version since a.pop(i) is slower than a[i:i+1]=[] (at least on my computer).

I import sys to get sys.maxint.  Is that the proper way to get the maximum integer?

Also, I found in testing this patch that Python has some very low and depressing limits on the number of levels in nested lists!


Issue created by migration from https://trac.sagemath.org/ticket/1016





---

archive/issue_comments_006217.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-28T18:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1016#issuecomment-6217",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed



---

archive/issue_events_001140.json:
```json
{
    "actor": "cwitty",
    "created_at": "2007-10-28T18:34:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1016",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1016#event-1140"
}
```



---

archive/issue_comments_006218.json:
```json
{
    "body": "Attachment [flatten.patch](tarball://root/attachments/some-uuid/ticket1016/flatten.patch) by cwitty created at 2007-10-28 18:34:51",
    "created_at": "2007-10-28T18:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1016",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1016#issuecomment-6218",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [flatten.patch](tarball://root/attachments/some-uuid/ticket1016/flatten.patch) by cwitty created at 2007-10-28 18:34:51
