# Issue 3551: magma_version command

archive/issues_003551.json:
```json
{
    "body": "Assignee: tba\n\nThe magma_version command is not documented; I would suggest that it say \"this command returns a tuple of the form ((int,int,int),str) giving the version numbers, and it depends on having magma installed\".\n\nIt also actually calls magma (to ask it its version number, I think). Would it be worth storing the version information in a file somewhere to aviod having to start a magma session?\n\nIssue created by migration from https://trac.sagemath.org/ticket/3551\n\n",
    "created_at": "2008-07-05T11:39:11Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "title": "magma_version command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3551",
    "user": "ljpk"
}
```
Assignee: tba

The magma_version command is not documented; I would suggest that it say "this command returns a tuple of the form ((int,int,int),str) giving the version numbers, and it depends on having magma installed".

It also actually calls magma (to ask it its version number, I think). Would it be worth storing the version information in a file somewhere to aviod having to start a magma session?

Issue created by migration from https://trac.sagemath.org/ticket/3551





---

archive/issue_comments_025117.json:
```json
{
    "body": "You can't store it in a file since the Magma version on any given system could be different.\n\nThat being said, lots of functions in sage/interfaces/ need to be documented.",
    "created_at": "2008-07-05T23:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3551#issuecomment-25117",
    "user": "mhansen"
}
```

You can't store it in a file since the Magma version on any given system could be different.

That being said, lots of functions in sage/interfaces/ need to be documented.



---

archive/issue_comments_025118.json:
```json
{
    "body": "> It also actually calls magma (to ask it its version number, I think). Would it be worth storing the \n> version information in a file somewhere to aviod having to start a magma session? \n\nAlso, it would suddenly give a wrong answer as soon as one changes their magma version, which presumably happens a lot. \n\nWilliam",
    "created_at": "2008-07-07T00:16:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3551#issuecomment-25118",
    "user": "was"
}
```

> It also actually calls magma (to ask it its version number, I think). Would it be worth storing the 
> version information in a file somewhere to aviod having to start a magma session? 

Also, it would suddenly give a wrong answer as soon as one changes their magma version, which presumably happens a lot. 

William



---

archive/issue_comments_025119.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-07-07T00:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3551#issuecomment-25119",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_025120.json:
```json
{
    "body": "This was now closed by some other magma documentation patch that is in 3.1.4.",
    "created_at": "2008-10-23T16:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3551#issuecomment-25120",
    "user": "was"
}
```

This was now closed by some other magma documentation patch that is in 3.1.4.



---

archive/issue_comments_025121.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-23T16:34:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3551",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3551#issuecomment-25121",
    "user": "was"
}
```

Resolution: fixed
