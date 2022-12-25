# Issue 3428: [with patch, needs review] univariate polynomial quo_rem 0 trouble

archive/issues_003428.json:
```json
{
    "body": "Assignee: somebody\n\nAttached patch fixes this:\n\n\n```\nsage: R.<x> = ZZ[]\nsage: 0//(2*x)\n---------------------------------------------------------------------------\nArithmeticError                           Traceback (most recent call last)\n\n...\n/home/burcin/work/sage/sage-3.0.2/polynomial_integer_dense_ntl.pyx in sage.rings.polynomial.polynomial_integer_dense_ntl.Polynomial_integer_dense_ntl.quo_rem (sage/rings/polynomial/polynomial_integer_dense_ntl.cpp:4638)()\n\nArithmeticError: division not exact in Z[x] (consider coercing to Q[x] first) \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3428\n\n",
    "created_at": "2008-06-15T19:34:54Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "[with patch, needs review] univariate polynomial quo_rem 0 trouble",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3428",
    "user": "https://github.com/burcin"
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

archive/issue_comments_024103.json:
```json
{
    "body": "univariate poly quo_rem zero handling fix",
    "created_at": "2008-06-15T19:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24103",
    "user": "https://github.com/burcin"
}
```

univariate poly quo_rem zero handling fix



---

archive/issue_comments_024104.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_craigcitro\".",
    "created_at": "2008-06-15T21:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24104",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_craigcitro".



---

archive/issue_comments_024105.json:
```json
{
    "body": "Attachment [univariate_poly_quo_rem_zero.patch](tarball://root/attachments/some-uuid/ticket3428/univariate_poly_quo_rem_zero.patch) by @craigcitro created at 2008-06-15 21:55:42",
    "created_at": "2008-06-15T21:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24105",
    "user": "https://github.com/craigcitro"
}
```

Attachment [univariate_poly_quo_rem_zero.patch](tarball://root/attachments/some-uuid/ticket3428/univariate_poly_quo_rem_zero.patch) by @craigcitro created at 2008-06-15 21:55:42



---

archive/issue_events_003643.json:
```json
{
    "actor": "@burcin",
    "created_at": "2008-06-17T19:41:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3428#event-3643"
}
```



---

archive/issue_comments_024106.json:
```json
{
    "body": "This won't be necessary when #2357 is merged. I suggest we resolve this with `wontfix`.",
    "created_at": "2008-06-17T19:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24106",
    "user": "https://github.com/burcin"
}
```

This won't be necessary when #2357 is merged. I suggest we resolve this with `wontfix`.



---

archive/issue_comments_024107.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-17T19:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24107",
    "user": "https://github.com/burcin"
}
```

Resolution: fixed



---

archive/issue_comments_024108.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-06-17T22:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24108",
    "user": "https://github.com/craigcitro"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_024109.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-06-17T22:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24109",
    "user": "https://github.com/craigcitro"
}
```

Changing status from closed to reopened.



---

archive/issue_events_003644.json:
```json
{
    "actor": "@craigcitro",
    "created_at": "2008-06-17T22:37:04Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3428#event-3644"
}
```



---

archive/issue_comments_024110.json:
```json
{
    "body": "However, we're not going to kill the NTL interface, so this should still be fixed.",
    "created_at": "2008-06-17T22:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24110",
    "user": "https://github.com/craigcitro"
}
```

However, we're not going to kill the NTL interface, so this should still be fixed.



---

archive/issue_comments_024111.json:
```json
{
    "body": "Looks good. I added one additional doctest to make sure that the exact failure reported is now doctested. \n\nReview by craigcitro and ncalexan.",
    "created_at": "2008-06-19T20:20:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24111",
    "user": "https://github.com/craigcitro"
}
```

Looks good. I added one additional doctest to make sure that the exact failure reported is now doctested. 

Review by craigcitro and ncalexan.



---

archive/issue_comments_024112.json:
```json
{
    "body": "apply after Burcin's patch",
    "created_at": "2008-06-19T20:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24112",
    "user": "https://github.com/craigcitro"
}
```

apply after Burcin's patch



---

archive/issue_events_003645.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-06-23T10:00:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3428#event-3645"
}
```



---

archive/issue_comments_024113.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-23T10:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24113",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024114.json:
```json
{
    "body": "Attachment [trac-3428-doctest.patch](tarball://root/attachments/some-uuid/ticket3428/trac-3428-doctest.patch) by mabshoff created at 2008-06-23 10:00:53\n\nMerged in Sage 3.0.4.alpha0",
    "created_at": "2008-06-23T10:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3428#issuecomment-24114",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-3428-doctest.patch](tarball://root/attachments/some-uuid/ticket3428/trac-3428-doctest.patch) by mabshoff created at 2008-06-23 10:00:53

Merged in Sage 3.0.4.alpha0
