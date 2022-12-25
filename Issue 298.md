# Issue 298: autotesting of examples

archive/issues_000298.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kini @jdemeyer\n\n* get Rishi's autotesting of examples directory to work: He developed it under OS X, but it doesn't work on Linux because of differences in how they run scripts, etc.  Plus, it's a really hard challenge to create such automated testing, so it needs to be looked over again.  \n \n\nIssue created by migration from https://trac.sagemath.org/ticket/298\n\n",
    "created_at": "2007-02-27T02:21:54Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "autotesting of examples",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/298",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @kini @jdemeyer

* get Rishi's autotesting of examples directory to work: He developed it under OS X, but it doesn't work on Linux because of differences in how they run scripts, etc.  Plus, it's a really hard challenge to create such automated testing, so it needs to be looked over again.  
 

Issue created by migration from https://trac.sagemath.org/ticket/298





---

archive/issue_events_000689.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-09-11T02:40:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/298#event-689"
}
```



---

archive/issue_comments_001409.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-04-19T21:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/298#issuecomment-1409",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_001410.json:
```json
{
    "body": "Where is that code? Does that mean that we want to be able to run the doctests in examples? Then certainly this ought to be of much higher priority since the examples *must* work with the version of Sage that shipped it.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-19T21:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/298#issuecomment-1410",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Where is that code? Does that mean that we want to be able to run the doctests in examples? Then certainly this ought to be of much higher priority since the examples *must* work with the version of Sage that shipped it.

Cheers,

Michael



---

archive/issue_comments_001411.json:
```json
{
    "body": "This looks invalid or maybe even done.",
    "created_at": "2009-11-19T22:42:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/298#issuecomment-1411",
    "user": "https://github.com/jasongrout"
}
```

This looks invalid or maybe even done.



---

archive/issue_comments_001412.json:
```json
{
    "body": "\n```\nwstein:\nWhy do you think #298 should be closed?\n[2:45pm] wstein:\nIt's more important than ever to fix.\n[2:45pm] jason-:\nI thought it was talking about doctesting, basically\n[2:45pm] wstein:\nThere is a directory SAGE_ROOT/examples.\n[2:45pm] wstein:\nThat code isn't tested at all.\n[2:45pm] jason-:\nto quote the comment, \"where is that code\"?\n[2:45pm] wstein:\nIt's a terrifying disaster.\n[2:45pm] jason-:\noh, okay\n[2:45pm] jason-:\nnever mind\n[2:46pm] wstein:\nI can't believe I still haven't dealt with this... but oh well.\n[2:46pm] wstein:\nIt's one of those things that looks easy until you try it.\n```\n",
    "created_at": "2009-11-19T22:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/298#issuecomment-1412",
    "user": "https://github.com/williamstein"
}
```


```
wstein:
Why do you think #298 should be closed?
[2:45pm] wstein:
It's more important than ever to fix.
[2:45pm] jason-:
I thought it was talking about doctesting, basically
[2:45pm] wstein:
There is a directory SAGE_ROOT/examples.
[2:45pm] wstein:
That code isn't tested at all.
[2:45pm] jason-:
to quote the comment, "where is that code"?
[2:45pm] wstein:
It's a terrifying disaster.
[2:45pm] jason-:
oh, okay
[2:45pm] jason-:
never mind
[2:46pm] wstein:
I can't believe I still haven't dealt with this... but oh well.
[2:46pm] wstein:
It's one of those things that looks easy until you try it.
```




---

archive/issue_comments_001413.json:
```json
{
    "body": "See the related ticket #7494.  If that is closed, then this ticket is certainly invalid.",
    "created_at": "2009-11-19T23:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/298#issuecomment-1413",
    "user": "https://github.com/williamstein"
}
```

See the related ticket #7494.  If that is closed, then this ticket is certainly invalid.



---

archive/issue_comments_001414.json:
```json
{
    "body": "Since #7494 has been closed, I think this can be, too.",
    "created_at": "2011-10-08T17:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/298#issuecomment-1414",
    "user": "https://github.com/jhpalmieri"
}
```

Since #7494 has been closed, I think this can be, too.



---

archive/issue_comments_001415.json:
```json
{
    "body": "Yes.",
    "created_at": "2011-10-10T09:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/298#issuecomment-1415",
    "user": "https://github.com/kini"
}
```

Yes.



---

archive/issue_comments_001416.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-10-10T09:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/298#issuecomment-1416",
    "user": "https://github.com/kini"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_001417.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-10-10T09:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/298#issuecomment-1417",
    "user": "https://github.com/kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_000690.json:
```json
{
    "actor": "https://github.com/nexttime",
    "created_at": "2011-10-10T12:28:07Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "milestone": "sage-feature",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/298#event-690"
}
```



---

archive/issue_events_000691.json:
```json
{
    "actor": "https://github.com/nexttime",
    "created_at": "2011-10-10T12:28:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/298#event-691"
}
```



---

archive/issue_events_000692.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-10-10T13:35:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/298#event-692"
}
```



---

archive/issue_comments_001418.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2011-10-10T13:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/298#issuecomment-1418",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: wontfix
