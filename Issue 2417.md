# Issue 2417: discriminant method sometimes returns values in the fraction field

archive/issues_002417.json:
```json
{
    "body": "Assignee: @williamstein\n\nFor non-monic polynomials, the discriminant method introduced in #2392 returns values in the fraction field of the base ring, instead of in the base ring.\n\n```\nsage: R.<y> = QQ[]\nsage: S.<x> = R[]\nsage: (x*y+x+y+1).discriminant()\n1\nsage: (x*y+x+y+1).discriminant().parent()\nFraction Field of Univariate Polynomial Ring in y over Rational Field\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2417\n\n",
    "created_at": "2008-03-07T04:43:09Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "discriminant method sometimes returns values in the fraction field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2417",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @williamstein

For non-monic polynomials, the discriminant method introduced in #2392 returns values in the fraction field of the base ring, instead of in the base ring.

```
sage: R.<y> = QQ[]
sage: S.<x> = R[]
sage: (x*y+x+y+1).discriminant()
1
sage: (x*y+x+y+1).discriminant().parent()
Fraction Field of Univariate Polynomial Ring in y over Rational Field
```



Issue created by migration from https://trac.sagemath.org/ticket/2417





---

archive/issue_events_005700.json:
```json
{
    "actor": "https://github.com/aghitza",
    "created_at": "2008-03-24T02:16:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2417",
    "milestone": "sage-2.11",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2417#event-5700"
}
```



---

archive/issue_comments_016265.json:
```json
{
    "body": "Attachment [2417_discriminant.patch](tarball://root/attachments/some-uuid/ticket2417/2417_discriminant.patch) by @aghitza created at 2008-03-24 02:16:34\n\nThis is due to the fact that discriminants are computed via resultants, using a formula that sometimes divides the resultant by the leading coefficient.  When the coefficients are themselves polynomials, this makes the result appear in the fraction field.\n\nThe fix is very simple: just coerce the result back into the base ring before returning.  This is in the attached patch, together with a couple of typo fixes.  I've also replaced one of the doctests that was supposed to illustrate precisely this behavior (but didn't) with Carl's example.",
    "created_at": "2008-03-24T02:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2417#issuecomment-16265",
    "user": "https://github.com/aghitza"
}
```

Attachment [2417_discriminant.patch](tarball://root/attachments/some-uuid/ticket2417/2417_discriminant.patch) by @aghitza created at 2008-03-24 02:16:34

This is due to the fact that discriminants are computed via resultants, using a formula that sometimes divides the resultant by the leading coefficient.  When the coefficients are themselves polynomials, this makes the result appear in the fraction field.

The fix is very simple: just coerce the result back into the base ring before returning.  This is in the attached patch, together with a couple of typo fixes.  I've also replaced one of the doctests that was supposed to illustrate precisely this behavior (but didn't) with Carl's example.



---

archive/issue_comments_016266.json:
```json
{
    "body": "Works well for me.",
    "created_at": "2008-03-26T06:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2417#issuecomment-16266",
    "user": "https://github.com/robertwb"
}
```

Works well for me.



---

archive/issue_comments_016267.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-26T22:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2417#issuecomment-16267",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016268.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-26T22:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2417",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2417#issuecomment-16268",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_events_005701.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-26T22:09:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2417",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2417#event-5701"
}
```
