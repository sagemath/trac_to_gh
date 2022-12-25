# Issue 1534: Purge java3d from extcode

archive/issues_001534.json:
```json
{
    "body": "Assignee: @robertwb\n\nOnce #1533 is done, we need to remove the files from extcode. This should be done is such a way that the history of the (several MB) jar files is purged, I'm still looking for the best way to do this. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1534\n\n",
    "closed_at": "2014-08-29T18:33:34Z",
    "created_at": "2007-12-16T07:24:54Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Purge java3d from extcode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1534",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb

Once #1533 is done, we need to remove the files from extcode. This should be done is such a way that the history of the (several MB) jar files is purged, I'm still looking for the best way to do this. 

Issue created by migration from https://trac.sagemath.org/ticket/1534





---

archive/issue_comments_009765.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2007-12-16T07:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9765",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_009766.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-16T07:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9766",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009767.json:
```json
{
    "body": "See http://www.selenic.com/pipermail/mercurial/2007-May/013256.html for some brief discussion of the question.  The answer seems to be to use \"hg clone -r\" and \"hg transplant\".\n\nBe sure to test \"sage -upgrade\" when you make this change.",
    "created_at": "2007-12-16T19:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9767",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

See http://www.selenic.com/pipermail/mercurial/2007-May/013256.html for some brief discussion of the question.  The answer seems to be to use "hg clone -r" and "hg transplant".

Be sure to test "sage -upgrade" when you make this change.



---

archive/issue_comments_009768.json:
```json
{
    "body": "Looks good. We need to make sure that if developers work on extcode they don't merge this stuff back in though.",
    "created_at": "2007-12-17T18:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9768",
    "user": "https://github.com/robertwb"
}
```

Looks good. We need to make sure that if developers work on extcode they don't merge this stuff back in though.



---

archive/issue_comments_009769.json:
```json
{
    "body": "I had lots of problems trying to use hg transplant, which just doesn't work for me.\n\ncwitty remarks: Looks like what we really want is http://www.selenic.com/pipermail/mercurial/2006-June/008878.html ; too bad it seems like nobody's touched it since mid-2006.",
    "created_at": "2008-01-19T18:38:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9769",
    "user": "https://github.com/williamstein"
}
```

I had lots of problems trying to use hg transplant, which just doesn't work for me.

cwitty remarks: Looks like what we really want is http://www.selenic.com/pipermail/mercurial/2006-June/008878.html ; too bad it seems like nobody's touched it since mid-2006.



---

archive/issue_comments_009770.json:
```json
{
    "body": "Changing type from defect to task.",
    "created_at": "2010-03-17T05:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9770",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to task.



---

archive/issue_events_003867.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:34:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1534#event-3867"
}
```



---

archive/issue_events_003868.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1534#event-3868"
}
```



---

archive/issue_events_003869.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1534#event-3869"
}
```



---

archive/issue_events_003870.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1534#event-3870"
}
```



---

archive/issue_events_003871.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:19:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1534#event-3871"
}
```



---

archive/issue_events_003872.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1534#event-3872"
}
```



---

archive/issue_events_003873.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1534#event-3873"
}
```



---

archive/issue_comments_009771.json:
```json
{
    "body": "There is no java3d in SAGE_EXTCODE.",
    "created_at": "2014-08-19T16:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9771",
    "user": "https://github.com/a-andre"
}
```

There is no java3d in SAGE_EXTCODE.



---

archive/issue_comments_009772.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-19T16:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9772",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_events_003874.json:
```json
{
    "actor": "https://github.com/a-andre",
    "created_at": "2014-08-19T16:45:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1534#event-3874"
}
```



---

archive/issue_events_003875.json:
```json
{
    "actor": "https://github.com/a-andre",
    "created_at": "2014-08-19T16:45:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1534#event-3875"
}
```



---

archive/issue_comments_009773.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-08-26T19:24:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9773",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_009774.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-08-29T18:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1534#issuecomment-9774",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_003876.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-08-29T18:33:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1534",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1534#event-3876"
}
```
