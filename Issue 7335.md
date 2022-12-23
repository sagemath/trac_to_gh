# Issue 7335: tachyon fails to build on Cygwin

archive/issues_007335.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  was\n\nIt fails with the following error\n\n\n```\ncc1: error: unrecognized command line option \"-mpentium\"\n```\n\n\nThe fix is simply to simply remove that part of the flags from the Make-arch file for the win32 target.\n\nI will post an updated spkg shortly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7335\n\n",
    "created_at": "2009-10-28T19:33:41Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "title": "tachyon fails to build on Cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7335",
    "user": "mhansen"
}
```
Assignee: tbd

CC:  was

It fails with the following error


```
cc1: error: unrecognized command line option "-mpentium"
```


The fix is simply to simply remove that part of the flags from the Make-arch file for the win32 target.

I will post an updated spkg shortly.

Issue created by migration from https://trac.sagemath.org/ticket/7335





---

archive/issue_comments_061377.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-06T05:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61377",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061378.json:
```json
{
    "body": "There is an spkg at http://sage.math.washington.edu/home/mhansen/tachyon-0.98beta.p10.spkg",
    "created_at": "2009-11-06T05:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61378",
    "user": "mhansen"
}
```

There is an spkg at http://sage.math.washington.edu/home/mhansen/tachyon-0.98beta.p10.spkg



---

archive/issue_comments_061379.json:
```json
{
    "body": "It works.",
    "created_at": "2009-11-06T06:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61379",
    "user": "was"
}
```

It works.



---

archive/issue_comments_061380.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-06T06:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61380",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061381.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61381",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_061382.json:
```json
{
    "body": "#11504 is this again.\n\nI couldn't extract this properly (it tried, and looked right, but then had 'x's next to everything and was not a folder).\n\nAnyway, the fix is the same.",
    "created_at": "2011-06-16T16:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61382",
    "user": "kcrisman"
}
```

#11504 is this again.

I couldn't extract this properly (it tried, and looked right, but then had 'x's next to everything and was not a folder).

Anyway, the fix is the same.
