# Issue 3427: [with patch; needs review] remove ntl library from sage_object build dependency in setup.py

archive/issues_003427.json:
```json
{
    "body": "Assignee: mabshoff\n\nI can think of no good reason that the ntl library is linked into sage_object.pyx!  It absolutely shouldn't be needed.   Not having it there is needed for making sagelite. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3427\n\n",
    "created_at": "2008-06-14T22:15:34Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "[with patch; needs review] remove ntl library from sage_object build dependency in setup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3427",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

I can think of no good reason that the ntl library is linked into sage_object.pyx!  It absolutely shouldn't be needed.   Not having it there is needed for making sagelite. 

Issue created by migration from https://trac.sagemath.org/ticket/3427





---

archive/issue_events_007737.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-15T19:05:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3427",
    "milestone": "sage-3.0.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3427#event-7737"
}
```



---

archive/issue_comments_024100.json:
```json
{
    "body": "Attachment [sage-3427.patch](tarball://root/attachments/some-uuid/ticket3427/sage-3427.patch) by mabshoff created at 2008-06-15 19:05:54\n\nPositive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-15T19:05:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3427#issuecomment-24100",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-3427.patch](tarball://root/attachments/some-uuid/ticket3427/sage-3427.patch) by mabshoff created at 2008-06-15 19:05:54

Positive review.

Cheers,

Michael



---

archive/issue_comments_024101.json:
```json
{
    "body": "Merged in Sage 3.0.3.rc0",
    "created_at": "2008-06-15T19:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3427#issuecomment-24101",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.rc0



---

archive/issue_events_007738.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-15T19:15:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3427",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3427#event-7738"
}
```



---

archive/issue_comments_024102.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-15T19:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3427#issuecomment-24102",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
