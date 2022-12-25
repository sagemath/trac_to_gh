# Issue 4474: A hack in preparsing files is dangerous/confusing

archive/issues_004474.json:
```json
{
    "body": "Assignee: cwitty\n\nThere is a dangerous hack in preparser.py. Given input file:\n\n```\nload a.sage\nload b.py\n```\n   \nThen b.py will be loaded while the file is being *parsed*, and *before* a.sage is loaded.  That would be very confusing.  See the related #4473 and apply that patch before working on this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4474\n\n",
    "closed_at": "2014-05-06T15:15:25Z",
    "created_at": "2008-11-09T03:16:04Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "A hack in preparsing files is dangerous/confusing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4474",
    "user": "https://github.com/williamstein"
}
```
Assignee: cwitty

There is a dangerous hack in preparser.py. Given input file:

```
load a.sage
load b.py
```
   
Then b.py will be loaded while the file is being *parsed*, and *before* a.sage is loaded.  That would be very confusing.  See the related #4473 and apply that patch before working on this.

Issue created by migration from https://trac.sagemath.org/ticket/4474





---

archive/issue_events_010106.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4474#event-10106"
}
```



---

archive/issue_events_010107.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4474#event-10107"
}
```



---

archive/issue_events_010108.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4474#event-10108"
}
```



---

archive/issue_events_010109.json:
```json
{
    "actor": "https://github.com/a-andre",
    "created_at": "2014-05-01T08:36:20Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4474#event-10109"
}
```



---

archive/issue_events_010110.json:
```json
{
    "actor": "https://github.com/a-andre",
    "created_at": "2014-05-01T08:36:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4474#event-10110"
}
```



---

archive/issue_comments_032979.json:
```json
{
    "body": "The hack has been removed in #7514.",
    "created_at": "2014-05-01T08:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4474#issuecomment-32979",
    "user": "https://github.com/a-andre"
}
```

The hack has been removed in #7514.



---

archive/issue_comments_032980.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-05-01T08:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4474#issuecomment-32980",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_032981.json:
```json
{
    "body": "You must set it to positive_review in this case.",
    "created_at": "2014-05-05T11:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4474#issuecomment-32981",
    "user": "https://github.com/nathanncohen"
}
```

You must set it to positive_review in this case.



---

archive/issue_comments_032982.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-05-05T11:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4474#issuecomment-32982",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_032983.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-05-06T15:15:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4474#issuecomment-32983",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate



---

archive/issue_events_010111.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-05-06T15:15:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4474",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4474#event-10111"
}
```
