# Issue 4573: Permutation not callable, but PermutationGroupElement is.

archive/issues_004573.json:
```json
{
    "body": "Assignee: saliola\n\nCC:  sage-combinat\n\n\n```\nsage: p = PermutationGroupElement([2, 1, 4, 5, 3])\nsage: p(1)\n2\nsage: q = Permutation([2, 1, 4, 5, 3])\nsage: q(1)\n...\nTypeError: 'Permutation_class' object is not callable\n```\n\n\nThis causes me some confusion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4573\n\n",
    "created_at": "2008-11-20T22:15:08Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Permutation not callable, but PermutationGroupElement is.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4573",
    "user": "saliola"
}
```
Assignee: saliola

CC:  sage-combinat


```
sage: p = PermutationGroupElement([2, 1, 4, 5, 3])
sage: p(1)
2
sage: q = Permutation([2, 1, 4, 5, 3])
sage: q(1)
...
TypeError: 'Permutation_class' object is not callable
```


This causes me some confusion.

Issue created by migration from https://trac.sagemath.org/ticket/4573





---

archive/issue_comments_034267.json:
```json
{
    "body": "Attachment\n\n(against 3.2.rc2)",
    "created_at": "2008-11-20T22:16:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4573#issuecomment-34267",
    "user": "saliola"
}
```

Attachment

(against 3.2.rc2)



---

archive/issue_comments_034268.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-11-21T14:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4573#issuecomment-34268",
    "user": "mhansen"
}
```

Looks good.



---

archive/issue_comments_034269.json:
```json
{
    "body": "Merged in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T20:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4573#issuecomment-34269",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.alpha0



---

archive/issue_comments_034270.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T20:23:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4573",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4573#issuecomment-34270",
    "user": "mabshoff"
}
```

Resolution: fixed
