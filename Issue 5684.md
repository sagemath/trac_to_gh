# Issue 5684: [with patch, needs review] Taking negative powers of Laurent polynomial throws exception

archive/issues_005684.json:
```json
{
    "body": "Assignee: tbd\n\nTaking negative powers of a Laurent polynomial doesn't currently work due to a typo in LaurentPolynomial_mpair.__pow__(). The attached patch fixes this.\n\n\n```\nsage: F.<t> = LaurentPolynomialRing(GF(3))\nsage: (1+t)^(-1)\nTypeError: fraction_field() takes no arguments (1 given)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5684\n\n",
    "created_at": "2009-04-04T20:40:48Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] Taking negative powers of Laurent polynomial throws exception",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5684",
    "user": "https://github.com/wjp"
}
```
Assignee: tbd

Taking negative powers of a Laurent polynomial doesn't currently work due to a typo in LaurentPolynomial_mpair.__pow__(). The attached patch fixes this.


```
sage: F.<t> = LaurentPolynomialRing(GF(3))
sage: (1+t)^(-1)
TypeError: fraction_field() takes no arguments (1 given)
```


Issue created by migration from https://trac.sagemath.org/ticket/5684





---

archive/issue_comments_044363.json:
```json
{
    "body": "Attachment [laurent_polynomial_negpow.patch](tarball://root/attachments/some-uuid/ticket5684/laurent_polynomial_negpow.patch) by @wjp created at 2009-04-04 20:41:12",
    "created_at": "2009-04-04T20:41:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5684#issuecomment-44363",
    "user": "https://github.com/wjp"
}
```

Attachment [laurent_polynomial_negpow.patch](tarball://root/attachments/some-uuid/ticket5684/laurent_polynomial_negpow.patch) by @wjp created at 2009-04-04 20:41:12



---

archive/issue_comments_044364.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-13T01:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5684#issuecomment-44364",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_comments_044365.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-13T01:49:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5684",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5684#issuecomment-44365",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
