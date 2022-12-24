# Issue 951: evaluating polynomial over Z/nZ produces incorrect type

archive/issues_000951.json:
```json
{
    "body": "Assignee: somebody\n\nWhen evaluating a polynomial over Z/nZ at a point, I get a polynomial instead of a constant:\n\n\n```\nsage: R.<x> = PolynomialRing(Integers(10))\nsage: f = x^2 + x + 1\nsage: f(3)\n3\nsage: type(f(3))\n<type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_zz'>\n```\n\n\nIt should behave more like this:\n\n```\nsage: S.<y> = PolynomialRing(ZZ)     \nsage: g = y^2 + y + 1\nsage: type(g(3))\n<type 'sage.rings.integer.Integer'>\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/951\n\n",
    "created_at": "2007-10-20T21:21:02Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "evaluating polynomial over Z/nZ produces incorrect type",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/951",
    "user": "dmharvey"
}
```
Assignee: somebody

When evaluating a polynomial over Z/nZ at a point, I get a polynomial instead of a constant:


```
sage: R.<x> = PolynomialRing(Integers(10))
sage: f = x^2 + x + 1
sage: f(3)
3
sage: type(f(3))
<type 'sage.rings.polynomial.polynomial_modn_dense_ntl.Polynomial_dense_modn_ntl_zz'>
```


It should behave more like this:

```
sage: S.<y> = PolynomialRing(ZZ)     
sage: g = y^2 + y + 1
sage: type(g(3))
<type 'sage.rings.integer.Integer'>
```



Issue created by migration from https://trac.sagemath.org/ticket/951





---

archive/issue_comments_005799.json:
```json
{
    "body": "Attachment [7031.patch](tarball://root/attachments/some-uuid/ticket951/7031.patch) by cwitty created at 2007-10-21 01:19:20",
    "created_at": "2007-10-21T01:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/951#issuecomment-5799",
    "user": "cwitty"
}
```

Attachment [7031.patch](tarball://root/attachments/some-uuid/ticket951/7031.patch) by cwitty created at 2007-10-21 01:19:20



---

archive/issue_comments_005800.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-21T01:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/951",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/951#issuecomment-5800",
    "user": "was"
}
```

Resolution: fixed
