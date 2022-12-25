# Issue 4168: native mpfr polynomials

archive/issues_004168.json:
```json
{
    "body": "Assignee: tbd\n\n#4151 implements these, should be used by default for RR['x']\n\nIssue created by migration from https://trac.sagemath.org/ticket/4168\n\n",
    "created_at": "2008-09-22T17:59:42Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "native mpfr polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4168",
    "user": "https://github.com/robertwb"
}
```
Assignee: tbd

#4151 implements these, should be used by default for RR['x']

Issue created by migration from https://trac.sagemath.org/ticket/4168





---

archive/issue_comments_030191.json:
```json
{
    "body": "Hi Robert,\n\nwhat is the plan here?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T03:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4168#issuecomment-30191",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Robert,

what is the plan here?

Cheers,

Michael



---

archive/issue_comments_030192.json:
```json
{
    "body": "Well, this is pretty low-hanging fruit, but I've just got too many things higher on my priority list (sage and otherwise). \n\nIf no one else gets around to this, eventually I will. The code is there, it's just a matter of hooking it up and making sure it still works everywhere (and there might be some numerical noise as it handles polynomial multiplication in a more numerically stable way).",
    "created_at": "2008-10-27T16:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4168#issuecomment-30192",
    "user": "https://github.com/robertwb"
}
```

Well, this is pretty low-hanging fruit, but I've just got too many things higher on my priority list (sage and otherwise). 

If no one else gets around to this, eventually I will. The code is there, it's just a matter of hooking it up and making sure it still works everywhere (and there might be some numerical noise as it handles polynomial multiplication in a more numerically stable way).



---

archive/issue_comments_030193.json:
```json
{
    "body": "Attachment [4168-RRx.patch](tarball://root/attachments/some-uuid/ticket4168/4168-RRx.patch) by @robertwb created at 2008-10-31 17:54:54\n\nOK, I did this yesterday during bug days. Ran all tests and fixed a bit of numerical noise this morning.",
    "created_at": "2008-10-31T17:54:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4168#issuecomment-30193",
    "user": "https://github.com/robertwb"
}
```

Attachment [4168-RRx.patch](tarball://root/attachments/some-uuid/ticket4168/4168-RRx.patch) by @robertwb created at 2008-10-31 17:54:54

OK, I did this yesterday during bug days. Ran all tests and fixed a bit of numerical noise this morning.



---

archive/issue_comments_030194.json:
```json
{
    "body": "Looks good and passes tests.",
    "created_at": "2008-11-21T15:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4168#issuecomment-30194",
    "user": "https://github.com/mwhansen"
}
```

Looks good and passes tests.



---

archive/issue_events_004405.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-21T20:19:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4168",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4168#event-4405"
}
```



---

archive/issue_comments_030195.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T20:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4168#issuecomment-30195",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030196.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T20:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4168#issuecomment-30196",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.alpha0
