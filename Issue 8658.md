# Issue 8658: opencdk spkg has incorrect DSO linking

archive/issues_008658.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nKeywords: DSO\n\nopencdk fails to explicitly link against libgcrypt. This is exposed by the changed ld behavior in Fedora 13 (beta), see https://fedoraproject.org/wiki/UnderstandingDSOLinkChange\n\nThe new version fixes this and is necessary to compile on F13. You can get it at\n\nhttp://www.stp.dias.ie/~vbraun/Sage/spkg/opencdk-0.6.6.p4.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/8658\n\n",
    "created_at": "2010-04-07T22:24:48Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "opencdk spkg has incorrect DSO linking",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8658",
    "user": "vbraun"
}
```
Assignee: AlexGhitza

Keywords: DSO

opencdk fails to explicitly link against libgcrypt. This is exposed by the changed ld behavior in Fedora 13 (beta), see https://fedoraproject.org/wiki/UnderstandingDSOLinkChange

The new version fixes this and is necessary to compile on F13. You can get it at

http://www.stp.dias.ie/~vbraun/Sage/spkg/opencdk-0.6.6.p4.spkg

Issue created by migration from https://trac.sagemath.org/ticket/8658





---

archive/issue_comments_078558.json:
```json
{
    "body": "I'd like to get this in 4.4.4.  There are a couple of issues. `/bin/sh` on boxen doesn't like ` Makefile.{am,in} `.  Also, sed on Solaris doesn't support `-i`.  While the Makefiles don't need to be used on Solaris, it be nice to not have those fail.  Also, we should check the exit status to make sure the command successfully ran.",
    "created_at": "2010-06-09T18:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8658#issuecomment-78558",
    "user": "mhansen"
}
```

I'd like to get this in 4.4.4.  There are a couple of issues. `/bin/sh` on boxen doesn't like ` Makefile.{am,in} `.  Also, sed on Solaris doesn't support `-i`.  While the Makefiles don't need to be used on Solaris, it be nice to not have those fail.  Also, we should check the exit status to make sure the command successfully ran.



---

archive/issue_comments_078559.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-09T18:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8658#issuecomment-78559",
    "user": "mhansen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_078560.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-09T19:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8658#issuecomment-78560",
    "user": "vbraun"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078561.json:
```json
{
    "body": "Ok updated version now copies a suitable Makefile.in file from patches/ instead of the sed hack:\n\nhttp://www.stp.dias.ie/~vbraun/Sage/spkg/opencdk-0.6.6.p4.spkg\n\nThe Makefile.am is not needed, so I did not change it. Hopefully upstream will make a new release before we have to edit this again. The Fedora people are trying to push these changes upstream.",
    "created_at": "2010-06-09T19:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8658#issuecomment-78561",
    "user": "vbraun"
}
```

Ok updated version now copies a suitable Makefile.in file from patches/ instead of the sed hack:

http://www.stp.dias.ie/~vbraun/Sage/spkg/opencdk-0.6.6.p4.spkg

The Makefile.am is not needed, so I did not change it. Hopefully upstream will make a new release before we have to edit this again. The Fedora people are trying to push these changes upstream.



---

archive/issue_comments_078562.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-11T18:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8658#issuecomment-78562",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078563.json:
```json
{
    "body": "I've merged http://sage.math.washington.edu/home/mhansen/opencdk-0.6.6.p4.spkg",
    "created_at": "2010-06-11T18:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8658#issuecomment-78563",
    "user": "mhansen"
}
```

I've merged http://sage.math.washington.edu/home/mhansen/opencdk-0.6.6.p4.spkg



---

archive/issue_comments_078564.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-11T18:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8658",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8658#issuecomment-78564",
    "user": "mhansen"
}
```

Resolution: fixed
