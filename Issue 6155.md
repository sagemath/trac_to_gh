# Issue 6155: fix stein-watkins huge optional database

archive/issues_006155.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nThe full Stein-Watkins package fails to install cleanly on x86_64-\nredhat-linux\n\nhttp://modular.math.washington.edu/Tables/ecdb/stein-watkins-ecdb.spkg\n\nThe relevant lines from install-log seem to be:\n\nmv: invalid option -- r\nTry `mv --help' for more information.\n\nSince the install script only moves some .bz2 files into the data\ndirectory, it's easy to figure out how to do this by hand and after a\n2.7Gb download, one is remarkably motivated to do so. So I'm a very\nhappy user of the database now. But William might want to fix the\ninstall script ...\n\nCheers,\n\nNils\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6155\n\n",
    "created_at": "2009-05-30T03:52:10Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fix stein-watkins huge optional database",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6155",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd


```
The full Stein-Watkins package fails to install cleanly on x86_64-
redhat-linux

http://modular.math.washington.edu/Tables/ecdb/stein-watkins-ecdb.spkg

The relevant lines from install-log seem to be:

mv: invalid option -- r
Try `mv --help' for more information.

Since the install script only moves some .bz2 files into the data
directory, it's easy to figure out how to do this by hand and after a
2.7Gb download, one is remarkably motivated to do so. So I'm a very
happy user of the database now. But William might want to fix the
install script ...

Cheers,

Nils
```


Issue created by migration from https://trac.sagemath.org/ticket/6155





---

archive/issue_events_014475.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6155",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6155#event-14475"
}
```



---

archive/issue_comments_049018.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-13T16:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6155#issuecomment-49018",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_049019.json:
```json
{
    "body": "`http://modular.math.washington.edu/Tables/ecdb/stein-watkins-ecdb.spkg` still contains a broken package, but at least the updated one at http://www.sagemath.org/spkg/huge/stein-watkins-ecdb.spkg works.",
    "created_at": "2013-08-13T16:09:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6155#issuecomment-49019",
    "user": "https://github.com/jdemeyer"
}
```

`http://modular.math.washington.edu/Tables/ecdb/stein-watkins-ecdb.spkg` still contains a broken package, but at least the updated one at http://www.sagemath.org/spkg/huge/stein-watkins-ecdb.spkg works.



---

archive/issue_events_014476.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T16:09:32Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6155",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6155#event-14476"
}
```



---

archive/issue_events_014477.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T16:09:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6155",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6155#event-14477"
}
```



---

archive/issue_comments_049020.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-08-13T16:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6155#issuecomment-49020",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_014478.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-16T11:12:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6155",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6155#event-14478"
}
```



---

archive/issue_comments_049021.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-08-16T11:12:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6155",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6155#issuecomment-49021",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
