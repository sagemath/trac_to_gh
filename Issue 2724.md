# Issue 2724: Graph.show3D should have default aspect ratio of [1,1,1]

archive/issues_002724.json:
```json
{
    "body": "Assignee: rlm\n\nIn the following:\n\n\n```\nsage: g=graphs.PetersenGraph()\nsage: g.show3d()\n```\n\n\nthe edges look messed up (some are darker and some are lighter and it changes as you rotate the graph).  Putting aspect_ratio=[1,1,1] fixes the problem:\n\n\n```\nsage: g=graphs.PetersenGraph()\nsage: g.show3d(aspect_ratio=[1,1,1])\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2724\n\n",
    "created_at": "2008-03-29T19:37:19Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Graph.show3D should have default aspect ratio of [1,1,1]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2724",
    "user": "jason"
}
```
Assignee: rlm

In the following:


```
sage: g=graphs.PetersenGraph()
sage: g.show3d()
```


the edges look messed up (some are darker and some are lighter and it changes as you rotate the graph).  Putting aspect_ratio=[1,1,1] fixes the problem:


```
sage: g=graphs.PetersenGraph()
sage: g.show3d(aspect_ratio=[1,1,1])
```



Issue created by migration from https://trac.sagemath.org/ticket/2724





---

archive/issue_comments_018771.json:
```json
{
    "body": "Might this be a duplicate of #2477, i.e. show3d vs. plot3d? This also has some overlap with #2100.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-29T19:50:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2724#issuecomment-18771",
    "user": "mabshoff"
}
```

Might this be a duplicate of #2477, i.e. show3d vs. plot3d? This also has some overlap with #2100.

Cheers,

Michael



---

archive/issue_comments_018772.json:
```json
{
    "body": "This is an exact duplicate of #2477. Make sure to check before posting tickets!",
    "created_at": "2008-03-29T20:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2724#issuecomment-18772",
    "user": "rlm"
}
```

This is an exact duplicate of #2477. Make sure to check before posting tickets!



---

archive/issue_comments_018773.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-29T20:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2724#issuecomment-18773",
    "user": "rlm"
}
```

Resolution: duplicate



---

archive/issue_comments_018774.json:
```json
{
    "body": "You're right, it's a dup of #2477.  I tried searching for a ticket, but didn't find that one (I was looking for show3d).\n\nI've posted a review for that patch.",
    "created_at": "2008-03-29T20:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2724",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2724#issuecomment-18774",
    "user": "jason"
}
```

You're right, it's a dup of #2477.  I tried searching for a ticket, but didn't find that one (I was looking for show3d).

I've posted a review for that patch.
