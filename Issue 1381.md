# Issue 1381: optimized algorithm for some FractionField substitutions

archive/issues_001381.json:
```json
{
    "body": "Assignee: somebody\n\nFractionField substitutions can be quite painfully slow because they result in many many gcd computations.  Attached is a patch which does some book-keeping to alleviate this bottleneck.  The code of this patch needs to be hooked into the !__call!__ method of the FractionFieldElement and MPolynomial_elements (or whatever it is called).  I think it would also make sense for univariate Polynomial_element.\n\nSome benchmarks:\n\n```\nsage: R.<x,y,z>=QQ[]\nsage: f1=(x+y)/(x^2-z^2) # small fraction\nsage: f2=(x+y+z+x^2+y^2+z^2)/(x^2-z^2) \u00a0# bigger fraction\nsage: d1={x:z^2,y:x} \u00a0 \u00a0 # substitution of simple monomials\nsage: d2={x:z^-2,y:z/x} \u00a0# substitution of things in the fraction field\n**************\nsage: timeit f1.subs(d1)\n1000 loops, best of 3: 1.63 ms per loop\nsage: timeit fast_subst(f1,d1)\n1000 loops, best of 3: 528 \u00b5s per loop\n**************\nsage: timeit f2.subs(d1)\n100 loops, best of 3: 2.4 ms per loop\nsage: timeit fast_subst(f2,d1)\n1000 loops, best of 3: 681 \u00b5s per loop\n**************\nsage: timeit f1.subs(d2)\n100 loops, best of 3: 2.04 ms per loop\nsage: timeit fast_subst(f1,d2)\n1000 loops, best of 3: 635 \u00b5s per loop\n**************\nsage: timeit f2.subs(d2)\n100 loops, best of 3: 2.85 ms per loop\nsage: timeit fast_subst(f2,d2)\n1000 loops, best of 3: 834 \u00b5s per loop\n```\n\n\nNote that the book-keeping is mostly arrays of int exponents.  This indicates to me that a cython version of this might be much improved.\n\nI'll get around to integrating this patch myself sometime, but here it is if anyone really wants it sooner.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1381\n\n",
    "created_at": "2007-12-03T10:12:23Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "optimized algorithm for some FractionField substitutions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1381",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: somebody

FractionField substitutions can be quite painfully slow because they result in many many gcd computations.  Attached is a patch which does some book-keeping to alleviate this bottleneck.  The code of this patch needs to be hooked into the !__call!__ method of the FractionFieldElement and MPolynomial_elements (or whatever it is called).  I think it would also make sense for univariate Polynomial_element.

Some benchmarks:

```
sage: R.<x,y,z>=QQ[]
sage: f1=(x+y)/(x^2-z^2) # small fraction
sage: f2=(x+y+z+x^2+y^2+z^2)/(x^2-z^2)  # bigger fraction
sage: d1={x:z^2,y:x}     # substitution of simple monomials
sage: d2={x:z^-2,y:z/x}  # substitution of things in the fraction field
**************
sage: timeit f1.subs(d1)
1000 loops, best of 3: 1.63 ms per loop
sage: timeit fast_subst(f1,d1)
1000 loops, best of 3: 528 µs per loop
**************
sage: timeit f2.subs(d1)
100 loops, best of 3: 2.4 ms per loop
sage: timeit fast_subst(f2,d1)
1000 loops, best of 3: 681 µs per loop
**************
sage: timeit f1.subs(d2)
100 loops, best of 3: 2.04 ms per loop
sage: timeit fast_subst(f1,d2)
1000 loops, best of 3: 635 µs per loop
**************
sage: timeit f2.subs(d2)
100 loops, best of 3: 2.85 ms per loop
sage: timeit fast_subst(f2,d2)
1000 loops, best of 3: 834 µs per loop
```


Note that the book-keeping is mostly arrays of int exponents.  This indicates to me that a cython version of this might be much improved.

I'll get around to integrating this patch myself sometime, but here it is if anyone really wants it sooner.

Issue created by migration from https://trac.sagemath.org/ticket/1381





---

archive/issue_comments_008834.json:
```json
{
    "body": "Attachment [fast_subst.py](tarball://root/attachments/some-uuid/ticket1381/fast_subst.py) by jbmohler created at 2007-12-03 10:12:51\n\nfast_subst prototype",
    "created_at": "2007-12-03T10:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1381#issuecomment-8834",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [fast_subst.py](tarball://root/attachments/some-uuid/ticket1381/fast_subst.py) by jbmohler created at 2007-12-03 10:12:51

fast_subst prototype
