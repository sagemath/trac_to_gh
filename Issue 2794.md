# Issue 2794: [with patch, needs review] PolyBoRi to Magma conversion

archive/issues_002794.json:
```json
{
    "body": "Assignee: malb\n\nCC:  burcin\n\nKeywords: polybori, magma\n\nThis now works:\n\n```\nsage: B.<a,b,z> = BooleanPolynomialRing(3)\nsage: B._magma_()\n\nAffine Algebra of rank 3 over GF(2)\nLexicographical Order\nVariables: a, b, z\nQuotient relations:\n[\na^2 + a,\nb^2 + b,\nz^2 + z\n]\nsage: magma(a+b)\na + b\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2794\n\n",
    "created_at": "2008-04-04T09:50:44Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] PolyBoRi to Magma conversion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2794",
    "user": "malb"
}
```
Assignee: malb

CC:  burcin

Keywords: polybori, magma

This now works:

```
sage: B.<a,b,z> = BooleanPolynomialRing(3)
sage: B._magma_()

Affine Algebra of rank 3 over GF(2)
Lexicographical Order
Variables: a, b, z
Quotient relations:
[
a^2 + a,
b^2 + b,
z^2 + z
]
sage: magma(a+b)
a + b
```


Issue created by migration from https://trac.sagemath.org/ticket/2794





---

archive/issue_comments_019185.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-04T09:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2794#issuecomment-19185",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_019186.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-04T21:29:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2794#issuecomment-19186",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_019187.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T22:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2794#issuecomment-19187",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019188.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T22:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2794#issuecomment-19188",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha1
