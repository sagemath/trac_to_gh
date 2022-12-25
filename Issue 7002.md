# Issue 7002: Notebook documentation says to use "#auto", but should be "%auto"

archive/issues_007002.json:
```json
{
    "body": "Assignee: tba\n\nCC:  mvngu @kcrisman\n\n#auto was the old way, %auto was the new way.  Plus, we should say % directives need to happen above the input. \n\nTo see the problem, click the \"Help\" in the upper right corner.  The second row is:\n\nAny cells with \"#auto\" in the input is automatically evaluated when the worksheet is first opened.\n\nThis should be changed to:\n\nAny cells with \"%auto\" above the input is automatically evaluated when the worksheet is first opened.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7002\n\n",
    "created_at": "2009-09-23T13:29:00Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "Notebook documentation says to use \"#auto\", but should be \"%auto\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7002",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tba

CC:  mvngu @kcrisman

#auto was the old way, %auto was the new way.  Plus, we should say % directives need to happen above the input. 

To see the problem, click the "Help" in the upper right corner.  The second row is:

Any cells with "#auto" in the input is automatically evaluated when the worksheet is first opened.

This should be changed to:

Any cells with "%auto" above the input is automatically evaluated when the worksheet is first opened.

Issue created by migration from https://trac.sagemath.org/ticket/7002





---

archive/issue_comments_057778.json:
```json
{
    "body": "I hate to say this... is a deprecation period in order here?  Or was #auto never the way to do it in the first place?  I have to admit I was always confused by it, which probably led to very few worksheets using it in classes!",
    "created_at": "2009-09-23T15:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57778",
    "user": "https://github.com/kcrisman"
}
```

I hate to say this... is a deprecation period in order here?  Or was #auto never the way to do it in the first place?  I have to admit I was always confused by it, which probably led to very few worksheets using it in classes!



---

archive/issue_comments_057779.json:
```json
{
    "body": "Probably, though I'm not sure how we would do a deprecation, since it is the notebook feature that is deprecated, not something in the Sage process doing the calculations.\n\n\"#auto\" used to be the way to do things before Mike Hansen refactored things (in January or February, I believe).  \n\nWhat I am suggesting is just that the documentation be changed to reflect the new way.  The \"#auto\" still works.  I'd just like to get new people using \"%auto\".",
    "created_at": "2009-09-23T16:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57779",
    "user": "https://github.com/jasongrout"
}
```

Probably, though I'm not sure how we would do a deprecation, since it is the notebook feature that is deprecated, not something in the Sage process doing the calculations.

"#auto" used to be the way to do things before Mike Hansen refactored things (in January or February, I believe).  

What I am suggesting is just that the documentation be changed to reflect the new way.  The "#auto" still works.  I'd just like to get new people using "%auto".



---

archive/issue_comments_057780.json:
```json
{
    "body": "Attachment [trac-7002-autoevaluate.patch](tarball://root/attachments/some-uuid/ticket7002/trac-7002-autoevaluate.patch) by @jasongrout created at 2009-09-23 16:32:25",
    "created_at": "2009-09-23T16:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57780",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7002-autoevaluate.patch](tarball://root/attachments/some-uuid/ticket7002/trac-7002-autoevaluate.patch) by @jasongrout created at 2009-09-23 16:32:25



---

archive/issue_comments_057781.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> Probably, though I'm not sure how we would do a deprecation, since it is the notebook feature that is deprecated, not something in the Sage process doing the calculations.\n> \n> \"#auto\" used to be the way to do things before Mike Hansen refactored things (in January or February, I believe).  \n> \n> What I am suggesting is just that the documentation be changed to reflect the new way.  The \"#auto\" still works.  I'd just like to get new people using \"%auto\".\n\nOh, if it still works and we aren't getting rid of it, then probably just making the change is okay.  \n\nIncidentally, this doesn't apply cleanly due to someone having added something about HTML above the Shell scripts thingie.  Does this patch depend on something?",
    "created_at": "2009-09-23T16:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57781",
    "user": "https://github.com/kcrisman"
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

archive/issue_comments_057782.json:
```json
{
    "body": "No, it doesn't depend on anything, but it was a patch based on the last version I have on my laptop, so something like 4.1.1 or 4.1.2.alpha1 or something.",
    "created_at": "2009-09-23T16:58:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57782",
    "user": "https://github.com/jasongrout"
}
```

No, it doesn't depend on anything, but it was a patch based on the last version I have on my laptop, so something like 4.1.1 or 4.1.2.alpha1 or something.



---

archive/issue_comments_057783.json:
```json
{
    "body": "Based on 4.1.2.alpha2",
    "created_at": "2009-09-23T17:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57783",
    "user": "https://github.com/kcrisman"
}
```

Based on 4.1.2.alpha2



---

archive/issue_comments_057784.json:
```json
{
    "body": "Attachment [trac-7002-autoevaluate-rebase.patch](tarball://root/attachments/some-uuid/ticket7002/trac-7002-autoevaluate-rebase.patch) by @kcrisman created at 2009-09-23 17:49:23\n\nPositive review, since I just tested that %auto still works (as well as #auto); apply rebase patch only.",
    "created_at": "2009-09-23T17:49:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57784",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac-7002-autoevaluate-rebase.patch](tarball://root/attachments/some-uuid/ticket7002/trac-7002-autoevaluate-rebase.patch) by @kcrisman created at 2009-09-23 17:49:23

Positive review, since I just tested that %auto still works (as well as #auto); apply rebase patch only.



---

archive/issue_events_016429.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-24T07:16:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7002#event-16429"
}
```



---

archive/issue_comments_057785.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T07:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57785",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057786.json:
```json
{
    "body": "Merged `trac-7002-autoevaluate-rebase.patch`.",
    "created_at": "2009-09-24T07:16:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57786",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged `trac-7002-autoevaluate-rebase.patch`.



---

archive/issue_comments_057787.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57787",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.



---

archive/issue_comments_057788.json:
```json
{
    "body": "I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.",
    "created_at": "2011-05-30T17:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57788",
    "user": "https://github.com/jasongrout"
}
```

I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.



---

archive/issue_comments_057789.json:
```json
{
    "body": "Attachment [7002_rebase_4.7.patch](tarball://root/attachments/some-uuid/ticket7002/7002_rebase_4.7.patch) by @jdemeyer created at 2011-05-31 08:50:16",
    "created_at": "2011-05-31T08:50:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57789",
    "user": "https://github.com/jdemeyer"
}
```

Attachment [7002_rebase_4.7.patch](tarball://root/attachments/some-uuid/ticket7002/7002_rebase_4.7.patch) by @jdemeyer created at 2011-05-31 08:50:16



---

archive/issue_events_016430.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-31T08:54:13Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7002#event-16430"
}
```



---

archive/issue_comments_057790.json:
```json
{
    "body": "Replying to [comment:11 jason]:\n> I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.\n\nCorrect.  Thanks for checking on this also, Jeroen.\n\nI do remember that there is a different ticket open for \"really\" doing this, isn't there?   Unfortunately I just came back on the grid for the first time in a week so I don't have time to search for it.",
    "created_at": "2011-06-01T03:14:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57790",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:11 jason]:
> I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.

Correct.  Thanks for checking on this also, Jeroen.

I do remember that there is a different ticket open for "really" doing this, isn't there?   Unfortunately I just came back on the grid for the first time in a week so I don't have time to search for it.



---

archive/issue_comments_057791.json:
```json
{
    "body": "Replying to [comment:13 kcrisman]:\n> Replying to [comment:11 jason]:\n> > I just checked the help in 4.6.2 and it appears that these changes do *not* appear in the help text.\n> \n> Correct.  Thanks for checking on this also, Jeroen.\n> \n> I do remember that there is a different ticket open for \"really\" doing this, isn't there?   Unfortunately I just came back on the grid for the first time in a week so I don't have time to search for it.\n\nIt's #8956, apparently.  I've requested that one be closed, since the issue is dealt with here.",
    "created_at": "2011-06-20T15:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7002",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7002#issuecomment-57791",
    "user": "https://github.com/kcrisman"
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
