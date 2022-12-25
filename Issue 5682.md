# Issue 5682: Quotient for univariate Laurent polynomials

archive/issues_005682.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: Laurent polynomial, quotient, division\n\nIt would be nice if this worked rather than returning an error:\n\n```\nsage: F.<t> = LaurentPolynomialRing(GF(2))\nsage: t // t\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/kedlaya/.sage/temp/kedlaya_laptop/18179/_home_kedlaya__sage_init_sage_0.py in <module>()\n\nTypeError: unsupported operand type(s) for //: 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair' and 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair'\n```\n\nAs it stands, I don't think univariate Laurent polynomial rings over a field support any division operation that stays within the ring:\n\n```\nsage: (t/t).parent()\nFraction Field of Univariate Laurent Polynomial Ring in t over Finite Field of size 2\n```\n\nexcept maybe if I access the internal representation (as a quotient ring) and implement it by hand.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5682\n\n",
    "created_at": "2009-04-04T14:55:46Z",
    "labels": [
        "component: algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Quotient for univariate Laurent polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5682",
    "user": "https://github.com/kedlaya"
}
```
Assignee: tbd

Keywords: Laurent polynomial, quotient, division

It would be nice if this worked rather than returning an error:

```
sage: F.<t> = LaurentPolynomialRing(GF(2))
sage: t // t
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/kedlaya/.sage/temp/kedlaya_laptop/18179/_home_kedlaya__sage_init_sage_0.py in <module>()

TypeError: unsupported operand type(s) for //: 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair' and 'sage.rings.polynomial.laurent_polynomial.LaurentPolynomial_mpair'
```

As it stands, I don't think univariate Laurent polynomial rings over a field support any division operation that stays within the ring:

```
sage: (t/t).parent()
Fraction Field of Univariate Laurent Polynomial Ring in t over Finite Field of size 2
```

except maybe if I access the internal representation (as a quotient ring) and implement it by hand.


Issue created by migration from https://trac.sagemath.org/ticket/5682





---

archive/issue_comments_044351.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-04-09T04:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5682#issuecomment-44351",
    "user": "https://github.com/tscrim"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044352.json:
```json
{
    "body": "This is done in #11726.",
    "created_at": "2014-04-09T04:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5682#issuecomment-44352",
    "user": "https://github.com/tscrim"
}
```

This is done in #11726.



---

archive/issue_comments_044353.json:
```json
{
    "body": "Agreed, thanks!",
    "created_at": "2014-04-09T17:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5682#issuecomment-44353",
    "user": "https://github.com/kedlaya"
}
```

Agreed, thanks!



---

archive/issue_comments_044354.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-04-09T17:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5682#issuecomment-44354",
    "user": "https://github.com/kedlaya"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044355.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-04-09T19:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5682",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5682#issuecomment-44355",
    "user": "https://github.com/vbraun"
}
```

Resolution: duplicate



---

archive/issue_events_005924.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-04-09T19:42:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5682",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5682#event-5924"
}
```
