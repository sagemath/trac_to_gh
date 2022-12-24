# Issue 9513: Sage 4.4.4 build fails due to mixing prefix/home

archive/issues_009513.json:
```json
{
    "body": "Assignee: @aghitza\n\nOn my System (SuSE 11.1 x86_64). The build fails and complains about mixing --prefix and --home when doing `python install` on various packages: \nnetworkx, mercurial (perhaps more to come))\nIn addition in the spkg of scons --prefix is missing completely.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9513\n\n",
    "created_at": "2010-07-15T21:06:03Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage 4.4.4 build fails due to mixing prefix/home",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9513",
    "user": "PolyBoRi"
}
```
Assignee: @aghitza

On my System (SuSE 11.1 x86_64). The build fails and complains about mixing --prefix and --home when doing `python install` on various packages: 
networkx, mercurial (perhaps more to come))
In addition in the spkg of scons --prefix is missing completely.

Issue created by migration from https://trac.sagemath.org/ticket/9513





---

archive/issue_comments_091469.json:
```json
{
    "body": "Changing component from algebra to build.",
    "created_at": "2010-07-29T13:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91469",
    "user": "@loefflerd"
}
```

Changing component from algebra to build.



---

archive/issue_comments_091470.json:
```json
{
    "body": "This has very little to do with algebra -- please use appropriate values for \"component\" when creating tickets.",
    "created_at": "2010-07-29T13:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91470",
    "user": "@loefflerd"
}
```

This has very little to do with algebra -- please use appropriate values for "component" when creating tickets.



---

archive/issue_comments_091471.json:
```json
{
    "body": "Changing assignee from @aghitza to GeorgSWeber.",
    "created_at": "2010-07-29T13:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91471",
    "user": "@loefflerd"
}
```

Changing assignee from @aghitza to GeorgSWeber.



---

archive/issue_comments_091472.json:
```json
{
    "body": "Hello,\nI think this is just the same as #9536. Its Fix also cures this problem.\n\nRegards,\n  Alexander",
    "created_at": "2010-07-29T14:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91472",
    "user": "@alexanderdreyer"
}
```

Hello,
I think this is just the same as #9536. Its Fix also cures this problem.

Regards,
  Alexander



---

archive/issue_comments_091473.json:
```json
{
    "body": "See #9536.",
    "created_at": "2010-08-19T06:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91473",
    "user": "@alexanderdreyer"
}
```

See #9536.



---

archive/issue_comments_091474.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-08-19T06:47:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9513",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9513#issuecomment-91474",
    "user": "@alexanderdreyer"
}
```

Resolution: duplicate
