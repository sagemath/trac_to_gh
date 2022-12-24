# Issue 5733: bug in 3d plotting of graphs

archive/issues_005733.json:
```json
{
    "body": "Assignee: rlm\n\n\n```\nsage: G=Graph({'a':['a','b','b','b','e'],'b':['c','d','e'],'c':\nsage: ['c','d','d','d'],'d':['e']})\nsage: G.show3d()\nTraceback (most recent call last):\n...\nZeroDivisionError: float division\n```\n\n\nReported by alec`@`mihailovs\n\nIssue created by migration from https://trac.sagemath.org/ticket/5733\n\n",
    "created_at": "2009-04-10T14:19:31Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "bug in 3d plotting of graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5733",
    "user": "was"
}
```
Assignee: rlm


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

archive/issue_comments_044799.json:
```json
{
    "body": "Apparently show3d() chokes on loops (that's the error: I think it's trying to make a cylinder (edge) with length 0).  Also, show3d doesn't show multiple edges.",
    "created_at": "2009-04-10T14:38:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5733#issuecomment-44799",
    "user": "jason"
}
```

Apparently show3d() chokes on loops (that's the error: I think it's trying to make a cylinder (edge) with length 0).  Also, show3d doesn't show multiple edges.



---

archive/issue_comments_044800.json:
```json
{
    "body": "This needs to be implemented, but until then it needs to fail more gracefully. Thus the proposed patch. If implementing this isn't a ticket yet, it probably should be.",
    "created_at": "2009-04-10T15:32:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5733#issuecomment-44800",
    "user": "rlm"
}
```

This needs to be implemented, but until then it needs to fail more gracefully. Thus the proposed patch. If implementing this isn't a ticket yet, it probably should be.



---

archive/issue_comments_044801.json:
```json
{
    "body": "Attachment [trac_5733.patch](tarball://root/attachments/some-uuid/ticket5733/trac_5733.patch) by rlm created at 2009-04-10 15:32:37",
    "created_at": "2009-04-10T15:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5733#issuecomment-44801",
    "user": "rlm"
}
```

Attachment [trac_5733.patch](tarball://root/attachments/some-uuid/ticket5733/trac_5733.patch) by rlm created at 2009-04-10 15:32:37



---

archive/issue_comments_044802.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T06:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5733#issuecomment-44802",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_044803.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T06:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5733#issuecomment-44803",
    "user": "mabshoff"
}
```

Resolution: fixed
