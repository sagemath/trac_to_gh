# Issue 967: [with patch] inplace operators for GF(p),GF(p^n) and MPolynomial_libsingular

archive/issues_000967.json:
```json
{
    "body": "Assignee: somebody\n\nThe attached patches implement inplace operators for `IntegerMod`, `FiniteFieldElement_givaro` and `MPolynomial_libsingular`.\n\nSome timings for GF(q)\n\nBefore:\n\n\n```\nsage: k.<a> = GF(2^15)\nsage: A = [a^i for i in range(k.order())]\nsage: %timeit _ = sum(A)\n100 loops, best of 3: 6.79 ms per loop\n```\n\n\nAfter:\n\n\n```\nsage: k.<a> = GF(2^15)\nsage: A = [a^i for i in range(k.order())]\nsage: %timeit _ = sum(A)\n100 loops, best of 3: 2.05 ms per loop\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/967\n\n",
    "created_at": "2007-10-21T22:37:50Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "[with patch] inplace operators for GF(p),GF(p^n) and MPolynomial_libsingular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/967",
    "user": "malb"
}
```
Assignee: somebody

The attached patches implement inplace operators for `IntegerMod`, `FiniteFieldElement_givaro` and `MPolynomial_libsingular`.

Some timings for GF(q)

Before:


```
sage: k.<a> = GF(2^15)
sage: A = [a^i for i in range(k.order())]
sage: %timeit _ = sum(A)
100 loops, best of 3: 6.79 ms per loop
```


After:


```
sage: k.<a> = GF(2^15)
sage: A = [a^i for i in range(k.order())]
sage: %timeit _ = sum(A)
100 loops, best of 3: 2.05 ms per loop
```


Issue created by migration from https://trac.sagemath.org/ticket/967





---

archive/issue_comments_005903.json:
```json
{
    "body": "Attachment [iadd_gfp.patch](tarball://root/attachments/some-uuid/ticket967/iadd_gfp.patch) by malb created at 2007-10-21 22:38:42",
    "created_at": "2007-10-21T22:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/967#issuecomment-5903",
    "user": "malb"
}
```

Attachment [iadd_gfp.patch](tarball://root/attachments/some-uuid/ticket967/iadd_gfp.patch) by malb created at 2007-10-21 22:38:42



---

archive/issue_comments_005904.json:
```json
{
    "body": "Attachment [iadd_mpoly.patch](tarball://root/attachments/some-uuid/ticket967/iadd_mpoly.patch) by malb created at 2007-10-21 22:38:55",
    "created_at": "2007-10-21T22:38:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/967#issuecomment-5904",
    "user": "malb"
}
```

Attachment [iadd_mpoly.patch](tarball://root/attachments/some-uuid/ticket967/iadd_mpoly.patch) by malb created at 2007-10-21 22:38:55



---

archive/issue_comments_005905.json:
```json
{
    "body": "Changing assignee from somebody to malb.",
    "created_at": "2007-10-21T22:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/967#issuecomment-5905",
    "user": "malb"
}
```

Changing assignee from somebody to malb.



---

archive/issue_comments_005906.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-21T22:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/967#issuecomment-5906",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005907.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-23T19:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/967#issuecomment-5907",
    "user": "malb"
}
```

Resolution: fixed



---

archive/issue_comments_005908.json:
```json
{
    "body": "This was applied to 2.8.9.alpha0",
    "created_at": "2007-10-23T19:55:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/967#issuecomment-5908",
    "user": "malb"
}
```

This was applied to 2.8.9.alpha0
