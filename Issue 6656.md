# Issue 6656: [with patch, needs review] fix latex method for laurent series element

archive/issues_006656.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nIn the [Sage Notebook Bugreports](http://spreadsheets.google.com/pub?key=pCwvGVwSMxTzT6E2xNdo5fA), there is a report of an error with typesetting Laurent series elements:\n\n```\nsage: R.<a,b>=PolynomialRing(QQ)\nsage: T.<x>=LaurentSeriesRing(R)\nsage: latex(a*x+b*x)\n'a + bx'\n```\n\nIt ought to be (a+b)x, but the parentheses are missing.  The attached patch should fix this.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6656\n\n",
    "created_at": "2009-07-29T19:05:01Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] fix latex method for laurent series element",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6656",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

In the [Sage Notebook Bugreports](http://spreadsheets.google.com/pub?key=pCwvGVwSMxTzT6E2xNdo5fA), there is a report of an error with typesetting Laurent series elements:

```
sage: R.<a,b>=PolynomialRing(QQ)
sage: T.<x>=LaurentSeriesRing(R)
sage: latex(a*x+b*x)
'a + bx'
```

It ought to be (a+b)x, but the parentheses are missing.  The attached patch should fix this.


Issue created by migration from https://trac.sagemath.org/ticket/6656





---

archive/issue_comments_054641.json:
```json
{
    "body": "Attachment\n\nreviewer patch",
    "created_at": "2009-08-03T01:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6656#issuecomment-54641",
    "user": "mvngu"
}
```

Attachment

reviewer patch



---

archive/issue_comments_054642.json:
```json
{
    "body": "Before the patch:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: R.<a,b> = PolynomialRing(QQ)\nsage: T.<x> = LaurentSeriesRing(R)\nsage: y = a*x + b*x\nsage: y._latex_()\n'a + bx'\nsage: latex(y)\na + bx\n```\n\nAfter the patch:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: R.<a,b> = PolynomialRing(QQ)\nsage: T.<x> = LaurentSeriesRing(R)\nsage: y = a*x + b*x\nsage: y._latex_()\n'\\\\left(a + b\\\\right)x'\nsage: latex(y)\n\\left(a + b\\right)x\n```\n\nNote that one can also obtain the LaTeX representation of an object through the `latex()` function. So I'm attaching a patch on top of John's that also calls that function. If John is OK with the patch `trac_6656-reviewer.patch`, then the ticket has positive review from me.",
    "created_at": "2009-08-03T01:47:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6656#issuecomment-54642",
    "user": "mvngu"
}
```

Before the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: R.<a,b> = PolynomialRing(QQ)
sage: T.<x> = LaurentSeriesRing(R)
sage: y = a*x + b*x
sage: y._latex_()
'a + bx'
sage: latex(y)
a + bx
```

After the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: R.<a,b> = PolynomialRing(QQ)
sage: T.<x> = LaurentSeriesRing(R)
sage: y = a*x + b*x
sage: y._latex_()
'\\left(a + b\\right)x'
sage: latex(y)
\left(a + b\right)x
```

Note that one can also obtain the LaTeX representation of an object through the `latex()` function. So I'm attaching a patch on top of John's that also calls that function. If John is OK with the patch `trac_6656-reviewer.patch`, then the ticket has positive review from me.



---

archive/issue_comments_054643.json:
```json
{
    "body": "Sure, looks fine to me. Tests still pass with the reviewer patch.",
    "created_at": "2009-08-03T02:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6656#issuecomment-54643",
    "user": "jhpalmieri"
}
```

Sure, looks fine to me. Tests still pass with the reviewer patch.



---

archive/issue_comments_054644.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-03T02:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6656#issuecomment-54644",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_054645.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-08-03T02:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6656#issuecomment-54645",
    "user": "mvngu"
}
```

Merged both patches.
