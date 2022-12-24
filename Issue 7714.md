# Issue 7714: bug in matrix rank over multivariate polynomial ring

archive/issues_007714.json:
```json
{
    "body": "Assignee: malb\n\nCC:  burcin\n\n\n```\nsage: matrix([PolynomialRing(GF(2),2,'x').gen()]).rank()\n[x0]\n1\n{(0, 0): x0}\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/scratch/wstein/sage/temp/sage.math.washington.edu/22996/_scratch_wstein_sage_init_sage_0.py in <module>()\n\n/scratch/wstein/build/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.rank (sage/matrix/matrix0.c:16202)()\n\n/scratch/wstein/build/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.pivots (sage/matrix/matrix0.c:16074)()\n\nRuntimeError: BUG: matrix pivots should have been set but weren't, matrix parent = 'Full MatrixSpace of 1 by 1 dense matrices over Multivariate Polynomial Ring in x0, x1 over Finite Field of size 2'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7714\n\n",
    "created_at": "2009-12-16T16:37:08Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "bug in matrix rank over multivariate polynomial ring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7714",
    "user": "was"
}
```
Assignee: malb

CC:  burcin


```
sage: matrix([PolynomialRing(GF(2),2,'x').gen()]).rank()
[x0]
1
{(0, 0): x0}
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/scratch/wstein/sage/temp/sage.math.washington.edu/22996/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.rank (sage/matrix/matrix0.c:16202)()

/scratch/wstein/build/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/matrix/matrix0.so in sage.matrix.matrix0.Matrix.pivots (sage/matrix/matrix0.c:16074)()

RuntimeError: BUG: matrix pivots should have been set but weren't, matrix parent = 'Full MatrixSpace of 1 by 1 dense matrices over Multivariate Polynomial Ring in x0, x1 over Finite Field of size 2'
```


Issue created by migration from https://trac.sagemath.org/ticket/7714





---

archive/issue_comments_066247.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-12T15:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66247",
    "user": "malb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066248.json:
```json
{
    "body": "This shouldn't print out things before throwing the error.",
    "created_at": "2010-09-23T22:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66248",
    "user": "jason"
}
```

This shouldn't print out things before throwing the error.



---

archive/issue_comments_066249.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-23T22:55:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66249",
    "user": "jason"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066250.json:
```json
{
    "body": "Attachment [trac_7714.patch](tarball://root/attachments/some-uuid/ticket7714/trac_7714.patch) by malb created at 2010-11-03 15:34:02\n\nFixed.",
    "created_at": "2010-11-03T15:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66250",
    "user": "malb"
}
```

Attachment [trac_7714.patch](tarball://root/attachments/some-uuid/ticket7714/trac_7714.patch) by malb created at 2010-11-03 15:34:02

Fixed.



---

archive/issue_comments_066251.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-03T15:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66251",
    "user": "malb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066252.json:
```json
{
    "body": "Jason, can you take another look at this ticket?",
    "created_at": "2010-11-23T17:36:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66252",
    "user": "malb"
}
```

Jason, can you take another look at this ticket?



---

archive/issue_comments_066253.json:
```json
{
    "body": "The bug of the ticket is correctly solved by the patch. However, current doctest just shows that the bug is solved by a corner case, but not a normal usage. Please, add an example of a normal case. Something like a 3x4 matrix of rank 2.",
    "created_at": "2010-12-04T16:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66253",
    "user": "lftabera"
}
```

The bug of the ticket is correctly solved by the patch. However, current doctest just shows that the bug is solved by a corner case, but not a normal usage. Please, add an example of a normal case. Something like a 3x4 matrix of rank 2.



---

archive/issue_comments_066254.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-04T16:51:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66254",
    "user": "lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066255.json:
```json
{
    "body": "Attachment [trac_7714_reviewer.patch](tarball://root/attachments/some-uuid/ticket7714/trac_7714_reviewer.patch) by lftabera created at 2011-09-13 11:05:55",
    "created_at": "2011-09-13T11:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66255",
    "user": "lftabera"
}
```

Attachment [trac_7714_reviewer.patch](tarball://root/attachments/some-uuid/ticket7714/trac_7714_reviewer.patch) by lftabera created at 2011-09-13 11:05:55



---

archive/issue_comments_066256.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-09-13T11:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66256",
    "user": "lftabera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066257.json:
```json
{
    "body": "I give a positive review to Martin's patch.\n\nI also send a reviewr patch uptading the doctest (pivots return a tuple) and adding another example.",
    "created_at": "2011-09-13T11:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66257",
    "user": "lftabera"
}
```

I give a positive review to Martin's patch.

I also send a reviewr patch uptading the doctest (pivots return a tuple) and adding another example.



---

archive/issue_comments_066258.json:
```json
{
    "body": "Reviewer patch looks good.",
    "created_at": "2011-09-13T11:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66258",
    "user": "malb"
}
```

Reviewer patch looks good.



---

archive/issue_comments_066259.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-09-13T11:44:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66259",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066260.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-17T04:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7714",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7714#issuecomment-66260",
    "user": "leif"
}
```

Resolution: fixed
