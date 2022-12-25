# Issue 5869: Fix libgpg-error shared library name on FreeBSD

archive/issues_005869.json:
```json
{
    "body": "Assignee: tbd\n\nEnsure that a symlink is created from libgpg-error.so to the actual .so name on FreeBSD.  This fixes the gnutls build on FreeBSD.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5869\n\n",
    "created_at": "2009-04-23T07:04:38Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Fix libgpg-error shared library name on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5869",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: tbd

Ensure that a symlink is created from libgpg-error.so to the actual .so name on FreeBSD.  This fixes the gnutls build on FreeBSD.


Issue created by migration from https://trac.sagemath.org/ticket/5869





---

archive/issue_comments_046268.json:
```json
{
    "body": "Attachment [libgpg_error-1.6.p0.patch](tarball://root/attachments/some-uuid/ticket5869/libgpg_error-1.6.p0.patch) by mabshoff created at 2009-04-23 07:31:38\n\nI will work on integrating this tomorrow.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T07:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46268",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [libgpg_error-1.6.p0.patch](tarball://root/attachments/some-uuid/ticket5869/libgpg_error-1.6.p0.patch) by mabshoff created at 2009-04-23 07:31:38

I will work on integrating this tomorrow.

Cheers,

Michael



---

archive/issue_comments_046269.json:
```json
{
    "body": "Changing assignee from tbd to mabshoff.",
    "created_at": "2009-04-23T08:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46269",
    "user": "https://github.com/peterjeremy"
}
```

Changing assignee from tbd to mabshoff.



---

archive/issue_comments_046270.json:
```json
{
    "body": "Changing component from algebra to freebsd.",
    "created_at": "2009-04-23T08:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46270",
    "user": "https://github.com/peterjeremy"
}
```

Changing component from algebra to freebsd.



---

archive/issue_comments_046271.json:
```json
{
    "body": "Changing assignee from mabshoff to @mwhansen.",
    "created_at": "2009-06-20T07:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46271",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from mabshoff to @mwhansen.



---

archive/issue_comments_046272.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T07:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46272",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046273.json:
```json
{
    "body": "Looks good to me.\n\nThe spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/libgpg_error-1.6.p1.spkg .",
    "created_at": "2009-06-20T07:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46273",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.

The spkg with this patch incorporated can be found at http://sage.math.washington.edu/home/mhansen/libgpg_error-1.6.p1.spkg .



---

archive/issue_comments_046274.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T22:37:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5869#issuecomment-46274",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_006125.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2009-07-02T22:37:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5869",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5869#event-6125"
}
```
