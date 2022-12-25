# Issue 3186: fix 64 bit OSX build support for numpy

archive/issues_003186.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe need to create a fake gcc injecting \"-m64\" in the argument list since otherwise the conftest will fail.\n\nSpkg is coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3186\n\n",
    "created_at": "2008-05-13T13:48:57Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "fix 64 bit OSX build support for numpy",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3186",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

We need to create a fake gcc injecting "-m64" in the argument list since otherwise the conftest will fail.

Spkg is coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3186





---

archive/issue_comments_021996.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-13T13:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3186#issuecomment-21996",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021997.json:
```json
{
    "body": "Attachment [numpy-20080104-1.0.4.p2-64bit-osx.patch](tarball://root/attachments/some-uuid/ticket3186/numpy-20080104-1.0.4.p2-64bit-osx.patch) by mabshoff created at 2008-05-19 03:49:45",
    "created_at": "2008-05-19T03:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3186#issuecomment-21997",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [numpy-20080104-1.0.4.p2-64bit-osx.patch](tarball://root/attachments/some-uuid/ticket3186/numpy-20080104-1.0.4.p2-64bit-osx.patch) by mabshoff created at 2008-05-19 03:49:45



---

archive/issue_comments_021998.json:
```json
{
    "body": "Attachment [numpy-20080104-1.0.4.p2-64bit-osx_part2.patch](tarball://root/attachments/some-uuid/ticket3186/numpy-20080104-1.0.4.p2-64bit-osx_part2.patch) by mabshoff created at 2008-05-19 03:49:55",
    "created_at": "2008-05-19T03:49:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3186#issuecomment-21998",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [numpy-20080104-1.0.4.p2-64bit-osx_part2.patch](tarball://root/attachments/some-uuid/ticket3186/numpy-20080104-1.0.4.p2-64bit-osx_part2.patch) by mabshoff created at 2008-05-19 03:49:55



---

archive/issue_comments_021999.json:
```json
{
    "body": "Attachment [numpy-20080104-1.0.4.p2-64bit-osx_part3.patch](tarball://root/attachments/some-uuid/ticket3186/numpy-20080104-1.0.4.p2-64bit-osx_part3.patch) by mabshoff created at 2008-05-19 03:57:37\n\nThe updated spkg is at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha1/numpy-20080104-1.0.4.p4.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-05-19T03:57:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3186#issuecomment-21999",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [numpy-20080104-1.0.4.p2-64bit-osx_part3.patch](tarball://root/attachments/some-uuid/ticket3186/numpy-20080104-1.0.4.p2-64bit-osx_part3.patch) by mabshoff created at 2008-05-19 03:57:37

The updated spkg is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.2/alpha1/numpy-20080104-1.0.4.p4.spkg

Cheers,

Michael



---

archive/issue_events_003404.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-05-19T04:01:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3186",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3186#event-3404"
}
```



---

archive/issue_comments_022000.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha1",
    "created_at": "2008-05-19T04:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3186#issuecomment-22000",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.alpha1



---

archive/issue_comments_022001.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-19T04:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3186",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3186#issuecomment-22001",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
