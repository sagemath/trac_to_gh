# Issue 6932: jordan_form with transformation=true fails on a 1x1 matrix.

archive/issues_006932.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: jordan_form\n\nThe following code fails:\n\n```\nM=Matrix(1,1,[1])\nM.jordan_form(transformation=True)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6932\n\n",
    "created_at": "2009-09-15T05:54:37Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "jordan_form with transformation=true fails on a 1x1 matrix.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6932",
    "user": "https://github.com/syazdani77"
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

archive/issue_comments_057176.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2009-11-15T13:10:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57176",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_057177.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T12:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57177",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057178.json:
```json
{
    "body": "This is fixed by the patch at ticket #6942.  Once that ticket receives a positive review, this ticket can be closed.",
    "created_at": "2010-01-19T12:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57178",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

This is fixed by the patch at ticket #6942.  Once that ticket receives a positive review, this ticket can be closed.



---

archive/issue_comments_057179.json:
```json
{
    "body": "I checked with sage-4.3.3, and we indeed get the correct rank (7) for #6942, thus I guess we can\nindeed close that ticket:\n\n```\nsage: M=Matrix(1,1,[1])\nsage: M.jordan_form(transformation=True)\n([1], [1])\n```\n",
    "created_at": "2010-02-25T22:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57179",
    "user": "https://github.com/zimmermann6"
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

archive/issue_comments_057180.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-25T22:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57180",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057181.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T04:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57181",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057182.json:
```json
{
    "body": "Close as fixed by #6942.",
    "created_at": "2010-03-03T04:11:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6932#issuecomment-57182",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed by #6942.



---

archive/issue_events_007155.json:
```json
{
    "actor": "mvngu",
    "created_at": "2010-03-03T04:11:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6932",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6932#event-7155"
}
```
