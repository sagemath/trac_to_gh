# Issue 7686: Remove "AppleDouble encoded Macintosh files" from SPKGs

archive/issues_007686.json:
```json
{
    "body": "Assignee: tbd\n\nThe spkg's with ._ file crap all over the place are:\n\n* `flintqs-20070817.p8` (standard)\n* `gap_packages-4.4.12.p1` (optional)\n* `boost_1_34_1` (experimental)\n* `quantlib-0.9.6` (experimental)\n* `quantlib_swig-0.9.6` (experimental)\n\nThis can be fixed by extracting the spkg, deleting the crap, and remaking it with \"sage -pkg\".  I think \"sage -pkg\" works correctly on OS X now-a-days, but certainly does on Linux.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7686\n\n",
    "closed_at": "2016-06-12T12:02:30Z",
    "created_at": "2009-12-15T19:14:07Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Remove \"AppleDouble encoded Macintosh files\" from SPKGs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7686",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

The spkg's with ._ file crap all over the place are:

* `flintqs-20070817.p8` (standard)
* `gap_packages-4.4.12.p1` (optional)
* `boost_1_34_1` (experimental)
* `quantlib-0.9.6` (experimental)
* `quantlib_swig-0.9.6` (experimental)

This can be fixed by extracting the spkg, deleting the crap, and remaking it with "sage -pkg".  I think "sage -pkg" works correctly on OS X now-a-days, but certainly does on Linux.

Issue created by migration from https://trac.sagemath.org/ticket/7686





---

archive/issue_events_018347.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7686#event-18347"
}
```



---

archive/issue_events_018348.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7686#event-18348"
}
```



---

archive/issue_events_018349.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7686#event-18349"
}
```



---

archive/issue_events_018350.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7686#event-18350"
}
```



---

archive/issue_events_018351.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7686#event-18351"
}
```



---

archive/issue_events_018352.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7686#event-18352"
}
```



---

archive/issue_events_018353.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7686#event-18353"
}
```



---

archive/issue_events_018354.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2016-04-11T09:52:17Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7686#event-18354"
}
```



---

archive/issue_events_018355.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2016-04-11T09:52:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7686#event-18355"
}
```



---

archive/issue_comments_065844.json:
```json
{
    "body": "Obsolete, we no longer use SPKG files.",
    "created_at": "2016-04-11T09:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7686#issuecomment-65844",
    "user": "https://github.com/jdemeyer"
}
```

Obsolete, we no longer use SPKG files.



---

archive/issue_comments_065845.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-04-11T09:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7686#issuecomment-65845",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065846.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-04-11T09:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7686#issuecomment-65846",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_018356.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-06-12T12:02:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7686#event-18356"
}
```



---

archive/issue_comments_065847.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7686#issuecomment-65847",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
