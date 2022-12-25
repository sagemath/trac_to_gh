# Issue 7335: tachyon fails to build on Cygwin

archive/issues_007335.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein\n\nIt fails with the following error\n\n\n```\ncc1: error: unrecognized command line option \"-mpentium\"\n```\n\n\nThe fix is simply to simply remove that part of the flags from the Make-arch file for the win32 target.\n\nI will post an updated spkg shortly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7335\n\n",
    "created_at": "2009-10-28T19:33:41Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "tachyon fails to build on Cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7335",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

CC:  @williamstein

It fails with the following error


```
cc1: error: unrecognized command line option "-mpentium"
```


The fix is simply to simply remove that part of the flags from the Make-arch file for the win32 target.

I will post an updated spkg shortly.

Issue created by migration from https://trac.sagemath.org/ticket/7335





---

archive/issue_comments_061264.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-06T05:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61264",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061265.json:
```json
{
    "body": "There is an spkg at http://sage.math.washington.edu/home/mhansen/tachyon-0.98beta.p10.spkg",
    "created_at": "2009-11-06T05:08:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61265",
    "user": "https://github.com/mwhansen"
}
```

There is an spkg at http://sage.math.washington.edu/home/mhansen/tachyon-0.98beta.p10.spkg



---

archive/issue_comments_061266.json:
```json
{
    "body": "It works.",
    "created_at": "2009-11-06T06:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61266",
    "user": "https://github.com/williamstein"
}
```

It works.



---

archive/issue_comments_061267.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-06T06:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61267",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061268.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61268",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007557.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-11-12T06:16:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7335#event-7557"
}
```



---

archive/issue_comments_061269.json:
```json
{
    "body": "#11504 is this again.\n\nI couldn't extract this properly (it tried, and looked right, but then had 'x's next to everything and was not a folder).\n\nAnyway, the fix is the same.",
    "created_at": "2011-06-16T16:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7335#issuecomment-61269",
    "user": "https://github.com/kcrisman"
}
```

#11504 is this again.

I couldn't extract this properly (it tried, and looked right, but then had 'x's next to everything and was not a folder).

Anyway, the fix is the same.
