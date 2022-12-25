# Issue 5680: Use new bits from FLINT 1.2.4 (followup to #5240)

archive/issues_005680.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin wbhart\n\nNow that FLINT 1.2.4 is in Sage we should hook up various new methods:\n\n* factor\n* square free factoring\n* derivative\n* powermod\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5680\n\n",
    "created_at": "2009-04-04T05:19:10Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Use new bits from FLINT 1.2.4 (followup to #5240)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5680",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @malb

CC:  @burcin wbhart

Now that FLINT 1.2.4 is in Sage we should hook up various new methods:

* factor
* square free factoring
* derivative
* powermod

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5680





---

archive/issue_comments_044335.json:
```json
{
    "body": "Bill suggested that I also CC Burcin on this ticket so he knows that it exists :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-04T22:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44335",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Bill suggested that I also CC Burcin on this ticket so he knows that it exists :)

Cheers,

Michael



---

archive/issue_comments_044336.json:
```json
{
    "body": "Changing component from misc to basic arithmetic.",
    "created_at": "2009-10-20T14:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44336",
    "user": "https://github.com/burcin"
}
```

Changing component from misc to basic arithmetic.



---

archive/issue_comments_044337.json:
```json
{
    "body": "I attached a patch that exposes some more functionality from FLINT and adds a function for rational reconstruction to zmod_poly wrappers. Changes include:\n\n* factor\n* is_irreducible\n* scalar multiplication\n* is_irreducible\n* monic\n* evaluate\n* short products\n* rational function reconstruction (not a FLINT function)",
    "created_at": "2009-10-20T14:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44337",
    "user": "https://github.com/burcin"
}
```

I attached a patch that exposes some more functionality from FLINT and adds a function for rational reconstruction to zmod_poly wrappers. Changes include:

* factor
* is_irreducible
* scalar multiplication
* is_irreducible
* monic
* evaluate
* short products
* rational function reconstruction (not a FLINT function)



---

archive/issue_comments_044338.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-20T14:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44338",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_044339.json:
```json
{
    "body": "Attachment [trac_5680-flint_zmod_poly_enhancements.patch](tarball://root/attachments/some-uuid/ticket5680/trac_5680-flint_zmod_poly_enhancements.patch) by @burcin created at 2009-10-20 14:44:26",
    "created_at": "2009-10-20T14:44:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44339",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_5680-flint_zmod_poly_enhancements.patch](tarball://root/attachments/some-uuid/ticket5680/trac_5680-flint_zmod_poly_enhancements.patch) by @burcin created at 2009-10-20 14:44:26



---

archive/issue_comments_044340.json:
```json
{
    "body": "With Sage 4.2.alpha1, I get the following failures:\n\n\n```\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padics.py # 18 doctests failed\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py # 15 doctests failed\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py # 5 doctests failed\n        sage -t -long devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py # 1 doctests failed\n        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_padic_field.py # 2 doctests failed\n```\n\n\nAlso, in squarefree_decomposition, there is an \"EXAMPLES:\" that needs to be \"EXAMPLES::\".",
    "created_at": "2009-10-21T07:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44340",
    "user": "https://github.com/mwhansen"
}
```

With Sage 4.2.alpha1, I get the following failures:


```
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/padics.py # 18 doctests failed
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py # 15 doctests failed
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/monsky_washnitzer.py # 5 doctests failed
        sage -t -long devel/sage-main/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py # 1 doctests failed
        sage -t -long devel/sage-main/sage/schemes/elliptic_curves/ell_padic_field.py # 2 doctests failed
```


Also, in squarefree_decomposition, there is an "EXAMPLES:" that needs to be "EXAMPLES::".



---

archive/issue_comments_044341.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-21T07:37:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44341",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_044342.json:
```json
{
    "body": "Attachment [trac_5680-flint_zmod_poly_enhancements.take2.patch](tarball://root/attachments/some-uuid/ticket5680/trac_5680-flint_zmod_poly_enhancements.take2.patch) by @burcin created at 2009-10-21 17:13:17\n\nOops, I hadn't run doctests on `schemes`, and it was a genuine bug with scalar multiplication.\n\nNew patch attachment:trac_5680-flint_zmod_poly_enhancements.take2.patch should fix all problems.",
    "created_at": "2009-10-21T17:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44342",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_5680-flint_zmod_poly_enhancements.take2.patch](tarball://root/attachments/some-uuid/ticket5680/trac_5680-flint_zmod_poly_enhancements.take2.patch) by @burcin created at 2009-10-21 17:13:17

Oops, I hadn't run doctests on `schemes`, and it was a genuine bug with scalar multiplication.

New patch attachment:trac_5680-flint_zmod_poly_enhancements.take2.patch should fix all problems.



---

archive/issue_comments_044343.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-21T17:13:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44343",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_044344.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-05T01:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44344",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_044345.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-05T01:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44345",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_005922.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-11-05T01:19:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5680#event-5922"
}
```



---

archive/issue_comments_044346.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-05T01:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5680#issuecomment-44346",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
