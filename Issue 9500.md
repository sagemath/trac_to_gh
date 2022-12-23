# Issue 9500: implement inversion of elements in a (more) general quotient ring

archive/issues_009500.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nMake this work:\n\n\n```\n\n            sage: R.<x,y> = QQ[]\n            sage: I = R.ideal([x^2 + 1, y^3 - 2])\n            sage: S.<i,cuberoot> = R.quotient(I)\n            sage: 1/(1+i)\n            -1/2*i + 1/2\n\n        Confirm via symbolic computation::\n        \n            sage: 1/(1+sqrt(-1))\n            -1/2*I + 1/2\n\n        Another more complicated quotient::\n        \n            sage: b = 1/(i+cuberoot); b\n            1/5*i*cuberoot^2 - 2/5*i*cuberoot + 2/5*cuberoot^2 - 1/5*i + 1/5*cuberoot - 2/5\n            sage: b*(i+cuberoot)\n            1\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9500\n\n",
    "created_at": "2010-07-14T17:08:14Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "implement inversion of elements in a (more) general quotient ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9500",
    "user": "was"
}
```
Assignee: AlexGhitza

Make this work:


```

            sage: R.<x,y> = QQ[]
            sage: I = R.ideal([x^2 + 1, y^3 - 2])
            sage: S.<i,cuberoot> = R.quotient(I)
            sage: 1/(1+i)
            -1/2*i + 1/2

        Confirm via symbolic computation::
        
            sage: 1/(1+sqrt(-1))
            -1/2*I + 1/2

        Another more complicated quotient::
        
            sage: b = 1/(i+cuberoot); b
            1/5*i*cuberoot^2 - 2/5*i*cuberoot + 2/5*cuberoot^2 - 1/5*i + 1/5*cuberoot - 2/5
            sage: b*(i+cuberoot)
            1
```


Issue created by migration from https://trac.sagemath.org/ticket/9500





---

archive/issue_comments_091227.json:
```json
{
    "body": "Relevant benchmarks: http://wiki.sagemath.org/days23.5/projects/relative_number_fields",
    "created_at": "2010-07-14T19:45:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9500#issuecomment-91227",
    "user": "was"
}
```

Relevant benchmarks: http://wiki.sagemath.org/days23.5/projects/relative_number_fields



---

archive/issue_comments_091228.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-14T20:29:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9500#issuecomment-91228",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_091229.json:
```json
{
    "body": "#9499 needs to be finished before this can be reviewed.",
    "created_at": "2010-07-14T20:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9500#issuecomment-91229",
    "user": "was"
}
```

#9499 needs to be finished before this can be reviewed.



---

archive/issue_comments_091230.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-14T20:30:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9500#issuecomment-91230",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091231.json:
```json
{
    "body": "Patch look good and applies cleanly to 4.4.4 +#9499 (which is required).",
    "created_at": "2010-07-14T23:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9500#issuecomment-91231",
    "user": "malb"
}
```

Patch look good and applies cleanly to 4.4.4 +#9499 (which is required).



---

archive/issue_comments_091232.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-14T23:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9500#issuecomment-91232",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091233.json:
```json
{
    "body": "Doctests pass.",
    "created_at": "2010-07-14T23:05:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9500#issuecomment-91233",
    "user": "malb"
}
```

Doctests pass.



---

archive/issue_comments_091234.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:32:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9500#issuecomment-91234",
    "user": "mpatel"
}
```

Resolution: fixed
