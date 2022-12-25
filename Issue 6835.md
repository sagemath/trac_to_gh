# Issue 6835: Inconsistent types for degree of finite fields

archive/issues_006835.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jcooley\n\nKeywords: finite field\n\nFinite fields in Sage have 4 different types, depending on the characteristic and degree.  There is an inconsistency in the type of the degree of the field:\n\n```\nsage: k = GF(2,'b'); type(k); type(k.degree())\n<class 'sage.rings.finite_field_prime_modn.FiniteField_prime_modn'>\n<type 'int'>\nsage: k = GF(2^10,'b'); type(k); type(k.degree())\n<type 'sage.rings.finite_field_givaro.FiniteField_givaro'>\n<type 'sage.rings.integer.Integer'>\nsage: k = GF(2^40,'b'); type(k); type(k.degree())\n<type 'sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2e'>\n<type 'sage.rings.integer.Integer'>\nsage: k = GF(3^40,'b'); type(k); type(k.degree())\n<class 'sage.rings.finite_field_ext_pari.FiniteField_ext_pari'>\n<type 'int'>\n```\n\ni.e. in 2 of the 4 cases the degree is an int rather than an Integer.\n\nPatch soon.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6835\n\n",
    "created_at": "2009-08-28T10:59:12Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Inconsistent types for degree of finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6835",
    "user": "https://github.com/JohnCremona"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/6835





---

archive/issue_comments_056257.json:
```json
{
    "body": "Applies to 4.1.1",
    "created_at": "2009-08-28T11:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6835#issuecomment-56257",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 4.1.1



---

archive/issue_comments_056258.json:
```json
{
    "body": "Attachment [trac_6835-finite-field-degree.patch](tarball://root/attachments/some-uuid/ticket6835/trac_6835-finite-field-degree.patch) by @JohnCremona created at 2009-08-28 11:24:59\n\nThe patch is very simple, just two lines changed (one for each type).  I tested all files in sage/rings.  After:\n\n```\nsage: k = GF(2,'b'); type(k); type(k.degree())\n<class 'sage.rings.finite_field_prime_modn.FiniteField_prime_modn'>\n<type 'sage.rings.integer.Integer'>\nsage: k = GF(2^10,'b'); type(k); type(k.degree())\n<type 'sage.rings.finite_field_givaro.FiniteField_givaro'>\n<type 'sage.rings.integer.Integer'>\nsage: k = GF(2^40,'b'); type(k); type(k.degree())\n<type 'sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2e'>\n<type 'sage.rings.integer.Integer'>\nsage: k = GF(3^40,'b'); type(k); type(k.degree())\n<class 'sage.rings.finite_field_ext_pari.FiniteField_ext_pari'>\n<type 'sage.rings.integer.Integer'>\n```",
    "created_at": "2009-08-28T11:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6835#issuecomment-56258",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_6835-finite-field-degree.patch](tarball://root/attachments/some-uuid/ticket6835/trac_6835-finite-field-degree.patch) by @JohnCremona created at 2009-08-28 11:24:59

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

archive/issue_comments_056259.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-03T07:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6835#issuecomment-56259",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016090.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-03T07:39:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6835",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6835#event-16090"
}
```
