# Issue 6835: Inconsistent types for degree of finite fields

Issue created by migration from https://trac.sagemath.org/ticket/6835

Original creator: cremona

Original creation time: 2009-08-28 10:59:12

Assignee: tbd

CC:  jcooley

Keywords: finite field

Finite fields in Sage have 4 different types, depending on the characteristic and degree.  There is an inconsistency in the type of the degree of the field:

```
sage: k = GF(2,'b'); type(k); type(k.degree())
<class 'sage.rings.finite_field_prime_modn.FiniteField_prime_modn'>
<type 'int'>
sage: k = GF(2^10,'b'); type(k); type(k.degree())
<type 'sage.rings.finite_field_givaro.FiniteField_givaro'>
<type 'sage.rings.integer.Integer'>
sage: k = GF(2^40,'b'); type(k); type(k.degree())
<type 'sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2e'>
<type 'sage.rings.integer.Integer'>
sage: k = GF(3^40,'b'); type(k); type(k.degree())
<class 'sage.rings.finite_field_ext_pari.FiniteField_ext_pari'>
<type 'int'>
```


i.e. in 2 of the 4 cases the degree is an int rather than an Integer.

Patch soon.



---

Comment by cremona created at 2009-08-28 11:22:39

Applies to 4.1.1


---

Attachment

The patch is very simple, just two lines changed (one for each type).  I tested all files in sage/rings.  After:

```
sage: k = GF(2,'b'); type(k); type(k.degree())
<class 'sage.rings.finite_field_prime_modn.FiniteField_prime_modn'>
<type 'sage.rings.integer.Integer'>
sage: k = GF(2^10,'b'); type(k); type(k.degree())
<type 'sage.rings.finite_field_givaro.FiniteField_givaro'>
<type 'sage.rings.integer.Integer'>
sage: k = GF(2^40,'b'); type(k); type(k.degree())
<type 'sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2e'>
<type 'sage.rings.integer.Integer'>
sage: k = GF(3^40,'b'); type(k); type(k.degree())
<class 'sage.rings.finite_field_ext_pari.FiniteField_ext_pari'>
<type 'sage.rings.integer.Integer'>
```



---

Comment by mvngu created at 2009-09-03 07:39:38

Resolution: fixed
