# Issue 9060: break symmetries in subgraph search

archive/issues_009060.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nUseless, when looking for a triangle, to test both abc, bca, and cab. The same is true when looking for Cycles, for complete graphs, etc...\n\nThere may be a way to generally deal with those symmetries to improve the speed of subgraph search.\n\nIf not, it is still possible to manually improve it for cycles, complete graphs, and other \"common\" graphs.\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9060\n\n",
    "created_at": "2010-05-26T22:37:24Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "break symmetries in subgraph search",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9060",
    "user": "@nathanncohen"
}
```
Assignee: jason, ncohen, rlm

Useless, when looking for a triangle, to test both abc, bca, and cab. The same is true when looking for Cycles, for complete graphs, etc...

There may be a way to generally deal with those symmetries to improve the speed of subgraph search.

If not, it is still possible to manually improve it for cycles, complete graphs, and other "common" graphs.

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9060





---

archive/issue_comments_084060.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:01:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9060",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9060#issuecomment-84060",
    "user": "@nathanncohen"
}
```

Changing status from new to needs_work.
