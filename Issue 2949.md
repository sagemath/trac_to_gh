# Issue 2949: change slightly the docstring for assume (utterly trivial)

archive/issues_002949.json:
```json
{
    "body": "Assignee: @williamstein\n\nChange the output of assume? to:\n\n\n```\nsage: from sage.calculus.calculus import maxima as calcmaxima\nsage: calcmaxima.eval('declare(n,integer)')\n```\n\n\nto\n\n\n```\nsage: sage.calculus.calculus.maxima.eval('declare(n,integer)')\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2949\n\n",
    "created_at": "2008-04-18T00:24:13Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "change slightly the docstring for assume (utterly trivial)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2949",
    "user": "@williamstein"
}
```
Assignee: @williamstein

Change the output of assume? to:


```
sage: from sage.calculus.calculus import maxima as calcmaxima
sage: calcmaxima.eval('declare(n,integer)')
```


to


```
sage: sage.calculus.calculus.maxima.eval('declare(n,integer)')
```


Issue created by migration from https://trac.sagemath.org/ticket/2949





---

archive/issue_comments_020334.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-04-18T06:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20334",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_020335.json:
```json
{
    "body": "Attachment [2949.patch](tarball://root/attachments/some-uuid/ticket2949/2949.patch) by @mwhansen created at 2008-04-18 06:10:12",
    "created_at": "2008-04-18T06:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20335",
    "user": "@mwhansen"
}
```

Attachment [2949.patch](tarball://root/attachments/some-uuid/ticket2949/2949.patch) by @mwhansen created at 2008-04-18 06:10:12



---

archive/issue_comments_020336.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-18T06:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20336",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020337.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-18T19:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20337",
    "user": "@dfdeshom"
}
```

Looks good to me.



---

archive/issue_comments_020338.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-18T20:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20338",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020339.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-18T20:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20339",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha6
