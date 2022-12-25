# Issue 1519: hg problem -- This should work but doesn't: sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/1514/trac-1514.patch?format=raw')

archive/issues_001519.json:
```json
{
    "body": "Assignee: @williamstein\n\nDoing\n\n```\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/1514/trac-1514.patch?format=raw')\n```\n\nshould work, but doesn't, because of the ?stuff at the end.  Fix this.\n\nHow to test the patch: Try applying a patch or bundle by pasting in the URL to the raw format as in the example above. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1519\n\n",
    "created_at": "2007-12-15T05:52:18Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "hg problem -- This should work but doesn't: sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/1514/trac-1514.patch?format=raw')",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1519",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Doing

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/1514/trac-1514.patch?format=raw')
```

should work, but doesn't, because of the ?stuff at the end.  Fix this.

How to test the patch: Try applying a patch or bundle by pasting in the URL to the raw format as in the example above. 

Issue created by migration from https://trac.sagemath.org/ticket/1519





---

archive/issue_comments_009705.json:
```json
{
    "body": "Attachment [trac-1519.patch](tarball://root/attachments/some-uuid/ticket1519/trac-1519.patch) by @williamstein created at 2007-12-15 06:19:18",
    "created_at": "2007-12-15T06:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1519#issuecomment-9705",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1519.patch](tarball://root/attachments/some-uuid/ticket1519/trac-1519.patch) by @williamstein created at 2007-12-15 06:19:18



---

archive/issue_comments_009706.json:
```json
{
    "body": "Note -- there is no easy way to doctest this, since it requires existence of a specific file on the internet with a funny ? in its filename..., and to apply that patch to a repository...",
    "created_at": "2007-12-15T06:20:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1519#issuecomment-9706",
    "user": "https://github.com/williamstein"
}
```

Note -- there is no easy way to doctest this, since it requires existence of a specific file on the internet with a funny ? in its filename..., and to apply that patch to a repository...



---

archive/issue_comments_009707.json:
```json
{
    "body": "looks good to me and is quite useful.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-15T11:00:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1519#issuecomment-9707",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

looks good to me and is quite useful.

Cheers,

Michael



---

archive/issue_comments_009708.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T11:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1519#issuecomment-9708",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_comments_009709.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T11:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1519",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1519#issuecomment-9709",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003838.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T11:06:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1519",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1519#event-3838"
}
```
