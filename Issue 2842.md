# Issue 2842: [with patch, needs review] PyLint unused variable cleanup for sage.rings.polynomial

archive/issues_002842.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: pylint\n\nThe attached patch\n* removes unused variables,\n* removes unused imports,\n* defines undefined variables,\n\nfrom several files in sage.rings.polynomial. It doesn't fix all issues in that module but this patch is still open for reviews.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2842\n\n",
    "created_at": "2008-04-07T13:10:29Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] PyLint unused variable cleanup for sage.rings.polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2842",
    "user": "@malb"
}
```
Assignee: cwitty

Keywords: pylint

The attached patch
* removes unused variables,
* removes unused imports,
* defines undefined variables,

from several files in sage.rings.polynomial. It doesn't fix all issues in that module but this patch is still open for reviews.

Issue created by migration from https://trac.sagemath.org/ticket/2842





---

archive/issue_comments_019501.json:
```json
{
    "body": "Attachment [pylint_polynomial_unused.patch](tarball://root/attachments/some-uuid/ticket2842/pylint_polynomial_unused.patch) by @malb created at 2008-04-07 13:10:39",
    "created_at": "2008-04-07T13:10:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2842#issuecomment-19501",
    "user": "@malb"
}
```

Attachment [pylint_polynomial_unused.patch](tarball://root/attachments/some-uuid/ticket2842/pylint_polynomial_unused.patch) by @malb created at 2008-04-07 13:10:39



---

archive/issue_comments_019502.json:
```json
{
    "body": "Attachment [2842.patch](tarball://root/attachments/some-uuid/ticket2842/2842.patch) by @mwhansen created at 2008-04-07 22:55:03\n\nLooks good to me.  Apply just 2842.patch after #2844 .",
    "created_at": "2008-04-07T22:55:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2842#issuecomment-19502",
    "user": "@mwhansen"
}
```

Attachment [2842.patch](tarball://root/attachments/some-uuid/ticket2842/2842.patch) by @mwhansen created at 2008-04-07 22:55:03

Looks good to me.  Apply just 2842.patch after #2844 .



---

archive/issue_comments_019503.json:
```json
{
    "body": "I am seeing one doctest failure on sage.math:\n\n```\nsage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha3/tmp/multi_polynomial_libsingular.py\", line 496:\n    sage: R.<x,y> = QQ[]; S.<xx,yy> = GF(5)[]; S(5*x*y + x + 17*y)\nExpected:\n    xx + 2*yy\nGot:\n    xx + 0*yy\n**********************************************************************\n```\n\nMartin will start poking around tomorrow.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-08T00:27:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2842#issuecomment-19503",
    "user": "mabshoff"
}
```

I am seeing one doctest failure on sage.math:

```
sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha3/tmp/multi_polynomial_libsingular.py", line 496:
    sage: R.<x,y> = QQ[]; S.<xx,yy> = GF(5)[]; S(5*x*y + x + 17*y)
Expected:
    xx + 2*yy
Got:
    xx + 0*yy
**********************************************************************
```

Martin will start poking around tomorrow.

Cheers,

Michael



---

archive/issue_comments_019504.json:
```json
{
    "body": "Note that post the #2844 merge you ought to apply 2842.patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-08T00:31:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2842#issuecomment-19504",
    "user": "mabshoff"
}
```

Note that post the #2844 merge you ought to apply 2842.patch.

Cheers,

Michael



---

archive/issue_comments_019505.json:
```json
{
    "body": "Oh well, just applying #2844 causes the above libSingular failures. So I am merging this patch since it works. I would recommend opening another ticket once somebody else can verify the same issue I see. A compile from scratch on sage.math ought to lead to the same result.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-08T01:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2842#issuecomment-19505",
    "user": "mabshoff"
}
```

Oh well, just applying #2844 causes the above libSingular failures. So I am merging this patch since it works. I would recommend opening another ticket once somebody else can verify the same issue I see. A compile from scratch on sage.math ought to lead to the same result.

Cheers,

Michael



---

archive/issue_comments_019506.json:
```json
{
    "body": "Merged 2842.patch in Sage 3.0.alpha3",
    "created_at": "2008-04-08T01:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2842#issuecomment-19506",
    "user": "mabshoff"
}
```

Merged 2842.patch in Sage 3.0.alpha3



---

archive/issue_comments_019507.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-08T01:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2842",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2842#issuecomment-19507",
    "user": "mabshoff"
}
```

Resolution: fixed
