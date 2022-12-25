# Issue 2330: modforms -- implement computation of weight 1 forms in Sage

archive/issues_002330.json:
```json
{
    "body": "Assignee: @williamstein\n\nKevin Buzzard and I intend to do this ASAP based on algorithms he designed in 2002.\n\nIf you see this and are interested in helping, send me an email (wstein`@`gmail.com).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2330\n\n",
    "created_at": "2008-02-27T11:02:54Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "modforms -- implement computation of weight 1 forms in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2330",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Kevin Buzzard and I intend to do this ASAP based on algorithms he designed in 2002.

If you see this and are interested in helping, send me an email (wstein`@`gmail.com).

Issue created by migration from https://trac.sagemath.org/ticket/2330





---

archive/issue_comments_015542.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-02-27T11:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15542",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_015543.json:
```json
{
    "body": "Changing assignee from @williamstein to @craigcitro.",
    "created_at": "2008-04-13T01:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15543",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @craigcitro.



---

archive/issue_comments_015544.json:
```json
{
    "body": "Changing component from number theory to modular forms.",
    "created_at": "2008-04-13T01:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15544",
    "user": "https://github.com/aghitza"
}
```

Changing component from number theory to modular forms.



---

archive/issue_comments_015545.json:
```json
{
    "body": "Presumably this would be based on http://wwwf.imperial.ac.uk/~buzzard/maths/research/papers/wt1.pdf",
    "created_at": "2017-02-06T18:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15545",
    "user": "https://github.com/roed314"
}
```

Presumably this would be based on http://wwwf.imperial.ac.uk/~buzzard/maths/research/papers/wt1.pdf



---

archive/issue_comments_015546.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-11-08T02:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15546",
    "user": "https://github.com/loefflerd"
}
```

New commits:



---

archive/issue_comments_015547.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-11-08T02:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15547",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_015548.json:
```json
{
    "body": "It's awesome to have weight 1 forms!\n\nOverall, the code looks good.  A few issues to be addressed:\n\n* There's a plugin failure complaining about two lines with non-ASCII characters\n* The definition of `R` in the docstring of `modular_ratio_space` is off by one compared to the usage of `R` in the code.",
    "created_at": "2017-11-08T07:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15548",
    "user": "https://github.com/roed314"
}
```

It's awesome to have weight 1 forms!

Overall, the code looks good.  A few issues to be addressed:

* There's a plugin failure complaining about two lines with non-ASCII characters
* The definition of `R` in the docstring of `modular_ratio_space` is off by one compared to the usage of `R` in the code.



---

archive/issue_comments_015549.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-11-08T07:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15549",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_015550.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-11-08T12:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15550",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_015551.json:
```json
{
    "body": "This should address those two issues.\n----\nNew commits:",
    "created_at": "2017-11-08T12:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15551",
    "user": "https://github.com/loefflerd"
}
```

This should address those two issues.
----
New commits:



---

archive/issue_comments_015552.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-11-08T12:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15552",
    "user": "https://github.com/loefflerd"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_015553.json:
```json
{
    "body": "I'm a bit puzzled that four out of the five patchbot reports for the first version of the code are reporting test failures, all of which are nothing to do with the ticket as far as I can see -- is there something wrong with the patchbot? Most of them seem to be timeout errors.",
    "created_at": "2017-11-08T12:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15553",
    "user": "https://github.com/loefflerd"
}
```

I'm a bit puzzled that four out of the five patchbot reports for the first version of the code are reporting test failures, all of which are nothing to do with the ticket as far as I can see -- is there something wrong with the patchbot? Most of them seem to be timeout errors.



---

archive/issue_comments_015554.json:
```json
{
    "body": "I'm not sure what's wrong with the other patchbots, but I've seen some of these errors in other places.  It's certainly not a problem with your code.\n\nLooks good!",
    "created_at": "2017-11-08T18:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15554",
    "user": "https://github.com/roed314"
}
```

I'm not sure what's wrong with the other patchbots, but I've seen some of these errors in other places.  It's certainly not a problem with your code.

Looks good!



---

archive/issue_comments_015555.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-11-08T18:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15555",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_002508.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2017-12-11T01:04:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2330#event-2508"
}
```



---

archive/issue_comments_015556.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-12-11T01:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15556",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
