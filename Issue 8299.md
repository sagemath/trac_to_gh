# Issue 8299: coercion and the bool type

archive/issues_008299.json:
```json
{
    "body": "Assignee: @robertwb\n\nClearly this is undesirable:\n\n\n```\nsage: 5r + True\n6\nsage: 5 + True\n2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8299\n\n",
    "created_at": "2010-02-18T22:28:12Z",
    "labels": [
        "coercion",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "coercion and the bool type",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8299",
    "user": "@robertwb"
}
```
Assignee: @robertwb

Clearly this is undesirable:


```
sage: 5r + True
6
sage: 5 + True
2
```


Issue created by migration from https://trac.sagemath.org/ticket/8299





---

archive/issue_comments_073516.json:
```json
{
    "body": "Attachment [8299-integer-bool-coerce.patch](tarball://root/attachments/some-uuid/ticket8299/8299-integer-bool-coerce.patch) by @robertwb created at 2010-02-18 22:30:21",
    "created_at": "2010-02-18T22:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8299#issuecomment-73516",
    "user": "@robertwb"
}
```

Attachment [8299-integer-bool-coerce.patch](tarball://root/attachments/some-uuid/ticket8299/8299-integer-bool-coerce.patch) by @robertwb created at 2010-02-18 22:30:21



---

archive/issue_comments_073517.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-18T22:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8299#issuecomment-73517",
    "user": "@robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073518.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-26T11:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8299#issuecomment-73518",
    "user": "rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073519.json:
```json
{
    "body": "All good Robert. This patch treats True as 1, False as 0 for arithmetic with non-complex types.\n\n```\nsage: [k+True for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]\n[4, 4, 4.00000000000000, 4.0, 4/3, 2]\n\nsage: [k+False for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]\n[3, 3, 3.00000000000000, 3.0, 1/3, 1]\n\nsage: [k*True for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]\n[3, 3, 3.00000000000000, 3.0, 1/3, 1]\n\nsage: [k*False for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]\n[0, 0, 0.000000000000000, 0.0, 0, 0]\n```\n",
    "created_at": "2010-02-26T11:13:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8299#issuecomment-73519",
    "user": "rossk"
}
```

All good Robert. This patch treats True as 1, False as 0 for arithmetic with non-complex types.

```
sage: [k+True for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]
[4, 4, 4.00000000000000, 4.0, 4/3, 2]

sage: [k+False for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]
[3, 3, 3.00000000000000, 3.0, 1/3, 1]

sage: [k*True for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]
[3, 3, 3.00000000000000, 3.0, 1/3, 1]

sage: [k*False for k in (3, 3r, 3.0, 3.0r, 1/3, 3*I+5)]
[0, 0, 0.000000000000000, 0.0, 0, 0]
```




---

archive/issue_comments_073520.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-02T21:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8299#issuecomment-73520",
    "user": "mvngu"
}
```

Resolution: fixed
