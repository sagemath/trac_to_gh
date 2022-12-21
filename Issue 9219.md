# Issue 9219: add a statistics chapter to the sage reference manual

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-11 18:39:11

Assignee: mvngu

CC:  kcrisman




---

Comment by was created at 2010-06-11 18:39:19

Changing type from defect to enhancement.


---

Attachment


---

Comment by was created at 2010-06-11 18:53:11

Changing status from new to needs_review.


---

Attachment

Apply after initial patch and #9218's initial patch


---

Comment by kcrisman created at 2010-06-18 18:01:10

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-06-18 18:01:10

Looks fine except for two double colons where they shouldn't be and one indenting issue.  Note that I did *not* change all possible variables to double-backtick mode; I think that is a big enough job to require a new ticket, not to mention it's not the actual title of this ticket.


---

Comment by mpatel created at 2010-07-21 10:03:09

Resolution: fixed


---

Comment by mpatel created at 2010-07-21 10:03:09

Docbuild warnings:

```
docstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel:14: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel.viterbi:20: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.distributions.Distribution.prob:13: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.distributions.Distribution.sample:14: (WARNING/2) Literal block expected; none found.
```

I'm closing this ticket, but I've opened #9561 as a blocker for 4.5.2.
