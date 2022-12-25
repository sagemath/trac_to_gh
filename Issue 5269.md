# Issue 5269: coordinate ring of an affine patch on a hyperelliptic curve is broken

archive/issues_005269.json:
```json
{
    "body": "Assignee: @williamstein\n\nWhen taking an affine patch of a hyperelliptic curve, the defining polynomial (sometimes?) has the wrong parent:\n\n\n```\nsage: P.<x> = QQ[]\nsage: f = 4*x^5 - 30*x^3 + 45*x - 22\nsage: C = HyperellipticCurve(f)\nsage: D = C.affine_patch(0); D\nClosed subscheme of Affine Space of dimension 2 over Rational Field defined by:\n  x0^2*x1^3 + 22*x1^5 - 45*x1^4 + 30*x1^2 - 4\nsage: f = D.defining_polynomials()[0]; f\nx0^2*x1^3 + 22*x1^5 - 45*x1^4 + 30*x1^2 - 4\nsage: f.parent()\nMultivariate Polynomial Ring in x0, x1, x2 over Rational Field\n```\n\n\nEverything is fine except the last line: the parent of f should be a multivariate polynomial ring in two variables, not three.\n\nThis might be a more generic problem and not necessarily related to hyperelliptic curves.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5269\n\n",
    "created_at": "2009-02-14T11:52:33Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "coordinate ring of an affine patch on a hyperelliptic curve is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5269",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

When taking an affine patch of a hyperelliptic curve, the defining polynomial (sometimes?) has the wrong parent:


```
sage: P.<x> = QQ[]
sage: f = 4*x^5 - 30*x^3 + 45*x - 22
sage: C = HyperellipticCurve(f)
sage: D = C.affine_patch(0); D
Closed subscheme of Affine Space of dimension 2 over Rational Field defined by:
  x0^2*x1^3 + 22*x1^5 - 45*x1^4 + 30*x1^2 - 4
sage: f = D.defining_polynomials()[0]; f
x0^2*x1^3 + 22*x1^5 - 45*x1^4 + 30*x1^2 - 4
sage: f.parent()
Multivariate Polynomial Ring in x0, x1, x2 over Rational Field
```


Everything is fine except the last line: the parent of f should be a multivariate polynomial ring in two variables, not three.

This might be a more generic problem and not necessarily related to hyperelliptic curves.


Issue created by migration from https://trac.sagemath.org/ticket/5269





---

archive/issue_comments_040369.json:
```json
{
    "body": "Changing assignee from @williamstein to @aghitza.",
    "created_at": "2009-02-14T11:53:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5269#issuecomment-40369",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @aghitza.



---

archive/issue_comments_040370.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-14T11:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5269#issuecomment-40370",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040371.json:
```json
{
    "body": "The attached patch fixes the issue by making sure that the defining polynomials for a subscheme are elements of the coordinate ring of the ambient space.",
    "created_at": "2009-02-14T13:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5269#issuecomment-40371",
    "user": "https://github.com/aghitza"
}
```

The attached patch fixes the issue by making sure that the defining polynomials for a subscheme are elements of the coordinate ring of the ambient space.



---

archive/issue_events_012243.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2009-02-14T13:24:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5269",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5269#event-12243"
}
```



---

archive/issue_comments_040372.json:
```json
{
    "body": "Attachment [trac_5269.patch](tarball://root/attachments/some-uuid/ticket5269/trac_5269.patch) by @malb created at 2009-02-14 17:34:20\n\nPatch looks good and doctests pass.",
    "created_at": "2009-02-14T17:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5269#issuecomment-40372",
    "user": "https://github.com/malb"
}
```

Attachment [trac_5269.patch](tarball://root/attachments/some-uuid/ticket5269/trac_5269.patch) by @malb created at 2009-02-14 17:34:20

Patch looks good and doctests pass.



---

archive/issue_events_012244.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-15T07:56:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5269",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5269#event-12244"
}
```



---

archive/issue_comments_040373.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-15T07:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5269#issuecomment-40373",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040374.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T07:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5269",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5269#issuecomment-40374",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael
