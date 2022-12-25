# Issue 724: graph6 parsing does not throw an error when the string is the wrong size.

archive/issues_000724.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: graph6, graph\n\nMaking a graph from a graph6 string should check to make sure the string is the right size and throw an error if the string is too long or too short.  I believe now it just silently hands back a graph that is not correct.\n\nThis is bad, especially when your string has an escaped character and you didn't realize it :).\n\nIssue created by migration from https://trac.sagemath.org/ticket/724\n\n",
    "created_at": "2007-09-21T00:40:12Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "graph6 parsing does not throw an error when the string is the wrong size.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/724",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Keywords: graph6, graph

Making a graph from a graph6 string should check to make sure the string is the right size and throw an error if the string is too long or too short.  I believe now it just silently hands back a graph that is not correct.

This is bad, especially when your string has an escaped character and you didn't realize it :).

Issue created by migration from https://trac.sagemath.org/ticket/724





---

archive/issue_comments_004207.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-24T07:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4207",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_004208.json:
```json
{
    "body": "Changing assignee from @williamstein to @rlmill.",
    "created_at": "2007-10-24T07:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4208",
    "user": "https://github.com/rlmill"
}
```

Changing assignee from @williamstein to @rlmill.



---

archive/issue_comments_004209.json:
```json
{
    "body": "Attachment [7087.patch](tarball://root/attachments/some-uuid/ticket724/7087.patch) by @rlmill created at 2007-10-24 07:50:00",
    "created_at": "2007-10-24T07:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4209",
    "user": "https://github.com/rlmill"
}
```

Attachment [7087.patch](tarball://root/attachments/some-uuid/ticket724/7087.patch) by @rlmill created at 2007-10-24 07:50:00



---

archive/issue_comments_004210.json:
```json
{
    "body": "This patches cleanly onto 2.8.9.",
    "created_at": "2007-10-25T18:54:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4210",
    "user": "https://github.com/rlmill"
}
```

This patches cleanly onto 2.8.9.



---

archive/issue_comments_004211.json:
```json
{
    "body": "Please add doctests to show the new exceptions.  (Every bug fix should have a doctest.)\n\nThanks!",
    "created_at": "2007-10-26T06:38:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4211",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Please add doctests to show the new exceptions.  (Every bug fix should have a doctest.)

Thanks!



---

archive/issue_comments_004212.json:
```json
{
    "body": "Attachment [7148.patch](tarball://root/attachments/some-uuid/ticket724/7148.patch) by cwitty created at 2007-10-27 04:53:30",
    "created_at": "2007-10-27T04:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4212",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [7148.patch](tarball://root/attachments/some-uuid/ticket724/7148.patch) by cwitty created at 2007-10-27 04:53:30



---

archive/issue_comments_004213.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T04:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/724#issuecomment-4213",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed
