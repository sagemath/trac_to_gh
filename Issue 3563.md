# Issue 3563: sage/misc/cython.py: make "def atlas()" deal with the Accelerate Framework on OSX

archive/issues_003563.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe review of #3530 exposed a bug hidden in sage/misc/cython.py: \"def atlas()\" would not return anything useful on OSX since we need to link against the Accelerate Framework.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3563\n\n",
    "created_at": "2008-07-06T12:04:15Z",
    "labels": [
        "build",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "sage/misc/cython.py: make \"def atlas()\" deal with the Accelerate Framework on OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3563",
    "user": "mabshoff"
}
```
Assignee: mabshoff

The review of #3530 exposed a bug hidden in sage/misc/cython.py: "def atlas()" would not return anything useful on OSX since we need to link against the Accelerate Framework.

Issue created by migration from https://trac.sagemath.org/ticket/3563





---

archive/issue_comments_025176.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-09-14T11:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3563#issuecomment-25176",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025177.json:
```json
{
    "body": "This issue actually breaks Cython on OSX 10.4 since the linker fails after it complains about a missing ATLAS.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T11:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3563#issuecomment-25177",
    "user": "mabshoff"
}
```

This issue actually breaks Cython on OSX 10.4 since the linker fails after it complains about a missing ATLAS.

Cheers,

Michael



---

archive/issue_comments_025178.json:
```json
{
    "body": "Attachment [trac_3563.2.patch](tarball://root/attachments/some-uuid/ticket3563/trac_3563.2.patch) by mabshoff created at 2008-09-15 12:11:06",
    "created_at": "2008-09-15T12:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3563#issuecomment-25178",
    "user": "mabshoff"
}
```

Attachment [trac_3563.2.patch](tarball://root/attachments/some-uuid/ticket3563/trac_3563.2.patch) by mabshoff created at 2008-09-15 12:11:06



---

archive/issue_comments_025179.json:
```json
{
    "body": "Looks good to me, and\n\n```\n[05:11am] mabshoff: ok, fixed the tests, passes on OSX and not-OSX: #3563\n```\n",
    "created_at": "2008-09-15T12:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3563#issuecomment-25179",
    "user": "rlm"
}
```

Looks good to me, and

```
[05:11am] mabshoff: ok, fixed the tests, passes on OSX and not-OSX: #3563
```




---

archive/issue_comments_025180.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-15T12:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3563#issuecomment-25180",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025181.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc4",
    "created_at": "2008-09-15T12:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3563#issuecomment-25181",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.rc4
