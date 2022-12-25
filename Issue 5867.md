# Issue 5867: Fix gd build on FreeBSD

archive/issues_005867.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn FreeBSD, libiconv will be installed in /usr/local/lib - which is not searched by default.  Explicitly add /usr/local/lib to LDFLAGS to ensure it is correctly detected by the gd configure script.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5867\n\n",
    "created_at": "2009-04-23T06:56:11Z",
    "labels": [
        "component: porting: bsd",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Fix gd build on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5867",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: mabshoff

On FreeBSD, libiconv will be installed in /usr/local/lib - which is not searched by default.  Explicitly add /usr/local/lib to LDFLAGS to ensure it is correctly detected by the gd configure script.

Issue created by migration from https://trac.sagemath.org/ticket/5867





---

archive/issue_comments_046256.json:
```json
{
    "body": "Attachment [gd-2.0.35.p1.patch](tarball://root/attachments/some-uuid/ticket5867/gd-2.0.35.p1.patch) by mabshoff created at 2009-04-23 07:01:43",
    "created_at": "2009-04-23T07:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46256",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [gd-2.0.35.p1.patch](tarball://root/attachments/some-uuid/ticket5867/gd-2.0.35.p1.patch) by mabshoff created at 2009-04-23 07:01:43



---

archive/issue_comments_046257.json:
```json
{
    "body": "I will work on integrating this tomorrow.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46257",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I will work on integrating this tomorrow.

Cheers,

Michael



---

archive/issue_comments_046258.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T02:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46258",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046259.json:
```json
{
    "body": "Looks good to me.\n\nThe spkg with this fix is at http://sage.math.washington.edu/home/mhansen/gd-2.0.35.p2.spkg",
    "created_at": "2009-06-20T02:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46259",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.

The spkg with this fix is at http://sage.math.washington.edu/home/mhansen/gd-2.0.35.p2.spkg



---

archive/issue_comments_046260.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-06-20T02:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46260",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_046261.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T22:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5867#issuecomment-46261",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
