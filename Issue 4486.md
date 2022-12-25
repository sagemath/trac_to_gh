# Issue 4486: Clean up partitions_c.cc and partitions_c.h

archive/issues_004486.json:
```json
{
    "body": "Assignee: @tornaria\n\nThese files need audited. In particular, `partitions_c.cc` should depend on `partitions_c.h`, and shouldn't duplicate the code there. Someone familiar with C should go ahead and clean these files up.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4486\n\n",
    "created_at": "2008-11-09T23:22:58Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Clean up partitions_c.cc and partitions_c.h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4486",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @tornaria

These files need audited. In particular, `partitions_c.cc` should depend on `partitions_c.h`, and shouldn't duplicate the code there. Someone familiar with C should go ahead and clean these files up.

Issue created by migration from https://trac.sagemath.org/ticket/4486





---

archive/issue_comments_033066.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-23T02:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4486#issuecomment-33066",
    "user": "https://github.com/aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_events_010149.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4486",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4486#event-10149"
}
```



---

archive/issue_events_010150.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4486",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4486#event-10150"
}
```



---

archive/issue_events_010151.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4486",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4486#event-10151"
}
```



---

archive/issue_events_010152.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4486",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4486#event-10152"
}
```



---

archive/issue_events_010153.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4486",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4486#event-10153"
}
```



---

archive/issue_events_010154.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4486",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4486#event-10154"
}
```



---

archive/issue_events_010155.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4486",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4486#event-10155"
}
```



---

archive/issue_comments_033067.json:
```json
{
    "body": "Perhaps they could just be replaced by the implementation in arb once arb becomes a standard part of Sage.",
    "created_at": "2015-04-14T07:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4486",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4486#issuecomment-33067",
    "user": "https://github.com/mezzarobba"
}
```

Perhaps they could just be replaced by the implementation in arb once arb becomes a standard part of Sage.
