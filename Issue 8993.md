# Issue 8993: Representation of polynomial quotient rings in Singular

archive/issues_008993.json:
```json
{
    "body": "Assignee: was\n\nKeywords: polynomial quotient ring, singular\n\nCurrently there is no representation of univariate polynomial quotient rings in the Singular interface; it was only implemented for the multivariate case.\n\nThe attached patch implements it:\n\n```\nsage: P.<x> = QQ[]\nsage: Q.<xi> = P.quo([(x^2+1)])\nsage: singular(xi)\nxi\nsage: singular(Q)\n//   characteristic : 0\n//   number of vars : 1\n//        block   1 : ordering lp\n//                  : names    xi\n//        block   2 : ordering C\n// quotient ring from ideal\n_[1]=xi^2+1\nsage: (singular(xi)*singular(xi)).NF('std(0)')\n-1\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8993\n\n",
    "created_at": "2010-05-19T16:48:31Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Representation of polynomial quotient rings in Singular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8993",
    "user": "SimonKing"
}
```
Assignee: was

Keywords: polynomial quotient ring, singular

Currently there is no representation of univariate polynomial quotient rings in the Singular interface; it was only implemented for the multivariate case.

The attached patch implements it:

```
sage: P.<x> = QQ[]
sage: Q.<xi> = P.quo([(x^2+1)])
sage: singular(xi)
xi
sage: singular(Q)
//   characteristic : 0
//   number of vars : 1
//        block   1 : ordering lp
//                  : names    xi
//        block   2 : ordering C
// quotient ring from ideal
_[1]=xi^2+1
sage: (singular(xi)*singular(xi)).NF('std(0)')
-1
```



Issue created by migration from https://trac.sagemath.org/ticket/8993





---

archive/issue_comments_083158.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-19T16:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83158",
    "user": "SimonKing"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083159.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-25T01:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83159",
    "user": "robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083160.json:
```json
{
    "body": "Mostly looks good, the only issue is that you should never \"import sage\" (or sage.all) from within the sage library.",
    "created_at": "2010-05-25T01:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83160",
    "user": "robertwb"
}
```

Mostly looks good, the only issue is that you should never "import sage" (or sage.all) from within the sage library.



---

archive/issue_comments_083161.json:
```json
{
    "body": "Replying to [comment:2 robertwb]:\n> Mostly looks good, the only issue is that you should never \"import sage\" (or sage.all) from within the sage library. \n\nDo I understand correctly:\n\nIt is OK that I do `from sage.all import singular` inside one method, but I should not do `import sage` on top of the file?\n\nI'll submit a correction soon.\n\nCheers,\n\nSimon",
    "created_at": "2010-05-25T07:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83161",
    "user": "SimonKing"
}
```

Replying to [comment:2 robertwb]:
> Mostly looks good, the only issue is that you should never "import sage" (or sage.all) from within the sage library. 

Do I understand correctly:

It is OK that I do `from sage.all import singular` inside one method, but I should not do `import sage` on top of the file?

I'll submit a correction soon.

Cheers,

Simon



---

archive/issue_comments_083162.json:
```json
{
    "body": "Yes.",
    "created_at": "2010-05-25T07:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83162",
    "user": "robertwb"
}
```

Yes.



---

archive/issue_comments_083163.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-25T08:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83163",
    "user": "SimonKing"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083164.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n> ...\n> It is OK that I do `from sage.all import singular` inside one method, but I should not do `import sage` on top of the file?\n> \n> I'll submit a correction soon.\n\nDone!",
    "created_at": "2010-05-25T08:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83164",
    "user": "SimonKing"
}
```

Replying to [comment:3 SimonKing]:
> ...
> It is OK that I do `from sage.all import singular` inside one method, but I should not do `import sage` on top of the file?
> 
> I'll submit a correction soon.

Done!



---

archive/issue_comments_083165.json:
```json
{
    "body": "Patch looks okay, doctests pass.",
    "created_at": "2010-07-21T15:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83165",
    "user": "malb"
}
```

Patch looks okay, doctests pass.



---

archive/issue_comments_083166.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T15:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83166",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083167.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-22T02:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83167",
    "user": "ddrake"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083168.json:
```json
{
    "body": "Please include the ticket number in the commit messages for your patches!",
    "created_at": "2010-07-22T02:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83168",
    "user": "ddrake"
}
```

Please include the ticket number in the commit messages for your patches!



---

archive/issue_comments_083169.json:
```json
{
    "body": "Attachment [8993_poly_quotient_in_singular.patch](tarball://root/attachments/some-uuid/ticket8993/8993_poly_quotient_in_singular.patch) by SimonKing created at 2010-07-22 08:11:25\n\nImplement polynomial quotient rings in singular interface",
    "created_at": "2010-07-22T08:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83169",
    "user": "SimonKing"
}
```

Attachment [8993_poly_quotient_in_singular.patch](tarball://root/attachments/some-uuid/ticket8993/8993_poly_quotient_in_singular.patch) by SimonKing created at 2010-07-22 08:11:25

Implement polynomial quotient rings in singular interface



---

archive/issue_comments_083170.json:
```json
{
    "body": "Attachment [8993_poly_quotient_in_singular.p1.patch](tarball://root/attachments/some-uuid/ticket8993/8993_poly_quotient_in_singular.p1.patch) by SimonKing created at 2010-07-22 08:12:02\n\nAvoid \"import sage\" according to the reviewer's request - apply after first patch",
    "created_at": "2010-07-22T08:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83170",
    "user": "SimonKing"
}
```

Attachment [8993_poly_quotient_in_singular.p1.patch](tarball://root/attachments/some-uuid/ticket8993/8993_poly_quotient_in_singular.p1.patch) by SimonKing created at 2010-07-22 08:12:02

Avoid "import sage" according to the reviewer's request - apply after first patch



---

archive/issue_comments_083171.json:
```json
{
    "body": "Replying to [comment:7 ddrake]:\n> Please include the ticket number in the commit messages for your patches!\n\nI changed the commit message accordingly and updated the attachments. I hope this entitles me to switch back to \"positive review\".",
    "created_at": "2010-07-22T08:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83171",
    "user": "SimonKing"
}
```

Replying to [comment:7 ddrake]:
> Please include the ticket number in the commit messages for your patches!

I changed the commit message accordingly and updated the attachments. I hope this entitles me to switch back to "positive review".



---

archive/issue_comments_083172.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-22T08:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83172",
    "user": "SimonKing"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_083173.json:
```json
{
    "body": "Replying to [comment:8 SimonKing]:\n> I changed the commit message accordingly and updated the attachments. I hope this entitles me to switch back to \"positive review\".\n\nIt certainly does. Thanks for fixing this! It should get merged in 4.5.2.alpha1.",
    "created_at": "2010-07-22T09:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83173",
    "user": "ddrake"
}
```

Replying to [comment:8 SimonKing]:
> I changed the commit message accordingly and updated the attachments. I hope this entitles me to switch back to "positive review".

It certainly does. Thanks for fixing this! It should get merged in 4.5.2.alpha1.



---

archive/issue_comments_083174.json:
```json
{
    "body": "Merged both patches in 4.5.2.alpha1.",
    "created_at": "2010-07-22T23:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83174",
    "user": "ddrake"
}
```

Merged both patches in 4.5.2.alpha1.



---

archive/issue_comments_083175.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T23:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83175",
    "user": "ddrake"
}
```

Resolution: fixed
