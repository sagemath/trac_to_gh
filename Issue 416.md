# Issue 416: Faster GF(2^n) arithmetic for n >= 16

archive/issues_000416.json:
```json
{
    "body": "Assignee: somebody\n\nUsing a Python wrapper around Pari is too slow.  ntl.GF2E on the other hand should be a lot faster.\n\nIssue created by migration from https://trac.sagemath.org/ticket/416\n\n",
    "created_at": "2007-08-10T14:43:59Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "title": "Faster GF(2^n) arithmetic for n >= 16",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/416",
    "user": "malb"
}
```
Assignee: somebody

Using a Python wrapper around Pari is too slow.  ntl.GF2E on the other hand should be a lot faster.

Issue created by migration from https://trac.sagemath.org/ticket/416





---

archive/issue_comments_002051.json:
```json
{
    "body": "Changing assignee from somebody to malb.",
    "created_at": "2007-10-21T22:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/416#issuecomment-2051",
    "user": "malb"
}
```

Changing assignee from somebody to malb.



---

archive/issue_comments_002052.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-21T22:54:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/416#issuecomment-2052",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002053.json:
```json
{
    "body": "Attachment",
    "created_at": "2007-10-25T12:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/416#issuecomment-2053",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_002054.json:
```json
{
    "body": "The attached patch implements GF(2<sup>n</sup>) for n >= 16 using NTL's GF2E and also refactors `FiniteField*` such that writing GF(p<sup>n</sup>) for p<sup>n</sup> >= 2<sup>16</sup> should be easier. This patch also fixes an issue with `ntl.GF2X` and applies cleanly against 2.8.9. 'make test' passes.\n\nSpeed:\n\n\n```\nsage: F1 = FiniteField_givaro(2^15,'a')\nsage: F2 = FiniteField_ntl_gf2e(2^15,'a')\nsage: F3 = FiniteField_ext_pari(2^15,'a')\n\nsage: F1.polynomial()\na^15 + a^5 + a^4 + a^2 + 1\nsage: F2.polynomial()\na^15 + a^5 + a^4 + a^2 + 1\nsage: F3.polynomial()\na^15 + a^5 + a^4 + a^2 + 1\n\nsage: e1 = F1.random_element(); f1 = F1.random_element()\nsage: e2 = F2.random_element(); f2 = F2.random_element()\nsage: e3 = F3.random_element(); f3 = F3.random_element()\n\nsage: %timeit e1*f1\n1000000 loops, best of 3: 249 ns per loop\nsage: %timeit e2*f2\n1000000 loops, best of 3: 496 ns per loop\nsage: %timeit e3*f3\n10000 loops, best of 3: 36.9 \u00b5s per loop\n\nsage: %timeit e1+f1\n1000000 loops, best of 3: 255 ns per loop\nsage: %timeit e2+f2\n1000000 loops, best of 3: 391 ns per loop\nsage: %timeit e3+f3\n10000 loops, best of 3: 12.9 \u00b5s per loop\n```\n",
    "created_at": "2007-10-25T13:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/416#issuecomment-2054",
    "user": "malb"
}
```

The attached patch implements GF(2<sup>n</sup>) for n >= 16 using NTL's GF2E and also refactors `FiniteField*` such that writing GF(p<sup>n</sup>) for p<sup>n</sup> >= 2<sup>16</sup> should be easier. This patch also fixes an issue with `ntl.GF2X` and applies cleanly against 2.8.9. 'make test' passes.

Speed:


```
sage: F1 = FiniteField_givaro(2^15,'a')
sage: F2 = FiniteField_ntl_gf2e(2^15,'a')
sage: F3 = FiniteField_ext_pari(2^15,'a')

sage: F1.polynomial()
a^15 + a^5 + a^4 + a^2 + 1
sage: F2.polynomial()
a^15 + a^5 + a^4 + a^2 + 1
sage: F3.polynomial()
a^15 + a^5 + a^4 + a^2 + 1

sage: e1 = F1.random_element(); f1 = F1.random_element()
sage: e2 = F2.random_element(); f2 = F2.random_element()
sage: e3 = F3.random_element(); f3 = F3.random_element()

sage: %timeit e1*f1
1000000 loops, best of 3: 249 ns per loop
sage: %timeit e2*f2
1000000 loops, best of 3: 496 ns per loop
sage: %timeit e3*f3
10000 loops, best of 3: 36.9 µs per loop

sage: %timeit e1+f1
1000000 loops, best of 3: 255 ns per loop
sage: %timeit e2+f2
1000000 loops, best of 3: 391 ns per loop
sage: %timeit e3+f3
10000 loops, best of 3: 12.9 µs per loop
```




---

archive/issue_comments_002055.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T02:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/416#issuecomment-2055",
    "user": "cwitty"
}
```

Resolution: fixed
