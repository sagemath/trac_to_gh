# Issue 3524: Buildbot

archive/issues_003524.json:
```json
{
    "body": "Assignee: ghtdak\n\nCC:  @mwhansen mvngu drkirkby @nexttime @jdemeyer @kini\n\n[Buildbot](http://buildbot.net/) is a [continuous integration](http://en.wikipedia.org/wiki/Continuous_integration) system for software projects.\n\nLinks:\n\n* [Buildbot manual](http://buildbot.net/buildbot/docs/current/)\n* [Buildbot API reference](http://buildbot.net/buildbot/docs/current/reference/)\n* [Projects using Buildbot](http://buildbot.net/trac/wiki/SuccessStories)\n* [Set up password-protection for the \"Force Build\" and other buttons](http://agile.idyll.org/wiki/BuildbotConfiguration)\n\nAlternatives:\n\n* [Bitten](http://bitten.edgewall.org/)\n* [CDash](http://www.cdash.org/)\n* [Hudson](http://hudson-ci.org/)\n* [others](http://en.wikipedia.org/wiki/Comparison_of_Continuous_Integration_Software)\n\nImportant relevant tickets: #8677, #9433, #9739, #9799, #9811, #9876, #10040.\nWe also need to speed up t2's ATLAS build (cf. #4949, #6705, #9780).\n\nSee [this page](http://boxen.math.washington.edu/buildbots/) for Sage-related Buildbots. [TODO](http://boxen.math.washington.edu/home/buildbot/TODO) for the Sage Buildbot.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3524\n\n",
    "closed_at": "2012-05-21T08:05:39Z",
    "created_at": "2008-06-27T23:58:11Z",
    "labels": [
        "component: build",
        "critical"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Buildbot",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3524",
    "user": "https://trac.sagemath.org/admin/accounts/users/ghtdak"
}
```
Assignee: ghtdak

CC:  @mwhansen mvngu drkirkby @nexttime @jdemeyer @kini

[Buildbot](http://buildbot.net/) is a [continuous integration](http://en.wikipedia.org/wiki/Continuous_integration) system for software projects.

Links:

* [Buildbot manual](http://buildbot.net/buildbot/docs/current/)
* [Buildbot API reference](http://buildbot.net/buildbot/docs/current/reference/)
* [Projects using Buildbot](http://buildbot.net/trac/wiki/SuccessStories)
* [Set up password-protection for the "Force Build" and other buttons](http://agile.idyll.org/wiki/BuildbotConfiguration)

Alternatives:

* [Bitten](http://bitten.edgewall.org/)
* [CDash](http://www.cdash.org/)
* [Hudson](http://hudson-ci.org/)
* [others](http://en.wikipedia.org/wiki/Comparison_of_Continuous_Integration_Software)

Important relevant tickets: #8677, #9433, #9739, #9799, #9811, #9876, #10040.
We also need to speed up t2's ATLAS build (cf. #4949, #6705, #9780).

See [this page](http://boxen.math.washington.edu/buildbots/) for Sage-related Buildbots. [TODO](http://boxen.math.washington.edu/home/buildbot/TODO) for the Sage Buildbot.

Issue created by migration from https://trac.sagemath.org/ticket/3524





---

archive/issue_comments_024783.json:
```json
{
    "body": "I do not think this is sufficiently precise to be a trac ticket.  This should be made into a single precise clear task that somebody volunteers to do or closed as invalid.",
    "created_at": "2008-06-28T12:29:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24783",
    "user": "https://github.com/williamstein"
}
```

I do not think this is sufficiently precise to be a trac ticket.  This should be made into a single precise clear task that somebody volunteers to do or closed as invalid.



---

archive/issue_comments_024784.json:
```json
{
    "body": "Buildbot Implementation Plan\n\n1) Setup Buildbot master and slaves for release testing: Implement shellcommand interfaces to download, build and test candidate tarballs\n\n- includes configuring status delivery via mail / web and irc\n\n2) Integration with Hg: finer grained use of distributed testing through Hg pull\n\n3) Twisted PB integration: Buildbot supports PB and can be used for real-time status\n\n3) Integration with test framework: unittest and doctest",
    "created_at": "2008-06-28T16:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24784",
    "user": "https://trac.sagemath.org/admin/accounts/users/ghtdak"
}
```

Buildbot Implementation Plan

1) Setup Buildbot master and slaves for release testing: Implement shellcommand interfaces to download, build and test candidate tarballs

- includes configuring status delivery via mail / web and irc

2) Integration with Hg: finer grained use of distributed testing through Hg pull

3) Twisted PB integration: Buildbot supports PB and can be used for real-time status

3) Integration with test framework: unittest and doctest



---

archive/issue_comments_024785.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-06-28T17:34:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24785",
    "user": "https://trac.sagemath.org/admin/accounts/users/ghtdak"
}
```

Resolution: invalid



---

archive/issue_events_008040.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/ghtdak",
    "created_at": "2008-06-28T17:34:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3524#event-8040"
}
```



---

archive/issue_comments_024786.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2010-01-30T12:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24786",
    "user": "https://github.com/qed777"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_024787.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-01-30T12:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24787",
    "user": "https://github.com/qed777"
}
```

Changing status from closed to new.



---

archive/issue_events_008041.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-01-30T12:02:11Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3524#event-8041"
}
```



---

archive/issue_comments_024788.json:
```json
{
    "body": "I'm reopening this, because it's important and overdue.  We can discuss possible approaches on sage-devel.",
    "created_at": "2010-01-30T12:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24788",
    "user": "https://github.com/qed777"
}
```

I'm reopening this, because it's important and overdue.  We can discuss possible approaches on sage-devel.



---

archive/issue_comments_024789.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2010-01-30T12:02:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24789",
    "user": "https://github.com/qed777"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_024790.json:
```json
{
    "body": "Changing component from distribution to build.",
    "created_at": "2010-08-30T08:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24790",
    "user": "https://github.com/qed777"
}
```

Changing component from distribution to build.



---

archive/issue_comments_024791.json:
```json
{
    "body": "Can this now be closed, since the buildbot is working? \n\nDave",
    "created_at": "2010-11-11T22:40:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24791",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Can this now be closed, since the buildbot is working? 

Dave



---

archive/issue_comments_024792.json:
```json
{
    "body": "Replying to [comment:15 drkirkby]:\n> Can this now be closed, since the buildbot is working? \n\n\n\"Sounds\" good!",
    "created_at": "2010-11-11T23:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24792",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:15 drkirkby]:
> Can this now be closed, since the buildbot is working? 


"Sounds" good!



---

archive/issue_comments_024793.json:
```json
{
    "body": "What IRC integration would be desirable?",
    "created_at": "2011-10-13T13:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24793",
    "user": "https://github.com/nexttime"
}
```

What IRC integration would be desirable?



---

archive/issue_comments_024794.json:
```json
{
    "body": "Oh, I just wanted to improve sagebot's trac reporting. I also want to do some other stuff with trac tracking, but none of this is related to the buildbot.",
    "created_at": "2011-10-13T13:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24794",
    "user": "https://github.com/kini"
}
```

Oh, I just wanted to improve sagebot's trac reporting. I also want to do some other stuff with trac tracking, but none of this is related to the buildbot.



---

archive/issue_comments_024795.json:
```json
{
    "body": "Replying to [comment:15 drkirkby]:\n> Can this now be closed, since the buildbot is working?\n\n\nIt's working, but not very well.\n\nAnybody has any clue what's wrong with\n\n```\nhttp://build.sagemath.org/sage/builders/Skynet%20download\n```",
    "created_at": "2011-11-02T14:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24795",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:15 drkirkby]:
> Can this now be closed, since the buildbot is working?


It's working, but not very well.

Anybody has any clue what's wrong with

```
http://build.sagemath.org/sage/builders/Skynet%20download
```



---

archive/issue_comments_024796.json:
```json
{
    "body": "I'm putting this to needs review, since the buildbot is clearly already an active part of the release process. If there are things to be improved there should be a new ticket (not this one whose goal was to get something running in the first place).",
    "created_at": "2012-03-15T00:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24796",
    "user": "https://github.com/koffie"
}
```

I'm putting this to needs review, since the buildbot is clearly already an active part of the release process. If there are things to be improved there should be a new ticket (not this one whose goal was to get something running in the first place).



---

archive/issue_comments_024797.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-03-15T00:15:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24797",
    "user": "https://github.com/koffie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_024798.json:
```json
{
    "body": "What is there to review? It seems to me like you are proposing to close this ticket outright, in which case the correct status should be positive_review (so the release manager sees it).",
    "created_at": "2012-05-16T14:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24798",
    "user": "https://github.com/kini"
}
```

What is there to review? It seems to me like you are proposing to close this ticket outright, in which case the correct status should be positive_review (so the release manager sees it).



---

archive/issue_comments_024799.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-16T14:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24799",
    "user": "https://github.com/kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008042.json:
```json
{
    "actor": "https://github.com/kini",
    "created_at": "2012-05-16T14:14:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3524#event-8042"
}
```



---

archive/issue_comments_024800.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-05-21T08:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3524#issuecomment-24800",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_008043.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-05-21T08:05:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3524",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3524#event-8043"
}
```
