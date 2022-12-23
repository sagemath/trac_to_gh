# Issue 9815: Elliptic Curves over RR or CC have wrong type

Issue created by migration from https://trac.sagemath.org/ticket/9816

Original creator: cremona

Original creation time: 2010-08-27 08:49:04

Assignee: cremona

As of 4.5.3.alpha2, elliptic curves defined over RR or CC without giving the base explicitly are given type `EllipticCurve_generic` instead of `EllipticCurve_field`, which means that some functions which should be available for them are not:

For example, over RR:

```
sage: E = EllipticCurve([1.2,3.4])
sage: type(E)
<class 'sage.schemes.elliptic_curves.ell_generic.EllipticCurve_generic'>
sage: E.weierstrass_p()
...
AttributeError: 'EllipticCurve_generic' object has no attribute 'weierstrass_p'
sage: E = EllipticCurve(RR,[1.2,3.4])
sage: type(E)
<class 'sage.schemes.elliptic_curves.ell_field.EllipticCurve_field'>
sage: E.weierstrass_p()
1.00000000000000*z^-2 + 0.000000000000000*z^-1 + 0.000000000000000 + 0.000000000000000*z - 0.240000000000000*z^2 + 0.000000000000000*z^3 - 0.485714285714286*z^4 + 0.000000000000000*z^5 + 0.0192000000000000*z^6 + 0.000000000000000*z^7 + 0.0317922077922077*z^8 + 0.000000000000000*z^9 + 0.0174386436420723*z^10 + 0.000000000000000*z^11 - 0.00169558441558439*z^12 + 0.000000000000000*z^13 - 0.00137243886869437*z^14 + 0.000000000000000*z^15 - 0.000392255141636108*z^16 + 0.000000000000000*z^17 + 0.0000813530244020272*z^18 + O(z^20)
```

and similarly over CC.

This is easy to fix, and I'll post a patch shortly.



---

Attachment

applies to 4.5.3.alpha2


---

Comment by cremona created at 2010-08-27 09:08:21

The patch fixes this.  It catches all bases which pass the is_field() test, after testing for the special types (rational, number fields, finite fields, etc).  So it gives better functionality for elliptic curves over RR, CC, QQbar, functions fields, ...


---

Comment by cremona created at 2010-08-27 09:08:21

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-08-31 19:01:48

That is fine. All test pass on my 4.5.2. Thanks John.

Chris.


---

Comment by wuthrich created at 2010-08-31 19:01:48

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 11:37:54

Resolution: fixed
