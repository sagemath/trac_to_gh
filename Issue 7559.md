# Issue 7559: replace all the deprecation warning using deprecated_function_alias whenever possible

archive/issues_007559.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nathanncohen @hivert\n\nThis was suggested by Nathann Cohen. This is a followup of #7515 where a short mantra for deprecated function aliases is set-up.\n\nI'll not have the time to do this right now so any volunteer is welcome. \n\nCheers\n\nFlorent \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7559\n\n",
    "created_at": "2009-11-30T12:23:50Z",
    "labels": [
        "component: misc",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "replace all the deprecation warning using deprecated_function_alias whenever possible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7559",
    "user": "https://github.com/hivert"
}
```
Assignee: tbd

CC:  @nathanncohen @hivert

This was suggested by Nathann Cohen. This is a followup of #7515 where a short mantra for deprecated function aliases is set-up.

I'll not have the time to do this right now so any volunteer is welcome. 

Cheers

Florent 



Issue created by migration from https://trac.sagemath.org/ticket/7559





---

archive/issue_comments_064183.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-06-14T14:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64183",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064184.json:
```json
{
    "body": "This ticket isn't really a precise task. I think with #13109 any non-optimal use of deprecation should just die out eventually.\n\nI propose we close this ticket as invalid.",
    "created_at": "2012-06-14T14:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64184",
    "user": "https://github.com/vbraun"
}
```

This ticket isn't really a precise task. I think with #13109 any non-optimal use of deprecation should just die out eventually.

I propose we close this ticket as invalid.



---

archive/issue_comments_064185.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2012-06-14T14:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64185",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_064186.json:
```json
{
    "body": "I don't know about this being imprecise.  It says to replace `deprecation` with `deprecation_function_alias` wherever possible.   It's true that they will be removed someday, so this isn't a very high priority ticket!  But given that many of them haven't been removed yet, if someone really wanted to, this would be an ok thing to do by someone wanting to learn how to develop for Sage.\n\nI'm downgrading and turning this into an enhancement, since this is not really a bug at all.   Once older deprecations are removed one could also closed this ticket.",
    "created_at": "2012-06-14T14:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64186",
    "user": "https://github.com/kcrisman"
}
```

I don't know about this being imprecise.  It says to replace `deprecation` with `deprecation_function_alias` wherever possible.   It's true that they will be removed someday, so this isn't a very high priority ticket!  But given that many of them haven't been removed yet, if someone really wanted to, this would be an ok thing to do by someone wanting to learn how to develop for Sage.

I'm downgrading and turning this into an enhancement, since this is not really a bug at all.   Once older deprecations are removed one could also closed this ticket.



---

archive/issue_comments_064187.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-06-14T14:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64187",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064188.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2012-06-14T14:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64188",
    "user": "https://github.com/kcrisman"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_064189.json:
```json
{
    "body": "Any volunteers for beautifying the deprecations so that they'll look really good when we delete them next year? No? Thought so!",
    "created_at": "2012-06-14T14:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64189",
    "user": "https://github.com/vbraun"
}
```

Any volunteers for beautifying the deprecations so that they'll look really good when we delete them next year? No? Thought so!



---

archive/issue_comments_064190.json:
```json
{
    "body": "Changing priority from minor to trivial.",
    "created_at": "2012-06-14T15:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64190",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from minor to trivial.



---

archive/issue_comments_064191.json:
```json
{
    "body": "> Any volunteers for beautifying the deprecations so that they'll look really good when we delete them next year? No? Thought so!\nObviously.  However, there haven't even been any volunteers for deleting some of the deprecations in question - some of which are nearly three years old!  Just because a ticket is fairly pointless doesn't mean it isn't valid, if you take my meaning :)  Downgrading to trivial.",
    "created_at": "2012-06-14T15:27:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7559#issuecomment-64191",
    "user": "https://github.com/kcrisman"
}
```

> Any volunteers for beautifying the deprecations so that they'll look really good when we delete them next year? No? Thought so!
Obviously.  However, there haven't even been any volunteers for deleting some of the deprecations in question - some of which are nearly three years old!  Just because a ticket is fairly pointless doesn't mean it isn't valid, if you take my meaning :)  Downgrading to trivial.



---

archive/issue_events_017922.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7559#event-17922"
}
```



---

archive/issue_events_017923.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7559#event-17923"
}
```



---

archive/issue_events_017924.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7559#event-17924"
}
```



---

archive/issue_events_017925.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7559#event-17925"
}
```



---

archive/issue_events_017926.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7559#event-17926"
}
```



---

archive/issue_events_017927.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7559#event-17927"
}
```



---

archive/issue_events_017928.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7559",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7559#event-17928"
}
```
