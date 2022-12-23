# Issue 8779: Categories for polynomial rings

archive/issues_008779.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat\n\nKeywords: polynomial rings, categories\n\n\n```\nsage: QQ[x].categories()\n[Category of commutative rings, Category of rings, ...]\n```\n\n\nThis list should at least contain `EuclideanDomains()` and `GradedAlgebrasWithBasis(QQ)`. Maybe even `GradedHopfAlgebrasWithBasis(QQ)`.\n\nAt that occasion, the various accessors (term, ...) here and in ModulesWithBasis should be made consistent.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8779\n\n",
    "created_at": "2010-04-27T06:19:21Z",
    "labels": [
        "categories",
        "major",
        "enhancement"
    ],
    "title": "Categories for polynomial rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8779",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat

Keywords: polynomial rings, categories


```
sage: QQ[x].categories()
[Category of commutative rings, Category of rings, ...]
```


This list should at least contain `EuclideanDomains()` and `GradedAlgebrasWithBasis(QQ)`. Maybe even `GradedHopfAlgebrasWithBasis(QQ)`.

At that occasion, the various accessors (term, ...) here and in ModulesWithBasis should be made consistent.

Issue created by migration from https://trac.sagemath.org/ticket/8779





---

archive/issue_comments_080367.json:
```json
{
    "body": "Has this been superceded by #9944?",
    "created_at": "2014-11-14T10:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8779#issuecomment-80367",
    "user": "jpflori"
}
```

Has this been superceded by #9944?



---

archive/issue_comments_080368.json:
```json
{
    "body": "Partially, but polynomial rings are not yet considered to be graded (we already have this implemented because of the `degree` method).",
    "created_at": "2014-11-14T15:52:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8779",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8779#issuecomment-80368",
    "user": "tscrim"
}
```

Partially, but polynomial rings are not yet considered to be graded (we already have this implemented because of the `degree` method).
