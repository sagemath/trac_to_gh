# Issue 7002: Notebook documentation says to use "#auto", but should be "%auto"

archive/issues_007002.json:
```json
{
    "body": "Assignee: tba\n\nCC:  mvngu kcrisman\n\n#auto was the old way, %auto was the new way.  Plus, we should say % directives need to happen above the input. \n\nTo see the problem, click the \"Help\" in the upper right corner.  The second row is:\n\nAny cells with \"#auto\" in the input is automatically evaluated when the worksheet is first opened.\n\nThis should be changed to:\n\nAny cells with \"%auto\" above the input is automatically evaluated when the worksheet is first opened.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7002\n\n",
    "created_at": "2009-09-23T13:29:00Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "title": "Notebook documentation says to use \"#auto\", but should be \"%auto\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7002",
    "user": "jason"
}
```
Assignee: tba

CC:  mvngu kcrisman

#auto was the old way, %auto was the new way.  Plus, we should say % directives need to happen above the input. 

To see the problem, click the "Help" in the upper right corner.  The second row is:

Any cells with "#auto" in the input is automatically evaluated when the worksheet is first opened.

This should be changed to:

Any cells with "%auto" above the input is automatically evaluated when the worksheet is first opened.

Issue created by migration from https://trac.sagemath.org/ticket/7002





---

archive/issue_comments_057886.json:
```json
{
    "body": "I hate to say this... is a deprecation period in order here?  Or was #auto never the way to do it in the first place?  I have to admit I was always confused by it, which probably led to very few worksheets using it in classes!",
    "created_at": "2009-09-23T15:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57886",
    "user": "kcrisman"
}
```

I hate to say this... is a deprecation period in order here?  Or was #auto never the way to do it in the first place?  I have to admit I was always confused by it, which probably led to very few worksheets using it in classes!



---

archive/issue_comments_057887.json:
```json
{
    "body": "Probably, though I'm not sure how we would do a deprecation, since it is the notebook feature that is deprecated, not something in the Sage process doing the calculations.\n\n\"#auto\" used to be the way to do things before Mike Hansen refactored things (in January or February, I believe).  \n\nWhat I am suggesting is just that the documentation be changed to reflect the new way.  The \"#auto\" still works.  I'd just like to get new people using \"%auto\".",
    "created_at": "2009-09-23T16:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57887",
    "user": "jason"
}
```

Probably, though I'm not sure how we would do a deprecation, since it is the notebook feature that is deprecated, not something in the Sage process doing the calculations.

"#auto" used to be the way to do things before Mike Hansen refactored things (in January or February, I believe).  

What I am suggesting is just that the documentation be changed to reflect the new way.  The "#auto" still works.  I'd just like to get new people using "%auto".



---

archive/issue_comments_057888.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-09-23T16:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57888",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_057889.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> Probably, though I'm not sure how we would do a deprecation, since it is the notebook feature that is deprecated, not something in the Sage process doing the calculations.\n> \n> \"#auto\" used to be the way to do things before Mike Hansen refactored things (in January or February, I believe).  \n> \n> What I am suggesting is just that the documentation be changed to reflect the new way.  The \"#auto\" still works.  I'd just like to get new people using \"%auto\".\n\nOh, if it still works and we aren't getting rid of it, then probably just making the change is okay.  \n\nIncidentally, this doesn't apply cleanly due to someone having added something about HTML above the Shell scripts thingie.  Does this patch depend on something?",
    "created_at": "2009-09-23T16:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57889",
    "user": "kcrisman"
}
```

Replying to [comment:3 jason]:
> Probably, though I'm not sure how we would do a deprecation, since it is the notebook feature that is deprecated, not something in the Sage process doing the calculations.
> 
> "#auto" used to be the way to do things before Mike Hansen refactored things (in January or February, I believe).  
> 
> What I am suggesting is just that the documentation be changed to reflect the new way.  The "#auto" still works.  I'd just like to get new people using "%auto".

Oh, if it still works and we aren't getting rid of it, then probably just making the change is okay.  

Incidentally, this doesn't apply cleanly due to someone having added something about HTML above the Shell scripts thingie.  Does this patch depend on something?



---

archive/issue_comments_057890.json:
```json
{
    "body": "No, it doesn't depend on anything, but it was a patch based on the last version I have on my laptop, so something like 4.1.1 or 4.1.2.alpha1 or something.",
    "created_at": "2009-09-23T16:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57890",
    "user": "jason"
}
```

No, it doesn't depend on anything, but it was a patch based on the last version I have on my laptop, so something like 4.1.1 or 4.1.2.alpha1 or something.



---

archive/issue_comments_057891.json:
```json
{
    "body": "Based on 4.1.2.alpha2",
    "created_at": "2009-09-23T17:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57891",
    "user": "kcrisman"
}
```

Based on 4.1.2.alpha2



---

archive/issue_comments_057892.json:
```json
{
    "body": "Attachment\n\nPositive review, since I just tested that %auto still works (as well as #auto); apply rebase patch only.",
    "created_at": "2009-09-23T17:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57892",
    "user": "kcrisman"
}
```

Attachment

Positive review, since I just tested that %auto still works (as well as #auto); apply rebase patch only.



---

archive/issue_comments_057893.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T07:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57893",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057894.json:
```json
{
    "body": "Merged `trac-7002-autoevaluate-rebase.patch`.",
    "created_at": "2009-09-24T07:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57894",
    "user": "mvngu"
}
```

Merged `trac-7002-autoevaluate-rebase.patch`.



---

archive/issue_comments_057895.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57895",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.



---

archive/issue_comments_057896.json:
```json
{
    "body": "I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.",
    "created_at": "2011-05-30T17:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57896",
    "user": "jason"
}
```

I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.



---

archive/issue_comments_057897.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-05-31T08:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57897",
    "user": "jdemeyer"
}
```

Attachment



---

archive/issue_comments_057898.json:
```json
{
    "body": "Replying to [comment:11 jason]:\n> I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.\n\nCorrect.  Thanks for checking on this also, Jeroen.\n\nI do remember that there is a different ticket open for \"really\" doing this, isn't there?   Unfortunately I just came back on the grid for the first time in a week so I don't have time to search for it.",
    "created_at": "2011-06-01T03:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57898",
    "user": "kcrisman"
}
```

Replying to [comment:11 jason]:
> I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.

Correct.  Thanks for checking on this also, Jeroen.

I do remember that there is a different ticket open for "really" doing this, isn't there?   Unfortunately I just came back on the grid for the first time in a week so I don't have time to search for it.



---

archive/issue_comments_057899.json:
```json
{
    "body": "Replying to [comment:13 kcrisman]:\n> Replying to [comment:11 jason]:\n> > I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.\n> \n> Correct.  Thanks for checking on this also, Jeroen.\n> \n> I do remember that there is a different ticket open for \"really\" doing this, isn't there?   Unfortunately I just came back on the grid for the first time in a week so I don't have time to search for it.\n\nIt's #8956, apparently.  I've requested that one be closed, since the issue is dealt with here.",
    "created_at": "2011-06-20T15:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57899",
    "user": "kcrisman"
}
```

Replying to [comment:13 kcrisman]:
> Replying to [comment:11 jason]:
> > I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.
> 
> Correct.  Thanks for checking on this also, Jeroen.
> 
> I do remember that there is a different ticket open for "really" doing this, isn't there?   Unfortunately I just came back on the grid for the first time in a week so I don't have time to search for it.

It's #8956, apparently.  I've requested that one be closed, since the issue is dealt with here.
