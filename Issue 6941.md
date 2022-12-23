# Issue 6941: GCD, XGCD for polynomial rings with templating

archive/issues_006941.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  rws jpflori\n\nGCD and XGCD methods should return *monic* greatest common divisors.  However, at the moment these two methods in the template file ``sage/rings/polynomial/polynomial_template.pxi`` prevent this by enforcing that ``gcd(a,0) == a`` and ``gcd(0,b) == b``.\n\nI suggest that the code for these two methods in the template file should only refer to the corresponding ``celement_foo`` methods of the actual implementation.  This way, all the logic is in the ``celement_foo`` methods, rather than being split between the two levels.\n\nThe patch for this should touch the template file as well as the two linkage files for GF2X and zmod polynomials.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6941\n\n",
    "created_at": "2009-09-15T22:39:51Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "title": "GCD, XGCD for polynomial rings with templating",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6941",
    "user": "spancratz"
}
```
Assignee: tbd

CC:  rws jpflori

GCD and XGCD methods should return *monic* greatest common divisors.  However, at the moment these two methods in the template file ``sage/rings/polynomial/polynomial_template.pxi`` prevent this by enforcing that ``gcd(a,0) == a`` and ``gcd(0,b) == b``.

I suggest that the code for these two methods in the template file should only refer to the corresponding ``celement_foo`` methods of the actual implementation.  This way, all the logic is in the ``celement_foo`` methods, rather than being split between the two levels.

The patch for this should touch the template file as well as the two linkage files for GF2X and zmod polynomials.

Issue created by migration from https://trac.sagemath.org/ticket/6941





---

archive/issue_comments_057386.json:
```json
{
    "body": "Attachment\n\nThe patch looks good, applies cleanly and doctests pass. However, do we really need to mimic the old behaviour?",
    "created_at": "2009-09-17T19:54:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6941#issuecomment-57386",
    "user": "malb"
}
```

Attachment

The patch looks good, applies cleanly and doctests pass. However, do we really need to mimic the old behaviour?



---

archive/issue_comments_057387.json:
```json
{
    "body": "Replying to [comment:1 malb]:\n> The patch looks good, applies cleanly and doctests pass. However, do we really need to mimic the old behaviour?\n\nI assume you are referring to the hyperelliptic curves part?  Yes, I think so.  Otherwise, some doctests fail.  I haven't tried to fully understand the mathematics of that part, but it seems to depend on the assumption gcd(a,0) == a.\n\nSebastian",
    "created_at": "2009-09-19T19:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6941#issuecomment-57387",
    "user": "spancratz"
}
```

Replying to [comment:1 malb]:
> The patch looks good, applies cleanly and doctests pass. However, do we really need to mimic the old behaviour?

I assume you are referring to the hyperelliptic curves part?  Yes, I think so.  Otherwise, some doctests fail.  I haven't tried to fully understand the mathematics of that part, but it seems to depend on the assumption gcd(a,0) == a.

Sebastian



---

archive/issue_comments_057388.json:
```json
{
    "body": "Maybe we can ask the person who wrote that code?",
    "created_at": "2009-09-29T08:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6941#issuecomment-57388",
    "user": "malb"
}
```

Maybe we can ask the person who wrote that code?



---

archive/issue_comments_057389.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-11-04T08:29:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6941#issuecomment-57389",
    "user": "mhansen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_057390.json:
```json
{
    "body": "If we need to mimic the old xgcd behavior, it would be much better to abstract that out into its own function with a docstring and some tests.",
    "created_at": "2010-05-27T22:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6941#issuecomment-57390",
    "user": "robertwb"
}
```

If we need to mimic the old xgcd behavior, it would be much better to abstract that out into its own function with a docstring and some tests.



---

archive/issue_comments_057391.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-05-27T22:04:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6941#issuecomment-57391",
    "user": "robertwb"
}
```

Changing status from needs_info to needs_work.
