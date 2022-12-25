# Issue 1097: p-adic polynomials don't have discriminant

archive/issues_001097.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R.<x> = PolynomialRing(ZZ)\nsage: x.discriminant()\n1\n\nsage: R.<x> = PolynomialRing(Zp(5))\nsage: x.discriminant()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/Users/david/temp/<ipython console> in <module>()\n\n<type 'exceptions.AttributeError'>: 'Polynomial_padic_capped_relative_dense' object has no attribute 'discriminant'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1097\n\n",
    "created_at": "2007-11-04T02:00:08Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "p-adic polynomials don't have discriminant",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1097",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody


```
sage: R.<x> = PolynomialRing(ZZ)
sage: x.discriminant()
1

sage: R.<x> = PolynomialRing(Zp(5))
sage: x.discriminant()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/Users/david/temp/<ipython console> in <module>()

<type 'exceptions.AttributeError'>: 'Polynomial_padic_capped_relative_dense' object has no attribute 'discriminant'
```



Issue created by migration from https://trac.sagemath.org/ticket/1097





---

archive/issue_comments_006615.json:
```json
{
    "body": "This is still a problem with 2.9.1.1. \n\nCheers,\n\nMichael",
    "created_at": "2007-12-26T02:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1097#issuecomment-6615",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still a problem with 2.9.1.1. 

Cheers,

Michael



---

archive/issue_comments_006616.json:
```json
{
    "body": "Alex Ghitza and Mike Hansen have confirmed that this is now fixed:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.alpha1, Release Date: 2008-04-04                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: sage: R.<x> = PolynomialRing(Zp(5))\nsage: sage: x.discriminant()\n1 + O(5^20)\nsage:\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-04-06T21:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1097#issuecomment-6616",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Alex Ghitza and Mike Hansen have confirmed that this is now fixed:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.alpha1, Release Date: 2008-04-04                  |
| Type notebook() for the GUI, and license() for information.        |
sage: sage: R.<x> = PolynomialRing(Zp(5))
sage: sage: x.discriminant()
1 + O(5^20)
sage:
```


Cheers,

Michael



---

archive/issue_events_001223.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-06T21:50:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1097",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1097#event-1223"
}
```



---

archive/issue_comments_006617.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-06T21:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1097#issuecomment-6617",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
