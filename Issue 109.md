# Issue 109: inconsistent return type for generic powering or something

archive/issues_000109.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<x> = PolynomialRing(pAdicField(5))\nsage: type(x)\n <class 'sage.rings.polynomial_element.Polynomial_generic_dense_field'>\nsage: type(x**int(0))\n <class 'sage.rings.polynomial_element.Polynomial_generic_dense_field'>\nsage: type((x**3)**int(0))\n <type 'int'>\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/109\n\n",
    "created_at": "2006-10-04T21:25:16Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "title": "inconsistent return type for generic powering or something",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/109",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody


```
sage: R.<x> = PolynomialRing(pAdicField(5))
sage: type(x)
 <class 'sage.rings.polynomial_element.Polynomial_generic_dense_field'>
sage: type(x**int(0))
 <class 'sage.rings.polynomial_element.Polynomial_generic_dense_field'>
sage: type((x**3)**int(0))
 <type 'int'>
```



Issue created by migration from https://trac.sagemath.org/ticket/109





---

archive/issue_comments_000510.json:
```json
{
    "body": "Sorry that was a misleading example. It has nothing to do with `int(0)`, the same thing happens for SAGE Integer(0).",
    "created_at": "2006-10-04T21:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/109#issuecomment-510",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

Sorry that was a misleading example. It has nothing to do with `int(0)`, the same thing happens for SAGE Integer(0).



---

archive/issue_comments_000511.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-05T07:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/109#issuecomment-511",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_000113.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2006-10-05T07:56:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/109",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/109#event-113"
}
```



---

archive/issue_comments_000512.json:
```json
{
    "body": "Fixed for sage-1.4.",
    "created_at": "2006-10-05T07:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/109",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/109#issuecomment-512",
    "user": "https://github.com/williamstein"
}
```

Fixed for sage-1.4.
