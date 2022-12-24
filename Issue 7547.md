# Issue 7547: improve has_multiple_edges

archive/issues_007547.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @nathanncohen\n\nIt seems to be the main bottleneck in graph plotting!\nThis patch cuts down by 30% the time for `sage -t graph.py` on my machine... (and doctests of course still pass)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7547\n\n",
    "created_at": "2009-11-28T02:14:34Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "improve has_multiple_edges",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7547",
    "user": "ylchapuy"
}
```
Assignee: @rlmill

CC:  @nathanncohen

It seems to be the main bottleneck in graph plotting!
This patch cuts down by 30% the time for `sage -t graph.py` on my machine... (and doctests of course still pass)

Issue created by migration from https://trac.sagemath.org/ticket/7547





---

archive/issue_comments_064103.json:
```json
{
    "body": "For the record:\n\n```\nsage: P = graphs.PetersenGraph()\nsage: D = graphs.DodecahedralGraph()\nsage: L = D.lexicographic_product(P) \nsage: L.allow_multiple_edges(True)\nsage: time L.has_multiple_edges()\n```\n\n\nBefore: Wall time: 39.56 s\n\nAfter: Wall time: 19.32 s\n\nI hope I did no mistake, it's 4 a.m here...",
    "created_at": "2009-11-28T03:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64103",
    "user": "ylchapuy"
}
```

For the record:

```
sage: P = graphs.PetersenGraph()
sage: D = graphs.DodecahedralGraph()
sage: L = D.lexicographic_product(P) 
sage: L.allow_multiple_edges(True)
sage: time L.has_multiple_edges()
```


Before: Wall time: 39.56 s

After: Wall time: 19.32 s

I hope I did no mistake, it's 4 a.m here...



---

archive/issue_comments_064104.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-28T03:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64104",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064105.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-28T05:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64105",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064106.json:
```json
{
    "body": "Nice work!",
    "created_at": "2009-11-28T05:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64106",
    "user": "@rlmill"
}
```

Nice work!



---

archive/issue_comments_064107.json:
```json
{
    "body": "Well done !! :-)\n\nNathann",
    "created_at": "2009-11-28T08:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64107",
    "user": "@nathanncohen"
}
```

Well done !! :-)

Nathann



---

archive/issue_comments_064108.json:
```json
{
    "body": "Sorry to give myself a \"needs work\" but my ideas are much clearer this morning.\nNew patch to come in a few minutes!",
    "created_at": "2009-11-28T10:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64108",
    "user": "ylchapuy"
}
```

Sorry to give myself a "needs work" but my ideas are much clearer this morning.
New patch to come in a few minutes!



---

archive/issue_comments_064109.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-11-28T10:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64109",
    "user": "ylchapuy"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_064110.json:
```json
{
    "body": "based on 4.3.alpha0",
    "created_at": "2009-11-28T10:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64110",
    "user": "ylchapuy"
}
```

based on 4.3.alpha0



---

archive/issue_comments_064111.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-28T10:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64111",
    "user": "ylchapuy"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064112.json:
```json
{
    "body": "Attachment [trac_7547-has_multiple_edges.patch](tarball://root/attachments/some-uuid/ticket7547/trac_7547-has_multiple_edges.patch) by ylchapuy created at 2009-11-28 10:22:31\n\nNew timing for the same test: 1.22s. It's useful to sleep!",
    "created_at": "2009-11-28T10:22:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64112",
    "user": "ylchapuy"
}
```

Attachment [trac_7547-has_multiple_edges.patch](tarball://root/attachments/some-uuid/ticket7547/trac_7547-has_multiple_edges.patch) by ylchapuy created at 2009-11-28 10:22:31

New timing for the same test: 1.22s. It's useful to sleep!



---

archive/issue_comments_064113.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-28T19:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64113",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064114.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T06:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7547",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7547#issuecomment-64114",
    "user": "@mwhansen"
}
```

Resolution: fixed
