# Issue 6117: graph plotting with show ignores keyword 'talk'

archive/issues_006117.json:
```json
{
    "body": "Assignee: ekirkman\n\nCC:  @rlmill\n\nBug pointed out by Fidel Barrera-Cruz.  Entering\n\n```\ng = graphs.PetersenGraph()\ng.show(talk=True)\n```\n\nresults in \n\n```\nTypeError: show() got an unexpected keyword argument 'talk'\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6117\n\n",
    "created_at": "2009-05-21T22:13:58Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "graph plotting with show ignores keyword 'talk'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6117",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```
Assignee: ekirkman

CC:  @rlmill

Bug pointed out by Fidel Barrera-Cruz.  Entering

```
g = graphs.PetersenGraph()
g.show(talk=True)
```

results in 

```
TypeError: show() got an unexpected keyword argument 'talk'
```

Issue created by migration from https://trac.sagemath.org/ticket/6117





---

archive/issue_comments_048788.json:
```json
{
    "body": "Attachment [trac_6117.patch](tarball://root/attachments/some-uuid/ticket6117/trac_6117.patch) by ekirkman created at 2009-05-21 22:34:48",
    "created_at": "2009-05-21T22:34:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6117#issuecomment-48788",
    "user": "https://trac.sagemath.org/admin/accounts/users/ekirkman"
}
```

Attachment [trac_6117.patch](tarball://root/attachments/some-uuid/ticket6117/trac_6117.patch) by ekirkman created at 2009-05-21 22:34:48



---

archive/issue_comments_048789.json:
```json
{
    "body": "I don't like the deletion/dotting out of the doctest in `sage/graphs/graph.py`. Is that really needed?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-22T13:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6117#issuecomment-48789",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I don't like the deletion/dotting out of the doctest in `sage/graphs/graph.py`. Is that really needed?

Cheers,

Michael



---

archive/issue_comments_048790.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-22T13:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6117#issuecomment-48790",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_014403.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-22T13:45:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6117",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6117#event-14403"
}
```



---

archive/issue_comments_048791.json:
```json
{
    "body": "Merged in Sage 4.0.rc1 since it fixes a real bug, but if my comment above could be addressed I wouldn't be too sad ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-22T13:45:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6117",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6117#issuecomment-48791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.rc1 since it fixes a real bug, but if my comment above could be addressed I wouldn't be too sad ;)

Cheers,

Michael
