# Issue 4570: change the numpy include to the standard place

archive/issues_004570.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  robertwb\n\nThe standard numpy cython include is \"numpy/arrayobject.h\".  This changes Sage to use the standard include.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4570\n\n",
    "created_at": "2008-11-20T21:54:40Z",
    "labels": [
        "build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "change the numpy include to the standard place",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4570",
    "user": "jason"
}
```
Assignee: mabshoff

CC:  robertwb

The standard numpy cython include is "numpy/arrayobject.h".  This changes Sage to use the standard include.

Issue created by migration from https://trac.sagemath.org/ticket/4570





---

archive/issue_comments_034236.json:
```json
{
    "body": "Attachment [numpy-proper-include.patch](tarball://root/attachments/some-uuid/ticket4570/numpy-proper-include.patch) by jason created at 2008-11-20 21:55:17",
    "created_at": "2008-11-20T21:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4570#issuecomment-34236",
    "user": "jason"
}
```

Attachment [numpy-proper-include.patch](tarball://root/attachments/some-uuid/ticket4570/numpy-proper-include.patch) by jason created at 2008-11-20 21:55:17



---

archive/issue_comments_034237.json:
```json
{
    "body": "Looks good to me, but I don't have a recent enough sage to try it out (merge conflicts). I guess it's time to download 3.2 now.",
    "created_at": "2008-11-20T22:08:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4570#issuecomment-34237",
    "user": "robertwb"
}
```

Looks good to me, but I don't have a recent enough sage to try it out (merge conflicts). I guess it's time to download 3.2 now.



---

archive/issue_comments_034238.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T10:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4570#issuecomment-34238",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034239.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T10:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4570",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4570#issuecomment-34239",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha0
