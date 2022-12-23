# Issue 8913: S.cayley_graph(side = "twosided") returns broken labels

archive/issues_008913.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  sage-combinat rbeezer\n\nThis patch reinstates appropriate labeling of the edges for two sided cayley graphs::\n\n```\n   sage: S = FiniteSemigroups().example(alphabet=('a','b'))\n   sage: g = S.cayley_graph(side=\"twosided\")\n   sage: g.edges()\n   [('a', 'a', (0, 'left')), ('a', 'a', (0, 'right')), ('a', 'ab', (1, 'right')), ('a', 'ba', (1, 'left')), ('ab', 'ab', (0, 'left')), ('ab', 'ab', (0, 'right')), ('ab', 'ab', (1, 'right')), ('ab', 'ba', (1, 'left')), ('b', 'ab', (0, 'left')), ('b', 'b', (1, 'left')), ('b', 'b', (1, 'right')), ('b', 'ba', (0, 'right')), ('ba', 'ab', (0, 'left')), ('ba', 'ba', (0, 'right')), ('ba', 'ba', (1, 'left')), ('ba', 'ba', (1, 'right'))]\n```\n\n\nThis was inadvertently broken by #8044 which discarded the `left` / `right` info.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8913\n\n",
    "created_at": "2010-05-07T15:10:43Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "S.cayley_graph(side = \"twosided\") returns broken labels",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8913",
    "user": "nthiery"
}
```
Assignee: nthiery

CC:  sage-combinat rbeezer

This patch reinstates appropriate labeling of the edges for two sided cayley graphs::

```
   sage: S = FiniteSemigroups().example(alphabet=('a','b'))
   sage: g = S.cayley_graph(side="twosided")
   sage: g.edges()
   [('a', 'a', (0, 'left')), ('a', 'a', (0, 'right')), ('a', 'ab', (1, 'right')), ('a', 'ba', (1, 'left')), ('ab', 'ab', (0, 'left')), ('ab', 'ab', (0, 'right')), ('ab', 'ab', (1, 'right')), ('ab', 'ba', (1, 'left')), ('b', 'ab', (0, 'left')), ('b', 'b', (1, 'left')), ('b', 'b', (1, 'right')), ('b', 'ba', (0, 'right')), ('ba', 'ab', (0, 'left')), ('ba', 'ba', (0, 'right')), ('ba', 'ba', (1, 'left')), ('ba', 'ba', (1, 'right'))]
```


This was inadvertently broken by #8044 which discarded the `left` / `right` info.

Issue created by migration from https://trac.sagemath.org/ticket/8913





---

archive/issue_comments_082103.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-18T21:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-82103",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082104.json:
```json
{
    "body": "Changing keywords from \"\" to \"cayley graph\".",
    "created_at": "2010-05-18T21:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-82104",
    "user": "nthiery"
}
```

Changing keywords from "" to "cayley graph".



---

archive/issue_comments_082105.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-18T21:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-82105",
    "user": "nthiery"
}
```

Attachment



---

archive/issue_comments_082106.json:
```json
{
    "body": "Looks good.  Running tests now.",
    "created_at": "2010-05-19T03:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-82106",
    "user": "rbeezer"
}
```

Looks good.  Running tests now.



---

archive/issue_comments_082107.json:
```json
{
    "body": "Looks good (including the addition of a new doctest for this situation).\n\nApplies, builds, whole library passes tests, docs are fine, all on 4.4.2.rc0.\n\nPositive review.",
    "created_at": "2010-05-19T05:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-82107",
    "user": "rbeezer"
}
```

Looks good (including the addition of a new doctest for this situation).

Applies, builds, whole library passes tests, docs are fine, all on 4.4.2.rc0.

Positive review.



---

archive/issue_comments_082108.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-19T05:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-82108",
    "user": "rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082109.json:
```json
{
    "body": "Replying to [comment:4 rbeezer]:\n> Looks good (including the addition of a new doctest for this situation).\n> \n> Applies, builds, whole library passes tests, docs are fine, all on 4.4.2.rc0.\n> \n> Positive review.\n\nThanks Rob, that was quick!",
    "created_at": "2010-05-19T06:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-82109",
    "user": "nthiery"
}
```

Replying to [comment:4 rbeezer]:
> Looks good (including the addition of a new doctest for this situation).
> 
> Applies, builds, whole library passes tests, docs are fine, all on 4.4.2.rc0.
> 
> Positive review.

Thanks Rob, that was quick!



---

archive/issue_comments_082110.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-82110",
    "user": "mhansen"
}
```

Resolution: fixed
