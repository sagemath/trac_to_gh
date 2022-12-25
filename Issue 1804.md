# Issue 1804: Factorization.__mul__ assumes that the primes in the factorization commute, which may not be a valid assumption

archive/issues_001804.json:
```json
{
    "body": "Assignee: somebody\n\nThis is LAME:\n\n\n```\nsage: R.<x,y> = FreeAlgebra(QQ, 2)\nsage: F = Factorization([(x,3), (y,2)]); F\nx^3 * y^2\nsage: F*F\nx^6 * y^4\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1804\n\n",
    "created_at": "2008-01-17T19:52:14Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Factorization.__mul__ assumes that the primes in the factorization commute, which may not be a valid assumption",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1804",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

This is LAME:


```
sage: R.<x,y> = FreeAlgebra(QQ, 2)
sage: F = Factorization([(x,3), (y,2)]); F
x^3 * y^2
sage: F*F
x^6 * y^4
```


Issue created by migration from https://trac.sagemath.org/ticket/1804





---

archive/issue_comments_011373.json:
```json
{
    "body": "Same comments apply to __invert__ in the file factorization.py.  \n\n```\nsage: R.<x,y> = FreeAlgebra(QQ, 2)\nsage: F = Factorization([(x,3), (y,2)]); F\nx^3 * y^2\nsage: F^(-1)\nx^-3 * y^-2\n\n```\n",
    "created_at": "2008-01-17T19:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1804#issuecomment-11373",
    "user": "https://github.com/williamstein"
}
```

Same comments apply to __invert__ in the file factorization.py.  

```
sage: R.<x,y> = FreeAlgebra(QQ, 2)
sage: F = Factorization([(x,3), (y,2)]); F
x^3 * y^2
sage: F^(-1)
x^-3 * y^-2

```




---

archive/issue_comments_011374.json:
```json
{
    "body": "Attachment [ncalexan-1804.patch](tarball://root/attachments/some-uuid/ticket1804/ncalexan-1804.patch) by @ncalexan created at 2008-01-20 00:35:07",
    "created_at": "2008-01-20T00:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1804#issuecomment-11374",
    "user": "https://github.com/ncalexan"
}
```

Attachment [ncalexan-1804.patch](tarball://root/attachments/some-uuid/ticket1804/ncalexan-1804.patch) by @ncalexan created at 2008-01-20 00:35:07



---

archive/issue_comments_011375.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-01-21T02:04:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1804#issuecomment-11375",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_011376.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T02:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1804#issuecomment-11376",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011377.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-21T02:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1804",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1804#issuecomment-11377",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha1
