# Issue 7686: Remove all "AppleDouble encoded Macintosh files" from the Sage source distribution

archive/issues_007686.json:
```json
{
    "body": "Assignee: tbd\n\nThe spkg's with ._ file crap all over the place are:\n\n* f2c-20070816.p1\n* flintqs-20070817.p4\n* ghmm-20080813.p0\n* lcalc-20080205.p3\n\nThis can be fixed by extracting the spkg, deleting the crap, and remaking it with \"sage -pkg\".  I think \"sage -pkg\" works correctly on OS X now-a-days, but certainly does on Linux.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7686\n\n",
    "created_at": "2009-12-15T19:14:07Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Remove all \"AppleDouble encoded Macintosh files\" from the Sage source distribution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7686",
    "user": "was"
}
```
Assignee: tbd

The spkg's with ._ file crap all over the place are:

* f2c-20070816.p1
* flintqs-20070817.p4
* ghmm-20080813.p0
* lcalc-20080205.p3

This can be fixed by extracting the spkg, deleting the crap, and remaking it with "sage -pkg".  I think "sage -pkg" works correctly on OS X now-a-days, but certainly does on Linux.

Issue created by migration from https://trac.sagemath.org/ticket/7686





---

archive/issue_comments_065960.json:
```json
{
    "body": "Obsolete, we no longer use SPKG files.",
    "created_at": "2016-04-11T09:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7686#issuecomment-65960",
    "user": "jdemeyer"
}
```

Obsolete, we no longer use SPKG files.



---

archive/issue_comments_065961.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-04-11T09:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7686#issuecomment-65961",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065962.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-04-11T09:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7686#issuecomment-65962",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065963.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7686#issuecomment-65963",
    "user": "vbraun"
}
```

Resolution: fixed
