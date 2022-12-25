# Issue 733: generating docs

archive/issues_000733.json:
```json
{
    "body": "Assignee: tba\n\nI updated the reference manual tex files by doing:\n\ncd sage/devel/doc/ref/\n./update\ncd ..\nmake pdf\n\nHowever, it claimed that there was nothing to be done, since everything was up to date.  I had to make clobber before it would build the documentation again.\n\nIs there a way to have the ./update command touch a file which was then a dependency for the make pdf/html/etc commands?  That way, running ./update would force make to rerun the pdf/html/etc generation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/733\n\n",
    "created_at": "2007-09-21T19:18:07Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "generating docs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/733",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tba

I updated the reference manual tex files by doing:

cd sage/devel/doc/ref/
./update
cd ..
make pdf

However, it claimed that there was nothing to be done, since everything was up to date.  I had to make clobber before it would build the documentation again.

Is there a way to have the ./update command touch a file which was then a dependency for the make pdf/html/etc commands?  That way, running ./update would force make to rerun the pdf/html/etc generation.


Issue created by migration from https://trac.sagemath.org/ticket/733





---

archive/issue_comments_004286.json:
```json
{
    "body": "I think this has been fixed. \n\nCheers,\n\nMichael",
    "created_at": "2008-03-11T01:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/733#issuecomment-4286",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I think this has been fixed. 

Cheers,

Michael



---

archive/issue_comments_004287.json:
```json
{
    "body": "`rebuild` works, so I am closing this. If anything comes up again please open a more specific  ticket with an actual example.",
    "created_at": "2008-03-22T05:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/733#issuecomment-4287",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

`rebuild` works, so I am closing this. If anything comes up again please open a more specific  ticket with an actual example.



---

archive/issue_events_000820.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-22T05:58:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/733",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/733#event-820"
}
```



---

archive/issue_comments_004288.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2008-03-22T05:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/733#issuecomment-4288",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: worksforme
