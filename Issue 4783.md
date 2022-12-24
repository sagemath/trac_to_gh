# Issue 4783: [with patch; needs review] email -- create an "email" command, so users can easily notify themselves when their sage programs have completed some task

archive/issues_004783.json:
```json
{
    "body": "Assignee: cwitty\n\nThis was inspired by three things:\n\n1. I want a little script that will automatically email me whenever sagenb.org or any other website I manage stops responding for a certain amount of time.  \n\n2. Users every so often complain that sage.math doesn't have sendmail installed, so they can't put in code like `os.system('mail ...')`.  I.e., also, often people start a big computation, and it would be useful for them to get an email when it finishes.\n\n3. When I run the sage buildbot, it might be nice if the buildbot script could use sage to email me a summary of all failed tests (?).\n\nIssue created by migration from https://trac.sagemath.org/ticket/4783\n\n",
    "created_at": "2008-12-13T16:22:34Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch; needs review] email -- create an \"email\" command, so users can easily notify themselves when their sage programs have completed some task",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4783",
    "user": "@williamstein"
}
```
Assignee: cwitty

This was inspired by three things:

1. I want a little script that will automatically email me whenever sagenb.org or any other website I manage stops responding for a certain amount of time.  

2. Users every so often complain that sage.math doesn't have sendmail installed, so they can't put in code like `os.system('mail ...')`.  I.e., also, often people start a big computation, and it would be useful for them to get an email when it finishes.

3. When I run the sage buildbot, it might be nice if the buildbot script could use sage to email me a summary of all failed tests (?).

Issue created by migration from https://trac.sagemath.org/ticket/4783





---

archive/issue_comments_036266.json:
```json
{
    "body": "Attachment [trac_4783.patch](tarball://root/attachments/some-uuid/ticket4783/trac_4783.patch) by @williamstein created at 2008-12-13 16:25:01",
    "created_at": "2008-12-13T16:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4783#issuecomment-36266",
    "user": "@williamstein"
}
```

Attachment [trac_4783.patch](tarball://root/attachments/some-uuid/ticket4783/trac_4783.patch) by @williamstein created at 2008-12-13 16:25:01



---

archive/issue_comments_036267.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-14T05:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4783#issuecomment-36267",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036268.json:
```json
{
    "body": "Merged in Sage 3.2.2.rc0",
    "created_at": "2008-12-14T05:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4783",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4783#issuecomment-36268",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.rc0
