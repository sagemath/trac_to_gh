# Issue 644: (sin + cos)(1) does not work

archive/issues_000644.json:
```json
{
    "body": "Assignee: @williamstein\n\nBoth sin and cos are functions of one (undetermined) variable, and can be called, but when one performs arithmetic on them this changes. \n\nMaybe there should be a CallableSymbolicExpressionRing with an unnamed variable that coerces into any CallableSymbolicExpressionRing with a specified variable name? \n\nsage: f = sin\nsage: g = cos\nsage: f(1)\nsin(1)\nsage: g(1)\ncos(1)\nsage: h = f+g\nsage: h(1)\nsin + cos # should be sin(1)+cos(1)\nsage: f = 3*sin\nsage: f(1)\n3*sin # should be 3*sin(1)\n\nIssue created by migration from https://trac.sagemath.org/ticket/644\n\n",
    "created_at": "2007-09-12T19:00:58Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "(sin + cos)(1) does not work",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/644",
    "user": "@robertwb"
}
```
Assignee: @williamstein

Both sin and cos are functions of one (undetermined) variable, and can be called, but when one performs arithmetic on them this changes. 

Maybe there should be a CallableSymbolicExpressionRing with an unnamed variable that coerces into any CallableSymbolicExpressionRing with a specified variable name? 

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

Issue created by migration from https://trac.sagemath.org/ticket/644





---

archive/issue_comments_003338.json:
```json
{
    "body": "Better formatting: \n\n```\nsage: f = sin\nsage: g = cos\nsage: f(1)\nsin(1)\nsage: g(1)\ncos(1)\nsage: h = f+g\nsage: h(1)\nsin + cos         # should be sin(1)+cos(1), or at least throw an error\nsage: f = 3*sin\nsage: f(1)\n3*sin             # should be 3*sin(1)\n```\n",
    "created_at": "2007-09-12T19:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3338",
    "user": "@robertwb"
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

archive/issue_comments_003339.json:
```json
{
    "body": "Also should have \n\n\n```\nsage: f(x) = x^2\nsage: f + sin\nx |--> sin(x) + x^2\n```\n",
    "created_at": "2007-09-13T09:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3339",
    "user": "@robertwb"
}
```

Also should have 


```
sage: f(x) = x^2
sage: f + sin
x |--> sin(x) + x^2
```




---

archive/issue_comments_003340.json:
```json
{
    "body": "See much discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/2f627fbe8d0f71c0",
    "created_at": "2007-09-13T09:13:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3340",
    "user": "@robertwb"
}
```

See much discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/2f627fbe8d0f71c0



---

archive/issue_comments_003341.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-01T06:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3341",
    "user": "@mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_003342.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-12-01T06:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3342",
    "user": "@mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_003343.json:
```json
{
    "body": "This patch should be applied after #644.",
    "created_at": "2007-12-01T06:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3343",
    "user": "@mwhansen"
}
```

This patch should be applied after #644.



---

archive/issue_comments_003344.json:
```json
{
    "body": "Attachment [644.patch](tarball://root/attachments/some-uuid/ticket644/644.patch) by mabshoff created at 2007-12-01 16:16:45\n\nMerged in 2.8.15.alpha1.",
    "created_at": "2007-12-01T16:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3344",
    "user": "mabshoff"
}
```

Attachment [644.patch](tarball://root/attachments/some-uuid/ticket644/644.patch) by mabshoff created at 2007-12-01 16:16:45

Merged in 2.8.15.alpha1.



---

archive/issue_comments_003345.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T16:16:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/644",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/644#issuecomment-3345",
    "user": "mabshoff"
}
```

Resolution: fixed
