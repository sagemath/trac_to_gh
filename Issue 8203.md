# Issue 8203: misc doc fixes

archive/issues_008203.json:
```json
{
    "body": "Assignee: mvngu\n\nThe attached patch fixes several warnings when building the documentation.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8203\n\n",
    "created_at": "2010-02-07T03:48:02Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "misc doc fixes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8203",
    "user": "@jhpalmieri"
}
```
Assignee: mvngu

The attached patch fixes several warnings when building the documentation.


Issue created by migration from https://trac.sagemath.org/ticket/8203





---

archive/issue_comments_072352.json:
```json
{
    "body": "The attachment [trac_8203-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8203/trac_8203-doc.patch) conflicts with the patch at #8190: \n\n```\n[mvngu@sage sage-main]$ pwd\n/dev/shm/mvngu/sage-4.3.2-sage.math/devel/sage-main\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8190/trac_8190-docbuild.patch && hg qpush\nadding trac_8190-docbuild.patch to series file\napplying trac_8190-docbuild.patch\nnow at: trac_8190-docbuild.patch\n[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8203/trac_8203-doc.patch && hg qpush\nadding trac_8203-doc.patch to series file\napplying trac_8203-doc.patch\npatching file sage/gsl/ode.pyx\nHunk #1 FAILED at 205\n1 out of 3 hunks FAILED -- saving rejects to file sage/gsl/ode.pyx.rej\npatching file sage/rings/polynomial/multi_polynomial_ideal.py\nHunk #1 FAILED at 644\n1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej\npatching file sage/rings/quotient_ring.py\nHunk #1 FAILED at 527\n1 out of 1 hunks FAILED -- saving rejects to file sage/rings/quotient_ring.py.rej\npatching file sage/schemes/elliptic_curves/ell_generic.py\nHunk #1 FAILED at 2155\n1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_generic.py.rej\npatching file sage/symbolic/expression.pyx\nHunk #1 succeeded at 4978 with fuzz 2 (offset -957 lines).\npatching file sage/symbolic/relation.py\nHunk #1 FAILED at 860\nHunk #2 FAILED at 925\nHunk #3 FAILED at 985\nHunk #4 FAILED at 1014\n4 out of 4 hunks FAILED -- saving rejects to file sage/symbolic/relation.py.rej\npatch failed, unable to continue (try -v)\npatch failed, rejects left in working dir\nerrors during apply, please fix and refresh trac_8203-doc.patch\n```\n\nDo you want to rebase [trac_8203-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8203/trac_8203-doc.patch) on top of #8190?",
    "created_at": "2010-02-07T04:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8203#issuecomment-72352",
    "user": "mvngu"
}
```

The attachment [trac_8203-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8203/trac_8203-doc.patch) conflicts with the patch at #8190: 

```
[mvngu@sage sage-main]$ pwd
/dev/shm/mvngu/sage-4.3.2-sage.math/devel/sage-main
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8190/trac_8190-docbuild.patch && hg qpush
adding trac_8190-docbuild.patch to series file
applying trac_8190-docbuild.patch
now at: trac_8190-docbuild.patch
[mvngu@sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8203/trac_8203-doc.patch && hg qpush
adding trac_8203-doc.patch to series file
applying trac_8203-doc.patch
patching file sage/gsl/ode.pyx
Hunk #1 FAILED at 205
1 out of 3 hunks FAILED -- saving rejects to file sage/gsl/ode.pyx.rej
patching file sage/rings/polynomial/multi_polynomial_ideal.py
Hunk #1 FAILED at 644
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej
patching file sage/rings/quotient_ring.py
Hunk #1 FAILED at 527
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/quotient_ring.py.rej
patching file sage/schemes/elliptic_curves/ell_generic.py
Hunk #1 FAILED at 2155
1 out of 1 hunks FAILED -- saving rejects to file sage/schemes/elliptic_curves/ell_generic.py.rej
patching file sage/symbolic/expression.pyx
Hunk #1 succeeded at 4978 with fuzz 2 (offset -957 lines).
patching file sage/symbolic/relation.py
Hunk #1 FAILED at 860
Hunk #2 FAILED at 925
Hunk #3 FAILED at 985
Hunk #4 FAILED at 1014
4 out of 4 hunks FAILED -- saving rejects to file sage/symbolic/relation.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_8203-doc.patch
```

Do you want to rebase [trac_8203-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8203/trac_8203-doc.patch) on top of #8190?



---

archive/issue_comments_072353.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-02-07T04:06:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8203#issuecomment-72353",
    "user": "mvngu"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_072354.json:
```json
{
    "body": "Replying to [comment:1 mvngu]:\n> Do you want to rebase [trac_8203-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8203/trac_8203-doc.patch) on top of #8190?\n\nDo I *want* to?  Not really.  But here's a new version of the patch.\n\nBy the way, can I add \"delete `SAGE_ROOT/devel/sage/doc/en/reference/sage/misc/attach.rst`\" to this ticket, since this didn't get done as part of #8022?",
    "created_at": "2010-02-07T05:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8203#issuecomment-72354",
    "user": "@jhpalmieri"
}
```

Replying to [comment:1 mvngu]:
> Do you want to rebase [trac_8203-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8203/trac_8203-doc.patch) on top of #8190?

Do I *want* to?  Not really.  But here's a new version of the patch.

By the way, can I add "delete `SAGE_ROOT/devel/sage/doc/en/reference/sage/misc/attach.rst`" to this ticket, since this didn't get done as part of #8022?



---

archive/issue_comments_072355.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-07T05:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8203#issuecomment-72355",
    "user": "@jhpalmieri"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_072356.json:
```json
{
    "body": "Attachment [trac_8203-doc.patch](tarball://root/attachments/some-uuid/ticket8203/trac_8203-doc.patch) by @jhpalmieri created at 2010-02-07 05:37:52",
    "created_at": "2010-02-07T05:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8203#issuecomment-72356",
    "user": "@jhpalmieri"
}
```

Attachment [trac_8203-doc.patch](tarball://root/attachments/some-uuid/ticket8203/trac_8203-doc.patch) by @jhpalmieri created at 2010-02-07 05:37:52



---

archive/issue_comments_072357.json:
```json
{
    "body": "Looks good to me, seems pretty simple and docs build OK.  Positive review.",
    "created_at": "2010-02-07T23:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8203#issuecomment-72357",
    "user": "mhampton"
}
```

Looks good to me, seems pretty simple and docs build OK.  Positive review.



---

archive/issue_comments_072358.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-07T23:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8203#issuecomment-72358",
    "user": "mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072359.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8203",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8203#issuecomment-72359",
    "user": "@qed777"
}
```

Resolution: fixed
