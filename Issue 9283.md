# Issue 9283: sage notebook error when opening default page

archive/issues_009283.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @fchapoton\n\nWhen I start sage notebook and it start the default page with link:\u00a0http://localhost:8000/?startup_token=bc78dfa581c408ffb65ce4d556960690, i get error:\n\n2010-06-20 !16:02:21+0300 [HTTPChannel,1,127.0.0.1] /opt/sagemath/local/lib/python2.6/site-packages/twisted/internet/!defer.py:262: exceptions.DeprecationWarning: Don't pass strings (like 'Bad token') to failure.Failure (replacing with a DefaultException).\n\n\n\n2010-06-20 !16:00:21+0300 [HTTPChannel,1,127.0.0.1] Exception rendering:\n\n2010-06-20 !16:00:21+0300 [HTTPChannel,1,127.0.0.1] Unhandled Error\u00a0\u00a0 \u00a0 \u00a0 \u00a0Traceback (most recent call last):\u00a0\u00a0 \u00a0 \u00a0 \u00a0Failure: twisted.python.failure.DefaultException: Bad tokenMy browser opens up with with text:\n\n# Internal Server Error\nAn error occurred rendering the requested  page. More information is available in the server log.\n\nIf i delete the startup token part, everything works correctly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9283\n\n",
    "created_at": "2010-06-20T13:06:39Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage notebook error when opening default page",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9283",
    "user": "https://trac.sagemath.org/admin/accounts/users/retry"
}
```
Assignee: jason, was

CC:  @fchapoton

When I start sage notebook and it start the default page with link: http://localhost:8000/?startup_token=bc78dfa581c408ffb65ce4d556960690, i get error:

2010-06-20 !16:02:21+0300 [HTTPChannel,1,127.0.0.1] /opt/sagemath/local/lib/python2.6/site-packages/twisted/internet/!defer.py:262: exceptions.DeprecationWarning: Don't pass strings (like 'Bad token') to failure.Failure (replacing with a DefaultException).



2010-06-20 !16:00:21+0300 [HTTPChannel,1,127.0.0.1] Exception rendering:

2010-06-20 !16:00:21+0300 [HTTPChannel,1,127.0.0.1] Unhandled Error        Traceback (most recent call last):        Failure: twisted.python.failure.DefaultException: Bad tokenMy browser opens up with with text:

# Internal Server Error
An error occurred rendering the requested  page. More information is available in the server log.

If i delete the startup token part, everything works correctly.

Issue created by migration from https://trac.sagemath.org/ticket/9283





---

archive/issue_comments_087305.json:
```json
{
    "body": "Attachment [notebook.log](tarball://root/attachments/some-uuid/ticket9283/notebook.log) by retry created at 2010-06-20 13:06:55\n\nfull notebook log.",
    "created_at": "2010-06-20T13:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9283#issuecomment-87305",
    "user": "https://trac.sagemath.org/admin/accounts/users/retry"
}
```

Attachment [notebook.log](tarball://root/attachments/some-uuid/ticket9283/notebook.log) by retry created at 2010-06-20 13:06:55

full notebook log.



---

archive/issue_events_022867.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/retry",
    "created_at": "2010-06-26T12:08:00Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22867"
}
```



---

archive/issue_events_022868.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22868"
}
```



---

archive/issue_events_022869.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22869"
}
```



---

archive/issue_events_022870.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22870"
}
```



---

archive/issue_events_022871.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22871"
}
```



---

archive/issue_events_022872.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22872"
}
```



---

archive/issue_events_022873.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22873"
}
```



---

archive/issue_events_022874.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22874"
}
```



---

archive/issue_events_022875.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22875"
}
```



---

archive/issue_comments_087306.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9283#issuecomment-87306",
    "user": "https://github.com/mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_087307.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9283#issuecomment-87307",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_events_022876.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-08-18T00:36:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22876"
}
```



---

archive/issue_events_022877.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-08-18T00:36:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22877"
}
```



---

archive/issue_comments_087308.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-08-22T08:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9283#issuecomment-87308",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087309.json:
```json
{
    "body": "yep.",
    "created_at": "2020-08-22T08:18:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9283#issuecomment-87309",
    "user": "https://github.com/dimpase"
}
```

yep.



---

archive/issue_comments_087310.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-22T08:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9283#issuecomment-87310",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_022878.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-08-22T08:43:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9283",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9283#event-22878"
}
```
