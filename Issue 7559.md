# Issue 7559: replace all the deprecation warning using deprecated_function_alias whenever possible

archive/issues_007559.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  ncohen hivert\n\nThis was suggested by Nathann Cohen. This is a followup of #7515 where a short mantra for deprecated function aliases is set-up.\n\nI'll not have the time to do this right now so any volunteer is welcome. \n\nCheers\n\nFlorent \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7559\n\n",
    "created_at": "2009-11-30T12:23:50Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "replace all the deprecation warning using deprecated_function_alias whenever possible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7559",
    "user": "hivert"
}
```
Assignee: tbd

CC:  ncohen hivert

This was suggested by Nathann Cohen. This is a followup of #7515 where a short mantra for deprecated function aliases is set-up.

I'll not have the time to do this right now so any volunteer is welcome. 

Cheers

Florent 



Issue created by migration from https://trac.sagemath.org/ticket/7559





---

archive/issue_comments_064299.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-14T14:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64299",
    "user": "vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064300.json:
```json
{
    "body": "This ticket isn't really a precise task. I think with #13109 any non-optimal use of deprecation should just die out eventually.\n\nI propose we close this ticket as invalid.",
    "created_at": "2012-06-14T14:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64300",
    "user": "vbraun"
}
```

This ticket isn't really a precise task. I think with #13109 any non-optimal use of deprecation should just die out eventually.

I propose we close this ticket as invalid.



---

archive/issue_comments_064301.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-06-14T14:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64301",
    "user": "kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_064302.json:
```json
{
    "body": "I don't know about this being imprecise.  It says to replace `deprecation` with `deprecation_function_alias` wherever possible.   It's true that they will be removed someday, so this isn't a very high priority ticket!  But given that many of them haven't been removed yet, if someone really wanted to, this would be an ok thing to do by someone wanting to learn how to develop for Sage.\n\nI'm downgrading and turning this into an enhancement, since this is not really a bug at all.   Once older deprecations are removed one could also closed this ticket.",
    "created_at": "2012-06-14T14:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64302",
    "user": "kcrisman"
}
```

I don't know about this being imprecise.  It says to replace `deprecation` with `deprecation_function_alias` wherever possible.   It's true that they will be removed someday, so this isn't a very high priority ticket!  But given that many of them haven't been removed yet, if someone really wanted to, this would be an ok thing to do by someone wanting to learn how to develop for Sage.

I'm downgrading and turning this into an enhancement, since this is not really a bug at all.   Once older deprecations are removed one could also closed this ticket.



---

archive/issue_comments_064303.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-06-14T14:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64303",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064304.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2012-06-14T14:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64304",
    "user": "kcrisman"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_064305.json:
```json
{
    "body": "Any volunteers for beautifying the deprecations so that they'll look really good when we delete them next year? No? Thought so!",
    "created_at": "2012-06-14T14:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64305",
    "user": "vbraun"
}
```

Any volunteers for beautifying the deprecations so that they'll look really good when we delete them next year? No? Thought so!



---

archive/issue_comments_064306.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2012-06-14T15:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64306",
    "user": "kcrisman"
}
```

Changing priority from minor to trivial.



---

archive/issue_comments_064307.json:
```json
{
    "body": "> Any volunteers for beautifying the deprecations so that they'll look really good when we delete them next year? No? Thought so!\nObviously.  However, there haven't even been any volunteers for deleting some of the deprecations in question - some of which are nearly three years old!  Just because a ticket is fairly pointless doesn't mean it isn't valid, if you take my meaning :)  Downgrading to trivial.",
    "created_at": "2012-06-14T15:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64307",
    "user": "kcrisman"
}
```

> Any volunteers for beautifying the deprecations so that they'll look really good when we delete them next year? No? Thought so!
Obviously.  However, there haven't even been any volunteers for deleting some of the deprecations in question - some of which are nearly three years old!  Just because a ticket is fairly pointless doesn't mean it isn't valid, if you take my meaning :)  Downgrading to trivial.
