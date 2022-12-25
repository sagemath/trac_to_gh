# Issue 9847: 'sage -advanced' does not mention the '-R' flag, which starts the R interpreter

archive/issues_009847.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\nTo run the copy of R bundled with Sage, we can use `sage -R`, but this option is not documented in the help message returned by `sage -advanced`.\n\nThe relevant file is `SAGE_ROOT/local/bin/sage-sage`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9848\n\n",
    "created_at": "2010-09-01T09:51:49Z",
    "labels": [
        "component: user interface",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "'sage -advanced' does not mention the '-R' flag, which starts the R interpreter",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9847",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @kcrisman

To run the copy of R bundled with Sage, we can use `sage -R`, but this option is not documented in the help message returned by `sage -advanced`.

The relevant file is `SAGE_ROOT/local/bin/sage-sage`.

Issue created by migration from https://trac.sagemath.org/ticket/9848





---

archive/issue_comments_097036.json:
```json
{
    "body": "Are there any other programs we can run in this way which are not on that list?  Gap, Pari, Maxima are all there...",
    "created_at": "2010-09-01T12:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9847#issuecomment-97036",
    "user": "https://github.com/kcrisman"
}
```

Are there any other programs we can run in this way which are not on that list?  Gap, Pari, Maxima are all there...



---

archive/issue_comments_097037.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-19T13:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9847#issuecomment-97037",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097038.json:
```json
{
    "body": "Huh, this was fixed at some point in the recent past.   At any rate, it is in the released 4.7.1.\n\n```\n  -maxima [...]       -- run Sage's Maxima with given arguments\n  -mwrank [...]       -- run Sage's mwrank with given arguments\n  -python [...]       -- run the Python interpreter\n  -R [...]            -- run Sage's R with given arguments\n  -scons [...]        -- run Sage's scons\n```\n\nIn fact, it even shows up in `./sage -help`.",
    "created_at": "2011-08-19T13:31:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9847#issuecomment-97038",
    "user": "https://github.com/kcrisman"
}
```

Huh, this was fixed at some point in the recent past.   At any rate, it is in the released 4.7.1.

```
  -maxima [...]       -- run Sage's Maxima with given arguments
  -mwrank [...]       -- run Sage's mwrank with given arguments
  -python [...]       -- run the Python interpreter
  -R [...]            -- run Sage's R with given arguments
  -scons [...]        -- run Sage's scons
```

In fact, it even shows up in `./sage -help`.



---

archive/issue_comments_097039.json:
```json
{
    "body": "This, along with a lot of other stuff, was added in #10326.",
    "created_at": "2011-08-19T13:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9847#issuecomment-97039",
    "user": "https://github.com/kcrisman"
}
```

This, along with a lot of other stuff, was added in #10326.



---

archive/issue_comments_097040.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-19T13:34:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9847#issuecomment-97040",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097041.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-08-22T08:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9847#issuecomment-97041",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
