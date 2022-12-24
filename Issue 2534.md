# Issue 2534: Sage does not handle Symmetrica's large integers

archive/issues_002534.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis causes problems when working with larger partitions.  For example,\n\n```\nsage: s = SFASchur(QQ)\nsage: a = s([8,8])\nsage: a.itensor(a)\n```\n\ngives the wrong results.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2534\n\n",
    "created_at": "2008-03-15T23:36:24Z",
    "labels": [
        "interfaces",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "Sage does not handle Symmetrica's large integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2534",
    "user": "@mwhansen"
}
```
Assignee: @williamstein

This causes problems when working with larger partitions.  For example,

```
sage: s = SFASchur(QQ)
sage: a = s([8,8])
sage: a.itensor(a)
```

gives the wrong results.

Issue created by migration from https://trac.sagemath.org/ticket/2534





---

archive/issue_comments_017276.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-15T23:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2534#issuecomment-17276",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017277.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-03-15T23:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2534#issuecomment-17277",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_017278.json:
```json
{
    "body": "I have a fix for this, but cannot get the Cython generated code to compile.",
    "created_at": "2008-03-15T23:36:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2534#issuecomment-17278",
    "user": "@mwhansen"
}
```

I have a fix for this, but cannot get the Cython generated code to compile.



---

archive/issue_comments_017279.json:
```json
{
    "body": "Attachment [2534.patch](tarball://root/attachments/some-uuid/ticket2534/2534.patch) by @mwhansen created at 2008-03-16 03:32:25",
    "created_at": "2008-03-16T03:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2534#issuecomment-17279",
    "user": "@mwhansen"
}
```

Attachment [2534.patch](tarball://root/attachments/some-uuid/ticket2534/2534.patch) by @mwhansen created at 2008-03-16 03:32:25



---

archive/issue_comments_017280.json:
```json
{
    "body": "Attachment [2534.2.patch](tarball://root/attachments/some-uuid/ticket2534/2534.2.patch) by @mwhansen created at 2008-03-16 04:23:24\n\nOnly apply 2534.2.patch which was made against 2.10.4.alpha0.",
    "created_at": "2008-03-16T04:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2534#issuecomment-17280",
    "user": "@mwhansen"
}
```

Attachment [2534.2.patch](tarball://root/attachments/some-uuid/ticket2534/2534.2.patch) by @mwhansen created at 2008-03-16 04:23:24

Only apply 2534.2.patch which was made against 2.10.4.alpha0.



---

archive/issue_comments_017281.json:
```json
{
    "body": "Patch looks good to me, testall shows no problem.",
    "created_at": "2008-03-16T05:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2534#issuecomment-17281",
    "user": "mabshoff"
}
```

Patch looks good to me, testall shows no problem.



---

archive/issue_comments_017282.json:
```json
{
    "body": "Merged in Sage 2.10.4.rc0 - I will valgrind this once rc0 is out.",
    "created_at": "2008-03-16T05:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2534#issuecomment-17282",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.rc0 - I will valgrind this once rc0 is out.



---

archive/issue_comments_017283.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-16T05:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2534#issuecomment-17283",
    "user": "mabshoff"
}
```

Resolution: fixed
