# Issue 2723: [with patch] coercion error in monomial_quotient

archive/issues_002723.json:
```json
{
    "body": "Assignee: malb\n\nThe monomial_quotient method can give invalid data:\n\n```\nsage: R.<x,y>=ZZ[]\nsage: R.monomial_quotient(2*x*y,y,coeff=True)\n2*x\nsage: R.monomial_quotient(2*x*y,3*y,coeff=True)\n2/3*x\nsage: R.monomial_quotient(2*x*y,3*y,coeff=True).parent()\nMultivariate Polynomial Ring in x, y over Integer Ring\n```\n\n2/3 is *not* an Integer!\n\nThe attached patch gives:\n\n```\nsage: R.<x,y>=ZZ[]\nsage: R.monomial_quotient(2*x*y,y,coeff=True)\n2*x\nsage: R.monomial_quotient(2*x*y,3*y,coeff=True)\n...\n<type 'exceptions.TypeError'>: no coercion of this rational to integer\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2723\n\n",
    "created_at": "2008-03-29T18:49:27Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch] coercion error in monomial_quotient",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2723",
    "user": "jbmohler"
}
```
Assignee: malb

The monomial_quotient method can give invalid data:

```
sage: R.<x,y>=ZZ[]
sage: R.monomial_quotient(2*x*y,y,coeff=True)
2*x
sage: R.monomial_quotient(2*x*y,3*y,coeff=True)
2/3*x
sage: R.monomial_quotient(2*x*y,3*y,coeff=True).parent()
Multivariate Polynomial Ring in x, y over Integer Ring
```

2/3 is *not* an Integer!

The attached patch gives:

```
sage: R.<x,y>=ZZ[]
sage: R.monomial_quotient(2*x*y,y,coeff=True)
2*x
sage: R.monomial_quotient(2*x*y,3*y,coeff=True)
...
<type 'exceptions.TypeError'>: no coercion of this rational to integer
```



Issue created by migration from https://trac.sagemath.org/ticket/2723





---

archive/issue_comments_018767.json:
```json
{
    "body": "Attachment [mpoly-div-quotient.patch](tarball://root/attachments/some-uuid/ticket2723/mpoly-div-quotient.patch) by jbmohler created at 2008-03-29 18:52:36",
    "created_at": "2008-03-29T18:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2723#issuecomment-18767",
    "user": "jbmohler"
}
```

Attachment [mpoly-div-quotient.patch](tarball://root/attachments/some-uuid/ticket2723/mpoly-div-quotient.patch) by jbmohler created at 2008-03-29 18:52:36



---

archive/issue_comments_018768.json:
```json
{
    "body": "patch looks good.",
    "created_at": "2008-03-29T19:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2723#issuecomment-18768",
    "user": "malb"
}
```

patch looks good.



---

archive/issue_comments_018769.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T19:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2723#issuecomment-18769",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018770.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T19:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2723#issuecomment-18770",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0
