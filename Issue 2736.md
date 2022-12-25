# Issue 2736: [with patch, needs review] fix for dsage doctest failures in sage-2.11.rc0

archive/issues_002736.json:
```json
{
    "body": "Assignee: @yqiang\n\nAttached is a patch which fixes the annoying exceptions thrown by the doctest runner at the end of the dsage doctests. \n\nThis patch does the following:\n1) Explicitly call .wait() on subprocess.Popen instances\n2) Explicitly delete the reference to the Popen instances before letting the interpreter exit\n3) Explicitly join the dsage thread before letting the interpreter exit in the doctest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2736\n\n",
    "created_at": "2008-03-30T21:45:12Z",
    "labels": [
        "component: dsage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, needs review] fix for dsage doctest failures in sage-2.11.rc0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2736",
    "user": "https://github.com/yqiang"
}
```
Assignee: @yqiang

Attached is a patch which fixes the annoying exceptions thrown by the doctest runner at the end of the dsage doctests. 

This patch does the following:
1) Explicitly call .wait() on subprocess.Popen instances
2) Explicitly delete the reference to the Popen instances before letting the interpreter exit
3) Explicitly join the dsage thread before letting the interpreter exit in the doctest.

Issue created by migration from https://trac.sagemath.org/ticket/2736





---

archive/issue_comments_018776.json:
```json
{
    "body": "Attachment [dsage_doctest_threading.patch](tarball://root/attachments/some-uuid/ticket2736/dsage_doctest_threading.patch) by @williamstein created at 2008-03-30 22:03:49\n\nTested on OS X.",
    "created_at": "2008-03-30T22:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2736#issuecomment-18776",
    "user": "https://github.com/williamstein"
}
```

Attachment [dsage_doctest_threading.patch](tarball://root/attachments/some-uuid/ticket2736/dsage_doctest_threading.patch) by @williamstein created at 2008-03-30 22:03:49

Tested on OS X.



---

archive/issue_comments_018777.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-30T22:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2736#issuecomment-18777",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018778.json:
```json
{
    "body": "Merged in Sage 2.11.final",
    "created_at": "2008-03-30T22:05:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2736#issuecomment-18778",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.final



---

archive/issue_events_002924.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-30T22:05:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2736",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2736#event-2924"
}
```
