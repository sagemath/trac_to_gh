# Issue 7366: fix GF(4,'a').list()

archive/issues_007366.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nThis should work:\n\n\n```python\nsage: K.<a>=GF(4)\nsage: [x for x in K]\n[0, a, a + 1, 1]\nsage: hasattr(K, '__iter__')\nTrue\nsage: K.list()\n...\nTypeError:\n'sage.rings.finite_field_givaro.FiniteField_givaro_iterator' object is not iterable\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7366\n\n",
    "created_at": "2009-11-01T00:11:13Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "fix GF(4,'a').list()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7366",
    "user": "malb"
}
```
Assignee: AlexGhitza

This should work:


```python
sage: K.<a>=GF(4)
sage: [x for x in K]
[0, a, a + 1, 1]
sage: hasattr(K, '__iter__')
True
sage: K.list()
...
TypeError:
'sage.rings.finite_field_givaro.FiniteField_givaro_iterator' object is not iterable

```


Issue created by migration from https://trac.sagemath.org/ticket/7366





---

archive/issue_comments_061732.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-11-01T00:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7366#issuecomment-61732",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_061733.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-01T00:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7366#issuecomment-61733",
    "user": "malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061734.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-01T03:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7366#issuecomment-61734",
    "user": "rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061735.json:
```json
{
    "body": "Builds on 4.2, fixes the problem, passes all tests.\n\nPositive review.",
    "created_at": "2009-11-01T03:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7366#issuecomment-61735",
    "user": "rbeezer"
}
```

Builds on 4.2, fixes the problem, passes all tests.

Positive review.



---

archive/issue_comments_061736.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-01T04:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7366#issuecomment-61736",
    "user": "mhansen"
}
```

Resolution: fixed
