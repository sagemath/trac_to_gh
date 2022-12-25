# Issue 6043: [with patch, positive review] optimize the construction of Lagrange interpolation polynomials

archive/issues_006043.json:
```json
{
    "body": "Assignee: tbd\n\nThe method `lagrange_polynomial()` in `sage/rings/polynomial/polynomial_ring.py` for generating the `n`-th Lagrange interpolation polynomial currently is a straightforward implementation that uses the definition of Lagrange interpolation polynomial. This is inefficient if one wants to use more interpolating points to generate a better Lagrange interpolation polynomial. To generate a better interpolation polynomial, the method currently would generate it from scratch. The patch `trac_6043.patch` adds two options to the method `lagrange_polynomial()`:\n* `algorithm` --- (default: divided_difference) If `algorithm=\"divided_difference\"`, then use the method of divided difference. If `algorithm=\"neville\"`, then use a variant of Neville's method to recursively generate the n-th Lagrange interpolation polynomial. This adaptation of Neville's method is more memory efficient than the original Neville's method, since the former doesn't generate the full Neville table resulting from Neville's recursive procedure. Instead the adaptation only keeps track of the current and previous rows of the said table. \n* `previous_row` --- (default: None) This is only relevant if used together with `algorithm=\"neville\"`. Here \"previous row\" refers to the last row in the Neville table that was obtained from a previous computation of an n-th Lagrange interpolation polynomial using Neville's method. If the last row is provided, then use a memory efficient variant of Neville's method to recursively generate a better interpolation polynomial from the results of previous computation.\nThe following are some timing statistics obtained using sage.math. When the results of previous computations are fed to `lagrange_polynomial` in order to produce better interpolation polynomials, we can gain an efficiency of up to 42%.\n\n```\n# BEFORE\n\n# using the definition of Lagrange interpolation polynomial\nsage: R = PolynomialRing(QQ, 'x')\nsage: %timeit R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])\n1000 loops, best of 3: 1.71 ms per loop\nsage: R = PolynomialRing(GF(2**3,'a'), 'x')\nsage: a = R.base_ring().gen()\nsage: timeit(\"R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])\")\n625 loops, best of 3: 233 \u00b5s per loop\n\n# without using precomputed values to generate successively better interpolation polynomials\n\nsage: R = PolynomialRing(QQ, 'x')\nsage: timeit(\"R.lagrange_polynomial([(0,1),(2,2)])\");\n625 loops, best of 3: 571 \u00b5s per loop\nsage: # add two more points\nsage: timeit(\"R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])\");\n125 loops, best of 3: 2.29 ms per loop\nsage: \nsage: R = PolynomialRing(GF(2**3,'a'), 'x')\nsage: a = R.base_ring().gen()\nsage: timeit(\"R.lagrange_polynomial([(a^2+a,a),(a,1)])\")\n625 loops, best of 3: 76.1 \u00b5s per loop\nsage: # add another point\nsage: timeit(\"R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])\")\n625 loops, best of 3: 229 \u00b5s per loop\nsage:\nsage: R = PolynomialRing(QQ, 'x')\nsage: points = [(random(), random()) for i in xrange(100)]\nsage: time R.lagrange_polynomial(points);\nCPU times: user 1.21 s, sys: 0.00 s, total: 1.21 s\nWall time: 1.21 s\nsage: # add three more points\nsage: for i in xrange(3): points.append((random(), random()))\n....: \nsage: time R.lagrange_polynomial(points);\nCPU times: user 1.28 s, sys: 0.01 s, total: 1.29 s\nWall time: 1.29 s\nsage: # add another 100 points\nsage: for i in xrange(100): points.append((random(), random()))\n....: \nsage: time R.lagrange_polynomial(points);\nCPU times: user 5.87 s, sys: 0.02 s, total: 5.89 s\nWall time: 5.89 s\n\n\n# AFTER\n\n# using the method of divided-difference\nsage: R = PolynomialRing(QQ, 'x')\nsage: %timeit R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])\n1000 loops, best of 3: 827 \u00b5s per loop\nsage: R = PolynomialRing(GF(2**3,'a'), 'x')\nsage: a = R.base_ring().gen()\nsage: timeit(\"R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])\")\n625 loops, best of 3: 111 \u00b5s per loop\n\n# using precomputed values to generate successively better interpolation polynomials\n\nsage: R = PolynomialRing(QQ, 'x')\nsage: timeit(\"R.lagrange_polynomial([(0,1),(2,2)], neville=True)\");\n625 loops, best of 3: 332 \u00b5s per loop\nsage: p = R.lagrange_polynomial([(0,1),(2,2)], neville=True);\nsage: # add two more points\nsage: timeit(\"R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)], neville=True, previous_row=p)\");\n625 loops, best of 3: 1.41 ms per loop\nsage:\nsage: R = PolynomialRing(GF(2**3,'a'), 'x')\nsage: a = R.base_ring().gen()\nsage: timeit(\"R.lagrange_polynomial([(a^2+a,a),(a,1)], neville=True)\");\n625 loops, best of 3: 36.4 \u00b5s per loop\nsage: p = R.lagrange_polynomial([(a^2+a,a),(a,1)], neville=True);\nsage: # add another point\nsage: timeit(\"R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)], neville=True, previous_row=p)\");\n625 loops, best of 3: 131 \u00b5s per loop\nsage:\nsage: R = PolynomialRing(QQ, 'x')\nsage: points = [(random(), random()) for i in xrange(100)]\nsage: time R.lagrange_polynomial(points, neville=True);\nCPU times: user 1.26 s, sys: 0.00 s, total: 1.26 s\nWall time: 1.26 s\nsage: p = R.lagrange_polynomial(points, neville=True);\nsage: # add three more points\nsage: for i in xrange(3): points.append((random(), random()))\n....: \nsage: time R.lagrange_polynomial(points, neville=True, previous_row=p);\nCPU times: user 0.09 s, sys: 0.00 s, total: 0.09 s\nWall time: 0.08 s\nsage: p = R.lagrange_polynomial(points, neville=True, previous_row=p)\nsage: # add another 100 points\nsage: for i in xrange(100): points.append((random(), random()))\n....: \nsage: time R.lagrange_polynomial(points, neville=True, previous_row=p);\nCPU times: user 4.62 s, sys: 0.00 s, total: 4.62 s\nWall time: 4.62 s\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6043\n\n",
    "closed_at": "2009-06-04T19:04:42Z",
    "created_at": "2009-05-15T08:38:40Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "[with patch, positive review] optimize the construction of Lagrange interpolation polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6043",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

The method `lagrange_polynomial()` in `sage/rings/polynomial/polynomial_ring.py` for generating the `n`-th Lagrange interpolation polynomial currently is a straightforward implementation that uses the definition of Lagrange interpolation polynomial. This is inefficient if one wants to use more interpolating points to generate a better Lagrange interpolation polynomial. To generate a better interpolation polynomial, the method currently would generate it from scratch. The patch `trac_6043.patch` adds two options to the method `lagrange_polynomial()`:
* `algorithm` --- (default: divided_difference) If `algorithm="divided_difference"`, then use the method of divided difference. If `algorithm="neville"`, then use a variant of Neville's method to recursively generate the n-th Lagrange interpolation polynomial. This adaptation of Neville's method is more memory efficient than the original Neville's method, since the former doesn't generate the full Neville table resulting from Neville's recursive procedure. Instead the adaptation only keeps track of the current and previous rows of the said table. 
* `previous_row` --- (default: None) This is only relevant if used together with `algorithm="neville"`. Here "previous row" refers to the last row in the Neville table that was obtained from a previous computation of an n-th Lagrange interpolation polynomial using Neville's method. If the last row is provided, then use a memory efficient variant of Neville's method to recursively generate a better interpolation polynomial from the results of previous computation.
The following are some timing statistics obtained using sage.math. When the results of previous computations are fed to `lagrange_polynomial` in order to produce better interpolation polynomials, we can gain an efficiency of up to 42%.

```
# BEFORE

# using the definition of Lagrange interpolation polynomial
sage: R = PolynomialRing(QQ, 'x')
sage: %timeit R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])
1000 loops, best of 3: 1.71 ms per loop
sage: R = PolynomialRing(GF(2**3,'a'), 'x')
sage: a = R.base_ring().gen()
sage: timeit("R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])")
625 loops, best of 3: 233 µs per loop

# without using precomputed values to generate successively better interpolation polynomials

sage: R = PolynomialRing(QQ, 'x')
sage: timeit("R.lagrange_polynomial([(0,1),(2,2)])");
625 loops, best of 3: 571 µs per loop
sage: # add two more points
sage: timeit("R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])");
125 loops, best of 3: 2.29 ms per loop
sage: 
sage: R = PolynomialRing(GF(2**3,'a'), 'x')
sage: a = R.base_ring().gen()
sage: timeit("R.lagrange_polynomial([(a^2+a,a),(a,1)])")
625 loops, best of 3: 76.1 µs per loop
sage: # add another point
sage: timeit("R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])")
625 loops, best of 3: 229 µs per loop
sage:
sage: R = PolynomialRing(QQ, 'x')
sage: points = [(random(), random()) for i in xrange(100)]
sage: time R.lagrange_polynomial(points);
CPU times: user 1.21 s, sys: 0.00 s, total: 1.21 s
Wall time: 1.21 s
sage: # add three more points
sage: for i in xrange(3): points.append((random(), random()))
....: 
sage: time R.lagrange_polynomial(points);
CPU times: user 1.28 s, sys: 0.01 s, total: 1.29 s
Wall time: 1.29 s
sage: # add another 100 points
sage: for i in xrange(100): points.append((random(), random()))
....: 
sage: time R.lagrange_polynomial(points);
CPU times: user 5.87 s, sys: 0.02 s, total: 5.89 s
Wall time: 5.89 s


# AFTER

# using the method of divided-difference
sage: R = PolynomialRing(QQ, 'x')
sage: %timeit R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)])
1000 loops, best of 3: 827 µs per loop
sage: R = PolynomialRing(GF(2**3,'a'), 'x')
sage: a = R.base_ring().gen()
sage: timeit("R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)])")
625 loops, best of 3: 111 µs per loop

# using precomputed values to generate successively better interpolation polynomials

sage: R = PolynomialRing(QQ, 'x')
sage: timeit("R.lagrange_polynomial([(0,1),(2,2)], neville=True)");
625 loops, best of 3: 332 µs per loop
sage: p = R.lagrange_polynomial([(0,1),(2,2)], neville=True);
sage: # add two more points
sage: timeit("R.lagrange_polynomial([(0,1),(2,2),(3,-2),(-4,9)], neville=True, previous_row=p)");
625 loops, best of 3: 1.41 ms per loop
sage:
sage: R = PolynomialRing(GF(2**3,'a'), 'x')
sage: a = R.base_ring().gen()
sage: timeit("R.lagrange_polynomial([(a^2+a,a),(a,1)], neville=True)");
625 loops, best of 3: 36.4 µs per loop
sage: p = R.lagrange_polynomial([(a^2+a,a),(a,1)], neville=True);
sage: # add another point
sage: timeit("R.lagrange_polynomial([(a^2+a,a),(a,1),(a^2,a^2+a+1)], neville=True, previous_row=p)");
625 loops, best of 3: 131 µs per loop
sage:
sage: R = PolynomialRing(QQ, 'x')
sage: points = [(random(), random()) for i in xrange(100)]
sage: time R.lagrange_polynomial(points, neville=True);
CPU times: user 1.26 s, sys: 0.00 s, total: 1.26 s
Wall time: 1.26 s
sage: p = R.lagrange_polynomial(points, neville=True);
sage: # add three more points
sage: for i in xrange(3): points.append((random(), random()))
....: 
sage: time R.lagrange_polynomial(points, neville=True, previous_row=p);
CPU times: user 0.09 s, sys: 0.00 s, total: 0.09 s
Wall time: 0.08 s
sage: p = R.lagrange_polynomial(points, neville=True, previous_row=p)
sage: # add another 100 points
sage: for i in xrange(100): points.append((random(), random()))
....: 
sage: time R.lagrange_polynomial(points, neville=True, previous_row=p);
CPU times: user 4.62 s, sys: 0.00 s, total: 4.62 s
Wall time: 4.62 s
```

Issue created by migration from https://trac.sagemath.org/ticket/6043





---

archive/issue_events_014192.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-15T09:06:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6043",
    "milestone": "sage-4.0.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6043#event-14192"
}
```



---

archive/issue_comments_048038.json:
```json
{
    "body": "based on Sage 4.0",
    "created_at": "2009-05-31T06:46:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6043#issuecomment-48038",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.0



---

archive/issue_comments_048039.json:
```json
{
    "body": "Attachment [trac_6043.patch](tarball://root/attachments/some-uuid/ticket6043/trac_6043.patch) by @mwhansen created at 2009-06-04 19:04:42\n\nLooks good to me.  Nice work!\n\nMerged in 4.0.1.rc1.",
    "created_at": "2009-06-04T19:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6043#issuecomment-48039",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6043.patch](tarball://root/attachments/some-uuid/ticket6043/trac_6043.patch) by @mwhansen created at 2009-06-04 19:04:42

Looks good to me.  Nice work!

Merged in 4.0.1.rc1.



---

archive/issue_events_014193.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T19:04:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6043",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6043#event-14193"
}
```



---

archive/issue_comments_048040.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T19:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6043#issuecomment-48040",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_048041.json:
```json
{
    "body": "I noticed some typos in the patch. This is addressed by #6221.",
    "created_at": "2009-06-05T05:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6043",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6043#issuecomment-48041",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I noticed some typos in the patch. This is addressed by #6221.
