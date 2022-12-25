# Issue 9199: plot(..., fill=False) still turns on filling

archive/issues_009199.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  @kcrisman\n\nTry `plot(x^2,(x,-1,1), fill=False)`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9199\n\n",
    "created_at": "2010-06-10T01:14:40Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "plot(..., fill=False) still turns on filling",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9199",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  @kcrisman

Try `plot(x^2,(x,-1,1), fill=False)`.

Issue created by migration from https://trac.sagemath.org/ticket/9199





---

archive/issue_comments_085903.json:
```json
{
    "body": "Right, because `fill=None` is the current default.  This should be very easy to fix.",
    "created_at": "2010-07-27T17:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85903",
    "user": "https://github.com/kcrisman"
}
```

Right, because `fill=None` is the current default.  This should be very easy to fix.



---

archive/issue_comments_085904.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner\".",
    "created_at": "2010-07-27T17:49:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85904",
    "user": "https://github.com/kcrisman"
}
```

Changing keywords from "" to "beginner".



---

archive/issue_comments_085905.json:
```json
{
    "body": "make \"fill=False\" work.",
    "created_at": "2010-08-03T06:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85905",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

make "fill=False" work.



---

archive/issue_comments_085906.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-03T06:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85906",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_085907.json:
```json
{
    "body": "Attachment [trac_9199_plot_fill.patch](tarball://root/attachments/some-uuid/ticket9199/trac_9199_plot_fill.patch) by ryan created at 2010-08-03 06:34:10\n\nhere is the patch that fixes the fill=False issue.  It breaks fill=None (however, fill=None isn't really that natural).\n\nInteresting issue...when running the doctests for this patch, the doctest timed out and then crashed.\n---------------------------------------\nTrying:\nplot(x**Integer(3),(x,Integer(1),Integer(2))) # this one does not###line\n2276:_sage_ >>> plot(x^3,(x,1,2)) # this one does not\nExpecting nothing\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n[361.7 s]\n--------------------------------------- \nwhen plotting this in sagenb, it works fine.",
    "created_at": "2010-08-03T06:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85907",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_9199_plot_fill.patch](tarball://root/attachments/some-uuid/ticket9199/trac_9199_plot_fill.patch) by ryan created at 2010-08-03 06:34:10

here is the patch that fixes the fill=False issue.  It breaks fill=None (however, fill=None isn't really that natural).

Interesting issue...when running the doctests for this patch, the doctest timed out and then crashed.
---------------------------------------
Trying:
plot(x**Integer(3),(x,Integer(1),Integer(2))) # this one does not###line
2276:_sage_ >>> plot(x^3,(x,1,2)) # this one does not
Expecting nothing
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
[361.7 s]
--------------------------------------- 
when plotting this in sagenb, it works fine.



---

archive/issue_comments_085908.json:
```json
{
    "body": "Oops, here it is with better formatting.\n\n\n```\n---------------------------------------\nTrying:\nplot(x**Integer(3),(x,Integer(1),Integer(2))) # this one does not###line\n2276:_sage_ >>> plot(x^3,(x,1,2)) # this one does not\nExpecting nothing\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n*** *** Error: TIMED OUT! *** ***\n[361.7 s]\n--------------------------------------- \n```\n",
    "created_at": "2010-08-03T06:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85908",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Oops, here it is with better formatting.


```
---------------------------------------
Trying:
plot(x**Integer(3),(x,Integer(1),Integer(2))) # this one does not###line
2276:_sage_ >>> plot(x^3,(x,1,2)) # this one does not
Expecting nothing
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
[361.7 s]
--------------------------------------- 
```




---

archive/issue_comments_085909.json:
```json
{
    "body": "This could come from the change somehow.  \n\nMore important is whether anyone relies somewhere else in the code on fill=None as working.  There should be a way to handle both of these - catch fill=False and then rename fill to None, for instance.  What do you think?",
    "created_at": "2010-08-03T15:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85909",
    "user": "https://github.com/kcrisman"
}
```

This could come from the change somehow.  

More important is whether anyone relies somewhere else in the code on fill=None as working.  There should be a way to handle both of these - catch fill=False and then rename fill to None, for instance.  What do you think?



---

archive/issue_comments_085910.json:
```json
{
    "body": "well...about sage -t.  Every doctest I run crashes (they all time out and then crash at about 360 seconds).  It even crashes with my sage-main branch (which is my clean sage 4.5.1).  It's strange because with my last patch, the doctests work fine.  I'll try undoing the changes and see it changes anything.\n\nAs far as handling fill both False and None, not anything big.\njust need to change \n\n```\nif fill is not False:\n\nto\n\nif fill is not False and fill is not None:\n```\n\n\nI originally had it the second way, but I removed in the hopes that it would fix the doctest crashes (it didn't).\n\nI'll add it back as soon as I get back to my sage computer.",
    "created_at": "2010-08-03T15:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85910",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

well...about sage -t.  Every doctest I run crashes (they all time out and then crash at about 360 seconds).  It even crashes with my sage-main branch (which is my clean sage 4.5.1).  It's strange because with my last patch, the doctests work fine.  I'll try undoing the changes and see it changes anything.

As far as handling fill both False and None, not anything big.
just need to change 

```
if fill is not False:

to

if fill is not False and fill is not None:
```


I originally had it the second way, but I removed in the hopes that it would fix the doctest crashes (it didn't).

I'll add it back as soon as I get back to my sage computer.



---

archive/issue_comments_085911.json:
```json
{
    "body": "Attachment [trac_9199_plot_fill.2.patch](tarball://root/attachments/some-uuid/ticket9199/trac_9199_plot_fill.2.patch) by ryan created at 2010-08-04 21:56:22\n\nupdate: fill=None works too!",
    "created_at": "2010-08-04T21:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85911",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_9199_plot_fill.2.patch](tarball://root/attachments/some-uuid/ticket9199/trac_9199_plot_fill.2.patch) by ryan created at 2010-08-04 21:56:22

update: fill=None works too!



---

archive/issue_comments_085912.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-28T18:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85912",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085913.json:
```json
{
    "body": "How did you get that second patch (i.e., how did you generated whatever you posted as the patch)?  It seems to be two patches concatenated together.  When I apply it, I don't get the \"fill=None works again\" behavior or piece of code.",
    "created_at": "2010-08-29T02:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85913",
    "user": "https://github.com/jasongrout"
}
```

How did you get that second patch (i.e., how did you generated whatever you posted as the patch)?  It seems to be two patches concatenated together.  When I apply it, I don't get the "fill=None works again" behavior or piece of code.



---

archive/issue_comments_085914.json:
```json
{
    "body": "Attachment [trac_9199_plot_fill-rebased.patch](tarball://root/attachments/some-uuid/ticket9199/trac_9199_plot_fill-rebased.patch) by @jasongrout created at 2010-08-29 02:53:15\n\nRebased to 4.5.2; apply only this patch",
    "created_at": "2010-08-29T02:53:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85914",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_9199_plot_fill-rebased.patch](tarball://root/attachments/some-uuid/ticket9199/trac_9199_plot_fill-rebased.patch) by @jasongrout created at 2010-08-29 02:53:15

Rebased to 4.5.2; apply only this patch



---

archive/issue_comments_085915.json:
```json
{
    "body": "I rebased your patch (your patch had the default color to be rgbcolor=(0,0,0) for some reason), and combined your two patches into one patch.  However, when I do:\n\n\n```\nplot(x^2,(x,-1,1), fill=None)\n\n```\n\n\nI get filling (where I didn't before the patch).",
    "created_at": "2010-08-29T02:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85915",
    "user": "https://github.com/jasongrout"
}
```

I rebased your patch (your patch had the default color to be rgbcolor=(0,0,0) for some reason), and combined your two patches into one patch.  However, when I do:


```
plot(x^2,(x,-1,1), fill=None)

```


I get filling (where I didn't before the patch).



---

archive/issue_comments_085916.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-29T02:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85916",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_085917.json:
```json
{
    "body": "Updated patch (with Sage 4.5.3)",
    "created_at": "2010-09-11T05:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85917",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Updated patch (with Sage 4.5.3)



---

archive/issue_comments_085918.json:
```json
{
    "body": "Attachment [trac_9199_plot_fill.3.patch](tarball://root/attachments/some-uuid/ticket9199/trac_9199_plot_fill.3.patch) by ryan created at 2010-09-11 05:22:02\n\nReplying to [comment:8 jason]:\n> I rebased your patch (your patch had the default color to be rgbcolor=(0,0,0) for some reason), and combined your two patches into one patch.  However, when I do:\n> \n> {{{\n> plot(x^2,(x,-1,1), fill=None)\n> \n> }}}\n> \n> I get filling (where I didn't before the patch).\n\nUpdated patch should fix this.",
    "created_at": "2010-09-11T05:22:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85918",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_9199_plot_fill.3.patch](tarball://root/attachments/some-uuid/ticket9199/trac_9199_plot_fill.3.patch) by ryan created at 2010-09-11 05:22:02

Replying to [comment:8 jason]:
> I rebased your patch (your patch had the default color to be rgbcolor=(0,0,0) for some reason), and combined your two patches into one patch.  However, when I do:
> 
> {{{
> plot(x^2,(x,-1,1), fill=None)
> 
> }}}
> 
> I get filling (where I didn't before the patch).

Updated patch should fix this.



---

archive/issue_comments_085919.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-11T05:26:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85919",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_085920.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-11T16:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85920",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085921.json:
```json
{
    "body": "Looks good!  Thanks!\n\nApply only trac_9199_plot_fill.3.patch\n\nKarl-Dieter: if you reviewed this patch too, add your name to the list.",
    "created_at": "2010-09-11T16:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85921",
    "user": "https://github.com/jasongrout"
}
```

Looks good!  Thanks!

Apply only trac_9199_plot_fill.3.patch

Karl-Dieter: if you reviewed this patch too, add your name to the list.



---

archive/issue_comments_085922.json:
```json
{
    "body": "Note that this is Ryan's first contribution (along with #8838 and #7154)",
    "created_at": "2010-09-11T16:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85922",
    "user": "https://github.com/jasongrout"
}
```

Note that this is Ryan's first contribution (along with #8838 and #7154)



---

archive/issue_events_022656.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T10:40:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9199#event-22656"
}
```



---

archive/issue_comments_085923.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T10:40:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9199",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9199#issuecomment-85923",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
