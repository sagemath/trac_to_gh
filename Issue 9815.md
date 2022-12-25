# Issue 9815: Elliptic Curves over RR or CC have wrong type

archive/issues_009815.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nAs of 4.5.3.alpha2, elliptic curves defined over RR or CC without giving the base explicitly are given type `EllipticCurve_generic` instead of `EllipticCurve_field`, which means that some functions which should be available for them are not:\n\nFor example, over RR:\n\n```\nsage: E = EllipticCurve([1.2,3.4])\nsage: type(E)\n<class 'sage.schemes.elliptic_curves.ell_generic.EllipticCurve_generic'>\nsage: E.weierstrass_p()\n...\nAttributeError: 'EllipticCurve_generic' object has no attribute 'weierstrass_p'\nsage: E = EllipticCurve(RR,[1.2,3.4])\nsage: type(E)\n<class 'sage.schemes.elliptic_curves.ell_field.EllipticCurve_field'>\nsage: E.weierstrass_p()\n1.00000000000000*z^-2 + 0.000000000000000*z^-1 + 0.000000000000000 + 0.000000000000000*z - 0.240000000000000*z^2 + 0.000000000000000*z^3 - 0.485714285714286*z^4 + 0.000000000000000*z^5 + 0.0192000000000000*z^6 + 0.000000000000000*z^7 + 0.0317922077922077*z^8 + 0.000000000000000*z^9 + 0.0174386436420723*z^10 + 0.000000000000000*z^11 - 0.00169558441558439*z^12 + 0.000000000000000*z^13 - 0.00137243886869437*z^14 + 0.000000000000000*z^15 - 0.000392255141636108*z^16 + 0.000000000000000*z^17 + 0.0000813530244020272*z^18 + O(z^20)\n```\n\nand similarly over CC.\n\nThis is easy to fix, and I'll post a patch shortly.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9816\n\n",
    "created_at": "2010-08-27T08:49:04Z",
    "labels": [
        "component: elliptic curves",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Elliptic Curves over RR or CC have wrong type",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9815",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @JohnCremona

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


Issue created by migration from https://trac.sagemath.org/ticket/9816





---

archive/issue_comments_096639.json:
```json
{
    "body": "Attachment [trac_9816-ec-type.patch](tarball://root/attachments/some-uuid/ticket9816/trac_9816-ec-type.patch) by @JohnCremona created at 2010-08-27 09:06:58\n\napplies to 4.5.3.alpha2",
    "created_at": "2010-08-27T09:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9815#issuecomment-96639",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_9816-ec-type.patch](tarball://root/attachments/some-uuid/ticket9816/trac_9816-ec-type.patch) by @JohnCremona created at 2010-08-27 09:06:58

applies to 4.5.3.alpha2



---

archive/issue_comments_096640.json:
```json
{
    "body": "The patch fixes this.  It catches all bases which pass the is_field() test, after testing for the special types (rational, number fields, finite fields, etc).  So it gives better functionality for elliptic curves over RR, CC, QQbar, functions fields, ...",
    "created_at": "2010-08-27T09:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9815#issuecomment-96640",
    "user": "https://github.com/JohnCremona"
}
```

The patch fixes this.  It catches all bases which pass the is_field() test, after testing for the special types (rational, number fields, finite fields, etc).  So it gives better functionality for elliptic curves over RR, CC, QQbar, functions fields, ...



---

archive/issue_comments_096641.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-27T09:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9815#issuecomment-96641",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096642.json:
```json
{
    "body": "That is fine. All test pass on my 4.5.2. Thanks John.\n\nChris.",
    "created_at": "2010-08-31T19:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9815#issuecomment-96642",
    "user": "https://github.com/categorie"
}
```

That is fine. All test pass on my 4.5.2. Thanks John.

Chris.



---

archive/issue_comments_096643.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-31T19:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9815#issuecomment-96643",
    "user": "https://github.com/categorie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096644.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9815",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9815#issuecomment-96644",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
