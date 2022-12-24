# Issue 8814: Remove redundant checks for elliptic curve group structure

archive/issues_008814.json:
```json
{
    "body": "Assignee: cremona\n\nCC:  cremona\n\nThese were doing nothing but slowing things down. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8814\n\n",
    "created_at": "2010-04-29T04:11:13Z",
    "labels": [
        "elliptic curves",
        "major",
        "enhancement"
    ],
    "title": "Remove redundant checks for elliptic curve group structure",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8814",
    "user": "robertwb"
}
```
Assignee: cremona

CC:  cremona

These were doing nothing but slowing things down. 

Issue created by migration from https://trac.sagemath.org/ticket/8814





---

archive/issue_comments_080899.json:
```json
{
    "body": "Attachment [8814-ec-group-speedup.patch](tarball://root/attachments/some-uuid/ticket8814/8814-ec-group-speedup.patch) by robertwb created at 2010-04-29 04:15:35\n\nBefore: \n\n\n```\nsage: F.<a>=GF(101^3,'a')\nsage: timeit(\"EllipticCurve([2*a^2 + 48*a + 27, 89*a^2 + 76*a + 24]).abelian_group()\")\n5 loops, best of 3: 1.37 s per loop\nsage: timeit(\"EllipticCurve(GF(1009), [2, 1]).abelian_group()\")\n25 loops, best of 3: 21.1 ms per loop\n```\n\n\nAfter:\n\n\n```\nsage: F.<a>=GF(101^3,'a')\nsage: timeit(\"EllipticCurve([2*a^2 + 48*a + 27, 89*a^2 + 76*a + 24]).abelian_group()\")\n5 loops, best of 3: 1.28 s per loop\nsage: timeit(\"EllipticCurve(GF(1009), [2, 1]).abelian_group()\")\n5 loops, best of 3: 15.2 ms per loop\n```\n\n\nOf course, this is just low hanging fruit (I've gotten 40x or more speedup in EC point arithmetic alone via Cython) but every little bit helps.",
    "created_at": "2010-04-29T04:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8814#issuecomment-80899",
    "user": "robertwb"
}
```

Attachment [8814-ec-group-speedup.patch](tarball://root/attachments/some-uuid/ticket8814/8814-ec-group-speedup.patch) by robertwb created at 2010-04-29 04:15:35

Before: 


```
sage: F.<a>=GF(101^3,'a')
sage: timeit("EllipticCurve([2*a^2 + 48*a + 27, 89*a^2 + 76*a + 24]).abelian_group()")
5 loops, best of 3: 1.37 s per loop
sage: timeit("EllipticCurve(GF(1009), [2, 1]).abelian_group()")
25 loops, best of 3: 21.1 ms per loop
```


After:


```
sage: F.<a>=GF(101^3,'a')
sage: timeit("EllipticCurve([2*a^2 + 48*a + 27, 89*a^2 + 76*a + 24]).abelian_group()")
5 loops, best of 3: 1.28 s per loop
sage: timeit("EllipticCurve(GF(1009), [2, 1]).abelian_group()")
5 loops, best of 3: 15.2 ms per loop
```


Of course, this is just low hanging fruit (I've gotten 40x or more speedup in EC point arithmetic alone via Cython) but every little bit helps.



---

archive/issue_comments_080900.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-29T04:15:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8814#issuecomment-80900",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080901.json:
```json
{
    "body": "Looks good, will test properly shortly...",
    "created_at": "2010-04-29T07:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8814#issuecomment-80901",
    "user": "cremona"
}
```

Looks good, will test properly shortly...



---

archive/issue_comments_080902.json:
```json
{
    "body": "Applies to 4.4 and tests pass -- positive review!",
    "created_at": "2010-04-29T08:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8814#issuecomment-80902",
    "user": "cremona"
}
```

Applies to 4.4 and tests pass -- positive review!



---

archive/issue_comments_080903.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-29T08:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8814#issuecomment-80903",
    "user": "cremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080904.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-08T21:52:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8814",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8814#issuecomment-80904",
    "user": "mvngu"
}
```

Resolution: fixed
