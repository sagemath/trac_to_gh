# Issue 9561: Docbuild warnings caused by #9219

archive/issues_009561.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  kcrisman mvngu\n\nThe forthcoming 4.5.2.alpha0 includes #9219, which appears to cause the following docbuild warnings:\n\n```\ndocstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel:14: (WARNING/2) Literal block expected; none found.\ndocstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel.viterbi:20: (WARNING/2) Literal block expected; none found.\ndocstring of sage.stats.hmm.distributions.Distribution.prob:13: (WARNING/2) Literal block expected; none found.\ndocstring of sage.stats.hmm.distributions.Distribution.sample:14: (WARNING/2) Literal block expected; none found.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9561\n\n",
    "created_at": "2010-07-21T10:01:54Z",
    "labels": [
        "documentation",
        "blocker",
        "bug"
    ],
    "title": "Docbuild warnings caused by #9219",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9561",
    "user": "mpatel"
}
```
Assignee: mvngu

CC:  kcrisman mvngu

The forthcoming 4.5.2.alpha0 includes #9219, which appears to cause the following docbuild warnings:

```
docstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel:14: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel.viterbi:20: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.distributions.Distribution.prob:13: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.distributions.Distribution.sample:14: (WARNING/2) Literal block expected; none found.
```


Issue created by migration from https://trac.sagemath.org/ticket/9561





---

archive/issue_comments_092166.json:
```json
{
    "body": "This was caused by someone getting too excited about \n\n```\nEXAMPLES::\n```\n\nwhich does indeed often introduce actual examples, but now is more likely to have more text before the code itself.  Should be very easy review.",
    "created_at": "2010-07-22T14:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9561#issuecomment-92166",
    "user": "kcrisman"
}
```

This was caused by someone getting too excited about 

```
EXAMPLES::
```

which does indeed often introduce actual examples, but now is more likely to have more text before the code itself.  Should be very easy review.



---

archive/issue_comments_092167.json:
```json
{
    "body": "Attachment\n\nBased on 4.5.1 plus relevant patches",
    "created_at": "2010-07-22T14:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9561#issuecomment-92167",
    "user": "kcrisman"
}
```

Attachment

Based on 4.5.1 plus relevant patches



---

archive/issue_comments_092168.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-22T14:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9561#issuecomment-92168",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092169.json:
```json
{
    "body": "Either do 4.5.1 and patches from #9218 and #9219, or base on 4.5.2.alpha0.  This should remove the warnings.",
    "created_at": "2010-07-22T14:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9561#issuecomment-92169",
    "user": "kcrisman"
}
```

Either do 4.5.1 and patches from #9218 and #9219, or base on 4.5.2.alpha0.  This should remove the warnings.



---

archive/issue_comments_092170.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T00:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9561#issuecomment-92170",
    "user": "jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092171.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-23T02:29:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9561",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9561#issuecomment-92171",
    "user": "ddrake"
}
```

Resolution: fixed
