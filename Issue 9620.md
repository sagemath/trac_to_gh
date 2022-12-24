# Issue 9620: conflicting branch cut conventions

archive/issues_009620.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @jdemeyer\n\nFor multi-valued complex functions, the choice of principal values and where complex branch cuts are continuous is a matter of convention but there is a clear predominant convention which has been advocated by Kahan, can be found in Guy Steele's CLTL2 (chapter 12.5.3) and is implemented in most Lisp dialects, in the C99 standard, the upcoming C++0x standard, the CLN library, Mathematica, Maple, Sage's CDF, MPMath, and many others.\n\nHowever, some libraries disagree with the predominant convention for branch cuts of inverse trigonometric and hyperbolic functions.\n\nUnfortunately for Sage, Pari is one of the systems that disagree. This leads to surprising results that are difficult to explain to new users, like this fine example:\n\n```\n  sage: acosh(-1.0-0.00001*I) - acosh(CDF(-1,-0.0000001))\n  -0.00347850806404590 + 6.27970680439127*I\n```\n\n\nIt turns out that all of Pari's branch cuts of inverse trigonometric and hyperbolic functions are somehow affected.\n\nLuckily we don't disagree about roots and the logarithm any more. :-)\n\n* asin: The asin() function is not continuous as the cut is approached coming around the finite endpoint of the cuts in a counter clockwise direction.\n\n* acos: Pari picks an unconventional principal branch in the left complex plain.\n\n* atan: The atan() function is not continous as the cut is appraoched coming around the finite endpoint of the cut along the negative imaginary axis in a counter clockwise direction.\n\n* asinh: The asinh() function is not continuous as the cut is approached coming around the finite endpoint of the cuts in a counter clockwise direction.\n\n* acosh: Pari picks an unconventional principal branch in the lower complex plain.\n\n* atanh: The atan() function is not continous as the cut is appraoched coming around the finite endpoint of the cut along the positive real axis in a counter clockwise direction.\n\nApplying the attached patch to Pari 2.3.5 in Sage 4.5.1 makes the implementations in sage.libs.mpmath, sage.libs.pari, and sage.rings.complex_double return the same values within numerical accuracy.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9620\n\n",
    "created_at": "2010-07-28T07:55:46Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "conflicting branch cut conventions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9620",
    "user": "@RBKreckel"
}
```
Assignee: @aghitza

CC:  @jdemeyer

For multi-valued complex functions, the choice of principal values and where complex branch cuts are continuous is a matter of convention but there is a clear predominant convention which has been advocated by Kahan, can be found in Guy Steele's CLTL2 (chapter 12.5.3) and is implemented in most Lisp dialects, in the C99 standard, the upcoming C++0x standard, the CLN library, Mathematica, Maple, Sage's CDF, MPMath, and many others.

However, some libraries disagree with the predominant convention for branch cuts of inverse trigonometric and hyperbolic functions.

Unfortunately for Sage, Pari is one of the systems that disagree. This leads to surprising results that are difficult to explain to new users, like this fine example:

```
  sage: acosh(-1.0-0.00001*I) - acosh(CDF(-1,-0.0000001))
  -0.00347850806404590 + 6.27970680439127*I
```


It turns out that all of Pari's branch cuts of inverse trigonometric and hyperbolic functions are somehow affected.

Luckily we don't disagree about roots and the logarithm any more. :-)

* asin: The asin() function is not continuous as the cut is approached coming around the finite endpoint of the cuts in a counter clockwise direction.

* acos: Pari picks an unconventional principal branch in the left complex plain.

* atan: The atan() function is not continous as the cut is appraoched coming around the finite endpoint of the cut along the negative imaginary axis in a counter clockwise direction.

* asinh: The asinh() function is not continuous as the cut is approached coming around the finite endpoint of the cuts in a counter clockwise direction.

* acosh: Pari picks an unconventional principal branch in the lower complex plain.

* atanh: The atan() function is not continous as the cut is appraoched coming around the finite endpoint of the cut along the positive real axis in a counter clockwise direction.

Applying the attached patch to Pari 2.3.5 in Sage 4.5.1 makes the implementations in sage.libs.mpmath, sage.libs.pari, and sage.rings.complex_double return the same values within numerical accuracy.

Issue created by migration from https://trac.sagemath.org/ticket/9620





---

archive/issue_comments_093185.json:
```json
{
    "body": "Attachment [pari-2.3.5.patch](tarball://root/attachments/some-uuid/ticket9620/pari-2.3.5.patch) by @RBKreckel created at 2010-07-28 07:56:36",
    "created_at": "2010-07-28T07:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9620#issuecomment-93185",
    "user": "@RBKreckel"
}
```

Attachment [pari-2.3.5.patch](tarball://root/attachments/some-uuid/ticket9620/pari-2.3.5.patch) by @RBKreckel created at 2010-07-28 07:56:36



---

archive/issue_comments_093186.json:
```json
{
    "body": "Reported upstream as http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1084.",
    "created_at": "2010-07-28T19:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9620#issuecomment-93186",
    "user": "@RBKreckel"
}
```

Reported upstream as http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1084.



---

archive/issue_comments_093187.json:
```json
{
    "body": "See #10430",
    "created_at": "2010-12-09T21:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9620#issuecomment-93187",
    "user": "@jdemeyer"
}
```

See #10430



---

archive/issue_comments_093188.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-10T22:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9620#issuecomment-93188",
    "user": "@jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093189.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-15T10:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9620#issuecomment-93189",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093190.json:
```json
{
    "body": "Richard B. Kreckel wrote in an email:\n\nSo, back to the review:\n\nI've checked that it works fine now. The results of pari(re+im*I).f() are compatible with f(CDF(re,im)) and mpmath.f(re+I*im) in the entire complex plain, where f is any of asin, acos, atan, asinh, acosh, and atanh.\n\nthank you\n   -richy.",
    "created_at": "2010-12-15T10:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9620#issuecomment-93190",
    "user": "@jdemeyer"
}
```

Richard B. Kreckel wrote in an email:

So, back to the review:

I've checked that it works fine now. The results of pari(re+im*I).f() are compatible with f(CDF(re,im)) and mpmath.f(re+I*im) in the entire complex plain, where f is any of asin, acos, atan, asinh, acosh, and atanh.

thank you
   -richy.



---

archive/issue_comments_093191.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-12-24T17:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9620#issuecomment-93191",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
