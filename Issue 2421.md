# Issue 2421: .round(), .floor(), .ceil(), and .trunc() on RealNumber should have the same return type

archive/issues_002421.json:
```json
{
    "body": "Assignee: somebody\n\nCurrently the `RealNumber` methods .round() and .trunc() return `RealNumber`, but .floor() and .ceil() return `Integer`.  I think that all four methods should return `Integer`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2421\n\n",
    "created_at": "2008-03-07T15:23:43Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": ".round(), .floor(), .ceil(), and .trunc() on RealNumber should have the same return type",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2421",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: somebody

Currently the `RealNumber` methods .round() and .trunc() return `RealNumber`, but .floor() and .ceil() return `Integer`.  I think that all four methods should return `Integer`.

Issue created by migration from https://trac.sagemath.org/ticket/2421





---

archive/issue_comments_016347.json:
```json
{
    "body": "Attachment [2421.patch](tarball://root/attachments/some-uuid/ticket2421/2421.patch) by @dfdeshom created at 2008-03-10 20:17:42",
    "created_at": "2008-03-10T20:17:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16347",
    "user": "https://github.com/dfdeshom"
}
```

Attachment [2421.patch](tarball://root/attachments/some-uuid/ticket2421/2421.patch) by @dfdeshom created at 2008-03-10 20:17:42



---

archive/issue_comments_016348.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-10T20:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16348",
    "user": "https://github.com/dfdeshom"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016349.json:
```json
{
    "body": "Changing assignee from somebody to @dfdeshom.",
    "created_at": "2008-03-10T20:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16349",
    "user": "https://github.com/dfdeshom"
}
```

Changing assignee from somebody to @dfdeshom.



---

archive/issue_events_005722.json:
```json
{
    "actor": "https://github.com/dfdeshom",
    "created_at": "2008-03-12T05:05:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "milestone": "sage-2.10.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2421#event-5722"
}
```



---

archive/issue_comments_016350.json:
```json
{
    "body": "patch looks good. I say apply.",
    "created_at": "2008-03-12T09:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16350",
    "user": "https://github.com/malb"
}
```

patch looks good. I say apply.



---

archive/issue_comments_016351.json:
```json
{
    "body": "Didier, please submit mercurial patches in the future so you will get proper credit for your patches in the changelog. In this case it was too late and now credit goes to me :(\n\nCheers,\n\nMichael",
    "created_at": "2008-03-12T19:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16351",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Didier, please submit mercurial patches in the future so you will get proper credit for your patches in the changelog. In this case it was too late and now credit goes to me :(

Cheers,

Michael



---

archive/issue_comments_016352.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-12T19:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16352",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016353.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-12T19:41:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2421#issuecomment-16353",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0



---

archive/issue_events_005723.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-12T19:41:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2421",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2421#event-5723"
}
```
