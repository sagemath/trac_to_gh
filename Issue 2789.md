# Issue 2789: multivariate polynomials over residue fields of number fields are broken

archive/issues_002789.json:
```json
{
    "body": "Assignee: somebody\n\nThis example from Genya Zaytman:\n\n\n```\nsage: F1.<u> = NumberField(x^6 + 6*x^5 + 124*x^4 + 452*x^3 + 4336*x^2 + 8200*x + 42316)\nsage: reduct_id = F1.factor_integer(47)[0][0]\nsage: Rf = F1.residue_field(reduct_id)   # = GF(47^3)\nsage: R1.<X,Y> = PolynomialRing(Rf)\nsage: ubar = Rf(u)\nsage: I = ideal([ubar*X+Y])\nsage: I.groebner_basis()\n[boom]\n```\n\n\nBasically all we're doing is working with polynomials over a finite field. Perhaps the singular interface can't handle the way the field is presented, or something like that.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2789\n\n",
    "created_at": "2008-04-03T03:50:11Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "multivariate polynomials over residue fields of number fields are broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2789",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: somebody

This example from Genya Zaytman:


```
sage: F1.<u> = NumberField(x^6 + 6*x^5 + 124*x^4 + 452*x^3 + 4336*x^2 + 8200*x + 42316)
sage: reduct_id = F1.factor_integer(47)[0][0]
sage: Rf = F1.residue_field(reduct_id)   # = GF(47^3)
sage: R1.<X,Y> = PolynomialRing(Rf)
sage: ubar = Rf(u)
sage: I = ideal([ubar*X+Y])
sage: I.groebner_basis()
[boom]
```


Basically all we're doing is working with polynomials over a finite field. Perhaps the singular interface can't handle the way the field is presented, or something like that.


Issue created by migration from https://trac.sagemath.org/ticket/2789





---

archive/issue_events_006440.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-03T21:17:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2789#event-6440"
}
```



---

archive/issue_comments_019115.json:
```json
{
    "body": "This now works without major changes... but I found a show stopper bug.  It had to do with hashing \"large\" residue fields, meaning large characteristic residue fields.  The hash method tried to hash an ideal of the residue field itself, which tried to hash its parent, leading to an infinite loop.\n\nThis means that at no time has a residue field with cardinality a very large prime been created in Sage!\n\nI've added the obvious .ideal() method, tested the hashing and construction for larger examples, and added doctests showing Groebner basis computations.",
    "created_at": "2009-01-22T09:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2789#issuecomment-19115",
    "user": "https://github.com/ncalexan"
}
```

This now works without major changes... but I found a show stopper bug.  It had to do with hashing "large" residue fields, meaning large characteristic residue fields.  The hash method tried to hash an ideal of the residue field itself, which tried to hash its parent, leading to an infinite loop.

This means that at no time has a residue field with cardinality a very large prime been created in Sage!

I've added the obvious .ideal() method, tested the hashing and construction for larger examples, and added doctests showing Groebner basis computations.



---

archive/issue_comments_019116.json:
```json
{
    "body": "Changing component from basic arithmetic to commutative algebra.",
    "created_at": "2009-01-22T09:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2789#issuecomment-19116",
    "user": "https://github.com/ncalexan"
}
```

Changing component from basic arithmetic to commutative algebra.



---

archive/issue_comments_019117.json:
```json
{
    "body": "Changing assignee from somebody to @malb.",
    "created_at": "2009-01-22T09:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2789#issuecomment-19117",
    "user": "https://github.com/ncalexan"
}
```

Changing assignee from somebody to @malb.



---

archive/issue_comments_019118.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-01-22T09:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2789#issuecomment-19118",
    "user": "https://github.com/ncalexan"
}
```

Changing priority from major to critical.



---

archive/issue_comments_019119.json:
```json
{
    "body": "Changing keywords from \"\" to \"residue field multivariate prime groebner basis\".",
    "created_at": "2009-01-22T09:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2789#issuecomment-19119",
    "user": "https://github.com/ncalexan"
}
```

Changing keywords from "" to "residue field multivariate prime groebner basis".



---

archive/issue_comments_019120.json:
```json
{
    "body": "Attachment [trac_2789.2.patch](tarball://root/attachments/some-uuid/ticket2789/trac_2789.2.patch) by @malb created at 2009-01-22 19:12:06\n\nreplaces some line numbers in verbose output by ...",
    "created_at": "2009-01-22T19:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2789#issuecomment-19120",
    "user": "https://github.com/malb"
}
```

Attachment [trac_2789.2.patch](tarball://root/attachments/some-uuid/ticket2789/trac_2789.2.patch) by @malb created at 2009-01-22 19:12:06

replaces some line numbers in verbose output by ...



---

archive/issue_comments_019121.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-23T02:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2789#issuecomment-19121",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_006441.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T02:33:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2789#event-6441"
}
```



---

archive/issue_events_006442.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T02:33:12Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2789#event-6442"
}
```



---

archive/issue_events_006443.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-23T02:33:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2789#event-6443"
}
```



---

archive/issue_comments_019122.json:
```json
{
    "body": "Merged in Sage 3.3.alpha1",
    "created_at": "2009-01-23T02:33:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2789#issuecomment-19122",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha1
