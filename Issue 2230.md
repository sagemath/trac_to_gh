# Issue 2230: sage-2.10.2.alpha1 -- linear algebra hash not implemented

archive/issues_002230.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis was my fault, caused by me not having a 64-bit install to test on when I implemented the patch.  Just fix it by putting the correct answer in under #64-bit\n\n```\n         [1.3 s]\nsage -t  devel/sage-main/sage/modules/quotient_module.py    **********************************************************************\nFile \"quotient_module.py\", line 130:\n    sage: hash(Q)\nExpected:\n    fixme\nGot:\n    -5856620741060301410\n**********************************************************************\nFile \"quotient_module.py\", line 135:\n    sage: hash((V, W))\nExpected:\n    fixme\nGot:\n    -5856620741060301410\n**********************************************************************\n1 items had failures:\n   2 of   4 in __main__.example_3\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file .doctest_quotient_module.py\n         [1.7 s]\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2230\n\n",
    "created_at": "2008-02-20T07:04:30Z",
    "labels": [
        "component: linear algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "sage-2.10.2.alpha1 -- linear algebra hash not implemented",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2230",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This was my fault, caused by me not having a 64-bit install to test on when I implemented the patch.  Just fix it by putting the correct answer in under #64-bit

```
         [1.3 s]
sage -t  devel/sage-main/sage/modules/quotient_module.py    **********************************************************************
File "quotient_module.py", line 130:
    sage: hash(Q)
Expected:
    fixme
Got:
    -5856620741060301410
**********************************************************************
File "quotient_module.py", line 135:
    sage: hash((V, W))
Expected:
    fixme
Got:
    -5856620741060301410
**********************************************************************
1 items had failures:
   2 of   4 in __main__.example_3
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_quotient_module.py
         [1.7 s]

```


Issue created by migration from https://trac.sagemath.org/ticket/2230





---

archive/issue_comments_014741.json:
```json
{
    "body": "Attachment [sage-2230.patch](tarball://root/attachments/some-uuid/ticket2230/sage-2230.patch) by @williamstein created at 2008-02-21 18:34:48",
    "created_at": "2008-02-21T18:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2230#issuecomment-14741",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2230.patch](tarball://root/attachments/some-uuid/ticket2230/sage-2230.patch) by @williamstein created at 2008-02-21 18:34:48



---

archive/issue_comments_014742.json:
```json
{
    "body": "Patch is simple enough, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T18:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2230#issuecomment-14742",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch is simple enough, positive review.

Cheers,

Michael



---

archive/issue_comments_014743.json:
```json
{
    "body": "Merged in Sage 2.10.2.rc0",
    "created_at": "2008-02-21T18:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2230#issuecomment-14743",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.rc0



---

archive/issue_events_005311.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-21T18:52:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2230",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2230#event-5311"
}
```



---

archive/issue_comments_014744.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T18:52:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2230#issuecomment-14744",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
