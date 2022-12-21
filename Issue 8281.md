# Issue 8281: coercion problem breaks hecke_operator_on_basis over finite fields

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2010-02-16 03:03:08

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


---

Comment by AlexGhitza created at 2010-02-16 12:59:43

This is not, as I first thought, a coercion problem (there is no coercion between the cyclotomic field of degree 1 aka QQ and a finite field).

The problem is this: when the character eps is not given, it defaults to the trivial character *over QQ*.  It should really be over the base ring of the elements of the given basis instead.  The attached patch fixes this.


---

Comment by AlexGhitza created at 2010-02-16 12:59:43

Changing status from new to needs_review.


---

Attachment


---

Comment by davidloeffler created at 2010-04-05 14:41:34

Changing status from needs_review to positive_review.


---

Comment by davidloeffler created at 2010-04-05 14:41:34

Looks fine to me. All doctests pass on my system (and I can't imagine any of this behaviour is at all platform-specific); and as an added bonus it doesn't conflict with the other positive-reviewed patches.


---

Comment by jhpalmieri created at 2010-04-15 20:06:56

Merged in 4.4.alpha0:
 - trac_8281.patch


---

Comment by jhpalmieri created at 2010-04-15 20:06:56

Resolution: fixed
