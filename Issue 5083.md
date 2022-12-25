# Issue 5083: Colormap updating?

archive/issues_005083.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  abergeron @williamstein @mwhansen\n\nReferring to #4884 and the last set of comments there - loose ends for colormap info:\n\n1. So should there be cmap_help or not?  abergeron's last statement  in #4884 implies yes.  If so...\n\n2. For every function (e.g. matrix_plot) where cmap is an option, that function's docstring should have as a doctest a full call of cmap_help (or whatever with its output.  Also in the cmap_help doctest should have the whole output of cmap_help show up, not have ... where the actual colormaps are outputted.\n\nIf neither of these things are true, please close this ticket.  It seemed like both were true, though.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5083\n\n",
    "created_at": "2009-01-24T02:44:59Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Colormap updating?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5083",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @williamstein

CC:  abergeron @williamstein @mwhansen

Referring to #4884 and the last set of comments there - loose ends for colormap info:

1. So should there be cmap_help or not?  abergeron's last statement  in #4884 implies yes.  If so...

2. For every function (e.g. matrix_plot) where cmap is an option, that function's docstring should have as a doctest a full call of cmap_help (or whatever with its output.  Also in the cmap_help doctest should have the whole output of cmap_help show up, not have ... where the actual colormaps are outputted.

If neither of these things are true, please close this ticket.  It seemed like both were true, though.

Issue created by migration from https://trac.sagemath.org/ticket/5083





---

archive/issue_comments_038662.json:
```json
{
    "body": "Tickets are not a good place for discussions, I will start a thread on sage-devel.",
    "created_at": "2009-01-24T02:50:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5083#issuecomment-38662",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```

Tickets are not a good place for discussions, I will start a thread on sage-devel.



---

archive/issue_comments_038663.json:
```json
{
    "body": "Sorry, I was not trying to cause trouble, just trying to ask for clarification and a followup ticket seemed appropriate as opposed to spamming sage-devel.",
    "created_at": "2009-01-24T02:56:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5083#issuecomment-38663",
    "user": "https://github.com/kcrisman"
}
```

Sorry, I was not trying to cause trouble, just trying to ask for clarification and a followup ticket seemed appropriate as opposed to spamming sage-devel.



---

archive/issue_comments_038664.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> Sorry, I was not trying to cause trouble, just trying to ask for clarification and a followup ticket seemed appropriate as opposed to spamming sage-devel.\n\n\nDo not worry about it. The merge of the cmap patch was somewhat rushed and may be not the optimal solution, but given the time table back then it was the right decision. \n\nAs Arnaud pointed out such discussions should be help on [sage-devel] since it is difficult for many people interested in this problem would be even aware that it is happening. Discussions on tickets also make the ticket harder to merge since I tend to read the ticket and when one has many it slows me down. One prime example of a messy ticket is the boolean logic one as well as the TinyMCE mess (sorry Jason :). It all gets resolved, but if the volume on [sage-devel] is too high people need to switch to digest mode for example.\n\nThe summary of the ticket should also be improved since the current title is meaningless to anyone not aware of the previous ticket. Fortunately you referred the ticket here, but you should also mention on the old ticket that the follow up ticket is this one.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-24T03:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5083#issuecomment-38664",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 kcrisman]:
> Sorry, I was not trying to cause trouble, just trying to ask for clarification and a followup ticket seemed appropriate as opposed to spamming sage-devel.


Do not worry about it. The merge of the cmap patch was somewhat rushed and may be not the optimal solution, but given the time table back then it was the right decision. 

As Arnaud pointed out such discussions should be help on [sage-devel] since it is difficult for many people interested in this problem would be even aware that it is happening. Discussions on tickets also make the ticket harder to merge since I tend to read the ticket and when one has many it slows me down. One prime example of a messy ticket is the boolean logic one as well as the TinyMCE mess (sorry Jason :). It all gets resolved, but if the volume on [sage-devel] is too high people need to switch to digest mode for example.

The summary of the ticket should also be improved since the current title is meaningless to anyone not aware of the previous ticket. Fortunately you referred the ticket here, but you should also mention on the old ticket that the follow up ticket is this one.

Cheers,

Michael



---

archive/issue_comments_038665.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-01-24T19:33:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5083#issuecomment-38665",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_038666.json:
```json
{
    "body": "If there really are a lot of options, I would rather see a cmap object so one could do\n\ncmap?\n... lots of documentation ...\n\ncmap.[tab]\n... list of options",
    "created_at": "2009-01-28T00:09:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5083#issuecomment-38666",
    "user": "https://github.com/robertwb"
}
```

If there really are a lot of options, I would rather see a cmap object so one could do

cmap?
... lots of documentation ...

cmap.[tab]
... list of options



---

archive/issue_comments_038667.json:
```json
{
    "body": "This is taken care of in #5601 along with a lot of other color things.  Thanks, Mitesh!\n\nTo release manager: please close this once #5601 is merged, assuming it is.",
    "created_at": "2009-12-10T14:20:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5083#issuecomment-38667",
    "user": "https://github.com/kcrisman"
}
```

This is taken care of in #5601 along with a lot of other color things.  Thanks, Mitesh!

To release manager: please close this once #5601 is merged, assuming it is.



---

archive/issue_events_011722.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5083#event-11722"
}
```



---

archive/issue_events_011723.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5083#event-11723"
}
```



---

archive/issue_events_011724.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5083#event-11724"
}
```



---

archive/issue_events_011725.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5083#event-11725"
}
```



---

archive/issue_events_011726.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5083#event-11726"
}
```



---

archive/issue_events_011727.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5083#event-11727"
}
```



---

archive/issue_events_011728.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5083#event-11728"
}
```



---

archive/issue_comments_038668.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-02-09T16:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5083#issuecomment-38668",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_events_011729.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2016-02-09T16:15:06Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5083#event-11729"
}
```



---

archive/issue_events_011730.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2016-02-09T16:15:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5083#event-11730"
}
```



---

archive/issue_comments_038669.json:
```json
{
    "body": "See comment:6",
    "created_at": "2016-02-09T16:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5083#issuecomment-38669",
    "user": "https://github.com/kcrisman"
}
```

See comment:6



---

archive/issue_comments_038670.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-02-09T16:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5083#issuecomment-38670",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_038671.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-02-23T22:59:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5083#issuecomment-38671",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_011731.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-02-23T22:59:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5083",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5083#event-11731"
}
```
