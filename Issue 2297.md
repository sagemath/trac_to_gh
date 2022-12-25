# Issue 2297: Tensor product of matrices [with patch, needs review]

archive/issues_002297.json:
```json
{
    "body": "Assignee: @simon-king-jena\n\nKeywords: tensor product\n\nI was missing a tensor product for matrices in Sage. While this is easy to obtain using `block_matrix`, it might be nicer to customize this as a method of `Matrix`. Example:\n\n\n```\nsage: M1=Matrix(QQ,[[-1,0],[-1/2,-1]])\nsage: M2=Matrix(ZZ,[[1,-1,2],[-2,4,8]])\nsage: M1.tensor_product(M2)\n\n[  -1    1   -2|   0    0    0]\n[   2   -4   -8|   0    0    0]\n[--------------+--------------]\n[-1/2  1/2   -1|  -1    1   -2]\n[   1   -2   -4|   2   -4   -8]\nsage: M2.tensor_product(M1)\n\n[  -1    0|   1    0|  -2    0]\n[-1/2   -1| 1/2    1|  -1   -2]\n[---------+---------+---------]\n[   2    0|  -4    0|  -8    0]\n[   1    2|  -2   -4|  -4   -8]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2297\n\n",
    "created_at": "2008-02-24T20:48:15Z",
    "labels": [
        "component: algebraic geometry",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Tensor product of matrices [with patch, needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2297",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @simon-king-jena

Keywords: tensor product

I was missing a tensor product for matrices in Sage. While this is easy to obtain using `block_matrix`, it might be nicer to customize this as a method of `Matrix`. Example:


```
sage: M1=Matrix(QQ,[[-1,0],[-1/2,-1]])
sage: M2=Matrix(ZZ,[[1,-1,2],[-2,4,8]])
sage: M1.tensor_product(M2)

[  -1    1   -2|   0    0    0]
[   2   -4   -8|   0    0    0]
[--------------+--------------]
[-1/2  1/2   -1|  -1    1   -2]
[   1   -2   -4|   2   -4   -8]
sage: M2.tensor_product(M1)

[  -1    0|   1    0|  -2    0]
[-1/2   -1| 1/2    1|  -1   -2]
[---------+---------+---------]
[   2    0|  -4    0|  -8    0]
[   1    2|  -2   -4|  -4   -8]
```



Issue created by migration from https://trac.sagemath.org/ticket/2297





---

archive/issue_comments_015197.json:
```json
{
    "body": "Attachment [tensorproduct.patch](tarball://root/attachments/some-uuid/ticket2297/tensorproduct.patch) by @simon-king-jena created at 2008-02-24 21:11:46",
    "created_at": "2008-02-24T21:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2297#issuecomment-15197",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [tensorproduct.patch](tarball://root/attachments/some-uuid/ticket2297/tensorproduct.patch) by @simon-king-jena created at 2008-02-24 21:11:46



---

archive/issue_comments_015198.json:
```json
{
    "body": "Changing component from algebraic geometry to linear algebra.",
    "created_at": "2008-02-24T21:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2297#issuecomment-15198",
    "user": "https://github.com/simon-king-jena"
}
```

Changing component from algebraic geometry to linear algebra.



---

archive/issue_comments_015199.json:
```json
{
    "body": "Hmm... I personally think that this should be called kronecker_product.",
    "created_at": "2008-02-24T21:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2297#issuecomment-15199",
    "user": "https://github.com/mwhansen"
}
```

Hmm... I personally think that this should be called kronecker_product.



---

archive/issue_comments_015200.json:
```json
{
    "body": "Replying to [comment:2 mhansen]:\n> Hmm... I personally think that this should be called kronecker_product.\n\nI wouldn't mind to call it like that. However, note that the corresponding function for Singular matrices is called tensor:\n\n```\nsage: R=singular.ring(0,'(x,y)','dp')\nsage: C=singular.matrix(2,2,'1,-1,0, 2')\nsage: D=singular.matrix(3,3,'0,0,-x, 0,y,0, x*y,0,0')\nsage: C.tensor(D)\n\n0,  0,-x,0,    0,  x,\n0,  y,0, 0,    -y, 0,\nx*y,0,0, -x*y, 0,  0,\n0,  0,0, 0,    0,  -2*x,\n0,  0,0, 0,    2*y,0,\n0,  0,0, 2*x*y,0,  0\n```\n\nThe implementation of the Kronecker product is part of a plot to define tensor products for free modules over polynomial rings (this is what i needed, originally).",
    "created_at": "2008-02-25T08:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2297#issuecomment-15200",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:2 mhansen]:
> Hmm... I personally think that this should be called kronecker_product.

I wouldn't mind to call it like that. However, note that the corresponding function for Singular matrices is called tensor:

```
sage: R=singular.ring(0,'(x,y)','dp')
sage: C=singular.matrix(2,2,'1,-1,0, 2')
sage: D=singular.matrix(3,3,'0,0,-x, 0,y,0, x*y,0,0')
sage: C.tensor(D)

0,  0,-x,0,    0,  x,
0,  y,0, 0,    -y, 0,
x*y,0,0, -x*y, 0,  0,
0,  0,0, 0,    0,  -2*x,
0,  0,0, 0,    2*y,0,
0,  0,0, 2*x*y,0,  0
```

The implementation of the Kronecker product is part of a plot to define tensor products for free modules over polynomial rings (this is what i needed, originally).



---

archive/issue_comments_015201.json:
```json
{
    "body": "I've played around with it and I think it looks good.  The name \"tensor product\" is just as common as \"Kronecker product\" for this.  (Actually, it's also a much better name than Kronecker product because it says where the operation is coming from).  If there is popular demand for this, we could have another method kronecker_product() that just calls this.\n\nAnyway, I say merge, and I'm eager to see the rest of the tensor product stuff.",
    "created_at": "2008-02-26T04:53:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2297#issuecomment-15201",
    "user": "https://github.com/aghitza"
}
```

I've played around with it and I think it looks good.  The name "tensor product" is just as common as "Kronecker product" for this.  (Actually, it's also a much better name than Kronecker product because it says where the operation is coming from).  If there is popular demand for this, we could have another method kronecker_product() that just calls this.

Anyway, I say merge, and I'm eager to see the rest of the tensor product stuff.



---

archive/issue_events_005419.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-26T05:07:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2297",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2297#event-5419"
}
```



---

archive/issue_comments_015202.json:
```json
{
    "body": "Merged in Sage 2.10.3.alpha0",
    "created_at": "2008-02-26T05:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2297#issuecomment-15202",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.alpha0



---

archive/issue_comments_015203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-26T05:07:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2297",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2297#issuecomment-15203",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
