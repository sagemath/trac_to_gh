# Issue 7329: Make integration of vectors work (component-wise)

archive/issues_007329.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  rbeezer kcrisman\n\nIt would be great if this worked:\n\n\n```\n            sage: t=var('t')                      \n            sage: r=vector([t,t^2,sin(t)])\n            sage: integrate(r,t)\n            (1/2*t^2, 1/3*t^3, -cos(t))\n            sage: integrate(r,(t,0,1))\n            (1/2, 1/3, -cos(1) + 1)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7329\n\n",
    "created_at": "2009-10-28T02:46:06Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "title": "Make integration of vectors work (component-wise)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7329",
    "user": "jason"
}
```
Assignee: burcin

CC:  rbeezer kcrisman

It would be great if this worked:


```
            sage: t=var('t')                      
            sage: r=vector([t,t^2,sin(t)])
            sage: integrate(r,t)
            (1/2*t^2, 1/3*t^3, -cos(t))
            sage: integrate(r,(t,0,1))
            (1/2, 1/3, -cos(1) + 1)
```



Issue created by migration from https://trac.sagemath.org/ticket/7329





---

archive/issue_comments_061293.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-10-28T04:26:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7329#issuecomment-61293",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_061294.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-28T04:27:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7329#issuecomment-61294",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061295.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-28T05:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7329#issuecomment-61295",
    "user": "rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061296.json:
```json
{
    "body": "Looks real good (and useful).\n\nBuilds fine, passes tests in sage/modules/module_element.py, behaves as expected, docs look good.\n\nPositive review.",
    "created_at": "2009-10-28T05:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7329#issuecomment-61296",
    "user": "rbeezer"
}
```

Looks real good (and useful).

Builds fine, passes tests in sage/modules/module_element.py, behaves as expected, docs look good.

Positive review.



---

archive/issue_comments_061297.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T16:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7329#issuecomment-61297",
    "user": "mhansen"
}
```

Resolution: fixed
