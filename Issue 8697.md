# Issue 8697: Add basic generic test methods

archive/issues_008697.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: generic tests\n\nIn SageObject:\n\n- _test_eq: tests self == self, (self != self) == False, (self == None) == False, self != None (this would have caught #8695)\n\n- _test_hash: test that the result of __hash__ is an int or that it raises an appropriate exception\n\n- Please Florent, add here what we had thought about\n\nIssue created by migration from https://trac.sagemath.org/ticket/8697\n\n",
    "created_at": "2010-04-16T21:37:32Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Add basic generic test methods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8697",
    "user": "https://github.com/nthiery"
}
```
Assignee: tbd

Keywords: generic tests

In SageObject:

- _test_eq: tests self == self, (self != self) == False, (self == None) == False, self != None (this would have caught #8695)

- _test_hash: test that the result of __hash__ is an int or that it raises an appropriate exception

- Please Florent, add here what we had thought about

Issue created by migration from https://trac.sagemath.org/ticket/8697





---

archive/issue_comments_079095.json:
```json
{
    "body": ">  - Please Florent, add here what we had thought about\n\nThis looks like a duplicate of #8402... and should be closed.",
    "created_at": "2010-04-16T23:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8697#issuecomment-79095",
    "user": "https://github.com/hivert"
}
```

>  - Please Florent, add here what we had thought about

This looks like a duplicate of #8402... and should be closed.



---

archive/issue_comments_079096.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-04-18T10:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8697#issuecomment-79096",
    "user": "https://github.com/nthiery"
}
```

Resolution: duplicate



---

archive/issue_comments_079097.json:
```json
{
    "body": "Replying to [comment:1 hivert]:\n> >  - Please Florent, add here what we had thought about\n> \n> This looks like a duplicate of #8402... and should be closed.\n\nOops, right. Sorry.",
    "created_at": "2010-04-18T10:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8697#issuecomment-79097",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:1 hivert]:
> >  - Please Florent, add here what we had thought about
> 
> This looks like a duplicate of #8402... and should be closed.

Oops, right. Sorry.



---

archive/issue_events_021100.json:
```json
{
    "actor": "https://github.com/nthiery",
    "created_at": "2010-04-18T10:02:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8697",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8697#event-21100"
}
```



---

archive/issue_events_021101.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-04-18T23:54:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8697",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8697#event-21101"
}
```
