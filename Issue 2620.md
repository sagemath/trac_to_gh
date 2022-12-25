# Issue 2620: [with patch, positive review] generator generator support for ideal

archive/issues_002620.json:
```json
{
    "body": "Assignee: @malb\n\nPython has a generator type which is cool and now this works:\n\n```\nP.<a,b,c,d,e> = PolynomialRing(GF(2), 5, order='lex')\nI1 = ideal([a*b + c*d + 1, a*c*e + d*e, a*b*e + c*e, b*c + c*d*e + 1])\nQ = P.quotient( sage.rings.ideal.FieldIdeal(P) )\nI2 = ideal( Q(f) for f in I1.gens() ) # note we don't construct a list\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2620\n\n",
    "closed_at": "2008-04-01T14:30:59Z",
    "created_at": "2008-03-20T22:15:35Z",
    "labels": [
        "component: commutative algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, positive review] generator generator support for ideal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2620",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

Python has a generator type which is cool and now this works:

```
P.<a,b,c,d,e> = PolynomialRing(GF(2), 5, order='lex')
I1 = ideal([a*b + c*d + 1, a*c*e + d*e, a*b*e + c*e, b*c + c*d*e + 1])
Q = P.quotient( sage.rings.ideal.FieldIdeal(P) )
I2 = ideal( Q(f) for f in I1.gens() ) # note we don't construct a list
```

Issue created by migration from https://trac.sagemath.org/ticket/2620





---

archive/issue_comments_017956.json:
```json
{
    "body": "Attachment [generator_generator.patch](tarball://root/attachments/some-uuid/ticket2620/generator_generator.patch) by mabshoff created at 2008-04-01 14:30:40\n\nPatch looks good to me. Doctests pass. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-01T14:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2620#issuecomment-17956",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [generator_generator.patch](tarball://root/attachments/some-uuid/ticket2620/generator_generator.patch) by mabshoff created at 2008-04-01 14:30:40

Patch looks good to me. Doctests pass. Positive review.

Cheers,

Michael



---

archive/issue_comments_017957.json:
```json
{
    "body": "Merged in Sage 3.0.alpha0",
    "created_at": "2008-04-01T14:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2620#issuecomment-17957",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha0



---

archive/issue_events_006123.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-01T14:30:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2620",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2620#event-6123"
}
```



---

archive/issue_comments_017958.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-01T14:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2620#issuecomment-17958",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
