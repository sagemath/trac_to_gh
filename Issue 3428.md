# Issue 3428: [with patch, needs review] univariate polynomial quo_rem 0 trouble

archive/issues_003428.json:
```json
{
    "body": "Assignee: somebody\n\nAttached patch fixes this:\n\n\n```\nsage: R.<x> = ZZ[]\nsage: 0//(2*x)\n---------------------------------------------------------------------------\nArithmeticError                           Traceback (most recent call last)\n\n...\n/home/burcin/work/sage/sage-3.0.2/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.quo_rem (sage/rings/polynomial/polynomial_integer_dense_ntl.cpp:4638)()\n\nArithmeticError: division not exact in Z[x] (consider coercing to Q[x] first) \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3428\n\n",
    "created_at": "2008-06-15T19:34:54Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] univariate polynomial quo_rem 0 trouble",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3428",
    "user": "burcin"
}
```
Assignee: somebody

Attached patch fixes this:


```
sage: R.<x> = ZZ[]
sage: 0//(2*x)
---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)

...
/home/burcin/work/sage/sage-3.0.2/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.quo_rem (sage/rings/polynomial/polynomial_integer_dense_ntl.cpp:4638)()

ArithmeticError: division not exact in Z[x] (consider coercing to Q[x] first) 
```


Issue created by migration from https://trac.sagemath.org/ticket/3428





---

archive/issue_comments_024152.json:
```json
{
    "body": "univariate poly quo_rem zero handling fix",
    "created_at": "2008-06-15T19:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24152",
    "user": "burcin"
}
```

univariate poly quo_rem zero handling fix



---

archive/issue_comments_024153.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-15T21:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24153",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_024154.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-06-15T21:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24154",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_024155.json:
```json
{
    "body": "This won't be necessary when #2357 is merged. I suggest we resolve this with `wontfix`.",
    "created_at": "2008-06-17T19:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24155",
    "user": "burcin"
}
```

This won't be necessary when #2357 is merged. I suggest we resolve this with `wontfix`.



---

archive/issue_comments_024156.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-17T19:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24156",
    "user": "burcin"
}
```

Resolution: fixed



---

archive/issue_comments_024157.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-06-17T22:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24157",
    "user": "craigcitro"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_024158.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-06-17T22:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24158",
    "user": "craigcitro"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_024159.json:
```json
{
    "body": "However, we're not going to kill the NTL interface, so this should still be fixed.",
    "created_at": "2008-06-17T22:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24159",
    "user": "craigcitro"
}
```

However, we're not going to kill the NTL interface, so this should still be fixed.



---

archive/issue_comments_024160.json:
```json
{
    "body": "Looks good. I added one additional doctest to make sure that the exact failure reported is now doctested. \n\nReview by craigcitro and ncalexan.",
    "created_at": "2008-06-19T20:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24160",
    "user": "craigcitro"
}
```

Looks good. I added one additional doctest to make sure that the exact failure reported is now doctested. 

Review by craigcitro and ncalexan.



---

archive/issue_comments_024161.json:
```json
{
    "body": "apply after Burcin's patch",
    "created_at": "2008-06-19T20:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24161",
    "user": "craigcitro"
}
```

apply after Burcin's patch



---

archive/issue_comments_024162.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T10:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24162",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024163.json:
```json
{
    "body": "Attachment\n\nMerged in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T10:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24163",
    "user": "mabshoff"
}
```

Attachment

Merged in Sage 3.0.4.alpha0
