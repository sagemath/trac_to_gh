# Issue 2226: sage-2.10.2.alpha1 -- integral is now wrong (imho) for polynomials

archive/issues_002226.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis doctest fails:\n\n```\n\t [2.5 s]\nsage -t  devel/sage-main/sage/misc/functional.py            **********************************************************************\nFile \"functional.py\", line 438:\n    sage: integral(f)\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_29[1]>\", line 1, in <module>\n        integral(f)###line 438:\n    sage: integral(f)\n      File \"/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/misc/functional.py\", line 452, in integral\n        return x.integral(*args, **kwds)\n      File \"polynomial_element.pyx\", line 1499, in sage.rings.polynomial.polynomial_element.Polynomial.integral\n    ArithmeticError: coefficients of integral cannot be coerced into the base ring\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_29\n***Test Failed*** 1 failures.\n```\n\n\nThis is caused because cyclotomic polys are now over ZZ instead of QQ.\nAlso, integral *should* coerce to the fraction field.  This is really\ndumb to have this fail.\n\n\n```\nbsd:sage-2.10.2.alpha1 was$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.2.alpha1, Release Date: 2008-02-19               |\n| Type notebook() for the GUI, and license() for information.        |\nsage:         sage: f = cyclotomic_polynomial(10)                                                                                                                             \nsage:         sage: integral(f)   \n---------------------------------------------------------------------------\n<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)\n\n/Users/was/build/sage-2.10.2.alpha1/<ipython console> in <module>()\n\n/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/misc/functional.py in integral(x, *args, **kwds)\n    450     \"\"\"\n    451     if hasattr(x, 'integral'):\n--> 452         return x.integral(*args, **kwds)\n    453     else:\n    454         from sage.calculus.calculus import SR\n\n/Users/was/build/sage-2.10.2.alpha1/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.integral()\n\n<type 'exceptions.ArithmeticError'>: coefficients of integral cannot be coerced into the base ring\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2226\n\n",
    "created_at": "2008-02-20T07:00:39Z",
    "labels": [
        "component: calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "sage-2.10.2.alpha1 -- integral is now wrong (imho) for polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2226",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

This doctest fails:

```
	 [2.5 s]
sage -t  devel/sage-main/sage/misc/functional.py            **********************************************************************
File "functional.py", line 438:
    sage: integral(f)
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_29[1]>", line 1, in <module>
        integral(f)###line 438:
    sage: integral(f)
      File "/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/misc/functional.py", line 452, in integral
        return x.integral(*args, **kwds)
      File "polynomial_element.pyx", line 1499, in sage.rings.polynomial.polynomial_element.Polynomial.integral
    ArithmeticError: coefficients of integral cannot be coerced into the base ring
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_29
***Test Failed*** 1 failures.
```


This is caused because cyclotomic polys are now over ZZ instead of QQ.
Also, integral *should* coerce to the fraction field.  This is really
dumb to have this fail.


```
bsd:sage-2.10.2.alpha1 was$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.2.alpha1, Release Date: 2008-02-19               |
| Type notebook() for the GUI, and license() for information.        |
sage:         sage: f = cyclotomic_polynomial(10)                                                                                                                             
sage:         sage: integral(f)   
---------------------------------------------------------------------------
<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)

/Users/was/build/sage-2.10.2.alpha1/<ipython console> in <module>()

/Users/was/build/sage-2.10.2.alpha1/local/lib/python2.5/site-packages/sage/misc/functional.py in integral(x, *args, **kwds)
    450     """
    451     if hasattr(x, 'integral'):
--> 452         return x.integral(*args, **kwds)
    453     else:
    454         from sage.calculus.calculus import SR

/Users/was/build/sage-2.10.2.alpha1/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.integral()

<type 'exceptions.ArithmeticError'>: coefficients of integral cannot be coerced into the base ring
```


Issue created by migration from https://trac.sagemath.org/ticket/2226





---

archive/issue_comments_014718.json:
```json
{
    "body": "Attachment [sage-2226.patch](tarball://root/attachments/some-uuid/ticket2226/sage-2226.patch) by @williamstein created at 2008-02-21 17:30:38\n\nThe attached patch adds a bunch of much-needed docstrings to polynomial_element.pyx.  It also, more to the point, fixes f.integrate() to pass to the fraction field if needed.",
    "created_at": "2008-02-21T17:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2226#issuecomment-14718",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-2226.patch](tarball://root/attachments/some-uuid/ticket2226/sage-2226.patch) by @williamstein created at 2008-02-21 17:30:38

The attached patch adds a bunch of much-needed docstrings to polynomial_element.pyx.  It also, more to the point, fixes f.integrate() to pass to the fraction field if needed.



---

archive/issue_comments_014719.json:
```json
{
    "body": "Patch looks good to me, nice improvement docstring and test-wise.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T17:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2226#issuecomment-14719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me, nice improvement docstring and test-wise.

Cheers,

Michael



---

archive/issue_comments_014720.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-21T17:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2226#issuecomment-14720",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014721.json:
```json
{
    "body": "Merged in Sage 2.10.2.rc0",
    "created_at": "2008-02-21T17:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2226",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2226#issuecomment-14721",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.2.rc0
