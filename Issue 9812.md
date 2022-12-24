# Issue 9812: parametric plot aspect ratio

archive/issues_009812.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  kcrisman rbeezer\n\nI think parametric_plot should default to having an aspect ratio of 1.  Often we are plotting circles or other objects where we actually want to see the relationship between the two variables.\n\nBesides, it seems like mma does this too.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9813\n\n",
    "created_at": "2010-08-27T01:39:32Z",
    "labels": [
        "graphics",
        "major",
        "enhancement"
    ],
    "title": "parametric plot aspect ratio",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9812",
    "user": "jason"
}
```
Assignee: jason, was

CC:  kcrisman rbeezer

I think parametric_plot should default to having an aspect ratio of 1.  Often we are plotting circles or other objects where we actually want to see the relationship between the two variables.

Besides, it seems like mma does this too.

Issue created by migration from https://trac.sagemath.org/ticket/9813





---

archive/issue_comments_096762.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-08-27T01:39:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96762",
    "user": "jason"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_096763.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-08-27T01:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96763",
    "user": "jason"
}
```

Changing priority from major to minor.



---

archive/issue_comments_096764.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-27T01:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96764",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_096765.json:
```json
{
    "body": "Unfortunately I won't be reviewing much until I switch to wireless, or the semester proves easy... but I would point out that Minh has done some work trying to make sure we are unified in whether it's 2D or 2d or whatever.  I feel like his p.o.v. was 2D.  Look at things like `disk.py` or `circle.py`, where I believe this came into play when I upgraded the docs last year.",
    "created_at": "2010-08-27T02:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96765",
    "user": "kcrisman"
}
```

Unfortunately I won't be reviewing much until I switch to wireless, or the semester proves easy... but I would point out that Minh has done some work trying to make sure we are unified in whether it's 2D or 2d or whatever.  I feel like his p.o.v. was 2D.  Look at things like `disk.py` or `circle.py`, where I believe this came into play when I upgraded the docs last year.



---

archive/issue_comments_096766.json:
```json
{
    "body": "Oh, and I should point out that I expect this patch will work as advertised!  Code and examples seem straightforward.  By the way, somewhere in the developer guide it should say that you need extra lines after plots for them to show up in the live doc - I didn't know that until quite recently, probably courtesy of you.",
    "created_at": "2010-08-27T02:40:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96766",
    "user": "kcrisman"
}
```

Oh, and I should point out that I expect this patch will work as advertised!  Code and examples seem straightforward.  By the way, somewhere in the developer guide it should say that you need extra lines after plots for them to show up in the live doc - I didn't know that until quite recently, probably courtesy of you.



---

archive/issue_comments_096767.json:
```json
{
    "body": "Attachment [trac-9813-parametric-aspect.patch](tarball://root/attachments/some-uuid/ticket9813/trac-9813-parametric-aspect.patch) by jason created at 2010-09-05 03:00:39",
    "created_at": "2010-09-05T03:00:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96767",
    "user": "jason"
}
```

Attachment [trac-9813-parametric-aspect.patch](tarball://root/attachments/some-uuid/ticket9813/trac-9813-parametric-aspect.patch) by jason created at 2010-09-05 03:00:39



---

archive/issue_comments_096768.json:
```json
{
    "body": "tiny reviewer patch",
    "created_at": "2010-09-06T04:23:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96768",
    "user": "ddrake"
}
```

tiny reviewer patch



---

archive/issue_comments_096769.json:
```json
{
    "body": "Attachment [trac_9813_reviewer.patch](tarball://root/attachments/some-uuid/ticket9813/trac_9813_reviewer.patch) by ddrake created at 2010-09-06 04:24:12\n\nLooks good. I've added a little reviewer patch that adds in hyperlinks for the polar_plot docstring.",
    "created_at": "2010-09-06T04:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96769",
    "user": "ddrake"
}
```

Attachment [trac_9813_reviewer.patch](tarball://root/attachments/some-uuid/ticket9813/trac_9813_reviewer.patch) by ddrake created at 2010-09-06 04:24:12

Looks good. I've added a little reviewer patch that adds in hyperlinks for the polar_plot docstring.



---

archive/issue_comments_096770.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-06T04:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96770",
    "user": "ddrake"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096771.json:
```json
{
    "body": "Release manager: apply attachment:trac-9813-parametric-aspect.patch and then attachment:trac_9813_reviewer.patch .",
    "created_at": "2010-09-06T04:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96771",
    "user": "ddrake"
}
```

Release manager: apply attachment:trac-9813-parametric-aspect.patch and then attachment:trac_9813_reviewer.patch .



---

archive/issue_comments_096772.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9812",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9812#issuecomment-96772",
    "user": "mpatel"
}
```

Resolution: fixed
