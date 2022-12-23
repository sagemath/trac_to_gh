# Issue 1960: bug when reducing Gröbner basis

archive/issues_001960.json:
```json
{
    "body": "Assignee: malb\n\nThis bug was reported by James Carlson:\n\n\n```\nsage: R.<u,v> = PolynomialRing(QQ)\nsage: g = u^4 + v^4 + u^3 + v^3\nsage: I = ideal(g) + ideal(g.jacob())\nsage: I.dimension()\n0\nsage: PD = I.primary_decomposition()\nsage: len(PD)\n1\nsage: P = PD[0]\nsage: I == P\nTrue\nsage: I.vector_space_dimension()\n9 \nsage: P.vector_space_dimension()\n4 # <<<<<<<<<<<<< doesn't match\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1960\n\n",
    "created_at": "2008-01-28T14:48:54Z",
    "labels": [
        "commutative algebra",
        "critical",
        "bug"
    ],
    "title": "bug when reducing Gr\u00f6bner basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1960",
    "user": "malb"
}
```
Assignee: malb

This bug was reported by James Carlson:


```
sage: R.<u,v> = PolynomialRing(QQ)
sage: g = u^4 + v^4 + u^3 + v^3
sage: I = ideal(g) + ideal(g.jacob())
sage: I.dimension()
0
sage: PD = I.primary_decomposition()
sage: len(PD)
1
sage: P = PD[0]
sage: I == P
True
sage: I.vector_space_dimension()
9 
sage: P.vector_space_dimension()
4 # <<<<<<<<<<<<< doesn't match
```


Issue created by migration from https://trac.sagemath.org/ticket/1960





---

archive/issue_comments_012655.json:
```json
{
    "body": "Attachment\n\nIn fact, the behaviour was correct in the sense that the specification (documentation) and the code agreed. However, this was at least counter intuitive. This method returned the vector space dimension of the ring modulo the leading terms of the generators of the ideal rather than modulo the ideal. This makes sense in the context of Singular where an ideal is identified with its generators but it doesn't make sense in the context of Sage where this identification is not true. Thus, now allways the vector space dimension of ring modulo the ideal is returned.",
    "created_at": "2008-01-28T15:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1960#issuecomment-12655",
    "user": "malb"
}
```

Attachment

In fact, the behaviour was correct in the sense that the specification (documentation) and the code agreed. However, this was at least counter intuitive. This method returned the vector space dimension of the ring modulo the leading terms of the generators of the ideal rather than modulo the ideal. This makes sense in the context of Singular where an ideal is identified with its generators but it doesn't make sense in the context of Sage where this identification is not true. Thus, now allways the vector space dimension of ring modulo the ideal is returned.



---

archive/issue_comments_012656.json:
```json
{
    "body": "Changes look good, and sage -t is happy.",
    "created_at": "2008-01-31T01:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1960#issuecomment-12656",
    "user": "AlexGhitza"
}
```

Changes look good, and sage -t is happy.



---

archive/issue_comments_012657.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc4",
    "created_at": "2008-02-01T00:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1960#issuecomment-12657",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc4



---

archive/issue_comments_012658.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-01T00:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1960#issuecomment-12658",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012659.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc4",
    "created_at": "2008-02-01T00:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1960#issuecomment-12659",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.rc4
