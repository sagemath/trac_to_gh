# Issue 9318: Fix S-Box CNF generation for non permutations

archive/issues_009318.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThis should work:\n\n\n```python\nsage: o = range(8) + range(8)\nsage: shuffle(o)\nsage: S = mq.SBox(o)\nsage: S.is_permutation()\nFalse\n\nsage: len(S.cnf()) == 3*2^4\nTrue\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9318\n\n",
    "created_at": "2010-06-23T15:41:09Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Fix S-Box CNF generation for non permutations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9318",
    "user": "malb"
}
```
Assignee: AlexGhitza

This should work:


```python
sage: o = range(8) + range(8)
sage: shuffle(o)
sage: S = mq.SBox(o)
sage: S.is_permutation()
False

sage: len(S.cnf()) == 3*2^4
True
```



Issue created by migration from https://trac.sagemath.org/ticket/9318





---

archive/issue_comments_087811.json:
```json
{
    "body": "Attachment [sbox_fixes.patch](tarball://root/attachments/some-uuid/ticket9318/sbox_fixes.patch) by malb created at 2010-06-23 15:42:00",
    "created_at": "2010-06-23T15:42:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9318#issuecomment-87811",
    "user": "malb"
}
```

Attachment [sbox_fixes.patch](tarball://root/attachments/some-uuid/ticket9318/sbox_fixes.patch) by malb created at 2010-06-23 15:42:00



---

archive/issue_comments_087812.json:
```json
{
    "body": "Applies fine to sage-4.5.alpha0, and does the job. If it was \"needs_review\" I would give a positive one...",
    "created_at": "2010-06-28T21:47:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9318#issuecomment-87812",
    "user": "ylchapuy"
}
```

Applies fine to sage-4.5.alpha0, and does the job. If it was "needs_review" I would give a positive one...



---

archive/issue_comments_087813.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-29T10:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9318#issuecomment-87813",
    "user": "malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087814.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-29T10:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9318#issuecomment-87814",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087815.json:
```json
{
    "body": "sorry, my bad",
    "created_at": "2010-06-29T10:20:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9318#issuecomment-87815",
    "user": "malb"
}
```

sorry, my bad



---

archive/issue_comments_087816.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T09:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9318#issuecomment-87816",
    "user": "mpatel"
}
```

Resolution: fixed
