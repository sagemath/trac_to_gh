# Issue 2611: [with patch, needs review] add monomial_coefficent to boolean polynomials

archive/issues_002611.json:
```json
{
    "body": "Assignee: malb\n\nCC:  burcin\n\nWith the attached patch this works:\n\n```\nsage: sr = mq.SR(gf2=True)\nsage: sr\nSR(1,1,1,4)\n\nsage: F,s = sr.polynomial_system()\nsage: R = F.ring()\nsage: B = BooleanPolynomialRing(R.ngens(),R.variable_names(),R.term_order())\nsage: F = [B(f) for f in F]\nsage: F = mq.MPolynomialSystem(B,F)\nsage: F\nPolynomial System with 56 Polynomials in 20 Variables\nsage: A,v = F.coefficient_matrix() # this relies on monomial_coefficient\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2611\n\n",
    "created_at": "2008-03-20T11:53:32Z",
    "labels": [
        "commutative algebra",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] add monomial_coefficent to boolean polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2611",
    "user": "malb"
}
```
Assignee: malb

CC:  burcin

With the attached patch this works:

```
sage: sr = mq.SR(gf2=True)
sage: sr
SR(1,1,1,4)

sage: F,s = sr.polynomial_system()
sage: R = F.ring()
sage: B = BooleanPolynomialRing(R.ngens(),R.variable_names(),R.term_order())
sage: F = [B(f) for f in F]
sage: F = mq.MPolynomialSystem(B,F)
sage: F
Polynomial System with 56 Polynomials in 20 Variables
sage: A,v = F.coefficient_matrix() # this relies on monomial_coefficient
```


Issue created by migration from https://trac.sagemath.org/ticket/2611





---

archive/issue_comments_017920.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-20T11:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2611#issuecomment-17920",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_017921.json:
```json
{
    "body": "I'm concerned by this:\n\n```\nsage: R.<x,y,z,a,b,c>=BooleanPolynomialRing(6)\nsage: f=(1-x)*(1+y)\nsage: f\nx*y + x + y + 1\nsage: f.monomial_coefficient(1)  # Shouldn't this return 1?\n0\nsage: f.monomial_coefficient(x^0)\n1\n```\n\nI think a little bit of type checking would improve things.\n\nI also notice that we don't have a coefficient method like the other mpoly rings.  However, I don't think we should let lack of associated functionality hold up a patch providing functionality.",
    "created_at": "2008-03-20T12:26:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2611#issuecomment-17921",
    "user": "jbmohler"
}
```

I'm concerned by this:

```
sage: R.<x,y,z,a,b,c>=BooleanPolynomialRing(6)
sage: f=(1-x)*(1+y)
sage: f
x*y + x + y + 1
sage: f.monomial_coefficient(1)  # Shouldn't this return 1?
0
sage: f.monomial_coefficient(x^0)
1
```

I think a little bit of type checking would improve things.

I also notice that we don't have a coefficient method like the other mpoly rings.  However, I don't think we should let lack of associated functionality hold up a patch providing functionality.



---

archive/issue_comments_017922.json:
```json
{
    "body": "Attachment\n\nThe attached patch fixes the issue with different types.",
    "created_at": "2008-03-20T13:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2611#issuecomment-17922",
    "user": "malb"
}
```

Attachment

The attached patch fixes the issue with different types.



---

archive/issue_comments_017923.json:
```json
{
    "body": "Looks good to me, and Joel's concerns have been addressed.",
    "created_at": "2008-03-28T14:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2611#issuecomment-17923",
    "user": "AlexGhitza"
}
```

Looks good to me, and Joel's concerns have been addressed.



---

archive/issue_comments_017924.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-28T15:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2611#issuecomment-17924",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2



---

archive/issue_comments_017925.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T15:14:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2611",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2611#issuecomment-17925",
    "user": "mabshoff"
}
```

Resolution: fixed
