# Issue 4636: improve polynomial_modn_dense_ntl.Polynomial_dense_mod_p

Issue created by migration from https://trac.sagemath.org/ticket/4636

Original creator: ncalexan

Original creation time: 2008-11-27 04:44:35

Assignee: was

CC:  craigcitro

Keywords: polynomial modn finite field gf

sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p is very old.

The attached patch removes (but doesn't yet delete -- could you verify it can be removed, reviewer?) Polynomial_dense_mod_p and implements polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz/ZZ using the newer techniques.

It makes basic arithmetic faster.  I was finding that arithmetic in GF(next_prime(2^50))['x'] was slower than in Zmod(next_prime(2^50)+1)['x'], but now I cannot find the comparison!  In any case, this is much faster for doing gcd/xgcd in GF(p)['x'].


---

Attachment


---

Comment by malb created at 2008-11-27 10:27:11

Hi Nick, did you see the 'newest' technique to implement these things? It is not 100% polished yet (e.g. I suppose context handling should be improved) but it should be the most straight forward in terms of avoiding code duplication. See `sage.rings.polynomial.polynomial_gf2x` and `sage.rings.polynomial.polynomial_template` for details.


---

Comment by was created at 2008-11-27 16:41:10

Nick, Is this supposed be "with patch; needs review"?


---

Comment by was created at 2008-11-28 04:45:08

REFEREE REPORT:

I applied this patch and doctested the rings directory.  I get a couple of doctest failures:


```
sage -t  devel/sage-main/sage/rings/integer_mod.pyx
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/rings/integer_mod.pyx", line 505:
    sage: type(a.polynomial())
Expected:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
Got:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz'>
**********************************************************************

sage -t  devel/sage-main/sage/rings/finite_field_givaro.pyx
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/rings/finite_field_givaro.pyx", line 1799:
    sage: type(f)
Expected:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
Got:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz'>
**********************************************************************
1 items had failures:


sage -t  devel/sage-main/sage/rings/finite_field.py
**********************************************************************
File "/Users/wstein/sage/devel/sage-main/sage/rings/finite_field.py", line 178:
    sage: type(f)
Expected:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_mod_p'>
Got:
    <type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modp_ntl_zz'>
**********************************************************************
1 items had failures:

...
	sage -t  devel/sage-main/sage/rings/polynomial/multi_polynomial_libsingular.pyx # 1 doctests failed
	sage -t  devel/sage-main/sage/rings/integer_mod.pyx # 1 doctests failed
	sage -t  devel/sage-main/sage/rings/finite_field_givaro.pyx # 1 doctests failed
	sage -t  devel/sage-main/sage/rings/finite_field.py # 1 doctests failed

```



---

Comment by malb created at 2009-01-23 07:16:45

I should reimplement this using `polynomial_template.pxi` and Nick will review it once its done.


---

Comment by malb created at 2009-01-25 19:00:58

Changing assignee from was to malb.


---

Comment by malb created at 2009-01-25 19:00:58

Changing status from new to assigned.


---

Comment by mhansen created at 2009-10-19 17:36:29

What is the status of this?  If no one is going to do the templated version, then we should probably include this code.


---

Comment by malb created at 2010-07-21 16:06:04

I vote for closing this ticket


```
sage: f = GF(7)['x']([2, 1, 3])
sage: type(f)
<type 'sage.rings.polynomial.polynomial_zmod_flint.Polynomial_zmod_flint'>
```



---

Comment by mhansen created at 2012-05-28 07:33:53

I agree with malb.


---

Comment by mhansen created at 2012-05-28 07:33:53

Changing keywords from "polynomial modn finite field gf" to "polynomial modn finite field gf sd40.5".


---

Comment by mhansen created at 2012-05-28 07:33:53

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2012-06-02 12:46:13

Resolution: worksforme
