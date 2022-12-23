# Issue 254: p-adic precision drop in evaluating a polynomial

archive/issues_000254.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: R = pAdicField(5)\n\nsage: T.<u> = PolynomialRing(R)\n\nsage: h = u + (1 + O(5^8))*u^2 + (1 + O(5^4))*u^3\n\nsage: h(u)\n (1 + O(5^4))*u^3 + (1 + O(5^4))*u^2 + (1 + O(5^4))*u\n```\n\n\nIt looks like the precision of all the coefficient is dropping to that of the lowest precision of the other coefficients. It's not clear to me why the precision is dropping. [What I really want to do is evaluate h(2*u), which should just multiply each coefficient by the appropriate power of 2.]\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/254\n\n",
    "created_at": "2007-02-09T21:16:13Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "p-adic precision drop in evaluating a polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/254",
    "user": "dmharvey"
}
```
Assignee: somebody


```
sage: R = pAdicField(5)

sage: T.<u> = PolynomialRing(R)

sage: h = u + (1 + O(5^8))*u^2 + (1 + O(5^4))*u^3

sage: h(u)
 (1 + O(5^4))*u^3 + (1 + O(5^4))*u^2 + (1 + O(5^4))*u
```


It looks like the precision of all the coefficient is dropping to that of the lowest precision of the other coefficients. It's not clear to me why the precision is dropping. [What I really want to do is evaluate h(2*u), which should just multiply each coefficient by the appropriate power of 2.]


Issue created by migration from https://trac.sagemath.org/ticket/254





---

archive/issue_comments_001145.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-18T18:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/254#issuecomment-1145",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_001146.json:
```json
{
    "body": "David Roe fixed this with his new p-adic polynomials class.",
    "created_at": "2007-08-18T18:10:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/254#issuecomment-1146",
    "user": "was"
}
```

David Roe fixed this with his new p-adic polynomials class.
