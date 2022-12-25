# Issue 977: Schubert polynomials send 1 -> wrong polynomial ring

archive/issues_000977.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat\n\nIt seems that this is only happening with the identity element. Here's an example:\n\n```\nsage: R = SchubertPolynomialRing(ZZ)\nsage: f = R([1])\nsage: type(f.expand())\n<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>\nsage: f = R([1,2])\nsage: type(f.expand())\n<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>\n\n# But all of the polynomials returned should be multi-polynomials\n\nsage: f = R([1,3,2,4])\nsage: type(f.expand())\n<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/977\n\n",
    "created_at": "2007-10-23T21:06:30Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.9",
    "title": "Schubert polynomials send 1 -> wrong polynomial ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/977",
    "user": "https://github.com/rlmill"
}
```
Assignee: @mwhansen

CC:  sage-combinat

It seems that this is only happening with the identity element. Here's an example:

```
sage: R = SchubertPolynomialRing(ZZ)
sage: f = R([1])
sage: type(f.expand())
<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>
sage: f = R([1,2])
sage: type(f.expand())
<type 'sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl'>

# But all of the polynomials returned should be multi-polynomials

sage: f = R([1,3,2,4])
sage: type(f.expand())
<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>
```

Issue created by migration from https://trac.sagemath.org/ticket/977





---

archive/issue_events_002701.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-23T21:25:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/977",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/977#event-2701"
}
```



---

archive/issue_comments_005945.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-23T23:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/977#issuecomment-5945",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_events_002702.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-10-23T23:50:56Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/977",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/977#event-2702"
}
```



---

archive/issue_events_002703.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2007-10-23T23:50:56Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/977",
    "milestone": "sage-2.8.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/977#event-2703"
}
```



---

archive/issue_comments_005946.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-24T21:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/977#issuecomment-5946",
    "user": "https://github.com/malb"
}
```

Resolution: fixed



---

archive/issue_events_002704.json:
```json
{
    "actor": "https://github.com/malb",
    "created_at": "2007-10-24T21:48:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/977",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/977#event-2704"
}
```



---

archive/issue_comments_005947.json:
```json
{
    "body": "Attachment [schubert.patch](tarball://root/attachments/some-uuid/ticket977/schubert.patch) by @malb created at 2007-10-24 21:48:49\n\nthis is applied to 2.8.9.alpha1",
    "created_at": "2007-10-24T21:48:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/977#issuecomment-5947",
    "user": "https://github.com/malb"
}
```

Attachment [schubert.patch](tarball://root/attachments/some-uuid/ticket977/schubert.patch) by @malb created at 2007-10-24 21:48:49

this is applied to 2.8.9.alpha1
