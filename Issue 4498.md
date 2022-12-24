# Issue 4498: The argument function does not work with variables.

archive/issues_004498.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @kcrisman ktkohl\n\n\"The function should return the argument of a complex function.\" - Ronan Paix\u00e3o\n\nIssue created by migration from https://trac.sagemath.org/ticket/4498\n\n",
    "created_at": "2008-11-11T23:21:48Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "The argument function does not work with variables.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4498",
    "user": "TimothyClemans"
}
```
Assignee: somebody

CC:  @kcrisman ktkohl

"The function should return the argument of a complex function." - Ronan Paixão

Issue created by migration from https://trac.sagemath.org/ticket/4498





---

archive/issue_comments_033264.json:
```json
{
    "body": "\n```\narg(x)\n///\n\nTraceback (most recent call last):\n File \"<stdin>\", line 1, in <module>\n File \"/home/ronan/.sage/sage_notebook/worksheets/admin/0/code/127.py\",\nline 6, in <module>\n   exec compile(ur'arg(x)' + '\\n', '', 'single')\n File\n\"/home/ronan/progs/sage/local/lib/python2.5/site-packages/ZODB3-3.7.0-py2.5-linux-i686.egg/\", line 1, in <module>\n\n File\n\"/home/ronan/progs/sage/local/lib/python2.5/site-packages/sage/misc/functional.py\", line 67, in arg\n   except AttributeError: return CDF(x).arg()\n File \"complex_double.pyx\", line 286, in\nsage.rings.complex_double.ComplexDoubleField_class.__call__\n(sage/rings/complex_double.c:3324)\n File\n\"/home/ronan/progs/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 1454, in _complex_double_\n   raise TypeError\nTypeError\n```\n",
    "created_at": "2008-11-11T23:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33264",
    "user": "TimothyClemans"
}
```


```
arg(x)
///

Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/home/ronan/.sage/sage_notebook/worksheets/admin/0/code/127.py",
line 6, in <module>
   exec compile(ur'arg(x)' + '\n', '', 'single')
 File
"/home/ronan/progs/sage/local/lib/python2.5/site-packages/ZODB3-3.7.0-py2.5-linux-i686.egg/", line 1, in <module>

 File
"/home/ronan/progs/sage/local/lib/python2.5/site-packages/sage/misc/functional.py", line 67, in arg
   except AttributeError: return CDF(x).arg()
 File "complex_double.pyx", line 286, in
sage.rings.complex_double.ComplexDoubleField_class.__call__
(sage/rings/complex_double.c:3324)
 File
"/home/ronan/progs/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1454, in _complex_double_
   raise TypeError
TypeError
```




---

archive/issue_comments_033265.json:
```json
{
    "body": "Please post a complete session. As is the above is not very clear.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-12T14:16:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33265",
    "user": "mabshoff"
}
```

Please post a complete session. As is the above is not very clear.

Cheers,

Michael



---

archive/issue_comments_033266.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-11-12T17:13:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33266",
    "user": "@williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_033267.json:
```json
{
    "body": "Is this really an enchancement? As it is, just using arg(x) already raises an error and everything that needs arg() must be implemented numerically.",
    "created_at": "2008-11-15T17:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33267",
    "user": "ronanpaixao"
}
```

Is this really an enchancement? As it is, just using arg(x) already raises an error and everything that needs arg() must be implemented numerically.



---

archive/issue_comments_033268.json:
```json
{
    "body": "> Is this really an enchancement? As it is, just using arg(x) already \n> raises an error and everything that needs arg() must be implemented numerically. \n\nYes, this is an enhancement since it is implementing new functionality. \nIt would be a bug fix if there were a bug in the existing arg function, where it produced invalid results on supported input.\n\n -- William",
    "created_at": "2008-11-16T19:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33268",
    "user": "@williamstein"
}
```

> Is this really an enchancement? As it is, just using arg(x) already 
> raises an error and everything that needs arg() must be implemented numerically. 

Yes, this is an enhancement since it is implementing new functionality. 
It would be a bug fix if there were a bug in the existing arg function, where it produced invalid results on supported input.

 -- William



---

archive/issue_comments_033269.json:
```json
{
    "body": "Changing component from basic arithmetic to symbolics.",
    "created_at": "2010-05-26T21:00:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33269",
    "user": "@kcrisman"
}
```

Changing component from basic arithmetic to symbolics.



---

archive/issue_comments_033270.json:
```json
{
    "body": "This was also reported in #6220. I will close that as duplicate.",
    "created_at": "2010-05-27T10:25:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33270",
    "user": "@burcin"
}
```

This was also reported in #6220. I will close that as duplicate.



---

archive/issue_comments_033271.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-08-28T16:14:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33271",
    "user": "@burcin"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_033272.json:
```json
{
    "body": "Changing keywords from \"beginner\" to \"beginner, sd35.5\".",
    "created_at": "2012-01-11T15:39:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33272",
    "user": "ktkohl"
}
```

Changing keywords from "beginner" to "beginner, sd35.5".



---

archive/issue_comments_033273.json:
```json
{
    "body": "symbolic arg function",
    "created_at": "2012-01-12T04:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33273",
    "user": "ktkohl"
}
```

symbolic arg function



---

archive/issue_comments_033274.json:
```json
{
    "body": "Attachment [trac_4498_arg.1.patch](tarball://root/attachments/some-uuid/ticket4498/trac_4498_arg.1.patch) by ktkohl created at 2012-01-12 04:54:33",
    "created_at": "2012-01-12T04:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33274",
    "user": "ktkohl"
}
```

Attachment [trac_4498_arg.1.patch](tarball://root/attachments/some-uuid/ticket4498/trac_4498_arg.1.patch) by ktkohl created at 2012-01-12 04:54:33



---

archive/issue_comments_033275.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-12T04:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33275",
    "user": "ktkohl"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_033276.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-01-12T15:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33276",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033277.json:
```json
{
    "body": "There are a few small formatting issues, and it would be good to add an example showing that `arg(sqrt(2)+i)` remaining symbolic (as opposed to `arctan(1/sqrt(2))`) still evaluates correctly numerically.  Otherwise looks fine.  Currently running tests, as `arg` is likely used in a *lot* of places in Sage...",
    "created_at": "2012-01-12T15:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33277",
    "user": "@kcrisman"
}
```

There are a few small formatting issues, and it would be good to add an example showing that `arg(sqrt(2)+i)` remaining symbolic (as opposed to `arctan(1/sqrt(2))`) still evaluates correctly numerically.  Otherwise looks fine.  Currently running tests, as `arg` is likely used in a *lot* of places in Sage...



---

archive/issue_comments_033278.json:
```json
{
    "body": "\n```\n\nFile \"/Users/karl-dietercrisman/Downloads/sage-4.8.alpha5/devel/sage-main/sage/symbolic/random_tests.py\", line 16:\n    sage: [f for (one,f,arity) in _mk_full_functions()]\nExpected:\n    [Ei, abs, arccos, arccosh, arccot, arccoth, arccsc, arccsch,\n    arcsec, arcsech, arcsin, arcsinh, arctan, arctan2, arctanh,\n    binomial, ceil, conjugate, cos, cosh, cot, coth, csc, csch,\n    dickman_rho, dilog, dirac_delta, elliptic_e, elliptic_ec,\n    elliptic_eu, elliptic_f, elliptic_kc, elliptic_pi, erf, exp,\n    factorial, floor, heaviside, imag_part, integrate,\n    kronecker_delta, log, polylog, real_part, sec, sech, sgn, sin,\n    sinh, tan, tanh, unit_step, zeta, zetaderiv]\nGot:\n    [Ei, abs, arccos, arccosh, arccot, arccoth, arccsc, arccsch, arcsec, arcsech, arcsin, arcsinh, arctan, arctan2, arctanh, arg, binomial, ceil, conjugate, cos, cosh, cot, coth, csc, csch, dickman_rho, dilog, dirac_delta, elliptic_e, elliptic_ec, elliptic_eu, elliptic_f, elliptic_kc, elliptic_pi, erf, exp, factorial, floor, heaviside, imag_part, integrate, kronecker_delta, log, polylog, real_part, sec, sech, sgn, sin, sinh, tan, tanh, unit_step, zeta, zetaderiv]\n**********************************************************************\nFile \"/Users/karl-dietercrisman/Downloads/sage-4.8.alpha5/devel/sage-main/sage/symbolic/random_tests.py\", line 238:\n    sage: random_expr(5, verbose=True)\nExpected:\n    About to apply dirac_delta to [1]\n    About to apply arccsch to [0]\n    About to apply <built-in function add> to [0, arccsch(0)]\n    arccsch(0)\nGot:\n    About to apply dirac_delta to [1]\n    About to apply arcsec to [0]\n    About to apply <built-in function add> to [0, arcsec(0)]\n    arcsec(0)\n```\n",
    "created_at": "2012-01-12T15:08:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33278",
    "user": "@kcrisman"
}
```


```

File "/Users/karl-dietercrisman/Downloads/sage-4.8.alpha5/devel/sage-main/sage/symbolic/random_tests.py", line 16:
    sage: [f for (one,f,arity) in _mk_full_functions()]
Expected:
    [Ei, abs, arccos, arccosh, arccot, arccoth, arccsc, arccsch,
    arcsec, arcsech, arcsin, arcsinh, arctan, arctan2, arctanh,
    binomial, ceil, conjugate, cos, cosh, cot, coth, csc, csch,
    dickman_rho, dilog, dirac_delta, elliptic_e, elliptic_ec,
    elliptic_eu, elliptic_f, elliptic_kc, elliptic_pi, erf, exp,
    factorial, floor, heaviside, imag_part, integrate,
    kronecker_delta, log, polylog, real_part, sec, sech, sgn, sin,
    sinh, tan, tanh, unit_step, zeta, zetaderiv]
Got:
    [Ei, abs, arccos, arccosh, arccot, arccoth, arccsc, arccsch, arcsec, arcsech, arcsin, arcsinh, arctan, arctan2, arctanh, arg, binomial, ceil, conjugate, cos, cosh, cot, coth, csc, csch, dickman_rho, dilog, dirac_delta, elliptic_e, elliptic_ec, elliptic_eu, elliptic_f, elliptic_kc, elliptic_pi, erf, exp, factorial, floor, heaviside, imag_part, integrate, kronecker_delta, log, polylog, real_part, sec, sech, sgn, sin, sinh, tan, tanh, unit_step, zeta, zetaderiv]
**********************************************************************
File "/Users/karl-dietercrisman/Downloads/sage-4.8.alpha5/devel/sage-main/sage/symbolic/random_tests.py", line 238:
    sage: random_expr(5, verbose=True)
Expected:
    About to apply dirac_delta to [1]
    About to apply arccsch to [0]
    About to apply <built-in function add> to [0, arccsch(0)]
    arccsch(0)
Got:
    About to apply dirac_delta to [1]
    About to apply arcsec to [0]
    About to apply <built-in function add> to [0, arcsec(0)]
    arcsec(0)
```




---

archive/issue_comments_033279.json:
```json
{
    "body": "I think the Maxima translation may not be correct.\n\n```\n\n -- Function: carg (<z>)\n     Returns the complex argument of <z>.  The complex argument is an\n     angle `theta' in `(-%pi, %pi]' such that `r exp (theta %i) = <z>'\n     where `r' is the magnitude of <z>.\n\n     `carg' is a computational function, not a simplifying function.\n\n     See also `abs' (complex magnitude), `polarform', `rectform',\n     `realpart', and `imagpart'.\n\n     Examples:\n\n          (%i1) carg (1);\n          (%o1)                           0\n          (%i2) carg (1 + %i);\n                                         %pi\n          (%o2)                          ---\n                                          4\n          (%i3) carg (exp (%i));\n          (%o3)                           1\n          (%i4) carg (exp (%pi * %i));\n          (%o4)                          %pi\n          (%i5) carg (exp (3/2 * %pi * %i));\n                                          %pi\n          (%o5)                         - ---\n                                           2\n          (%i6) carg (17 * exp (2 * %i));\n          (%o6)                           2\n\n\n(%o3)                                true\n```\n\nSee also Barton Willis' [parg](http://maxima.sourceforge.net/docs/manual/en/maxima_80.html#Item_003a-parg), though that only works if having loaded `to_poly_solve`.",
    "created_at": "2012-01-12T16:25:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33279",
    "user": "@kcrisman"
}
```

I think the Maxima translation may not be correct.

```

 -- Function: carg (<z>)
     Returns the complex argument of <z>.  The complex argument is an
     angle `theta' in `(-%pi, %pi]' such that `r exp (theta %i) = <z>'
     where `r' is the magnitude of <z>.

     `carg' is a computational function, not a simplifying function.

     See also `abs' (complex magnitude), `polarform', `rectform',
     `realpart', and `imagpart'.

     Examples:

          (%i1) carg (1);
          (%o1)                           0
          (%i2) carg (1 + %i);
                                         %pi
          (%o2)                          ---
                                          4
          (%i3) carg (exp (%i));
          (%o3)                           1
          (%i4) carg (exp (%pi * %i));
          (%o4)                          %pi
          (%i5) carg (exp (3/2 * %pi * %i));
                                          %pi
          (%o5)                         - ---
                                           2
          (%i6) carg (17 * exp (2 * %i));
          (%o6)                           2


(%o3)                                true
```

See also Barton Willis' [parg](http://maxima.sourceforge.net/docs/manual/en/maxima_80.html#Item_003a-parg), though that only works if having loaded `to_poly_solve`.



---

archive/issue_comments_033280.json:
```json
{
    "body": "Otherwise, all tests pass!",
    "created_at": "2012-01-12T16:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33280",
    "user": "@kcrisman"
}
```

Otherwise, all tests pass!



---

archive/issue_comments_033281.json:
```json
{
    "body": "Do this to check the fix works.\n\n```\nsage: maxima(arg(x))\natan2(0,x)\nsage: maxima(arg(2+i))\natan(1/2)\nsage: maxima(arg(sqrt(2)+i))\natan(1/sqrt(2))\nsage: arg(2+i)\narctan(1/2)\nsage: arg(sqrt(2)+i)\narg(sqrt(2) + I)\n```\n\nIt also seems to help with the sqrt(2) issue, in a manner of speaking.  One could tell someone to do \n\n```\nsage: arg(sqrt(2)+i).simplify()\narctan(1/2*sqrt(2))\n```\n",
    "created_at": "2012-01-12T16:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33281",
    "user": "@kcrisman"
}
```

Do this to check the fix works.

```
sage: maxima(arg(x))
atan2(0,x)
sage: maxima(arg(2+i))
atan(1/2)
sage: maxima(arg(sqrt(2)+i))
atan(1/sqrt(2))
sage: arg(2+i)
arctan(1/2)
sage: arg(sqrt(2)+i)
arg(sqrt(2) + I)
```

It also seems to help with the sqrt(2) issue, in a manner of speaking.  One could tell someone to do 

```
sage: arg(sqrt(2)+i).simplify()
arctan(1/2*sqrt(2))
```




---

archive/issue_comments_033282.json:
```json
{
    "body": "revision of arg function--apply instead of the previous patch",
    "created_at": "2012-01-12T17:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33282",
    "user": "ktkohl"
}
```

revision of arg function--apply instead of the previous patch



---

archive/issue_comments_033283.json:
```json
{
    "body": "Attachment [trac_4498_arg.2.patch](tarball://root/attachments/some-uuid/ticket4498/trac_4498_arg.2.patch) by ktkohl created at 2012-01-12 17:06:43",
    "created_at": "2012-01-12T17:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33283",
    "user": "ktkohl"
}
```

Attachment [trac_4498_arg.2.patch](tarball://root/attachments/some-uuid/ticket4498/trac_4498_arg.2.patch) by ktkohl created at 2012-01-12 17:06:43



---

archive/issue_comments_033284.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-01-12T17:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33284",
    "user": "ktkohl"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033285.json:
```json
{
    "body": "Attachment [trac_4498_arg.3.patch](tarball://root/attachments/some-uuid/ticket4498/trac_4498_arg.3.patch) by ktkohl created at 2012-01-12 18:41:28\n\nsymbolic arg--fixed whitespace issues--use this one instead of others",
    "created_at": "2012-01-12T18:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33285",
    "user": "ktkohl"
}
```

Attachment [trac_4498_arg.3.patch](tarball://root/attachments/some-uuid/ticket4498/trac_4498_arg.3.patch) by ktkohl created at 2012-01-12 18:41:28

symbolic arg--fixed whitespace issues--use this one instead of others



---

archive/issue_comments_033286.json:
```json
{
    "body": "Attachment [trac_4498-symbolic_arg.cleanup.patch](tarball://root/attachments/some-uuid/ticket4498/trac_4498-symbolic_arg.cleanup.patch) by @burcin created at 2012-02-07 10:11:24",
    "created_at": "2012-02-07T10:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33286",
    "user": "@burcin"
}
```

Attachment [trac_4498-symbolic_arg.cleanup.patch](tarball://root/attachments/some-uuid/ticket4498/trac_4498-symbolic_arg.cleanup.patch) by @burcin created at 2012-02-07 10:11:24



---

archive/issue_comments_033287.json:
```json
{
    "body": "I uploaded a new patch with minor modifications to Karen's. In particular, it\n\n* removes the duplicate commands that appear in the `EXAMPLES` and `TESTS` blocks for `Function_arg`.\n* import `CC` directly instead of calling `ComplexField` in `_evalf_()`.\n\nI give a positive review to Karen's patch. If someone can take a quick look at my changes to check if I didn't mess anything up, this can be merged.",
    "created_at": "2012-02-07T10:30:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33287",
    "user": "@burcin"
}
```

I uploaded a new patch with minor modifications to Karen's. In particular, it

* removes the duplicate commands that appear in the `EXAMPLES` and `TESTS` blocks for `Function_arg`.
* import `CC` directly instead of calling `ComplexField` in `_evalf_()`.

I give a positive review to Karen's patch. If someone can take a quick look at my changes to check if I didn't mess anything up, this can be merged.



---

archive/issue_comments_033288.json:
```json
{
    "body": "It doesn't appear that you messed anything up, except ...\n\n```\nsage: arg(3.0)\n---------------------------------------------------------------------------\n<snip>\n   1426             return x.arg()\n   1427         except AttributeError:\n-> 1428             from sage.rings.complex_field import CC\n   1429             x = CC(x)\n   1430             return x.arg()\n\nImportError: cannot import name CC\n```\n\nSo apparently that won't work.  Otherwise the changes are fine.",
    "created_at": "2012-02-07T14:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33288",
    "user": "@kcrisman"
}
```

It doesn't appear that you messed anything up, except ...

```
sage: arg(3.0)
---------------------------------------------------------------------------
<snip>
   1426             return x.arg()
   1427         except AttributeError:
-> 1428             from sage.rings.complex_field import CC
   1429             x = CC(x)
   1430             return x.arg()

ImportError: cannot import name CC
```

So apparently that won't work.  Otherwise the changes are fine.



---

archive/issue_comments_033289.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-02-07T14:14:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33289",
    "user": "@kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_033290.json:
```json
{
    "body": "Attachment [trac_4498-arg_evalf.patch](tarball://root/attachments/some-uuid/ticket4498/trac_4498-arg_evalf.patch) by @burcin created at 2012-02-07 15:51:06",
    "created_at": "2012-02-07T15:51:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33290",
    "user": "@burcin"
}
```

Attachment [trac_4498-arg_evalf.patch](tarball://root/attachments/some-uuid/ticket4498/trac_4498-arg_evalf.patch) by @burcin created at 2012-02-07 15:51:06



---

archive/issue_comments_033291.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-02-07T15:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33291",
    "user": "@burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_033292.json:
```json
{
    "body": "Apparently I didn't run tests, latex output was also broken.\n\nattachment:trac_4498-arg_evalf.patch, to be applied after attachment:trac_4498-symbolic_arg.cleanup.patch, implements a new `_evalf_()` function which keeps the precision of the input. This one needs a real review. :)",
    "created_at": "2012-02-07T15:54:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33292",
    "user": "@burcin"
}
```

Apparently I didn't run tests, latex output was also broken.

attachment:trac_4498-arg_evalf.patch, to be applied after attachment:trac_4498-symbolic_arg.cleanup.patch, implements a new `_evalf_()` function which keeps the precision of the input. This one needs a real review. :)



---

archive/issue_comments_033293.json:
```json
{
    "body": "This makes a lot more sense.  Running tests...\n\nWhy `parent_d` and not `parent`?  Just wondering in case there is a convention I should be aware of.",
    "created_at": "2012-02-07T16:08:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33293",
    "user": "@kcrisman"
}
```

This makes a lot more sense.  Running tests...

Why `parent_d` and not `parent`?  Just wondering in case there is a convention I should be aware of.



---

archive/issue_comments_033294.json:
```json
{
    "body": "Using `parent` as the name of the keyword argument masks the imported `parent()` function, which I used in the function body.",
    "created_at": "2012-02-07T16:13:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33294",
    "user": "@burcin"
}
```

Using `parent` as the name of the keyword argument masks the imported `parent()` function, which I used in the function body.



---

archive/issue_comments_033295.json:
```json
{
    "body": "I wondered; that makes sense.\n\nAll looks well.  Just a question - do you want to include any of the following as tests?\n\n```\nsage: arg(long(1000))\n0\nsage: arg(1j)\n1.57079632679490\nsage: arg(1J)\n1.57079632679490\nsage: arg(complex(0,1))\n1.57079632679490\nsage: arg(complex(1,0))\n0.000000000000000\nsage: arg(int(10))\n0\n```\n\nIt's not a big deal to me either way, I just wanted to test them.",
    "created_at": "2012-02-07T16:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33295",
    "user": "@kcrisman"
}
```

I wondered; that makes sense.

All looks well.  Just a question - do you want to include any of the following as tests?

```
sage: arg(long(1000))
0
sage: arg(1j)
1.57079632679490
sage: arg(1J)
1.57079632679490
sage: arg(complex(0,1))
1.57079632679490
sage: arg(complex(1,0))
0.000000000000000
sage: arg(int(10))
0
```

It's not a big deal to me either way, I just wanted to test them.



---

archive/issue_comments_033296.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-07T16:39:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33296",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_033297.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-02-12T12:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33297",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_033298.json:
```json
{
    "body": "This patch conflicts with #9130.  Either this one or #9130 should be rebased.",
    "created_at": "2012-02-12T12:47:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33298",
    "user": "@jdemeyer"
}
```

This patch conflicts with #9130.  Either this one or #9130 should be rebased.



---

archive/issue_comments_033299.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-02-13T09:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33299",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_033300.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-02-14T14:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33300",
    "user": "@jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_033301.json:
```json
{
    "body": "standard form for name",
    "created_at": "2017-07-19T08:21:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4498",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4498#issuecomment-33301",
    "user": "@fchapoton"
}
```

standard form for name
