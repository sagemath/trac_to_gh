# Issue 2545: [with patch, positive review] FractionFieldElement lacks derivative method

archive/issues_002545.json:
```json
{
    "body": "Assignee: @burcin\n\nAttached patch adds a `derivative` method to `FractionFieldElement`s, and fixes a bug in the `_derivative` method of `Polynomial_rational_dense`.\n\nSo these now work:\n\n```\nsage: R = ZZ['x']\nsage: S = R.fraction_field(); x = S.gen()\nsage: R(1).derivative(R(x))\n0\n\nsage: F = FractionField(PolynomialRing(RationalField(),'x,y'))\nsage: x,y = F.gens()\nsage: (1/(x+y)).derivative(x,y)\n2/(x^3 + 3*x^2*y + 3*x*y^2 + y^3)\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2545\n\n",
    "closed_at": "2008-03-18T00:06:36Z",
    "created_at": "2008-03-16T12:35:22Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, positive review] FractionFieldElement lacks derivative method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2545",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

Attached patch adds a `derivative` method to `FractionFieldElement`s, and fixes a bug in the `_derivative` method of `Polynomial_rational_dense`.

So these now work:

```
sage: R = ZZ['x']
sage: S = R.fraction_field(); x = S.gen()
sage: R(1).derivative(R(x))
0

sage: F = FractionField(PolynomialRing(RationalField(),'x,y'))
sage: x,y = F.gens()
sage: (1/(x+y)).derivative(x,y)
2/(x^3 + 3*x^2*y + 3*x*y^2 + y^3)
```




Issue created by migration from https://trac.sagemath.org/ticket/2545





---

archive/issue_comments_017334.json:
```json
{
    "body": "derivative method for FractionFieldElement",
    "created_at": "2008-03-16T12:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2545#issuecomment-17334",
    "user": "https://github.com/burcin"
}
```

derivative method for FractionFieldElement



---

archive/issue_comments_017335.json:
```json
{
    "body": "Attachment [sage_fraction_field_derivative.patch](tarball://root/attachments/some-uuid/ticket2545/sage_fraction_field_derivative.patch) by @aghitza created at 2008-03-16 14:34:11\n\nThis appears to work as advertised.  I have one request: the docstrings for derivative() and _derivative() refer to \"the derivative of this polynomial\", which is bad since these elements are (most of the time) not polynomials.  This should be replaced with \"rational function\" or something similar.",
    "created_at": "2008-03-16T14:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2545#issuecomment-17335",
    "user": "https://github.com/aghitza"
}
```

Attachment [sage_fraction_field_derivative.patch](tarball://root/attachments/some-uuid/ticket2545/sage_fraction_field_derivative.patch) by @aghitza created at 2008-03-16 14:34:11

This appears to work as advertised.  I have one request: the docstrings for derivative() and _derivative() refer to "the derivative of this polynomial", which is bad since these elements are (most of the time) not polynomials.  This should be replaced with "rational function" or something similar.



---

archive/issue_comments_017336.json:
```json
{
    "body": "new patch with requested doc changes",
    "created_at": "2008-03-16T14:48:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2545#issuecomment-17336",
    "user": "https://github.com/burcin"
}
```

new patch with requested doc changes



---

archive/issue_comments_017337.json:
```json
{
    "body": "Attachment [2545-sage_fraction_field_derivative-1.patch](tarball://root/attachments/some-uuid/ticket2545/2545-sage_fraction_field_derivative-1.patch) by @burcin created at 2008-03-16 14:51:03\n\nYou're right, I copied the text from the docstring for polynomials, and forgot to change it. :)\n\nattachment:2545-sage_fraction_field_derivative-1.patch replaces \"polynomial\" with \"rational function\" as suggested.",
    "created_at": "2008-03-16T14:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2545#issuecomment-17337",
    "user": "https://github.com/burcin"
}
```

Attachment [2545-sage_fraction_field_derivative-1.patch](tarball://root/attachments/some-uuid/ticket2545/2545-sage_fraction_field_derivative-1.patch) by @burcin created at 2008-03-16 14:51:03

You're right, I copied the text from the docstring for polynomials, and forgot to change it. :)

attachment:2545-sage_fraction_field_derivative-1.patch replaces "polynomial" with "rational function" as suggested.



---

archive/issue_comments_017338.json:
```json
{
    "body": "Cool.  I'm satisfied.",
    "created_at": "2008-03-16T15:14:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2545#issuecomment-17338",
    "user": "https://github.com/aghitza"
}
```

Cool.  I'm satisfied.



---

archive/issue_comments_017339.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-18T00:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2545#issuecomment-17339",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017340.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-18T00:06:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2545",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2545#issuecomment-17340",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha0



---

archive/issue_events_005959.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-18T00:06:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2545",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2545#event-5959"
}
```
