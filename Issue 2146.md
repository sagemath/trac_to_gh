# Issue 2146: PolyBoRi random_element is broken

archive/issues_002146.json:
```json
{
    "body": "Assignee: malb\n\nCC:  malb\n\nSee below. \n\n\n```\nsage: R.<x,y,z> = BooleanPolynomialRing(3)\nsage: R.random_element()\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/Users/was/<ipython console> in <module>()\n\n/Users/was/multi_polynomial_ring_generic.pyx in sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic.random_element()\n\n/Users/was/pbori.pyx in sage.rings.polynomial.pbori.BooleanPolynomialRing.__call__()\n\n<type 'exceptions.TypeError'>: cannot convert <type 'dict'> to BooleanPolynomial\nsage: \n\n```\n\n\nBy the way, wouldn't it be better to call it `PolynomialBooleanRing` instead\nof `BooleanPolynomialRing`?  I suggest this for two reasons:\n1. It is PolyBoRi, after all, not BoPolyRi.\n2. The other Sage polynomial ring(s) starts with \"Polynomial\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/2146\n\n",
    "created_at": "2008-02-13T03:49:00Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "PolyBoRi random_element is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2146",
    "user": "was"
}
```
Assignee: malb

CC:  malb

See below. 


```
sage: R.<x,y,z> = BooleanPolynomialRing(3)
sage: R.random_element()
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/multi_polynomial_ring_generic.pyx in sage.rings.polynomial.multi_polynomial_ring_generic.MPolynomialRing_generic.random_element()

/Users/was/pbori.pyx in sage.rings.polynomial.pbori.BooleanPolynomialRing.__call__()

<type 'exceptions.TypeError'>: cannot convert <type 'dict'> to BooleanPolynomial
sage: 

```


By the way, wouldn't it be better to call it `PolynomialBooleanRing` instead
of `BooleanPolynomialRing`?  I suggest this for two reasons:
1. It is PolyBoRi, after all, not BoPolyRi.
2. The other Sage polynomial ring(s) starts with "Polynomial"

Issue created by migration from https://trac.sagemath.org/ticket/2146





---

archive/issue_comments_014080.json:
```json
{
    "body": "Renaming `BooleanPolynomialRing` is now #2149.",
    "created_at": "2008-02-13T18:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2146#issuecomment-14080",
    "user": "burcin"
}
```

Renaming `BooleanPolynomialRing` is now #2149.



---

archive/issue_comments_014081.json:
```json
{
    "body": "Add random_element to BooleanPolynomialRing",
    "created_at": "2008-02-17T14:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2146#issuecomment-14081",
    "user": "burcin"
}
```

Add random_element to BooleanPolynomialRing



---

archive/issue_comments_014082.json:
```json
{
    "body": "Attachment [2146-BooelanPolynomial_random_element.patch](tarball://root/attachments/some-uuid/ticket2146/2146-BooelanPolynomial_random_element.patch) by burcin created at 2008-02-17 16:40:48\n\nattachment:2146-BooelanPolynomial_random_element.patch adds a `random_element` method to `BooleanPolynomialRing`.\n\nThe doctests for errors work only after applying the patch for `sage-doctest` at ticket:2193.",
    "created_at": "2008-02-17T16:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2146#issuecomment-14082",
    "user": "burcin"
}
```

Attachment [2146-BooelanPolynomial_random_element.patch](tarball://root/attachments/some-uuid/ticket2146/2146-BooelanPolynomial_random_element.patch) by burcin created at 2008-02-17 16:40:48

attachment:2146-BooelanPolynomial_random_element.patch adds a `random_element` method to `BooleanPolynomialRing`.

The doctests for errors work only after applying the patch for `sage-doctest` at ticket:2193.



---

archive/issue_comments_014083.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-17T16:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2146#issuecomment-14083",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_014084.json:
```json
{
    "body": "Changing assignee from malb to burcin.",
    "created_at": "2008-02-17T16:40:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2146#issuecomment-14084",
    "user": "burcin"
}
```

Changing assignee from malb to burcin.



---

archive/issue_comments_014085.json:
```json
{
    "body": "Looks good to me.\n\nThe docstrings are not formatted nicely -- they should be wrapped at 78 chars.",
    "created_at": "2008-02-19T00:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2146#issuecomment-14085",
    "user": "ncalexan"
}
```

Looks good to me.

The docstrings are not formatted nicely -- they should be wrapped at 78 chars.



---

archive/issue_comments_014086.json:
```json
{
    "body": "Merged in Sage 2.10.2.alpha1",
    "created_at": "2008-02-19T15:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2146#issuecomment-14086",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.2.alpha1



---

archive/issue_comments_014087.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-19T15:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2146",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2146#issuecomment-14087",
    "user": "mabshoff"
}
```

Resolution: fixed
