# Issue 1960: bug when reducing Gröbner basis

archive/issues_001960.json:
```json
{
    "body": "Assignee: @malb\n\nThis bug was reported by James Carlson:\n\n\n```\nsage: R.<u,v> = PolynomialRing(QQ)\nsage: g = u^4 + v^4 + u^3 + v^3\nsage: I = ideal(g) + ideal(g.jacob())\nsage: I.dimension()\n0\nsage: PD = I.primary_decomposition()\nsage: len(PD)\n1\nsage: P = PD[0]\nsage: I == P\nTrue\nsage: I.vector_space_dimension()\n9 \nsage: P.vector_space_dimension()\n4 # <<<<<<<<<<<<< doesn't match\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1960\n\n",
    "created_at": "2008-01-28T14:48:54Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "bug when reducing Gr\u00f6bner basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1960",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

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

archive/issue_comments_012624.json:
```json
{
    "body": "Attachment [trac_1960_vdim.patch](tarball://root/attachments/some-uuid/ticket1960/trac_1960_vdim.patch) by @malb created at 2008-01-28 15:10:20\n\nIn fact, the behaviour was correct in the sense that the specification (documentation) and the code agreed. However, this was at least counter intuitive. This method returned the vector space dimension of the ring modulo the leading terms of the generators of the ideal rather than modulo the ideal. This makes sense in the context of Singular where an ideal is identified with its generators but it doesn't make sense in the context of Sage where this identification is not true. Thus, now allways the vector space dimension of ring modulo the ideal is returned.",
    "created_at": "2008-01-28T15:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1960#issuecomment-12624",
    "user": "https://github.com/malb"
}
```

Attachment [trac_1960_vdim.patch](tarball://root/attachments/some-uuid/ticket1960/trac_1960_vdim.patch) by @malb created at 2008-01-28 15:10:20

In fact, the behaviour was correct in the sense that the specification (documentation) and the code agreed. However, this was at least counter intuitive. This method returned the vector space dimension of the ring modulo the leading terms of the generators of the ideal rather than modulo the ideal. This makes sense in the context of Singular where an ideal is identified with its generators but it doesn't make sense in the context of Sage where this identification is not true. Thus, now allways the vector space dimension of ring modulo the ideal is returned.



---

archive/issue_comments_012625.json:
```json
{
    "body": "Changes look good, and sage -t is happy.",
    "created_at": "2008-01-31T01:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1960#issuecomment-12625",
    "user": "https://github.com/aghitza"
}
```

Changes look good, and sage -t is happy.



---

archive/issue_comments_012626.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc4",
    "created_at": "2008-02-01T00:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1960#issuecomment-12626",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc4



---

archive/issue_comments_012627.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-01T00:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1960#issuecomment-12627",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012628.json:
```json
{
    "body": "Merged in Sage 2.10.1.rc4",
    "created_at": "2008-02-01T00:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1960#issuecomment-12628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.rc4



---

archive/issue_events_002115.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-02-01T00:39:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1960",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1960#event-2115"
}
```
