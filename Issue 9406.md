# Issue 9406: Multi-dimensional polynomial fit

archive/issues_009406.json:
```json
{
    "body": "Assignee: olazo\n\nCC:  @nathanncohen\n\nKeywords: polynomial,fit\n\nAt this point, the only way (to my knowledge) to use the least-squares algorithm within sage is trough numpy.polyfit, which is limited to 1-dimensional polynomials. It takes a list of 2-tuples which are interpreted as points of the form (x,P). And returns an array of coefficients of the polynomial with the specified degree.\n\nI've written a sage script that works for arbitrary dimensions, taking a list of N-tuples, and returns a polynomial (as a sage-expression) with the specified degree for each dimension.\n\nI'll post this as soon as I gain access to off-line sage (at this point I am stuck without it).\n\nThis would bring us closer to Mathematica's mighty Fit:\n\n[http://reference.wolfram.com/mathematica/ref/Fit.html](http://reference.wolfram.com/mathematica/ref/Fit.html)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9406\n\n",
    "created_at": "2010-07-02T03:06:24Z",
    "labels": [
        "numerical",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.1",
    "title": "Multi-dimensional polynomial fit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9406",
    "user": "olazo"
}
```
Assignee: olazo

CC:  @nathanncohen

Keywords: polynomial,fit

At this point, the only way (to my knowledge) to use the least-squares algorithm within sage is trough numpy.polyfit, which is limited to 1-dimensional polynomials. It takes a list of 2-tuples which are interpreted as points of the form (x,P). And returns an array of coefficients of the polynomial with the specified degree.

I've written a sage script that works for arbitrary dimensions, taking a list of N-tuples, and returns a polynomial (as a sage-expression) with the specified degree for each dimension.

I'll post this as soon as I gain access to off-line sage (at this point I am stuck without it).

This would bring us closer to Mathematica's mighty Fit:

[http://reference.wolfram.com/mathematica/ref/Fit.html](http://reference.wolfram.com/mathematica/ref/Fit.html)

Issue created by migration from https://trac.sagemath.org/ticket/9406





---

archive/issue_comments_089630.json:
```json
{
    "body": "It seems that a much more powerful tool than the one I was about to submit is already included in sage: find_fit. Since find_fit already does everything I proposed, I advice this ticket to be closed.",
    "created_at": "2010-07-15T19:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9406#issuecomment-89630",
    "user": "olazo"
}
```

It seems that a much more powerful tool than the one I was about to submit is already included in sage: find_fit. Since find_fit already does everything I proposed, I advice this ticket to be closed.



---

archive/issue_comments_089631.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2010-07-18T19:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9406",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9406#issuecomment-89631",
    "user": "@rlmill"
}
```

Resolution: worksforme
