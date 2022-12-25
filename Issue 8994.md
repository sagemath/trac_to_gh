# Issue 8994: Improve convolution support

archive/issues_008994.json:
```json
{
    "body": "Assignee: @burcin\n\nKeywords: convolution, convolve, discrete, continuous\n\nWe have convolution scattered in several places, including\n\n```\nsage.rings.polynomial.convolution\nsage.functions.piecewise.PiecewisePolynomial.convolution\nsage.gsl.dft.IndexedSequence.convolution\n```\n\nThis should be extended to make it easier to use/find and to support more arbitrary inputs, both discrete and continuous.\n\nSee [http://groups.google.com/group/sage-support/browse_thread/thread/7f90c228df9530dd](http://groups.google.com/group/sage-support/browse_thread/thread/7f90c228df9530dd) for background.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8994\n\n",
    "created_at": "2010-05-19T17:21:31Z",
    "labels": [
        "component: symbolics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "Improve convolution support",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8994",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @burcin

Keywords: convolution, convolve, discrete, continuous

We have convolution scattered in several places, including

```
sage.rings.polynomial.convolution
sage.functions.piecewise.PiecewisePolynomial.convolution
sage.gsl.dft.IndexedSequence.convolution
```

This should be extended to make it easier to use/find and to support more arbitrary inputs, both discrete and continuous.

See [http://groups.google.com/group/sage-support/browse_thread/thread/7f90c228df9530dd](http://groups.google.com/group/sage-support/browse_thread/thread/7f90c228df9530dd) for background.

Issue created by migration from https://trac.sagemath.org/ticket/8994





---

archive/issue_comments_083040.json:
```json
{
    "body": "Updated description to reflect changes in new `piecewise` implementation (#14801).\nChanging to \"wishlist\" because nobody seems to have worked on it in 6 years",
    "created_at": "2016-06-25T17:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8994#issuecomment-83040",
    "user": "https://github.com/mkoeppe"
}
```

Updated description to reflect changes in new `piecewise` implementation (#14801).
Changing to "wishlist" because nobody seems to have worked on it in 6 years
