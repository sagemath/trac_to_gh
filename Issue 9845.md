# Issue 9845: misspelled word in parallel help function info

archive/issues_009845.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: help info parallel\n\nsage: help(parallel)\n\nhelp on function parallel in module sage.parallel.decorate:\n\nparallel(p_iter='fork', ncpus=None, **kwds)\n    This is a decorator that gives a function a parallel interface,\n    allowing it to be called with a list of inputs, whose ***valuaes*** will\n    be computed in parallel.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9846\n\n",
    "created_at": "2010-09-01T05:48:06Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "misspelled word in parallel help function info",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9845",
    "user": "https://trac.sagemath.org/admin/accounts/users/negas"
}
```
Assignee: mvngu

Keywords: help info parallel

sage: help(parallel)

help on function parallel in module sage.parallel.decorate:

parallel(p_iter='fork', ncpus=None, **kwds)
    This is a decorator that gives a function a parallel interface,
    allowing it to be called with a list of inputs, whose ***valuaes*** will
    be computed in parallel.

Issue created by migration from https://trac.sagemath.org/ticket/9846





---

archive/issue_comments_097008.json:
```json
{
    "body": "Attachment [trac_9846_parallel_help.patch](tarball://root/attachments/some-uuid/ticket9846/trac_9846_parallel_help.patch) by @a-andre created at 2011-01-07 10:07:24",
    "created_at": "2011-01-07T10:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9845#issuecomment-97008",
    "user": "https://github.com/a-andre"
}
```

Attachment [trac_9846_parallel_help.patch](tarball://root/attachments/some-uuid/ticket9846/trac_9846_parallel_help.patch) by @a-andre created at 2011-01-07 10:07:24



---

archive/issue_events_024781.json:
```json
{
    "actor": "https://github.com/a-andre",
    "created_at": "2011-01-07T10:09:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9845#event-24781"
}
```



---

archive/issue_comments_097009.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-07T10:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9845#issuecomment-97009",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097010.json:
```json
{
    "body": "Also added an example for `__call__`.",
    "created_at": "2011-01-07T10:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9845#issuecomment-97010",
    "user": "https://github.com/a-andre"
}
```

Also added an example for `__call__`.



---

archive/issue_comments_097011.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-10T00:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9845#issuecomment-97011",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024782.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-19T22:21:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9845#event-24782"
}
```



---

archive/issue_comments_097012.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9845#issuecomment-97012",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
