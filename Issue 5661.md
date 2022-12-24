# Issue 5661: implement numerical_diff and generalize numerical_integral

archive/issues_005661.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  jkantor\n\nKeywords: numerical integration differentiation\n\nsage does not differentiate numerically at this time; a `numerical_diff` similar to Maple's `fdiff` would have helped me implement Riemann theta functions.\n\nsage's `numerical_integral` uses GSL, which means it only handles RDF.  Weak!\n\nIssue created by migration from https://trac.sagemath.org/ticket/5661\n\n",
    "created_at": "2009-04-01T21:31:26Z",
    "labels": [
        "numerical",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "implement numerical_diff and generalize numerical_integral",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5661",
    "user": "@ncalexan"
}
```
Assignee: jkantor

CC:  jkantor

Keywords: numerical integration differentiation

sage does not differentiate numerically at this time; a `numerical_diff` similar to Maple's `fdiff` would have helped me implement Riemann theta functions.

sage's `numerical_integral` uses GSL, which means it only handles RDF.  Weak!

Issue created by migration from https://trac.sagemath.org/ticket/5661





---

archive/issue_comments_044260.json:
```json
{
    "body": "Pari can do arbitrary precision numerical integration.  It would be cool if you could make a version of numerical_integral that uses PARI instead, and is hence arbitrary precision.    It would likely be a lot lot slower than the GSL-based numerical_integral, though.",
    "created_at": "2009-04-02T15:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5661#issuecomment-44260",
    "user": "@williamstein"
}
```

Pari can do arbitrary precision numerical integration.  It would be cool if you could make a version of numerical_integral that uses PARI instead, and is hence arbitrary precision.    It would likely be a lot lot slower than the GSL-based numerical_integral, though.



---

archive/issue_comments_044261.json:
```json
{
    "body": "Arbitrary-precision integration and differentiation is also available in mpmath.",
    "created_at": "2009-04-02T20:46:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5661#issuecomment-44261",
    "user": "@fredrik-johansson"
}
```

Arbitrary-precision integration and differentiation is also available in mpmath.



---

archive/issue_comments_044262.json:
```json
{
    "body": "> Arbitrary-precision integration and differentiation is also available in mpmath. \n\nCool.  And in case people don't know, mpmath is in Sage.\n\n```\nsage: import sympy.mpmath\nsage: sympy.mpmath.\nDisplay all 206 possibilities? (y or n)\n```\n",
    "created_at": "2009-04-02T23:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5661",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5661#issuecomment-44262",
    "user": "@williamstein"
}
```

> Arbitrary-precision integration and differentiation is also available in mpmath. 

Cool.  And in case people don't know, mpmath is in Sage.

```
sage: import sympy.mpmath
sage: sympy.mpmath.
Display all 206 possibilities? (y or n)
```

