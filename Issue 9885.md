# Issue 9885: slow coercion from integer mod ring to integer ring, part 2

archive/issues_009885.json:
```json
{
    "body": "Assignee: tbd\n\nSage 4.5.3, 2.6GHz Opteron, Linux\n\nThis is ok:\n\n\n```\nsage: R = Integers(3^20)\nsage: u = R(2)\nsage: timeit(\"z = u.lift()\")\n625 loops, best of 3: 351 ns per loop\n```\n\n\nThis is not:\n\n```\nsage: timeit(\"z = ZZ(u)\")\n625 loops, best of 3: 37.9 \u00b5s per loop\n```\n\n\nWow. See also #9885 for a not-quite-as-insane version of this.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9886\n\n",
    "created_at": "2010-09-09T16:07:25Z",
    "labels": [
        "component: performance",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "slow coercion from integer mod ring to integer ring, part 2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9885",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: tbd

Sage 4.5.3, 2.6GHz Opteron, Linux

This is ok:


```
sage: R = Integers(3^20)
sage: u = R(2)
sage: timeit("z = u.lift()")
625 loops, best of 3: 351 ns per loop
```


This is not:

```
sage: timeit("z = ZZ(u)")
625 loops, best of 3: 37.9 µs per loop
```


Wow. See also #9885 for a not-quite-as-insane version of this.


Issue created by migration from https://trac.sagemath.org/ticket/9886





---

archive/issue_comments_097821.json:
```json
{
    "body": "The patch at #9887 should fix this, but it doesn't.  I'm not sure why.",
    "created_at": "2010-09-23T11:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9885#issuecomment-97821",
    "user": "https://github.com/roed314"
}
```

The patch at #9887 should fix this, but it doesn't.  I'm not sure why.



---

archive/issue_comments_097822.json:
```json
{
    "body": "I figured out why.  Hashing for R is slow, and ZZ._convert_map_hash needs to compute hash(R) to get the appropriate morphism.  See #10130 for a patch fixing this.",
    "created_at": "2010-10-15T07:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9885#issuecomment-97822",
    "user": "https://github.com/roed314"
}
```

I figured out why.  Hashing for R is slow, and ZZ._convert_map_hash needs to compute hash(R) to get the appropriate morphism.  See #10130 for a patch fixing this.



---

archive/issue_comments_097823.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-14T17:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9885#issuecomment-97823",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097824.json:
```json
{
    "body": "sage-6.2.beta4:\n\n```\nsage: sage: timeit(\"z = u.lift()\")\n625 loops, best of 3: 142 ns per loop\nsage: sage: timeit(\"z = ZZ(u)\")\n625 loops, best of 3: 280 ns per loop\n```\n",
    "created_at": "2014-03-14T17:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9885#issuecomment-97824",
    "user": "https://github.com/mezzarobba"
}
```

sage-6.2.beta4:

```
sage: sage: timeit("z = u.lift()")
625 loops, best of 3: 142 ns per loop
sage: sage: timeit("z = ZZ(u)")
625 loops, best of 3: 280 ns per loop
```




---

archive/issue_comments_097825.json:
```json
{
    "body": "Similar relative result here. (However, my times are 3x slower with 3GHz AMD Phenom, fascinating).",
    "created_at": "2014-03-24T16:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9885#issuecomment-97825",
    "user": "https://github.com/rwst"
}
```

Similar relative result here. (However, my times are 3x slower with 3GHz AMD Phenom, fascinating).



---

archive/issue_comments_097826.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-24T16:55:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9885#issuecomment-97826",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_010012.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-03-31T15:04:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9885",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9885#event-10012"
}
```



---

archive/issue_comments_097827.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-03-31T15:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9885",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9885#issuecomment-97827",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate
