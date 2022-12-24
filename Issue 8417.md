# Issue 8417: improve CubeGraph and HyperStarGraph generation

archive/issues_008417.json:
```json
{
    "body": "Assignee: @rlmill\n\nsee the title...\n\nIssue created by migration from https://trac.sagemath.org/ticket/8417\n\n",
    "created_at": "2010-03-02T11:00:37Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "improve CubeGraph and HyperStarGraph generation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8417",
    "user": "ylchapuy"
}
```
Assignee: @rlmill

see the title...

Issue created by migration from https://trac.sagemath.org/ticket/8417





---

archive/issue_comments_075423.json:
```json
{
    "body": "Attachment [trac_8417.patch](tarball://root/attachments/some-uuid/ticket8417/trac_8417.patch) by ylchapuy created at 2010-03-02 11:02:15",
    "created_at": "2010-03-02T11:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8417#issuecomment-75423",
    "user": "ylchapuy"
}
```

Attachment [trac_8417.patch](tarball://root/attachments/some-uuid/ticket8417/trac_8417.patch) by ylchapuy created at 2010-03-02 11:02:15



---

archive/issue_comments_075424.json:
```json
{
    "body": "the provided patch does also some 'cosmetic' changes, replacing \n`range(2*n)[n:]`with `range(n,2*n)`.",
    "created_at": "2010-03-02T11:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8417#issuecomment-75424",
    "user": "ylchapuy"
}
```

the provided patch does also some 'cosmetic' changes, replacing 
`range(2*n)[n:]`with `range(n,2*n)`.



---

archive/issue_comments_075425.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-02T11:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8417#issuecomment-75425",
    "user": "ylchapuy"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075426.json:
```json
{
    "body": "Apply both patches in order.",
    "created_at": "2010-03-09T16:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8417#issuecomment-75426",
    "user": "@rlmill"
}
```

Apply both patches in order.



---

archive/issue_comments_075427.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-09T16:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8417#issuecomment-75427",
    "user": "@rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075428.json:
```json
{
    "body": "Beware, with your patch applied I get:\n\n```\nsage: %timeit graphs.CubeGraph(12)\n5 loops, best of 3: 2.95 s per loop\nsage: time g = graphs.CubeGraph(14)\nCPU times: user 72.66 s, sys: 0.42 s, total: 73.08 s\n```\n\nwhereas with mine only I have:\n\n```\nsage: %timeit graphs.CubeGraph(12)\n5 loops, best of 3: 653 ms per loop\nsage: time g = graphs.CubeGraph(14)\nCPU times: user 3.10 s, sys: 0.06 s, total: 3.16 s\n```\n\n\nThis is mainly because using the construction `Graph(d, ...)` add\nsome checks I avoid setting vertices and edges myself.",
    "created_at": "2010-03-09T18:14:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8417#issuecomment-75428",
    "user": "ylchapuy"
}
```

Beware, with your patch applied I get:

```
sage: %timeit graphs.CubeGraph(12)
5 loops, best of 3: 2.95 s per loop
sage: time g = graphs.CubeGraph(14)
CPU times: user 72.66 s, sys: 0.42 s, total: 73.08 s
```

whereas with mine only I have:

```
sage: %timeit graphs.CubeGraph(12)
5 loops, best of 3: 653 ms per loop
sage: time g = graphs.CubeGraph(14)
CPU times: user 3.10 s, sys: 0.06 s, total: 3.16 s
```


This is mainly because using the construction `Graph(d, ...)` add
some checks I avoid setting vertices and edges myself.



---

archive/issue_comments_075429.json:
```json
{
    "body": "apply on top of other patch",
    "created_at": "2010-03-09T18:21:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8417#issuecomment-75429",
    "user": "@rlmill"
}
```

apply on top of other patch



---

archive/issue_comments_075430.json:
```json
{
    "body": "Attachment [trac_8417-ref.patch](tarball://root/attachments/some-uuid/ticket8417/trac_8417-ref.patch) by @rlmill created at 2010-03-09 18:23:57\n\nReplying to [comment:3 ylchapuy]:\n> Beware, with your patch applied I get:\n\nThank you for pointing this out. I've reverted that part of the patch.\n\nCan you see any way to make the overhead from checking in this case any better? Also, what do you think about a check=False option in graph construction, more generally?",
    "created_at": "2010-03-09T18:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8417#issuecomment-75430",
    "user": "@rlmill"
}
```

Attachment [trac_8417-ref.patch](tarball://root/attachments/some-uuid/ticket8417/trac_8417-ref.patch) by @rlmill created at 2010-03-09 18:23:57

Replying to [comment:3 ylchapuy]:
> Beware, with your patch applied I get:

Thank you for pointing this out. I've reverted that part of the patch.

Can you see any way to make the overhead from checking in this case any better? Also, what do you think about a check=False option in graph construction, more generally?



---

archive/issue_comments_075431.json:
```json
{
    "body": "Merged into 4.4.alpha0:\n- trac_8417.patch\n- trac_8417-ref.patch",
    "created_at": "2010-04-15T23:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8417#issuecomment-75431",
    "user": "@jhpalmieri"
}
```

Merged into 4.4.alpha0:
- trac_8417.patch
- trac_8417-ref.patch



---

archive/issue_comments_075432.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8417#issuecomment-75432",
    "user": "@jhpalmieri"
}
```

Resolution: fixed
