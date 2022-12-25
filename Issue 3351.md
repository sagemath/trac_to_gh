# Issue 3351: update SAGE_ROOT/COPYING.txt to clarify situation wrt Maxima license

archive/issues_003351.json:
```json
{
    "body": "Assignee: mabshoff\n\nSee \n\n   http://www.math.utexas.edu/pipermail/maxima/2008/011882.html\n\nwhere we learn that Maxima is GPLv2 only, not GPLv2+.  This means that\nwe can not binary link Maxima and Sage. \n\nSomething from the email at the above link should be mentioned in the\nCOPYING.txt file, and the statement at the top of COPYING.txt that\n\n\"Every component of SAGE except jsmath is licensed under a GPL v2 (or\nlater) compatible license.\" may need to be changed to\n\n\"Every component of SAGE except jsmath is licensed under a GPL v2 compatible\nor GPLv2+  compatible license.  All components that are binary linked\nto Sage are GPLv2+.\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/3351\n\n",
    "created_at": "2008-06-02T13:43:34Z",
    "labels": [
        "component: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "update SAGE_ROOT/COPYING.txt to clarify situation wrt Maxima license",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3351",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

See 

   http://www.math.utexas.edu/pipermail/maxima/2008/011882.html

where we learn that Maxima is GPLv2 only, not GPLv2+.  This means that
we can not binary link Maxima and Sage. 

Something from the email at the above link should be mentioned in the
COPYING.txt file, and the statement at the top of COPYING.txt that

"Every component of SAGE except jsmath is licensed under a GPL v2 (or
later) compatible license." may need to be changed to

"Every component of SAGE except jsmath is licensed under a GPL v2 compatible
or GPLv2+  compatible license.  All components that are binary linked
to Sage are GPLv2+."

Issue created by migration from https://trac.sagemath.org/ticket/3351





---

archive/issue_comments_023245.json:
```json
{
    "body": "Changing component from Cygwin to packages.",
    "created_at": "2008-06-02T13:43:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3351#issuecomment-23245",
    "user": "https://github.com/williamstein"
}
```

Changing component from Cygwin to packages.



---

archive/issue_comments_023246.json:
```json
{
    "body": "The statement \"All components that are binary linked to Sage are GPLv2+.\" is incorrect since we are linking against a [L]GPL V3+ GSL, GMP and GNUTSL library.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-02T15:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3351#issuecomment-23246",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The statement "All components that are binary linked to Sage are GPLv2+." is incorrect since we are linking against a [L]GPL V3+ GSL, GMP and GNUTSL library.

Cheers,

Michael



---

archive/issue_comments_023247.json:
```json
{
    "body": "This has been fixed in #12447.",
    "created_at": "2014-08-12T21:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3351#issuecomment-23247",
    "user": "https://github.com/a-andre"
}
```

This has been fixed in #12447.



---

archive/issue_comments_023248.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-12T21:04:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3351#issuecomment-23248",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023249.json:
```json
{
    "body": "Yes, you are right!",
    "created_at": "2014-08-14T13:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3351#issuecomment-23249",
    "user": "https://github.com/kcrisman"
}
```

Yes, you are right!



---

archive/issue_comments_023250.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-08-14T13:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3351#issuecomment-23250",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_003569.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-08-20T20:32:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3351",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3351#event-3569"
}
```



---

archive/issue_comments_023251.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-08-20T20:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3351",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3351#issuecomment-23251",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate
