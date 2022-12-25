# Issue 4965: [with patch, needs work] Z/nZ[x] via FLINT's zmod_poly

archive/issues_004965.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @burcin @williamstein\n\nThe attached patches wrap FLINT's Z/nZ[x] for word sized n. This provides a considerable speed-up (~ 20x) for univariate polynomial arithmetic over these rings and also cleans up the code using the `polynomial_template.pxi` mechanism. For that `polynomial_template.pxi` was also cleaned-up which should make it more suitable for other backend implementations.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4965\n\n",
    "created_at": "2009-01-11T22:03:25Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, needs work] Z/nZ[x] via FLINT's zmod_poly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4965",
    "user": "https://github.com/malb"
}
```
Assignee: somebody

CC:  @burcin @williamstein

The attached patches wrap FLINT's Z/nZ[x] for word sized n. This provides a considerable speed-up (~ 20x) for univariate polynomial arithmetic over these rings and also cleans up the code using the `polynomial_template.pxi` mechanism. For that `polynomial_template.pxi` was also cleaned-up which should make it more suitable for other backend implementations.

Issue created by migration from https://trac.sagemath.org/ticket/4965





---

archive/issue_comments_037674.json:
```json
{
    "body": "apply this first",
    "created_at": "2009-01-11T22:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37674",
    "user": "https://github.com/malb"
}
```

apply this first



---

archive/issue_comments_037675.json:
```json
{
    "body": "Attachment [polynomial_template.patch](tarball://root/attachments/some-uuid/ticket4965/polynomial_template.patch) by @malb created at 2009-01-11 22:06:12\n\n## Speed-Up on sage.math\n\n### Old\n\n\n```\nsage: P.<x> = PolynomialRing(GF(7))\nsage: type(x)\n<type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>\nsage: f = P.random_element(100)\nsage: g = P.random_element(100)\nsage: %timeit f*g\n1000 loops, best of 3: 445 \u00b5s per loop\n```\n\n\n### New\n\n\n```\nsage: P.<x> = PolynomialRing(GF(7))\nsage: type(x)\n<type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>\nsage: f = P.random_element(100)\nsage: g = P.random_element(100)\nsage: %timeit f*g\n100000 loops, best of 3: 7.92 \u00b5s per loop\n```\n",
    "created_at": "2009-01-11T22:06:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37675",
    "user": "https://github.com/malb"
}
```

Attachment [polynomial_template.patch](tarball://root/attachments/some-uuid/ticket4965/polynomial_template.patch) by @malb created at 2009-01-11 22:06:12

## Speed-Up on sage.math

### Old


```
sage: P.<x> = PolynomialRing(GF(7))
sage: type(x)
<type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
sage: f = P.random_element(100)
sage: g = P.random_element(100)
sage: %timeit f*g
1000 loops, best of 3: 445 µs per loop
```


### New


```
sage: P.<x> = PolynomialRing(GF(7))
sage: type(x)
<type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
sage: f = P.random_element(100)
sage: g = P.random_element(100)
sage: %timeit f*g
100000 loops, best of 3: 7.92 µs per loop
```




---

archive/issue_comments_037676.json:
```json
{
    "body": "At least these two doctests fail.\n\n\n```\nsage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\"\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\"\n```\n\n\nI would greatly appreciate input/pointers where to look for the bug. Once I figured out which of the functions I've touched returns wrong/unexpected answers, I can fix it. However, as of now, I don't know which one it is.",
    "created_at": "2009-01-11T22:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37676",
    "user": "https://github.com/malb"
}
```

At least these two doctests fail.


```
sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py"
```


I would greatly appreciate input/pointers where to look for the bug. Once I figured out which of the functions I've touched returns wrong/unexpected answers, I can fix it. However, as of now, I don't know which one it is.



---

archive/issue_comments_037677.json:
```json
{
    "body": "More details:\n\n\n```\nsage -t  \".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\"\n**********************************************************************\nFile \".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\", line 198:\n    sage: w.coleman_integral(P, Q)\nExpected:\n    O(11^6)\nGot:\n    6 + 7*11 + 8*11^2 + 7*11^3 + 3*11^4 + 10*11^5 + O(11^6)\n**********************************************************************\nFile \".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\", line 200:\n    sage: C.coleman_integral(x*w, P, Q)\nExpected:\n    O(11^6)\nGot:\n    3 + 11 + 6*11^2 + 2*11^3 + 8*11^5 + O(11^6)\n**********************************************************************\nFile \".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\", line 202:\n    sage: C.coleman_integral(x^2*w, P, Q)\nExpected:\n    3*11 + 2*11^2 + 7*11^3 + 2*11^4 + 10*11^5 + O(11^6)\nGot:\n    5 + 11 + 8*11^2 + 11^3 + 7*11^4 + 6*11^5 + O(11^6)\n**********************************************************************\nFile \".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\", line 213:\n    sage: w.integrate(P, Q), (x*w).integrate(P, Q)\nExpected:\n    (O(71^4), O(71^4))\nGot:\n    (40 + 4*71 + 21*71^2 + 39*71^3 + O(71^4), 2 + 58*71 + 27*71^2 + 49*71^3 + O(71^4))\n**********************************************************************\nFile \".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\", line 216:\n    sage: w.integrate(P, R)\nExpected:\n    42*71 + 63*71^2 + 55*71^3 + O(71^4)\nGot:\n    14 + 27*71 + 46*71^2 + 10*71^3 + O(71^4)\n```\n",
    "created_at": "2009-01-11T22:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37677",
    "user": "https://github.com/malb"
}
```

More details:


```
sage -t  ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 198:
    sage: w.coleman_integral(P, Q)
Expected:
    O(11^6)
Got:
    6 + 7*11 + 8*11^2 + 7*11^3 + 3*11^4 + 10*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 200:
    sage: C.coleman_integral(x*w, P, Q)
Expected:
    O(11^6)
Got:
    3 + 11 + 6*11^2 + 2*11^3 + 8*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 202:
    sage: C.coleman_integral(x^2*w, P, Q)
Expected:
    3*11 + 2*11^2 + 7*11^3 + 2*11^4 + 10*11^5 + O(11^6)
Got:
    5 + 11 + 8*11^2 + 11^3 + 7*11^4 + 6*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 213:
    sage: w.integrate(P, Q), (x*w).integrate(P, Q)
Expected:
    (O(71^4), O(71^4))
Got:
    (40 + 4*71 + 21*71^2 + 39*71^3 + O(71^4), 2 + 58*71 + 27*71^2 + 49*71^3 + O(71^4))
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 216:
    sage: w.integrate(P, R)
Expected:
    42*71 + 63*71^2 + 55*71^3 + O(71^4)
Got:
    14 + 27*71 + 46*71^2 + 10*71^3 + O(71^4)
```




---

archive/issue_comments_037678.json:
```json
{
    "body": "\n```\nFile \".../sage/schemes/elliptic_curves/ell_number_field.py\", line 728:\n    sage: EllipticCurve([1 + a , -1 + a , 1 + a , -11 + a , 5 -9*a  ]).conductor()\nException raised:\n    Traceback (most recent call last):\n      File \".../sage/schemes/elliptic_curves/ell_number_field.py\", line 747, in conductor\n        for d in self.local_data()],\\\n      File \".../sage/schemes/elliptic_curves/ell_number_field.py\", line 396, in local_data\n        return [self._get_local_data(pr, proof) for pr in primes]\n      File \".../sage/schemes/elliptic_curves/ell_number_field.py\", line 418, in _get_local_data\n        self._local_data[P] = EllipticCurveLocalData(self, P, proof)\n      File \".../schemes/elliptic_curves/ell_local_data.py\", line 140, in __init__\n        self._Emin, ch, self._val_disc, self._fp, self._KS, self._cp, self._split = self._tate(proof)\n      File \".../sage/schemes/elliptic_curves/ell_local_data.py\", line 520, in _tate\n        r = proot(-b6, 3)\n      File \".../sage/schemes/elliptic_curves/ell_local_data.py\", line 451, in <lambda>\n        proot = lambda x,e: F.lift(F(x).nth_root(e, extend = False, all = True)[0])\n      File \"integer_mod.pyx\", line 855, in sage.rings.integer_mod.IntegerMod_abstract.nth_root (sage/rings/integer_mod.c:7712)\n      File \"polynomial_element.pyx\", line 3715, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:24924)\n      File \"polynomial_element.pyx\", line 2096, in sage.rings.polynomial.polynomial_element.Polynomial.factor (sage/rings/polynomial/polynomial_element.c:15667)\n    ValueError: factorization of 0 not defined\n```\n",
    "created_at": "2009-01-11T22:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37678",
    "user": "https://github.com/malb"
}
```


```
File ".../sage/schemes/elliptic_curves/ell_number_field.py", line 728:
    sage: EllipticCurve([1 + a , -1 + a , 1 + a , -11 + a , 5 -9*a  ]).conductor()
Exception raised:
    Traceback (most recent call last):
      File ".../sage/schemes/elliptic_curves/ell_number_field.py", line 747, in conductor
        for d in self.local_data()],\
      File ".../sage/schemes/elliptic_curves/ell_number_field.py", line 396, in local_data
        return [self._get_local_data(pr, proof) for pr in primes]
      File ".../sage/schemes/elliptic_curves/ell_number_field.py", line 418, in _get_local_data
        self._local_data[P] = EllipticCurveLocalData(self, P, proof)
      File ".../schemes/elliptic_curves/ell_local_data.py", line 140, in __init__
        self._Emin, ch, self._val_disc, self._fp, self._KS, self._cp, self._split = self._tate(proof)
      File ".../sage/schemes/elliptic_curves/ell_local_data.py", line 520, in _tate
        r = proot(-b6, 3)
      File ".../sage/schemes/elliptic_curves/ell_local_data.py", line 451, in <lambda>
        proot = lambda x,e: F.lift(F(x).nth_root(e, extend = False, all = True)[0])
      File "integer_mod.pyx", line 855, in sage.rings.integer_mod.IntegerMod_abstract.nth_root (sage/rings/integer_mod.c:7712)
      File "polynomial_element.pyx", line 3715, in sage.rings.polynomial.polynomial_element.Polynomial.roots (sage/rings/polynomial/polynomial_element.c:24924)
      File "polynomial_element.pyx", line 2096, in sage.rings.polynomial.polynomial_element.Polynomial.factor (sage/rings/polynomial/polynomial_element.c:15667)
    ValueError: factorization of 0 not defined
```




---

archive/issue_comments_037679.json:
```json
{
    "body": "I'll try to look at the second of those since it seems to crop up in code which I wrote.  But I em extremely busy at the moment so cannot promise anything very quickly.",
    "created_at": "2009-01-11T22:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37679",
    "user": "https://github.com/JohnCremona"
}
```

I'll try to look at the second of those since it seems to crop up in code which I wrote.  But I em extremely busy at the moment so cannot promise anything very quickly.



---

archive/issue_comments_037680.json:
```json
{
    "body": "Replying to [comment:5 cremona]:\n> I'll try to look at the second of those since it seems to crop up in code which I wrote.  But I em extremely busy at the moment so cannot promise anything very quickly.\n\nThanks!",
    "created_at": "2009-01-11T22:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37680",
    "user": "https://github.com/malb"
}
```

Replying to [comment:5 cremona]:
> I'll try to look at the second of those since it seems to crop up in code which I wrote.  But I em extremely busy at the moment so cannot promise anything very quickly.

Thanks!



---

archive/issue_comments_037681.json:
```json
{
    "body": "The updated patch\n* addresses a couple of remarks by Bill Hart off-list\n* changes the celement definition (following Burcin's alternative implementation)\n\nBurcin also wrapped `zmod_poly_t` two months ago and our patches match a lot. Thus, copyright should be shared. The only reason I'm using my patches as a basis is because I know them better. Btw. Burcin's patches rearrange a fair amount of stuff in `polynomial_ring.pyx` which I don't. He also splits the `polynomial_template.pxi` in `polynomial_template.pxi` and `polynomial_template_field.pxi`.",
    "created_at": "2009-01-12T12:25:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37681",
    "user": "https://github.com/malb"
}
```

The updated patch
* addresses a couple of remarks by Bill Hart off-list
* changes the celement definition (following Burcin's alternative implementation)

Burcin also wrapped `zmod_poly_t` two months ago and our patches match a lot. Thus, copyright should be shared. The only reason I'm using my patches as a basis is because I know them better. Btw. Burcin's patches rearrange a fair amount of stuff in `polynomial_ring.pyx` which I don't. He also splits the `polynomial_template.pxi` in `polynomial_template.pxi` and `polynomial_template_field.pxi`.



---

archive/issue_comments_037682.json:
```json
{
    "body": "## \"Long\" Doctest Failures\n\nthis one is easy:\n\n\n```\nsage -t --long \"devel/sage/sage/schemes/elliptic_curves/padics.py\"\n...\nsage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint._derivative \n...\nsage.libs.ntl.ntl_lzz_pContext.ntl_zz_pContext     ValueError: Modulus (=2384185791015625) is too big\n```\n\n\n\n```\nFile \".../sage/schemes/elliptic_curves/ell_number_field.py\", line 728:\n    sage: EllipticCurve([1 + a , -1 + a , 1 + a , -11 + a , 5 -9*a  ]).conductor()\n...\n    ValueError: factorization of 0 not defined\n```\n\n\n\n```\nsage -t --long \"devel/sage/sage/schemes/elliptic_curves/sha_tate.py\"\n...\n    sage: EllipticCurve('858k2').sha().an_padic(7)  #rank 0, non trivial sha  (long\n...\nsage.libs.ntl.ntl_lzz_pContext.ntl_zz_pContext     ValueError: Modulus (=558545864083284007) is too big\n```\n\n\n\n```\nsage -t --long \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\"\n**********************************************************************\n    sage: w.coleman_integral(P, Q)\nExpected:\n    O(11^6)\nGot:\n    6 + 7*11 + 8*11^2 + 7*11^3 + 3*11^4 + 10*11^5 + O(11^6)\n**********************************************************************\n    sage: C.coleman_integral(x*w, P, Q)\nExpected:\n    O(11^6)\nGot:\n    3 + 11 + 6*11^2 + 2*11^3 + 8*11^5 + O(11^6)\n**********************************************************************\n    sage: C.coleman_integral(x^2*w, P, Q)\nExpected:\n    3*11 + 2*11^2 + 7*11^3 + 2*11^4 + 10*11^5 + O(11^6)\nGot:\n    5 + 11 + 8*11^2 + 11^3 + 7*11^4 + 6*11^5 + O(11^6)\n**********************************************************************\n    sage: w.integrate(P, Q), (x*w).integrate(P, Q)\nExpected:\n    (O(71^4), O(71^4))\nGot:\n    (40 + 4*71 + 21*71^2 + 39*71^3 + O(71^4), 2 + 58*71 + 27*71^2 + 49*71^3 + O(71^4))\n**********************************************************************\n    sage: w.integrate(P, R)\nExpected:\n    42*71 + 63*71^2 + 55*71^3 + O(71^4)\nGot:\n    14 + 27*71 + 46*71^2 + 10*71^3 + O(71^4)\n**********************************************************************\n```\n",
    "created_at": "2009-01-12T12:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37682",
    "user": "https://github.com/malb"
}
```

## "Long" Doctest Failures

this one is easy:


```
sage -t --long "devel/sage/sage/schemes/elliptic_curves/padics.py"
...
sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint._derivative 
...
sage.libs.ntl.ntl_lzz_pContext.ntl_zz_pContext     ValueError: Modulus (=2384185791015625) is too big
```



```
File ".../sage/schemes/elliptic_curves/ell_number_field.py", line 728:
    sage: EllipticCurve([1 + a , -1 + a , 1 + a , -11 + a , 5 -9*a  ]).conductor()
...
    ValueError: factorization of 0 not defined
```



```
sage -t --long "devel/sage/sage/schemes/elliptic_curves/sha_tate.py"
...
    sage: EllipticCurve('858k2').sha().an_padic(7)  #rank 0, non trivial sha  (long
...
sage.libs.ntl.ntl_lzz_pContext.ntl_zz_pContext     ValueError: Modulus (=558545864083284007) is too big
```



```
sage -t --long "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
**********************************************************************
    sage: w.coleman_integral(P, Q)
Expected:
    O(11^6)
Got:
    6 + 7*11 + 8*11^2 + 7*11^3 + 3*11^4 + 10*11^5 + O(11^6)
**********************************************************************
    sage: C.coleman_integral(x*w, P, Q)
Expected:
    O(11^6)
Got:
    3 + 11 + 6*11^2 + 2*11^3 + 8*11^5 + O(11^6)
**********************************************************************
    sage: C.coleman_integral(x^2*w, P, Q)
Expected:
    3*11 + 2*11^2 + 7*11^3 + 2*11^4 + 10*11^5 + O(11^6)
Got:
    5 + 11 + 8*11^2 + 11^3 + 7*11^4 + 6*11^5 + O(11^6)
**********************************************************************
    sage: w.integrate(P, Q), (x*w).integrate(P, Q)
Expected:
    (O(71^4), O(71^4))
Got:
    (40 + 4*71 + 21*71^2 + 39*71^3 + O(71^4), 2 + 58*71 + 27*71^2 + 49*71^3 + O(71^4))
**********************************************************************
    sage: w.integrate(P, R)
Expected:
    42*71 + 63*71^2 + 55*71^3 + O(71^4)
Got:
    14 + 27*71 + 46*71^2 + 10*71^3 + O(71^4)
**********************************************************************
```




---

archive/issue_comments_037683.json:
```json
{
    "body": "The updated `zmod_poly.patch` fixes the two \n\n\n```\nValueError: Modulus (...) is too big\n```\n\n\nerrors. So we're back to square one and these two fail:\n\n\n```\nsage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\"\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\"\n```\n",
    "created_at": "2009-01-12T16:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37683",
    "user": "https://github.com/malb"
}
```

The updated `zmod_poly.patch` fixes the two 


```
ValueError: Modulus (...) is too big
```


errors. So we're back to square one and these two fail:


```
sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py"
```




---

archive/issue_comments_037684.json:
```json
{
    "body": "The patch update adds a simple zn_poly interface to `Polynomial_zmod_flint`.\n\n## Performance\n\n\n```\ndef f(p,n):\n    P = PolynomialRing(GF(next_prime(p)),'x')\n    f = P.random_element(n)\n    g = P.random_element(n)\n\n    t0 = cputime()\n    r0 = f*g\n    t0 = cputime(t0)\n\n    t1 = cputime()\n    r1 = f._mul_zn_poly(g)\n    t1 = cputime(t1)\n\n    assert(r0 == r1)\n\n    return p,n,t0,t1\n\nfor i in range(21): \n   f(2**47,2**i)\n```\n\n\nreturns\n\n\n```\n# (140737488355328, 1, 0.0, 0.0)\n# (140737488355328, 2, 0.0, 0.0)\n# (140737488355328, 4, 0.00099999999999766942, 0.0)\n# (140737488355328, 8, 0.0, 0.0)\n# (140737488355328, 16, 0.0, 0.0)\n# (140737488355328, 32, 0.0059990000000027521, 0.0)\n# (140737488355328, 64, 0.0, 0.0)\n# (140737488355328, 128, 0.0, 0.0)\n# (140737488355328, 256, 0.0, 0.0)\n# (140737488355328, 512, 0.0, 0.00099999999999766942)\n# (140737488355328, 1024, 0.00099999999999766942, 0.0)\n# (140737488355328, 2048, 0.0020000000000024443, 0.0019989999999978636)\n# (140737488355328, 4096, 0.0049989999999979773, 0.005000000000002558)\n# (140737488355328, 8192, 0.010998000000000729, 0.011997999999998399)\n# (140737488355328, 16384, 0.023995999999996798, 0.023997000000001378)\n# (140737488355328, 32768, 0.050992000000000814, 0.052991999999996153)\n# (140737488355328, 65536, 0.1149820000000048, 0.10598499999999689)\n# (140737488355328, 131072, 0.29195599999999189, 0.21996599999999944)\n# (140737488355328, 262144, 0.6119070000000022, 0.45393199999999467)\n# (140737488355328, 524288, 1.5217689999999919, 1.0278430000000043)\n# (140737488355328, 1048576, 3.1365230000000111, 2.0966819999999871)\n```\n",
    "created_at": "2009-01-13T01:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37684",
    "user": "https://github.com/malb"
}
```

The patch update adds a simple zn_poly interface to `Polynomial_zmod_flint`.

## Performance


```
def f(p,n):
    P = PolynomialRing(GF(next_prime(p)),'x')
    f = P.random_element(n)
    g = P.random_element(n)

    t0 = cputime()
    r0 = f*g
    t0 = cputime(t0)

    t1 = cputime()
    r1 = f._mul_zn_poly(g)
    t1 = cputime(t1)

    assert(r0 == r1)

    return p,n,t0,t1

for i in range(21): 
   f(2**47,2**i)
```


returns


```
# (140737488355328, 1, 0.0, 0.0)
# (140737488355328, 2, 0.0, 0.0)
# (140737488355328, 4, 0.00099999999999766942, 0.0)
# (140737488355328, 8, 0.0, 0.0)
# (140737488355328, 16, 0.0, 0.0)
# (140737488355328, 32, 0.0059990000000027521, 0.0)
# (140737488355328, 64, 0.0, 0.0)
# (140737488355328, 128, 0.0, 0.0)
# (140737488355328, 256, 0.0, 0.0)
# (140737488355328, 512, 0.0, 0.00099999999999766942)
# (140737488355328, 1024, 0.00099999999999766942, 0.0)
# (140737488355328, 2048, 0.0020000000000024443, 0.0019989999999978636)
# (140737488355328, 4096, 0.0049989999999979773, 0.005000000000002558)
# (140737488355328, 8192, 0.010998000000000729, 0.011997999999998399)
# (140737488355328, 16384, 0.023995999999996798, 0.023997000000001378)
# (140737488355328, 32768, 0.050992000000000814, 0.052991999999996153)
# (140737488355328, 65536, 0.1149820000000048, 0.10598499999999689)
# (140737488355328, 131072, 0.29195599999999189, 0.21996599999999944)
# (140737488355328, 262144, 0.6119070000000022, 0.45393199999999467)
# (140737488355328, 524288, 1.5217689999999919, 1.0278430000000043)
# (140737488355328, 1048576, 3.1365230000000111, 2.0966819999999871)
```




---

archive/issue_comments_037685.json:
```json
{
    "body": "Here's what is causing the problem in the ell_number_field.py test:\n\nIf F is a field of 3 elements, b=F(0), then b.nth_root(0) gives an error:\n\n```\nsage: K.<a>=NumberField(x^2-x+3)\nsage: F=K.residue_field(a); F; F.order()\nResidue field of Fractional ideal (a)\n3\nsage: b=F(0); b\n0\nsage: b.nth_root(3)\nValueError: factorization of 0 not defined\n```\n\nThe nth_root() function being called here is at fault, but that's as far as I got.",
    "created_at": "2009-01-13T23:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37685",
    "user": "https://github.com/JohnCremona"
}
```

Here's what is causing the problem in the ell_number_field.py test:

If F is a field of 3 elements, b=F(0), then b.nth_root(0) gives an error:

```
sage: K.<a>=NumberField(x^2-x+3)
sage: F=K.residue_field(a); F; F.order()
Residue field of Fractional ideal (a)
3
sage: b=F(0); b
0
sage: b.nth_root(3)
ValueError: factorization of 0 not defined
```

The nth_root() function being called here is at fault, but that's as far as I got.



---

archive/issue_comments_037686.json:
```json
{
    "body": "PS To the above:  The nth_root() function should definitely catch x=0 as a special trivial case.  But here that would just hide the problem, that calling roots() on the polynomial `x^3` over the field F causes a crash.  I have not time to dig deeper:  I would expect that first one would take `gcd(x<sup>3,x</sup>3-x)` ...",
    "created_at": "2009-01-14T08:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37686",
    "user": "https://github.com/JohnCremona"
}
```

PS To the above:  The nth_root() function should definitely catch x=0 as a special trivial case.  But here that would just hide the problem, that calling roots() on the polynomial `x^3` over the field F causes a crash.  I have not time to dig deeper:  I would expect that first one would take `gcd(x<sup>3,x</sup>3-x)` ...



---

archive/issue_comments_037687.json:
```json
{
    "body": "Thanks a lot John! I now have a function to debug which should be sufficient to track down the bug.",
    "created_at": "2009-01-14T09:47:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37687",
    "user": "https://github.com/malb"
}
```

Thanks a lot John! I now have a function to debug which should be sufficient to track down the bug.



---

archive/issue_comments_037688.json:
```json
{
    "body": "Thanks to John's comment we're now down to one doctest failure:\n\n\n```\nsage -t --long ...sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\n```\n\n\n\n```\n**********************************************************************\nFile \".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\", line 198:\n    sage: w.coleman_integral(P, Q)\nExpected:\n    O(11^6)\nGot:\n    6 + 7*11 + 8*11^2 + 7*11^3 + 3*11^4 + 10*11^5 + O(11^6)\n**********************************************************************\nFile \".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\", line 200:\n    sage: C.coleman_integral(x*w, P, Q)\nExpected:\n    O(11^6)\nGot:\n    3 + 11 + 6*11^2 + 2*11^3 + 8*11^5 + O(11^6)\n**********************************************************************\nFile \".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\", line 202:\n    sage: C.coleman_integral(x^2*w, P, Q)\nExpected:\n    3*11 + 2*11^2 + 7*11^3 + 2*11^4 + 10*11^5 + O(11^6)\nGot:\n    5 + 11 + 8*11^2 + 11^3 + 7*11^4 + 6*11^5 + O(11^6)\n**********************************************************************\nFile \".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\", line 213:\n    sage: w.integrate(P, Q), (x*w).integrate(P, Q)\nExpected:\n    (O(71^4), O(71^4))\nGot:\n    (40 + 4*71 + 21*71^2 + 39*71^3 + O(71^4), 2 + 58*71 + 27*71^2 + 49*71^3 + O(71^4))\n**********************************************************************\nFile \".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\", line 216:\n    sage: w.integrate(P, R)\nExpected:\n    42*71 + 63*71^2 + 55*71^3 + O(71^4)\nGot:\n    14 + 27*71 + 46*71^2 + 10*71^3 + O(71^4)\n```\n",
    "created_at": "2009-01-14T13:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37688",
    "user": "https://github.com/malb"
}
```

Thanks to John's comment we're now down to one doctest failure:


```
sage -t --long ...sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py
```



```
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 198:
    sage: w.coleman_integral(P, Q)
Expected:
    O(11^6)
Got:
    6 + 7*11 + 8*11^2 + 7*11^3 + 3*11^4 + 10*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 200:
    sage: C.coleman_integral(x*w, P, Q)
Expected:
    O(11^6)
Got:
    3 + 11 + 6*11^2 + 2*11^3 + 8*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 202:
    sage: C.coleman_integral(x^2*w, P, Q)
Expected:
    3*11 + 2*11^2 + 7*11^3 + 2*11^4 + 10*11^5 + O(11^6)
Got:
    5 + 11 + 8*11^2 + 11^3 + 7*11^4 + 6*11^5 + O(11^6)
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 213:
    sage: w.integrate(P, Q), (x*w).integrate(P, Q)
Expected:
    (O(71^4), O(71^4))
Got:
    (40 + 4*71 + 21*71^2 + 39*71^3 + O(71^4), 2 + 58*71 + 27*71^2 + 49*71^3 + O(71^4))
**********************************************************************
File ".../sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py", line 216:
    sage: w.integrate(P, R)
Expected:
    42*71 + 63*71^2 + 55*71^3 + O(71^4)
Got:
    14 + 27*71 + 46*71^2 + 10*71^3 + O(71^4)
```




---

archive/issue_comments_037689.json:
```json
{
    "body": "I'm glad that this bug made me look at that code, since what I found was that the only situations where I was calling that nth_root() function were for square roots in residue fields of characteristic 2 and cube roots in char. 3.  In both cases there is a special p'th root function implemented by jhpalmieri in #4553 which I reviewed and which could be used instead, which should be quicker.  So this bug will have had a useful side-effect or two...",
    "created_at": "2009-01-14T20:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37689",
    "user": "https://github.com/JohnCremona"
}
```

I'm glad that this bug made me look at that code, since what I found was that the only situations where I was calling that nth_root() function were for square roots in residue fields of characteristic 2 and cube roots in char. 3.  In both cases there is a special p'th root function implemented by jhpalmieri in #4553 which I reviewed and which could be used instead, which should be quicker.  So this bug will have had a useful side-effect or two...



---

archive/issue_comments_037690.json:
```json
{
    "body": "Some comments: \n\n1) Is there any reason __len__ was removed from GF(2)[x]? If we're going to take it out, it should at lest be deprecated, but I think it's useful to have. \n2) It is preferable to use .pxd files rather than .pxi files. \n\nI'm still looking into why the doctest failure above, and nothing obvious is coming to mind. Falling back to ntl polynomials gives the same wrong answer, so it must be something different in the way polynomials are interfaced/used.",
    "created_at": "2009-01-15T02:17:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37690",
    "user": "https://github.com/robertwb"
}
```

Some comments: 

1) Is there any reason __len__ was removed from GF(2)[x]? If we're going to take it out, it should at lest be deprecated, but I think it's useful to have. 
2) It is preferable to use .pxd files rather than .pxi files. 

I'm still looking into why the doctest failure above, and nothing obvious is coming to mind. Falling back to ntl polynomials gives the same wrong answer, so it must be something different in the way polynomials are interfaced/used.



---

archive/issue_comments_037691.json:
```json
{
    "body": "Attachment [4965-shift-fix.patch](tarball://root/attachments/some-uuid/ticket4965/4965-shift-fix.patch) by @robertwb created at 2009-01-15 05:29:22",
    "created_at": "2009-01-15T05:29:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37691",
    "user": "https://github.com/robertwb"
}
```

Attachment [4965-shift-fix.patch](tarball://root/attachments/some-uuid/ticket4965/4965-shift-fix.patch) by @robertwb created at 2009-01-15 05:29:22



---

archive/issue_comments_037692.json:
```json
{
    "body": "See attached. \n\nPerhaps `__rshift__` and `__lshift__` should call shift, it seems redundant to have code in all three. Also, I bet ntl and flint can shift faster than a multiply and/or divide.",
    "created_at": "2009-01-15T05:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37692",
    "user": "https://github.com/robertwb"
}
```

See attached. 

Perhaps `__rshift__` and `__lshift__` should call shift, it seems redundant to have code in all three. Also, I bet ntl and flint can shift faster than a multiply and/or divide.



---

archive/issue_comments_037693.json:
```json
{
    "body": "> Perhaps `__rshift__` and `__lshift__` should call shift, it seems \n> redundant to have code in all three. Also, I bet ntl and flint can shift faster\n> than a multiply and/or divide. \n\nI'd expect them to detect shifts, but I might be wrong. Should there be a  `celement_rshift`/`celement_lshift`?",
    "created_at": "2009-01-15T12:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37693",
    "user": "https://github.com/malb"
}
```

> Perhaps `__rshift__` and `__lshift__` should call shift, it seems 
> redundant to have code in all three. Also, I bet ntl and flint can shift faster
> than a multiply and/or divide. 

I'd expect them to detect shifts, but I might be wrong. Should there be a  `celement_rshift`/`celement_lshift`?



---

archive/issue_comments_037694.json:
```json
{
    "body": "Malb, my wrapper provides support for the shifts, you can just copy it from there.\n\nI think keeping a generic implementation in the Polynomial_template class, and overriding it if there is support for faster methods is good enough. Though maybe separating the user interface and functionality into 2 different functions (e.g. shift_left(), _shift_left_c()) might be better, so that the user interface and docstrings are consistent for subclasses.",
    "created_at": "2009-01-15T12:21:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37694",
    "user": "https://github.com/burcin"
}
```

Malb, my wrapper provides support for the shifts, you can just copy it from there.

I think keeping a generic implementation in the Polynomial_template class, and overriding it if there is support for faster methods is good enough. Though maybe separating the user interface and functionality into 2 different functions (e.g. shift_left(), _shift_left_c()) might be better, so that the user interface and docstrings are consistent for subclasses.



---

archive/issue_comments_037695.json:
```json
{
    "body": "Replying to [comment:17 robertwb]:\n> Some comments: \n> \n> 1) Is there any reason __len__ was removed from GF(2)[x]? If we're going to take it out, it should at lest be deprecated, but I think it's useful to have. \n\nlen shouldn't have been there in the first place because it is inconsistent with the rest of the univariate polynomials. \n\n> 2) It is preferable to use .pxd files rather than .pxi files. \n\nOkay, I'll change that then.",
    "created_at": "2009-01-15T12:43:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37695",
    "user": "https://github.com/malb"
}
```

Replying to [comment:17 robertwb]:
> Some comments: 
> 
> 1) Is there any reason __len__ was removed from GF(2)[x]? If we're going to take it out, it should at lest be deprecated, but I think it's useful to have. 

len shouldn't have been there in the first place because it is inconsistent with the rest of the univariate polynomials. 

> 2) It is preferable to use .pxd files rather than .pxi files. 

Okay, I'll change that then.



---

archive/issue_comments_037696.json:
```json
{
    "body": "Replying to [comment:17 robertwb]:\n> I'm still looking into why the doctest failure above, and nothing obvious is coming to mind. Falling back to ntl polynomials gives the same wrong answer, so it must be something different in the way polynomials are interfaced/used. \n\nI can't reproduce the behaviour you're describing. Maybe you missed that there are two places where `Polynomial_zmod_poly` is constructed (modn and modp). It fails if I leave the modn stuff in.",
    "created_at": "2009-01-15T13:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37696",
    "user": "https://github.com/malb"
}
```

Replying to [comment:17 robertwb]:
> I'm still looking into why the doctest failure above, and nothing obvious is coming to mind. Falling back to ntl polynomials gives the same wrong answer, so it must be something different in the way polynomials are interfaced/used. 

I can't reproduce the behaviour you're describing. Maybe you missed that there are two places where `Polynomial_zmod_poly` is constructed (modn and modp). It fails if I leave the modn stuff in.



---

archive/issue_comments_037697.json:
```json
{
    "body": "it seems like Robert's patch fixes the issue (I just realized now). I'm running `-t --long` now to see if everything is alright. Then I'll switch stuff around to pxd and do the shift business.",
    "created_at": "2009-01-15T14:40:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37697",
    "user": "https://github.com/malb"
}
```

it seems like Robert's patch fixes the issue (I just realized now). I'm running `-t --long` now to see if everything is alright. Then I'll switch stuff around to pxd and do the shift business.



---

archive/issue_comments_037698.json:
```json
{
    "body": "\n```\nmalb@sage:~/sage-3.2.2/devel/sage$ sage -tp 10 --long sage/\n...\nAll tests passed!\n```\n",
    "created_at": "2009-01-15T16:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37698",
    "user": "https://github.com/malb"
}
```


```
malb@sage:~/sage-3.2.2/devel/sage$ sage -tp 10 --long sage/
...
All tests passed!
```




---

archive/issue_comments_037699.json:
```json
{
    "body": "malb: Yes, I was missing the fact that I had to change modn and modp, but in any case I found the bug in the end. \n\nRegarding len, I think it would be useful to have for all univariate polynomials, but it's not a big deal. \n\nRegarding shifts, I think we already have too many functions, and shouldn't be introducing even more. I think there should be a celement_shift (which takes positive and negative values), and the template `__lshift__, __rshift__`, and `shift` all call this. It's probably the exception to not have specialized shift methods, and in this case one would manually implement them in celement_shift.",
    "created_at": "2009-01-15T19:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37699",
    "user": "https://github.com/robertwb"
}
```

malb: Yes, I was missing the fact that I had to change modn and modp, but in any case I found the bug in the end. 

Regarding len, I think it would be useful to have for all univariate polynomials, but it's not a big deal. 

Regarding shifts, I think we already have too many functions, and shouldn't be introducing even more. I think there should be a celement_shift (which takes positive and negative values), and the template `__lshift__, __rshift__`, and `shift` all call this. It's probably the exception to not have specialized shift methods, and in this case one would manually implement them in celement_shift.



---

archive/issue_comments_037700.json:
```json
{
    "body": "I've made the shifting issue a new ticket: #4982",
    "created_at": "2009-01-15T19:59:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37700",
    "user": "https://github.com/robertwb"
}
```

I've made the shifting issue a new ticket: #4982



---

archive/issue_comments_037701.json:
```json
{
    "body": "So I need to switch from pxi to pxd for \n* `polynomial_template.pxi`\n* `ntl_GF2X_linkage.pxi`\n* `flint_zmod_poly_linkage.pxi`\nand the ticket is ready for review. Or am I missing something?",
    "created_at": "2009-01-15T20:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37701",
    "user": "https://github.com/malb"
}
```

So I need to switch from pxi to pxd for 
* `polynomial_template.pxi`
* `ntl_GF2X_linkage.pxi`
* `flint_zmod_poly_linkage.pxi`
and the ticket is ready for review. Or am I missing something?



---

archive/issue_comments_037702.json:
```json
{
    "body": "Sorry for not being clear. The files you listed:\n\n* polynomial_template.pxi\n* flint_zmod_poly_linkage.pxi \n\nare the ones that should be .pxi (as they're actually included). The files that should be .pxd are\n\n* flint.pxi\n* ntl_interface.pxi\n* zmod_poly.pxi\n\nas they are declaration files. An example is worth a thousand words, I'll attach a patch (which you can fold into yours if you want).",
    "created_at": "2009-01-15T21:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37702",
    "user": "https://github.com/robertwb"
}
```

Sorry for not being clear. The files you listed:

* polynomial_template.pxi
* flint_zmod_poly_linkage.pxi 

are the ones that should be .pxi (as they're actually included). The files that should be .pxd are

* flint.pxi
* ntl_interface.pxi
* zmod_poly.pxi

as they are declaration files. An example is worth a thousand words, I'll attach a patch (which you can fold into yours if you want).



---

archive/issue_comments_037703.json:
```json
{
    "body": "move pxi declarations to pxd",
    "created_at": "2009-01-15T21:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37703",
    "user": "https://github.com/robertwb"
}
```

move pxi declarations to pxd



---

archive/issue_comments_037704.json:
```json
{
    "body": "Attachment [4965-pxi-to-pxd.patch](tarball://root/attachments/some-uuid/ticket4965/4965-pxi-to-pxd.patch) by @robertwb created at 2009-01-15 21:20:59\n\nOK, I attached a patch. This should probably be folded into zmod_poly.patch",
    "created_at": "2009-01-15T21:20:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37704",
    "user": "https://github.com/robertwb"
}
```

Attachment [4965-pxi-to-pxd.patch](tarball://root/attachments/some-uuid/ticket4965/4965-pxi-to-pxd.patch) by @robertwb created at 2009-01-15 21:20:59

OK, I attached a patch. This should probably be folded into zmod_poly.patch



---

archive/issue_comments_037705.json:
```json
{
    "body": "I had a lock and the direct use of ling in the FLINT headers is a bad thing on LLP platforms, i.e. Solaris, for at least efficiency reasons. I will complain about this to Bill and see what happens, but I guess this should not prevent this patch from going in for now.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-15T22:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37705",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I had a lock and the direct use of ling in the FLINT headers is a bad thing on LLP platforms, i.e. Solaris, for at least efficiency reasons. I will complain about this to Bill and see what happens, but I guess this should not prevent this patch from going in for now.

Cheers,

Michael



---

archive/issue_comments_037706.json:
```json
{
    "body": "to apply:\n* `polynomial_template.patch`\n* `zmod_poly.patch`",
    "created_at": "2009-01-19T02:37:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37706",
    "user": "https://github.com/malb"
}
```

to apply:
* `polynomial_template.patch`
* `zmod_poly.patch`



---

archive/issue_comments_037707.json:
```json
{
    "body": "For the record: Doctests on sage.math pass.\n\nRobert: If humanly possible can you review this in the next couple hours? Then this patch will make it into 3.3.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T05:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37707",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: Doctests on sage.math pass.

Robert: If humanly possible can you review this in the next couple hours? Then this patch will make it into 3.3.alpha0.

Cheers,

Michael



---

archive/issue_comments_037708.json:
```json
{
    "body": "The code looks good, and seems to work for me. \n\nOne failure in the doctests: \n\n\n```\nsage -t  \"sage/rings/polynomial//polynomial_zmod_flint.pyx\" \n**********************************************************************\nFile \"/Users/robert/sage/sage-3.1.3/devel/sage-trac4965/sage/rings/polynomial/polynomial_zmod_flint.pyx\", line 236:\n    sage: f*g == f._mul_zn_poly(g)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/robert/sage/current/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/robert/sage/current/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/robert/sage/current/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_8[5]>\", line 1, in <module>\n        f*g == f._mul_zn_poly(g)###line 236:\n    sage: f*g == f._mul_zn_poly(g)\n    AttributeError: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute '_mul_zn_poly'\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_8\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /Users/robert/sage/current/tmp/.doctest_polynomial_zmod_flint.py\n```\n\n\nshould be an easy fix.",
    "created_at": "2009-01-19T21:28:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37708",
    "user": "https://github.com/robertwb"
}
```

The code looks good, and seems to work for me. 

One failure in the doctests: 


```
sage -t  "sage/rings/polynomial//polynomial_zmod_flint.pyx" 
**********************************************************************
File "/Users/robert/sage/sage-3.1.3/devel/sage-trac4965/sage/rings/polynomial/polynomial_zmod_flint.pyx", line 236:
    sage: f*g == f._mul_zn_poly(g)
Exception raised:
    Traceback (most recent call last):
      File "/Users/robert/sage/current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/robert/sage/current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/robert/sage/current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[5]>", line 1, in <module>
        f*g == f._mul_zn_poly(g)###line 236:
    sage: f*g == f._mul_zn_poly(g)
    AttributeError: 'sage.rings.polynomial.polynomial_modn_dense_ntl.Po' object has no attribute '_mul_zn_poly'
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_8
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/robert/sage/current/tmp/.doctest_polynomial_zmod_flint.py
```


should be an easy fix.



---

archive/issue_comments_037709.json:
```json
{
    "body": "I cannot reproduce your failure neither could mabshoff (from the above statement). Maybe there was a problem applying the patches?",
    "created_at": "2009-01-20T05:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37709",
    "user": "https://github.com/malb"
}
```

I cannot reproduce your failure neither could mabshoff (from the above statement). Maybe there was a problem applying the patches?



---

archive/issue_comments_037710.json:
```json
{
    "body": "I bet I have a different cutoff between flint and ntl for a 32-bit machine.",
    "created_at": "2009-01-20T06:01:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37710",
    "user": "https://github.com/robertwb"
}
```

I bet I have a different cutoff between flint and ntl for a 32-bit machine.



---

archive/issue_comments_037711.json:
```json
{
    "body": "You are of course right. I changed the doctest to use `next_prime(GF(2^31))` which should work on 32-bit systems. However, this raises the question whether we want to be consistent across all platforms for the cutoff: w.r.t. `Matrix_modn_dense` mabshoff and wstein indicated their desire to do so in another ticket.",
    "created_at": "2009-01-20T06:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37711",
    "user": "https://github.com/malb"
}
```

You are of course right. I changed the doctest to use `next_prime(GF(2^31))` which should work on 32-bit systems. However, this raises the question whether we want to be consistent across all platforms for the cutoff: w.r.t. `Matrix_modn_dense` mabshoff and wstein indicated their desire to do so in another ticket.



---

archive/issue_comments_037712.json:
```json
{
    "body": "Looks like you have to go down to 2^30. \n\n\n```\nsage: P.<x> = PolynomialRing(GF(next_prime(2^31)))\nsage: type(x)\n<type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>\nsage: P.<x> = PolynomialRing(GF(next_prime(2^30)))\nsage: type(x)\n<type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>\n```\n\n\nPersonally, I think it's a bad idea to impose a 32-b it cutoff for 64-bit platforms.",
    "created_at": "2009-01-20T06:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37712",
    "user": "https://github.com/robertwb"
}
```

Looks like you have to go down to 2^30. 


```
sage: P.<x> = PolynomialRing(GF(next_prime(2^31)))
sage: type(x)
<type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
sage: P.<x> = PolynomialRing(GF(next_prime(2^30)))
sage: type(x)
<type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
```


Personally, I think it's a bad idea to impose a 32-b it cutoff for 64-bit platforms.



---

archive/issue_comments_037713.json:
```json
{
    "body": "Attachment [zmod_poly.patch](tarball://root/attachments/some-uuid/ticket4965/zmod_poly.patch) by @malb created at 2009-01-20 06:26:22\n\ngoing down to 2^30",
    "created_at": "2009-01-20T06:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37713",
    "user": "https://github.com/malb"
}
```

Attachment [zmod_poly.patch](tarball://root/attachments/some-uuid/ticket4965/zmod_poly.patch) by @malb created at 2009-01-20 06:26:22

going down to 2^30



---

archive/issue_comments_037714.json:
```json
{
    "body": "Replying to [comment:37 robertwb]:\n> Looks like you have to go down to 2^30. \n\ndone.",
    "created_at": "2009-01-20T06:27:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37714",
    "user": "https://github.com/malb"
}
```

Replying to [comment:37 robertwb]:
> Looks like you have to go down to 2^30. 

done.



---

archive/issue_comments_037715.json:
```json
{
    "body": "That resolved all of my concerns, positive review.",
    "created_at": "2009-01-20T07:06:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37715",
    "user": "https://github.com/robertwb"
}
```

That resolved all of my concerns, positive review.



---

archive/issue_comments_037716.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-22T23:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037717.json:
```json
{
    "body": "Merged polynomial_template.patch and zmod_poly.patch in Sage 3.3.alpha1",
    "created_at": "2009-01-22T23:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4965#issuecomment-37717",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged polynomial_template.patch and zmod_poly.patch in Sage 3.3.alpha1



---

archive/issue_events_005208.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-22T23:34:40Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4965",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4965#event-5208"
}
```
