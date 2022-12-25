# Issue 9219: add a statistics chapter to the sage reference manual

archive/issues_009219.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @kcrisman\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9219\n\n",
    "created_at": "2010-06-11T18:39:11Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "add a statistics chapter to the sage reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9219",
    "user": "https://github.com/williamstein"
}
```
Assignee: mvngu

CC:  @kcrisman



Issue created by migration from https://trac.sagemath.org/ticket/9219





---

archive/issue_comments_086246.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-06-11T18:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9219#issuecomment-86246",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_086247.json:
```json
{
    "body": "Attachment [trac_9219_stats_doc.patch](tarball://root/attachments/some-uuid/ticket9219/trac_9219_stats_doc.patch) by @williamstein created at 2010-06-11 18:53:11",
    "created_at": "2010-06-11T18:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9219#issuecomment-86247",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_9219_stats_doc.patch](tarball://root/attachments/some-uuid/ticket9219/trac_9219_stats_doc.patch) by @williamstein created at 2010-06-11 18:53:11



---

archive/issue_comments_086248.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-11T18:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9219#issuecomment-86248",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086249.json:
```json
{
    "body": "Attachment [trac_9219-reviewer.patch](tarball://root/attachments/some-uuid/ticket9219/trac_9219-reviewer.patch) by @kcrisman created at 2010-06-18 17:59:41\n\nApply after initial patch and #9218's initial patch",
    "created_at": "2010-06-18T17:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9219#issuecomment-86249",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9219-reviewer.patch](tarball://root/attachments/some-uuid/ticket9219/trac_9219-reviewer.patch) by @kcrisman created at 2010-06-18 17:59:41

Apply after initial patch and #9218's initial patch



---

archive/issue_comments_086250.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-18T18:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9219#issuecomment-86250",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086251.json:
```json
{
    "body": "Looks fine except for two double colons where they shouldn't be and one indenting issue.  Note that I did *not* change all possible variables to double-backtick mode; I think that is a big enough job to require a new ticket, not to mention it's not the actual title of this ticket.",
    "created_at": "2010-06-18T18:01:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9219#issuecomment-86251",
    "user": "https://github.com/kcrisman"
}
```

Looks fine except for two double colons where they shouldn't be and one indenting issue.  Note that I did *not* change all possible variables to double-backtick mode; I think that is a big enough job to require a new ticket, not to mention it's not the actual title of this ticket.



---

archive/issue_comments_086252.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-21T10:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9219#issuecomment-86252",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_086253.json:
```json
{
    "body": "Docbuild warnings:\n\n```\ndocstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel:14: (WARNING/2) Literal block expected; none found.\ndocstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel.viterbi:20: (WARNING/2) Literal block expected; none found.\ndocstring of sage.stats.hmm.distributions.Distribution.prob:13: (WARNING/2) Literal block expected; none found.\ndocstring of sage.stats.hmm.distributions.Distribution.sample:14: (WARNING/2) Literal block expected; none found.\n```\n\nI'm closing this ticket, but I've opened #9561 as a blocker for 4.5.2.",
    "created_at": "2010-07-21T10:03:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9219",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9219#issuecomment-86253",
    "user": "https://github.com/qed777"
}
```

Docbuild warnings:

```
docstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel:14: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.chmm.GaussianHiddenMarkovModel.viterbi:20: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.distributions.Distribution.prob:13: (WARNING/2) Literal block expected; none found.
docstring of sage.stats.hmm.distributions.Distribution.sample:14: (WARNING/2) Literal block expected; none found.
```

I'm closing this ticket, but I've opened #9561 as a blocker for 4.5.2.
