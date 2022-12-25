# Issue 430: RDF poly's don't factor

archive/issues_000430.json:
```json
{
    "body": "Assignee: @rlmill\n\nKeywords: RDF factor\n\npolynomial_element.Polynomial.factor doesn't\nknow what to do with the RDF ring.\n\nhttp://www.gnu.org/software/gsl/manual/html_node/Polynomials.html\n\nsage: import numpy\n\nsage:  numpy.roots?\n\nThe values in the rank-1 array p are coefficients of a polynomial. If the length of p is n+1 then the polynomial is\n\np[0] * x**n + p[1] * x**(n-1) + ... + p[n-1]*x + p[n]\n\nsage: a=numpy.array([1,0,1],dtype=float)\nsage: numpy.roots(a) \n\nIssue created by migration from https://trac.sagemath.org/ticket/430\n\n",
    "created_at": "2007-08-16T03:10:55Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.2",
    "title": "RDF poly's don't factor",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/430",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

Keywords: RDF factor

polynomial_element.Polynomial.factor doesn't
know what to do with the RDF ring.

http://www.gnu.org/software/gsl/manual/html_node/Polynomials.html

sage: import numpy

sage:  numpy.roots?

The values in the rank-1 array p are coefficients of a polynomial. If the length of p is n+1 then the polynomial is

p[0] * x**n + p[1] * x**(n-1) + ... + p[n-1]*x + p[n]

sage: a=numpy.array([1,0,1],dtype=float)
sage: numpy.roots(a) 

Issue created by migration from https://trac.sagemath.org/ticket/430





---

archive/issue_comments_002146.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-08-18T16:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/430#issuecomment-2146",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002147.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2007-08-18T19:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/430#issuecomment-2147",
    "user": "https://github.com/rlmill"
}
```

Resolution: worksforme



---

archive/issue_comments_002148.json:
```json
{
    "body": "The factoring now works, but it depends on root finding, which currently sucks. A new ticket will be made for the root problem.",
    "created_at": "2007-08-18T19:15:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/430#issuecomment-2148",
    "user": "https://github.com/rlmill"
}
```

The factoring now works, but it depends on root finding, which currently sucks. A new ticket will be made for the root problem.
