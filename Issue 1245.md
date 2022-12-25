# Issue 1245: Error coercing multivariate polynomial rings with one variable into composite integer rings

archive/issues_001245.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb\n\nKeywords: coercion coerce multivariate univariate composite\n\nThis works:\n\n\n```\nsage: PolynomialRing(ZZ, 2, 'x').gen() * Mod(1, 9)\nx0\nsage: PolynomialRing(ZZ, 2, 'x').gen() * Mod(1, 3)\nx0\n```\n\n\nThis doesn't:\n\n\n```\nsage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 3)\nx\nsage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 9)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/ncalexan/<ipython console> in <module>()\n\n/Users/ncalexan/element.pyx in sage.structure.element.RingElement.__mul__()\n\n/Users/ncalexan/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()\n\n<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Multivariate Polynomial Ring in x over Integer Ring' and 'Ring of integers modulo 9'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1245\n\n",
    "created_at": "2007-11-22T23:57:05Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.4",
    "title": "Error coercing multivariate polynomial rings with one variable into composite integer rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1245",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @williamstein

CC:  @robertwb

Keywords: coercion coerce multivariate univariate composite

This works:


```
sage: PolynomialRing(ZZ, 2, 'x').gen() * Mod(1, 9)
x0
sage: PolynomialRing(ZZ, 2, 'x').gen() * Mod(1, 3)
x0
```


This doesn't:


```
sage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 3)
x
sage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 9)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/ncalexan/<ipython console> in <module>()

/Users/ncalexan/element.pyx in sage.structure.element.RingElement.__mul__()

/Users/ncalexan/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '*': 'Multivariate Polynomial Ring in x over Integer Ring' and 'Ring of integers modulo 9'
```


Issue created by migration from https://trac.sagemath.org/ticket/1245





---

archive/issue_events_003291.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-20T03:02:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1245#event-3291"
}
```



---

archive/issue_comments_007777.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2007-12-20T03:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1245#issuecomment-7777",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_007778.json:
```json
{
    "body": "This is still a problem with Sage 2.10.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-20T03:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1245#issuecomment-7778",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still a problem with Sage 2.10.

Cheers,

Michael



---

archive/issue_comments_007779.json:
```json
{
    "body": "Changing component from algebraic geometry to commutative algebra.",
    "created_at": "2008-01-24T09:00:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1245#issuecomment-7779",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebraic geometry to commutative algebra.



---

archive/issue_comments_007780.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2008-02-15T23:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1245#issuecomment-7780",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_007781.json:
```json
{
    "body": "Still an issue with Sage 2.10.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-15T23:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1245#issuecomment-7781",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Still an issue with Sage 2.10.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_007782.json:
```json
{
    "body": "I'm stuck with this bug, I don't know where to look. Robert, can you take a look?",
    "created_at": "2008-08-18T11:13:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1245#issuecomment-7782",
    "user": "https://github.com/malb"
}
```

I'm stuck with this bug, I don't know where to look. Robert, can you take a look?



---

archive/issue_events_003292.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-11-14T09:41:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1245#event-3292"
}
```



---

archive/issue_comments_007783.json:
```json
{
    "body": "This has been fixed in at least Sage 3.1.4\n\n\n```\nsage: sage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 3)\nx\nsage: sage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 9)\nx\nsage: _.parent()\nUnivariate Polynomial Ring in x over Ring of integers modulo 9\n```\n",
    "created_at": "2008-11-14T09:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1245#issuecomment-7783",
    "user": "https://github.com/mwhansen"
}
```

This has been fixed in at least Sage 3.1.4


```
sage: sage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 3)
x
sage: sage: PolynomialRing(ZZ, 1, 'x').gen() * Mod(1, 9)
x
sage: _.parent()
Univariate Polynomial Ring in x over Ring of integers modulo 9
```




---

archive/issue_comments_007784.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-14T09:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1245#issuecomment-7784",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_003293.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-11-14T09:41:04Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1245#event-3293"
}
```



---

archive/issue_events_003294.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2008-11-14T09:41:04Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1245",
    "milestone": "sage-3.1.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1245#event-3294"
}
```
