# Issue 9561: Docbuild warnings caused by #9219

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-21 10:01:54

Assignee: mvngu

CC:  kcrisman mvngu

The forthcoming 4.5.2.alpha0 includes #9219, which appears to cause the following docbuild warnings:

```
docstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel:14: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel.viterbi:20: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.distributions.Distribution.prob:13: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.distributions.Distribution.sample:14: (WARNING/2) Literal block expected; none found.
```



---

Comment by kcrisman created at 2010-07-22 14:15:06

This was caused by someone getting too excited about 

```
EXAMPLES::
```

which does indeed often introduce actual examples, but now is more likely to have more text before the code itself.  Should be very easy review.


---

Attachment

Based on 4.5.1 plus relevant patches


---

Comment by kcrisman created at 2010-07-22 14:18:00

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-07-22 14:18:00

Either do 4.5.1 and patches from #9218 and #9219, or base on 4.5.2.alpha0.  This should remove the warnings.


---

Comment by jhpalmieri created at 2010-07-23 00:32:12

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-23 02:29:55

Resolution: fixed
