# Issue 2650: matrix() constructor with empty dictionary returns non-empty matrix

archive/issues_002650.json:
```json
{
    "body": "Assignee: was\n\nThis ticket depends on the patch from ticket #2649, without which an exception is raised.\n\nThe following code\n\n```\nsage: matrix({})\n```\n\nreturns the matrix [0].  I think it should return [].\n\nIssue created by migration from https://trac.sagemath.org/ticket/2650\n\n",
    "created_at": "2008-03-22T19:31:04Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "title": "matrix() constructor with empty dictionary returns non-empty matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2650",
    "user": "rhinton"
}
```
Assignee: was

This ticket depends on the patch from ticket #2649, without which an exception is raised.

The following code

```
sage: matrix({})
```

returns the matrix [0].  I think it should return [].

Issue created by migration from https://trac.sagemath.org/ticket/2650





---

archive/issue_comments_018212.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-23T02:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2650#issuecomment-18212",
    "user": "rhinton"
}
```

Resolution: duplicate



---

archive/issue_comments_018213.json:
```json
{
    "body": "subsumed by #2651",
    "created_at": "2008-03-23T02:16:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2650",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2650#issuecomment-18213",
    "user": "rhinton"
}
```

subsumed by #2651
