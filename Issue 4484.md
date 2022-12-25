# Issue 4484: make a platform_quirks.h

archive/issues_004484.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere are lots of platform-specific quirks in various parts of the Sage library. For instance, see the `#if defined(__sun)` at the top of `partitions_c.cc` (`partitions_c.h`). These should be moved to a single header in `libcsage`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4484\n\n",
    "created_at": "2008-11-09T23:05:29Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make a platform_quirks.h",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4484",
    "user": "https://github.com/craigcitro"
}
```
Assignee: mabshoff

There are lots of platform-specific quirks in various parts of the Sage library. For instance, see the `#if defined(__sun)` at the top of `partitions_c.cc` (`partitions_c.h`). These should be moved to a single header in `libcsage`.

Issue created by migration from https://trac.sagemath.org/ticket/4484





---

archive/issue_comments_033055.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-10T08:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4484#issuecomment-33055",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033056.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-05-19T13:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4484#issuecomment-33056",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_010145.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-19T13:09:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4484",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4484#event-10145"
}
```



---

archive/issue_comments_033057.json:
```json
{
    "body": "We managed to live without this, so I guess it's not really needed.",
    "created_at": "2013-05-19T13:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4484#issuecomment-33057",
    "user": "https://github.com/jdemeyer"
}
```

We managed to live without this, so I guess it's not really needed.



---

archive/issue_comments_033058.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-05-19T13:10:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4484#issuecomment-33058",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_033059.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2013-05-21T07:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4484",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4484#issuecomment-33059",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: wontfix



---

archive/issue_events_010146.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-21T07:23:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4484",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4484#event-10146"
}
```
