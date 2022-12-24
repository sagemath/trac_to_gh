# Issue 6932: jordan_form with transformation=true fails on a 1x1 matrix.

archive/issues_006932.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: jordan_form\n\nThe following code fails:\n\n```\nM=Matrix(1,1,[1])\nM.jordan_form(transformation=True)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6932\n\n",
    "created_at": "2009-09-15T05:54:37Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "jordan_form with transformation=true fails on a 1x1 matrix.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6932",
    "user": "@syazdani77"
}
```
Assignee: tbd

Keywords: jordan_form

The following code fails:

```
M=Matrix(1,1,[1])
M.jordan_form(transformation=True)
```



Issue created by migration from https://trac.sagemath.org/ticket/6932





---

archive/issue_comments_057284.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2009-11-15T13:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57284",
    "user": "@aghitza"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_057285.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T12:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57285",
    "user": "spancratz"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057286.json:
```json
{
    "body": "This is fixed by the patch at ticket #6942.  Once that ticket receives a positive review, this ticket can be closed.",
    "created_at": "2010-01-19T12:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57286",
    "user": "spancratz"
}
```

This is fixed by the patch at ticket #6942.  Once that ticket receives a positive review, this ticket can be closed.



---

archive/issue_comments_057287.json:
```json
{
    "body": "I checked with sage-4.3.3, and we indeed get the correct rank (7) for #6942, thus I guess we can\nindeed close that ticket:\n\n```\nsage: M=Matrix(1,1,[1])\nsage: M.jordan_form(transformation=True)\n([1], [1])\n```\n",
    "created_at": "2010-02-25T22:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57287",
    "user": "@zimmermann6"
}
```

I checked with sage-4.3.3, and we indeed get the correct rank (7) for #6942, thus I guess we can
indeed close that ticket:

```
sage: M=Matrix(1,1,[1])
sage: M.jordan_form(transformation=True)
([1], [1])
```




---

archive/issue_comments_057288.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-25T22:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57288",
    "user": "@zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057289.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T04:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57289",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057290.json:
```json
{
    "body": "Close as fixed by #6942.",
    "created_at": "2010-03-03T04:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57290",
    "user": "mvngu"
}
```

Close as fixed by #6942.
