# Issue 4563: polar plot does not accept (t, 0, 2*pi) syntax for the interval

archive/issues_004563.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @mwhansen\n\nThis does not work:\n\n\n```\nsage: polar_plot(x, (x, 0, 1))\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/jason/<ipython console> in <module>()\n\nTypeError: polar_plot() takes exactly 3 arguments (2 given)\n```\n\n\nBut this does:\n\n\n```\nsage: polar_plot(x,0, 1)\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4563\n\n",
    "created_at": "2008-11-20T08:19:26Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "polar plot does not accept (t, 0, 2*pi) syntax for the interval",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4563",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  @mwhansen

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

archive/issue_comments_034110.json:
```json
{
    "body": "Ccing mhansen since he is currently working on plotting code.",
    "created_at": "2008-11-20T08:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4563#issuecomment-34110",
    "user": "https://github.com/jasongrout"
}
```

Ccing mhansen since he is currently working on plotting code.



---

archive/issue_comments_034111.json:
```json
{
    "body": "Attachment [trac-4563.patch](tarball://root/attachments/some-uuid/ticket4563/trac-4563.patch) by @jasongrout created at 2009-01-22 19:00:44",
    "created_at": "2009-01-22T19:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4563#issuecomment-34111",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-4563.patch](tarball://root/attachments/some-uuid/ticket4563/trac-4563.patch) by @jasongrout created at 2009-01-22 19:00:44



---

archive/issue_comments_034112.json:
```json
{
    "body": "Looks good to me. Just a touch of fuzz for against, 3.2.3, but it merged fine.",
    "created_at": "2009-01-23T04:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4563#issuecomment-34112",
    "user": "https://github.com/robertwb"
}
```

Looks good to me. Just a touch of fuzz for against, 3.2.3, but it merged fine.



---

archive/issue_comments_034113.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T08:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4563#issuecomment-34113",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034114.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T08:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4563",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4563#issuecomment-34114",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1
