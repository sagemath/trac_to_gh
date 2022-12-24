# Issue 6803: Implement symbolic Kronecker delta and also make current signum (sgn) symbolic

archive/issues_006803.json:
```json
{
    "body": "We should have a symbolic Kronecker delta in Sage.\n\nAlso, current implementation of signum (sgn) function \nreturns wrong answer for symbolic input.\n\n```\nsage: sgn(x)\n1\nsage: sgn(-x)\n1\n```\n\n\nSo we should make sgn() symbolic aware. Given, implementation of \nthese functions in new symbolics should be very similar to the existing generalized function **Dirac delta** and **Heaviside**, I am putting them together here. \n\nAlso, ticket #777 should be closed down as Sign is already in Sage\nand this ticket will further enhance it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6803\n\n",
    "created_at": "2009-08-22T11:34:45Z",
    "labels": [
        "symbolics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Implement symbolic Kronecker delta and also make current signum (sgn) symbolic",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6803",
    "user": "@golam-m-hossain"
}
```
We should have a symbolic Kronecker delta in Sage.

Also, current implementation of signum (sgn) function 
returns wrong answer for symbolic input.

```
sage: sgn(x)
1
sage: sgn(-x)
1
```


So we should make sgn() symbolic aware. Given, implementation of 
these functions in new symbolics should be very similar to the existing generalized function **Dirac delta** and **Heaviside**, I am putting them together here. 

Also, ticket #777 should be closed down as Sign is already in Sage
and this ticket will further enhance it.

Issue created by migration from https://trac.sagemath.org/ticket/6803





---

archive/issue_comments_056013.json:
```json
{
    "body": "Attachment [trac_6803-symbolic-kronecker-n-signum.patch](tarball://root/attachments/some-uuid/ticket6803/trac_6803-symbolic-kronecker-n-signum.patch) by @golam-m-hossain created at 2009-08-23 11:27:49",
    "created_at": "2009-08-23T11:27:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56013",
    "user": "@golam-m-hossain"
}
```

Attachment [trac_6803-symbolic-kronecker-n-signum.patch](tarball://root/attachments/some-uuid/ticket6803/trac_6803-symbolic-kronecker-n-signum.patch) by @golam-m-hossain created at 2009-08-23 11:27:49



---

archive/issue_comments_056014.json:
```json
{
    "body": "Overall this is good, and should get positive review.  However, there is a doctest failure (very typical when one adds a new symbolic function in line 204 of symbolic/random_tests.py, with random_expr().  This should be easy to fix.",
    "created_at": "2009-09-23T02:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56014",
    "user": "@kcrisman"
}
```

Overall this is good, and should get positive review.  However, there is a doctest failure (very typical when one adds a new symbolic function in line 204 of symbolic/random_tests.py, with random_expr().  This should be easy to fix.



---

archive/issue_comments_056015.json:
```json
{
    "body": "I have attached the patch, but with the random test fixed as a reviewer patch.  Apply only this patch.",
    "created_at": "2009-11-10T15:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56015",
    "user": "@kcrisman"
}
```

I have attached the patch, but with the random test fixed as a reviewer patch.  Apply only this patch.



---

archive/issue_comments_056016.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-10T15:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56016",
    "user": "@kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_056017.json:
```json
{
    "body": "Based on 4.2.1.alpha0, apply only this patch.",
    "created_at": "2009-11-10T15:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56017",
    "user": "@kcrisman"
}
```

Based on 4.2.1.alpha0, apply only this patch.



---

archive/issue_comments_056018.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-10T15:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56018",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056019.json:
```json
{
    "body": "Attachment [trac_6803-symbolic-kronecker-n-signum-review.patch](tarball://root/attachments/some-uuid/ticket6803/trac_6803-symbolic-kronecker-n-signum-review.patch) by @kcrisman created at 2009-11-10 15:58:50",
    "created_at": "2009-11-10T15:58:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56019",
    "user": "@kcrisman"
}
```

Attachment [trac_6803-symbolic-kronecker-n-signum-review.patch](tarball://root/attachments/some-uuid/ticket6803/trac_6803-symbolic-kronecker-n-signum-review.patch) by @kcrisman created at 2009-11-10 15:58:50



---

archive/issue_comments_056020.json:
```json
{
    "body": "I had to add a small patch to the doctest for sage.quadratic_forms.extras.sgn to make sure that the doctest was actually doctesting that function.",
    "created_at": "2009-11-17T07:27:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56020",
    "user": "@mwhansen"
}
```

I had to add a small patch to the doctest for sage.quadratic_forms.extras.sgn to make sure that the doctest was actually doctesting that function.



---

archive/issue_comments_056021.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T07:27:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56021",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_056022.json:
```json
{
    "body": "Replying to [comment:5 mhansen]:\n> I had to add a small patch to the doctest for sage.quadratic_forms.extras.sgn to make sure that the doctest was actually doctesting that function.\n\nCan you post that here, or at least the code in braces - just for posterity?",
    "created_at": "2009-11-17T14:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56022",
    "user": "@kcrisman"
}
```

Replying to [comment:5 mhansen]:
> I had to add a small patch to the doctest for sage.quadratic_forms.extras.sgn to make sure that the doctest was actually doctesting that function.

Can you post that here, or at least the code in braces - just for posterity?



---

archive/issue_comments_056023.json:
```json
{
    "body": "apply after previous",
    "created_at": "2009-12-09T03:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56023",
    "user": "mvngu"
}
```

apply after previous



---

archive/issue_comments_056024.json:
```json
{
    "body": "Attachment [trac_6803-sgn.patch](tarball://root/attachments/some-uuid/ticket6803/trac_6803-sgn.patch) by mvngu created at 2009-12-09 03:35:36\n\nReplying to [comment:6 kcrisman]:\n> Can you post that here, or at least the code in braces - just for posterity?  \n\nmhansen's patch is contained in `trac_6803-sgn.patch`",
    "created_at": "2009-12-09T03:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6803#issuecomment-56024",
    "user": "mvngu"
}
```

Attachment [trac_6803-sgn.patch](tarball://root/attachments/some-uuid/ticket6803/trac_6803-sgn.patch) by mvngu created at 2009-12-09 03:35:36

Replying to [comment:6 kcrisman]:
> Can you post that here, or at least the code in braces - just for posterity?  

mhansen's patch is contained in `trac_6803-sgn.patch`
