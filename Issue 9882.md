# Issue 9882: slow coercion of list to polynomial over integer mod ring

archive/issues_009882.json:
```json
{
    "body": "Assignee: tbd\n\nSage 4.5.3, 2.6GHz Opteron, Linux: \n\n\n```\nsage: R = Integers(3^20)\nsage: S.<x> = PolynomialRing(R)\nsage: L = [R.random_element() for i in range(100)]\nsage: timeit(\"f = S(L)\")\n125 loops, best of 3: 4.79 ms per loop\n```\n\n\nThat's about 124000 cycles per coefficient conversion. Compare to the cost of multiplying polynomials of the same degree:\n\n```\nsage: f = S([R.random_element() for i in range(100)])\nsage: g = S([R.random_element() for i in range(100)])\nsage: timeit(\"h = f * g\")\n625 loops, best of 3: 31.8 \u00b5s per loop\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9883\n\n",
    "created_at": "2010-09-09T16:00:33Z",
    "labels": [
        "component: performance",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "slow coercion of list to polynomial over integer mod ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9882",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: tbd

Sage 4.5.3, 2.6GHz Opteron, Linux: 


```
sage: R = Integers(3^20)
sage: S.<x> = PolynomialRing(R)
sage: L = [R.random_element() for i in range(100)]
sage: timeit("f = S(L)")
125 loops, best of 3: 4.79 ms per loop
```


That's about 124000 cycles per coefficient conversion. Compare to the cost of multiplying polynomials of the same degree:

```
sage: f = S([R.random_element() for i in range(100)])
sage: g = S([R.random_element() for i in range(100)])
sage: timeit("h = f * g")
625 loops, best of 3: 31.8 µs per loop
```



Issue created by migration from https://trac.sagemath.org/ticket/9883





---

archive/issue_comments_097793.json:
```json
{
    "body": "This is sped up by about a factor of 200 by the patch at #9887. If that's positively reviewed, I would suggest closing this ticket.",
    "created_at": "2010-09-23T11:31:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9882#issuecomment-97793",
    "user": "https://github.com/roed314"
}
```

This is sped up by about a factor of 200 by the patch at #9887. If that's positively reviewed, I would suggest closing this ticket.



---

archive/issue_comments_097794.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-02-02T11:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9882#issuecomment-97794",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097795.json:
```json
{
    "body": "With sage-6.1:\n\n```\nsage: sage: R = Integers(3^20)\nsage: sage: S.<x> = PolynomialRing(R)\nsage: sage: L = [R.random_element() for i in range(100)]\nsage: sage: timeit(\"f = S(L)\")\n625 loops, best of 3: 49.6 \u00b5s per loop\nsage: sage: L = [R.random_element() for i in range(1000)]\nsage: sage: timeit(\"f = S(L)\")\n625 loops, best of 3: 388 \u00b5s per loop\n\nsage: sage: f = S([R.random_element() for i in range(100)])\nsage: sage: g = S([R.random_element() for i in range(100)])\nsage: sage: timeit(\"h = f * g\")\n625 loops, best of 3: 10.9 \u00b5s per loop\n```\n",
    "created_at": "2014-02-02T11:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9882#issuecomment-97795",
    "user": "https://github.com/mezzarobba"
}
```

With sage-6.1:

```
sage: sage: R = Integers(3^20)
sage: sage: S.<x> = PolynomialRing(R)
sage: sage: L = [R.random_element() for i in range(100)]
sage: sage: timeit("f = S(L)")
625 loops, best of 3: 49.6 µs per loop
sage: sage: L = [R.random_element() for i in range(1000)]
sage: sage: timeit("f = S(L)")
625 loops, best of 3: 388 µs per loop

sage: sage: f = S([R.random_element() for i in range(100)])
sage: sage: g = S([R.random_element() for i in range(100)])
sage: sage: timeit("h = f * g")
625 loops, best of 3: 10.9 µs per loop
```




---

archive/issue_comments_097796.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-09T21:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9882#issuecomment-97796",
    "user": "https://github.com/a-andre"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_010010.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-02-11T21:22:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9882",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9882#event-10010"
}
```



---

archive/issue_comments_097797.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-02-11T21:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9882",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9882#issuecomment-97797",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate
