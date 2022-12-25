# Issue 5006: the hg script installed by install_script() does not pass parameters correctly

archive/issues_005006.json:
```json
{
    "body": "Assignee: cwitty\n\nThe script currently is:\n\n```/bin/sh\nsage -hg $*\n```\nBut this is broken when running something like\n\n```\nhg ci -u \"User Foo\"\n```\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5006\n\n",
    "created_at": "2009-01-18T05:10:24Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "the hg script installed by install_script() does not pass parameters correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5006",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: cwitty

The script currently is:

```/bin/sh
sage -hg $*
```
But this is broken when running something like

```
hg ci -u "User Foo"
```

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5006





---

archive/issue_comments_038103.json:
```json
{
    "body": "This seems to be fixed.",
    "created_at": "2010-10-10T21:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5006#issuecomment-38103",
    "user": "https://github.com/jdemeyer"
}
```

This seems to be fixed.



---

archive/issue_events_011572.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-10-10T21:27:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5006",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5006#event-11572"
}
```



---

archive/issue_comments_038104.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-10T21:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5006#issuecomment-38104",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_038105.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-12-03T06:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5006#issuecomment-38105",
    "user": "https://github.com/robertwb"
}
```

Resolution: worksforme



---

archive/issue_events_011573.json:
```json
{
    "actor": "https://github.com/robertwb",
    "created_at": "2010-12-03T06:56:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5006",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5006#event-11573"
}
```
