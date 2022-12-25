# Issue 4087: [with patch, needs review] Improved printing of polynomials with 'negative' coefficients

archive/issues_004087.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage: K.<w> = CyclotomicField(3)\nsage: PK.<X> = K[]\nsage: X^2 - w*X\nX^2 + (-w)*X\nsage: (X + w)*(X + w^2)\nX^2 + (-1)*X + 1\n```\n\nIt would be much better if these polynomials were printed as `X^2 - w*X` \nand `X^2 - X + 1`, respectively.  For polynomials with integer or rational \ncoefficients such behaviour is already implemented.  Thus\n\n```\nsage: PolynomialRing(QQ, 'X')((X + w)*(X + w^2))\nX^2 - X + 1\n```\n\nThe attached patch makes this work more generally, and adjusts\n`latex(polynomial)` correspondingly.\n\nThe patch also changes 59 doctests to reflect the new code; in every\ncase the new output is more readable.  The doctests for the\nrelevant `_repr` and `_latex_` functions did not previously test those\nfunctions since they involved polynomials with rational coefficients, for\nwhich different methods are used.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4087\n\n",
    "created_at": "2008-09-09T11:39:37Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, needs review] Improved printing of polynomials with 'negative' coefficients",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4087",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```
Assignee: tbd


```
sage: K.<w> = CyclotomicField(3)
sage: PK.<X> = K[]
sage: X^2 - w*X
X^2 + (-w)*X
sage: (X + w)*(X + w^2)
X^2 + (-1)*X + 1
```

It would be much better if these polynomials were printed as `X^2 - w*X` 
and `X^2 - X + 1`, respectively.  For polynomials with integer or rational 
coefficients such behaviour is already implemented.  Thus

```
sage: PolynomialRing(QQ, 'X')((X + w)*(X + w^2))
X^2 - X + 1
```

The attached patch makes this work more generally, and adjusts
`latex(polynomial)` correspondingly.

The patch also changes 59 doctests to reflect the new code; in every
case the new output is more readable.  The doctests for the
relevant `_repr` and `_latex_` functions did not previously test those
functions since they involved polynomials with rational coefficients, for
which different methods are used.



Issue created by migration from https://trac.sagemath.org/ticket/4087





---

archive/issue_comments_029426.json:
```json
{
    "body": "Attachment [sage-4087.patch](tarball://root/attachments/some-uuid/ticket4087/sage-4087.patch) by mabshoff created at 2008-09-10 00:46:12",
    "created_at": "2008-09-10T00:46:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4087#issuecomment-29426",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [sage-4087.patch](tarball://root/attachments/some-uuid/ticket4087/sage-4087.patch) by mabshoff created at 2008-09-10 00:46:12



---

archive/issue_comments_029427.json:
```json
{
    "body": "The patch works with 3.1.2, subject to:\n\n```\npatching file sage/rings/number_field/number_field.py\nHunk #8 succeeded at 5055 with fuzz 1 (offset 21 lines).\n```\n\nafter which all doctests still pass.",
    "created_at": "2008-09-18T15:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4087#issuecomment-29427",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

The patch works with 3.1.2, subject to:

```
patching file sage/rings/number_field/number_field.py
Hunk #8 succeeded at 5055 with fuzz 1 (offset 21 lines).
```

after which all doctests still pass.



---

archive/issue_comments_029428.json:
```json
{
    "body": "Patch applies as advertised to 3.1.2 (just the fuzz).\n\nI take it that \"sage -testall\" has been done?  With or without \"-long\"?  Assuming so, I approve of this cosmetic but worthwhile patch.  I'm not doing a testall myself as I already have one in progress.",
    "created_at": "2008-09-18T20:44:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4087#issuecomment-29428",
    "user": "https://github.com/JohnCremona"
}
```

Patch applies as advertised to 3.1.2 (just the fuzz).

I take it that "sage -testall" has been done?  With or without "-long"?  Assuming so, I approve of this cosmetic but worthwhile patch.  I'm not doing a testall myself as I already have one in progress.



---

archive/issue_comments_029429.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha0",
    "created_at": "2008-09-19T00:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4087#issuecomment-29429",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha0



---

archive/issue_comments_029430.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-19T00:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4087#issuecomment-29430",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
