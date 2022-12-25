# Issue 3456: SQLize the notebook

archive/issues_003456.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @williamstein\n\nKeywords: notebook database sql\n\nThe public notebook is useless as is.  Life will be better with SQL.  This is probably a duplicate, but I couldn't find the original ticket.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3456\n\n",
    "created_at": "2008-06-18T01:25:47Z",
    "labels": [
        "component: notebook",
        "blocker"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "SQLize the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3456",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: boothby

CC:  @williamstein

Keywords: notebook database sql

The public notebook is useless as is.  Life will be better with SQL.  This is probably a duplicate, but I couldn't find the original ticket.

Issue created by migration from https://trac.sagemath.org/ticket/3456





---

archive/issue_comments_024315.json:
```json
{
    "body": "Attachment [3456-prelim.patch](tarball://root/attachments/some-uuid/ticket3456/3456-prelim.patch) by boothby created at 2008-07-04 07:28:12\n\nvery very pre-pre-alpha!",
    "created_at": "2008-07-04T07:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3456#issuecomment-24315",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [3456-prelim.patch](tarball://root/attachments/some-uuid/ticket3456/3456-prelim.patch) by boothby created at 2008-07-04 07:28:12

very very pre-pre-alpha!



---

archive/issue_comments_024316.json:
```json
{
    "body": "The attachment 3456-prelim.patch is a start.  Currently, it makes the notebook unrunnable.  The schema contained in base.py should be taken as a suggestion, and has not been tested.  One big issue that's currently slowing my progress is unfamiliarity with certain unpickling issues.  I'll be able to experimentally verify what will work, but it's taking much more time than expected.  The problem is, every object that's databased through the SQLAlchemy ORM must inherit from Object.  Further, it would be nice to use the [declarative base model](http://www.sqlalchemy.org/docs/05/ormtutorial.html#datamapping_declarative).  I'm not sure what happens when one unpickles an instance of a class which has changed to inherit from something else, etc, so I'm unsure how I should proceed here.",
    "created_at": "2008-07-04T07:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3456#issuecomment-24316",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

The attachment 3456-prelim.patch is a start.  Currently, it makes the notebook unrunnable.  The schema contained in base.py should be taken as a suggestion, and has not been tested.  One big issue that's currently slowing my progress is unfamiliarity with certain unpickling issues.  I'll be able to experimentally verify what will work, but it's taking much more time than expected.  The problem is, every object that's databased through the SQLAlchemy ORM must inherit from Object.  Further, it would be nice to use the [declarative base model](http://www.sqlalchemy.org/docs/05/ormtutorial.html#datamapping_declarative).  I'm not sure what happens when one unpickles an instance of a class which has changed to inherit from something else, etc, so I'm unsure how I should proceed here.



---

archive/issue_events_007835.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/boothby",
    "created_at": "2008-07-14T20:39:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3456#event-7835"
}
```



---

archive/issue_comments_024317.json:
```json
{
    "body": "Changing priority from blocker to minor.",
    "created_at": "2008-07-14T20:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3456#issuecomment-24317",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing priority from blocker to minor.



---

archive/issue_comments_024318.json:
```json
{
    "body": "I'm officially back-burnering this because 1) wstein has resolved the biggest problem that this addresses, 2) I'm busier than I expected to be, and I can't devote myself to such a large-scale project.  If somebody else wants to take the torch, I support it.",
    "created_at": "2008-07-14T20:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3456#issuecomment-24318",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

I'm officially back-burnering this because 1) wstein has resolved the biggest problem that this addresses, 2) I'm busier than I expected to be, and I can't devote myself to such a large-scale project.  If somebody else wants to take the torch, I support it.



---

archive/issue_comments_024319.json:
```json
{
    "body": "Nice idea!  But at this point probably needs to be \"wontfix\" because real database stuff is in the cloud and the notebook will probably be dedicated to smaller-scale solutions.",
    "created_at": "2014-09-17T02:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3456#issuecomment-24319",
    "user": "https://github.com/kcrisman"
}
```

Nice idea!  But at this point probably needs to be "wontfix" because real database stuff is in the cloud and the notebook will probably be dedicated to smaller-scale solutions.



---

archive/issue_comments_024320.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-17T02:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3456#issuecomment-24320",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_events_007836.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2014-09-17T02:58:18Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "milestone": "sage-wishlist",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3456#event-7836"
}
```



---

archive/issue_events_007837.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2014-09-17T02:58:18Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3456#event-7837"
}
```



---

archive/issue_comments_024321.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-17T02:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3456#issuecomment-24321",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007838.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-09-18T18:00:06Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3456#event-7838"
}
```



---

archive/issue_comments_024322.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2014-09-18T18:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3456#issuecomment-24322",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix
