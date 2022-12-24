# Issue 5868: Fix libgcrypt shared library name on FreeBSD

archive/issues_005868.json:
```json
{
    "body": "Assignee: mabshoff\n\nEnsure that a symlink is created from libgcrypt.so to the actual .so name on FreeBSD.  This fixes the gnutls build on FreeBSD.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5868\n\n",
    "created_at": "2009-04-23T07:00:46Z",
    "labels": [
        "porting: BSD",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Fix libgcrypt shared library name on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5868",
    "user": "@peterjeremy"
}
```
Assignee: mabshoff

Ensure that a symlink is created from libgcrypt.so to the actual .so name on FreeBSD.  This fixes the gnutls build on FreeBSD.



Issue created by migration from https://trac.sagemath.org/ticket/5868





---

archive/issue_comments_046351.json:
```json
{
    "body": "Attachment [libgcrypt-1.4.3.p0.patch](tarball://root/attachments/some-uuid/ticket5868/libgcrypt-1.4.3.p0.patch) by @peterjeremy created at 2009-04-23 07:01:01",
    "created_at": "2009-04-23T07:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46351",
    "user": "@peterjeremy"
}
```

Attachment [libgcrypt-1.4.3.p0.patch](tarball://root/attachments/some-uuid/ticket5868/libgcrypt-1.4.3.p0.patch) by @peterjeremy created at 2009-04-23 07:01:01



---

archive/issue_comments_046352.json:
```json
{
    "body": "I will work on integrating this tomorrow.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46352",
    "user": "mabshoff"
}
```

I will work on integrating this tomorrow.

Cheers,

Michael



---

archive/issue_comments_046353.json:
```json
{
    "body": "Looks good to me.\n\nThe spkg with this change can be found at http://sage.math.washington.edu/home/mhansen/libgcrypt-1.4.3.p1.spkg",
    "created_at": "2009-06-20T02:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46353",
    "user": "@mwhansen"
}
```

Looks good to me.

The spkg with this change can be found at http://sage.math.washington.edu/home/mhansen/libgcrypt-1.4.3.p1.spkg



---

archive/issue_comments_046354.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-06-20T02:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46354",
    "user": "@mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_046355.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T02:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46355",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046356.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T22:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5868",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5868#issuecomment-46356",
    "user": "@rlmill"
}
```

Resolution: fixed
