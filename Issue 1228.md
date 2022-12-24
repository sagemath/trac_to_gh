# Issue 1228: 2.8.13.rc1: sage/rings/arith.py doctest failure

archive/issues_001228.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe get:\n\n```\nFile \"arith.py\", line 2393:\n     sage: continued_fraction_list(sqrt(4/19))\nExpected:\n     [0, 2, 5, 1, 1, 2, 1, 16, 1, 2, 1, 1, 5, 4, 5, 1, 1, 2, 1, 18]\nGot:\n     [0, 2, 5, 1, 1, 2, 1, 16, 1, 2, 1, 1, 5, 4, 5, 1, 1, 2, 1, 15, 2]\n```\n\nThis is fallout from #1196:\n\n```\nWith 2.8.12 we get:\n\nsage: n(sqrt(4/19))\n0.458831467741123\n\nWith 2.8.13.rc1 we get:\n\nsage: n(sqrt(4/19))\n0.458831467741124\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1228\n\n",
    "created_at": "2007-11-20T23:03:57Z",
    "labels": [
        "doctest coverage",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.13",
    "title": "2.8.13.rc1: sage/rings/arith.py doctest failure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1228",
    "user": "mabshoff"
}
```
Assignee: mabshoff

We get:

```
File "arith.py", line 2393:
     sage: continued_fraction_list(sqrt(4/19))
Expected:
     [0, 2, 5, 1, 1, 2, 1, 16, 1, 2, 1, 1, 5, 4, 5, 1, 1, 2, 1, 18]
Got:
     [0, 2, 5, 1, 1, 2, 1, 16, 1, 2, 1, 1, 5, 4, 5, 1, 1, 2, 1, 15, 2]
```

This is fallout from #1196:

```
With 2.8.12 we get:

sage: n(sqrt(4/19))
0.458831467741123

With 2.8.13.rc1 we get:

sage: n(sqrt(4/19))
0.458831467741124
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1228





---

archive/issue_comments_007640.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-20T23:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1228#issuecomment-7640",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007641.json:
```json
{
    "body": "\n```\nRegarding #1228 change the doctest to the new answer.\nIt's actually much better.\n```\n",
    "created_at": "2007-11-21T12:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1228#issuecomment-7641",
    "user": "@williamstein"
}
```


```
Regarding #1228 change the doctest to the new answer.
It's actually much better.
```




---

archive/issue_comments_007642.json:
```json
{
    "body": "Merged in 2.8.13.rc2.\n\nFixed the doctest directly :)",
    "created_at": "2007-11-21T13:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1228#issuecomment-7642",
    "user": "mabshoff"
}
```

Merged in 2.8.13.rc2.

Fixed the doctest directly :)



---

archive/issue_comments_007643.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-11-21T13:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1228#issuecomment-7643",
    "user": "mabshoff"
}
```

Resolution: fixed
