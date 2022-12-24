# Issue 3277: context for calculus assumptions

archive/issues_003277.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  @mezzarobba @EmmanuelCharpentier\n\none should be able to do something like\n\n```\nwith assumptions(x<0):\n    ...\n```\n\n\nwhere assume() and forget() would be called on the entering and exiting of the block. This could probably be cleanly done with maxima's contexts. \n\nIssue created by migration from https://trac.sagemath.org/ticket/3277\n\n",
    "created_at": "2008-05-23T08:15:57Z",
    "labels": [
        "calculus",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "context for calculus assumptions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3277",
    "user": "@robertwb"
}
```
Assignee: @garyfurnish

CC:  @mezzarobba @EmmanuelCharpentier

one should be able to do something like

```
with assumptions(x<0):
    ...
```


where assume() and forget() would be called on the entering and exiting of the block. This could probably be cleanly done with maxima's contexts. 

Issue created by migration from https://trac.sagemath.org/ticket/3277





---

archive/issue_comments_022668.json:
```json
{
    "body": "I'm going to implement passing of assumptions into functions, so much of this can be done as an addon to that (with some global assumption list)",
    "created_at": "2008-05-23T19:41:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22668",
    "user": "@garyfurnish"
}
```

I'm going to implement passing of assumptions into functions, so much of this can be done as an addon to that (with some global assumption list)



---

archive/issue_comments_022669.json:
```json
{
    "body": "See also #780 and #1163 for discussions of assumption issues.",
    "created_at": "2009-01-29T16:42:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22669",
    "user": "@kcrisman"
}
```

See also #780 and #1163 for discussions of assumption issues.



---

archive/issue_comments_022670.json:
```json
{
    "body": "See also [this ask.sagemath.org question](http://ask.sagemath.org/question/1154/piecewise-assumptions-for-integration), which would love this.  Note that [Maxima does support contexts](http://maxima.sourceforge.net/docs/manual/en/maxima_11.html#contexts).",
    "created_at": "2012-02-14T14:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22670",
    "user": "@kcrisman"
}
```

See also [this ask.sagemath.org question](http://ask.sagemath.org/question/1154/piecewise-assumptions-for-integration), which would love this.  Note that [Maxima does support contexts](http://maxima.sourceforge.net/docs/manual/en/maxima_11.html#contexts).



---

archive/issue_comments_022671.json:
```json
{
    "body": "Changing keywords from \"\" to \"assume\".",
    "created_at": "2012-02-14T14:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22671",
    "user": "@kcrisman"
}
```

Changing keywords from "" to "assume".



---

archive/issue_comments_022672.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-06T00:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22672",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_022673.json:
```json
{
    "body": "This was implemented in #24119. Should be closed as a dup",
    "created_at": "2020-07-06T00:59:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22673",
    "user": "@mkoeppe"
}
```

This was implemented in #24119. Should be closed as a dup



---

archive/issue_comments_022674.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-06T01:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22674",
    "user": "@DaveWitteMorris"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_022675.json:
```json
{
    "body": "NO WAY!  Thanks to Emmanuel for that!",
    "created_at": "2020-07-06T11:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22675",
    "user": "@kcrisman"
}
```

NO WAY!  Thanks to Emmanuel for that!



---

archive/issue_comments_022676.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> NO WAY!  Thanks to Emmanuel for that!\n\nI may be dense but ... What do you mean by \"NO WAY!\" ? Do you think that this ticket should be treated separately from #24119 ?",
    "created_at": "2020-07-06T11:46:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22676",
    "user": "@EmmanuelCharpentier"
}
```

Replying to [comment:7 kcrisman]:
> NO WAY!  Thanks to Emmanuel for that!

I may be dense but ... What do you mean by "NO WAY!" ? Do you think that this ticket should be treated separately from #24119 ?



---

archive/issue_comments_022677.json:
```json
{
    "body": "> > NO WAY!  Thanks to Emmanuel for that!\n> \n> I may be dense but ... What do you mean by \"NO WAY!\" ? Do you think that this ticket should be treated separately from #24119 ?\n\nSorry, an Americanism - it means, \"I don't believe this amazing thing that has happened!\"  Purely a phrase of thankfulness and surprise.",
    "created_at": "2020-07-10T14:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22677",
    "user": "@kcrisman"
}
```

> > NO WAY!  Thanks to Emmanuel for that!
> 
> I may be dense but ... What do you mean by "NO WAY!" ? Do you think that this ticket should be treated separately from #24119 ?

Sorry, an Americanism - it means, "I don't believe this amazing thing that has happened!"  Purely a phrase of thankfulness and surprise.



---

archive/issue_comments_022678.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2020-08-22T07:10:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3277#issuecomment-22678",
    "user": "@slel"
}
```

Resolution: fixed
