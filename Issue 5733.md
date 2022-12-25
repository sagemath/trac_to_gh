# Issue 5733: bug in 3d plotting of graphs

archive/issues_005733.json:
```json
{
    "body": "Assignee: @rlmill\n\n\n```\nsage: G=Graph({'a':['a','b','b','b','e'],'b':['c','d','e'],'c':\nsage: ['c','d','d','d'],'d':['e']})\nsage: G.show3d()\nTraceback (most recent call last):\n...\nZeroDivisionError: float division\n```\n\n\nReported by alec`@`mihailovs\n\nIssue created by migration from https://trac.sagemath.org/ticket/5733\n\n",
    "created_at": "2009-04-10T14:19:31Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "bug in 3d plotting of graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5733",
    "user": "https://github.com/williamstein"
}
```
Assignee: @rlmill


```
sage: G=Graph({'a':['a','b','b','b','e'],'b':['c','d','e'],'c':
sage: ['c','d','d','d'],'d':['e']})
sage: G.show3d()
Traceback (most recent call last):
...
ZeroDivisionError: float division
```


Reported by alec`@`mihailovs

Issue created by migration from https://trac.sagemath.org/ticket/5733





---

archive/issue_comments_044714.json:
```json
{
    "body": "Apparently show3d() chokes on loops (that's the error: I think it's trying to make a cylinder (edge) with length 0).  Also, show3d doesn't show multiple edges.",
    "created_at": "2009-04-10T14:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5733#issuecomment-44714",
    "user": "https://github.com/jasongrout"
}
```

Apparently show3d() chokes on loops (that's the error: I think it's trying to make a cylinder (edge) with length 0).  Also, show3d doesn't show multiple edges.



---

archive/issue_comments_044715.json:
```json
{
    "body": "This needs to be implemented, but until then it needs to fail more gracefully. Thus the proposed patch. If implementing this isn't a ticket yet, it probably should be.",
    "created_at": "2009-04-10T15:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5733#issuecomment-44715",
    "user": "https://github.com/rlmill"
}
```

This needs to be implemented, but until then it needs to fail more gracefully. Thus the proposed patch. If implementing this isn't a ticket yet, it probably should be.



---

archive/issue_comments_044716.json:
```json
{
    "body": "Attachment [trac_5733.patch](tarball://root/attachments/some-uuid/ticket5733/trac_5733.patch) by @rlmill created at 2009-04-10 15:32:37",
    "created_at": "2009-04-10T15:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5733#issuecomment-44716",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_5733.patch](tarball://root/attachments/some-uuid/ticket5733/trac_5733.patch) by @rlmill created at 2009-04-10 15:32:37



---

archive/issue_events_013458.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-13T06:23:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5733#event-13458"
}
```



---

archive/issue_comments_044717.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T06:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5733#issuecomment-44717",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_events_013459.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-13T06:23:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5733#event-13459"
}
```



---

archive/issue_comments_044718.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T06:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5733#issuecomment-44718",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
