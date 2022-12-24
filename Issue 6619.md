# Issue 6619: [with patch, needs review] Fix ``inner`` option for integer vectors

archive/issues_006619.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  sage-combinat burcin\n\nKeywords: inner, integer vectors\n\n\n```\n            sage: IV = IntegerVectors(3,10,inner=[4,1,3], min_part = 2)\n            sage: min_length, max_length, floor, ceiling, min_slope, max_slope = IV._parameters()\n            sage: floor(1), floor(2), floor(3)\n            (4, 2, 3)\n\n            sage: IV = IntegerVectors(3, 10, outer=[4,1,3], max_part = 3)\n            sage: min_length, max_length, floor, ceiling, min_slope, max_slope = IV._parameters()\n            sage: ceiling(1), ceiling(2), ceiling(3)\n            (3, 1, 3)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6619\n\n",
    "created_at": "2009-07-25T15:01:53Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Fix ``inner`` option for integer vectors",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6619",
    "user": "nthiery"
}
```
Assignee: tbd

CC:  sage-combinat burcin

Keywords: inner, integer vectors


```
            sage: IV = IntegerVectors(3,10,inner=[4,1,3], min_part = 2)
            sage: min_length, max_length, floor, ceiling, min_slope, max_slope = IV._parameters()
            sage: floor(1), floor(2), floor(3)
            (4, 2, 3)

            sage: IV = IntegerVectors(3, 10, outer=[4,1,3], max_part = 3)
            sage: min_length, max_length, floor, ceiling, min_slope, max_slope = IV._parameters()
            sage: ceiling(1), ceiling(2), ceiling(3)
            (3, 1, 3)
```


Issue created by migration from https://trac.sagemath.org/ticket/6619





---

archive/issue_comments_054242.json:
```json
{
    "body": "Attachment [trac_6619_integer_vector_inner-fix-nt.patch](tarball://root/attachments/some-uuid/ticket6619/trac_6619_integer_vector_inner-fix-nt.patch) by nthiery created at 2009-07-25 15:03:16",
    "created_at": "2009-07-25T15:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6619#issuecomment-54242",
    "user": "nthiery"
}
```

Attachment [trac_6619_integer_vector_inner-fix-nt.patch](tarball://root/attachments/some-uuid/ticket6619/trac_6619_integer_vector_inner-fix-nt.patch) by nthiery created at 2009-07-25 15:03:16



---

archive/issue_comments_054243.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-25T15:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6619#issuecomment-54243",
    "user": "nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_054244.json:
```json
{
    "body": "Changing assignee from tbd to nthiery.",
    "created_at": "2009-07-25T15:09:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6619#issuecomment-54244",
    "user": "nthiery"
}
```

Changing assignee from tbd to nthiery.



---

archive/issue_comments_054245.json:
```json
{
    "body": "Changing component from algebra to combinatorics.",
    "created_at": "2009-07-25T16:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6619#issuecomment-54245",
    "user": "ddrake"
}
```

Changing component from algebra to combinatorics.



---

archive/issue_comments_054246.json:
```json
{
    "body": "Positive review.",
    "created_at": "2009-07-25T16:59:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6619#issuecomment-54246",
    "user": "ddrake"
}
```

Positive review.



---

archive/issue_comments_054247.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-25T21:16:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6619#issuecomment-54247",
    "user": "mvngu"
}
```

Resolution: fixed
