# Issue 1706: Eigenspaces bug?

archive/issues_001706.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  ncalexander@gmail.com\n\nShouldn't the sum of the dimensions be 2?\n\n```\nsage: M = Matrix(CC, [[1,0],[0,1]])\nsage: M\n\n[1.00000000000000                0]\n[               0 1.00000000000000]\nsage: M.eigenspaces()\n\n[\n(1.00000000000000, [\n(1.00000000000000, 0),\n(0, 1.00000000000000)\n]),\n(1.00000000000000, [\n(1.00000000000000, 0),\n(0, 1.00000000000000)\n])\n]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1706\n\n",
    "created_at": "2008-01-07T05:11:17Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Eigenspaces bug?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1706",
    "user": "https://github.com/rlmill"
}
```
Assignee: @williamstein

CC:  ncalexander@gmail.com

Shouldn't the sum of the dimensions be 2?

```
sage: M = Matrix(CC, [[1,0],[0,1]])
sage: M

[1.00000000000000                0]
[               0 1.00000000000000]
sage: M.eigenspaces()

[
(1.00000000000000, [
(1.00000000000000, 0),
(0, 1.00000000000000)
]),
(1.00000000000000, [
(1.00000000000000, 0),
(0, 1.00000000000000)
])
]
```

Issue created by migration from https://trac.sagemath.org/ticket/1706





---

archive/issue_comments_010777.json:
```json
{
    "body": "The problem is that fcp (factored char poly) returns (x-1)*(x-1), as opposed to (x-1)^2. (That is, it says that there are two distinct factors, each of which happens to be the same.) However, the eigenspaces algorithm implicitly assumes that the terms in self.fcp() are distinct.",
    "created_at": "2008-01-07T05:15:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1706#issuecomment-10777",
    "user": "https://github.com/craigcitro"
}
```

The problem is that fcp (factored char poly) returns (x-1)*(x-1), as opposed to (x-1)^2. (That is, it says that there are two distinct factors, each of which happens to be the same.) However, the eigenspaces algorithm implicitly assumes that the terms in self.fcp() are distinct.



---

archive/issue_events_004163.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2008-01-18T16:20:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1706",
    "milestone": "sage-2.10.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1706#event-4163"
}
```



---

archive/issue_comments_010778.json:
```json
{
    "body": "More data from Sage 2.9.3 which might shed some light on the problem:\n\n```\nsage: M=Matrix(ZZ,[[1,0],[0,1]])\nsage: M.fcp()\n(x - 1)^2\nsage: M=Matrix(QQ,[[1,0],[0,1]])\nsage: M.fcp()\n(x - 1)^2\nsage: M=Matrix(RR,[[1,0],[0,1]])\nsage: M.fcp()\n(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)\nsage: M=Matrix(CC,[[1,0],[0,1]])\nsage: M.fcp()\n(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)\n\n```\n\nand \n\n```\nsage: R.<x>=RR[x]\nsage: ((x-1)^2).factor()\n(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)\nsage: a=((x-1)^2).factor()\nsage: a\n(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)\nsage: a[0]\n(1.00000000000000*x - 1.00000000000000, 1)\nsage: a[0]==a[1]\nTrue\nsage: var('x')\nx\nsage: Q.<x>=QQ[x]\nsage: ((x-1)^2).factor()\n(x - 1)^2\n```",
    "created_at": "2008-01-19T06:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1706#issuecomment-10778",
    "user": "https://github.com/jasongrout"
}
```

More data from Sage 2.9.3 which might shed some light on the problem:

```
sage: M=Matrix(ZZ,[[1,0],[0,1]])
sage: M.fcp()
(x - 1)^2
sage: M=Matrix(QQ,[[1,0],[0,1]])
sage: M.fcp()
(x - 1)^2
sage: M=Matrix(RR,[[1,0],[0,1]])
sage: M.fcp()
(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)
sage: M=Matrix(CC,[[1,0],[0,1]])
sage: M.fcp()
(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)

```

and 

```
sage: R.<x>=RR[x]
sage: ((x-1)^2).factor()
(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)
sage: a=((x-1)^2).factor()
sage: a
(1.00000000000000*x - 1.00000000000000) * (1.00000000000000*x - 1.00000000000000)
sage: a[0]
(1.00000000000000*x - 1.00000000000000, 1)
sage: a[0]==a[1]
True
sage: var('x')
x
sage: Q.<x>=QQ[x]
sage: ((x-1)^2).factor()
(x - 1)^2
```



---

archive/issue_comments_010779.json:
```json
{
    "body": "See #2050 for a related ticket, which would likely remove the functionality that is broken above.",
    "created_at": "2008-02-05T05:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1706#issuecomment-10779",
    "user": "https://github.com/williamstein"
}
```

See #2050 for a related ticket, which would likely remove the functionality that is broken above.



---

archive/issue_comments_010780.json:
```json
{
    "body": "If #2050 is applied, this will be fixed (the functionality will by default raise NotImplemented).  Patch is attached to #2050.",
    "created_at": "2008-02-17T00:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1706#issuecomment-10780",
    "user": "https://github.com/ncalexan"
}
```

If #2050 is applied, this will be fixed (the functionality will by default raise NotImplemented).  Patch is attached to #2050.



---

archive/issue_comments_010781.json:
```json
{
    "body": "I can confirm that this is taken care of after #2050 is applied.",
    "created_at": "2008-02-27T23:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1706#issuecomment-10781",
    "user": "https://github.com/mwhansen"
}
```

I can confirm that this is taken care of after #2050 is applied.



---

archive/issue_comments_010782.json:
```json
{
    "body": "The patch for #2050 was merged in 2.10.3.rc0 .",
    "created_at": "2008-02-28T01:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1706#issuecomment-10782",
    "user": "https://github.com/mwhansen"
}
```

The patch for #2050 was merged in 2.10.3.rc0 .



---

archive/issue_events_004164.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-02-28T01:13:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1706",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1706#event-4164"
}
```



---

archive/issue_comments_010783.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T01:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1706#issuecomment-10783",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
