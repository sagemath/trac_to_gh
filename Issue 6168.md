# Issue 6168: FLINT wrapper not reducing coefficients properly

archive/issues_006168.json:
```json
{
    "body": "Assignee: tbd\n\nIt is possible to create FLINT `zmod_poly` objects whose coefficients are not reduced mod n (where n is the modulus). This is difficult to show directly in Sage, but here is an example symptom:\n\n\n```\nsage: R.<x> = PolynomialRing(Integers(15))\nsage: S.<y> = PolynomialRing(Integers(5))\nsage: f = S(5*x)\nsage: f\n0\nsage: f == 0\nFalse\nsage: f.degree()\n1\n```\n\n\nInternally the coefficient 5 is not reduced, but it prints as reduced.\n\nThis bug is probably the main cause of #5817.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6168\n\n",
    "created_at": "2009-05-31T05:40:26Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "FLINT wrapper not reducing coefficients properly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6168",
    "user": "dmharvey"
}
```
Assignee: tbd

It is possible to create FLINT `zmod_poly` objects whose coefficients are not reduced mod n (where n is the modulus). This is difficult to show directly in Sage, but here is an example symptom:


```
sage: R.<x> = PolynomialRing(Integers(15))
sage: S.<y> = PolynomialRing(Integers(5))
sage: f = S(5*x)
sage: f
0
sage: f == 0
False
sage: f.degree()
1
```


Internally the coefficient 5 is not reduced, but it prints as reduced.

This bug is probably the main cause of #5817.


Issue created by migration from https://trac.sagemath.org/ticket/6168





---

archive/issue_comments_049205.json:
```json
{
    "body": "See also\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/3d1e310b021c1620",
    "created_at": "2009-05-31T05:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49205",
    "user": "dmharvey"
}
```

See also

http://groups.google.com/group/sage-devel/browse_thread/thread/3d1e310b021c1620



---

archive/issue_comments_049206.json:
```json
{
    "body": "Changing component from algebra to basic arithmetic.",
    "created_at": "2009-05-31T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49206",
    "user": "was"
}
```

Changing component from algebra to basic arithmetic.



---

archive/issue_comments_049207.json:
```json
{
    "body": "Attachment [zmod_poly_set_fix.patch](tarball://root/attachments/some-uuid/ticket6168/zmod_poly_set_fix.patch) by was created at 2009-05-31 20:51:33",
    "created_at": "2009-05-31T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49207",
    "user": "was"
}
```

Attachment [zmod_poly_set_fix.patch](tarball://root/attachments/some-uuid/ticket6168/zmod_poly_set_fix.patch) by was created at 2009-05-31 20:51:33



---

archive/issue_comments_049208.json:
```json
{
    "body": "Changing assignee from tbd to somebody.",
    "created_at": "2009-05-31T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49208",
    "user": "was"
}
```

Changing assignee from tbd to somebody.



---

archive/issue_comments_049209.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-05-31T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49209",
    "user": "was"
}
```

Changing priority from major to critical.



---

archive/issue_comments_049210.json:
```json
{
    "body": "The patch applies against 4.0, and fixes the bug:\n\n```\nsage: R.<x> = PolynomialRing(Integers(15))\nsage: S.<y> = PolynomialRing(Integers(5))\nsage: f = S(5*x)\nsage: f\n0\nsage: f == 0\nTrue\nsage: f.degree()\n-1\n```\n\nMoreover, with this patch in, the spkg at #5817 passes all doctests. Positive review.",
    "created_at": "2009-06-02T01:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49210",
    "user": "kedlaya"
}
```

The patch applies against 4.0, and fixes the bug:

```
sage: R.<x> = PolynomialRing(Integers(15))
sage: S.<y> = PolynomialRing(Integers(5))
sage: f = S(5*x)
sage: f
0
sage: f == 0
True
sage: f.degree()
-1
```

Moreover, with this patch in, the spkg at #5817 passes all doctests. Positive review.



---

archive/issue_comments_049211.json:
```json
{
    "body": "Merged in 4.0.1.rc0.",
    "created_at": "2009-06-03T18:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49211",
    "user": "mhansen"
}
```

Merged in 4.0.1.rc0.



---

archive/issue_comments_049212.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-03T18:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49212",
    "user": "mhansen"
}
```

Resolution: fixed
