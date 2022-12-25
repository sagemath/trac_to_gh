# Issue 2949: change slightly the docstring for assume (utterly trivial)

archive/issues_002949.json:
```json
{
    "body": "Assignee: @williamstein\n\nChange the output of assume? to:\n\n\n```\nsage: from sage.calculus.calculus import maxima as calcmaxima\nsage: calcmaxima.eval('declare(n,integer)')\n```\n\n\nto\n\n\n```\nsage: sage.calculus.calculus.maxima.eval('declare(n,integer)')\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2949\n\n",
    "created_at": "2008-04-18T00:24:13Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "change slightly the docstring for assume (utterly trivial)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2949",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_020292.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2008-04-18T06:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20292",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_020293.json:
```json
{
    "body": "Attachment [2949.patch](tarball://root/attachments/some-uuid/ticket2949/2949.patch) by @mwhansen created at 2008-04-18 06:10:12",
    "created_at": "2008-04-18T06:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20293",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2949.patch](tarball://root/attachments/some-uuid/ticket2949/2949.patch) by @mwhansen created at 2008-04-18 06:10:12



---

archive/issue_comments_020294.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-18T06:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20294",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_020295.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-18T19:04:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20295",
    "user": "https://github.com/dfdeshom"
}
```

Looks good to me.



---

archive/issue_comments_020296.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-18T20:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20296",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020297.json:
```json
{
    "body": "Merged in Sage 3.0.alpha6",
    "created_at": "2008-04-18T20:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2949#issuecomment-20297",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha6



---

archive/issue_events_003155.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-18T20:19:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2949",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2949#event-3155"
}
```
