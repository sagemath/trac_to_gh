# Issue 4252: Arrangements / PermutationsNK iterator is broken

archive/issues_004252.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\n\n```\nsage: Arrangements(range(5),4).count()\n116\nsage: len(list(sage.combinat.permutation.PermutationsNK(5,4).iterator()))\n116\nsage: factorial(5)/factorial(5-4)\n120\n```\n\n\nThey should all be 120. This also doesn't work for the pairs: (4,4), (5, 4), (5, 5), (6, 4), (6, 5), (6, 6), ....\n\nIssue created by migration from https://trac.sagemath.org/ticket/4252\n\n",
    "created_at": "2008-10-07T19:40:10Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Arrangements / PermutationsNK iterator is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4252",
    "user": "@saliola"
}
```
Assignee: @mwhansen

CC:  sage-combinat


```
sage: Arrangements(range(5),4).count()
116
sage: len(list(sage.combinat.permutation.PermutationsNK(5,4).iterator()))
116
sage: factorial(5)/factorial(5-4)
120
```


They should all be 120. This also doesn't work for the pairs: (4,4), (5, 4), (5, 5), (6, 4), (6, 5), (6, 6), ....

Issue created by migration from https://trac.sagemath.org/ticket/4252





---

archive/issue_comments_030935.json:
```json
{
    "body": "This is a duplicate of #4213 which has been fixed in 3.1.3.",
    "created_at": "2008-10-07T19:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4252#issuecomment-30935",
    "user": "@mwhansen"
}
```

This is a duplicate of #4213 which has been fixed in 3.1.3.



---

archive/issue_comments_030936.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-10-07T19:55:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4252#issuecomment-30936",
    "user": "@mwhansen"
}
```

Resolution: duplicate
