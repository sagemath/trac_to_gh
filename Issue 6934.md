# Issue 6934: Fix eigenvectors (and a lot of other stuff) for symbolic matrices

archive/issues_006934.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout @rbeezer\n\nKeywords: symbolics, matrices, polynomials\n\nFrom sage-devel [http://groups.google.com/group/sage-devel/browse_thread/thread/4f39037d7fd17133](http://groups.google.com/group/sage-devel/browse_thread/thread/4f39037d7fd17133) we have the following:\n\n```\nsage: A=matrix(SR,[[1,2,3],[4,5,6],[7,8,9]]) \nsage: A.eigenvectors_right() \nTraceback (most recent call last): \n... \nTypeError: degree() takes exactly one argument (0 given)\n```\n\nAs it turns out, there are a HOST of things you can't do with A because of the new symbolics, which no one has yet implemented.  Another example:\n\n```\nsage: A = matrix(SR, [[1,2,3],[4,5,6],[7,8,9]])\nsage: A.charpoly()\n(x - 1)*((x - 9)*(x - 5) - 48) - 29*x - 3\nsage: type(_)\n<type 'sage.symbolic.expression.Expression'>\nsage: B = matrix(QQ, [[1,2,3],[4,5,6],[7,8,9]])\nsage: B.charpoly()\nx^3 - 15*x^2 - 18*x\nsage: type(_)\n<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense'>\n```\n\nwhich means minpoly does not work (because it requires a polynomial, not an expression) and so on. \n\nThese were not caught before because these things were not tested, since they weren't actually implemented in the dense symbolic matrix file.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6934\n\n",
    "created_at": "2009-09-15T13:46:05Z",
    "labels": [
        "linear algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Fix eigenvectors (and a lot of other stuff) for symbolic matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6934",
    "user": "@kcrisman"
}
```
Assignee: @williamstein

CC:  @jasongrout @rbeezer

Keywords: symbolics, matrices, polynomials

From sage-devel [http://groups.google.com/group/sage-devel/browse_thread/thread/4f39037d7fd17133](http://groups.google.com/group/sage-devel/browse_thread/thread/4f39037d7fd17133) we have the following:

```
sage: A=matrix(SR,[[1,2,3],[4,5,6],[7,8,9]]) 
sage: A.eigenvectors_right() 
Traceback (most recent call last): 
... 
TypeError: degree() takes exactly one argument (0 given)
```

As it turns out, there are a HOST of things you can't do with A because of the new symbolics, which no one has yet implemented.  Another example:

```
sage: A = matrix(SR, [[1,2,3],[4,5,6],[7,8,9]])
sage: A.charpoly()
(x - 1)*((x - 9)*(x - 5) - 48) - 29*x - 3
sage: type(_)
<type 'sage.symbolic.expression.Expression'>
sage: B = matrix(QQ, [[1,2,3],[4,5,6],[7,8,9]])
sage: B.charpoly()
x^3 - 15*x^2 - 18*x
sage: type(_)
<class 'sage.rings.polynomial.polynomial_element_generic.Polynomial_rational_dense'>
```

which means minpoly does not work (because it requires a polynomial, not an expression) and so on. 

These were not caught before because these things were not tested, since they weren't actually implemented in the dense symbolic matrix file.

Issue created by migration from https://trac.sagemath.org/ticket/6934





---

archive/issue_comments_057293.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-09-15T13:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57293",
    "user": "@kcrisman"
}
```

Changing priority from major to critical.



---

archive/issue_comments_057294.json:
```json
{
    "body": "Note that #6936 will help make this ticket more specific.",
    "created_at": "2009-09-15T18:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57294",
    "user": "@kcrisman"
}
```

Note that #6936 will help make this ticket more specific.



---

archive/issue_comments_057295.json:
```json
{
    "body": "See also #5639 which needs a review -- wink, wink.",
    "created_at": "2009-11-10T04:17:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57295",
    "user": "@mwhansen"
}
```

See also #5639 which needs a review -- wink, wink.



---

archive/issue_comments_057296.json:
```json
{
    "body": "I've attached an initial cut.  This needs doctests and testing in general.",
    "created_at": "2009-11-10T05:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57296",
    "user": "@jasongrout"
}
```

I've attached an initial cut.  This needs doctests and testing in general.



---

archive/issue_comments_057297.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-11-10T05:32:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57297",
    "user": "@jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_057298.json:
```json
{
    "body": "friendly reminder \u2026 will this be ready soon? can I do anything to speed this up? (i.e., what exactly still needs to be done here? where do I even have to apply this?)",
    "created_at": "2010-05-25T16:10:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57298",
    "user": "matthiasr"
}
```

friendly reminder … will this be ready soon? can I do anything to speed this up? (i.e., what exactly still needs to be done here? where do I even have to apply this?)



---

archive/issue_comments_057299.json:
```json
{
    "body": "Several things need to be done:\n\n1. Documentation for the function needs to be written.\n\n2. doctests need to be run in Sage to check to make sure something didn't break.\n\nTo apply the patch, you can follow the instructions in the Sage Developer's guide.",
    "created_at": "2010-05-25T16:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57299",
    "user": "@jasongrout"
}
```

Several things need to be done:

1. Documentation for the function needs to be written.

2. doctests need to be run in Sage to check to make sure something didn't break.

To apply the patch, you can follow the instructions in the Sage Developer's guide.



---

archive/issue_comments_057300.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-25T17:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57300",
    "user": "@jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_057301.json:
```json
{
    "body": "Attachment [trac-6934-SR-eigenvectors.patch](tarball://root/attachments/some-uuid/ticket6934/trac-6934-SR-eigenvectors.patch) by @jasongrout created at 2010-05-25 17:02:55\n\nOkay, I fixed everything and this should be ready for review now.  Doctests pass on 4.4.1 in matrix/*.py[x]",
    "created_at": "2010-05-25T17:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57301",
    "user": "@jasongrout"
}
```

Attachment [trac-6934-SR-eigenvectors.patch](tarball://root/attachments/some-uuid/ticket6934/trac-6934-SR-eigenvectors.patch) by @jasongrout created at 2010-05-25 17:02:55

Okay, I fixed everything and this should be ready for review now.  Doctests pass on 4.4.1 in matrix/*.py[x]



---

archive/issue_comments_057302.json:
```json
{
    "body": "Hi Jason,\n\nI can't get this to finish on a non-trivial 3x3 matrix.\n\n9 different variables:  100 minutes, 2 GB memory used, killed my system\n\n3x3 `VanderMonde` matrix, with one variable per row (each row is the 0, 1, 2 powers of the variable).  I killed it after 5 minutes.\n\nSo, yes, this would be nice for completeness, but seems of very limited value.  Do you (or anybody reading this) have any bigger, more interesting examples that actually finish?\n\nThe characteristic polynomial of a symbolic matrix can be computed quite quickly.  I don't imagine there is a good way to factor such a thing, though?\n\nRob",
    "created_at": "2010-05-28T17:16:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57302",
    "user": "@rbeezer"
}
```

Hi Jason,

I can't get this to finish on a non-trivial 3x3 matrix.

9 different variables:  100 minutes, 2 GB memory used, killed my system

3x3 `VanderMonde` matrix, with one variable per row (each row is the 0, 1, 2 powers of the variable).  I killed it after 5 minutes.

So, yes, this would be nice for completeness, but seems of very limited value.  Do you (or anybody reading this) have any bigger, more interesting examples that actually finish?

The characteristic polynomial of a symbolic matrix can be computed quite quickly.  I don't imagine there is a good way to factor such a thing, though?

Rob



---

archive/issue_comments_057303.json:
```json
{
    "body": "Well, once nice thing is that the eigenvectors/eigenvalues of a numeric matrix (like in the description) return root symbols instead of QQbar elements.  There have been lots of people complaining that the eigenvalues of a 2x2 matrix should just have square root signs.  With this patch, eigenvectors works too.",
    "created_at": "2010-05-28T18:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57303",
    "user": "@jasongrout"
}
```

Well, once nice thing is that the eigenvectors/eigenvalues of a numeric matrix (like in the description) return root symbols instead of QQbar elements.  There have been lots of people complaining that the eigenvalues of a 2x2 matrix should just have square root signs.  With this patch, eigenvectors works too.



---

archive/issue_comments_057304.json:
```json
{
    "body": "I might add that mathematica is fast (almost instantaneous) because they just punt to saying \"roots of this huge symbolic characteristic polynomial\".\n\nIt's too bad that we don't have a generic RootOf construct (I don't believe maxima has one either).  The closest we get is QQbar, but that only works for rational polynomials.",
    "created_at": "2010-05-28T18:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57304",
    "user": "@jasongrout"
}
```

I might add that mathematica is fast (almost instantaneous) because they just punt to saying "roots of this huge symbolic characteristic polynomial".

It's too bad that we don't have a generic RootOf construct (I don't believe maxima has one either).  The closest we get is QQbar, but that only works for rational polynomials.



---

archive/issue_comments_057305.json:
```json
{
    "body": "Attachment [trac_6934-reviewer-doctests.patch](tarball://root/attachments/some-uuid/ticket6934/trac_6934-reviewer-doctests.patch) by @rbeezer created at 2010-05-29 06:03:53\n\nOK, I see.  For example, this does a nice job with eigenvalues of graphs.  I've attached some doctests along these lines - if you want to include them, then go ahead and provide the review for the reviewer patch.  I'm clear for a positive review on the rest.",
    "created_at": "2010-05-29T06:03:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57305",
    "user": "@rbeezer"
}
```

Attachment [trac_6934-reviewer-doctests.patch](tarball://root/attachments/some-uuid/ticket6934/trac_6934-reviewer-doctests.patch) by @rbeezer created at 2010-05-29 06:03:53

OK, I see.  For example, this does a nice job with eigenvalues of graphs.  I've attached some doctests along these lines - if you want to include them, then go ahead and provide the review for the reviewer patch.  I'm clear for a positive review on the rest.



---

archive/issue_comments_057306.json:
```json
{
    "body": "Attachment [trac-6934-more-doctest-issues.patch](tarball://root/attachments/some-uuid/ticket6934/trac-6934-more-doctest-issues.patch) by @jasongrout created at 2010-09-03 21:53:07\n\napply on top of previous patches",
    "created_at": "2010-09-03T21:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57306",
    "user": "@jasongrout"
}
```

Attachment [trac-6934-more-doctest-issues.patch](tarball://root/attachments/some-uuid/ticket6934/trac-6934-more-doctest-issues.patch) by @jasongrout created at 2010-09-03 21:53:07

apply on top of previous patches



---

archive/issue_comments_057307.json:
```json
{
    "body": "Okay, back to you Rob.  I fixed one small problem with your docstring, but then realized that the file isn't included in the manual anyway.  So I added it to the manual and fixed two other small documentation problems.\n\nIf you think my changes are good, please set the ticket to positive review.",
    "created_at": "2010-09-03T21:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57307",
    "user": "@jasongrout"
}
```

Okay, back to you Rob.  I fixed one small problem with your docstring, but then realized that the file isn't included in the manual anyway.  So I added it to the manual and fixed two other small documentation problems.

If you think my changes are good, please set the ticket to positive review.



---

archive/issue_comments_057308.json:
```json
{
    "body": "Builds, passes all tests (-testall on 4.5.2) and the docs (the newly included module anyway) look good.  Thanks for the corrections on my additions.  I think this one is done.",
    "created_at": "2010-09-04T02:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57308",
    "user": "@rbeezer"
}
```

Builds, passes all tests (-testall on 4.5.2) and the docs (the newly included module anyway) look good.  Thanks for the corrections on my additions.  I think this one is done.



---

archive/issue_comments_057309.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-04T02:31:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57309",
    "user": "@rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057310.json:
```json
{
    "body": "Could someone please prepend the ticket number to the commit string for [attachment:trac-6934-more-doctest-issues.patch] (and restore the status to \"positive review\")?",
    "created_at": "2010-09-05T04:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57310",
    "user": "@qed777"
}
```

Could someone please prepend the ticket number to the commit string for [attachment:trac-6934-more-doctest-issues.patch] (and restore the status to "positive review")?



---

archive/issue_comments_057311.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-05T04:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57311",
    "user": "@qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_057312.json:
```json
{
    "body": "Attachment [trac-6934-more-doctests-issues.patch](tarball://root/attachments/some-uuid/ticket6934/trac-6934-more-doctests-issues.patch) by @rbeezer created at 2010-09-05 06:31:29",
    "created_at": "2010-09-05T06:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57312",
    "user": "@rbeezer"
}
```

Attachment [trac-6934-more-doctests-issues.patch](tarball://root/attachments/some-uuid/ticket6934/trac-6934-more-doctests-issues.patch) by @rbeezer created at 2010-09-05 06:31:29



---

archive/issue_comments_057313.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-05T06:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57313",
    "user": "@rbeezer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_057314.json:
```json
{
    "body": "Fixed the patch, tried to replace the existing one, but a stray \"S\" came into the filename.\n\nSo the third patch to apply for this ticket is the fourth one present at the moment, with \"doctests\" in the middle of the filename.",
    "created_at": "2010-09-05T06:34:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57314",
    "user": "@rbeezer"
}
```

Fixed the patch, tried to replace the existing one, but a stray "S" came into the filename.

So the third patch to apply for this ticket is the fourth one present at the moment, with "doctests" in the middle of the filename.



---

archive/issue_comments_057315.json:
```json
{
    "body": "Thanks!",
    "created_at": "2010-09-15T09:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57315",
    "user": "@qed777"
}
```

Thanks!



---

archive/issue_comments_057316.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T09:55:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6934",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6934#issuecomment-57316",
    "user": "@qed777"
}
```

Resolution: fixed
