# Issue 3057: MPolynomialRing_generic type-checks to determine commutativity

archive/issues_003057.json:
```json
{
    "body": "Assignee: tbd\n\nCreate a ring R which is commutative, but does not inherit from CommutativeRing.  That ring cannot be the base ring for an MPolynomialRing.  Rather than type-checking for CommutativeRing, this should call R.is_commutative().\n\n```\nsage: class CR(Ring):\n....:     def is_commutative(self):\n....:         return True\n....:\nsage: R = CR(None)\nsage: R['x,y']\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/boothby/<ipython console> in <module>()\n\n/home/boothby/ring.pyx in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:1672)()\n\n/home/boothby/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name)\n    261             names = arg1.split(',')\n    262             n = len(names)\n--> 263             R = _multi_variate(base_ring, names, n, sparse, order)\n    264     elif isinstance(arg1, (list, tuple)):\n    265             # PolynomialRing(base_ring, names (list or tuple), order='degrevlex'):\n\n/home/boothby/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py in _multi_variate(base_ring, names, n, sparse, order)\n    370                 R = m.MPolynomialRing_polydict_domain(base_ring, n, names, order)\n    371     else:\n--> 372         R = m.MPolynomialRing_polydict(base_ring, n, names, order)\n    373\n    374     _save_in_cache(key, R)\n\n/home/boothby/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring.py in __init__(self, base_ring, n, names, order)\n    131     def __init__(self, base_ring, n, names, order):\n    132         order = TermOrder(order,n)\n--> 133         MPolynomialRing_generic.__init__(self, base_ring, n, names, order)\n    134         # Construct the generators\n    135         v = [0 for _ in xrange(n)]\n\n/home/boothby/multi_polynomial_ring_generic.pyx in sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic.__init__ (sage/rings/polynomial/multi_polynomial_ring_generic.c:830)()\n\n<type 'exceptions.TypeError'>: Base ring must be a commutative ring.\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3057\n\n",
    "created_at": "2008-04-29T23:35:58Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "MPolynomialRing_generic type-checks to determine commutativity",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3057",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: tbd

Create a ring R which is commutative, but does not inherit from CommutativeRing.  That ring cannot be the base ring for an MPolynomialRing.  Rather than type-checking for CommutativeRing, this should call R.is_commutative().

```
sage: class CR(Ring):
....:     def is_commutative(self):
....:         return True
....:
sage: R = CR(None)
sage: R['x,y']
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/boothby/<ipython console> in <module>()

/home/boothby/ring.pyx in sage.rings.ring.Ring.__getitem__ (sage/rings/ring.c:1672)()

/home/boothby/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py in PolynomialRing(base_ring, arg1, arg2, sparse, order, names, name)
    261             names = arg1.split(',')
    262             n = len(names)
--> 263             R = _multi_variate(base_ring, names, n, sparse, order)
    264     elif isinstance(arg1, (list, tuple)):
    265             # PolynomialRing(base_ring, names (list or tuple), order='degrevlex'):

/home/boothby/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring_constructor.py in _multi_variate(base_ring, names, n, sparse, order)
    370                 R = m.MPolynomialRing_polydict_domain(base_ring, n, names, order)
    371     else:
--> 372         R = m.MPolynomialRing_polydict(base_ring, n, names, order)
    373
    374     _save_in_cache(key, R)

/home/boothby/sage/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ring.py in __init__(self, base_ring, n, names, order)
    131     def __init__(self, base_ring, n, names, order):
    132         order = TermOrder(order,n)
--> 133         MPolynomialRing_generic.__init__(self, base_ring, n, names, order)
    134         # Construct the generators
    135         v = [0 for _ in xrange(n)]

/home/boothby/multi_polynomial_ring_generic.pyx in sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic.__init__ (sage/rings/polynomial/multi_polynomial_ring_generic.c:830)()

<type 'exceptions.TypeError'>: Base ring must be a commutative ring.
```

Issue created by migration from https://trac.sagemath.org/ticket/3057





---

archive/issue_comments_021067.json:
```json
{
    "body": "Attachment [sage-3057.patch](tarball://root/attachments/some-uuid/ticket3057/sage-3057.patch) by boothby created at 2008-04-30 00:01:38",
    "created_at": "2008-04-30T00:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3057#issuecomment-21067",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [sage-3057.patch](tarball://root/attachments/some-uuid/ticket3057/sage-3057.patch) by boothby created at 2008-04-30 00:01:38



---

archive/issue_comments_021068.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-04-30T00:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3057#issuecomment-21068",
    "user": "https://github.com/williamstein"
}
```

Looks good.



---

archive/issue_events_006924.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-04-30T00:12:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3057",
    "milestone": "sage-3.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3057#event-6924"
}
```



---

archive/issue_comments_021069.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-30T01:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3057#issuecomment-21069",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006925.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-30T01:47:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3057",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3057#event-6925"
}
```



---

archive/issue_comments_021070.json:
```json
{
    "body": "Merged in Sage 3.0.1.alpha1",
    "created_at": "2008-04-30T01:47:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3057",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3057#issuecomment-21070",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.1.alpha1
