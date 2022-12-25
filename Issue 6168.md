# Issue 6168: FLINT wrapper not reducing coefficients properly

archive/issues_006168.json:
```json
{
    "body": "Assignee: tbd\n\nIt is possible to create FLINT `zmod_poly` objects whose coefficients are not reduced mod n (where n is the modulus). This is difficult to show directly in Sage, but here is an example symptom:\n\n\n```\nsage: R.<x> = PolynomialRing(Integers(15))\nsage: S.<y> = PolynomialRing(Integers(5))\nsage: f = S(5*x)\nsage: f\n0\nsage: f == 0\nFalse\nsage: f.degree()\n1\n```\n\n\nInternally the coefficient 5 is not reduced, but it prints as reduced.\n\nThis bug is probably the main cause of #5817.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6168\n\n",
    "created_at": "2009-05-31T05:40:26Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "FLINT wrapper not reducing coefficients properly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6168",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
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

archive/issue_comments_049110.json:
```json
{
    "body": "See also\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/3d1e310b021c1620",
    "created_at": "2009-05-31T05:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49110",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

See also

http://groups.google.com/group/sage-devel/browse_thread/thread/3d1e310b021c1620



---

archive/issue_comments_049111.json:
```json
{
    "body": "Changing component from algebra to basic arithmetic.",
    "created_at": "2009-05-31T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49111",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebra to basic arithmetic.



---

archive/issue_comments_049112.json:
```json
{
    "body": "Attachment [zmod_poly_set_fix.patch](tarball://root/attachments/some-uuid/ticket6168/zmod_poly_set_fix.patch) by @williamstein created at 2009-05-31 20:51:33",
    "created_at": "2009-05-31T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49112",
    "user": "https://github.com/williamstein"
}
```

Attachment [zmod_poly_set_fix.patch](tarball://root/attachments/some-uuid/ticket6168/zmod_poly_set_fix.patch) by @williamstein created at 2009-05-31 20:51:33



---

archive/issue_comments_049113.json:
```json
{
    "body": "Changing assignee from tbd to somebody.",
    "created_at": "2009-05-31T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49113",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from tbd to somebody.



---

archive/issue_comments_049114.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-05-31T20:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49114",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to critical.



---

archive/issue_comments_049115.json:
```json
{
    "body": "The patch applies against 4.0, and fixes the bug:\n\n```\nsage: R.<x> = PolynomialRing(Integers(15))\nsage: S.<y> = PolynomialRing(Integers(5))\nsage: f = S(5*x)\nsage: f\n0\nsage: f == 0\nTrue\nsage: f.degree()\n-1\n```\n\nMoreover, with this patch in, the spkg at #5817 passes all doctests. Positive review.",
    "created_at": "2009-06-02T01:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49115",
    "user": "https://github.com/kedlaya"
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

archive/issue_comments_049116.json:
```json
{
    "body": "Merged in 4.0.1.rc0.",
    "created_at": "2009-06-03T18:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49116",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.rc0.



---

archive/issue_events_006417.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-06-03T18:26:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6168#event-6417"
}
```



---

archive/issue_comments_049117.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-03T18:26:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6168",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6168#issuecomment-49117",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
