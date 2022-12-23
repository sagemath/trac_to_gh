# Issue 7396: Disjoint unions of enumerated sets.

archive/issues_007396.json:
```json
{
    "body": "Assignee: hivert\n\nCC:  sage-combinat\n\nKeywords: Disjoint union, enumerated sets\n\nThe patch implement the disjoint union of a family of enumerated sets. It allows in particular to deal with infinite unions such as in \n\n```\nsage: DisjointUnionEnumeratedSets(\n...       Family(NonNegativeIntegers(), Permutations))\nDisjoint union of Lazy family (Permutations(i))_{i in Non negative integers}\n```\n\n\nFlorent\n\nIssue created by migration from https://trac.sagemath.org/ticket/7396\n\n",
    "created_at": "2009-11-05T15:46:33Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Disjoint unions of enumerated sets.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7396",
    "user": "hivert"
}
```
Assignee: hivert

CC:  sage-combinat

Keywords: Disjoint union, enumerated sets

The patch implement the disjoint union of a family of enumerated sets. It allows in particular to deal with infinite unions such as in 

```
sage: DisjointUnionEnumeratedSets(
...       Family(NonNegativeIntegers(), Permutations))
Disjoint union of Lazy family (Permutations(i))_{i in Non negative integers}
```


Florent

Issue created by migration from https://trac.sagemath.org/ticket/7396





---

archive/issue_comments_062190.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-05T16:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7396#issuecomment-62190",
    "user": "hivert"
}
```

Attachment



---

archive/issue_comments_062191.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-05T16:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7396#issuecomment-62191",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062192.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-05T16:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7396#issuecomment-62192",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062193.json:
```json
{
    "body": "Patch good to go (we polished it together:-))!",
    "created_at": "2009-11-05T16:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7396#issuecomment-62193",
    "user": "nthiery"
}
```

Patch good to go (we polished it together:-))!



---

archive/issue_comments_062194.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T16:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7396#issuecomment-62194",
    "user": "mhansen"
}
```

Resolution: fixed
