# Issue 3272: [with patch, needs review] Bug in sparse polynomials over finite fields

archive/issues_003272.json:
```json
{
    "body": "Assignee: @craigcitro\n\nSomeone reported the following bug on `sage-support`:\n\n\n```\nsage: A.<T> = PolynomialRing(Integers(5),sparse=True)\nsage: f = T^2+1\nsage: B = A.quo(f)\nsage: C.<s> = PolynomialRing(B)\nUnivariate Quotient Polynomial Ring in Tbar over Ring of integers\nmodulo 5 with modulus T^2 + 1\nTraceback (most recent call last):\n...\nTypeError: gen must be of PARI type t_INT\n```\n\n\nThe problem was two-fold: `polynomial_element_generic.__init__` had two `elif` clauses in the wrong order (so that the code for pari `gen`s was never run), and further the code for pari `gen`s was wrong. This patch fixes both, and adds a doctest.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3272\n\n",
    "created_at": "2008-05-22T21:49:12Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "[with patch, needs review] Bug in sparse polynomials over finite fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3272",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

Someone reported the following bug on `sage-support`:


```
sage: A.<T> = PolynomialRing(Integers(5),sparse=True)
sage: f = T^2+1
sage: B = A.quo(f)
sage: C.<s> = PolynomialRing(B)
Univariate Quotient Polynomial Ring in Tbar over Ring of integers
modulo 5 with modulus T^2 + 1
Traceback (most recent call last):
...
TypeError: gen must be of PARI type t_INT
```


The problem was two-fold: `polynomial_element_generic.__init__` had two `elif` clauses in the wrong order (so that the code for pari `gen`s was never run), and further the code for pari `gen`s was wrong. This patch fixes both, and adds a doctest.



Issue created by migration from https://trac.sagemath.org/ticket/3272





---

archive/issue_comments_022595.json:
```json
{
    "body": "Attachment [trac-3272.patch](tarball://root/attachments/some-uuid/ticket3272/trac-3272.patch) by @mwhansen created at 2008-05-23 06:55:27\n\nLooks good to me.",
    "created_at": "2008-05-23T06:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3272#issuecomment-22595",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac-3272.patch](tarball://root/attachments/some-uuid/ticket3272/trac-3272.patch) by @mwhansen created at 2008-05-23 06:55:27

Looks good to me.



---

archive/issue_comments_022596.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-23T07:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3272#issuecomment-22596",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_022597.json:
```json
{
    "body": "Merged in Sage 3.0.2.rc0",
    "created_at": "2008-05-23T07:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3272",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3272#issuecomment-22597",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.2.rc0
