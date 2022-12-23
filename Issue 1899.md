# Issue 1899: Calling graphs with a matrix and loops=True blows up

archive/issues_001899.json:
```json
{
    "body": "Assignee: rlm\n\n\n```\nsage: Graph(matrix([[1,2],[3,4]]),loops=True)\n---------------------------------------------------------------------------\n<type 'exceptions.NameError'>             Traceback (most recent call last)\n\n/home/jason/download/sage-2.10-Linux-i686-Linux/devel/sage-main/sage/combinat/<ipython console> in <module>()\n\n/home/was/build/sage-2.10/local/lib/python2.5/site-packages/sage/graphs/graph.py in __init__(self, data, pos, loops, format, boundary, weighted, **kwds)\n\n<type 'exceptions.NameError'>: global name 'multiedges' is not defined\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1899\n\n",
    "created_at": "2008-01-23T22:19:40Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Calling graphs with a matrix and loops=True blows up",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1899",
    "user": "jason"
}
```
Assignee: rlm


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

archive/issue_comments_012017.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-23T23:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1899#issuecomment-12017",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_012018.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-01-24T04:01:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1899#issuecomment-12018",
    "user": "jason"
}
```

Looks good to me.



---

archive/issue_comments_012019.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-24T04:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1899#issuecomment-12019",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012020.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-24T04:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1899#issuecomment-12020",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
