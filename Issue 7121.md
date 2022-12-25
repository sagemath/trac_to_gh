# Issue 7121: Make it possible to build Sage but not documentation

archive/issues_007121.json:
```json
{
    "body": "Assignee: tbd\n\nOn slow machines (or even fast ones), building all the documentation for a build which will not be used for general purposes takes a looooong time.  There should be a switch for make and/or sage -upgrade which disables this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7121\n\n",
    "created_at": "2009-10-05T13:27:08Z",
    "labels": [
        "component: build",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Make it possible to build Sage but not documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7121",
    "user": "https://github.com/kcrisman"
}
```
Assignee: tbd

On slow machines (or even fast ones), building all the documentation for a build which will not be used for general purposes takes a looooong time.  There should be a switch for make and/or sage -upgrade which disables this.

Issue created by migration from https://trac.sagemath.org/ticket/7121





---

archive/issue_comments_058917.json:
```json
{
    "body": "Another option might be an environment variable 'NO_DOCUMENTATION' or similar. I was about to update sage-env to handle a lot more environment variables. This could be added. The biggest problem is chaning every single packaging that builds the documentation. Adding a switch or compiler variable is the easy part!\n\nDave",
    "created_at": "2009-10-05T14:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7121#issuecomment-58917",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Another option might be an environment variable 'NO_DOCUMENTATION' or similar. I was about to update sage-env to handle a lot more environment variables. This could be added. The biggest problem is chaning every single packaging that builds the documentation. Adding a switch or compiler variable is the easy part!

Dave



---

archive/issue_comments_058918.json:
```json
{
    "body": "I have a feeling that I was being silly about this.  One can do `make build`, I think.\n\nHowever, the targets in the Makefile are not particularly well documented in the installation guide.  So I'm changing this ticket's",
    "created_at": "2012-07-07T02:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7121#issuecomment-58918",
    "user": "https://github.com/kcrisman"
}
```

I have a feeling that I was being silly about this.  One can do `make build`, I think.

However, the targets in the Makefile are not particularly well documented in the installation guide.  So I'm changing this ticket's



---

archive/issue_comments_058919.json:
```json
{
    "body": "Changing component from build to documentation.",
    "created_at": "2012-07-07T02:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7121#issuecomment-58919",
    "user": "https://github.com/kcrisman"
}
```

Changing component from build to documentation.



---

archive/issue_events_016827.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7121#event-16827"
}
```



---

archive/issue_events_016828.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7121#event-16828"
}
```



---

archive/issue_events_016829.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7121#event-16829"
}
```



---

archive/issue_events_016830.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7121#event-16830"
}
```



---

archive/issue_events_016831.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7121#event-16831"
}
```



---

archive/issue_events_016832.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7121#event-16832"
}
```



---

archive/issue_events_016833.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7121#event-16833"
}
```



---

archive/issue_comments_058920.json:
```json
{
    "body": "Okay, the [installation guide](http://www.sagemath.org/doc/installation/source.html?#section-make) is a lot better now.  Updating description for some things I see us being able to do now.",
    "created_at": "2014-11-20T16:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7121#issuecomment-58920",
    "user": "https://github.com/kcrisman"
}
```

Okay, the [installation guide](http://www.sagemath.org/doc/installation/source.html?#section-make) is a lot better now.  Updating description for some things I see us being able to do now.



---

archive/issue_comments_058921.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2014-11-20T16:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7121#issuecomment-58921",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.
