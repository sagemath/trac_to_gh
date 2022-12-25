# Issue 8993: Representation of polynomial quotient rings in Singular

archive/issues_008993.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: polynomial quotient ring, singular\n\nCurrently there is no representation of univariate polynomial quotient rings in the Singular interface; it was only implemented for the multivariate case.\n\nThe attached patch implements it:\n\n```\nsage: P.<x> = QQ[]\nsage: Q.<xi> = P.quo([(x^2+1)])\nsage: singular(xi)\nxi\nsage: singular(Q)\n//   characteristic : 0\n//   number of vars : 1\n//        block   1 : ordering lp\n//                  : names    xi\n//        block   2 : ordering C\n// quotient ring from ideal\n_[1]=xi^2+1\nsage: (singular(xi)*singular(xi)).NF('std(0)')\n-1\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8993\n\n",
    "created_at": "2010-05-19T16:48:31Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Representation of polynomial quotient rings in Singular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8993",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @williamstein

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

archive/issue_comments_083022.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-19T16:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83022",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083023.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-25T01:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83023",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083024.json:
```json
{
    "body": "Mostly looks good, the only issue is that you should never \"import sage\" (or sage.all) from within the sage library.",
    "created_at": "2010-05-25T01:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83024",
    "user": "https://github.com/robertwb"
}
```

Mostly looks good, the only issue is that you should never "import sage" (or sage.all) from within the sage library.



---

archive/issue_comments_083025.json:
```json
{
    "body": "Replying to [comment:2 robertwb]:\n> Mostly looks good, the only issue is that you should never \"import sage\" (or sage.all) from within the sage library. \n\nDo I understand correctly:\n\nIt is OK that I do `from sage.all import singular` inside one method, but I should not do `import sage` on top of the file?\n\nI'll submit a correction soon.\n\nCheers,\n\nSimon",
    "created_at": "2010-05-25T07:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83025",
    "user": "https://github.com/simon-king-jena"
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

archive/issue_comments_083026.json:
```json
{
    "body": "Yes.",
    "created_at": "2010-05-25T07:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83026",
    "user": "https://github.com/robertwb"
}
```

Yes.



---

archive/issue_comments_083027.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-25T08:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83027",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083028.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n> ...\n> It is OK that I do `from sage.all import singular` inside one method, but I should not do `import sage` on top of the file?\n> \n> I'll submit a correction soon.\n\nDone!",
    "created_at": "2010-05-25T08:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83028",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:3 SimonKing]:
> ...
> It is OK that I do `from sage.all import singular` inside one method, but I should not do `import sage` on top of the file?
> 
> I'll submit a correction soon.

Done!



---

archive/issue_comments_083029.json:
```json
{
    "body": "Patch looks okay, doctests pass.",
    "created_at": "2010-07-21T15:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83029",
    "user": "https://github.com/malb"
}
```

Patch looks okay, doctests pass.



---

archive/issue_comments_083030.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-21T15:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83030",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083031.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-22T02:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83031",
    "user": "https://github.com/dandrake"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_083032.json:
```json
{
    "body": "Please include the ticket number in the commit messages for your patches!",
    "created_at": "2010-07-22T02:25:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83032",
    "user": "https://github.com/dandrake"
}
```

Please include the ticket number in the commit messages for your patches!



---

archive/issue_comments_083033.json:
```json
{
    "body": "Attachment [8993_poly_quotient_in_singular.patch](tarball://root/attachments/some-uuid/ticket8993/8993_poly_quotient_in_singular.patch) by @simon-king-jena created at 2010-07-22 08:11:25\n\nImplement polynomial quotient rings in singular interface",
    "created_at": "2010-07-22T08:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83033",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [8993_poly_quotient_in_singular.patch](tarball://root/attachments/some-uuid/ticket8993/8993_poly_quotient_in_singular.patch) by @simon-king-jena created at 2010-07-22 08:11:25

Implement polynomial quotient rings in singular interface



---

archive/issue_comments_083034.json:
```json
{
    "body": "Attachment [8993_poly_quotient_in_singular.p1.patch](tarball://root/attachments/some-uuid/ticket8993/8993_poly_quotient_in_singular.p1.patch) by @simon-king-jena created at 2010-07-22 08:12:02\n\nAvoid \"import sage\" according to the reviewer's request - apply after first patch",
    "created_at": "2010-07-22T08:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83034",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [8993_poly_quotient_in_singular.p1.patch](tarball://root/attachments/some-uuid/ticket8993/8993_poly_quotient_in_singular.p1.patch) by @simon-king-jena created at 2010-07-22 08:12:02

Avoid "import sage" according to the reviewer's request - apply after first patch



---

archive/issue_comments_083035.json:
```json
{
    "body": "Replying to [comment:7 ddrake]:\n> Please include the ticket number in the commit messages for your patches!\n\nI changed the commit message accordingly and updated the attachments. I hope this entitles me to switch back to \"positive review\".",
    "created_at": "2010-07-22T08:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83035",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:7 ddrake]:
> Please include the ticket number in the commit messages for your patches!

I changed the commit message accordingly and updated the attachments. I hope this entitles me to switch back to "positive review".



---

archive/issue_comments_083036.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-07-22T08:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83036",
    "user": "https://github.com/simon-king-jena"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_083037.json:
```json
{
    "body": "Replying to [comment:8 SimonKing]:\n> I changed the commit message accordingly and updated the attachments. I hope this entitles me to switch back to \"positive review\".\n\nIt certainly does. Thanks for fixing this! It should get merged in 4.5.2.alpha1.",
    "created_at": "2010-07-22T09:11:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83037",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:8 SimonKing]:
> I changed the commit message accordingly and updated the attachments. I hope this entitles me to switch back to "positive review".

It certainly does. Thanks for fixing this! It should get merged in 4.5.2.alpha1.



---

archive/issue_events_009148.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-22T23:51:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8993#event-9148"
}
```



---

archive/issue_comments_083038.json:
```json
{
    "body": "Merged both patches in 4.5.2.alpha1.",
    "created_at": "2010-07-22T23:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83038",
    "user": "https://github.com/dandrake"
}
```

Merged both patches in 4.5.2.alpha1.



---

archive/issue_comments_083039.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T23:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8993",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8993#issuecomment-83039",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed
