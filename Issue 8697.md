# Issue 8697: Add basic generic test methods

archive/issues_008697.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: generic tests\n\nIn SageObject:\n\n- _test_eq: tests self == self, (self != self) == False, (self == None) == False, self != None (this would have caught #8695)\n\n- _test_hash: test that the result of __hash__ is an int or that it raises an appropriate exception\n\n- Please Florent, add here what we had thought about\n\nIssue created by migration from https://trac.sagemath.org/ticket/8697\n\n",
    "created_at": "2010-04-16T21:37:32Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Add basic generic test methods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8697",
    "user": "nthiery"
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

archive/issue_comments_079225.json:
```json
{
    "body": ">  - Please Florent, add here what we had thought about\n\nThis looks like a duplicate of #8402... and should be closed.",
    "created_at": "2010-04-16T23:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8697#issuecomment-79225",
    "user": "hivert"
}
```

>  - Please Florent, add here what we had thought about

This looks like a duplicate of #8402... and should be closed.



---

archive/issue_comments_079226.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-04-18T10:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8697#issuecomment-79226",
    "user": "nthiery"
}
```

Resolution: duplicate



---

archive/issue_comments_079227.json:
```json
{
    "body": "Replying to [comment:1 hivert]:\n> >  - Please Florent, add here what we had thought about\n> \n> This looks like a duplicate of #8402... and should be closed.\n\nOops, right. Sorry.",
    "created_at": "2010-04-18T10:02:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8697",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8697#issuecomment-79227",
    "user": "nthiery"
}
```

Replying to [comment:1 hivert]:
> >  - Please Florent, add here what we had thought about
> 
> This looks like a duplicate of #8402... and should be closed.

Oops, right. Sorry.
