# Issue 8298: GLPK 4.42 + error message

archive/issues_008298.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @haraldschilly mvngu\n\nThe user has to run sage -b after installing GLPK or CBC because of recent modifications in the mip.pyx file.... As he may not be aware of it, Harald Schilly suggested a *** LARGE *** message, which will be printed after the package is installed.\n\nOn the way, I also updated the sources of glpk, as the most recent is the 4.42 while we were using 4.38\n\nIt can be downloaded on sage.math at :\n\n~/ncohen/glpk-4.42.p0.spkg\n\n* The package 4.38 will have to be removed when this one is made available *\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/8298\n\n",
    "created_at": "2010-02-18T14:03:46Z",
    "labels": [
        "component: packages: optional"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "GLPK 4.42 + error message",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8298",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: tbd

CC:  @haraldschilly mvngu

The user has to run sage -b after installing GLPK or CBC because of recent modifications in the mip.pyx file.... As he may not be aware of it, Harald Schilly suggested a *** LARGE *** message, which will be printed after the package is installed.

On the way, I also updated the sources of glpk, as the most recent is the 4.42 while we were using 4.38

It can be downloaded on sage.math at :

~/ncohen/glpk-4.42.p0.spkg

* The package 4.38 will have to be removed when this one is made available *

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/8298





---

archive/issue_comments_073388.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-27T13:30:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8298#issuecomment-73388",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073389.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-09T08:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8298#issuecomment-73389",
    "user": "https://github.com/dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073390.json:
```json
{
    "body": "Replying to [comment:1 ncohen]:\n\nOK, works (Linux x86_64 Debian, and Sparc Solaris 2.10), doctests pass, positive review.",
    "created_at": "2010-04-09T08:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8298#issuecomment-73390",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:1 ncohen]:

OK, works (Linux x86_64 Debian, and Sparc Solaris 2.10), doctests pass, positive review.



---

archive/issue_comments_073391.json:
```json
{
    "body": "Merged 2010/04/20.",
    "created_at": "2010-04-20T22:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8298#issuecomment-73391",
    "user": "https://github.com/jhpalmieri"
}
```

Merged 2010/04/20.



---

archive/issue_events_008495.json:
```json
{
    "actor": "@jhpalmieri",
    "created_at": "2010-04-20T22:55:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8298",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8298#event-8495"
}
```



---

archive/issue_comments_073392.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-20T22:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8298#issuecomment-73392",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
