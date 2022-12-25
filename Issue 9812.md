# Issue 9812: parametric plot  and polar plot aspect ratio

archive/issues_009812.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @kcrisman @rbeezer\n\nKeywords: beginner\n\nI think parametric_plot and polar_plot should default to having an aspect ratio of 1.  Often we are plotting circles or other objects where we actually want to see the relationship between the two variables.\n\nIn my tests, mma also gives an aspect_ratio of 1 for these sorts of plots.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9813\n\n",
    "closed_at": "2010-09-15T10:40:44Z",
    "created_at": "2010-08-27T01:39:32Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "parametric plot  and polar plot aspect ratio",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9812",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  @kcrisman @rbeezer

Keywords: beginner

I think parametric_plot and polar_plot should default to having an aspect ratio of 1.  Often we are plotting circles or other objects where we actually want to see the relationship between the two variables.

In my tests, mma also gives an aspect_ratio of 1 for these sorts of plots.

Issue created by migration from https://trac.sagemath.org/ticket/9813





---

archive/issue_comments_096603.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-08-27T01:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96603",
    "user": "https://github.com/jasongrout"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_096604.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-08-27T01:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96604",
    "user": "https://github.com/jasongrout"
}
```

Changing priority from major to minor.



---

archive/issue_comments_096605.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-27T01:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96605",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096606.json:
```json
{
    "body": "Unfortunately I won't be reviewing much until I switch to wireless, or the semester proves easy... but I would point out that Minh has done some work trying to make sure we are unified in whether it's 2D or 2d or whatever.  I feel like his p.o.v. was 2D.  Look at things like `disk.py` or `circle.py`, where I believe this came into play when I upgraded the docs last year.",
    "created_at": "2010-08-27T02:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96606",
    "user": "https://github.com/kcrisman"
}
```

Unfortunately I won't be reviewing much until I switch to wireless, or the semester proves easy... but I would point out that Minh has done some work trying to make sure we are unified in whether it's 2D or 2d or whatever.  I feel like his p.o.v. was 2D.  Look at things like `disk.py` or `circle.py`, where I believe this came into play when I upgraded the docs last year.



---

archive/issue_comments_096607.json:
```json
{
    "body": "Oh, and I should point out that I expect this patch will work as advertised!  Code and examples seem straightforward.  By the way, somewhere in the developer guide it should say that you need extra lines after plots for them to show up in the live doc - I didn't know that until quite recently, probably courtesy of you.",
    "created_at": "2010-08-27T02:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96607",
    "user": "https://github.com/kcrisman"
}
```

Oh, and I should point out that I expect this patch will work as advertised!  Code and examples seem straightforward.  By the way, somewhere in the developer guide it should say that you need extra lines after plots for them to show up in the live doc - I didn't know that until quite recently, probably courtesy of you.



---

archive/issue_comments_096608.json:
```json
{
    "body": "Attachment [trac-9813-parametric-aspect.patch](tarball://root/attachments/some-uuid/ticket9813/trac-9813-parametric-aspect.patch) by @jasongrout created at 2010-09-05 03:00:39",
    "created_at": "2010-09-05T03:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96608",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9813-parametric-aspect.patch](tarball://root/attachments/some-uuid/ticket9813/trac-9813-parametric-aspect.patch) by @jasongrout created at 2010-09-05 03:00:39



---

archive/issue_comments_096609.json:
```json
{
    "body": "tiny reviewer patch",
    "created_at": "2010-09-06T04:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96609",
    "user": "https://github.com/dandrake"
}
```

tiny reviewer patch



---

archive/issue_comments_096610.json:
```json
{
    "body": "Attachment [trac_9813_reviewer.patch](tarball://root/attachments/some-uuid/ticket9813/trac_9813_reviewer.patch) by @dandrake created at 2010-09-06 04:24:12\n\nLooks good. I've added a little reviewer patch that adds in hyperlinks for the polar_plot docstring.",
    "created_at": "2010-09-06T04:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96610",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_9813_reviewer.patch](tarball://root/attachments/some-uuid/ticket9813/trac_9813_reviewer.patch) by @dandrake created at 2010-09-06 04:24:12

Looks good. I've added a little reviewer patch that adds in hyperlinks for the polar_plot docstring.



---

archive/issue_comments_096611.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-06T04:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96611",
    "user": "https://github.com/dandrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096612.json:
```json
{
    "body": "Release manager: apply attachment:trac-9813-parametric-aspect.patch and then attachment:trac_9813_reviewer.patch .",
    "created_at": "2010-09-06T04:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96612",
    "user": "https://github.com/dandrake"
}
```

Release manager: apply attachment:trac-9813-parametric-aspect.patch and then attachment:trac_9813_reviewer.patch .



---

archive/issue_comments_096613.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96613",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_events_024653.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T10:40:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9812#event-24653"
}
```
