# Issue 4459: preparser incorrectly identifies integer methods that start with e

archive/issues_004459.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nsage: 3.exp()\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     RealNumber('3.e')xp()\n                       ^\nSyntaxError: invalid syntax\n\nsage: 3.is_square()\nFalse\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4459\n\n",
    "created_at": "2008-11-07T03:19:02Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "preparser incorrectly identifies integer methods that start with e",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4459",
    "user": "mhansen"
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

archive/issue_comments_032905.json:
```json
{
    "body": "The same thing happens for those that start with 'r':\n\n\n```\nsage: 3.rational_reconstruction()\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     3.ational_reconstruction()\n```\n",
    "created_at": "2008-11-07T03:21:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4459#issuecomment-32905",
    "user": "mhansen"
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

archive/issue_comments_032906.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-23T22:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4459#issuecomment-32906",
    "user": "boothby"
}
```

Resolution: duplicate



---

archive/issue_comments_032907.json:
```json
{
    "body": "Rolled into #5079",
    "created_at": "2009-01-23T22:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4459",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4459#issuecomment-32907",
    "user": "boothby"
}
```

Rolled into #5079
