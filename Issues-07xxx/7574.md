# Issue 7574: clean up of MIP interface

archive/issues_007574.json:
```json
{
    "body": "Assignee: jkantor\n\nKeywords: lp\n\nThere are a few issues with the MIP code:\n* ``max`` and ``min`` are built-in core functions in Python and shouldn't be used as variable names\n* ``id`` shouldn't be used as a variable name\n* I don't think we should have ``try: foo except: bar`` blocks without a specific ``except ThisandThatError``.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7574\n\n",
    "closed_at": "2016-08-30T13:32:25Z",
    "created_at": "2009-12-01T17:33:00Z",
    "labels": [
        "component: numerical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "clean up of MIP interface",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7574",
    "user": "https://github.com/malb"
}
```
Assignee: jkantor

Keywords: lp

There are a few issues with the MIP code:
* ``max`` and ``min`` are built-in core functions in Python and shouldn't be used as variable names
* ``id`` shouldn't be used as a variable name
* I don't think we should have ``try: foo except: bar`` blocks without a specific ``except ThisandThatError``.

Issue created by migration from https://trac.sagemath.org/ticket/7574





---

archive/issue_events_017958.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7574#event-17958"
}
```



---

archive/issue_events_017959.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7574#event-17959"
}
```



---

archive/issue_events_017960.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7574#event-17960"
}
```



---

archive/issue_events_017961.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7574#event-17961"
}
```



---

archive/issue_events_017962.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7574#event-17962"
}
```



---

archive/issue_events_017963.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7574#event-17963"
}
```



---

archive/issue_events_017964.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7574#event-17964"
}
```



---

archive/issue_comments_064355.json:
```json
{
    "body": "Changing keywords from \"\" to \"lp\".",
    "created_at": "2016-06-25T06:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64355",
    "user": "https://github.com/mkoeppe"
}
```

Changing keywords from "" to "lp".



---

archive/issue_comments_064356.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-06-25T06:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64356",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064357.json:
```json
{
    "body": "This is outdated. The first issue is duplicated in #20664. Can be closed.",
    "created_at": "2016-06-25T06:10:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64357",
    "user": "https://github.com/mkoeppe"
}
```

This is outdated. The first issue is duplicated in #20664. Can be closed.



---

archive/issue_events_017965.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2016-06-25T06:10:34Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7574#event-17965"
}
```



---

archive/issue_events_017966.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2016-06-25T06:10:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7574#event-17966"
}
```



---

archive/issue_comments_064358.json:
```json
{
    "body": "ok",
    "created_at": "2016-07-13T18:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64358",
    "user": "https://github.com/fchapoton"
}
```

ok



---

archive/issue_comments_064359.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-07-13T18:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64359",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_017967.json:
```json
{
    "actor": "https://github.com/embray",
    "created_at": "2016-08-30T13:32:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7574#event-17967"
}
```



---

archive/issue_comments_064360.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64360",
    "user": "https://github.com/embray"
}
```

Resolution: wontfix



---

archive/issue_comments_064361.json:
```json
{
    "body": "Determined to be invalid/duplicate/wontfix (closing as \"wontfix\" as a catch-all resolution).",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7574#issuecomment-64361",
    "user": "https://github.com/embray"
}
```

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).
