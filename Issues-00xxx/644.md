# Issue 644: [with patch] (sin + cos)(1) does not work

archive/issues_000644.json:
```json
{
    "body": "Assignee: @mwhansen\n\nBoth sin and cos are functions of one (undetermined) variable, and can be called, but when one performs arithmetic on them this changes. \n\nMaybe there should be a CallableSymbolicExpressionRing with an unnamed variable that coerces into any CallableSymbolicExpressionRing with a specified variable name? \n\n```\nsage: f = sin\nsage: g = cos\nsage: f(1)\nsin(1)\nsage: g(1)\ncos(1)\nsage: h = f+g\nsage: h(1)\nsin + cos # should be sin(1)+cos(1)\nsage: f = 3*sin\nsage: f(1)\n3*sin # should be 3*sin(1)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/644\n\n",
    "closed_at": "2007-12-01T16:16:45Z",
    "created_at": "2007-09-12T19:00:58Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] (sin + cos)(1) does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/644",
    "user": "https://github.com/robertwb"
}
```
Assignee: @mwhansen

Both sin and cos are functions of one (undetermined) variable, and can be called, but when one performs arithmetic on them this changes. 

Maybe there should be a CallableSymbolicExpressionRing with an unnamed variable that coerces into any CallableSymbolicExpressionRing with a specified variable name? 

```
sage: f = sin
sage: g = cos
sage: f(1)
sin(1)
sage: g(1)
cos(1)
sage: h = f+g
sage: h(1)
sin + cos # should be sin(1)+cos(1)
sage: f = 3*sin
sage: f(1)
3*sin # should be 3*sin(1)
```

Issue created by migration from https://trac.sagemath.org/ticket/644





---

archive/issue_comments_003325.json:
```json
{
    "body": "Better formatting: \n\n```\nsage: f = sin\nsage: g = cos\nsage: f(1)\nsin(1)\nsage: g(1)\ncos(1)\nsage: h = f+g\nsage: h(1)\nsin + cos         # should be sin(1)+cos(1), or at least throw an error\nsage: f = 3*sin\nsage: f(1)\n3*sin             # should be 3*sin(1)\n```",
    "created_at": "2007-09-12T19:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3325",
    "user": "https://github.com/robertwb"
}
```

Better formatting: 

```
sage: f = sin
sage: g = cos
sage: f(1)
sin(1)
sage: g(1)
cos(1)
sage: h = f+g
sage: h(1)
sin + cos         # should be sin(1)+cos(1), or at least throw an error
sage: f = 3*sin
sage: f(1)
3*sin             # should be 3*sin(1)
```



---

archive/issue_events_001715.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-09-12T20:34:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/644#event-1715"
}
```



---

archive/issue_comments_003326.json:
```json
{
    "body": "Also should have \n\n```\nsage: f(x) = x^2\nsage: f + sin\nx |--> sin(x) + x^2\n```",
    "created_at": "2007-09-13T09:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3326",
    "user": "https://github.com/robertwb"
}
```

Also should have 

```
sage: f(x) = x^2
sage: f + sin
x |--> sin(x) + x^2
```



---

archive/issue_comments_003327.json:
```json
{
    "body": "See much discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/2f627fbe8d0f71c0",
    "created_at": "2007-09-13T09:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3327",
    "user": "https://github.com/robertwb"
}
```

See much discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/2f627fbe8d0f71c0



---

archive/issue_comments_003328.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-01T06:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3328",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003329.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-12-01T06:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3329",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_events_001716.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-12-01T06:50:49Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/644#event-1716"
}
```



---

archive/issue_events_001717.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-12-01T06:50:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "milestone": "sage-2.8.15",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/644#event-1717"
}
```



---

archive/issue_comments_003330.json:
```json
{
    "body": "This patch should be applied after #644.",
    "created_at": "2007-12-01T06:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3330",
    "user": "https://github.com/mwhansen"
}
```

This patch should be applied after #644.



---

archive/issue_events_001718.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-01T16:16:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/644#event-1718"
}
```



---

archive/issue_comments_003331.json:
```json
{
    "body": "Attachment [644.patch](tarball://root/attachments/some-uuid/ticket644/644.patch) by mabshoff created at 2007-12-01 16:16:45\n\nMerged in 2.8.15.alpha1.",
    "created_at": "2007-12-01T16:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [644.patch](tarball://root/attachments/some-uuid/ticket644/644.patch) by mabshoff created at 2007-12-01 16:16:45

Merged in 2.8.15.alpha1.



---

archive/issue_comments_003332.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T16:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3332",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
