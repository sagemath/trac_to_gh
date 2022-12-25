# Issue 9883: slow coercion of polynomial to list over integer mod ring

archive/issues_009883.json:
```json
{
    "body": "Assignee: tbd\n\nSage 4.5.3, 2.6GHz Opteron, Linux\n\n```\nsage: R = Integers(3^20)\nsage: S.<x> = PolynomialRing(R)\nsage: f = S([R.random_element() for i in range(100)])\nsage: timeit(\"L = f.list()\")\n125 loops, best of 3: 1.13 ms per loop\n```\n\n\nThat's about 29000 cycles per coefficient conversion. See also #9883.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9884\n\n",
    "created_at": "2010-09-09T16:03:04Z",
    "labels": [
        "component: performance",
        "bug"
    ],
    "title": "slow coercion of polynomial to list over integer mod ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9883",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: tbd

Sage 4.5.3, 2.6GHz Opteron, Linux

```
sage: R = Integers(3^20)
sage: S.<x> = PolynomialRing(R)
sage: f = S([R.random_element() for i in range(100)])
sage: timeit("L = f.list()")
125 loops, best of 3: 1.13 ms per loop
```


That's about 29000 cycles per coefficient conversion. See also #9883.


Issue created by migration from https://trac.sagemath.org/ticket/9884





---

archive/issue_comments_097798.json:
```json
{
    "body": "This is sped up by about a factor of 33 by the patch at #9887.  If that's positively reviewed, I would suggest closing this ticket.",
    "created_at": "2010-09-23T11:30:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9883#issuecomment-97798",
    "user": "https://github.com/roed314"
}
```

This is sped up by about a factor of 33 by the patch at #9887.  If that's positively reviewed, I would suggest closing this ticket.



---

archive/issue_comments_097799.json:
```json
{
    "body": "6.2.beta4, on an Intel(R) Core(TM) i5-3320M CPU `@` 2.60GHz:\n\n```\nsage: R = Integers(3^20)\nsage: S.<x> = PolynomialRing(R)\nsage: f = S([R.random_element() for i in range(100)])\nsage: timeit(\"L = f.list()\")\n625 loops, best of 3: 166 \u00b5s per loop\n```\nSo I only get a factor of ~7 wrt the timings reported by David Harvey.\n\nDavid (Roe), can you please check if you still observe the same speedup or if there has been a regression in the meantime?",
    "created_at": "2014-02-02T11:51:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9883#issuecomment-97799",
    "user": "https://github.com/mezzarobba"
}
```

6.2.beta4, on an Intel(R) Core(TM) i5-3320M CPU `@` 2.60GHz:

```
sage: R = Integers(3^20)
sage: S.<x> = PolynomialRing(R)
sage: f = S([R.random_element() for i in range(100)])
sage: timeit("L = f.list()")
625 loops, best of 3: 166 µs per loop
```
So I only get a factor of ~7 wrt the timings reported by David Harvey.

David (Roe), can you please check if you still observe the same speedup or if there has been a regression in the meantime?



---

archive/issue_comments_097800.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2014-03-14T16:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9883#issuecomment-97800",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_097801.json:
```json
{
    "body": "Version 7.1.beta3 - Intel(R) Core(TM) i5-4278U CPU `@` 2.60GHz\n\n```\nsage: R = Integers(3^20)\nsage: S.<x> = PolynomialRing(R)\nsage: f = S([R.random_element() for i in range(100)])\nsage: timeit(\"L = f.list()\")\n625 loops, best of 3: 85.8 \u00b5s per loop\n\n```\n\na bit faster on my slightly faster cpu.\n\nFast enough?",
    "created_at": "2016-03-22T21:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9883#issuecomment-97801",
    "user": "https://github.com/edgarcosta"
}
```

Version 7.1.beta3 - Intel(R) Core(TM) i5-4278U CPU `@` 2.60GHz

```
sage: R = Integers(3^20)
sage: S.<x> = PolynomialRing(R)
sage: f = S([R.random_element() for i in range(100)])
sage: timeit("L = f.list()")
625 loops, best of 3: 85.8 µs per loop

```

a bit faster on my slightly faster cpu.

Fast enough?
