# Issue 7147: Change settings for INCLUDE_MPFR_PATCH from "1"  or "0" to "yes" or "no"

archive/issues_007147.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  david.kirkby@onetel.ne\n\nDue to a bug in Solaris, MPFR can fail tests on sun4v machines.\n\nWe have solved this (#6453) some months back.,I added some code to a shell script that could apply the patch or not depending on whether INCLUDE_MPFR_PATCH was set to 1 (apply patch) or 0 (do not apply). Given other variable in Sage use \"yes\" or \"no\", it would be sensible this was changed to be consistent. Clearly this is a very trivial patch, \n\nIssue created by migration from https://trac.sagemath.org/ticket/7147\n\n",
    "created_at": "2009-10-07T18:06:42Z",
    "labels": [
        "porting: Solaris",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Change settings for INCLUDE_MPFR_PATCH from \"1\"  or \"0\" to \"yes\" or \"no\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7147",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  david.kirkby@onetel.ne

Due to a bug in Solaris, MPFR can fail tests on sun4v machines.

We have solved this (#6453) some months back.,I added some code to a shell script that could apply the patch or not depending on whether INCLUDE_MPFR_PATCH was set to 1 (apply patch) or 0 (do not apply). Given other variable in Sage use "yes" or "no", it would be sensible this was changed to be consistent. Clearly this is a very trivial patch, 

Issue created by migration from https://trac.sagemath.org/ticket/7147





---

archive/issue_comments_059225.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-19T04:09:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7147#issuecomment-59225",
    "user": "@aghitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059226.json:
```json
{
    "body": "Where's the patch?",
    "created_at": "2009-10-19T04:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7147#issuecomment-59226",
    "user": "@aghitza"
}
```

Where's the patch?



---

archive/issue_comments_059227.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2009-10-19T04:11:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7147#issuecomment-59227",
    "user": "@aghitza"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_059228.json:
```json
{
    "body": "I'm closing this as invalid, as the variable can take on 3 values - 0, 1 and 2, not a yes/no.",
    "created_at": "2009-12-03T04:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7147#issuecomment-59228",
    "user": "drkirkby"
}
```

I'm closing this as invalid, as the variable can take on 3 values - 0, 1 and 2, not a yes/no.



---

archive/issue_comments_059229.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-12-03T04:51:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7147",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7147#issuecomment-59229",
    "user": "drkirkby"
}
```

Resolution: invalid
