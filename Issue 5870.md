# Issue 5870: Detect blas and atlas libraries for linbox on FreeBSD

archive/issues_005870.json:
```json
{
    "body": "Assignee: mabshoff\n\nspkg-install for linbox uses OS-specific code to detect and use the BLAS and Atlas libraries.  Add code to support FreeBSD.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5870\n\n",
    "created_at": "2009-04-23T07:12:05Z",
    "labels": [
        "component: porting: bsd"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Detect blas and atlas libraries for linbox on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5870",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: mabshoff

spkg-install for linbox uses OS-specific code to detect and use the BLAS and Atlas libraries.  Add code to support FreeBSD.

Issue created by migration from https://trac.sagemath.org/ticket/5870





---

archive/issue_comments_046275.json:
```json
{
    "body": "Attachment [linbox-1.1.6.patch](tarball://root/attachments/some-uuid/ticket5870/linbox-1.1.6.patch) by @peterjeremy created at 2009-04-23 07:12:14",
    "created_at": "2009-04-23T07:12:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46275",
    "user": "https://github.com/peterjeremy"
}
```

Attachment [linbox-1.1.6.patch](tarball://root/attachments/some-uuid/ticket5870/linbox-1.1.6.patch) by @peterjeremy created at 2009-04-23 07:12:14



---

archive/issue_comments_046276.json:
```json
{
    "body": "I will work on integrating this tomorrow.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:32:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46276",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will work on integrating this tomorrow.

Cheers,

Michael



---

archive/issue_comments_046277.json:
```json
{
    "body": "Looks good to me.\n\nAn spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/linbox-1.1.6.p0.spkg",
    "created_at": "2009-06-20T07:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46277",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.

An spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/linbox-1.1.6.p0.spkg



---

archive/issue_comments_046278.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-06-20T07:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46278",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_046279.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T07:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46279",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046280.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T22:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5870#issuecomment-46280",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_006126.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2009-07-02T22:47:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5870",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5870#event-6126"
}
```
