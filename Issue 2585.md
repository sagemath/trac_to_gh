# Issue 2585: [with-patch] padic bugfix - check=False in constructor

archive/issues_002585.json:
```json
{
    "body": "Assignee: roed\n\nFixes bug in Qp, Zp, etc that causes segmentation faults in the constructor.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2585\n\n",
    "created_at": "2008-03-18T12:06:34Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with-patch] padic bugfix - check=False in constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2585",
    "user": "roed"
}
```
Assignee: roed

Fixes bug in Qp, Zp, etc that causes segmentation faults in the constructor.

Issue created by migration from https://trac.sagemath.org/ticket/2585





---

archive/issue_comments_017695.json:
```json
{
    "body": "Attachment [2585.patch](tarball://root/attachments/some-uuid/ticket2585/2585.patch) by mhansen created at 2008-03-19 01:15:14",
    "created_at": "2008-03-19T01:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2585#issuecomment-17695",
    "user": "mhansen"
}
```

Attachment [2585.patch](tarball://root/attachments/some-uuid/ticket2585/2585.patch) by mhansen created at 2008-03-19 01:15:14



---

archive/issue_comments_017696.json:
```json
{
    "body": "I fixed a small bug in the patch (changed p in Zq integer check to q).  Apply 2585.patch.  Otherwise, it looks good to me.",
    "created_at": "2008-03-19T01:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2585#issuecomment-17696",
    "user": "mhansen"
}
```

I fixed a small bug in the patch (changed p in Zq integer check to q).  Apply 2585.patch.  Otherwise, it looks good to me.



---

archive/issue_comments_017697.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-19T01:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2585#issuecomment-17697",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017698.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-19T01:23:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2585",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2585#issuecomment-17698",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0
