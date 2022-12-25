# Issue 6682: Support non-ASCII characters in Sage sources

archive/issues_006682.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  mvngu @kini\n\nThis involves at least fixing the documentation build process and trac to support utf-8. Possibly other components as well. \n\nDiscussion at http://groups.google.com/group/sage-devel/browse_thread/thread/ff129ae1c62d5a78\n\nIssue created by migration from https://trac.sagemath.org/ticket/6682\n\n",
    "created_at": "2009-08-07T07:03:17Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Support non-ASCII characters in Sage sources",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6682",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd

CC:  mvngu @kini

This involves at least fixing the documentation build process and trac to support utf-8. Possibly other components as well. 

Discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/ff129ae1c62d5a78

Issue created by migration from https://trac.sagemath.org/ticket/6682





---

archive/issue_comments_054845.json:
```json
{
    "body": "Script to prepend coding to .py(x) files.  Not a patch.",
    "created_at": "2010-01-21T04:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6682#issuecomment-54845",
    "user": "https://github.com/qed777"
}
```

Script to prepend coding to .py(x) files.  Not a patch.



---

archive/issue_comments_054846.json:
```json
{
    "body": "Attachment [prependify.py](tarball://root/attachments/some-uuid/ticket6682/prependify.py) by @qed777 created at 2010-01-21 04:47:22\n\nFrom my brief experience with Unicode in SageNB sources (#7249 adds them to doctests), we may just need to\n\n* Prepend `# -*- coding: utf-8 -*-` to every .py file.  I assume we should do this for .pyx files, too.  I've attached a [attachment:prependify.py script] that can do this, although I'm sure there are more succinct ways.\n\n* Use `unicode` strings for docstrings that contain non-ASCII Unicode characters.  For example,\n\n```python\ndef f(n):\n    u\"\"\"\n    Transmogrifies ``n``, heinously. \u263a\n    \"\"\"\n    return transmogrify(n, algorithm='heinous')\n```\n\nNote: At #8000, Minh suggested polling sage-devel about allowing non-ASCII characters in Sage library code.  I'll try to do this soon.",
    "created_at": "2010-01-21T04:47:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6682#issuecomment-54846",
    "user": "https://github.com/qed777"
}
```

Attachment [prependify.py](tarball://root/attachments/some-uuid/ticket6682/prependify.py) by @qed777 created at 2010-01-21 04:47:22

From my brief experience with Unicode in SageNB sources (#7249 adds them to doctests), we may just need to

* Prepend `# -*- coding: utf-8 -*-` to every .py file.  I assume we should do this for .pyx files, too.  I've attached a [attachment:prependify.py script] that can do this, although I'm sure there are more succinct ways.

* Use `unicode` strings for docstrings that contain non-ASCII Unicode characters.  For example,

```python
def f(n):
    u"""
    Transmogrifies ``n``, heinously. ☺
    """
    return transmogrify(n, algorithm='heinous')
```

Note: At #8000, Minh suggested polling sage-devel about allowing non-ASCII characters in Sage library code.  I'll try to do this soon.



---

archive/issue_events_015765.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6682#event-15765"
}
```



---

archive/issue_events_015766.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6682#event-15766"
}
```



---

archive/issue_events_015767.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6682#event-15767"
}
```



---

archive/issue_comments_054847.json:
```json
{
    "body": "We already do support UTF-8 in Sage sources, nothing to see here...",
    "created_at": "2014-02-14T12:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6682#issuecomment-54847",
    "user": "https://github.com/jdemeyer"
}
```

We already do support UTF-8 in Sage sources, nothing to see here...



---

archive/issue_events_015768.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-02-14T12:39:13Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6682#event-15768"
}
```



---

archive/issue_events_015769.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2014-02-14T12:39:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6682#event-15769"
}
```



---

archive/issue_comments_054848.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-02-14T12:39:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6682#issuecomment-54848",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054849.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-14T12:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6682#issuecomment-54849",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054850.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-19T18:56:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6682#issuecomment-54850",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_015770.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-02-19T18:56:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6682",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6682#event-15770"
}
```
