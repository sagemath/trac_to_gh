# Issue 1219: bug in eigenspaces over CC

archive/issues_001219.json:
```json
{
    "body": "Assignee: @williamstein\n\nSomething funny is going on:\n\n\n```\nsage: MS = MatrixSpace(CC, 2, 2)\nsage: A = MS([[1,5],[3,-1]])\nsage: A.eigenspaces()\n\n[\n(4.00000000000000, [\n(1.00000000000000, 1.00000000000000)\n]),\n(-4.00000000000000, [\n\n])\n]\nsage: A.eigenspaces()[0]\n\n(4.00000000000000, [\n(1.00000000000000, 1.00000000000000)\n])\nsage: A.eigenspaces()[1]\n\n(-4.00000000000000, [\n\n])\nsage: MS = MatrixSpace(QQ, 2, 2)\nsage: A = MS([[1,5],[3,-1]])\nsage: A.eigenspaces()\n\n[\n(4, [\n(1, 1)\n]),\n(-4, [\n(1, -5/3)\n])\n]\n```\n\nI find it strange that eigenspaces works for QQ\nbut not for the larger field CC.\n\nWillam: The issue above is undoubtedly that\nthere is no specialized implementation of matrices over CC.\nIt's just completely generic code.  So some generic echelon\nis going wrong.  \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1219\n\n",
    "created_at": "2007-11-20T19:56:40Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in eigenspaces over CC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1219",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: @williamstein

Something funny is going on:


```
sage: MS = MatrixSpace(CC, 2, 2)
sage: A = MS([[1,5],[3,-1]])
sage: A.eigenspaces()

[
(4.00000000000000, [
(1.00000000000000, 1.00000000000000)
]),
(-4.00000000000000, [

])
]
sage: A.eigenspaces()[0]

(4.00000000000000, [
(1.00000000000000, 1.00000000000000)
])
sage: A.eigenspaces()[1]

(-4.00000000000000, [

])
sage: MS = MatrixSpace(QQ, 2, 2)
sage: A = MS([[1,5],[3,-1]])
sage: A.eigenspaces()

[
(4, [
(1, 1)
]),
(-4, [
(1, -5/3)
])
]
```

I find it strange that eigenspaces works for QQ
but not for the larger field CC.

Willam: The issue above is undoubtedly that
there is no specialized implementation of matrices over CC.
It's just completely generic code.  So some generic echelon
is going wrong.  


Issue created by migration from https://trac.sagemath.org/ticket/1219





---

archive/issue_comments_007547.json:
```json
{
    "body": "#1706 and #2050 are essentially the same.",
    "created_at": "2008-02-17T06:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1219#issuecomment-7547",
    "user": "https://github.com/ncalexan"
}
```

#1706 and #2050 are essentially the same.



---

archive/issue_comments_007548.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-02-17T06:52:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1219#issuecomment-7548",
    "user": "https://github.com/ncalexan"
}
```

Resolution: duplicate
