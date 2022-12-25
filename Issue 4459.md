# Issue 4459: preparser incorrectly identifies integer methods that start with e

archive/issues_004459.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nsage: 3.exp()\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     RealNumber('3.e')xp()\n                       ^\nSyntaxError: invalid syntax\n\nsage: 3.is_square()\nFalse\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4459\n\n",
    "created_at": "2008-11-07T03:19:02Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "preparser incorrectly identifies integer methods that start with e",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4459",
    "user": "https://github.com/mwhansen"
}
```
Assignee: cwitty


```
sage: 3.exp()
------------------------------------------------------------
   File "<ipython console>", line 1
     RealNumber('3.e')xp()
                       ^
SyntaxError: invalid syntax

sage: 3.is_square()
False
```



Issue created by migration from https://trac.sagemath.org/ticket/4459





---

archive/issue_comments_032841.json:
```json
{
    "body": "The same thing happens for those that start with 'r':\n\n\n```\nsage: 3.rational_reconstruction()\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     3.ational_reconstruction()\n```\n",
    "created_at": "2008-11-07T03:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4459#issuecomment-32841",
    "user": "https://github.com/mwhansen"
}
```

The same thing happens for those that start with 'r':


```
sage: 3.rational_reconstruction()
------------------------------------------------------------
   File "<ipython console>", line 1
     3.ational_reconstruction()
```




---

archive/issue_comments_032842.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-23T22:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4459#issuecomment-32842",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Resolution: duplicate



---

archive/issue_comments_032843.json:
```json
{
    "body": "Rolled into #5079",
    "created_at": "2009-01-23T22:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4459#issuecomment-32843",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Rolled into #5079



---

archive/issue_events_004705.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2009-01-23T22:30:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4459",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4459#event-4705"
}
```
