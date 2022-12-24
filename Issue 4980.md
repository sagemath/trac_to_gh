# Issue 4980: add info about slices to developer guide

archive/issues_004980.json:
```json
{
    "body": "Assignee: tba\n\nSomewhere we should note the standard way to deal with getting the indices from a slice object is\n\n\n```\nrange(*s.indices(size))\n```\n\n\nwhere s is our slice and size is the size of the object we are applying the slice to.  See #4974 for lots of other information and discussion of various ways to do this, converging on the above simply standard python.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4980\n\n",
    "created_at": "2009-01-15T06:12:26Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "add info about slices to developer guide",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4980",
    "user": "jason"
}
```
Assignee: tba

Somewhere we should note the standard way to deal with getting the indices from a slice object is


```
range(*s.indices(size))
```


where s is our slice and size is the size of the object we are applying the slice to.  See #4974 for lots of other information and discussion of various ways to do this, converging on the above simply standard python.

Issue created by migration from https://trac.sagemath.org/ticket/4980





---

archive/issue_comments_037966.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-01-17T09:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4980#issuecomment-37966",
    "user": "timdumol"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_037967.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2014-11-20T16:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4980#issuecomment-37967",
    "user": "kcrisman"
}
```

Changing priority from major to minor.
