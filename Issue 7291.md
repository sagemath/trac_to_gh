# Issue 7291: Max Cut

archive/issues_007291.json:
```json
{
    "body": "Assignee: rlm\n\nMax cut is a NP-Hard problem, which could as usual be written as a LP if no better solution is found.\n\nhttp://en.wikipedia.org/wiki/Maximum_cut\n\nIssue created by migration from https://trac.sagemath.org/ticket/7291\n\n",
    "created_at": "2009-10-25T09:20:40Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Max Cut",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7291",
    "user": "ncohen"
}
```
Assignee: rlm

Max cut is a NP-Hard problem, which could as usual be written as a LP if no better solution is found.

http://en.wikipedia.org/wiki/Maximum_cut

Issue created by migration from https://trac.sagemath.org/ticket/7291





---

archive/issue_comments_060697.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-14T17:54:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7291#issuecomment-60697",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060698.json:
```json
{
    "body": "You should include more examples in your doctests. At least make sure that each input is tested. For example:\n\n```\nsage: g.max_cut(vertices=True)\n30.0\n```\n\nShouldn't this be returning two sets of vertices?",
    "created_at": "2009-12-15T16:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7291#issuecomment-60698",
    "user": "rlm"
}
```

You should include more examples in your doctests. At least make sure that each input is tested. For example:

```
sage: g.max_cut(vertices=True)
30.0
```

Shouldn't this be returning two sets of vertices?



---

archive/issue_comments_060699.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T16:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7291#issuecomment-60699",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060700.json:
```json
{
    "body": "I had forgotten the implication : vertices=True => value_only=True :-)\n\nUpdated !",
    "created_at": "2009-12-16T11:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7291#issuecomment-60700",
    "user": "ncohen"
}
```

I had forgotten the implication : vertices=True => value_only=True :-)

Updated !



---

archive/issue_comments_060701.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-16T11:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7291#issuecomment-60701",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060702.json:
```json
{
    "body": "Attachment [trac_7291.patch](tarball://root/attachments/some-uuid/ticket7291/trac_7291.patch) by ncohen created at 2009-12-16 11:29:12",
    "created_at": "2009-12-16T11:29:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7291#issuecomment-60702",
    "user": "ncohen"
}
```

Attachment [trac_7291.patch](tarball://root/attachments/some-uuid/ticket7291/trac_7291.patch) by ncohen created at 2009-12-16 11:29:12



---

archive/issue_comments_060703.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T18:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7291#issuecomment-60703",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060704.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T22:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7291",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7291#issuecomment-60704",
    "user": "mhansen"
}
```

Resolution: fixed
