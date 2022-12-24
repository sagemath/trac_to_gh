# Issue 280: Extensions should coerce defining polynomials into base fields

archive/issues_000280.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: extension base field polynomial\n\nClearly ZZ['x'] coerces into K['x'], so this should not be an error.\n\n\n```\nsage:K.<a> = NumberField(ZZ['x'].0^3 - 5)\n\nsage: L.<b> = K.extension(ZZ['x'].0^2 - 3)\n---------------------------------------------------------------------------\n<type 'exceptions.ValueError'>            Traceback (most recent call last)\n...\n    821         if polynomial.parent().base_ring() != base:\n--> 822             raise ValueError, \"The polynomial must be defined over the base field\"\n    823 \n    824         # Generate the nf and bnf corresponding to the base field\n\n<type 'exceptions.ValueError'>: The polynomial must be defined over the base field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/280\n\n",
    "created_at": "2007-02-23T19:56:45Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "Extensions should coerce defining polynomials into base fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/280",
    "user": "ncalexan"
}
```
Assignee: somebody

Keywords: extension base field polynomial

Clearly ZZ['x'] coerces into K['x'], so this should not be an error.


```
sage:K.<a> = NumberField(ZZ['x'].0^3 - 5)

sage: L.<b> = K.extension(ZZ['x'].0^2 - 3)
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)
...
    821         if polynomial.parent().base_ring() != base:
--> 822             raise ValueError, "The polynomial must be defined over the base field"
    823 
    824         # Generate the nf and bnf corresponding to the base field

<type 'exceptions.ValueError'>: The polynomial must be defined over the base field
```


Issue created by migration from https://trac.sagemath.org/ticket/280





---

archive/issue_comments_001331.json:
```json
{
    "body": "Changing assignee from somebody to ncalexan.",
    "created_at": "2007-02-24T03:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/280#issuecomment-1331",
    "user": "was"
}
```

Changing assignee from somebody to ncalexan.



---

archive/issue_comments_001332.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-01T14:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/280#issuecomment-1332",
    "user": "dmharvey"
}
```

Resolution: fixed



---

archive/issue_comments_001333.json:
```json
{
    "body": "This seems to work now:\n\n\n```\nsage: K.<a> = NumberField(ZZ['x'].0^3 - 5)\nsage: L.<b> = K.extension(ZZ['x'].0^2 - 3)\nsage: L\nNumber Field in b with defining polynomial x^2 - 3 over its base field\nsage: L.polynomial()\nx^2 - 3\nsage: L.polynomial().parent()\nUnivariate Polynomial Ring in x over Number Field in a with defining polynomial x^3 - 5\n```\n",
    "created_at": "2007-12-01T14:57:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/280",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/280#issuecomment-1333",
    "user": "dmharvey"
}
```

This seems to work now:


```
sage: K.<a> = NumberField(ZZ['x'].0^3 - 5)
sage: L.<b> = K.extension(ZZ['x'].0^2 - 3)
sage: L
Number Field in b with defining polynomial x^2 - 3 over its base field
sage: L.polynomial()
x^2 - 3
sage: L.polynomial().parent()
Univariate Polynomial Ring in x over Number Field in a with defining polynomial x^3 - 5
```

