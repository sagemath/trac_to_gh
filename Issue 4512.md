# Issue 4512: [with patch, needs review] sage path-related troubles

archive/issues_004512.json:
```json
{
    "body": "Assignee: @craigcitro\n\nUnfortunately, it seems that `sage -sh` doesn't ask the shell to avoid processing the `.profile` or equivalent. In particular, it can lead to things like this:\n\n```\n[craigcitro@sharma ~/new-three-two]  $ ./sage -version\nSage Version 3.2.rc0, Release Date: 2008-11-10\n[craigcitro@sharma ~/new-three-two]  $ ./sage -sh\n\nStarting subshell with Sage environment variables set.\nBe sure to exit when you are done and do not do anything\nwith other copies of Sage!\n\n[craigcitro@sharma ~/new-three-two]  $ sage -version\nSAGE Version 3.1.4, Release Date: 2008-10-16\n[craigcitro@sharma ~/new-three-two]  $ which sage\n/usr/local/bin/sage\n```\n\nThis comes from the fact that I manually **prepend** certain things to my path in my `.bashrc`. Sadly, this leads to several small, subtle issues. I've attached a patch which turns several calls to `sage` into `$SAGE_ROOT/sage`.\n\nHowever, something more serious is needed. I think that the right approach is to start the new shell without processing any login files, so that we know our path is correct. The patch does that. \n\nI'm listing this as a blocker, because it causes such subtle errors, and because a fix is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4512\n\n",
    "created_at": "2008-11-13T10:58:04Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] sage path-related troubles",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4512",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

Unfortunately, it seems that `sage -sh` doesn't ask the shell to avoid processing the `.profile` or equivalent. In particular, it can lead to things like this:

```
[craigcitro@sharma ~/new-three-two]  $ ./sage -version
Sage Version 3.2.rc0, Release Date: 2008-11-10
[craigcitro@sharma ~/new-three-two]  $ ./sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

[craigcitro@sharma ~/new-three-two]  $ sage -version
SAGE Version 3.1.4, Release Date: 2008-10-16
[craigcitro@sharma ~/new-three-two]  $ which sage
/usr/local/bin/sage
```

This comes from the fact that I manually **prepend** certain things to my path in my `.bashrc`. Sadly, this leads to several small, subtle issues. I've attached a patch which turns several calls to `sage` into `$SAGE_ROOT/sage`.

However, something more serious is needed. I think that the right approach is to start the new shell without processing any login files, so that we know our path is correct. The patch does that. 

I'm listing this as a blocker, because it causes such subtle errors, and because a fix is attached.

Issue created by migration from https://trac.sagemath.org/ticket/4512





---

archive/issue_comments_033399.json:
```json
{
    "body": "Attachment [trac-4512.patch](tarball://root/attachments/some-uuid/ticket4512/trac-4512.patch) by @craigcitro created at 2008-11-13 10:59:05",
    "created_at": "2008-11-13T10:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4512#issuecomment-33399",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4512.patch](tarball://root/attachments/some-uuid/ticket4512/trac-4512.patch) by @craigcitro created at 2008-11-13 10:59:05



---

archive/issue_comments_033400.json:
```json
{
    "body": "This patch is for the `sage-scripts` repository, of course.",
    "created_at": "2008-11-13T10:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4512#issuecomment-33400",
    "user": "https://github.com/craigcitro"
}
```

This patch is for the `sage-scripts` repository, of course.



---

archive/issue_comments_033401.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-13T10:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4512#issuecomment-33401",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033402.json:
```json
{
    "body": "Could we at least have a PS1 that includes the current directory?  I always hated it when I was on a machine where \"sage -sh\" didn't use my existing PS1.",
    "created_at": "2008-11-13T12:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4512#issuecomment-33402",
    "user": "https://github.com/mwhansen"
}
```

Could we at least have a PS1 that includes the current directory?  I always hated it when I was on a machine where "sage -sh" didn't use my existing PS1.



---

archive/issue_comments_033403.json:
```json
{
    "body": "Yeah, that would be very reasonable.\n\nActually, we could go one further: have a specific place in `~/.sage/` where one can put `.profile` files and whatnot, with big warnings about paths. The point is really just that we don't want to grab the system-wide ones ...",
    "created_at": "2008-11-13T13:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4512#issuecomment-33403",
    "user": "https://github.com/craigcitro"
}
```

Yeah, that would be very reasonable.

Actually, we could go one further: have a specific place in `~/.sage/` where one can put `.profile` files and whatnot, with big warnings about paths. The point is really just that we don't want to grab the system-wide ones ...



---

archive/issue_comments_033404.json:
```json
{
    "body": "Craig,\n\nI am not so sure this is a blocker, i.e. just because your .profile is misconfigured doesn't mean that as a consequence somebody else's config will not be broken by fixing it for you. I am inclined to merge this patch, but I need to think about it.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-14T04:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4512#issuecomment-33404",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Craig,

I am not so sure this is a blocker, i.e. just because your .profile is misconfigured doesn't mean that as a consequence somebody else's config will not be broken by fixing it for you. I am inclined to merge this patch, but I need to think about it.

Cheers,

Michael



---

archive/issue_comments_033405.json:
```json
{
    "body": "Attachment [trac-4512-pt2.patch](tarball://root/attachments/some-uuid/ticket4512/trac-4512-pt2.patch) by mabshoff created at 2008-11-14 04:56:09\n\ntrac-4512-pt2.patch addresses all my concerns even though it could be cleaner, i.e. via some special parameter. Craig will do so in a followup ticket, so positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-14T04:56:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4512#issuecomment-33405",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-4512-pt2.patch](tarball://root/attachments/some-uuid/ticket4512/trac-4512-pt2.patch) by mabshoff created at 2008-11-14 04:56:09

trac-4512-pt2.patch addresses all my concerns even though it could be cleaner, i.e. via some special parameter. Craig will do so in a followup ticket, so positive review.

Cheers,

Michael



---

archive/issue_comments_033406.json:
```json
{
    "body": "Merged both patch in Sage 3.2.rc1",
    "created_at": "2008-11-14T06:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4512#issuecomment-33406",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patch in Sage 3.2.rc1



---

archive/issue_comments_033407.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-14T06:00:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4512#issuecomment-33407",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010225.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-14T06:00:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4512",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4512#event-10225"
}
```
