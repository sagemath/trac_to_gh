# Issue 8413: Add "Unknown" truth value

archive/issues_008413.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  @robertwb\n\nKeywords: Unknown Boolean\n\nAs discussed on [sage-devel](http://groups.google.com/group/sage-devel/t/5d9c32390ffe3c96) it could be good to have an \"Unkown\" value in sage which semantic is a truth value. Here are the intended truth table:\n\n```\n      and             or\n    F  U  T         F  U  T\n F [F, F, F]     F [F, U, T]\n U [F, U, U]     U [U, U, T]\n T [F, U, T]     T [T, T, T]\n```\nUnfortunately, without [PEP 335](http://www.python.org/dev/peps/pep-0335/), there is no way to achieve this with python's \"and\" and \"or\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/8413\n\n",
    "created_at": "2010-03-01T23:05:49Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Add \"Unknown\" truth value",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8413",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

CC:  @robertwb

Keywords: Unknown Boolean

As discussed on [sage-devel](http://groups.google.com/group/sage-devel/t/5d9c32390ffe3c96) it could be good to have an "Unkown" value in sage which semantic is a truth value. Here are the intended truth table:

```
      and             or
    F  U  T         F  U  T
 F [F, F, F]     F [F, U, T]
 U [F, U, U]     U [U, U, T]
 T [F, U, T]     T [T, T, T]
```
Unfortunately, without [PEP 335](http://www.python.org/dev/peps/pep-0335/), there is no way to achieve this with python's "and" and "or".

Issue created by migration from https://trac.sagemath.org/ticket/8413





---

archive/issue_comments_075255.json:
```json
{
    "body": "Attachment [trac_8413-Unknown_bool_value-fh.patch](tarball://root/attachments/some-uuid/ticket8413/trac_8413-Unknown_bool_value-fh.patch) by @hivert created at 2010-03-02 11:10:09",
    "created_at": "2010-03-02T11:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8413#issuecomment-75255",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8413-Unknown_bool_value-fh.patch](tarball://root/attachments/some-uuid/ticket8413/trac_8413-Unknown_bool_value-fh.patch) by @hivert created at 2010-03-02 11:10:09



---

archive/issue_comments_075256.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-02T11:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8413#issuecomment-75256",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075257.json:
```json
{
    "body": "For the record: all test pass.",
    "created_at": "2010-04-16T21:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8413#issuecomment-75257",
    "user": "https://github.com/nthiery"
}
```

For the record: all test pass.



---

archive/issue_comments_075258.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-22T23:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8413#issuecomment-75258",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075259.json:
```json
{
    "body": "Looks good.",
    "created_at": "2010-06-22T23:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8413#issuecomment-75259",
    "user": "https://github.com/robertwb"
}
```

Looks good.



---

archive/issue_events_020163.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-22T07:35:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8413",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8413#event-20163"
}
```



---

archive/issue_comments_075260.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T07:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8413",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8413#issuecomment-75260",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed
