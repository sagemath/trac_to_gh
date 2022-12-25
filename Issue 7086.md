# Issue 7086: vanilla hg vs. "sage -hg"

archive/issues_007086.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @hemmecke\n\nKeywords: hg\n\nVanilla hg accepts something like\n\n  hg commit -m 'some comment'\n\nHowever, if hg is a script that calls \"sage -hg\" (like /usr/local/bin/hg on sage.math.washington.edu), then the above command does not work.\n\nThe following was issued on the above server:\nmkdir a\ncd a\nhg init\necho \"abc def\" > abc\nhg add abc\nhg commit -m 'some comment'\ncomment: No such file or directory\nabort: file comment not found!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7086\n\n",
    "created_at": "2009-09-30T23:20:20Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "vanilla hg vs. \"sage -hg\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7086",
    "user": "https://github.com/hemmecke"
}
```
Assignee: cwitty

CC:  @hemmecke

Keywords: hg

Vanilla hg accepts something like

  hg commit -m 'some comment'

However, if hg is a script that calls "sage -hg" (like /usr/local/bin/hg on sage.math.washington.edu), then the above command does not work.

The following was issued on the above server:
mkdir a
cd a
hg init
echo "abc def" > abc
hg add abc
hg commit -m 'some comment'
comment: No such file or directory
abort: file comment not found!

Issue created by migration from https://trac.sagemath.org/ticket/7086





---

archive/issue_events_016762.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-10-10T21:36:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7086",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7086#event-16762"
}
```



---

archive/issue_comments_058465.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-10T21:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7086#issuecomment-58465",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058466.json:
```json
{
    "body": "This seems to be fixed now.",
    "created_at": "2010-10-10T21:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7086#issuecomment-58466",
    "user": "https://github.com/jdemeyer"
}
```

This seems to be fixed now.



---

archive/issue_events_016763.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-10-22T09:20:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7086",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7086#event-16763"
}
```



---

archive/issue_comments_058467.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-10-22T09:20:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7086",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7086#issuecomment-58467",
    "user": "https://github.com/qed777"
}
```

Resolution: worksforme
