# Issue 1792: Make Install problem with DESTDIR/sage script

archive/issues_001792.json:
```json
{
    "body": "Assignee: cwitty\n\nwhen running \"make install\" a script will be created in $DESTDIR called sage. This is intended to be the main executable for sage. However, SAGE_ROOT is not set correctly in this file. It would be nice if the make install process correctly set SAGE_ROOT=$DESTDIR during its installation.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1792\n\n",
    "created_at": "2008-01-16T04:56:34Z",
    "labels": [
        "component: relocation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.3",
    "title": "Make Install problem with DESTDIR/sage script",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1792",
    "user": "https://trac.sagemath.org/admin/accounts/users/pgrinber"
}
```
Assignee: cwitty

when running "make install" a script will be created in $DESTDIR called sage. This is intended to be the main executable for sage. However, SAGE_ROOT is not set correctly in this file. It would be nice if the make install process correctly set SAGE_ROOT=$DESTDIR during its installation.

Issue created by migration from https://trac.sagemath.org/ticket/1792





---

archive/issue_comments_011309.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2008-03-16T08:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11309",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_011310.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-16T08:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11310",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011311.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-05-20T08:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11311",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_011312.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-05-20T08:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11312",
    "user": "https://github.com/jdemeyer"
}
```

New commits:



---

archive/issue_comments_011313.json:
```json
{
    "body": "why remove this feature, which I'm using when compiling Sage from source since several years, and which is very useful for me (at least)?\n\nPaul",
    "created_at": "2016-05-20T08:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11313",
    "user": "https://github.com/zimmermann6"
}
```

why remove this feature, which I'm using when compiling Sage from source since several years, and which is very useful for me (at least)?

Paul



---

archive/issue_comments_011314.json:
```json
{
    "body": "Given that it doesn't work, you cannot really argue that I'm removing a feature.\n\nI'm just pointing out that it's not supported and that it's unlikely to become supported.",
    "created_at": "2016-05-20T08:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11314",
    "user": "https://github.com/jdemeyer"
}
```

Given that it doesn't work, you cannot really argue that I'm removing a feature.

I'm just pointing out that it's not supported and that it's unlikely to become supported.



---

archive/issue_comments_011315.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-05-23T22:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11315",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_011316.json:
```json
{
    "body": "This is definitely broken now",
    "created_at": "2016-05-23T22:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11316",
    "user": "https://github.com/vbraun"
}
```

This is definitely broken now



---

archive/issue_comments_011317.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-05-24T16:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1792#issuecomment-11317",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_001951.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-05-24T16:41:17Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1792",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1792#event-1951"
}
```
