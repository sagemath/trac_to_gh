# Issue 59: optimize elliptic curve arithmetic

archive/issues_000059.json:
```json
{
    "body": "Assignee: somebody\n\nWilliam, my student noticed some slow performance with elliptic curves \ngroup law.  I think there was a huge overhead in duplication:\n \nsage: E = EllipticCurve([GF(101)(1),3])\nsage: P = E([-1,1,1])\nsage: timeit 2*P\n100 loops, best of 3: 3.81 ms per loop\nsage: timeit P+P\n1000 loops, best of 3: 1.81 ms per loop\n \nBasically n*P was passing through all sorts of high-level layers for \ngroup schemes, abelian groups, and the like.\n \nI've started teaching two courses here, and at the latest, will have to \nadapt to becoming a Dad next Tuesday (my wife Martine is overdue). But I \nmay be able to add some code in the next three weeks.\n \n\nIssue created by migration from https://trac.sagemath.org/ticket/59\n\n",
    "created_at": "2006-09-14T12:37:01Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.3",
    "title": "optimize elliptic curve arithmetic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/59",
    "user": "was"
}
```
Assignee: somebody

William, my student noticed some slow performance with elliptic curves 
group law.  I think there was a huge overhead in duplication:
 
sage: E = EllipticCurve([GF(101)(1),3])
sage: P = E([-1,1,1])
sage: timeit 2*P
100 loops, best of 3: 3.81 ms per loop
sage: timeit P+P
1000 loops, best of 3: 1.81 ms per loop
 
Basically n*P was passing through all sorts of high-level layers for 
group schemes, abelian groups, and the like.
 
I've started teaching two courses here, and at the latest, will have to 
adapt to becoming a Dad next Tuesday (my wife Martine is overdue). But I 
may be able to add some code in the next three weeks.
 

Issue created by migration from https://trac.sagemath.org/ticket/59





---

archive/issue_comments_000307.json:
```json
{
    "body": "This was from David Kohel.  Here's a better formated version:\n\nWilliam, my student noticed some slow performance with elliptic curves \ngroup law.  I think there was a huge overhead in duplication:\n\n``` \nsage: E = EllipticCurve([GF(101)(1),3])\nsage: P = E([-1,1,1])\nsage: timeit 2*P\n100 loops, best of 3: 3.81 ms per loop\nsage: timeit P+P\n1000 loops, best of 3: 1.81 ms per loop\n }}}\nBasically n*P was passing through all sorts of high-level layers for \ngroup schemes, abelian groups, and the like.",
    "created_at": "2006-09-14T12:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/59",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/59#issuecomment-307",
    "user": "was"
}
```

This was from David Kohel.  Here's a better formated version:

William, my student noticed some slow performance with elliptic curves 
group law.  I think there was a huge overhead in duplication:

``` 
sage: E = EllipticCurve([GF(101)(1),3])
sage: P = E([-1,1,1])
sage: timeit 2*P
100 loops, best of 3: 3.81 ms per loop
sage: timeit P+P
1000 loops, best of 3: 1.81 ms per loop
 }}}
Basically n*P was passing through all sorts of high-level layers for 
group schemes, abelian groups, and the like.



---

archive/issue_comments_000308.json:
```json
{
    "body": "I guess this has been fixed. With Sage 2.8.2 I get:\n\n```\nsage: E = EllipticCurve([GF(101)(1),3])\nsage: P = E([-1,1,1])\nsage: timeit 2*P\n1000 loops, best of 3: 317 \u00b5s per loop\nsage: timeit P+P\n10000 loops, best of 3: 92.7 \u00b5s per loop\n```\n\nCheers,\n\nMichael",
    "created_at": "2007-08-22T19:46:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/59",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/59#issuecomment-308",
    "user": "mabshoff"
}
```

I guess this has been fixed. With Sage 2.8.2 I get:

```
sage: E = EllipticCurve([GF(101)(1),3])
sage: P = E([-1,1,1])
sage: timeit 2*P
1000 loops, best of 3: 317 µs per loop
sage: timeit P+P
10000 loops, best of 3: 92.7 µs per loop
```

Cheers,

Michael



---

archive/issue_comments_000309.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-23T05:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/59",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/59#issuecomment-309",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000310.json:
```json
{
    "body": "Fixed by Robert bradshaw.",
    "created_at": "2007-08-23T05:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/59",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/59#issuecomment-310",
    "user": "was"
}
```

Fixed by Robert bradshaw.



---

archive/issue_comments_000311.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2007-08-24T06:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/59",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/59#issuecomment-311",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_000312.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-08-24T06:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/59",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/59#issuecomment-312",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_000313.json:
```json
{
    "body": "Ok, reopened.\n\nFor details see http://groups.google.com/group/sage-devel/t/e884bb605728649a\n\nTo quote David Kohel:\n\n```\nI think the problem needs to be profiled.  The problem is likely NOT\nin elliptic curves, but some\nhorrendous chain of calls to module operations before getting to the\n(same) actual algorithms.\nNote that P*2 is slightly faster since it calls directly the member\nfunction of P rather than a\nfunction on integers.\n\nsage: E = EllipticCurve([GF(101)(1),3])\nsage: P = E([-1,1,1])\nsage: timeit 2*P\n1000 loops, best of 3: 309 \u00b5s per loop\nsage: timeit P+P\n10000 loops, best of 3: 89.8 \u00b5s per loop\nsage: timeit P*2\n1000 loops, best of 3: 204 \u00b5s per loop\n\nYes, reopen it: these sorts of problems need to be looked at and\noptimized.  The same problem\napplies to points on Jacobians (compare 2*P, P*2, and P+P).\n\n--David \n```\n",
    "created_at": "2007-08-24T06:55:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/59",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/59#issuecomment-313",
    "user": "mabshoff"
}
```

Ok, reopened.

For details see http://groups.google.com/group/sage-devel/t/e884bb605728649a

To quote David Kohel:

```
I think the problem needs to be profiled.  The problem is likely NOT
in elliptic curves, but some
horrendous chain of calls to module operations before getting to the
(same) actual algorithms.
Note that P*2 is slightly faster since it calls directly the member
function of P rather than a
function on integers.

sage: E = EllipticCurve([GF(101)(1),3])
sage: P = E([-1,1,1])
sage: timeit 2*P
1000 loops, best of 3: 309 µs per loop
sage: timeit P+P
10000 loops, best of 3: 89.8 µs per loop
sage: timeit P*2
1000 loops, best of 3: 204 µs per loop

Yes, reopen it: these sorts of problems need to be looked at and
optimized.  The same problem
applies to points on Jacobians (compare 2*P, P*2, and P+P).

--David 
```




---

archive/issue_comments_000314.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-29T02:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/59",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/59#issuecomment-314",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000315.json:
```json
{
    "body": "As of SAGE-2.8.3 (probably due to Tom Boothby's work), this is now resolved:\n\n```\nsage: E = EllipticCurve([GF(101)(1),3])\nsage: P = E([-1,1,1])\nsage: import timeit\nsage: t = timeit.Timer('2*P', 'from sage.all import EllipticCurve, GF; E = EllipticCurve([GF(101)(1),3]); P = E([-1,1,1])')\nsage: t.timeit(10000)\n1.0524919033050537\nsage: s = timeit.Timer('P+P', 'from sage.all import EllipticCurve, GF; E = EllipticCurve([GF(101)(1),3]); P = E([-1,1,1])')\nsage: s.timeit(10000)\n1.067209005355835\n```\n",
    "created_at": "2007-08-29T02:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/59",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/59#issuecomment-315",
    "user": "was"
}
```

As of SAGE-2.8.3 (probably due to Tom Boothby's work), this is now resolved:

```
sage: E = EllipticCurve([GF(101)(1),3])
sage: P = E([-1,1,1])
sage: import timeit
sage: t = timeit.Timer('2*P', 'from sage.all import EllipticCurve, GF; E = EllipticCurve([GF(101)(1),3]); P = E([-1,1,1])')
sage: t.timeit(10000)
1.0524919033050537
sage: s = timeit.Timer('P+P', 'from sage.all import EllipticCurve, GF; E = EllipticCurve([GF(101)(1),3]); P = E([-1,1,1])')
sage: s.timeit(10000)
1.067209005355835
```

