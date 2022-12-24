# Issue 4331: sage-vmware image - add keyboard reconfigure option

archive/issues_004331.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @slel\n\nChange the sage vmware image so there is another login option:\n\n\n```\nlogin: keyboard\n```\n\n\nThis would run `dpkg-reconfigure console-setup`\nas suggested by Martin Rubey in email:\n\n```\n>\n> Sorry, I meant, of all the things you tried was\n> just typing\n>\n>    dpkg-reconfigure console-setup\n>\n> the one and only thing you did, and that it worked?\n\nNearly: you will then be asked some simple questions which are obvious to\nanswer if you do not have an english keyboard.\n\n-- Martin Rubey\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4331\n\n",
    "created_at": "2008-10-20T16:26:21Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "sage-vmware image - add keyboard reconfigure option",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4331",
    "user": "@williamstein"
}
```
Assignee: mabshoff

CC:  @slel

Change the sage vmware image so there is another login option:


```
login: keyboard
```


This would run `dpkg-reconfigure console-setup`
as suggested by Martin Rubey in email:

```
>
> Sorry, I meant, of all the things you tried was
> just typing
>
>    dpkg-reconfigure console-setup
>
> the one and only thing you did, and that it worked?

Nearly: you will then be asked some simple questions which are obvious to
answer if you do not have an english keyboard.

-- Martin Rubey
```


Issue created by migration from https://trac.sagemath.org/ticket/4331





---

archive/issue_comments_031762.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2021-08-26T02:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4331#issuecomment-31762",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_031763.json:
```json
{
    "body": "outdated, should close",
    "created_at": "2021-08-26T02:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4331#issuecomment-31763",
    "user": "@mkoeppe"
}
```

outdated, should close



---

archive/issue_comments_031764.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2021-08-26T22:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4331#issuecomment-31764",
    "user": "@slel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_031765.json:
```json
{
    "body": "There seems to be no plan to resume producing\nthe vmware image at each Sage release.\n\nIts main use was arguably to work around\nthe lack of a version of Sage for Windows.\n\nThat use case largely fell with Erik Bray's\nCygwin-based Sage installer for 64-bit Windows.\n\nThe Sage Debian Live distribution also\nprovides a versatile portable solution.\n\nIn view of that, ok to close this.",
    "created_at": "2021-08-26T22:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4331#issuecomment-31765",
    "user": "@slel"
}
```

There seems to be no plan to resume producing
the vmware image at each Sage release.

Its main use was arguably to work around
the lack of a version of Sage for Windows.

That use case largely fell with Erik Bray's
Cygwin-based Sage installer for 64-bit Windows.

The Sage Debian Live distribution also
provides a versatile portable solution.

In view of that, ok to close this.



---

archive/issue_comments_031766.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2021-09-01T07:08:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4331",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4331#issuecomment-31766",
    "user": "@fchapoton"
}
```

Resolution: invalid
