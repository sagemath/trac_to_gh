# Issue 7852: solve_left for RDF matrices is WRONG

archive/issues_007852.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout\n\nObserve the docstring for solve_left for an RDF matrix:\n\n```\nsage: A = random_matrix(RDF,3)\nsage: A.solve_left?\nSolve the equation A*x = b, where\n        \n        EXAMPLES:\n            sage: A = matrix(RDF, 3,3, [1,2,5,7.6,2.3,1,1,2,-1]); A\n            [ 1.0  2.0  5.0]\n            [ 7.6  2.3  1.0]\n            [ 1.0  2.0 -1.0]\n            sage: b = vector(RDF,[1,2,3])\n            sage: x = A.solve_left(b); x\n            (-0.113695090439, 1.39018087855, -0.333333333333)\n            sage: A*x\n            (1.0, 2.0, 3.0)\n```\n\n\nBut that is solve_right. \n\nThis was evidently introduced by maybe Grout's \"Switch the RDF and CDF matrices to a numpy 1.2 backend; factor out common functionality to matrix_double_dense.pyx.\".\n\nReported by Stephanie Dietzel\n\nIssue created by migration from https://trac.sagemath.org/ticket/7852\n\n",
    "created_at": "2010-01-05T21:40:18Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "solve_left for RDF matrices is WRONG",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7852",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @jasongrout

Observe the docstring for solve_left for an RDF matrix:

```
sage: A = random_matrix(RDF,3)
sage: A.solve_left?
Solve the equation A*x = b, where
        
        EXAMPLES:
            sage: A = matrix(RDF, 3,3, [1,2,5,7.6,2.3,1,1,2,-1]); A
            [ 1.0  2.0  5.0]
            [ 7.6  2.3  1.0]
            [ 1.0  2.0 -1.0]
            sage: b = vector(RDF,[1,2,3])
            sage: x = A.solve_left(b); x
            (-0.113695090439, 1.39018087855, -0.333333333333)
            sage: A*x
            (1.0, 2.0, 3.0)
```


But that is solve_right. 

This was evidently introduced by maybe Grout's "Switch the RDF and CDF matrices to a numpy 1.2 backend; factor out common functionality to matrix_double_dense.pyx.".

Reported by Stephanie Dietzel

Issue created by migration from https://trac.sagemath.org/ticket/7852





---

archive/issue_comments_067898.json:
```json
{
    "body": "This might be related to #4932.  I'll put this on my list for the bug day coming up.",
    "created_at": "2010-01-05T22:16:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67898",
    "user": "https://github.com/jasongrout"
}
```

This might be related to #4932.  I'll put this on my list for the bug day coming up.



---

archive/issue_comments_067899.json:
```json
{
    "body": "Attachment [trac_7852-solve-linear-systems-CDF.patch](tarball://root/attachments/some-uuid/ticket7852/trac_7852-solve-linear-systems-CDF.patch) by @rbeezer created at 2011-02-24 22:33:43",
    "created_at": "2011-02-24T22:33:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67899",
    "user": "https://github.com/rbeezer"
}
```

Attachment [trac_7852-solve-linear-systems-CDF.patch](tarball://root/attachments/some-uuid/ticket7852/trac_7852-solve-linear-systems-CDF.patch) by @rbeezer created at 2011-02-24 22:33:43



---

archive/issue_comments_067900.json:
```json
{
    "body": "Patch corrects the naming problem, and creates upgraded ``solve_left`` and ``solve_right``.\n\nThis required just a few touch-ups where the name had been wrong, or the improved accuracy changed results.",
    "created_at": "2011-02-24T22:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67900",
    "user": "https://github.com/rbeezer"
}
```

Patch corrects the naming problem, and creates upgraded ``solve_left`` and ``solve_right``.

This required just a few touch-ups where the name had been wrong, or the improved accuracy changed results.



---

archive/issue_comments_067901.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-02-24T22:36:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67901",
    "user": "https://github.com/rbeezer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067902.json:
```json
{
    "body": "Without the patch, \"solve_right\" seems to work for nonsquare matrices over RDF, I guess because it's using the generic \"solve_right\" method from matrix2.pyx.  With the patch, it looks like this won't work any more; is that right?  Is there a good reason for not allowing square matrices?  We could instead add a method `_solve_right_nonsingular_square` to matrix_double_dense.pyx, and then I think this should be called by the generic solve_right method.\n\nFor \"solve_left\", could we just remove the version from matrix_double_dense.pyx altogether, and just use the generic version?",
    "created_at": "2011-03-21T19:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67902",
    "user": "https://github.com/jhpalmieri"
}
```

Without the patch, "solve_right" seems to work for nonsquare matrices over RDF, I guess because it's using the generic "solve_right" method from matrix2.pyx.  With the patch, it looks like this won't work any more; is that right?  Is there a good reason for not allowing square matrices?  We could instead add a method `_solve_right_nonsingular_square` to matrix_double_dense.pyx, and then I think this should be called by the generic solve_right method.

For "solve_left", could we just remove the version from matrix_double_dense.pyx altogether, and just use the generic version?



---

archive/issue_comments_067903.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n\nYes, there is some tension in handling inexact matrices with routines designed for exact matrices (which is the root issue here, I believe).  `NumPy/SciPy` just does not do certain things, such as computing a rank.\n\nI'm hoping to get some guidance from the `NumPy` folks here at Sage Days 29 right now and we can chat some more.",
    "created_at": "2011-03-21T21:04:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67903",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:4 jhpalmieri]:

Yes, there is some tension in handling inexact matrices with routines designed for exact matrices (which is the root issue here, I believe).  `NumPy/SciPy` just does not do certain things, such as computing a rank.

I'm hoping to get some guidance from the `NumPy` folks here at Sage Days 29 right now and we can chat some more.



---

archive/issue_comments_067904.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-25T03:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67904",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067905.json:
```json
{
    "body": "1) You can use svd to first get a square matrix that you can use to solve the system of linear equations.\n2) Why do you copy the code for left and right solve. There is a generic fallback in matrix2.pyx. If you want to replace the docstring for this class, can't you do just that?",
    "created_at": "2011-03-25T03:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67905",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

1) You can use svd to first get a square matrix that you can use to solve the system of linear equations.
2) Why do you copy the code for left and right solve. There is a generic fallback in matrix2.pyx. If you want to replace the docstring for this class, can't you do just that?



---

archive/issue_comments_067906.json:
```json
{
    "body": "We could use a direct call to `SciPy` solve for square nonsingular and analyze/exploit the SVD for nonsingular/rectangular.",
    "created_at": "2011-03-25T17:50:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67906",
    "user": "https://github.com/rbeezer"
}
```

We could use a direct call to `SciPy` solve for square nonsingular and analyze/exploit the SVD for nonsingular/rectangular.



---

archive/issue_comments_067907.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-07-18T04:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67907",
    "user": "https://github.com/rbeezer"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067908.json:
```json
{
    "body": "Finally getting back to this one.\n\n1.  solve_left and solve_right are confused at the moment - I think this is important to fix.\n\n2.  The code is different, in part because the error messages are explicit, naming rows and columns when sizes do not match.\n\n3.  The longer I think about it, the more I think we should *never* be feeding floating-point matrices into exact routines.  We should expose the ScyPy/NumPy/LAPACK routines as much as possible and not pretend the exact routines are going to give reasonable answers as a \"fallback.\"\n\n4.  I'm happy to try to get solutions to systems with non-square coefficient matrices with floating-point entries, but despite a lot of thought and reading, I'm not convinced of the right approach.  In any event, I'd like to fix the problem at hand, and do the non-square somewhere else.\n\n5.  I am going to set this to \"needs review\" but I'm happy to entertain more discussion - I'll just need convincing.\n\nRob",
    "created_at": "2011-07-18T04:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67908",
    "user": "https://github.com/rbeezer"
}
```

Finally getting back to this one.

1.  solve_left and solve_right are confused at the moment - I think this is important to fix.

2.  The code is different, in part because the error messages are explicit, naming rows and columns when sizes do not match.

3.  The longer I think about it, the more I think we should *never* be feeding floating-point matrices into exact routines.  We should expose the ScyPy/NumPy/LAPACK routines as much as possible and not pretend the exact routines are going to give reasonable answers as a "fallback."

4.  I'm happy to try to get solutions to systems with non-square coefficient matrices with floating-point entries, but despite a lot of thought and reading, I'm not convinced of the right approach.  In any event, I'd like to fix the problem at hand, and do the non-square somewhere else.

5.  I am going to set this to "needs review" but I'm happy to entertain more discussion - I'll just need convincing.

Rob



---

archive/issue_comments_067909.json:
```json
{
    "body": "What I was talking about when I mentioned the fallback is a piece of generic code for solve_left that calls solve_right. Thus you only need to implement one version. And you should, because code duplication makes mistakes more likely and maintenance harder. I will change this when reviewing this, and then will wait for your approval.",
    "created_at": "2011-08-04T10:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67909",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

What I was talking about when I mentioned the fallback is a piece of generic code for solve_left that calls solve_right. Thus you only need to implement one version. And you should, because code duplication makes mistakes more likely and maintenance harder. I will change this when reviewing this, and then will wait for your approval.



---

archive/issue_comments_067910.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-05T16:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67910",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067911.json:
```json
{
    "body": "I didn't touch the implementation of solve_right.  I changed my mind for the following simple reason. While the code is quite short and easy to check the documentation is very different (left replaced by right). So it seems quite impractical to duplicate it.\n\nWe should think about modifying the documentation so that it gets included in the reference manual. Also there is a pseudoregression in the code. Sage doesn't pretend it could solve equations with double dense matrices as right hand side. Scipy covers also this case, so we should open a new ticket for this.",
    "created_at": "2011-08-05T16:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67911",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

I didn't touch the implementation of solve_right.  I changed my mind for the following simple reason. While the code is quite short and easy to check the documentation is very different (left replaced by right). So it seems quite impractical to duplicate it.

We should think about modifying the documentation so that it gets included in the reference manual. Also there is a pseudoregression in the code. Sage doesn't pretend it could solve equations with double dense matrices as right hand side. Scipy covers also this case, so we should open a new ticket for this.



---

archive/issue_comments_067912.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2011-09-08T16:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67912",
    "user": "https://github.com/nexttime"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_067913.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-13T12:15:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67913",
    "user": "https://github.com/nexttime"
}
```

Resolution: fixed



---

archive/issue_comments_067914.json:
```json
{
    "body": "Attachment [trac_7852-fix_noise_errors_in_preparser_examples.reviewer.patch](tarball://root/attachments/some-uuid/ticket7852/trac_7852-fix_noise_errors_in_preparser_examples.reviewer.patch) by @nexttime created at 2011-09-26 01:22:48\n\nReviewer patch. Apply on top of main patch, which causes a signed zero on Itanium 2.",
    "created_at": "2011-09-26T01:22:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67914",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_7852-fix_noise_errors_in_preparser_examples.reviewer.patch](tarball://root/attachments/some-uuid/ticket7852/trac_7852-fix_noise_errors_in_preparser_examples.reviewer.patch) by @nexttime created at 2011-09-26 01:22:48

Reviewer patch. Apply on top of main patch, which causes a signed zero on Itanium 2.



---

archive/issue_comments_067915.json:
```json
{
    "body": "Attachment [trac_7852-fix_noise_errors_in_polys.reviewer.patch](tarball://root/attachments/some-uuid/ticket7852/trac_7852-fix_noise_errors_in_polys.reviewer.patch) by @nexttime created at 2011-09-26 01:24:49\n\nReviewer patch. Apply on top of main patch, which causes doctests to fail on a couple of systems due to noisy zero terms.",
    "created_at": "2011-09-26T01:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67915",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_7852-fix_noise_errors_in_polys.reviewer.patch](tarball://root/attachments/some-uuid/ticket7852/trac_7852-fix_noise_errors_in_polys.reviewer.patch) by @nexttime created at 2011-09-26 01:24:49

Reviewer patch. Apply on top of main patch, which causes doctests to fail on a couple of systems due to noisy zero terms.



---

archive/issue_comments_067916.json:
```json
{
    "body": "Attached two reviewer patches fixing doctest errors on some systems.\n\nThird patch to fix doctest errors in `sage/matrix/matrix_double_dense.pyx` coming soon.\n\nThe patch to the preparser examples requires #11848.",
    "created_at": "2011-09-26T01:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67916",
    "user": "https://github.com/nexttime"
}
```

Attached two reviewer patches fixing doctest errors on some systems.

Third patch to fix doctest errors in `sage/matrix/matrix_double_dense.pyx` coming soon.

The patch to the preparser examples requires #11848.



---

archive/issue_comments_067917.json:
```json
{
    "body": "Reviewer patch. Apply on top of main patch, which causes another doctest to fail on a couple of systems due to a noisy zero in a vector result.",
    "created_at": "2011-09-26T02:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67917",
    "user": "https://github.com/nexttime"
}
```

Reviewer patch. Apply on top of main patch, which causes another doctest to fail on a couple of systems due to a noisy zero in a vector result.



---

archive/issue_comments_067918.json:
```json
{
    "body": "Attachment [trac_7852-fix_noisy_zero_error_in_matrix_double_dense.reviewer.patch](tarball://root/attachments/some-uuid/ticket7852/trac_7852-fix_noisy_zero_error_in_matrix_double_dense.reviewer.patch) by @nexttime created at 2011-09-26 02:46:34\n\nThird reviewer patch (fixing a doctest error in `matrix_double_dense.pyx`) is up.",
    "created_at": "2011-09-26T02:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67918",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_7852-fix_noisy_zero_error_in_matrix_double_dense.reviewer.patch](tarball://root/attachments/some-uuid/ticket7852/trac_7852-fix_noisy_zero_error_in_matrix_double_dense.reviewer.patch) by @nexttime created at 2011-09-26 02:46:34

Third reviewer patch (fixing a doctest error in `matrix_double_dense.pyx`) is up.



---

archive/issue_comments_067919.json:
```json
{
    "body": "The three reviewer patches apply, build and pass their tests once #11848 is applied to a recent alpha3 prerelease that already has the main patch.  Currently passes all tests in `sage/matrix` but will run full tests overnight.\n\nThis has a positive review from me based on the reviewer contributions, but is marked as closed right now anyway.  I'll only retreat if something unexpected happens overnight.\n\nLeif - thank-you very much for getting these noisy tests cleaned up.\n\nRob",
    "created_at": "2011-09-26T03:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67919",
    "user": "https://github.com/rbeezer"
}
```

The three reviewer patches apply, build and pass their tests once #11848 is applied to a recent alpha3 prerelease that already has the main patch.  Currently passes all tests in `sage/matrix` but will run full tests overnight.

This has a positive review from me based on the reviewer contributions, but is marked as closed right now anyway.  I'll only retreat if something unexpected happens overnight.

Leif - thank-you very much for getting these noisy tests cleaned up.

Rob



---

archive/issue_comments_067920.json:
```json
{
    "body": "Reviewer patch. Slightly adjust threshold for noisy zero terms in polynomials, needed on MacOS X 10.6 x86_64 with GCC 4.2.1. Apply on top of other patches (i.e., the other reviewer patch to `polynomial_element.pyx`).",
    "created_at": "2011-09-27T21:46:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67920",
    "user": "https://github.com/nexttime"
}
```

Reviewer patch. Slightly adjust threshold for noisy zero terms in polynomials, needed on MacOS X 10.6 x86_64 with GCC 4.2.1. Apply on top of other patches (i.e., the other reviewer patch to `polynomial_element.pyx`).



---

archive/issue_comments_067921.json:
```json
{
    "body": "Attachment [trac_7852-adjust_noisy_zero_term_threshold_for_polys.reviewer.patch](tarball://root/attachments/some-uuid/ticket7852/trac_7852-adjust_noisy_zero_term_threshold_for_polys.reviewer.patch) by @nexttime created at 2011-09-27 21:52:53\n\nI've attached yet another patch slightly increasing one epsilon, since one doctest still failed on MacOS X 10.6 (due to almost zero terms in a polynomial).",
    "created_at": "2011-09-27T21:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67921",
    "user": "https://github.com/nexttime"
}
```

Attachment [trac_7852-adjust_noisy_zero_term_threshold_for_polys.reviewer.patch](tarball://root/attachments/some-uuid/ticket7852/trac_7852-adjust_noisy_zero_term_threshold_for_polys.reviewer.patch) by @nexttime created at 2011-09-27 21:52:53

I've attached yet another patch slightly increasing one epsilon, since one doctest still failed on MacOS X 10.6 (due to almost zero terms in a polynomial).



---

archive/issue_comments_067922.json:
```json
{
    "body": "Yes, I meant to bring this up in the flurry of noisy doctest fixes.  I have taken to not cutting it too fine on the zeros.  For example, if I get a \"zero\" on the order of `10^-16`, then I have taken to clipping zeros at `10^-14`.  There seems to be too much variability across systems, so if you cut it too close, then some system is eventually going to complain, it seems.\n\nThe latest patch looks good and applies and builds find, passing all tests in `sage/ring/polynomial` on the alpha3-prerelease I picked up about 10 days ago.  So ready to go, again.",
    "created_at": "2011-09-28T14:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67922",
    "user": "https://github.com/rbeezer"
}
```

Yes, I meant to bring this up in the flurry of noisy doctest fixes.  I have taken to not cutting it too fine on the zeros.  For example, if I get a "zero" on the order of `10^-16`, then I have taken to clipping zeros at `10^-14`.  There seems to be too much variability across systems, so if you cut it too close, then some system is eventually going to complain, it seems.

The latest patch looks good and applies and builds find, passing all tests in `sage/ring/polynomial` on the alpha3-prerelease I picked up about 10 days ago.  So ready to go, again.



---

archive/issue_comments_067923.json:
```json
{
    "body": "Follow-up ticket further increasing the threshold for noisy zero terms in polynomials (from 2.5e-15, needed for `bsd.math`, to 2.7e-15) for MacOS X 10.4 PPC once more: #11901",
    "created_at": "2011-10-07T17:16:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7852",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7852#issuecomment-67923",
    "user": "https://github.com/nexttime"
}
```

Follow-up ticket further increasing the threshold for noisy zero terms in polynomials (from 2.5e-15, needed for `bsd.math`, to 2.7e-15) for MacOS X 10.4 PPC once more: #11901
