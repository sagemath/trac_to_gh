# Issue 1899: Calling graphs with a matrix and loops=True blows up

archive/issues_001899.json:
```json
{
    "body": "Assignee: @rlmill\n\n```\nsage: Graph(matrix([[1,2],[3,4]]),loops=True)\n---------------------------------------------------------------------------\n<type 'exceptions.NameError'>             Traceback (most recent call last)\n\n/home/jason/download/sage-2.10-Linux-i686-Linux/devel/sage-main/sage/combinat/<ipython console> in <module>()\n\n/home/was/build/sage-2.10/local/lib/python2.5/site-packages/sage/graphs/graph.py in __init__(self, data, pos, loops, format, boundary, weighted, **kwds)\n\n<type 'exceptions.NameError'>: global name 'multiedges' is not defined\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1899\n\n",
    "created_at": "2008-01-23T22:19:40Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Calling graphs with a matrix and loops=True blows up",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1899",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

```
sage: Graph(matrix([[1,2],[3,4]]),loops=True)
---------------------------------------------------------------------------
<type 'exceptions.NameError'>             Traceback (most recent call last)

/home/jason/download/sage-2.10-Linux-i686-Linux/devel/sage-main/sage/combinat/<ipython console> in <module>()

/home/was/build/sage-2.10/local/lib/python2.5/site-packages/sage/graphs/graph.py in __init__(self, data, pos, loops, format, boundary, weighted, **kwds)

<type 'exceptions.NameError'>: global name 'multiedges' is not defined
```


Issue created by migration from https://trac.sagemath.org/ticket/1899





---

archive/issue_comments_011988.json:
```json
{
    "body": "Attachment [1899.patch](tarball://root/attachments/some-uuid/ticket1899/1899.patch) by @rlmill created at 2008-01-23 23:41:03",
    "created_at": "2008-01-23T23:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1899#issuecomment-11988",
    "user": "https://github.com/rlmill"
}
```

Attachment [1899.patch](tarball://root/attachments/some-uuid/ticket1899/1899.patch) by @rlmill created at 2008-01-23 23:41:03



---

archive/issue_comments_011989.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-01-24T04:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1899#issuecomment-11989",
    "user": "https://github.com/jasongrout"
}
```

Looks good to me.



---

archive/issue_comments_011990.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-24T04:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1899#issuecomment-11990",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011991.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-24T04:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1899#issuecomment-11991",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha2



---

archive/issue_events_004579.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-24T04:04:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1899#event-4579"
}
```
