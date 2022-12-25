# Issue 7458: [with patch, needs review] Sylvester matrix for polynomials

archive/issues_007458.json:
```json
{
    "body": "Assignee: @malb\n\nSmall patch to add Sylvester matrix calculation for univariate and multivariate polynomials.\n\nI think that my patch is a bit more general (and has doctests) compared to didier deshommes' patch here, which seems to have never been merged:\n\nhttp://sage.math.washington.edu/home/dfdeshom/custom/patches/sylveste...\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7458\n\n",
    "created_at": "2009-11-14T13:00:01Z",
    "labels": [
        "component: commutative algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "[with patch, needs review] Sylvester matrix for polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7458",
    "user": "https://trac.sagemath.org/admin/accounts/users/carlohamalainen"
}
```
Assignee: @malb

Small patch to add Sylvester matrix calculation for univariate and multivariate polynomials.

I think that my patch is a bit more general (and has doctests) compared to didier deshommes' patch here, which seems to have never been merged:

http://sage.math.washington.edu/home/dfdeshom/custom/patches/sylveste...


Issue created by migration from https://trac.sagemath.org/ticket/7458





---

archive/issue_comments_062705.json:
```json
{
    "body": "Attachment [sylvester.patch](tarball://root/attachments/some-uuid/ticket7458/sylvester.patch) by @lftabera created at 2010-11-06 11:47:07",
    "created_at": "2010-11-06T11:47:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7458#issuecomment-62705",
    "user": "https://github.com/lftabera"
}
```

Attachment [sylvester.patch](tarball://root/attachments/some-uuid/ticket7458/sylvester.patch) by @lftabera created at 2010-11-06 11:47:07



---

archive/issue_comments_062706.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-11-06T12:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7458#issuecomment-62706",
    "user": "https://github.com/lftabera"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_062707.json:
```json
{
    "body": "Attachment [trac-7458-sylvester-rebase-4.6.patch](tarball://root/attachments/some-uuid/ticket7458/trac-7458-sylvester-rebase-4.6.patch) by @lftabera created at 2010-11-06 12:06:38\n\nThis is a very basic feature that has to be in Sage.\n\nI have rebased Carlo patch to 4.6  but have not touched the code.\n\nI have some concerns that makes me mark the patch as needs work:\n\n- The univariate case should accept the same syntax as the multivariate case. In the univariate case, the preferred call is f.sylvester_matrix(g), but I do not want Sage to throw an error if I wrote f.sylvester_matrix(g, x)\n\n- Corner cases must be well documented. \n\n\n```\nsage: K.<x>=QQ[]\nsage: K(1).sylvester_matrix(K(1))\n[]\n```\n\n\nIn particular, I am not sure how to deal with the sylvester matrix of 0 and constant or 0 and 0\nCurretly it throws an error. My opinion is that this is not defined but  should throw a more meaningful error.\n\nMaple for instance return the empty matrix. So in maple:\n\nDeterminant(Sylvester_Matrix)  != Resultant \n\nIn this corner cases.\n\nI will  try to check what other CAS do to get a wider picture.\n\n- An example explicitly relating Sylvester matrix and resultant should be added.",
    "created_at": "2010-11-06T12:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7458#issuecomment-62707",
    "user": "https://github.com/lftabera"
}
```

Attachment [trac-7458-sylvester-rebase-4.6.patch](tarball://root/attachments/some-uuid/ticket7458/trac-7458-sylvester-rebase-4.6.patch) by @lftabera created at 2010-11-06 12:06:38

This is a very basic feature that has to be in Sage.

I have rebased Carlo patch to 4.6  but have not touched the code.

I have some concerns that makes me mark the patch as needs work:

- The univariate case should accept the same syntax as the multivariate case. In the univariate case, the preferred call is f.sylvester_matrix(g), but I do not want Sage to throw an error if I wrote f.sylvester_matrix(g, x)

- Corner cases must be well documented. 


```
sage: K.<x>=QQ[]
sage: K(1).sylvester_matrix(K(1))
[]
```


In particular, I am not sure how to deal with the sylvester matrix of 0 and constant or 0 and 0
Curretly it throws an error. My opinion is that this is not defined but  should throw a more meaningful error.

Maple for instance return the empty matrix. So in maple:

Determinant(Sylvester_Matrix)  != Resultant 

In this corner cases.

I will  try to check what other CAS do to get a wider picture.

- An example explicitly relating Sylvester matrix and resultant should be added.



---

archive/issue_comments_062708.json:
```json
{
    "body": "Changing keywords from \"\" to \"Sylvester matrix\".",
    "created_at": "2010-11-06T12:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7458#issuecomment-62708",
    "user": "https://github.com/lftabera"
}
```

Changing keywords from "" to "Sylvester matrix".



---

archive/issue_comments_062709.json:
```json
{
    "body": "- I have added more documentation and doctest.\n\n- The variable argument is now optional in both univariate and multivariate. If it is not used, the first variable of the polynomial ring is used.\n\n- I have added coercion to be able to compute the Sylvester matrix of polynomials in different rings, for ex. ZZ[x] and QQ[x] \n\n- solved an issue for the dimension of the matrix of the sylvester matrix of (x**n, 0)\n\nIt is not ready for review because the sylvester matrix of (0,0) is not implemented.",
    "created_at": "2010-11-06T17:30:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7458#issuecomment-62709",
    "user": "https://github.com/lftabera"
}
```

- I have added more documentation and doctest.

- The variable argument is now optional in both univariate and multivariate. If it is not used, the first variable of the polynomial ring is used.

- I have added coercion to be able to compute the Sylvester matrix of polynomials in different rings, for ex. ZZ[x] and QQ[x] 

- solved an issue for the dimension of the matrix of the sylvester matrix of (x**n, 0)

It is not ready for review because the sylvester matrix of (0,0) is not implemented.



---

archive/issue_comments_062710.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-12T13:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7458#issuecomment-62710",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062711.json:
```json
{
    "body": "Attachment [trac-7458-sylvester-improvements.patch](tarball://root/attachments/some-uuid/ticket7458/trac-7458-sylvester-improvements.patch) by @lftabera created at 2010-11-12 13:36:54\n\nFinally, if one of the polynomials is zero, the code raises a ValueError.",
    "created_at": "2010-11-12T13:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7458#issuecomment-62711",
    "user": "https://github.com/lftabera"
}
```

Attachment [trac-7458-sylvester-improvements.patch](tarball://root/attachments/some-uuid/ticket7458/trac-7458-sylvester-improvements.patch) by @lftabera created at 2010-11-12 13:36:54

Finally, if one of the polynomials is zero, the code raises a ValueError.



---

archive/issue_comments_062712.json:
```json
{
    "body": "Apply trac-7458-sylvester-rebase-4.6.patch, trac-7458-sylvester-improvements.patch",
    "created_at": "2010-12-04T12:51:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7458#issuecomment-62712",
    "user": "https://github.com/lftabera"
}
```

Apply trac-7458-sylvester-rebase-4.6.patch, trac-7458-sylvester-improvements.patch



---

archive/issue_comments_062713.json:
```json
{
    "body": "Very nice. I am impressed with the thoroughness of the testing of corner cases here. All doctests in sage/rings pass, and the reference manual builds OK.",
    "created_at": "2010-12-16T11:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7458#issuecomment-62713",
    "user": "https://github.com/loefflerd"
}
```

Very nice. I am impressed with the thoroughness of the testing of corner cases here. All doctests in sage/rings pass, and the reference manual builds OK.



---

archive/issue_comments_062714.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-16T11:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7458#issuecomment-62714",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007684.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-01-26T22:26:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7458#event-7684"
}
```



---

archive/issue_comments_062715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-26T22:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7458",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7458#issuecomment-62715",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
