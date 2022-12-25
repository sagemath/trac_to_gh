# Issue 9804: save_session is completely broken in the notebook

archive/issues_009804.json:
```json
{
    "body": "Assignee: jason, was\n\nTry\n\n```\nsave_session('foo')\n```\n\nin the notebook.  Boom!\n\nThe problem is these lines in misc/session.pyx:\n\n```\n    if embedded():\n        # Also save D to the data directory if we're using the notebook.\n        save(D, '../../data/' + name)\n```\n\n\nWhen I rewrote the notebook I forgot to change this appropriately.  I'm not sure exactly what the right fix is, but it is to somehow replace '../../data/' by the data\ndirectory (which is defined by the variable DATA in the notebook).\n\nIssue created by migration from https://trac.sagemath.org/ticket/9805\n\n",
    "created_at": "2010-08-26T03:09:59Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "save_session is completely broken in the notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9804",
    "user": "https://github.com/williamstein"
}
```
Assignee: jason, was

Try

```
save_session('foo')
```

in the notebook.  Boom!

The problem is these lines in misc/session.pyx:

```
    if embedded():
        # Also save D to the data directory if we're using the notebook.
        save(D, '../../data/' + name)
```


When I rewrote the notebook I forgot to change this appropriately.  I'm not sure exactly what the right fix is, but it is to somehow replace '../../data/' by the data
directory (which is defined by the variable DATA in the notebook).

Issue created by migration from https://trac.sagemath.org/ticket/9805





---

archive/issue_comments_096170.json:
```json
{
    "body": "Attachment [trac_9805.patch](tarball://root/attachments/some-uuid/ticket9805/trac_9805.patch) by @ppurka created at 2013-08-09 17:01:06\n\n[attachment:trac_9805.patch Example patch] is provided to inform user of the workaround. I don't see how to get the worksheet directory of the user automatically. The DATA variable seems inaccessible from session.pyx.",
    "created_at": "2013-08-09T17:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9804#issuecomment-96170",
    "user": "https://github.com/ppurka"
}
```

Attachment [trac_9805.patch](tarball://root/attachments/some-uuid/ticket9805/trac_9805.patch) by @ppurka created at 2013-08-09 17:01:06

[attachment:trac_9805.patch Example patch] is provided to inform user of the workaround. I don't see how to get the worksheet directory of the user automatically. The DATA variable seems inaccessible from session.pyx.



---

archive/issue_comments_096171.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-09T17:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9804#issuecomment-96171",
    "user": "https://github.com/ppurka"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096172.json:
```json
{
    "body": "Actually, this is pretty nice.  It tells of a workaround that is not onerous and should be familiar to people using the notebook.  What do you think, in retrospect?",
    "created_at": "2014-08-15T09:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9804#issuecomment-96172",
    "user": "https://github.com/kcrisman"
}
```

Actually, this is pretty nice.  It tells of a workaround that is not onerous and should be familiar to people using the notebook.  What do you think, in retrospect?



---

archive/issue_comments_096173.json:
```json
{
    "body": "Replying to [comment:6 kcrisman]:\n> Actually, this is pretty nice.  It tells of a workaround that is not onerous and should be familiar to people using the notebook.  What do you think, in retrospect?\nI don't even remember why I tried to patch this. If you think it is useful, I can create the git branch.",
    "created_at": "2014-08-17T06:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9804#issuecomment-96173",
    "user": "https://github.com/ppurka"
}
```

Replying to [comment:6 kcrisman]:
> Actually, this is pretty nice.  It tells of a workaround that is not onerous and should be familiar to people using the notebook.  What do you think, in retrospect?
I don't even remember why I tried to patch this. If you think it is useful, I can create the git branch.



---

archive/issue_comments_096174.json:
```json
{
    "body": "Interestingly, this works even if you *don't* save the worksheet - the cells that one made new disappear, but the sobj still appears.  This works nicely.\n\nIn this one case I am not sure if a doctest is useful - can you think of a viable one?\n----\nNew commits:",
    "created_at": "2014-10-22T18:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9804#issuecomment-96174",
    "user": "https://github.com/kcrisman"
}
```

Interestingly, this works even if you *don't* save the worksheet - the cells that one made new disappear, but the sobj still appears.  This works nicely.

In this one case I am not sure if a doctest is useful - can you think of a viable one?
----
New commits:



---

archive/issue_comments_096175.json:
```json
{
    "body": "I still can't think of one, since although we can test for the creation of the sobj (in fact, it is still created in the cell directory and could be saved!) and we can pretend to be in the notebook, there is no point in testing the message and we can't emulate the data directory without opening a notebook and so forth, not worth that.  In fact, `save_session(DATA)` and so forth works, but once again explicit is probably better than implicit...",
    "created_at": "2014-11-13T19:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9804#issuecomment-96175",
    "user": "https://github.com/kcrisman"
}
```

I still can't think of one, since although we can test for the creation of the sobj (in fact, it is still created in the cell directory and could be saved!) and we can pretend to be in the notebook, there is no point in testing the message and we can't emulate the data directory without opening a notebook and so forth, not worth that.  In fact, `save_session(DATA)` and so forth works, but once again explicit is probably better than implicit...



---

archive/issue_comments_096176.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-11-13T19:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9804#issuecomment-96176",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009928.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-11-14T21:01:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9804",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9804#event-9928"
}
```



---

archive/issue_comments_096177.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-11-14T21:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9804#issuecomment-96177",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_096178.json:
```json
{
    "body": "This issue is actually fixed (as opposed to being warned against) in #17482 - it turned out to be nearly trivial, as there is a symlink to `DATA` in every cell directory!",
    "created_at": "2014-12-10T17:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9804#issuecomment-96178",
    "user": "https://github.com/kcrisman"
}
```

This issue is actually fixed (as opposed to being warned against) in #17482 - it turned out to be nearly trivial, as there is a symlink to `DATA` in every cell directory!
