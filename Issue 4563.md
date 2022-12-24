# Issue 4563: polar plot does not accept (t, 0, 2*pi) syntax for the interval

archive/issues_004563.json:
```json
{
    "body": "Assignee: was\n\nCC:  mhansen\n\nThis does not work:\n\n\n```\nsage: polar_plot(x, (x, 0, 1))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/jason/<ipython console> in <module>()\n\nTypeError: polar_plot() takes exactly 3 arguments (2 given)\n```\n\n\nBut this does:\n\n\n```\nsage: polar_plot(x,0, 1)\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4563\n\n",
    "created_at": "2008-11-20T08:19:26Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "polar plot does not accept (t, 0, 2*pi) syntax for the interval",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4563",
    "user": "jason"
}
```
Assignee: was

CC:  mhansen

This does not work:


```
sage: polar_plot(x, (x, 0, 1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/jason/<ipython console> in <module>()

TypeError: polar_plot() takes exactly 3 arguments (2 given)
```


But this does:


```
sage: polar_plot(x,0, 1)
```




Issue created by migration from https://trac.sagemath.org/ticket/4563





---

archive/issue_comments_034177.json:
```json
{
    "body": "Ccing mhansen since he is currently working on plotting code.",
    "created_at": "2008-11-20T08:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4563#issuecomment-34177",
    "user": "jason"
}
```

Ccing mhansen since he is currently working on plotting code.



---

archive/issue_comments_034178.json:
```json
{
    "body": "Attachment [trac-4563.patch](tarball://root/attachments/some-uuid/ticket4563/trac-4563.patch) by jason created at 2009-01-22 19:00:44",
    "created_at": "2009-01-22T19:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4563#issuecomment-34178",
    "user": "jason"
}
```

Attachment [trac-4563.patch](tarball://root/attachments/some-uuid/ticket4563/trac-4563.patch) by jason created at 2009-01-22 19:00:44



---

archive/issue_comments_034179.json:
```json
{
    "body": "Looks good to me. Just a touch of fuzz for against, 3.2.3, but it merged fine.",
    "created_at": "2009-01-23T04:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4563#issuecomment-34179",
    "user": "robertwb"
}
```

Looks good to me. Just a touch of fuzz for against, 3.2.3, but it merged fine.



---

archive/issue_comments_034180.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4563#issuecomment-34180",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034181.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T08:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4563#issuecomment-34181",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha1
