# Issue 6047: Disable threading for boehm_gc

archive/issues_006047.json:
```json
{
    "body": "Assignee: mabshoff\n\nThreading causes trouble when building ecl against boehm since we need to link threading libraries into ecl, so just don't enable them in boehm. \n\nWhile I am in there also remove all the OSX crap from some finder indexing run.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/6047\n\n",
    "created_at": "2009-05-15T21:21:09Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Disable threading for boehm_gc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6047",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Threading causes trouble when building ecl against boehm since we need to link threading libraries into ecl, so just don't enable them in boehm. 

While I am in there also remove all the OSX crap from some finder indexing run.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/6047





---

archive/issue_comments_048091.json:
```json
{
    "body": "This was a red herring - invalid.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-16T00:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6047#issuecomment-48091",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This was a red herring - invalid.

Cheers,

Michael



---

archive/issue_events_006302.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-05-16T00:18:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6047",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6047#event-6302"
}
```



---

archive/issue_comments_048092.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-05-16T00:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6047",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6047#issuecomment-48092",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: invalid
