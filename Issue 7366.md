# Issue 7366: fix GF(4,'a').list()

archive/issues_007366.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis should work:\n\n```\nsage: K.<a>=GF(4)\nsage: [x for x in K]\n[0, a, a + 1, 1]\nsage: hasattr(K, '__iter__')\nTrue\nsage: K.list()\n...\nTypeError:\n'sage.rings.finite_field_givaro.FiniteField_givaro_iterator' object is not iterable\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7366\n\n",
    "closed_at": "2009-11-01T04:47:08Z",
    "created_at": "2009-11-01T00:11:13Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "fix GF(4,'a').list()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7366",
    "user": "https://github.com/malb"
}
```
Assignee: @aghitza

This should work:

```
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

archive/issue_comments_061618.json:
```json
{
    "body": "Attachment [finite_field_givaro_iter.patch](tarball://root/attachments/some-uuid/ticket7366/finite_field_givaro_iter.patch) by @malb created at 2009-11-01 00:11:34",
    "created_at": "2009-11-01T00:11:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7366#issuecomment-61618",
    "user": "https://github.com/malb"
}
```

Attachment [finite_field_givaro_iter.patch](tarball://root/attachments/some-uuid/ticket7366/finite_field_givaro_iter.patch) by @malb created at 2009-11-01 00:11:34



---

archive/issue_comments_061619.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-01T00:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7366#issuecomment-61619",
    "user": "https://github.com/malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061620.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-01T03:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7366#issuecomment-61620",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061621.json:
```json
{
    "body": "Builds on 4.2, fixes the problem, passes all tests.\n\nPositive review.",
    "created_at": "2009-11-01T03:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7366#issuecomment-61621",
    "user": "https://github.com/rbeezer"
}
```

Builds on 4.2, fixes the problem, passes all tests.

Positive review.



---

archive/issue_comments_061622.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-01T04:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7366",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7366#issuecomment-61622",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017426.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-01T04:47:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7366",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7366#event-17426"
}
```
