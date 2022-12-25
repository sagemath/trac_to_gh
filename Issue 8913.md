# Issue 8913: S.cayley_graph(side = "twosided") returns broken labels

archive/issues_008913.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @rbeezer\n\nThis patch reinstates appropriate labeling of the edges for two sided cayley graphs::\n\n```\n   sage: S = FiniteSemigroups().example(alphabet=('a','b'))\n   sage: g = S.cayley_graph(side=\"twosided\")\n   sage: g.edges()\n   [('a', 'a', (0, 'left')), ('a', 'a', (0, 'right')), ('a', 'ab', (1, 'right')), ('a', 'ba', (1, 'left')), ('ab', 'ab', (0, 'left')), ('ab', 'ab', (0, 'right')), ('ab', 'ab', (1, 'right')), ('ab', 'ba', (1, 'left')), ('b', 'ab', (0, 'left')), ('b', 'b', (1, 'left')), ('b', 'b', (1, 'right')), ('b', 'ba', (0, 'right')), ('ba', 'ab', (0, 'left')), ('ba', 'ba', (0, 'right')), ('ba', 'ba', (1, 'left')), ('ba', 'ba', (1, 'right'))]\n```\n\nThis was inadvertently broken by #8044 which discarded the `left` / `right` info.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8913\n\n",
    "created_at": "2010-05-07T15:10:43Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "S.cayley_graph(side = \"twosided\") returns broken labels",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8913",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat @rbeezer

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

archive/issue_comments_081968.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-18T21:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-81968",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081969.json:
```json
{
    "body": "Changing keywords from \"\" to \"cayley graph\".",
    "created_at": "2010-05-18T21:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-81969",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "" to "cayley graph".



---

archive/issue_comments_081970.json:
```json
{
    "body": "Attachment [trac_8913-cayley_graph_twosided_labels-nt.patch](tarball://root/attachments/some-uuid/ticket8913/trac_8913-cayley_graph_twosided_labels-nt.patch) by @nthiery created at 2010-05-18 21:18:56",
    "created_at": "2010-05-18T21:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-81970",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_8913-cayley_graph_twosided_labels-nt.patch](tarball://root/attachments/some-uuid/ticket8913/trac_8913-cayley_graph_twosided_labels-nt.patch) by @nthiery created at 2010-05-18 21:18:56



---

archive/issue_comments_081971.json:
```json
{
    "body": "Looks good.  Running tests now.",
    "created_at": "2010-05-19T03:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-81971",
    "user": "https://github.com/rbeezer"
}
```

Looks good.  Running tests now.



---

archive/issue_comments_081972.json:
```json
{
    "body": "Looks good (including the addition of a new doctest for this situation).\n\nApplies, builds, whole library passes tests, docs are fine, all on 4.4.2.rc0.\n\nPositive review.",
    "created_at": "2010-05-19T05:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-81972",
    "user": "https://github.com/rbeezer"
}
```

Looks good (including the addition of a new doctest for this situation).

Applies, builds, whole library passes tests, docs are fine, all on 4.4.2.rc0.

Positive review.



---

archive/issue_comments_081973.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-19T05:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-81973",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081974.json:
```json
{
    "body": "Replying to [comment:4 rbeezer]:\n> Looks good (including the addition of a new doctest for this situation).\n> \n> Applies, builds, whole library passes tests, docs are fine, all on 4.4.2.rc0.\n> \n> Positive review.\n\n\nThanks Rob, that was quick!",
    "created_at": "2010-05-19T06:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-81974",
    "user": "https://github.com/nthiery"
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

archive/issue_events_021772.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T01:12:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8913#event-21772"
}
```



---

archive/issue_comments_081975.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8913",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8913#issuecomment-81975",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
