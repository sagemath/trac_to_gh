# Issue 9080: add F-distribution support for RealDistribution

archive/issues_009080.json:
```json
{
    "body": "Assignee: amhou\n\nadd the F-distribution to the supported distributions for RealDistribution\n\nIssue created by migration from https://trac.sagemath.org/ticket/9080\n\n",
    "closed_at": "2011-07-22T12:49:00Z",
    "created_at": "2010-05-29T03:54:56Z",
    "labels": [
        "component: statistics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.2",
    "title": "add F-distribution support for RealDistribution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9080",
    "user": "https://github.com/kwankyu"
}
```
Assignee: amhou

add the F-distribution to the supported distributions for RealDistribution

Issue created by migration from https://trac.sagemath.org/ticket/9080





---

archive/issue_comments_084154.json:
```json
{
    "body": "Attachment [trac#9080.patch](tarball://root/attachments/some-uuid/ticket9080/trac#9080.patch) by @kwankyu created at 2010-05-29 03:59:00\n\nThe patch adds F-distribution.",
    "created_at": "2010-05-29T03:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84154",
    "user": "https://github.com/kwankyu"
}
```

Attachment [trac#9080.patch](tarball://root/attachments/some-uuid/ticket9080/trac#9080.patch) by @kwankyu created at 2010-05-29 03:59:00

The patch adds F-distribution.



---

archive/issue_comments_084155.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-29T03:59:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84155",
    "user": "https://github.com/kwankyu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084156.json:
```json
{
    "body": "You may want to rebase this against 4.6.alpha1 if necessary.  Also, the commit message should start with `Trac 9080` or something like that.  Finally, maybe the error message should say that this is not a supported distribution?  It's certainly conceivable that there would be one in the literature which isn't yet in Sage or GSL :)",
    "created_at": "2010-09-21T20:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84156",
    "user": "https://github.com/kcrisman"
}
```

You may want to rebase this against 4.6.alpha1 if necessary.  Also, the commit message should start with `Trac 9080` or something like that.  Finally, maybe the error message should say that this is not a supported distribution?  It's certainly conceivable that there would be one in the literature which isn't yet in Sage or GSL :)



---

archive/issue_comments_084157.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-21T20:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84157",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_084158.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-25T01:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84158",
    "user": "https://github.com/kwankyu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_084159.json:
```json
{
    "body": "I rebased the patch to the latest release of Sage (4.5.3). It was fun (and sad...) to see all different flavors of the heads of the commit messages used by developers. I followed the one DEMANDED by the developer manual. I changed all the error message as suggested.",
    "created_at": "2010-09-25T01:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84159",
    "user": "https://github.com/kwankyu"
}
```

I rebased the patch to the latest release of Sage (4.5.3). It was fun (and sad...) to see all different flavors of the heads of the commit messages used by developers. I followed the one DEMANDED by the developer manual. I changed all the error message as suggested.



---

archive/issue_comments_084160.json:
```json
{
    "body": "revised according to the reviewer's comments",
    "created_at": "2010-09-25T01:32:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84160",
    "user": "https://github.com/kwankyu"
}
```

revised according to the reviewer's comments



---

archive/issue_comments_084161.json:
```json
{
    "body": "Attachment [trac_9080.patch](tarball://root/attachments/some-uuid/ticket9080/trac_9080.patch) by @kwankyu created at 2010-09-25 01:41:06\n\nThere is a slight inconsistency even in the developer manual. In the section \"Producing Patches with Mercurial\", \"trac xxxx: ...\" is suggested while \"Trac xxxx: ...\" seems to be the official standard.",
    "created_at": "2010-09-25T01:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84161",
    "user": "https://github.com/kwankyu"
}
```

Attachment [trac_9080.patch](tarball://root/attachments/some-uuid/ticket9080/trac_9080.patch) by @kwankyu created at 2010-09-25 01:41:06

There is a slight inconsistency even in the developer manual. In the section "Producing Patches with Mercurial", "trac xxxx: ..." is suggested while "Trac xxxx: ..." seems to be the official standard.



---

archive/issue_comments_084162.json:
```json
{
    "body": "Replying to [comment:4 klee]:\n> There is a slight inconsistency even in the developer manual. In the section \"Producing Patches with Mercurial\", \"trac xxxx: ...\" is suggested while \"Trac xxxx: ...\" seems to be the official standard.\n\nYou could ask on sage-devel about this - for me, it's not so crucial, but mvngu might have an informed opinion.",
    "created_at": "2010-09-25T17:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84162",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:4 klee]:
> There is a slight inconsistency even in the developer manual. In the section "Producing Patches with Mercurial", "trac xxxx: ..." is suggested while "Trac xxxx: ..." seems to be the official standard.

You could ask on sage-devel about this - for me, it's not so crucial, but mvngu might have an informed opinion.



---

archive/issue_comments_084163.json:
```json
{
    "body": "Attachment [trac_9080-rebased.patch](tarball://root/attachments/some-uuid/ticket9080/trac_9080-rebased.patch) by @kcrisman created at 2011-06-16 23:58:51",
    "created_at": "2011-06-16T23:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84163",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9080-rebased.patch](tarball://root/attachments/some-uuid/ticket9080/trac_9080-rebased.patch) by @kcrisman created at 2011-06-16 23:58:51



---

archive/issue_comments_084164.json:
```json
{
    "body": "I've rebased this against 4.7.1.alpha2.",
    "created_at": "2011-06-17T00:51:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84164",
    "user": "https://github.com/kcrisman"
}
```

I've rebased this against 4.7.1.alpha2.



---

archive/issue_comments_084165.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-06-17T00:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84165",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084166.json:
```json
{
    "body": "Positive review.   Gives correct values, checked with Wolfram Alpha.  Not surprising, since GSL is a very stable library.\n\nBut we need a lot more doctests for just about all of these - see #11514.",
    "created_at": "2011-06-17T00:58:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84166",
    "user": "https://github.com/kcrisman"
}
```

Positive review.   Gives correct values, checked with Wolfram Alpha.  Not surprising, since GSL is a very stable library.

But we need a lot more doctests for just about all of these - see #11514.



---

archive/issue_events_022248.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-06-18T09:27:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "milestone": "sage-4.7.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9080#event-22248"
}
```



---

archive/issue_events_022249.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-07-22T12:49:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9080#event-22249"
}
```



---

archive/issue_comments_084167.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-07-22T12:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9080",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9080#issuecomment-84167",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
