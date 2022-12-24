# Issue 597: Why are single-argument arithmetic functions in the coercion model?

archive/issues_000597.json:
```json
{
    "body": "Assignee: somebody\n\nIs there any advantage to having _neg_c/_neg_/_neg_c_imple as opposed to overriding __neg__? \n\nIssue created by migration from https://trac.sagemath.org/ticket/597\n\n",
    "created_at": "2007-09-06T00:52:14Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Why are single-argument arithmetic functions in the coercion model?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/597",
    "user": "robertwb"
}
```
Assignee: somebody

Is there any advantage to having _neg_c/_neg_/_neg_c_imple as opposed to overriding __neg__? 

Issue created by migration from https://trac.sagemath.org/ticket/597





---

archive/issue_comments_003084.json:
```json
{
    "body": "Now that cpdef methods are used, one can just implement `__neg__` and `__inverse__`, we don't need this infrastructure for unary operations (and it slows them down). \n\nWe should do a full search of the source.",
    "created_at": "2008-11-14T07:12:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/597#issuecomment-3084",
    "user": "robertwb"
}
```

Now that cpdef methods are used, one can just implement `__neg__` and `__inverse__`, we don't need this infrastructure for unary operations (and it slows them down). 

We should do a full search of the source.



---

archive/issue_comments_003085.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-11-14T08:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/597#issuecomment-3085",
    "user": "mhansen"
}
```

Resolution: duplicate



---

archive/issue_comments_003086.json:
```json
{
    "body": "This is a now duplicate of #2072, which is more recent.",
    "created_at": "2008-11-14T08:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/597",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/597#issuecomment-3086",
    "user": "mhansen"
}
```

This is a now duplicate of #2072, which is more recent.
