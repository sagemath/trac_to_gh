# Issue 979: printing error with small reals

archive/issues_000979.json:
```json
{
    "body": "Assignee: mhansen\n\n\n```\nsage: a = .00000000000000000000001;a\n0.000000000000000000000010000000000000000000000\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/979\n\n",
    "created_at": "2007-10-24T03:49:28Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "printing error with small reals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/979",
    "user": "mhansen"
}
```
Assignee: mhansen


```
sage: a = .00000000000000000000001;a
0.000000000000000000000010000000000000000000000
```


Issue created by migration from https://trac.sagemath.org/ticket/979





---

archive/issue_comments_005970.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-24T05:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/979#issuecomment-5970",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005971.json:
```json
{
    "body": "Patch for this will be in the big patch for #962.",
    "created_at": "2007-10-24T05:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/979#issuecomment-5971",
    "user": "mhansen"
}
```

Patch for this will be in the big patch for #962.



---

archive/issue_comments_005972.json:
```json
{
    "body": "I believe this has already been taken care of.\n\nIn 2.8.15, we have\n\n\n```\nsage: a = .00000000000000000000001;a\n1.00000000000000e-23\n```\n",
    "created_at": "2007-12-06T21:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/979#issuecomment-5972",
    "user": "mhansen"
}
```

I believe this has already been taken care of.

In 2.8.15, we have


```
sage: a = .00000000000000000000001;a
1.00000000000000e-23
```




---

archive/issue_comments_005973.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-06T21:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/979#issuecomment-5973",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_005974.json:
```json
{
    "body": "Merged in 2.8.15.",
    "created_at": "2007-12-06T21:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/979",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/979#issuecomment-5974",
    "user": "mabshoff"
}
```

Merged in 2.8.15.
