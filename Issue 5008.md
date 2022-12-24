# Issue 5008: Solaris/gcc 4.3.2: fix matplotlib build

archive/issues_005008.json:
```json
{
    "body": "Assignee: mabshoff\n\nMatplotlib has some build problems on Solaris when using gcc 4.3.2 that do not happen on other platforms.\n\nSpkg coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5008\n\n",
    "created_at": "2009-01-18T06:31:49Z",
    "labels": [
        "porting: Solaris",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Solaris/gcc 4.3.2: fix matplotlib build",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5008",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Matplotlib has some build problems on Solaris when using gcc 4.3.2 that do not happen on other platforms.

Spkg coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5008





---

archive/issue_comments_038183.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-18T06:31:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5008#issuecomment-38183",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038184.json:
```json
{
    "body": "The spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/matplotlib-0.98.3.p5.spkg\n\nadds a Solaris 10 specific workaround. On other platforms the workaround is not applied.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T11:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5008#issuecomment-38184",
    "user": "mabshoff"
}
```

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/alpha0/matplotlib-0.98.3.p5.spkg

adds a Solaris 10 specific workaround. On other platforms the workaround is not applied.

Cheers,

Michael



---

archive/issue_comments_038185.json:
```json
{
    "body": "Works fine for me.",
    "created_at": "2009-01-19T11:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5008#issuecomment-38185",
    "user": "mhansen"
}
```

Works fine for me.



---

archive/issue_comments_038186.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T12:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5008#issuecomment-38186",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_038187.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T12:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5008",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5008#issuecomment-38187",
    "user": "mabshoff"
}
```

Resolution: fixed
