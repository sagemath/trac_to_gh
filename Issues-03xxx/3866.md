# Issue 3866: [with patch, not ready for review] Create a 2d locator interact widget

archive/issues_003866.json:
```json
{
    "body": "Assignee: @itolkov\n\nThis is a *very* *extremely* rough-cut of a 2d locator widget.  All the docstrings are blatantly wrong and the code is full of ugly things.  But it works, sort of.  It's a starting point for someone to finish.\n\nAn example:\n\n```\n@interact\ndef _(pos=locator(3)):\n    print pos\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3866\n\n",
    "closed_at": "2018-05-18T17:16:26Z",
    "created_at": "2008-08-15T03:46:33Z",
    "labels": [
        "component: interact"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, not ready for review] Create a 2d locator interact widget",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3866",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @itolkov

This is a *very* *extremely* rough-cut of a 2d locator widget.  All the docstrings are blatantly wrong and the code is full of ugly things.  But it works, sort of.  It's a starting point for someone to finish.

An example:

```
@interact
def _(pos=locator(3)):
    print pos
```


Issue created by migration from https://trac.sagemath.org/ticket/3866





---

archive/issue_comments_027499.json:
```json
{
    "body": "Attachment [locator.patch](tarball://root/attachments/some-uuid/ticket3866/locator.patch) by @jasongrout created at 2008-08-15 03:48:16",
    "created_at": "2008-08-15T03:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27499",
    "user": "https://github.com/jasongrout"
}
```

Attachment [locator.patch](tarball://root/attachments/some-uuid/ticket3866/locator.patch) by @jasongrout created at 2008-08-15 03:48:16



---

archive/issue_comments_027500.json:
```json
{
    "body": "Hi Jason,\n\ndoes this patch need a review?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-15T05:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27500",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Jason,

does this patch need a review?

Cheers,

Michael



---

archive/issue_comments_027501.json:
```json
{
    "body": "No, not yet; definitely not yet.  I'm embarrassed to post the patch as it was; I only posted it because I was more embarrassed by almost losing the patch (I just barely found it).",
    "created_at": "2008-08-15T07:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27501",
    "user": "https://github.com/jasongrout"
}
```

No, not yet; definitely not yet.  I'm embarrassed to post the patch as it was; I only posted it because I was more embarrassed by almost losing the patch (I just barely found it).



---

archive/issue_comments_027502.json:
```json
{
    "body": "I am thinking of giving this to a student of mine for an independent study project.  To avoid duplication of effort I would appreciate being informed of any independent effort on it.\n\nThanks,\nMarshall Hampton",
    "created_at": "2008-12-30T18:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27502",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I am thinking of giving this to a student of mine for an independent study project.  To avoid duplication of effort I would appreciate being informed of any independent effort on it.

Thanks,
Marshall Hampton



---

archive/issue_comments_027503.json:
```json
{
    "body": "Attachment [trac_3866_4.0.1_rebase.patch](tarball://root/attachments/some-uuid/ticket3866/trac_3866_4.0.1_rebase.patch) by mhampton created at 2009-06-11 23:01:08\n\nrebase against 4.0.1, along with some very minor cleanup",
    "created_at": "2009-06-11T23:01:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27503",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_3866_4.0.1_rebase.patch](tarball://root/attachments/some-uuid/ticket3866/trac_3866_4.0.1_rebase.patch) by mhampton created at 2009-06-11 23:01:08

rebase against 4.0.1, along with some very minor cleanup



---

archive/issue_comments_027504.json:
```json
{
    "body": "It looks like my student didn't get very far, unfortunately.  I will attempt to improve this further, but I am attaching a rebased (and slightly cleaned-up) patch in case other people want to move ahead faster.",
    "created_at": "2009-06-11T23:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27504",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

It looks like my student didn't get very far, unfortunately.  I will attempt to improve this further, but I am attaching a rebased (and slightly cleaned-up) patch in case other people want to move ahead faster.



---

archive/issue_comments_027505.json:
```json
{
    "body": "There is a bounty for a feature like this:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/4b52ee22e227370d/a5347db58d549c71?lnk=gst&q=locator#a5347db58d549c71",
    "created_at": "2010-08-13T04:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27505",
    "user": "https://github.com/jasongrout"
}
```

There is a bounty for a feature like this:

http://groups.google.com/group/sage-devel/browse_thread/thread/4b52ee22e227370d/a5347db58d549c71?lnk=gst&q=locator#a5347db58d549c71



---

archive/issue_events_008869.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3866#event-8869"
}
```



---

archive/issue_events_008870.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3866#event-8870"
}
```



---

archive/issue_events_008871.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3866#event-8871"
}
```



---

archive/issue_events_008872.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3866#event-8872"
}
```



---

archive/issue_events_008873.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3866#event-8873"
}
```



---

archive/issue_events_008874.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3866#event-8874"
}
```



---

archive/issue_events_008875.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3866#event-8875"
}
```



---

archive/issue_comments_027506.json:
```json
{
    "body": "Given that the legacy-notebook is no longer maintained or developed, let us close that old ticket.",
    "created_at": "2018-04-30T08:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27506",
    "user": "https://github.com/fchapoton"
}
```

Given that the legacy-notebook is no longer maintained or developed, let us close that old ticket.



---

archive/issue_events_008876.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2018-04-30T08:50:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3866#event-8876"
}
```



---

archive/issue_events_008877.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2018-04-30T08:50:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3866#event-8877"
}
```



---

archive/issue_comments_027507.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2018-04-30T08:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27507",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_027508.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2018-05-01T12:31:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27508",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_027509.json:
```json
{
    "body": "closing positively reviewed duplicates",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27509",
    "user": "https://github.com/videlec"
}
```

closing positively reviewed duplicates



---

archive/issue_events_008878.json:
```json
{
    "actor": "https://github.com/videlec",
    "created_at": "2018-05-18T17:16:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3866#event-8878"
}
```



---

archive/issue_comments_027510.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2018-05-18T17:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3866",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3866#issuecomment-27510",
    "user": "https://github.com/videlec"
}
```

Resolution: wontfix
