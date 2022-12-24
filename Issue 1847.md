# Issue 1847: add nice print method for Sha(Elliptic curve) [trivial to implement -- requires taste]

archive/issues_001847.json:
```json
{
    "body": "Assignee: @williamstein\n\nPrinting of Sha is ugly:\n\n\n```\nsage: E = EllipticCurve('37a')\nsage: Sha = E.sha(); Sha\n<class 'sage.schemes.elliptic_curves.sha.Sha'>\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1847\n\n",
    "created_at": "2008-01-19T12:46:42Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "add nice print method for Sha(Elliptic curve) [trivial to implement -- requires taste]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1847",
    "user": "@williamstein"
}
```
Assignee: @williamstein

Printing of Sha is ugly:


```
sage: E = EllipticCurve('37a')
sage: Sha = E.sha(); Sha
<class 'sage.schemes.elliptic_curves.sha.Sha'>
```


Issue created by migration from https://trac.sagemath.org/ticket/1847





---

archive/issue_comments_011689.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-01-23T20:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1847#issuecomment-11689",
    "user": "@aghitza"
}
```

Looks good.



---

archive/issue_comments_011690.json:
```json
{
    "body": "This patch causes the following doctest failure:\n\n```\nmabshoff@geom:/scratch/mabshoff/sage-3.3.alpha3$ ./sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha3/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\", line 3639:\n    sage: S\nExpected:\n    <class 'sage.schemes.elliptic_curves.sha_tate.Sha'>\nGot:\n    Shafarevich-Tate group for the Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field\n**********************************************************************\n```\n\nI guess the obvious fix is to change the doctest.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-25T20:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1847#issuecomment-11690",
    "user": "mabshoff"
}
```

This patch causes the following doctest failure:

```
mabshoff@geom:/scratch/mabshoff/sage-3.3.alpha3$ ./sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha3/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py", line 3639:
    sage: S
Expected:
    <class 'sage.schemes.elliptic_curves.sha_tate.Sha'>
Got:
    Shafarevich-Tate group for the Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
**********************************************************************
```

I guess the obvious fix is to change the doctest.

Cheers,

Michael



---

archive/issue_comments_011691.json:
```json
{
    "body": "Attachment [trac-1847.patch](tarball://root/attachments/some-uuid/ticket1847/trac-1847.patch) by @rlmill created at 2009-01-26 15:34:26\n\nPatch updated.",
    "created_at": "2009-01-26T15:34:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1847#issuecomment-11691",
    "user": "@rlmill"
}
```

Attachment [trac-1847.patch](tarball://root/attachments/some-uuid/ticket1847/trac-1847.patch) by @rlmill created at 2009-01-26 15:34:26

Patch updated.



---

archive/issue_comments_011692.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3",
    "created_at": "2009-01-28T14:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1847#issuecomment-11692",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3



---

archive/issue_comments_011693.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T14:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1847#issuecomment-11693",
    "user": "mabshoff"
}
```

Resolution: fixed
