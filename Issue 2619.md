# Issue 2619: [with patch, needs review] Gröbner bases over quotient rings

archive/issues_002619.json:
```json
{
    "body": "Assignee: malb\n\nAfter the patch was applied (which depends on #2618) this should work again:\n\n```\nsage: P.<a,b,c,d,e> = PolynomialRing(GF(2), 5, order='lex')\nsage: I1 = ideal([a*b + c*d + 1, a*c*e + d*e, a*b*e + c*e, b*c + c*d*e + 1])\nsage: Q = P.quotient( sage.rings.ideal.FieldIdeal(P) )\nsage: I2 = ideal([Q(f) for f in I1.gens()])\nsage: I2.groebner_basis()\n[ebar, cbar + 1, bbar + 1, abar + dbar + 1]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2619\n\n",
    "created_at": "2008-03-20T21:58:52Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] Gr\u00f6bner bases over quotient rings",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2619",
    "user": "malb"
}
```
Assignee: malb

After the patch was applied (which depends on #2618) this should work again:

```
sage: P.<a,b,c,d,e> = PolynomialRing(GF(2), 5, order='lex')
sage: I1 = ideal([a*b + c*d + 1, a*c*e + d*e, a*b*e + c*e, b*c + c*d*e + 1])
sage: Q = P.quotient( sage.rings.ideal.FieldIdeal(P) )
sage: I2 = ideal([Q(f) for f in I1.gens()])
sage: I2.groebner_basis()
[ebar, cbar + 1, bbar + 1, abar + dbar + 1]
```


Issue created by migration from https://trac.sagemath.org/ticket/2619





---

archive/issue_comments_017992.json:
```json
{
    "body": "Attachment\n\nLooks good to me.",
    "created_at": "2008-03-21T02:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2619#issuecomment-17992",
    "user": "mhansen"
}
```

Attachment

Looks good to me.



---

archive/issue_comments_017993.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-21T02:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2619#issuecomment-17993",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_comments_017994.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T02:23:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2619#issuecomment-17994",
    "user": "mabshoff"
}
```

Resolution: fixed
