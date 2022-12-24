# Issue 6523: .is_zero() method raises error for symbolic expression involving derivative

archive/issues_006523.json:
```json
{
    "body": "CC:  mhansen\n\nIf a symbolic expression contains \u00a0symbolic derivative then\nchecking whether it is zero, raises error:\n\n```\nsage: x.diff(x,2).is_zero()\nTrue\n\nsage: f(x) = function('f',x)\nsage: f(x).diff(x).is_zero()\n....\nNotImplementedError: derivative\n```\n\n\nThis fails because new symbolics tries to convert it to maxima\nexpression for checking the relation.\n\nIt works fine for any other expression not involving symbolic\nderivative and without invoking maxima.\n\nIt seems to me, pynac relational test needs to be fixed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6523\n\n",
    "created_at": "2009-07-13T11:39:09Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": ".is_zero() method raises error for symbolic expression involving derivative",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6523",
    "user": "gmhossain"
}
```
CC:  mhansen

If a symbolic expression contains  symbolic derivative then
checking whether it is zero, raises error:

```
sage: x.diff(x,2).is_zero()
True

sage: f(x) = function('f',x)
sage: f(x).diff(x).is_zero()
....
NotImplementedError: derivative
```


This fails because new symbolics tries to convert it to maxima
expression for checking the relation.

It works fine for any other expression not involving symbolic
derivative and without invoking maxima.

It seems to me, pynac relational test needs to be fixed.

Issue created by migration from https://trac.sagemath.org/ticket/6523





---

archive/issue_comments_053198.json:
```json
{
    "body": "Attachment [trac_6523-fixes-error-in-is_zero_method_for_symbolic_derivative.patch](tarball://root/attachments/some-uuid/ticket6523/trac_6523-fixes-error-in-is_zero_method_for_symbolic_derivative.patch) by gmhossain created at 2009-07-15 15:56:46",
    "created_at": "2009-07-15T15:56:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6523#issuecomment-53198",
    "user": "gmhossain"
}
```

Attachment [trac_6523-fixes-error-in-is_zero_method_for_symbolic_derivative.patch](tarball://root/attachments/some-uuid/ticket6523/trac_6523-fixes-error-in-is_zero_method_for_symbolic_derivative.patch) by gmhossain created at 2009-07-15 15:56:46



---

archive/issue_comments_053199.json:
```json
{
    "body": "Unfortunately, the fact that an expression contains a symbolic derivative doesn't guarantee that it is nonzero:\n\n\n```\nsage: t = f(x).derivative(x)\nsage: (x*t +(1-x)*t - t)\n-(x - 1)*D[1](f)(x) + x*D[1](f)(x) - D[1](f)(x)\nsage: (x*t +(1-x)*t - t).collect(x)\n0\n```\n\n\nThe right fix for this is to either implement the `.derivative()` method in `sage/symbolic/expression_conversions.py` or to change pynac to allow different parents in `evalf()`, so that conversion to `CIF` can be done without the code in `expression_conversions.pyx`. \n\nI was planning to do this for #6243, but ended up using a different/better fix there.",
    "created_at": "2009-08-01T11:16:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6523#issuecomment-53199",
    "user": "burcin"
}
```

Unfortunately, the fact that an expression contains a symbolic derivative doesn't guarantee that it is nonzero:


```
sage: t = f(x).derivative(x)
sage: (x*t +(1-x)*t - t)
-(x - 1)*D[1](f)(x) + x*D[1](f)(x) - D[1](f)(x)
sage: (x*t +(1-x)*t - t).collect(x)
0
```


The right fix for this is to either implement the `.derivative()` method in `sage/symbolic/expression_conversions.py` or to change pynac to allow different parents in `evalf()`, so that conversion to `CIF` can be done without the code in `expression_conversions.pyx`. 

I was planning to do this for #6243, but ended up using a different/better fix there.



---

archive/issue_comments_053200.json:
```json
{
    "body": "Attachment [trac_6523-derivative_is_zero.patch](tarball://root/attachments/some-uuid/ticket6523/trac_6523-derivative_is_zero.patch) by burcin created at 2009-11-21 11:20:32\n\nadd doctests",
    "created_at": "2009-11-21T11:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6523#issuecomment-53200",
    "user": "burcin"
}
```

Attachment [trac_6523-derivative_is_zero.patch](tarball://root/attachments/some-uuid/ticket6523/trac_6523-derivative_is_zero.patch) by burcin created at 2009-11-21 11:20:32

add doctests



---

archive/issue_comments_053201.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-21T11:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6523#issuecomment-53201",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_053202.json:
```json
{
    "body": "This is fixed by #7490, since we don't use the `expression_conversions` module to convert to `RIF` any more.\n\nattachment:trac_6523-derivative_is_zero.patch adds a doctest with the example in the description.",
    "created_at": "2009-11-21T11:24:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6523#issuecomment-53202",
    "user": "burcin"
}
```

This is fixed by #7490, since we don't use the `expression_conversions` module to convert to `RIF` any more.

attachment:trac_6523-derivative_is_zero.patch adds a doctest with the example in the description.



---

archive/issue_comments_053203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-06T08:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6523#issuecomment-53203",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_053204.json:
```json
{
    "body": "Looks good to me.\n\nMerged trac_6523-derivative_is_zero.patch.",
    "created_at": "2009-12-06T08:33:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6523",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6523#issuecomment-53204",
    "user": "mhansen"
}
```

Looks good to me.

Merged trac_6523-derivative_is_zero.patch.
