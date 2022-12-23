# Issue 4289: EllipticCurve behaviour

archive/issues_004289.json:
```json
{
    "body": "Assignee: was\n\nIf one types in\n`EllipticCurve(1,2)`\nthen one gets\n\n`Elliptic Curve defined by y^2  = x^3 + 5181*x - 5965058 over Rational Field`\n\nthis seemingly unrelated curve has j-invariant 1 and the 2 is ignored. Could the EllipticCurve function test for the presence of two numerical inputs and either raise an error or cast it to\n`EllipticCurve([1,2])`?\n\nIssue created by migration from https://trac.sagemath.org/ticket/4289\n\n",
    "created_at": "2008-10-14T21:30:29Z",
    "labels": [
        "number theory",
        "minor",
        "bug"
    ],
    "title": "EllipticCurve behaviour",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4289",
    "user": "ljpk"
}
```
Assignee: was

If one types in
`EllipticCurve(1,2)`
then one gets

`Elliptic Curve defined by y^2  = x^3 + 5181*x - 5965058 over Rational Field`

this seemingly unrelated curve has j-invariant 1 and the 2 is ignored. Could the EllipticCurve function test for the presence of two numerical inputs and either raise an error or cast it to
`EllipticCurve([1,2])`?

Issue created by migration from https://trac.sagemath.org/ticket/4289





---

archive/issue_comments_031392.json:
```json
{
    "body": "This should be an easy fix.",
    "created_at": "2008-10-14T21:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4289#issuecomment-31392",
    "user": "robertwb"
}
```

This should be an easy fix.



---

archive/issue_comments_031393.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-14T21:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4289#issuecomment-31393",
    "user": "robertwb"
}
```

Attachment



---

archive/issue_comments_031394.json:
```json
{
    "body": "I think raising an error is the most consistent thing to do.",
    "created_at": "2008-10-14T21:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4289#issuecomment-31394",
    "user": "robertwb"
}
```

I think raising an error is the most consistent thing to do.



---

archive/issue_comments_031395.json:
```json
{
    "body": "Positive review. I notice there is no doctest for EllipticCurve(j). It would be good to add one.\nAlso the doc is inconsistent wrt 'Returns' vs 'Return'.",
    "created_at": "2008-10-15T07:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4289#issuecomment-31395",
    "user": "zimmerma"
}
```

Positive review. I notice there is no doctest for EllipticCurve(j). It would be good to add one.
Also the doc is inconsistent wrt 'Returns' vs 'Return'.



---

archive/issue_comments_031396.json:
```json
{
    "body": "This trac and the last comment is linked to the old Ticket #128.\nAs noted there, we should remove `EllipticCurve(j)` from the possible ways of defining an elliptic curve anyway.",
    "created_at": "2008-10-15T09:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4289#issuecomment-31396",
    "user": "wuthrich"
}
```

This trac and the last comment is linked to the old Ticket #128.
As noted there, we should remove `EllipticCurve(j)` from the possible ways of defining an elliptic curve anyway.



---

archive/issue_comments_031397.json:
```json
{
    "body": "Merged in Sage 3.1.4.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-15T20:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4289#issuecomment-31397",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.4.

Cheers,

Michael



---

archive/issue_comments_031398.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-15T20:29:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4289",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4289#issuecomment-31398",
    "user": "mabshoff"
}
```

Resolution: fixed
