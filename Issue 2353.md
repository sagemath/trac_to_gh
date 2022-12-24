# Issue 2353: MPolynomialRing should be deprecated

archive/issues_002353.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @malb\n\nIt seems that the constructors `PolynomialRing` and `MPolynomialRing` are actually the same function.\n\nsage.rings.polynomial.multi_polynomial_ring imports `PolynomialRing` as `MPolynomialRing`, and this gets imported into global scope.\n\nKeeping to the python mantra \"there is only one way to do it\", the alias `MPolynomialRing` should be removed.\n\nSee ticket:2000 about this issue as well, though I don't see creating multivariate polynomial rings with only 1 variable as a valid use case to keep `MPolynomialRing`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2353\n\n",
    "created_at": "2008-02-29T10:02:59Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "MPolynomialRing should be deprecated",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2353",
    "user": "@burcin"
}
```
Assignee: @williamstein

CC:  @malb

It seems that the constructors `PolynomialRing` and `MPolynomialRing` are actually the same function.

sage.rings.polynomial.multi_polynomial_ring imports `PolynomialRing` as `MPolynomialRing`, and this gets imported into global scope.

Keeping to the python mantra "there is only one way to do it", the alias `MPolynomialRing` should be removed.

See ticket:2000 about this issue as well, though I don't see creating multivariate polynomial rings with only 1 variable as a valid use case to keep `MPolynomialRing`.

Issue created by migration from https://trac.sagemath.org/ticket/2353





---

archive/issue_comments_015818.json:
```json
{
    "body": "> See ticket:2000 about this issue as well, though I don't see creating multivariate\n> polynomial rings with only 1 variable as a valid use case to keep MPolynomialRing.\n\nYep, since this works I agree with you:\n\n```\nsage: type(PolynomialRing(QQ,'x',1))\n<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular'>\nsage: type(PolynomialRing(QQ,'x'))\n<class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_field'>\n```\n\n\nWilliam",
    "created_at": "2008-02-29T21:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2353#issuecomment-15818",
    "user": "@williamstein"
}
```

> See ticket:2000 about this issue as well, though I don't see creating multivariate
> polynomial rings with only 1 variable as a valid use case to keep MPolynomialRing.

Yep, since this works I agree with you:

```
sage: type(PolynomialRing(QQ,'x',1))
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular'>
sage: type(PolynomialRing(QQ,'x'))
<class 'sage.rings.polynomial.polynomial_ring.PolynomialRing_field'>
```


William



---

archive/issue_comments_015819.json:
```json
{
    "body": "add deprecation notice to MPolynomialRing, change doctests",
    "created_at": "2008-05-11T02:03:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2353#issuecomment-15819",
    "user": "@burcin"
}
```

add deprecation notice to MPolynomialRing, change doctests



---

archive/issue_comments_015820.json:
```json
{
    "body": "Attachment [2353_deprecate_MPolynomialRing.patch](tarball://root/attachments/some-uuid/ticket2353/2353_deprecate_MPolynomialRing.patch) by @burcin created at 2008-05-11 02:03:46\n\ndocumentation changes",
    "created_at": "2008-05-11T02:03:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2353#issuecomment-15820",
    "user": "@burcin"
}
```

Attachment [2353_deprecate_MPolynomialRing.patch](tarball://root/attachments/some-uuid/ticket2353/2353_deprecate_MPolynomialRing.patch) by @burcin created at 2008-05-11 02:03:46

documentation changes



---

archive/issue_comments_015821.json:
```json
{
    "body": "Changing assignee from @williamstein to @burcin.",
    "created_at": "2008-05-11T02:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2353#issuecomment-15821",
    "user": "@burcin"
}
```

Changing assignee from @williamstein to @burcin.



---

archive/issue_comments_015822.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-11T02:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2353#issuecomment-15822",
    "user": "@burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015823.json:
```json
{
    "body": "Attachment [2353_deprecate_MPolynomialRing-doc_changes.patch](tarball://root/attachments/some-uuid/ticket2353/2353_deprecate_MPolynomialRing-doc_changes.patch) by @burcin created at 2008-05-11 02:17:44\n\nattachment:2353_deprecate_MPolynomialRing.patch adds a deprecation notice to `MPolynomialRing` using Python's `warnings` module. It also prepends the docstring for `PolynomialRing` with the text:\n\n```\n    This function is deprecated and will be removed in a future version of\n    Sage. Please use PolynomialRing instead.\n\n    If you have questions regarding this function and it's replacement,\n    please send your comments to sage-support@googlegroups.com.\n```\n\n\nattachment:2353_deprecate_MPolynomialRing-doc_changes.patch replaces occurences of `MPolynomialRing` in the documentation with `PolynomialRing`. I don't know why the file `commontex/patchlevel.tex` appears in this patch.",
    "created_at": "2008-05-11T02:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2353#issuecomment-15823",
    "user": "@burcin"
}
```

Attachment [2353_deprecate_MPolynomialRing-doc_changes.patch](tarball://root/attachments/some-uuid/ticket2353/2353_deprecate_MPolynomialRing-doc_changes.patch) by @burcin created at 2008-05-11 02:17:44

attachment:2353_deprecate_MPolynomialRing.patch adds a deprecation notice to `MPolynomialRing` using Python's `warnings` module. It also prepends the docstring for `PolynomialRing` with the text:

```
    This function is deprecated and will be removed in a future version of
    Sage. Please use PolynomialRing instead.

    If you have questions regarding this function and it's replacement,
    please send your comments to sage-support@googlegroups.com.
```


attachment:2353_deprecate_MPolynomialRing-doc_changes.patch replaces occurences of `MPolynomialRing` in the documentation with `PolynomialRing`. I don't know why the file `commontex/patchlevel.tex` appears in this patch.



---

archive/issue_comments_015824.json:
```json
{
    "body": "Positive review, patches look good. The date/version string change for the doc patch might be an issue, I don't know.",
    "created_at": "2008-06-03T14:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2353#issuecomment-15824",
    "user": "@malb"
}
```

Positive review, patches look good. The date/version string change for the doc patch might be an issue, I don't know.



---

archive/issue_comments_015825.json:
```json
{
    "body": "The were some small problems with the doc patch:\n\n```\n--- a/tut/tut.tex       Sun May 04 11:23:15 2008 -0700\n+++ b/tut/tut.tex       Sun May 11 04:01:36 2008 +0200\n@@ -947,12 +947,10 @@ in one of two ways.\n \\index{polynomial!ring of multivariate}\n\n \\begin{verbatim}\n-sage: R = MPolynomialRing(GF(5),3,\"z\")\n+sage: R = PolynomialRing(GF(5),3,\"z\")\n sage: R\n Multivariate Polynomial Ring in z0, z1, z2 over Finite Field of size 5\n \\end{verbatim}\n-(The object \\code{MPolynomialRing(GF(5),3,\"z\")} is the same as\n-the object \\code{MPolynomialRing(GF(5),3,\"z\")}.)\n Just as for univariate polynomials, there is an alternative more\n compact notation:\n \\begin{verbatim}\n```\n\n\nThis conflicts with some work done by John Palmieri, so I resolved that manually.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-04T18:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2353#issuecomment-15825",
    "user": "mabshoff"
}
```

The were some small problems with the doc patch:

```
--- a/tut/tut.tex       Sun May 04 11:23:15 2008 -0700
+++ b/tut/tut.tex       Sun May 11 04:01:36 2008 +0200
@@ -947,12 +947,10 @@ in one of two ways.
 \index{polynomial!ring of multivariate}

 \begin{verbatim}
-sage: R = MPolynomialRing(GF(5),3,"z")
+sage: R = PolynomialRing(GF(5),3,"z")
 sage: R
 Multivariate Polynomial Ring in z0, z1, z2 over Finite Field of size 5
 \end{verbatim}
-(The object \code{MPolynomialRing(GF(5),3,"z")} is the same as
-the object \code{MPolynomialRing(GF(5),3,"z")}.)
 Just as for univariate polynomials, there is an alternative more
 compact notation:
 \begin{verbatim}
```


This conflicts with some work done by John Palmieri, so I resolved that manually.

Cheers,

Michael



---

archive/issue_comments_015826.json:
```json
{
    "body": "Merged both patches in Sage 3.0.3.alpha1",
    "created_at": "2008-06-04T18:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2353#issuecomment-15826",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.0.3.alpha1



---

archive/issue_comments_015827.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-04T18:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2353",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2353#issuecomment-15827",
    "user": "mabshoff"
}
```

Resolution: fixed
