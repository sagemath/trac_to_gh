# Issue 2620: [with patch, needs review] generator generator support for ideal

archive/issues_002620.json:
```json
{
    "body": "Assignee: @malb\n\nPython has a generator type which is cool and now this works:\n\n\n```\nP.<a,b,c,d,e> = PolynomialRing(GF(2), 5, order='lex')\nI1 = ideal([a*b + c*d + 1, a*c*e + d*e, a*b*e + c*e, b*c + c*d*e + 1])\nQ = P.quotient( sage.rings.ideal.FieldIdeal(P) )\nI2 = ideal( Q(f) for f in I1.gens() ) # note we don't construct a list\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2620\n\n",
    "created_at": "2008-03-20T22:15:35Z",
    "labels": [
        "commutative algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] generator generator support for ideal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2620",
    "user": "@malb"
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

archive/issue_comments_017995.json:
```json
{
    "body": "Attachment [generator_generator.patch](tarball://root/attachments/some-uuid/ticket2620/generator_generator.patch) by mabshoff created at 2008-04-01 14:30:40\n\nPatch looks good to me. Doctests pass. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-01T14:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2620#issuecomment-17995",
    "user": "mabshoff"
}
```

Attachment [generator_generator.patch](tarball://root/attachments/some-uuid/ticket2620/generator_generator.patch) by mabshoff created at 2008-04-01 14:30:40

Patch looks good to me. Doctests pass. Positive review.

Cheers,

Michael



---

archive/issue_comments_017996.json:
```json
{
    "body": "Merged in Sage 3.0.alpha0",
    "created_at": "2008-04-01T14:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2620#issuecomment-17996",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha0



---

archive/issue_comments_017997.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-01T14:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2620#issuecomment-17997",
    "user": "mabshoff"
}
```

Resolution: fixed
