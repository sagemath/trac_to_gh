# Issue 2255: matrix transpose does not maintain subdivision information

archive/issues_002255.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  ncalexander@gmail.com\n\nKeywords: matrix transpose subdivision subdivide\n\n\n```\nsage: tau = CC(I)*matrix(2, 2, [2, 0, 0, 2])\nsage: B = block_matrix([tau, tau, tau, tau], 2, 2)\nsage: B\n\n[2.00000000000000*I                  0|2.00000000000000*I                  0]\n[                 0 2.00000000000000*I|                 0 2.00000000000000*I]\n[-------------------------------------+-------------------------------------]\n[2.00000000000000*I                  0|2.00000000000000*I                  0]\n[                 0 2.00000000000000*I|                 0 2.00000000000000*I]\nsage: B.transpose()\n\n[2.00000000000000*I                  0 2.00000000000000*I                  0]\n[                 0 2.00000000000000*I                  0 2.00000000000000*I]\n[2.00000000000000*I                  0 2.00000000000000*I                  0]\n[                 0 2.00000000000000*I                  0 2.00000000000000*I]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2255\n\n",
    "created_at": "2008-02-22T05:43:57Z",
    "labels": [
        "linear algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "matrix transpose does not maintain subdivision information",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2255",
    "user": "@ncalexan"
}
```
Assignee: @williamstein

CC:  ncalexander@gmail.com

Keywords: matrix transpose subdivision subdivide


```
sage: tau = CC(I)*matrix(2, 2, [2, 0, 0, 2])
sage: B = block_matrix([tau, tau, tau, tau], 2, 2)
sage: B

[2.00000000000000*I                  0|2.00000000000000*I                  0]
[                 0 2.00000000000000*I|                 0 2.00000000000000*I]
[-------------------------------------+-------------------------------------]
[2.00000000000000*I                  0|2.00000000000000*I                  0]
[                 0 2.00000000000000*I|                 0 2.00000000000000*I]
sage: B.transpose()

[2.00000000000000*I                  0 2.00000000000000*I                  0]
[                 0 2.00000000000000*I                  0 2.00000000000000*I]
[2.00000000000000*I                  0 2.00000000000000*I                  0]
[                 0 2.00000000000000*I                  0 2.00000000000000*I]
```


Issue created by migration from https://trac.sagemath.org/ticket/2255





---

archive/issue_comments_014936.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-03-06T08:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2255#issuecomment-14936",
    "user": "@ncalexan"
}
```

Resolution: duplicate



---

archive/issue_comments_014937.json:
```json
{
    "body": "This is essentially a duplicate of #2142.",
    "created_at": "2008-03-06T08:36:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2255#issuecomment-14937",
    "user": "@ncalexan"
}
```

This is essentially a duplicate of #2142.
