# Issue 8632: .save ignores ymin etc.

archive/issues_008632.json:
```json
{
    "body": "Assignee: was\n\nCC:  kcrisman\n\na sage (4.3.3) notebook shows the correct picture of\n\n\n```\nplot(x^2-5,(x,0,5),ymin=0)\n```\n\n\n\nThe save method ignores the ymin parameter:\n\n\n```\nplot(x^2-5,(x,0,5),ymin=0).save(\"/tmp/test.png\")\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8632\n\n",
    "created_at": "2010-03-30T17:12:08Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": ".save ignores ymin etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8632",
    "user": "damm"
}
```
Assignee: was

CC:  kcrisman

a sage (4.3.3) notebook shows the correct picture of


```
plot(x^2-5,(x,0,5),ymin=0)
```



The save method ignores the ymin parameter:


```
plot(x^2-5,(x,0,5),ymin=0).save("/tmp/test.png")
```


Issue created by migration from https://trac.sagemath.org/ticket/8632





---

archive/issue_comments_078272.json:
```json
{
    "body": "See also #7981.",
    "created_at": "2010-11-19T03:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78272",
    "user": "novoselt"
}
```

See also #7981.



---

archive/issue_comments_078273.json:
```json
{
    "body": "With the current patch at #7981 this problem is gone. The graph goes a bit below ymin=0, but it happens in both cases in the same way, so save does not ignore the parameter anymore.",
    "created_at": "2011-01-13T05:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78273",
    "user": "novoselt"
}
```

With the current patch at #7981 this problem is gone. The graph goes a bit below ymin=0, but it happens in both cases in the same way, so save does not ignore the parameter anymore.



---

archive/issue_comments_078274.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-13T05:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78274",
    "user": "novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078275.json:
```json
{
    "body": "Easy review with #7981 applied ;-)",
    "created_at": "2011-01-13T05:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78275",
    "user": "novoselt"
}
```

Easy review with #7981 applied ;-)



---

archive/issue_comments_078276.json:
```json
{
    "body": "Except we need a patch :-)  It could go in the TESTS section; it would need to use the usual temp directory for Sage.",
    "created_at": "2011-01-13T15:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78276",
    "user": "kcrisman"
}
```

Except we need a patch :-)  It could go in the TESTS section; it would need to use the usual temp directory for Sage.



---

archive/issue_comments_078277.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-13T15:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78277",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078278.json:
```json
{
    "body": "Could you please remind me what is the usual temp directory for Sage?\n\nAlso, what exactly should the test do? How do I verify that images from `show` and `save` are the same? It seems like a waste of time on tests if it is only checked that these commands don't raise an exception - they were working before as well, just not as they should.",
    "created_at": "2011-01-13T16:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78278",
    "user": "novoselt"
}
```

Could you please remind me what is the usual temp directory for Sage?

Also, what exactly should the test do? How do I verify that images from `show` and `save` are the same? It seems like a waste of time on tests if it is only checked that these commands don't raise an exception - they were working before as well, just not as they should.



---

archive/issue_comments_078279.json:
```json
{
    "body": "Replying to [comment:5 novoselt]:\n> Could you please remind me what is the usual temp directory for Sage?\nSee line 1732 of your patch for #7981 ;-)  - `kwds.setdefault('filename', sage.misc.misc.tmp_filename() + '.png') `\n> Also, what exactly should the test do? How do I verify that images from `show` and `save` are the same? It seems like a waste of time on tests if it is only checked that these commands don't raise an exception - they were working before as well, just not as they should.\nSadly, we can't do that yet.  (Matplotlib apparently does do this with Nose, but we don't have the capability yet.)   Partly this could be useful for the future day when we CAN check things like this...\n\nBut for now the point is that at least someone can visually verify that there is a different min than $y=-5$ if they care to look.  We want to document that we have done something about the particular one. \n\nAlternately, you could try to ask a release manager to close this as a duplicate of #7981.  Personally, I think it would be worth adding an example to the save documentation that one can choose to either put the commands in `.save(foo=bar)` or to pass it one from `plot(f,foo=bar)`; that could be useful for a complete newbie to the code to see, so that they don't have to follow code around.",
    "created_at": "2011-01-13T17:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78279",
    "user": "kcrisman"
}
```

Replying to [comment:5 novoselt]:
> Could you please remind me what is the usual temp directory for Sage?
See line 1732 of your patch for #7981 ;-)  - `kwds.setdefault('filename', sage.misc.misc.tmp_filename() + '.png') `
> Also, what exactly should the test do? How do I verify that images from `show` and `save` are the same? It seems like a waste of time on tests if it is only checked that these commands don't raise an exception - they were working before as well, just not as they should.
Sadly, we can't do that yet.  (Matplotlib apparently does do this with Nose, but we don't have the capability yet.)   Partly this could be useful for the future day when we CAN check things like this...

But for now the point is that at least someone can visually verify that there is a different min than $y=-5$ if they care to look.  We want to document that we have done something about the particular one. 

Alternately, you could try to ask a release manager to close this as a duplicate of #7981.  Personally, I think it would be worth adding an example to the save documentation that one can choose to either put the commands in `.save(foo=bar)` or to pass it one from `plot(f,foo=bar)`; that could be useful for a complete newbie to the code to see, so that they don't have to follow code around.



---

archive/issue_comments_078280.json:
```json
{
    "body": "Attachment [trac_8632_save_ignores_options_from_plot.patch](tarball://root/attachments/some-uuid/ticket8632/trac_8632_save_ignores_options_from_plot.patch) by novoselt created at 2011-01-13 17:39:10",
    "created_at": "2011-01-13T17:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78280",
    "user": "novoselt"
}
```

Attachment [trac_8632_save_ignores_options_from_plot.patch](tarball://root/attachments/some-uuid/ticket8632/trac_8632_save_ignores_options_from_plot.patch) by novoselt created at 2011-01-13 17:39:10



---

archive/issue_comments_078281.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-13T17:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78281",
    "user": "novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078282.json:
```json
{
    "body": "Thank you! How about this patch?",
    "created_at": "2011-01-13T17:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78282",
    "user": "novoselt"
}
```

Thank you! How about this patch?



---

archive/issue_comments_078283.json:
```json
{
    "body": "I assume the patch depends on #7981, correct?",
    "created_at": "2011-01-13T17:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78283",
    "user": "kcrisman"
}
```

I assume the patch depends on #7981, correct?



---

archive/issue_comments_078284.json:
```json
{
    "body": "Yes!",
    "created_at": "2011-01-13T18:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78284",
    "user": "novoselt"
}
```

Yes!



---

archive/issue_comments_078285.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-14T02:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78285",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078286.json:
```json
{
    "body": "Positive review.  \n\nTo buildbot: depends on #7981, apply trac_8632_save_ignores_options_from_plot.patch",
    "created_at": "2011-01-14T02:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78286",
    "user": "kcrisman"
}
```

Positive review.  

To buildbot: depends on #7981, apply trac_8632_save_ignores_options_from_plot.patch



---

archive/issue_comments_078287.json:
```json
{
    "body": "Scratch that.  Need to change the patch a bit so documentation looks ok - a missing colon.",
    "created_at": "2011-01-14T02:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78287",
    "user": "kcrisman"
}
```

Scratch that.  Need to change the patch a bit so documentation looks ok - a missing colon.



---

archive/issue_comments_078288.json:
```json
{
    "body": "Attachment [trac_8632-reviewer.patch](tarball://root/attachments/some-uuid/ticket8632/trac_8632-reviewer.patch) by kcrisman created at 2011-01-14 02:41:34\n\nreviewer patch",
    "created_at": "2011-01-14T02:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78288",
    "user": "kcrisman"
}
```

Attachment [trac_8632-reviewer.patch](tarball://root/attachments/some-uuid/ticket8632/trac_8632-reviewer.patch) by kcrisman created at 2011-01-14 02:41:34

reviewer patch



---

archive/issue_comments_078289.json:
```json
{
    "body": "Okay, now all is well.  \n\nto buildbot: depends on #7981, apply trac_8632_save_ignores_options_from_plot.patch and trac_8632-reviewer.patch",
    "created_at": "2011-01-14T02:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78289",
    "user": "kcrisman"
}
```

Okay, now all is well.  

to buildbot: depends on #7981, apply trac_8632_save_ignores_options_from_plot.patch and trac_8632-reviewer.patch



---

archive/issue_comments_078290.json:
```json
{
    "body": "Thanks for the corrections, sorry for sloppiness!",
    "created_at": "2011-01-14T03:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78290",
    "user": "novoselt"
}
```

Thanks for the corrections, sorry for sloppiness!



---

archive/issue_comments_078291.json:
```json
{
    "body": "Just FYI - still applies fine on 4.6.2.alpha0.",
    "created_at": "2011-01-15T03:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78291",
    "user": "kcrisman"
}
```

Just FYI - still applies fine on 4.6.2.alpha0.



---

archive/issue_comments_078292.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> Just FYI - still applies fine on 4.6.2.alpha0.\n\nActually, it doesn't:\n\n```\npatching file sage/plot/plot.py\nHunk #1 FAILED at 2394.\n1 out of 1 hunk FAILED -- saving rejects to file sage/plot/plot.py.rej\n```\n",
    "created_at": "2011-01-19T01:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78292",
    "user": "jdemeyer"
}
```

Replying to [comment:14 kcrisman]:
> Just FYI - still applies fine on 4.6.2.alpha0.

Actually, it doesn't:

```
patching file sage/plot/plot.py
Hunk #1 FAILED at 2394.
1 out of 1 hunk FAILED -- saving rejects to file sage/plot/plot.py.rej
```




---

archive/issue_comments_078293.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-19T01:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78293",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_078294.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-19T01:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78294",
    "user": "jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_078295.json:
```json
{
    "body": "Sorry, I missed the dependency on #7981.",
    "created_at": "2011-01-19T01:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78295",
    "user": "jdemeyer"
}
```

Sorry, I missed the dependency on #7981.



---

archive/issue_comments_078296.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78296",
    "user": "jdemeyer"
}
```

Resolution: fixed
