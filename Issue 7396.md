# Issue 7396: Disjoint unions of enumerated sets.

archive/issues_007396.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat\n\nKeywords: Disjoint union, enumerated sets\n\nThe patch implement the disjoint union of a family of enumerated sets. It allows in particular to deal with infinite unions such as in \n\n```\nsage: DisjointUnionEnumeratedSets(\n...       Family(NonNegativeIntegers(), Permutations))\nDisjoint union of Lazy family (Permutations(i))_{i in Non negative integers}\n```\n\n\nFlorent\n\nIssue created by migration from https://trac.sagemath.org/ticket/7396\n\n",
    "created_at": "2009-11-05T15:46:33Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Disjoint unions of enumerated sets.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7396",
    "user": "https://github.com/hivert"
}
```
Assignee: @hivert

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

archive/issue_comments_062075.json:
```json
{
    "body": "Attachment [trac_7396_enumset_unions-fh.patch](tarball://root/attachments/some-uuid/ticket7396/trac_7396_enumset_unions-fh.patch) by @hivert created at 2009-11-05 16:02:21",
    "created_at": "2009-11-05T16:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7396#issuecomment-62075",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7396_enumset_unions-fh.patch](tarball://root/attachments/some-uuid/ticket7396/trac_7396_enumset_unions-fh.patch) by @hivert created at 2009-11-05 16:02:21



---

archive/issue_comments_062076.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-05T16:26:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7396#issuecomment-62076",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062077.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-05T16:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7396#issuecomment-62077",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062078.json:
```json
{
    "body": "Patch good to go (we polished it together:-))!",
    "created_at": "2009-11-05T16:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7396#issuecomment-62078",
    "user": "https://github.com/nthiery"
}
```

Patch good to go (we polished it together:-))!



---

archive/issue_comments_062079.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T16:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7396",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7396#issuecomment-62079",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007619.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-19T16:58:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7396",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7396#event-7619"
}
```
