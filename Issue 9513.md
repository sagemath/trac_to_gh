# Issue 9513: Sage 4.4.4 build fails due to mixing prefix/home

archive/issues_009513.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nOn my System (SuSE 11.1 x86_64). The build fails and complains about mixing --prefix and --home when doing `python install` on various packages: \nnetworkx, mercurial (perhaps more to come))\nIn addition in the spkg of scons --prefix is missing completely.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9513\n\n",
    "closed_at": "2010-08-19T06:47:51Z",
    "created_at": "2010-07-15T21:06:03Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage 4.4.4 build fails due to mixing prefix/home",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9513",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```
Assignee: GeorgSWeber

On my System (SuSE 11.1 x86_64). The build fails and complains about mixing --prefix and --home when doing `python install` on various packages: 
networkx, mercurial (perhaps more to come))
In addition in the spkg of scons --prefix is missing completely.

Issue created by migration from https://trac.sagemath.org/ticket/9513





---

archive/issue_comments_091316.json:
```json
{
    "body": "Changing component from algebra to build.",
    "created_at": "2010-07-29T13:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91316",
    "user": "https://github.com/loefflerd"
}
```

Changing component from algebra to build.



---

archive/issue_comments_091317.json:
```json
{
    "body": "This has very little to do with algebra -- please use appropriate values for \"component\" when creating tickets.",
    "created_at": "2010-07-29T13:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91317",
    "user": "https://github.com/loefflerd"
}
```

This has very little to do with algebra -- please use appropriate values for "component" when creating tickets.



---

archive/issue_comments_091318.json:
```json
{
    "body": "Changing assignee from @aghitza to GeorgSWeber.",
    "created_at": "2010-07-29T13:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91318",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @aghitza to GeorgSWeber.



---

archive/issue_comments_091319.json:
```json
{
    "body": "Hello,\nI think this is just the same as #9536. Its Fix also cures this problem.\n\nRegards,\n  Alexander",
    "created_at": "2010-07-29T14:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91319",
    "user": "https://github.com/alexanderdreyer"
}
```

Hello,
I think this is just the same as #9536. Its Fix also cures this problem.

Regards,
  Alexander



---

archive/issue_events_023629.json:
```json
{
    "actor": "https://github.com/alexanderdreyer",
    "created_at": "2010-08-19T06:47:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9513#event-23629"
}
```



---

archive/issue_comments_091320.json:
```json
{
    "body": "See #9536.",
    "created_at": "2010-08-19T06:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91320",
    "user": "https://github.com/alexanderdreyer"
}
```

See #9536.



---

archive/issue_comments_091321.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-19T06:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91321",
    "user": "https://github.com/alexanderdreyer"
}
```

Resolution: duplicate



---

archive/issue_events_023630.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-08-20T16:52:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9513#event-23630"
}
```
