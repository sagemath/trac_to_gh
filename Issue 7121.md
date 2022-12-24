# Issue 7121: Make it possible to build Sage but not documentation

archive/issues_007121.json:
```json
{
    "body": "Assignee: tbd\n\nOn slow machines (or even fast ones), building all the documentation for a build which will not be used for general purposes takes a looooong time.  There should be a switch for make and/or sage -upgrade which disables this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7121\n\n",
    "created_at": "2009-10-05T13:27:08Z",
    "labels": [
        "build",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Make it possible to build Sage but not documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7121",
    "user": "kcrisman"
}
```
Assignee: tbd

On slow machines (or even fast ones), building all the documentation for a build which will not be used for general purposes takes a looooong time.  There should be a switch for make and/or sage -upgrade which disables this.

Issue created by migration from https://trac.sagemath.org/ticket/7121





---

archive/issue_comments_059028.json:
```json
{
    "body": "Another option might be an environment variable 'NO_DOCUMENTATION' or similar. I was about to update sage-env to handle a lot more environment variables. This could be added. The biggest problem is chaning every single packaging that builds the documentation. Adding a switch or compiler variable is the easy part!\n\nDave",
    "created_at": "2009-10-05T14:29:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7121#issuecomment-59028",
    "user": "drkirkby"
}
```

Another option might be an environment variable 'NO_DOCUMENTATION' or similar. I was about to update sage-env to handle a lot more environment variables. This could be added. The biggest problem is chaning every single packaging that builds the documentation. Adding a switch or compiler variable is the easy part!

Dave



---

archive/issue_comments_059029.json:
```json
{
    "body": "I have a feeling that I was being silly about this.  One can do `make build`, I think.\n\nHowever, the targets in the Makefile are not particularly well documented in the installation guide.  So I'm changing this ticket's",
    "created_at": "2012-07-07T02:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7121#issuecomment-59029",
    "user": "kcrisman"
}
```

I have a feeling that I was being silly about this.  One can do `make build`, I think.

However, the targets in the Makefile are not particularly well documented in the installation guide.  So I'm changing this ticket's



---

archive/issue_comments_059030.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2012-07-07T02:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7121#issuecomment-59030",
    "user": "kcrisman"
}
```

Changing priority from minor to major.



---

archive/issue_comments_059031.json:
```json
{
    "body": "Changing component from build to documentation.",
    "created_at": "2012-07-07T02:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7121#issuecomment-59031",
    "user": "kcrisman"
}
```

Changing component from build to documentation.



---

archive/issue_comments_059032.json:
```json
{
    "body": "Okay, the [installation guide](http://www.sagemath.org/doc/installation/source.html?#section-make) is a lot better now.  Updating description for some things I see us being able to do now.",
    "created_at": "2014-11-20T16:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7121#issuecomment-59032",
    "user": "kcrisman"
}
```

Okay, the [installation guide](http://www.sagemath.org/doc/installation/source.html?#section-make) is a lot better now.  Updating description for some things I see us being able to do now.



---

archive/issue_comments_059033.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2014-11-20T16:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7121",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7121#issuecomment-59033",
    "user": "kcrisman"
}
```

Changing priority from major to minor.
