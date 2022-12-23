# Issue 3354: Bug in power series sqrt

archive/issues_003354.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: t = QQ[['t']].0\nsage: sqrt(1+t)\n1 + 1/2*t - 1/8*t^2 + 1/16*t^3 - 5/128*t^4 + 7/256*t^5 - 21/1024*t^6 + 33/2048*t^7 - 429/32768*t^8 + 715/65536*t^9 - 2431/262144*t^10 + 4199/524288*t^11 - 29393/4194304*t^12 + 52003/8388608*t^13 - 185725/33554432*t^14 + 334305/67108864*t^15 - 9694845/2147483648*t^16 + 17678835/4294967296*t^17 - 64822395/17179869184*t^18 + 119409675/34359738368*t^19 + O(t^20)\nsage: sqrt(2+t)\n------------------------------------------------------------\nTraceback (most recent call last):\n  File \"<ipython console>\", line 1, in <module>\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 7664, in __call__\n    return x.sqrt(*args, **kwds)\n  File \"power_series_ring_element.pyx\", line 1120, in sage.rings.power_series_ring_element.PowerSeries.sqrt (sage/rings/power_series_ring_element.c:7887)\n<type 'exceptions.ValueError'>: power series does not have a square root since it has odd valuation.\n```\n\n\nPerhaps the error is just bad, but it should be able to compute this by extending to a field with  sqrt(2).\n\nIssue created by migration from https://trac.sagemath.org/ticket/3354\n\n",
    "created_at": "2008-06-03T02:16:22Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Bug in power series sqrt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3354",
    "user": "robertwb"
}
```
Assignee: somebody


```
sage: t = QQ[['t']].0
sage: sqrt(1+t)
1 + 1/2*t - 1/8*t^2 + 1/16*t^3 - 5/128*t^4 + 7/256*t^5 - 21/1024*t^6 + 33/2048*t^7 - 429/32768*t^8 + 715/65536*t^9 - 2431/262144*t^10 + 4199/524288*t^11 - 29393/4194304*t^12 + 52003/8388608*t^13 - 185725/33554432*t^14 + 334305/67108864*t^15 - 9694845/2147483648*t^16 + 17678835/4294967296*t^17 - 64822395/17179869184*t^18 + 119409675/34359738368*t^19 + O(t^20)
sage: sqrt(2+t)
------------------------------------------------------------
Traceback (most recent call last):
  File "<ipython console>", line 1, in <module>
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 7664, in __call__
    return x.sqrt(*args, **kwds)
  File "power_series_ring_element.pyx", line 1120, in sage.rings.power_series_ring_element.PowerSeries.sqrt (sage/rings/power_series_ring_element.c:7887)
<type 'exceptions.ValueError'>: power series does not have a square root since it has odd valuation.
```


Perhaps the error is just bad, but it should be able to compute this by extending to a field with  sqrt(2).

Issue created by migration from https://trac.sagemath.org/ticket/3354





---

archive/issue_comments_023314.json:
```json
{
    "body": "Related:\n\n\n```\n[00:12] <jason--> sage: t = QQ[['t']].0\n[00:12] <jason--> sage: 1/(1-t)\n[00:12] <jason--> 1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + t^10 + t^11 + t^12 + t^13 + t^14 + t^15 + t^16 + t^17 + t^18 + t^19 + O(t^20)\n[00:12] <jason--> but log(1+t) doesn't work, for example\n[00:12] <jason--> should it?\n[00:12] <craigcitro> in principle, yes. :)\n[00:13] <craigcitro> see if (1+t) has a log method ...\n[00:13] <jason--> and sin(t), cos(t), etc.\n[00:13] <jason--> so maybe a fallback method that calls for a taylor series?\n```\n",
    "created_at": "2008-11-14T06:17:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3354#issuecomment-23314",
    "user": "jason"
}
```

Related:


```
[00:12] <jason--> sage: t = QQ[['t']].0
[00:12] <jason--> sage: 1/(1-t)
[00:12] <jason--> 1 + t + t^2 + t^3 + t^4 + t^5 + t^6 + t^7 + t^8 + t^9 + t^10 + t^11 + t^12 + t^13 + t^14 + t^15 + t^16 + t^17 + t^18 + t^19 + O(t^20)
[00:12] <jason--> but log(1+t) doesn't work, for example
[00:12] <jason--> should it?
[00:12] <craigcitro> in principle, yes. :)
[00:13] <craigcitro> see if (1+t) has a log method ...
[00:13] <jason--> and sin(t), cos(t), etc.
[00:13] <jason--> so maybe a fallback method that calls for a taylor series?
```




---

archive/issue_comments_023315.json:
```json
{
    "body": "Changing keywords from \"\" to \"power series\".",
    "created_at": "2013-07-30T16:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3354#issuecomment-23315",
    "user": "chapoton"
}
```

Changing keywords from "" to "power series".



---

archive/issue_comments_023316.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-13T16:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3354#issuecomment-23316",
    "user": "mmezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_023317.json:
```json
{
    "body": "Message fixed in #6998.",
    "created_at": "2015-04-13T16:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3354#issuecomment-23317",
    "user": "mmezzarobba"
}
```

Message fixed in #6998.



---

archive/issue_comments_023318.json:
```json
{
    "body": "In the description there is\n\n```\nPerhaps the error is just bad, but it should be able\nto compute this by extending to a field with sqrt(2).\n```\n\nNote that the following works, but it is not very direct\n\n```\nsage: (2+t).change_ring(QuadraticField(2)).sqrt()\na + 1/4*a*t - 1/32*a*t^2 + 1/128*a*t^3 - ... + O(t^20)\n```\n",
    "created_at": "2015-04-24T21:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3354#issuecomment-23318",
    "user": "vdelecroix"
}
```

In the description there is

```
Perhaps the error is just bad, but it should be able
to compute this by extending to a field with sqrt(2).
```

Note that the following works, but it is not very direct

```
sage: (2+t).change_ring(QuadraticField(2)).sqrt()
a + 1/4*a*t - 1/32*a*t^2 + 1/128*a*t^3 - ... + O(t^20)
```




---

archive/issue_comments_023319.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2015-04-24T21:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3354#issuecomment-23319",
    "user": "vdelecroix"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_023320.json:
```json
{
    "body": "In the meantime the error changed to:\n\n```\n/home/ralf/sage/src/sage/rings/power_series_ring_element.pyx in sage.rings.power_series_ring_element.PowerSeries.sqrt (build/cythonized/sage/rings/power_series_ring_element.c:13321)()\n   1295                     return a\n   1296             elif formal_sqrt:\n-> 1297                 raise ValueError, \"unable to take the square root of %s\"%u[0]\n   1298             else:\n   1299                 raise ValueError, \"power series does not have a square root since it has odd valuation.\"\n\nValueError: unable to take the square root of 3\n```\n\nThere are also these keywords to consider. However `extend=True` returns not a square root of the series but the square root of the extension ring, and I am not sure what use it is, I think it's simply a bug:\n\n```\n          - ``extend`` - bool (default: False); if True, return a square\n            root in an extension ring, if necessary. Otherwise, raise\n            a ValueError if the square root is not in the base power series\n            ring. For example, if ``extend`` is True the square root of a\n            power series with odd degree leading coefficient is\n            defined as an element of a formal extension ring.\n\n          - ``name`` - string; if ``extend`` is True, you must also specify the     print\n            name of the formal square root.\n\nsage: K.<t> = PowerSeriesRing(QQ, 5)\nsage: two = K(2)\nsage: sqrt2 = two.sqrt(extend=True, name='sqrt2')       \nsage: (t+sqrt2^2).sqrt()\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n<ipython-input-9-0401d4729a88> in <module>()\n----> 1 (t+sqrt2**Integer(2)).sqrt()\n\n/home/ralf/sage/src/sage/structure/element.pyx in sage.structure.element.CommutativeRingElement.sqrt (build/cythonized/sage/structure/element.c:19922)()\n   2424         from sage.rings.integral_domain import is_IntegralDomain\n   2425         P=self._parent\n-> 2426         is_sqr, sq_rt = self.is_square( root = True )\n   2427         if is_sqr:\n   2428             if all:\n\n/home/ralf/sage/src/sage/structure/element.pyx in sage.structure.element.CommutativeRingElement.is_square (build/cythonized/sage/structure/element.c:19744)()\n   2328             framework.\n   2329         \"\"\"\n-> 2330         raise NotImplementedError(\"is_square() not implemented for elements of %s\" % self.parent())\n   2331\n   2332     def sqrt(self, extend=True, all=False, name=None):\n\nNotImplementedError: is_square() not implemented for elements of Univariate Quotient Polynomial Ring in sqrt2 over Power Series Ring in t over Rational Field with modulus x^2 - 2\n```\n\n\nSo effectively the original issue (giving a correct result for `(2+t).sqrt()` regardless of whether automagically or by giving the `extend` keyword) is not fixed.",
    "created_at": "2015-12-25T08:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3354#issuecomment-23320",
    "user": "rws"
}
```

In the meantime the error changed to:

```
/home/ralf/sage/src/sage/rings/power_series_ring_element.pyx in sage.rings.power_series_ring_element.PowerSeries.sqrt (build/cythonized/sage/rings/power_series_ring_element.c:13321)()
   1295                     return a
   1296             elif formal_sqrt:
-> 1297                 raise ValueError, "unable to take the square root of %s"%u[0]
   1298             else:
   1299                 raise ValueError, "power series does not have a square root since it has odd valuation."

ValueError: unable to take the square root of 3
```

There are also these keywords to consider. However `extend=True` returns not a square root of the series but the square root of the extension ring, and I am not sure what use it is, I think it's simply a bug:

```
          - ``extend`` - bool (default: False); if True, return a square
            root in an extension ring, if necessary. Otherwise, raise
            a ValueError if the square root is not in the base power series
            ring. For example, if ``extend`` is True the square root of a
            power series with odd degree leading coefficient is
            defined as an element of a formal extension ring.

          - ``name`` - string; if ``extend`` is True, you must also specify the     print
            name of the formal square root.

sage: K.<t> = PowerSeriesRing(QQ, 5)
sage: two = K(2)
sage: sqrt2 = two.sqrt(extend=True, name='sqrt2')       
sage: (t+sqrt2^2).sqrt()
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
<ipython-input-9-0401d4729a88> in <module>()
----> 1 (t+sqrt2**Integer(2)).sqrt()

/home/ralf/sage/src/sage/structure/element.pyx in sage.structure.element.CommutativeRingElement.sqrt (build/cythonized/sage/structure/element.c:19922)()
   2424         from sage.rings.integral_domain import is_IntegralDomain
   2425         P=self._parent
-> 2426         is_sqr, sq_rt = self.is_square( root = True )
   2427         if is_sqr:
   2428             if all:

/home/ralf/sage/src/sage/structure/element.pyx in sage.structure.element.CommutativeRingElement.is_square (build/cythonized/sage/structure/element.c:19744)()
   2328             framework.
   2329         """
-> 2330         raise NotImplementedError("is_square() not implemented for elements of %s" % self.parent())
   2331
   2332     def sqrt(self, extend=True, all=False, name=None):

NotImplementedError: is_square() not implemented for elements of Univariate Quotient Polynomial Ring in sqrt2 over Power Series Ring in t over Rational Field with modulus x^2 - 2
```


So effectively the original issue (giving a correct result for `(2+t).sqrt()` regardless of whether automagically or by giving the `extend` keyword) is not fixed.



---

archive/issue_comments_023321.json:
```json
{
    "body": "I also think the default of `extend` should be true and for square roots of integers `N` the name `sqrtN` provided. Only raise an error for nonintegers if no name is given.\n\nEDIT: typos",
    "created_at": "2015-12-25T08:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3354#issuecomment-23321",
    "user": "rws"
}
```

I also think the default of `extend` should be true and for square roots of integers `N` the name `sqrtN` provided. Only raise an error for nonintegers if no name is given.

EDIT: typos



---

archive/issue_comments_023322.json:
```json
{
    "body": "Changing component from basic arithmetic to commutative algebra.",
    "created_at": "2015-12-26T05:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3354#issuecomment-23322",
    "user": "rws"
}
```

Changing component from basic arithmetic to commutative algebra.



---

archive/issue_comments_023323.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2015-12-26T05:23:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3354",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3354#issuecomment-23323",
    "user": "rws"
}
```

Changing status from needs_info to needs_work.
