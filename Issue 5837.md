# Issue 5837: bug in rational_diagonal_form() from QuadraticForm class

archive/issues_005837.json:
```json
{
    "body": "Assignee: LBerlioz\n\nCC:  tornaria\n\nKeywords: QuadraticForm diagonal\n\nThe following returns a non-diagonal QuadraticForm:\n\n\n```\nsage: Q=QuadraticForm(2*A) \nsage: Q.rational_diagonal_form()\nQuadratic form in 3 variables over Rational Field with coefficients:\n[ -3 -32 5184 ]\n[ * -81 26240 ]\n[ * * -2125111 ] \n```\n\n\nThis method works only when the matrix has a diagonal of only ones.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5837\n\n",
    "created_at": "2009-04-20T20:12:46Z",
    "labels": [
        "quadratic forms",
        "minor",
        "bug"
    ],
    "title": "bug in rational_diagonal_form() from QuadraticForm class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5837",
    "user": "LBerlioz"
}
```
Assignee: LBerlioz

CC:  tornaria

Keywords: QuadraticForm diagonal

The following returns a non-diagonal QuadraticForm:


```
sage: Q=QuadraticForm(2*A) 
sage: Q.rational_diagonal_form()
Quadratic form in 3 variables over Rational Field with coefficients:
[ -3 -32 5184 ]
[ * -81 26240 ]
[ * * -2125111 ] 
```


This method works only when the matrix has a diagonal of only ones.

Issue created by migration from https://trac.sagemath.org/ticket/5837





---

archive/issue_comments_045866.json:
```json
{
    "body": "Attachment [trac_5837](tarball://root/attachments/some-uuid/ticket5837/trac_5837) by LBerlioz created at 2009-04-20 20:18:20",
    "created_at": "2009-04-20T20:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5837#issuecomment-45866",
    "user": "LBerlioz"
}
```

Attachment [trac_5837](tarball://root/attachments/some-uuid/ticket5837/trac_5837) by LBerlioz created at 2009-04-20 20:18:20



---

archive/issue_comments_045867.json:
```json
{
    "body": "Attachment [trac_5837.patch](tarball://root/attachments/some-uuid/ticket5837/trac_5837.patch) by LBerlioz created at 2009-04-20 22:23:26",
    "created_at": "2009-04-20T22:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5837#issuecomment-45867",
    "user": "LBerlioz"
}
```

Attachment [trac_5837.patch](tarball://root/attachments/some-uuid/ticket5837/trac_5837.patch) by LBerlioz created at 2009-04-20 22:23:26



---

archive/issue_comments_045868.json:
```json
{
    "body": "Hi Luis, \n\nat this stage only blockers will be fixed in 3.4.1, so this ticket is getting bounced to 3.4.2. Since this bug produces mathematically incorrect answers this is also certainly not minor ;)\n\nYou should also attach a patch with a doctest that demonstrates that the problem has been fixed. Let me know if you have any questions. \n\nGonzalo: If you find  the time can you review this?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-20T22:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5837#issuecomment-45868",
    "user": "mabshoff"
}
```

Hi Luis, 

at this stage only blockers will be fixed in 3.4.1, so this ticket is getting bounced to 3.4.2. Since this bug produces mathematically incorrect answers this is also certainly not minor ;)

You should also attach a patch with a doctest that demonstrates that the problem has been fixed. Let me know if you have any questions. 

Gonzalo: If you find  the time can you review this?

Cheers,

Michael



---

archive/issue_comments_045869.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2009-04-20T22:36:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5837#issuecomment-45869",
    "user": "mabshoff"
}
```

Changing priority from minor to major.



---

archive/issue_comments_045870.json:
```json
{
    "body": "Some issues in your patch:\n\na. it's not a well formed patch (it's missing the filename to patch)\nb. some lines look badly indented, the `i=0` in the first line doesn't change the meaning, but the first `else` is paired with a `for`, not sure if that's what you actually mean.\nc. you should add a test case which shows the bug has been fixed. For instance, add something like\n {{{\n        sage: Q2=QuadraticForm(ZZ,3,[ -3,2,0 , 3,-2 , 5 ])\n        sage: Q2.rational_diagonal_form()\n        Quadratic form in 3 variables over Rational Field with coefficients: \n        [ -3 0 0 ]\n        [ * 10/3 0 ]\n        [ * * 47/10 ]\n}}}\n to the doctest.\nd. you are also changing the function to correctly handle quadratic forms with 0 in the diagonal. You should write a doctest for that case as well.\n\nPersonally, I'd avoid the exception and rewrite the code making an explicit test for `Q[i,i]Q=0`. This could also helps keeping the more natural `for i in range(n):` outer loop, which is easier to read than the `while i < n-1:` loop. The loop would just do a different thing depending on `Q[i,i]=0` or not. Just a suggestion, since you are writing the patch, do as you see is more convenient.",
    "created_at": "2009-04-20T22:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5837#issuecomment-45870",
    "user": "tornaria"
}
```

Some issues in your patch:

a. it's not a well formed patch (it's missing the filename to patch)
b. some lines look badly indented, the `i=0` in the first line doesn't change the meaning, but the first `else` is paired with a `for`, not sure if that's what you actually mean.
c. you should add a test case which shows the bug has been fixed. For instance, add something like
 {{{
        sage: Q2=QuadraticForm(ZZ,3,[ -3,2,0 , 3,-2 , 5 ])
        sage: Q2.rational_diagonal_form()
        Quadratic form in 3 variables over Rational Field with coefficients: 
        [ -3 0 0 ]
        [ * 10/3 0 ]
        [ * * 47/10 ]
}}}
 to the doctest.
d. you are also changing the function to correctly handle quadratic forms with 0 in the diagonal. You should write a doctest for that case as well.

Personally, I'd avoid the exception and rewrite the code making an explicit test for `Q[i,i]Q=0`. This could also helps keeping the more natural `for i in range(n):` outer loop, which is easier to read than the `while i < n-1:` loop. The loop would just do a different thing depending on `Q[i,i]=0` or not. Just a suggestion, since you are writing the patch, do as you see is more convenient.



---

archive/issue_comments_045871.json:
```json
{
    "body": "This issue is fixed in the doctest patch in #5954.",
    "created_at": "2009-05-18T23:47:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5837#issuecomment-45871",
    "user": "tornaria"
}
```

This issue is fixed in the doctest patch in #5954.



---

archive/issue_comments_045872.json:
```json
{
    "body": "Fixed via #5954, but credit still goes to Luiz for this ticket.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-19T00:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5837#issuecomment-45872",
    "user": "mabshoff"
}
```

Fixed via #5954, but credit still goes to Luiz for this ticket.

Cheers,

Michael



---

archive/issue_comments_045873.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-19T00:39:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5837#issuecomment-45873",
    "user": "mabshoff"
}
```

Resolution: fixed
