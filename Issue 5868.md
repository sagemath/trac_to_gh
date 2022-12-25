# Issue 5868: Fix libgcrypt shared library name on FreeBSD

archive/issues_005868.json:
```json
{
    "body": "Assignee: mabshoff\n\nEnsure that a symlink is created from libgcrypt.so to the actual .so name on FreeBSD.  This fixes the gnutls build on FreeBSD.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5868\n\n",
    "created_at": "2009-04-23T07:00:46Z",
    "labels": [
        "component: porting: bsd",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Fix libgcrypt shared library name on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5868",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: mabshoff

Ensure that a symlink is created from libgcrypt.so to the actual .so name on FreeBSD.  This fixes the gnutls build on FreeBSD.



Issue created by migration from https://trac.sagemath.org/ticket/5868





---

archive/issue_comments_046262.json:
```json
{
    "body": "Attachment [libgcrypt-1.4.3.p0.patch](tarball://root/attachments/some-uuid/ticket5868/libgcrypt-1.4.3.p0.patch) by @peterjeremy created at 2009-04-23 07:01:01",
    "created_at": "2009-04-23T07:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46262",
    "user": "https://github.com/peterjeremy"
}
```

Attachment [libgcrypt-1.4.3.p0.patch](tarball://root/attachments/some-uuid/ticket5868/libgcrypt-1.4.3.p0.patch) by @peterjeremy created at 2009-04-23 07:01:01



---

archive/issue_comments_046263.json:
```json
{
    "body": "I will work on integrating this tomorrow.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46263",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will work on integrating this tomorrow.

Cheers,

Michael



---

archive/issue_comments_046264.json:
```json
{
    "body": "Looks good to me.\n\nThe spkg with this change can be found at http://sage.math.washington.edu/home/mhansen/libgcrypt-1.4.3.p1.spkg",
    "created_at": "2009-06-20T02:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46264",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.

The spkg with this change can be found at http://sage.math.washington.edu/home/mhansen/libgcrypt-1.4.3.p1.spkg



---

archive/issue_comments_046265.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-06-20T02:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46265",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_046266.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T02:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46266",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046267.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T22:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46267",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_006124.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2009-07-02T22:32:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5868#event-6124"
}
```
