# Issue 2000: bug either in polynomial factorization or polynomial ring constructor

archive/issues_002000.json:
```json
{
    "body": "Assignee: malb\n\n\n```\n> ----------------------------------------------------------------------\n> | SAGE Version 2.10, Release Date: 2008-01-18                        |\n> | Type notebook() for the GUI, and license() for information.        |\n> ----------------------------------------------------------------------\n> \n> sage: R.<z> = PolynomialRing(CC,1)\n> sage: f = z^4 - 6*z + 3\n> sage: f.factor()\n\nBOOM!\n\n\nThis is a bug.  Fortunately, there is an easy workaround (see below). \nDon't put PolynomialRing(CC, 1); instead put PolynomialRing(CC).\n\nsage: R.<z> = PolynomialRing(CC)\nsage: f = z^4 - 6*z + 3\nsage: f.factor()\n(1.00000000000000*z - 1.60443920904349) * (1.00000000000000*z - 0.511399619393097) * (1.00000000000000*z + 1.05791941421830 - 1.59281852704435*I) * (1.00000000000000*z + 1.05791941421830 + 1.59281852704435*I)\n\nThe problem is that PolynomialRing(CC,1) creates a *multivariate polynomial ring*\nwhich happens to be in 1 variable, whereas PolynomialRing(CC) creates a \nunivariate polynomial ring (which is implemented under the hood differently\nthan a multivariate polynomial ring).\n\nThe bug is that PolynomialRing(CC,1) should create a univariate ring,\nwhereas MPolynomialRing(CC,1) should be how one creates a multivariate\npoly ring in 1 variable.   (I think.)\n\nAlternatively, the bug is that factoring a multivariate polynomial in 1 variable\nuses Singular instead of other better univariate code that we have. \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2000\n\n",
    "created_at": "2008-01-31T06:25:40Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "bug either in polynomial factorization or polynomial ring constructor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2000",
    "user": "was"
}
```
Assignee: malb


```
> ----------------------------------------------------------------------
> | SAGE Version 2.10, Release Date: 2008-01-18                        |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> 
> sage: R.<z> = PolynomialRing(CC,1)
> sage: f = z^4 - 6*z + 3
> sage: f.factor()

BOOM!


This is a bug.  Fortunately, there is an easy workaround (see below). 
Don't put PolynomialRing(CC, 1); instead put PolynomialRing(CC).

sage: R.<z> = PolynomialRing(CC)
sage: f = z^4 - 6*z + 3
sage: f.factor()
(1.00000000000000*z - 1.60443920904349) * (1.00000000000000*z - 0.511399619393097) * (1.00000000000000*z + 1.05791941421830 - 1.59281852704435*I) * (1.00000000000000*z + 1.05791941421830 + 1.59281852704435*I)

The problem is that PolynomialRing(CC,1) creates a *multivariate polynomial ring*
which happens to be in 1 variable, whereas PolynomialRing(CC) creates a 
univariate polynomial ring (which is implemented under the hood differently
than a multivariate polynomial ring).

The bug is that PolynomialRing(CC,1) should create a univariate ring,
whereas MPolynomialRing(CC,1) should be how one creates a multivariate
poly ring in 1 variable.   (I think.)

Alternatively, the bug is that factoring a multivariate polynomial in 1 variable
uses Singular instead of other better univariate code that we have. 
```



Issue created by migration from https://trac.sagemath.org/ticket/2000





---

archive/issue_comments_012936.json:
```json
{
    "body": "> The bug is that PolynomialRing(CC,1) should create a univariate ring,\n> whereas MPolynomialRing(CC,1) should be how one creates a multivariate\n> poly ring in 1 variable.\n\nI agree.\n\n> Alternatively, the bug is that factoring a multivariate polynomial in 1 variable\n> uses Singular instead of other better univariate code that we have. \n\nAlso, I agree.",
    "created_at": "2008-01-31T09:41:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2000#issuecomment-12936",
    "user": "malb"
}
```

> The bug is that PolynomialRing(CC,1) should create a univariate ring,
> whereas MPolynomialRing(CC,1) should be how one creates a multivariate
> poly ring in 1 variable.

I agree.

> Alternatively, the bug is that factoring a multivariate polynomial in 1 variable
> uses Singular instead of other better univariate code that we have. 

Also, I agree.



---

archive/issue_comments_012937.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-08-18T13:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2000#issuecomment-12937",
    "user": "malb"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_012938.json:
```json
{
    "body": "Attachment [2000.patch](tarball://root/attachments/some-uuid/ticket2000/2000.patch) by malb created at 2008-08-18 13:31:14\n\nReplying to [comment:1 malb]:\n> > The bug is that PolynomialRing(CC,1) should create a univariate ring,\n> > whereas MPolynomialRing(CC,1) should be how one creates a multivariate\n> > poly ring in 1 variable.\n> \n> I agree.\n\nSince MPolynomialRing is deprecated now, the reported behavior is indeed the correct behavior.\n \n> > Alternatively, the bug is that factoring a multivariate polynomial in 1 variable\n> > uses Singular instead of other better univariate code that we have. \n\nThis is fixed in the attached patch.",
    "created_at": "2008-08-18T13:31:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2000#issuecomment-12938",
    "user": "malb"
}
```

Attachment [2000.patch](tarball://root/attachments/some-uuid/ticket2000/2000.patch) by malb created at 2008-08-18 13:31:14

Replying to [comment:1 malb]:
> > The bug is that PolynomialRing(CC,1) should create a univariate ring,
> > whereas MPolynomialRing(CC,1) should be how one creates a multivariate
> > poly ring in 1 variable.
> 
> I agree.

Since MPolynomialRing is deprecated now, the reported behavior is indeed the correct behavior.
 
> > Alternatively, the bug is that factoring a multivariate polynomial in 1 variable
> > uses Singular instead of other better univariate code that we have. 

This is fixed in the attached patch.



---

archive/issue_comments_012939.json:
```json
{
    "body": "Looks good; all tests pass.",
    "created_at": "2008-08-23T17:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2000#issuecomment-12939",
    "user": "cwitty"
}
```

Looks good; all tests pass.



---

archive/issue_comments_012940.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-25T00:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2000#issuecomment-12940",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha1



---

archive/issue_comments_012941.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T00:42:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2000#issuecomment-12941",
    "user": "mabshoff"
}
```

Resolution: fixed
