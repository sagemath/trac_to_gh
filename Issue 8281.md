# Issue 8281: coercion problem breaks hecke_operator_on_basis over finite fields

archive/issues_008281.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  craigcitro\n\nThis happens in 4.3.3.alpha0:\n\n\n```\nsage: bas_mod5 = [f.change_ring(GF(5)) for f in victor_miller_basis(12, 20)]\nsage: hecke_operator_on_basis(bas_mod5, 2, 12)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/ghitza/shared/articles/eigensystems/code/<ipython console> in <module>()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/modular/modform/hecke_operator_on_qexp.pyc in hecke_operator_on_basis(B, n, k, eps, already_echelonized)\n    186     V = A.span_of_basis([g.padded_list(prec) for g in B],\n    187                         already_echelonized = already_echelonized)\n--> 188     return _hecke_operator_on_basis(B, V, n, k, eps)\n    189 \n    190     \n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/modular/modform/hecke_operator_on_qexp.pyc in _hecke_operator_on_basis(B, V, n, k, eps)\n    119     prec = V.degree()\n    120     TB = [hecke_operator_on_qexp(f, n, k, eps, prec, check=False, _return_list=True)\n--> 121                 for f in B]\n    122     TB = [V.coordinate_vector(w) for w in TB]\n    123     return matrix(V.base_ring(), len(B), len(B), TB, sparse=False)\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/modular/modform/hecke_operator_on_qexp.pyc in hecke_operator_on_qexp(f, n, k, eps, prec, check, _return_list)\n     87     for m in range(prec):\n     88         am = sum([eps(d) * d**l * f[m*n//(d*d)] for \\\n---> 89                   d in divisors(gcd(n, m)) if (m*n) % (d*d) == 0])\n     90         v.append(am)\n     91     if _return_list:\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11336)()\n\n/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6990)()\n\nTypeError: unsupported operand parent(s) for '*': 'Cyclotomic Field of order 1 and degree 1' and 'Finite Field of size 5'\n```\n\n\nI'm putting this in modular forms, but the underlying issue is likely a more general coercion problem.\n\nI'm ccing Craig because I seem to remember that he fixed something like this before :).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8281\n\n",
    "created_at": "2010-02-16T03:03:08Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "coercion problem breaks hecke_operator_on_basis over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8281",
    "user": "AlexGhitza"
}
```
Assignee: craigcitro

CC:  craigcitro

This happens in 4.3.3.alpha0:


```
sage: bas_mod5 = [f.change_ring(GF(5)) for f in victor_miller_basis(12, 20)]
sage: hecke_operator_on_basis(bas_mod5, 2, 12)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ghitza/shared/articles/eigensystems/code/<ipython console> in <module>()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/modular/modform/hecke_operator_on_qexp.pyc in hecke_operator_on_basis(B, n, k, eps, already_echelonized)
    186     V = A.span_of_basis([g.padded_list(prec) for g in B],
    187                         already_echelonized = already_echelonized)
--> 188     return _hecke_operator_on_basis(B, V, n, k, eps)
    189 
    190     

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/modular/modform/hecke_operator_on_qexp.pyc in _hecke_operator_on_basis(B, V, n, k, eps)
    119     prec = V.degree()
    120     TB = [hecke_operator_on_qexp(f, n, k, eps, prec, check=False, _return_list=True)
--> 121                 for f in B]
    122     TB = [V.coordinate_vector(w) for w in TB]
    123     return matrix(V.base_ring(), len(B), len(B), TB, sparse=False)

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/modular/modform/hecke_operator_on_qexp.pyc in hecke_operator_on_qexp(f, n, k, eps, prec, check, _return_list)
     87     for m in range(prec):
     88         am = sum([eps(d) * d**l * f[m*n//(d*d)] for \
---> 89                   d in divisors(gcd(n, m)) if (m*n) % (d*d) == 0])
     90         v.append(am)
     91     if _return_list:

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:11336)()

/home/ghitza/sage-devel/local/lib/python2.6/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6990)()

TypeError: unsupported operand parent(s) for '*': 'Cyclotomic Field of order 1 and degree 1' and 'Finite Field of size 5'
```


I'm putting this in modular forms, but the underlying issue is likely a more general coercion problem.

I'm ccing Craig because I seem to remember that he fixed something like this before :).

Issue created by migration from https://trac.sagemath.org/ticket/8281





---

archive/issue_comments_073326.json:
```json
{
    "body": "This is not, as I first thought, a coercion problem (there is no coercion between the cyclotomic field of degree 1 aka QQ and a finite field).\n\nThe problem is this: when the character eps is not given, it defaults to the trivial character *over QQ*.  It should really be over the base ring of the elements of the given basis instead.  The attached patch fixes this.",
    "created_at": "2010-02-16T12:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8281#issuecomment-73326",
    "user": "AlexGhitza"
}
```

This is not, as I first thought, a coercion problem (there is no coercion between the cyclotomic field of degree 1 aka QQ and a finite field).

The problem is this: when the character eps is not given, it defaults to the trivial character *over QQ*.  It should really be over the base ring of the elements of the given basis instead.  The attached patch fixes this.



---

archive/issue_comments_073327.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-16T12:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8281#issuecomment-73327",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073328.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-02-16T13:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8281#issuecomment-73328",
    "user": "AlexGhitza"
}
```

Attachment



---

archive/issue_comments_073329.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-05T14:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8281#issuecomment-73329",
    "user": "davidloeffler"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073330.json:
```json
{
    "body": "Looks fine to me. All doctests pass on my system (and I can't imagine any of this behaviour is at all platform-specific); and as an added bonus it doesn't conflict with the other positive-reviewed patches.",
    "created_at": "2010-04-05T14:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8281#issuecomment-73330",
    "user": "davidloeffler"
}
```

Looks fine to me. All doctests pass on my system (and I can't imagine any of this behaviour is at all platform-specific); and as an added bonus it doesn't conflict with the other positive-reviewed patches.



---

archive/issue_comments_073331.json:
```json
{
    "body": "Merged in 4.4.alpha0:\n- trac_8281.patch",
    "created_at": "2010-04-15T20:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8281#issuecomment-73331",
    "user": "jhpalmieri"
}
```

Merged in 4.4.alpha0:
- trac_8281.patch



---

archive/issue_comments_073332.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T20:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8281",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8281#issuecomment-73332",
    "user": "jhpalmieri"
}
```

Resolution: fixed
