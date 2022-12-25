# Issue 999: add optional sloccount script to sage-dist

archive/issues_000999.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: sloccount sage-dist\n\nsloccount measures the total numbers of lines in a project and estimates the time as well as amount of money needed to create the project. It also creates nice html output - for an example see\n\nhttp://sage.math.washington.edu/home/mabshoff/2.8.9.rc1-sloccount.html\n\nIt would be nice to have an optional script that would automatically create the output for the whole sage project.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/999\n\n",
    "closed_at": "2013-06-19T12:21:29Z",
    "created_at": "2007-10-25T16:37:13Z",
    "labels": [
        "component: distribution"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "add optional sloccount script to sage-dist",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/999",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Keywords: sloccount sage-dist

sloccount measures the total numbers of lines in a project and estimates the time as well as amount of money needed to create the project. It also creates nice html output - for an example see

http://sage.math.washington.edu/home/mabshoff/2.8.9.rc1-sloccount.html

It would be nice to have an optional script that would automatically create the output for the whole sage project.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/999





---

archive/issue_comments_006061.json:
```json
{
    "body": "To include the GAP code which is written in GAP, you need to count the lines in the *.gi files\nas well. I don't know if you can exclude all lines beginning with a # or not (these would be\ncomments or documentation).",
    "created_at": "2007-10-25T16:51:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/999#issuecomment-6061",
    "user": "https://github.com/wdjoyner"
}
```

To include the GAP code which is written in GAP, you need to count the lines in the *.gi files
as well. I don't know if you can exclude all lines beginning with a # or not (these would be
comments or documentation).



---

archive/issue_comments_006062.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-25T17:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/999#issuecomment-6062",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006063.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-02-03T02:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/999#issuecomment-6063",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_006064.json:
```json
{
    "body": "I don't think we need such a thing...",
    "created_at": "2013-06-13T12:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/999#issuecomment-6064",
    "user": "https://github.com/jdemeyer"
}
```

I don't think we need such a thing...



---

archive/issue_events_002748.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-06-13T12:27:05Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/999",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/999#event-2748"
}
```



---

archive/issue_comments_006065.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-13T12:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/999#issuecomment-6065",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_006066.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-13T12:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/999#issuecomment-6066",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_002749.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-06-19T12:21:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/999",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/999#event-2749"
}
```



---

archive/issue_comments_006067.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2013-06-19T12:21:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/999#issuecomment-6067",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: wontfix
