# Issue 1792: Make Install problem with DESTDIR/sage script

archive/issues_001792.json:
```json
{
    "body": "Assignee: cwitty\n\nwhen running \"make install\" a script will be created in $DESTDIR called sage. This is intended to be the main executable for sage. However, SAGE_ROOT is not set correctly in this file. It would be nice if the make install process correctly set SAGE_ROOT=$DESTDIR during its installation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1792\n\n",
    "created_at": "2008-01-16T04:56:34Z",
    "labels": [
        "relocation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.3",
    "title": "Make Install problem with DESTDIR/sage script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1792",
    "user": "pgrinber"
}
```
Assignee: cwitty

when running "make install" a script will be created in $DESTDIR called sage. This is intended to be the main executable for sage. However, SAGE_ROOT is not set correctly in this file. It would be nice if the make install process correctly set SAGE_ROOT=$DESTDIR during its installation.

Issue created by migration from https://trac.sagemath.org/ticket/1792





---

archive/issue_comments_011337.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2008-03-16T08:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11337",
    "user": "mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_011338.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-16T08:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11338",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011339.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-05-20T08:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11339",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_011340.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-05-20T08:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11340",
    "user": "jdemeyer"
}
```

New commits:



---

archive/issue_comments_011341.json:
```json
{
    "body": "why remove this feature, which I'm using when compiling Sage from source since several years, and which is very useful for me (at least)?\n\nPaul",
    "created_at": "2016-05-20T08:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11341",
    "user": "zimmerma"
}
```

why remove this feature, which I'm using when compiling Sage from source since several years, and which is very useful for me (at least)?

Paul



---

archive/issue_comments_011342.json:
```json
{
    "body": "Given that it doesn't work, you cannot really argue that I'm removing a feature.\n\nI'm just pointing out that it's not supported and that it's unlikely to become supported.",
    "created_at": "2016-05-20T08:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11342",
    "user": "jdemeyer"
}
```

Given that it doesn't work, you cannot really argue that I'm removing a feature.

I'm just pointing out that it's not supported and that it's unlikely to become supported.



---

archive/issue_comments_011343.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-05-23T22:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11343",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_011344.json:
```json
{
    "body": "This is definitely broken now",
    "created_at": "2016-05-23T22:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11344",
    "user": "vbraun"
}
```

This is definitely broken now



---

archive/issue_comments_011345.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-05-24T16:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11345",
    "user": "vbraun"
}
```

Resolution: fixed
