# Issue 9845: misspelled word in parallel help function info

archive/issues_009845.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: help info parallel\n\nsage: help(parallel)\n\nhelp on function parallel in module sage.parallel.decorate:\n\nparallel(p_iter='fork', ncpus=None, **kwds)\n    This is a decorator that gives a function a parallel interface,\n    allowing it to be called with a list of inputs, whose ***valuaes*** will\n    be computed in parallel.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9846\n\n",
    "created_at": "2010-09-01T05:48:06Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "misspelled word in parallel help function info",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9845",
    "user": "negas"
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

archive/issue_comments_097167.json:
```json
{
    "body": "Attachment [trac_9846_parallel_help.patch](tarball://root/attachments/some-uuid/ticket9846/trac_9846_parallel_help.patch) by aapitzsch created at 2011-01-07 10:07:24",
    "created_at": "2011-01-07T10:07:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9845#issuecomment-97167",
    "user": "aapitzsch"
}
```

Attachment [trac_9846_parallel_help.patch](tarball://root/attachments/some-uuid/ticket9846/trac_9846_parallel_help.patch) by aapitzsch created at 2011-01-07 10:07:24



---

archive/issue_comments_097168.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-07T10:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9845#issuecomment-97168",
    "user": "aapitzsch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097169.json:
```json
{
    "body": "Also added an example for `__call__`.",
    "created_at": "2011-01-07T10:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9845#issuecomment-97169",
    "user": "aapitzsch"
}
```

Also added an example for `__call__`.



---

archive/issue_comments_097170.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-10T00:02:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9845#issuecomment-97170",
    "user": "aly.deines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097171.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9845",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9845#issuecomment-97171",
    "user": "jdemeyer"
}
```

Resolution: fixed
