# Issue 3057: MPolynomialRing_generic type-checks to determine commutativity

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-04-29 23:35:58

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



---

Attachment


---

Comment by was created at 2008-04-30 00:12:03

Looks good.


---

Comment by mabshoff created at 2008-04-30 01:47:49

Resolution: fixed


---

Comment by mabshoff created at 2008-04-30 01:47:49

Merged in Sage 3.0.1.alpha1
