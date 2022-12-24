# Issue 8803: Bring doctest for plot/axes.py to 100% or remove it

archive/issues_008803.json:
```json
{
    "body": "Assignee: mvngu\n\nBring doctest coverage for plot/axes.py to 100% or remove it (since we now use matplotlib axes directly).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8803\n\n",
    "created_at": "2010-04-28T15:18:52Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "Bring doctest for plot/axes.py to 100% or remove it",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8803",
    "user": "@kcrisman"
}
```
Assignee: mvngu

Bring doctest coverage for plot/axes.py to 100% or remove it (since we now use matplotlib axes directly).

Issue created by migration from https://trac.sagemath.org/ticket/8803





---

archive/issue_comments_080761.json:
```json
{
    "body": "See # 5448; this module has been deprecated since Sage 4.1.2, which was released on October 14, 2009.  It has not yet been one year, nor will it have been when Sage 5.0 is released (let's hope!).  On the other hand, the whole module was essentially internal functions for use in plot functions.  At any rate, there is no point in doing any more doctests for this, even if it \"hurts\" the coverage score.\n\nThoughts?",
    "created_at": "2010-04-29T01:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80761",
    "user": "@kcrisman"
}
```

See # 5448; this module has been deprecated since Sage 4.1.2, which was released on October 14, 2009.  It has not yet been one year, nor will it have been when Sage 5.0 is released (let's hope!).  On the other hand, the whole module was essentially internal functions for use in plot functions.  At any rate, there is no point in doing any more doctests for this, even if it "hurts" the coverage score.

Thoughts?



---

archive/issue_comments_080762.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-04-29T01:03:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80762",
    "user": "@kcrisman"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_080763.json:
```json
{
    "body": "+1 for removing it if it causes any problems.  If it doesn't cause any problems, then we might as well leave it in for the sake of the deprecation policy.\n\nNote that I don't know that anything has ever actually been removed after being deprecated.  For example, the warning that comes when evaluating an expression like (x<sup>2+y</sup>2)(1,2) has been there for well over a year, but still shows no signs of disappearing.",
    "created_at": "2010-05-09T01:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80763",
    "user": "@jasongrout"
}
```

+1 for removing it if it causes any problems.  If it doesn't cause any problems, then we might as well leave it in for the sake of the deprecation policy.

Note that I don't know that anything has ever actually been removed after being deprecated.  For example, the warning that comes when evaluating an expression like (x<sup>2+y</sup>2)(1,2) has been there for well over a year, but still shows no signs of disappearing.



---

archive/issue_comments_080764.json:
```json
{
    "body": "Replying to [comment:2 jason]:\n> Note that I don't know that anything has ever actually been removed after being deprecated.  For example, the warning that comes when evaluating an expression like (x<sup>2+y</sup>2)(1,2) has been there for well over a year, but still shows no signs of disappearing.\n\nWith Sage 5.0 being the next major release, perhaps it's now time to remove any deprecated functions/classes/methods that are over 6 months old. Such removal could happen after Sage 4.4.2 is out next week.",
    "created_at": "2010-05-09T01:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80764",
    "user": "mvngu"
}
```

Replying to [comment:2 jason]:
> Note that I don't know that anything has ever actually been removed after being deprecated.  For example, the warning that comes when evaluating an expression like (x<sup>2+y</sup>2)(1,2) has been there for well over a year, but still shows no signs of disappearing.

With Sage 5.0 being the next major release, perhaps it's now time to remove any deprecated functions/classes/methods that are over 6 months old. Such removal could happen after Sage 4.4.2 is out next week.



---

archive/issue_comments_080765.json:
```json
{
    "body": "I agree that it would be a good time to remove old deprecated code.\n\nSince many of our users are on an academic cycle, maybe we ought to adjust the deprecation schedule so that deprecated things won't be removed during the academic year, but could be removed after the next big release after the later of 6 months or the end of the academic year?",
    "created_at": "2010-05-09T02:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80765",
    "user": "@jasongrout"
}
```

I agree that it would be a good time to remove old deprecated code.

Since many of our users are on an academic cycle, maybe we ought to adjust the deprecation schedule so that deprecated things won't be removed during the academic year, but could be removed after the next big release after the later of 6 months or the end of the academic year?



---

archive/issue_comments_080766.json:
```json
{
    "body": "Oh, I didn't realize it was 6 months - somehow I read on a thread that it was 12 months.  I don't think that axes.py creates any problems other than lowering our sage -coverage score :)  But Sage 5.0 does seem like an allowable time to remove things that have been deprecated for the requisite time.",
    "created_at": "2010-05-10T15:10:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80766",
    "user": "@kcrisman"
}
```

Oh, I didn't realize it was 6 months - somehow I read on a thread that it was 12 months.  I don't think that axes.py creates any problems other than lowering our sage -coverage score :)  But Sage 5.0 does seem like an allowable time to remove things that have been deprecated for the requisite time.



---

archive/issue_comments_080767.json:
```json
{
    "body": "We can really remove this now.",
    "created_at": "2011-02-16T22:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80767",
    "user": "@kcrisman"
}
```

We can really remove this now.



---

archive/issue_comments_080768.json:
```json
{
    "body": "+1 to removing this whenever the developer's guide first allows it.  Just today I saw the file and was temporarily confused before I realized that it is just old cruft that was once useful, but now is not needed.",
    "created_at": "2011-02-17T04:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80768",
    "user": "@jasongrout"
}
```

+1 to removing this whenever the developer's guide first allows it.  Just today I saw the file and was temporarily confused before I realized that it is just old cruft that was once useful, but now is not needed.



---

archive/issue_comments_080769.json:
```json
{
    "body": "Replying to [comment:1 kcrisman]:\n> See # 5448; this module has been deprecated since Sage 4.1.2, which was released on October 14, 2009.  It has not yet been one year, nor will it have been when Sage 5.0 is released (let's hope!).  On the other hand, the whole module was essentially internal functions for use in plot functions.  At any rate, there is no point in doing any more doctests for this, even if it \"hurts\" the coverage score.\n\nThe developer guide certainly was not thinking 18 months, and since this is not some common mistake like `f=4*x; f(3)` there should be no harm in removing it.  Looks like 5.0 isn't coming any time soon, but we should do this.  Patch coming up.",
    "created_at": "2011-02-17T14:18:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80769",
    "user": "@kcrisman"
}
```

Replying to [comment:1 kcrisman]:
> See # 5448; this module has been deprecated since Sage 4.1.2, which was released on October 14, 2009.  It has not yet been one year, nor will it have been when Sage 5.0 is released (let's hope!).  On the other hand, the whole module was essentially internal functions for use in plot functions.  At any rate, there is no point in doing any more doctests for this, even if it "hurts" the coverage score.

The developer guide certainly was not thinking 18 months, and since this is not some common mistake like `f=4*x; f(3)` there should be no harm in removing it.  Looks like 5.0 isn't coming any time soon, but we should do this.  Patch coming up.



---

archive/issue_comments_080770.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-02-17T14:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80770",
    "user": "@kcrisman"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_080771.json:
```json
{
    "body": "Ready for review.  Apply only attachment:trac_8803-remove-axes.patch\n\nJason, if you do this, might as well review #2100 at the same time ;)",
    "created_at": "2011-02-17T14:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80771",
    "user": "@kcrisman"
}
```

Ready for review.  Apply only attachment:trac_8803-remove-axes.patch

Jason, if you do this, might as well review #2100 at the same time ;)



---

archive/issue_comments_080772.json:
```json
{
    "body": "Well, sounds safe to remove it after all this time, and all tests pass on 4.7.rc1\n\nGood to go ! `:-)`\n\nNathann",
    "created_at": "2011-05-02T15:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80772",
    "user": "@nathanncohen"
}
```

Well, sounds safe to remove it after all this time, and all tests pass on 4.7.rc1

Good to go ! `:-)`

Nathann



---

archive/issue_comments_080773.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-05-02T15:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80773",
    "user": "@nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080774.json:
```json
{
    "body": "Thank you!  It's really silly that we hadn't removed it before, given that the deprecation period long since passed and it doesn't change functionality, but it's gratifying to know that it's not just people who use the graphics code all the time who search these tickets :)",
    "created_at": "2011-05-02T16:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80774",
    "user": "@kcrisman"
}
```

Thank you!  It's really silly that we hadn't removed it before, given that the deprecation period long since passed and it doesn't change functionality, but it's gratifying to know that it's not just people who use the graphics code all the time who search these tickets :)



---

archive/issue_comments_080775.json:
```json
{
    "body": "The deprecation has been in place for a LONG time, (over 18 months), and this module does not have any remaining functionality, nor was it ever really very end-user available.  We thought at one point that 5.0 would be in the near future, so we thought that was a good goal for when to remove it, but that was over a year ago.    This should be removed.  Jason?",
    "created_at": "2011-05-03T13:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80775",
    "user": "@kcrisman"
}
```

The deprecation has been in place for a LONG time, (over 18 months), and this module does not have any remaining functionality, nor was it ever really very end-user available.  We thought at one point that 5.0 would be in the near future, so we thought that was a good goal for when to remove it, but that was over a year ago.    This should be removed.  Jason?



---

archive/issue_comments_080776.json:
```json
{
    "body": "Please change the commit message of the patch such there aren't any very long lines.",
    "created_at": "2011-05-15T15:00:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80776",
    "user": "@jdemeyer"
}
```

Please change the commit message of the patch such there aren't any very long lines.



---

archive/issue_comments_080777.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-05-15T15:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80777",
    "user": "@jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_080778.json:
```json
{
    "body": "Attachment [trac_8803-remove-axes.patch](tarball://root/attachments/some-uuid/ticket8803/trac_8803-remove-axes.patch) by @kcrisman created at 2011-05-16 15:37:21\n\nHopefully this will do it.",
    "created_at": "2011-05-16T15:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80778",
    "user": "@kcrisman"
}
```

Attachment [trac_8803-remove-axes.patch](tarball://root/attachments/some-uuid/ticket8803/trac_8803-remove-axes.patch) by @kcrisman created at 2011-05-16 15:37:21

Hopefully this will do it.



---

archive/issue_comments_080779.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-05-16T15:37:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80779",
    "user": "@kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_080780.json:
```json
{
    "body": "Replying to [comment:18 kcrisman]:\n> Hopefully this will do it.  \n\nYep, thanks!",
    "created_at": "2011-05-16T19:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80780",
    "user": "@jdemeyer"
}
```

Replying to [comment:18 kcrisman]:
> Hopefully this will do it.  

Yep, thanks!



---

archive/issue_comments_080781.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-16T19:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8803#issuecomment-80781",
    "user": "@jdemeyer"
}
```

Resolution: fixed
