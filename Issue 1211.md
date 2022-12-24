# Issue 1211: NTL crash in polynomial remainder over ZZ

archive/issues_001211.json:
```json
{
    "body": "Assignee: malb\n\nKeywords: ntl polynomial remainder ZZ crash segfault\n\n\n```\nsage: x = ZZ['x'].0\nsage: x^2 % (2*x - 1)\nDivRem: quotient not defined over ZZ\n/Users/ncalexan/sage/local/bin/sage-sage: line 218: 28251 Abort trap              sage-ipython -c \"$SAGE_STARTUP_COMMAND;\" \"$@\"\n\nProcess SAGE exited abnormally with code 134\n```\n\n\nMac OS X 10.4 Intel Core2Duo, Darwin mero.local 8.10.1 Darwin Kernel Version 8.10.1: Wed May 23 16:33:00 PDT 2007; root:xnu-792.22.5~1/RELEASE_I386 i386 i386\n\nIssue created by migration from https://trac.sagemath.org/ticket/1211\n\n",
    "created_at": "2007-11-19T22:20:06Z",
    "labels": [
        "commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "NTL crash in polynomial remainder over ZZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1211",
    "user": "ncalexan"
}
```
Assignee: malb

Keywords: ntl polynomial remainder ZZ crash segfault


```
sage: x = ZZ['x'].0
sage: x^2 % (2*x - 1)
DivRem: quotient not defined over ZZ
/Users/ncalexan/sage/local/bin/sage-sage: line 218: 28251 Abort trap              sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$@"

Process SAGE exited abnormally with code 134
```


Mac OS X 10.4 Intel Core2Duo, Darwin mero.local 8.10.1 Darwin Kernel Version 8.10.1: Wed May 23 16:33:00 PDT 2007; root:xnu-792.22.5~1/RELEASE_I386 i386 i386

Issue created by migration from https://trac.sagemath.org/ticket/1211





---

archive/issue_comments_007515.json:
```json
{
    "body": "Changing assignee from malb to dmharvey.",
    "created_at": "2007-12-01T15:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1211#issuecomment-7515",
    "user": "dmharvey"
}
```

Changing assignee from malb to dmharvey.



---

archive/issue_comments_007516.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-01T15:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1211#issuecomment-7516",
    "user": "dmharvey"
}
```

Changing status from new to assigned.



---

archive/issue_comments_007517.json:
```json
{
    "body": "I'm about to attach a patch that fixes this (and also fixes division by zero crash too).\n\n\n```\nsage: R.<x> = PolynomialRing(ZZ)\nsage: x^2 % (2*x - 1)\n---------------------------------------------------------------------------\n<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)\n\n/Users/david/sage-2.8.14/<ipython console> in <module>()\n\n/Users/david/sage-2.8.14/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.__mod__()\n\n/Users/david/sage-2.8.14/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.quo_rem()\n\n<type 'exceptions.ArithmeticError'>: division not exact in Z[x] (consider coercing to Q[x] first)\nsage: x^2 % 0\n---------------------------------------------------------------------------\n<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)\n\n/Users/david/sage-2.8.14/<ipython console> in <module>()\n\n/Users/david/sage-2.8.14/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.__mod__()\n\n/Users/david/sage-2.8.14/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.quo_rem()\n\n<type 'exceptions.ArithmeticError'>: division by zero polynomial\nsage: (2*x^2) % (2*x)\n0\n```\n",
    "created_at": "2007-12-01T17:13:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1211#issuecomment-7517",
    "user": "dmharvey"
}
```

I'm about to attach a patch that fixes this (and also fixes division by zero crash too).


```
sage: R.<x> = PolynomialRing(ZZ)
sage: x^2 % (2*x - 1)
---------------------------------------------------------------------------
<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)

/Users/david/sage-2.8.14/<ipython console> in <module>()

/Users/david/sage-2.8.14/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.__mod__()

/Users/david/sage-2.8.14/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.quo_rem()

<type 'exceptions.ArithmeticError'>: division not exact in Z[x] (consider coercing to Q[x] first)
sage: x^2 % 0
---------------------------------------------------------------------------
<type 'exceptions.ArithmeticError'>       Traceback (most recent call last)

/Users/david/sage-2.8.14/<ipython console> in <module>()

/Users/david/sage-2.8.14/polynomial_element.pyx in sage.rings.polynomial.polynomial_element.Polynomial.__mod__()

/Users/david/sage-2.8.14/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.quo_rem()

<type 'exceptions.ArithmeticError'>: division by zero polynomial
sage: (2*x^2) % (2*x)
0
```




---

archive/issue_comments_007518.json:
```json
{
    "body": "Attachment [1211.hg](tarball://root/attachments/some-uuid/ticket1211/1211.hg) by dmharvey created at 2007-12-01 17:14:11",
    "created_at": "2007-12-01T17:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1211#issuecomment-7518",
    "user": "dmharvey"
}
```

Attachment [1211.hg](tarball://root/attachments/some-uuid/ticket1211/1211.hg) by dmharvey created at 2007-12-01 17:14:11



---

archive/issue_comments_007519.json:
```json
{
    "body": "Looks good, and all doctests still pass in sage/rings/polynomial/.",
    "created_at": "2007-12-01T23:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1211#issuecomment-7519",
    "user": "cwitty"
}
```

Looks good, and all doctests still pass in sage/rings/polynomial/.



---

archive/issue_comments_007520.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T00:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1211#issuecomment-7520",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007521.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T00:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1211",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1211#issuecomment-7521",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha2.
