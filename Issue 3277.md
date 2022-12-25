# Issue 3277: context for calculus assumptions

archive/issues_003277.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  @mezzarobba @EmmanuelCharpentier\n\nKeywords: assume\n\none should be able to do something like\n\n```\nwith assumptions(x<0):\n    ...\n```\n\nwhere assume() and forget() would be called on the entering and exiting of the block. This could probably be cleanly done with maxima's contexts. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3277\n\n",
    "closed_at": "2020-08-22T07:10:24Z",
    "created_at": "2008-05-23T08:15:57Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "context for calculus assumptions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3277",
    "user": "https://github.com/robertwb"
}
```
Assignee: @garyfurnish

CC:  @mezzarobba @EmmanuelCharpentier

Keywords: assume

one should be able to do something like

```
with assumptions(x<0):
    ...
```

where assume() and forget() would be called on the entering and exiting of the block. This could probably be cleanly done with maxima's contexts. 

Issue created by migration from https://trac.sagemath.org/ticket/3277





---

archive/issue_comments_022621.json:
```json
{
    "body": "I'm going to implement passing of assumptions into functions, so much of this can be done as an addon to that (with some global assumption list)",
    "created_at": "2008-05-23T19:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22621",
    "user": "https://github.com/garyfurnish"
}
```

I'm going to implement passing of assumptions into functions, so much of this can be done as an addon to that (with some global assumption list)



---

archive/issue_comments_022622.json:
```json
{
    "body": "See also #780 and #1163 for discussions of assumption issues.",
    "created_at": "2009-01-29T16:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22622",
    "user": "https://github.com/kcrisman"
}
```

See also #780 and #1163 for discussions of assumption issues.



---

archive/issue_comments_022623.json:
```json
{
    "body": "See also [this ask.sagemath.org question](http://ask.sagemath.org/question/1154/piecewise-assumptions-for-integration), which would love this.  Note that [Maxima does support contexts](http://maxima.sourceforge.net/docs/manual/en/maxima_11.html#contexts).",
    "created_at": "2012-02-14T14:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22623",
    "user": "https://github.com/kcrisman"
}
```

See also [this ask.sagemath.org question](http://ask.sagemath.org/question/1154/piecewise-assumptions-for-integration), which would love this.  Note that [Maxima does support contexts](http://maxima.sourceforge.net/docs/manual/en/maxima_11.html#contexts).



---

archive/issue_comments_022624.json:
```json
{
    "body": "Changing keywords from \"\" to \"assume\".",
    "created_at": "2012-02-14T14:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22624",
    "user": "https://github.com/kcrisman"
}
```

Changing keywords from "" to "assume".



---

archive/issue_events_007370.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-07-06T00:59:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3277#event-7370"
}
```



---

archive/issue_comments_022625.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-06T00:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22625",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_022626.json:
```json
{
    "body": "This was implemented in #24119. Should be closed as a dup",
    "created_at": "2020-07-06T00:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22626",
    "user": "https://github.com/mkoeppe"
}
```

This was implemented in #24119. Should be closed as a dup



---

archive/issue_comments_022627.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-06T01:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22627",
    "user": "https://github.com/DaveWitteMorris"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_022628.json:
```json
{
    "body": "NO WAY!  Thanks to Emmanuel for that!",
    "created_at": "2020-07-06T11:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22628",
    "user": "https://github.com/kcrisman"
}
```

NO WAY!  Thanks to Emmanuel for that!



---

archive/issue_comments_022629.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> NO WAY!  Thanks to Emmanuel for that!\n\n\nI may be dense but ... What do you mean by \"NO WAY!\" ? Do you think that this ticket should be treated separately from #24119 ?",
    "created_at": "2020-07-06T11:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22629",
    "user": "https://github.com/EmmanuelCharpentier"
}
```

Replying to [comment:7 kcrisman]:
> NO WAY!  Thanks to Emmanuel for that!


I may be dense but ... What do you mean by "NO WAY!" ? Do you think that this ticket should be treated separately from #24119 ?



---

archive/issue_comments_022630.json:
```json
{
    "body": "> > NO WAY!  Thanks to Emmanuel for that!\n\n> \n> I may be dense but ... What do you mean by \"NO WAY!\" ? Do you think that this ticket should be treated separately from #24119 ?\n\n\nSorry, an Americanism - it means, \"I don't believe this amazing thing that has happened!\"  Purely a phrase of thankfulness and surprise.",
    "created_at": "2020-07-10T14:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22630",
    "user": "https://github.com/kcrisman"
}
```

> > NO WAY!  Thanks to Emmanuel for that!

> 
> I may be dense but ... What do you mean by "NO WAY!" ? Do you think that this ticket should be treated separately from #24119 ?


Sorry, an Americanism - it means, "I don't believe this amazing thing that has happened!"  Purely a phrase of thankfulness and surprise.



---

archive/issue_events_007371.json:
```json
{
    "actor": "https://github.com/slel",
    "created_at": "2020-08-22T07:10:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3277#event-7371"
}
```



---

archive/issue_comments_022631.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-08-22T07:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22631",
    "user": "https://github.com/slel"
}
```

Resolution: fixed
