# Issue 4869: make element of relative number field from polynomial

archive/issues_004869.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @JohnCremona\n\nKeywords: relative number field polynomial\n\nJohn Cremona remarked at #4837:\n\nfor an absolute extension we can create an element from a polynomial over the base field, but not for a relative extension:\n\n\n```\nsage: K.<z>=CyclotomicField(7)\nsage: Ky.<y>=PolynomialRing(K)\nsage: L.<a>=K.extension(y^2+1)\nsage: K(K.polynomial_ring().random_element())\nz + 1\nsage: L(L.polynomial_ring().random_element())\n---------------------------------------------------------------------------\nTypeError           \n...\nTypeError: Unable to coerce 7/2*z^5 + 1/2*z^4 + z^3 - 37/2*z to a rational\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4869\n\n",
    "created_at": "2008-12-24T12:41:46Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "make element of relative number field from polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4869",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

CC:  @JohnCremona

Keywords: relative number field polynomial

John Cremona remarked at #4837:

for an absolute extension we can create an element from a polynomial over the base field, but not for a relative extension:


```
sage: K.<z>=CyclotomicField(7)
sage: Ky.<y>=PolynomialRing(K)
sage: L.<a>=K.extension(y^2+1)
sage: K(K.polynomial_ring().random_element())
z + 1
sage: L(L.polynomial_ring().random_element())
---------------------------------------------------------------------------
TypeError           
...
TypeError: Unable to coerce 7/2*z^5 + 1/2*z^4 + z^3 - 37/2*z to a rational
```



Issue created by migration from https://trac.sagemath.org/ticket/4869





---

archive/issue_comments_036813.json:
```json
{
    "body": "This is fixed by the patches for #1367.  This should be closed as a dupe after #1367 is merged.",
    "created_at": "2009-01-24T09:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4869#issuecomment-36813",
    "user": "https://github.com/ncalexan"
}
```

This is fixed by the patches for #1367.  This should be closed as a dupe after #1367 is merged.



---

archive/issue_events_005112.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-29T05:45:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4869",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4869#event-5112"
}
```



---

archive/issue_comments_036814.json:
```json
{
    "body": "Fixed via #1367 in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T05:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4869#issuecomment-36814",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed via #1367 in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_036815.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T05:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4869#issuecomment-36815",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
