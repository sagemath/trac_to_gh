# Issue 5809: schemes/generic/hypersurface.py is completely broken

archive/issues_005809.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nKeywords: hypersurface\n\nThe file has zero doctests, imports nonexisting classes and looks like it's never been used.\n\nI'm attaching a patch that implements only the basic constructors and properties of projective and affine hypersurfaces, with 100% doctest coverage (of course :)\n\nI plan to add some more interesting functionality later, but this is a start.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5809\n\n",
    "created_at": "2009-04-17T10:44:25Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "schemes/generic/hypersurface.py is completely broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5809",
    "user": "AlexGhitza"
}
```
Assignee: AlexGhitza

Keywords: hypersurface

The file has zero doctests, imports nonexisting classes and looks like it's never been used.

I'm attaching a patch that implements only the basic constructors and properties of projective and affine hypersurfaces, with 100% doctest coverage (of course :)

I plan to add some more interesting functionality later, but this is a start.


Issue created by migration from https://trac.sagemath.org/ticket/5809





---

archive/issue_comments_045624.json:
```json
{
    "body": "Attachment [trac_5809.patch](tarball://root/attachments/some-uuid/ticket5809/trac_5809.patch) by AlexGhitza created at 2009-04-17 10:46:27",
    "created_at": "2009-04-17T10:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5809#issuecomment-45624",
    "user": "AlexGhitza"
}
```

Attachment [trac_5809.patch](tarball://root/attachments/some-uuid/ticket5809/trac_5809.patch) by AlexGhitza created at 2009-04-17 10:46:27



---

archive/issue_comments_045625.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-17T11:28:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5809#issuecomment-45625",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045626.json:
```json
{
    "body": "apply after the main patch",
    "created_at": "2009-04-18T16:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5809#issuecomment-45626",
    "user": "cremona"
}
```

apply after the main patch



---

archive/issue_comments_045627.json:
```json
{
    "body": "Attachment [trac_5809-review.patch](tarball://root/attachments/some-uuid/ticket5809/trac_5809-review.patch) by cremona created at 2009-04-18 16:12:11\n\nPositive review!\n\nI added this to the reference manual which required a little tweaking (the EXAMPLES in an __init__ docstring are excluded from the manual since the function name starts with an underscore;  what works well is to copy the same examples into the class's own docstring, then they get into the manual).\n\nI tested that the docs now build ok and look ok in the html ref manual.\n\nI guess Alex should ok the extra patch.",
    "created_at": "2009-04-18T16:12:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5809#issuecomment-45627",
    "user": "cremona"
}
```

Attachment [trac_5809-review.patch](tarball://root/attachments/some-uuid/ticket5809/trac_5809-review.patch) by cremona created at 2009-04-18 16:12:11

Positive review!

I added this to the reference manual which required a little tweaking (the EXAMPLES in an __init__ docstring are excluded from the manual since the function name starts with an underscore;  what works well is to copy the same examples into the class's own docstring, then they get into the manual).

I tested that the docs now build ok and look ok in the html ref manual.

I guess Alex should ok the extra patch.



---

archive/issue_comments_045628.json:
```json
{
    "body": "John, thanks for reviewing and for the new fixes.  Your patch looks good.",
    "created_at": "2009-04-18T22:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5809#issuecomment-45628",
    "user": "AlexGhitza"
}
```

John, thanks for reviewing and for the new fixes.  Your patch looks good.



---

archive/issue_comments_045629.json:
```json
{
    "body": "There are some doctest failures against 3.4.1:\n\n```\n        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 2 doctests failed\n        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 3 doctests failed\n        sage -t  devel/sage/sage/schemes/plane_curves/constructor.py # 1 doctests failed\n        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_field.py # 1 doctests failed\n```\n\nFor example:\n\n```\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_point.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_point.py\", line 175:\n    sage: E(1,0,0)\nExpected:\n    Traceback (most recent call last):\n    ...\n    TypeError: coordinates [1, 0, 0] do not define a point on\n    Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field\nGot:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/sage-3.4.2.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.2.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mabshoff/sage-3.4.2.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[6]>\", line 1, in <module>\n        E(Integer(1),Integer(0),Integer(0))###line 175:\n    sage: E(1,0,0)\n      File \"/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_generic.py\", line 611, in __call__\n        return plane_curve.ProjectiveCurve_generic.__call__(self, *args, **kwds)\n      File \"/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.py\", line 198, in __call__\n        return self.point(args)\n      File \"/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.py\", line 232, in point\n        return self._point_class(self, v, check=check)\n      File \"/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_point.py\", line 275, in __init__\n        point_homset.codomain()._check_satisfies_equations(v)\n      File \"/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_field.py\", line 34, in _check_satisfies_equations\n        self._error_bad_coords(v)\n    AttributeError: 'EllipticCurve_rational_field' object has no attribute '_error_bad_coords'\n**********************************************************************\n<SNIP>\n```\n",
    "created_at": "2009-04-23T06:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5809#issuecomment-45629",
    "user": "mabshoff"
}
```

There are some doctest failures against 3.4.1:

```
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 2 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 3 doctests failed
        sage -t  devel/sage/sage/schemes/plane_curves/constructor.py # 1 doctests failed
        sage -t  devel/sage/sage/schemes/elliptic_curves/ell_field.py # 1 doctests failed
```

For example:

```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_point.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_point.py", line 175:
    sage: E(1,0,0)
Expected:
    Traceback (most recent call last):
    ...
    TypeError: coordinates [1, 0, 0] do not define a point on
    Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field
Got:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[6]>", line 1, in <module>
        E(Integer(1),Integer(0),Integer(0))###line 175:
    sage: E(1,0,0)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_generic.py", line 611, in __call__
        return plane_curve.ProjectiveCurve_generic.__call__(self, *args, **kwds)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.py", line 198, in __call__
        return self.point(args)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.py", line 232, in point
        return self._point_class(self, v, check=check)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_point.py", line 275, in __init__
        point_homset.codomain()._check_satisfies_equations(v)
      File "/scratch/mabshoff/sage-3.4.2.alpha0/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_field.py", line 34, in _check_satisfies_equations
        self._error_bad_coords(v)
    AttributeError: 'EllipticCurve_rational_field' object has no attribute '_error_bad_coords'
**********************************************************************
<SNIP>
```




---

archive/issue_comments_045630.json:
```json
{
    "body": "Ooops, wrong patch to complain about, reinstating positive review. My bad :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T06:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5809#issuecomment-45630",
    "user": "mabshoff"
}
```

Ooops, wrong patch to complain about, reinstating positive review. My bad :)

Cheers,

Michael



---

archive/issue_comments_045631.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T06:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5809#issuecomment-45631",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_045632.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-23T06:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5809#issuecomment-45632",
    "user": "mabshoff"
}
```

Resolution: fixed
