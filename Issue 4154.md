# Issue 4154: setting defaults for show options

archive/issues_004154.json:
```json
{
    "body": "Assignee: @williamstein\n\nThere ought to be a way to set defaults for the options to show.  Even just a dictionary in sage.plot.plot would be nice.\n\nA use-case would be setting the default aspect ratio to 1 so that if you are plotting lots of circles, it looks okay.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4154\n\n",
    "created_at": "2008-09-19T22:28:23Z",
    "labels": [
        "component: graphics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "setting defaults for show options",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4154",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

There ought to be a way to set defaults for the options to show.  Even just a dictionary in sage.plot.plot would be nice.

A use-case would be setting the default aspect ratio to 1 so that if you are plotting lots of circles, it looks okay.

Issue created by migration from https://trac.sagemath.org/ticket/4154





---

archive/issue_comments_030101.json:
```json
{
    "body": "See #4201 for a nice way to do this.",
    "created_at": "2008-09-26T22:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4154#issuecomment-30101",
    "user": "https://github.com/jasongrout"
}
```

See #4201 for a nice way to do this.



---

archive/issue_comments_030102.json:
```json
{
    "body": "I guess\n\n```\nsage.plot.plot.Graphics.SHOW_OPTIONS[\"aspect_ratio\"] = 1\n```\n\ndoes what was requested in this ticket (although I don't think that it is the best way).\n\nI am switching this ticket to positive review so that release managers can close it appropriately.",
    "created_at": "2010-11-19T02:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4154#issuecomment-30102",
    "user": "https://github.com/novoselt"
}
```

I guess

```
sage.plot.plot.Graphics.SHOW_OPTIONS["aspect_ratio"] = 1
```

does what was requested in this ticket (although I don't think that it is the best way).

I am switching this ticket to positive review so that release managers can close it appropriately.



---

archive/issue_comments_030103.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-11-19T02:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4154#issuecomment-30103",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_030104.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-19T02:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4154#issuecomment-30104",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_030105.json:
```json
{
    "body": "I agree with your assessment.\n\nIf you're interested in reviewing a ticket that deals with setting aspect ratios to more sensible defaults, and clarifying what Sage/Matplotlib means by aspect ratio, #2100 is up for review.",
    "created_at": "2010-11-19T02:50:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4154#issuecomment-30105",
    "user": "https://github.com/jasongrout"
}
```

I agree with your assessment.

If you're interested in reviewing a ticket that deals with setting aspect ratios to more sensible defaults, and clarifying what Sage/Matplotlib means by aspect ratio, #2100 is up for review.



---

archive/issue_comments_030106.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-11-21T08:59:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4154#issuecomment-30106",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_009446.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-21T08:59:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4154",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4154#event-9446"
}
```



---

archive/issue_events_009447.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-21T08:59:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4154",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4154#event-9447"
}
```
