# Issue 8818: Infinite loop in ZZ.range()

archive/issues_008818.json:
```json
{
    "body": "Assignee: AlexGhitza\n\n\n```\nsage: ZZ.range(1r, 10r)\n...\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8818\n\n",
    "created_at": "2010-04-29T07:06:09Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Infinite loop in ZZ.range()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8818",
    "user": "robertwb"
}
```
Assignee: AlexGhitza


```
sage: ZZ.range(1r, 10r)
...
```


Issue created by migration from https://trac.sagemath.org/ticket/8818





---

archive/issue_comments_080937.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-29T07:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8818#issuecomment-80937",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080938.json:
```json
{
    "body": "Attachment [8818-ZZ-range.patch](tarball://root/attachments/some-uuid/ticket8818/8818-ZZ-range.patch) by robertwb created at 2010-04-29 07:09:35\n\nLooks like it was a typo in that function, easy fix.",
    "created_at": "2010-04-29T07:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8818#issuecomment-80938",
    "user": "robertwb"
}
```

Attachment [8818-ZZ-range.patch](tarball://root/attachments/some-uuid/ticket8818/8818-ZZ-range.patch) by robertwb created at 2010-04-29 07:09:35

Looks like it was a typo in that function, easy fix.



---

archive/issue_comments_080939.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-29T10:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8818#issuecomment-80939",
    "user": "leif"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080940.json:
```json
{
    "body": "Though I prefer the `trac_` prefix (and the bug doesn't necessarily end up in an infinite loop)... ;-)",
    "created_at": "2010-04-29T10:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8818#issuecomment-80940",
    "user": "leif"
}
```

Though I prefer the `trac_` prefix (and the bug doesn't necessarily end up in an infinite loop)... ;-)



---

archive/issue_comments_080941.json:
```json
{
    "body": "Changing keywords from \"\" to \"integer_ring, IntegerRing, range()\".",
    "created_at": "2010-04-29T10:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8818#issuecomment-80941",
    "user": "leif"
}
```

Changing keywords from "" to "integer_ring, IntegerRing, range()".



---

archive/issue_comments_080942.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:31:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8818",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8818#issuecomment-80942",
    "user": "mvngu"
}
```

Resolution: fixed
