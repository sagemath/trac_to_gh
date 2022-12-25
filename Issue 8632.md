# Issue 8632: .save ignores ymin etc.

archive/issues_008632.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @kcrisman\n\na sage (4.3.3) notebook shows the correct picture of\n\n\n```\nplot(x^2-5,(x,0,5),ymin=0)\n```\n\n\n\nThe save method ignores the ymin parameter:\n\n\n```\nplot(x^2-5,(x,0,5),ymin=0).save(\"/tmp/test.png\")\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8632\n\n",
    "created_at": "2010-03-30T17:12:08Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": ".save ignores ymin etc.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8632",
    "user": "https://trac.sagemath.org/admin/accounts/users/damm"
}
```
Assignee: @williamstein

CC:  @kcrisman

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

archive/issue_comments_078143.json:
```json
{
    "body": "See also #7981.",
    "created_at": "2010-11-19T03:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78143",
    "user": "https://github.com/novoselt"
}
```

See also #7981.



---

archive/issue_comments_078144.json:
```json
{
    "body": "With the current patch at #7981 this problem is gone. The graph goes a bit below ymin=0, but it happens in both cases in the same way, so save does not ignore the parameter anymore.",
    "created_at": "2011-01-13T05:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78144",
    "user": "https://github.com/novoselt"
}
```

With the current patch at #7981 this problem is gone. The graph goes a bit below ymin=0, but it happens in both cases in the same way, so save does not ignore the parameter anymore.



---

archive/issue_comments_078145.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-13T05:47:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78145",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078146.json:
```json
{
    "body": "Easy review with #7981 applied ;-)",
    "created_at": "2011-01-13T05:52:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78146",
    "user": "https://github.com/novoselt"
}
```

Easy review with #7981 applied ;-)



---

archive/issue_comments_078147.json:
```json
{
    "body": "Except we need a patch :-)  It could go in the TESTS section; it would need to use the usual temp directory for Sage.",
    "created_at": "2011-01-13T15:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78147",
    "user": "https://github.com/kcrisman"
}
```

Except we need a patch :-)  It could go in the TESTS section; it would need to use the usual temp directory for Sage.



---

archive/issue_comments_078148.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-13T15:00:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78148",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078149.json:
```json
{
    "body": "Could you please remind me what is the usual temp directory for Sage?\n\nAlso, what exactly should the test do? How do I verify that images from `show` and `save` are the same? It seems like a waste of time on tests if it is only checked that these commands don't raise an exception - they were working before as well, just not as they should.",
    "created_at": "2011-01-13T16:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78149",
    "user": "https://github.com/novoselt"
}
```

Could you please remind me what is the usual temp directory for Sage?

Also, what exactly should the test do? How do I verify that images from `show` and `save` are the same? It seems like a waste of time on tests if it is only checked that these commands don't raise an exception - they were working before as well, just not as they should.



---

archive/issue_comments_078150.json:
```json
{
    "body": "Replying to [comment:5 novoselt]:\n> Could you please remind me what is the usual temp directory for Sage?\nSee line 1732 of your patch for #7981 ;-)  - `kwds.setdefault('filename', sage.misc.misc.tmp_filename() + '.png') `\n> Also, what exactly should the test do? How do I verify that images from `show` and `save` are the same? It seems like a waste of time on tests if it is only checked that these commands don't raise an exception - they were working before as well, just not as they should.\nSadly, we can't do that yet.  (Matplotlib apparently does do this with Nose, but we don't have the capability yet.)   Partly this could be useful for the future day when we CAN check things like this...\n\nBut for now the point is that at least someone can visually verify that there is a different min than $y=-5$ if they care to look.  We want to document that we have done something about the particular one. \n\nAlternately, you could try to ask a release manager to close this as a duplicate of #7981.  Personally, I think it would be worth adding an example to the save documentation that one can choose to either put the commands in `.save(foo=bar)` or to pass it one from `plot(f,foo=bar)`; that could be useful for a complete newbie to the code to see, so that they don't have to follow code around.",
    "created_at": "2011-01-13T17:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78150",
    "user": "https://github.com/kcrisman"
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

archive/issue_comments_078151.json:
```json
{
    "body": "Attachment [trac_8632_save_ignores_options_from_plot.patch](tarball://root/attachments/some-uuid/ticket8632/trac_8632_save_ignores_options_from_plot.patch) by @novoselt created at 2011-01-13 17:39:10",
    "created_at": "2011-01-13T17:39:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78151",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_8632_save_ignores_options_from_plot.patch](tarball://root/attachments/some-uuid/ticket8632/trac_8632_save_ignores_options_from_plot.patch) by @novoselt created at 2011-01-13 17:39:10



---

archive/issue_comments_078152.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-13T17:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78152",
    "user": "https://github.com/novoselt"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078153.json:
```json
{
    "body": "Thank you! How about this patch?",
    "created_at": "2011-01-13T17:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78153",
    "user": "https://github.com/novoselt"
}
```

Thank you! How about this patch?



---

archive/issue_comments_078154.json:
```json
{
    "body": "I assume the patch depends on #7981, correct?",
    "created_at": "2011-01-13T17:59:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78154",
    "user": "https://github.com/kcrisman"
}
```

I assume the patch depends on #7981, correct?



---

archive/issue_comments_078155.json:
```json
{
    "body": "Yes!",
    "created_at": "2011-01-13T18:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78155",
    "user": "https://github.com/novoselt"
}
```

Yes!



---

archive/issue_comments_078156.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-14T02:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78156",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078157.json:
```json
{
    "body": "Positive review.  \n\nTo buildbot: depends on #7981, apply trac_8632_save_ignores_options_from_plot.patch",
    "created_at": "2011-01-14T02:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78157",
    "user": "https://github.com/kcrisman"
}
```

Positive review.  

To buildbot: depends on #7981, apply trac_8632_save_ignores_options_from_plot.patch



---

archive/issue_comments_078158.json:
```json
{
    "body": "Scratch that.  Need to change the patch a bit so documentation looks ok - a missing colon.",
    "created_at": "2011-01-14T02:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78158",
    "user": "https://github.com/kcrisman"
}
```

Scratch that.  Need to change the patch a bit so documentation looks ok - a missing colon.



---

archive/issue_comments_078159.json:
```json
{
    "body": "Attachment [trac_8632-reviewer.patch](tarball://root/attachments/some-uuid/ticket8632/trac_8632-reviewer.patch) by @kcrisman created at 2011-01-14 02:41:34\n\nreviewer patch",
    "created_at": "2011-01-14T02:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78159",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_8632-reviewer.patch](tarball://root/attachments/some-uuid/ticket8632/trac_8632-reviewer.patch) by @kcrisman created at 2011-01-14 02:41:34

reviewer patch



---

archive/issue_comments_078160.json:
```json
{
    "body": "Okay, now all is well.  \n\nto buildbot: depends on #7981, apply trac_8632_save_ignores_options_from_plot.patch and trac_8632-reviewer.patch",
    "created_at": "2011-01-14T02:42:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78160",
    "user": "https://github.com/kcrisman"
}
```

Okay, now all is well.  

to buildbot: depends on #7981, apply trac_8632_save_ignores_options_from_plot.patch and trac_8632-reviewer.patch



---

archive/issue_comments_078161.json:
```json
{
    "body": "Thanks for the corrections, sorry for sloppiness!",
    "created_at": "2011-01-14T03:21:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78161",
    "user": "https://github.com/novoselt"
}
```

Thanks for the corrections, sorry for sloppiness!



---

archive/issue_comments_078162.json:
```json
{
    "body": "Just FYI - still applies fine on 4.6.2.alpha0.",
    "created_at": "2011-01-15T03:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78162",
    "user": "https://github.com/kcrisman"
}
```

Just FYI - still applies fine on 4.6.2.alpha0.



---

archive/issue_comments_078163.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> Just FYI - still applies fine on 4.6.2.alpha0.\n\nActually, it doesn't:\n\n```\npatching file sage/plot/plot.py\nHunk #1 FAILED at 2394.\n1 out of 1 hunk FAILED -- saving rejects to file sage/plot/plot.py.rej\n```\n",
    "created_at": "2011-01-19T01:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78163",
    "user": "https://github.com/jdemeyer"
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

archive/issue_comments_078164.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2011-01-19T01:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78164",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_078165.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2011-01-19T01:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78165",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_078166.json:
```json
{
    "body": "Sorry, I missed the dependency on #7981.",
    "created_at": "2011-01-19T01:45:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78166",
    "user": "https://github.com/jdemeyer"
}
```

Sorry, I missed the dependency on #7981.



---

archive/issue_comments_078167.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8632#issuecomment-78167",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_008801.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2011-01-25T08:14:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8632",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8632#event-8801"
}
```
