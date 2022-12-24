# Issue 335: directory not empty issue

archive/issues_000335.json:
```json
{
    "body": "Assignee: @williamstein\n\nFrom Kate Minola:\n\n\n```\nAfter building sage-2.4 on my pentium4-pc-linux machine,\nwhen I do 'make test', I get\n\n[stuff deleted]\nsage -t devel/sage-main/sage/geometry/lattice_polytope.py\nsage -t  devel/sage-main/sage/geometry/lattice_polytope.py  [Errno 39]\nDirectory not empty: '/home/kate/.sage//tmp/31372/'\n\n        [3.2 s]\n[stuff deleted]\n\nThe code in the function 'all_cached_data(polytopes)' in lattice_polytope.py\nseems to be causing this.\n\nEven though at the end, 'make test' says all the tests passed, this\nlooks like a problem.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/335\n\n",
    "created_at": "2007-03-27T14:28:48Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "directory not empty issue",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/335",
    "user": "@williamstein"
}
```
Assignee: @williamstein

From Kate Minola:


```
After building sage-2.4 on my pentium4-pc-linux machine,
when I do 'make test', I get

[stuff deleted]
sage -t devel/sage-main/sage/geometry/lattice_polytope.py
sage -t  devel/sage-main/sage/geometry/lattice_polytope.py  [Errno 39]
Directory not empty: '/home/kate/.sage//tmp/31372/'

        [3.2 s]
[stuff deleted]

The code in the function 'all_cached_data(polytopes)' in lattice_polytope.py
seems to be causing this.

Even though at the end, 'make test' says all the tests passed, this
looks like a problem.
```


Issue created by migration from https://trac.sagemath.org/ticket/335





---

archive/issue_comments_001647.json:
```json
{
    "body": "Mmmh, didn't this get fixed? Something with NFS mounts (or some other network file system via automounter)\n\nCheers,\n\nMichael",
    "created_at": "2007-08-24T23:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/335#issuecomment-1647",
    "user": "mabshoff"
}
```

Mmmh, didn't this get fixed? Something with NFS mounts (or some other network file system via automounter)

Cheers,

Michael



---

archive/issue_comments_001648.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-30T00:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/335#issuecomment-1648",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_001649.json:
```json
{
    "body": "This has long since been fixed.",
    "created_at": "2007-08-30T00:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/335",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/335#issuecomment-1649",
    "user": "@williamstein"
}
```

This has long since been fixed.
