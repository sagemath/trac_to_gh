# Issue 2330: modforms -- implement computation of weight 1 forms in Sage

archive/issues_002330.json:
```json
{
    "body": "Assignee: was\n\nKevin Buzzard and I intend to do this ASAP based on algorithms he designed in 2002.\n\nIf you see this and are interested in helping, send me an email (wstein`@`gmail.com).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2330\n\n",
    "created_at": "2008-02-27T11:02:54Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.2",
    "title": "modforms -- implement computation of weight 1 forms in Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2330",
    "user": "was"
}
```
Assignee: was

Kevin Buzzard and I intend to do this ASAP based on algorithms he designed in 2002.

If you see this and are interested in helping, send me an email (wstein`@`gmail.com).

Issue created by migration from https://trac.sagemath.org/ticket/2330





---

archive/issue_comments_015577.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-02-27T11:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15577",
    "user": "was"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_015578.json:
```json
{
    "body": "Changing assignee from was to craigcitro.",
    "created_at": "2008-04-13T01:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15578",
    "user": "AlexGhitza"
}
```

Changing assignee from was to craigcitro.



---

archive/issue_comments_015579.json:
```json
{
    "body": "Changing component from number theory to modular forms.",
    "created_at": "2008-04-13T01:56:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15579",
    "user": "AlexGhitza"
}
```

Changing component from number theory to modular forms.



---

archive/issue_comments_015580.json:
```json
{
    "body": "Presumably this would be based on http://wwwf.imperial.ac.uk/~buzzard/maths/research/papers/wt1.pdf",
    "created_at": "2017-02-06T18:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15580",
    "user": "roed"
}
```

Presumably this would be based on http://wwwf.imperial.ac.uk/~buzzard/maths/research/papers/wt1.pdf



---

archive/issue_comments_015581.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-11-08T02:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15581",
    "user": "davidloeffler"
}
```

New commits:



---

archive/issue_comments_015582.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2017-11-08T02:52:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15582",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_015583.json:
```json
{
    "body": "It's awesome to have weight 1 forms!\n\nOverall, the code looks good.  A few issues to be addressed:\n\n* There's a plugin failure complaining about two lines with non-ASCII characters\n* The definition of `R` in the docstring of `modular_ratio_space` is off by one compared to the usage of `R` in the code.",
    "created_at": "2017-11-08T07:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15583",
    "user": "roed"
}
```

It's awesome to have weight 1 forms!

Overall, the code looks good.  A few issues to be addressed:

* There's a plugin failure complaining about two lines with non-ASCII characters
* The definition of `R` in the docstring of `modular_ratio_space` is off by one compared to the usage of `R` in the code.



---

archive/issue_comments_015584.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2017-11-08T07:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15584",
    "user": "roed"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_015585.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-11-08T12:00:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15585",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_015586.json:
```json
{
    "body": "This should address those two issues.\n----\nNew commits:",
    "created_at": "2017-11-08T12:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15586",
    "user": "davidloeffler"
}
```

This should address those two issues.
----
New commits:



---

archive/issue_comments_015587.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-11-08T12:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15587",
    "user": "davidloeffler"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_015588.json:
```json
{
    "body": "I'm a bit puzzled that four out of the five patchbot reports for the first version of the code are reporting test failures, all of which are nothing to do with the ticket as far as I can see -- is there something wrong with the patchbot? Most of them seem to be timeout errors.",
    "created_at": "2017-11-08T12:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15588",
    "user": "davidloeffler"
}
```

I'm a bit puzzled that four out of the five patchbot reports for the first version of the code are reporting test failures, all of which are nothing to do with the ticket as far as I can see -- is there something wrong with the patchbot? Most of them seem to be timeout errors.



---

archive/issue_comments_015589.json:
```json
{
    "body": "I'm not sure what's wrong with the other patchbots, but I've seen some of these errors in other places.  It's certainly not a problem with your code.\n\nLooks good!",
    "created_at": "2017-11-08T18:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15589",
    "user": "roed"
}
```

I'm not sure what's wrong with the other patchbots, but I've seen some of these errors in other places.  It's certainly not a problem with your code.

Looks good!



---

archive/issue_comments_015590.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-11-08T18:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15590",
    "user": "roed"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_015591.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-12-11T01:04:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2330",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2330#issuecomment-15591",
    "user": "vbraun"
}
```

Resolution: fixed
