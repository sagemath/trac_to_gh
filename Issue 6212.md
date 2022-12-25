# Issue 6212: make sage -upgrade check that there are no applied hg queue patches

archive/issues_006212.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jasongrout jthurber\n\nKeywords: sage upgrade applied hg queue\n\nIt would be nice if sage -upgrade aborted if are applied hg queue patches, in the same way it aborts if there are local changes.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6212\n\n",
    "closed_at": "2014-03-19T04:35:53Z",
    "created_at": "2009-06-04T20:40:01Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make sage -upgrade check that there are no applied hg queue patches",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6212",
    "user": "https://github.com/ncalexan"
}
```
Assignee: tbd

CC:  @jasongrout jthurber

Keywords: sage upgrade applied hg queue

It would be nice if sage -upgrade aborted if are applied hg queue patches, in the same way it aborts if there are local changes.

Issue created by migration from https://trac.sagemath.org/ticket/6212





---

archive/issue_comments_049534.json:
```json
{
    "body": "Even better:\n\n```\n[1:38pm] jason-: you have patches that are applied using mercurial queues.  Do you want to pop all of the patches? [y/n]\n[1:38pm] jason-: yes would pop and continue the upgrae\n[1:39pm] jason-: no would quit the upgrade\n```",
    "created_at": "2009-06-04T20:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6212#issuecomment-49534",
    "user": "https://github.com/ncalexan"
}
```

Even better:

```
[1:38pm] jason-: you have patches that are applied using mercurial queues.  Do you want to pop all of the patches? [y/n]
[1:38pm] jason-: yes would pop and continue the upgrae
[1:39pm] jason-: no would quit the upgrade
```



---

archive/issue_events_014567.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6212",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6212#event-14567"
}
```



---

archive/issue_events_014568.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6212",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6212#event-14568"
}
```



---

archive/issue_events_014569.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6212",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6212#event-14569"
}
```



---

archive/issue_comments_049535.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-14T16:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6212#issuecomment-49535",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_049536.json:
```json
{
    "body": "we have switched to git, this is obsolete",
    "created_at": "2014-03-14T16:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6212#issuecomment-49536",
    "user": "https://github.com/fchapoton"
}
```

we have switched to git, this is obsolete



---

archive/issue_events_014570.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2014-03-14T16:44:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6212",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6212#event-14570"
}
```



---

archive/issue_events_014571.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2014-03-14T16:44:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6212",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6212#event-14571"
}
```



---

archive/issue_comments_049537.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-15T13:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6212#issuecomment-49537",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_014572.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-03-19T04:35:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6212",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6212#event-14572"
}
```



---

archive/issue_comments_049538.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-03-19T04:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6212#issuecomment-49538",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix
