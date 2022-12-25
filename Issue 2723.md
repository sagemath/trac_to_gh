# Issue 2723: [with patch] coercion error in monomial_quotient

archive/issues_002723.json:
```json
{
    "body": "Assignee: @malb\n\nThe monomial_quotient method can give invalid data:\n\n```\nsage: R.<x,y>=ZZ[]\nsage: R.monomial_quotient(2*x*y,y,coeff=True)\n2*x\nsage: R.monomial_quotient(2*x*y,3*y,coeff=True)\n2/3*x\nsage: R.monomial_quotient(2*x*y,3*y,coeff=True).parent()\nMultivariate Polynomial Ring in x, y over Integer Ring\n```\n\n2/3 is *not* an Integer!\n\nThe attached patch gives:\n\n```\nsage: R.<x,y>=ZZ[]\nsage: R.monomial_quotient(2*x*y,y,coeff=True)\n2*x\nsage: R.monomial_quotient(2*x*y,3*y,coeff=True)\n...\n<type 'exceptions.TypeError'>: no coercion of this rational to integer\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2723\n\n",
    "created_at": "2008-03-29T18:49:27Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch] coercion error in monomial_quotient",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2723",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: @malb

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

archive/issue_comments_018728.json:
```json
{
    "body": "Attachment [mpoly-div-quotient.patch](tarball://root/attachments/some-uuid/ticket2723/mpoly-div-quotient.patch) by jbmohler created at 2008-03-29 18:52:36",
    "created_at": "2008-03-29T18:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2723#issuecomment-18728",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [mpoly-div-quotient.patch](tarball://root/attachments/some-uuid/ticket2723/mpoly-div-quotient.patch) by jbmohler created at 2008-03-29 18:52:36



---

archive/issue_comments_018729.json:
```json
{
    "body": "patch looks good.",
    "created_at": "2008-03-29T19:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2723#issuecomment-18729",
    "user": "https://github.com/malb"
}
```

patch looks good.



---

archive/issue_events_002911.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-03-29T19:19:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2723",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2723#event-2911"
}
```



---

archive/issue_comments_018730.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T19:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2723#issuecomment-18730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018731.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T19:19:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2723",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2723#issuecomment-18731",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.rc0
