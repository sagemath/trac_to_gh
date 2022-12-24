# Issue 5006: the hg script installed by install_script() does not pass parameters correctly

archive/issues_005006.json:
```json
{
    "body": "Assignee: cwitty\n\nThe script currently is:\n\n```/bin/sh\nsage -hg $*\n```\n\nBut this is broken when running something like\n\n```\nhg ci -u \"User Foo\"\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5006\n\n",
    "created_at": "2009-01-18T05:10:24Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "the hg script installed by install_script() does not pass parameters correctly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5006",
    "user": "mabshoff"
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

archive/issue_comments_038175.json:
```json
{
    "body": "This seems to be fixed.",
    "created_at": "2010-10-10T21:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5006#issuecomment-38175",
    "user": "@jdemeyer"
}
```

This seems to be fixed.



---

archive/issue_comments_038176.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-10T21:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5006#issuecomment-38176",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_038177.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-12-03T06:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5006",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5006#issuecomment-38177",
    "user": "@robertwb"
}
```

Resolution: worksforme
