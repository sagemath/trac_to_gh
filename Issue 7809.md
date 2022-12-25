# Issue 7809: region_plot does not respect the passed variable order

archive/issues_007809.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe call `region_plot(2/x + 1/y > 1/x * 1/y, (x,-10,10), (y,-10,10))` passes the following function to setup_for_eval_on_grid: `(y, x) |--> -2/x - 1/y + 1/(x*y)`, but passes the variables in the order (x,y).  The problem is the equify function.  This patch simplifies the code in equify to not try to put an ordering on the variables, but to just pass back an expression (not a function).\n\nIn practice, since variables would be substituted by name, I don't think this will make a difference.  But it does make the code cleaner and more correct.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7809\n\n",
    "created_at": "2010-01-01T18:44:22Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "region_plot does not respect the passed variable order",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7809",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

The call `region_plot(2/x + 1/y > 1/x * 1/y, (x,-10,10), (y,-10,10))` passes the following function to setup_for_eval_on_grid: `(y, x) |--> -2/x - 1/y + 1/(x*y)`, but passes the variables in the order (x,y).  The problem is the equify function.  This patch simplifies the code in equify to not try to put an ordering on the variables, but to just pass back an expression (not a function).

In practice, since variables would be substituted by name, I don't think this will make a difference.  But it does make the code cleaner and more correct.

Issue created by migration from https://trac.sagemath.org/ticket/7809





---

archive/issue_comments_067441.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-01T18:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67441",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067442.json:
```json
{
    "body": "Attachment [trac-7809-simplify-equify.patch](tarball://root/attachments/some-uuid/ticket7809/trac-7809-simplify-equify.patch) by @jasongrout created at 2010-01-01 18:55:44",
    "created_at": "2010-01-01T18:55:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67442",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7809-simplify-equify.patch](tarball://root/attachments/some-uuid/ticket7809/trac-7809-simplify-equify.patch) by @jasongrout created at 2010-01-01 18:55:44



---

archive/issue_comments_067443.json:
```json
{
    "body": "Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like\n\n```\nsage: region_plot([y>.3, x>0, x^2+y^2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)\nsage: region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)\n```\n\nAlso, the example in the description fails!  Though, to be fair, it failed before as well - but I figure I should mention it in case it's related to this ticket after all.  Or was the syntax wrong?\n\n```\nsage: region_plot(2/x + 1/y > 1/x * 1/y, (x,-10,10), (y,-10,10))\nTypeError: reduce() of empty sequence with no initial value\n```\n",
    "created_at": "2010-01-04T16:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67443",
    "user": "https://github.com/kcrisman"
}
```

Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like

```
sage: region_plot([y>.3, x>0, x^2+y^2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
sage: region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
```

Also, the example in the description fails!  Though, to be fair, it failed before as well - but I figure I should mention it in case it's related to this ticket after all.  Or was the syntax wrong?

```
sage: region_plot(2/x + 1/y > 1/x * 1/y, (x,-10,10), (y,-10,10))
TypeError: reduce() of empty sequence with no initial value
```




---

archive/issue_comments_067444.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-04T16:11:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67444",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_067445.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like\n> {{{\n> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)\n> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)\n> }}}\n\n\nDoes this actually produce an incorrect plot before the patch?  I'll check, but I'm pretty sure it should work.\n\n\n> Also, the example in the description fails!  Though, to be fair, it failed before as well - but I figure I should mention it in case it's related to this ticket after all.  Or was the syntax wrong?\n> {{{\n> sage: region_plot(2/x + 1/y > 1/x * 1/y, (x,-10,10), (y,-10,10))\n> TypeError: reduce() of empty sequence with no initial value\n> }}}\n\nThis is not related to this ticket.  The error is caused by a bug in fast_callable--see #7810.",
    "created_at": "2010-01-04T16:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67445",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:2 kcrisman]:
> Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like
> {{{
> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> }}}


Does this actually produce an incorrect plot before the patch?  I'll check, but I'm pretty sure it should work.


> Also, the example in the description fails!  Though, to be fair, it failed before as well - but I figure I should mention it in case it's related to this ticket after all.  Or was the syntax wrong?
> {{{
> sage: region_plot(2/x + 1/y > 1/x * 1/y, (x,-10,10), (y,-10,10))
> TypeError: reduce() of empty sequence with no initial value
> }}}

This is not related to this ticket.  The error is caused by a bug in fast_callable--see #7810.



---

archive/issue_comments_067446.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> Replying to [comment:2 kcrisman]:\n> > Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like\n> > {{{\n> > sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)\n> > sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)\n> > }}}\n> \n> \n> Does this actually produce an incorrect plot before the patch?  I'll check, but I'm pretty sure it should work.\n> \n\nI didn't bother to check, but it seems like this was the concern, or?  At any rate there should be something documented that didn't work before and now does.  Otherwise I don't quite get why we are removing the potential for passing in the variables here.",
    "created_at": "2010-01-04T16:19:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67446",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:3 jason]:
> Replying to [comment:2 kcrisman]:
> > Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like
> > {{{
> > sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> > sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> > }}}
> 
> 
> Does this actually produce an incorrect plot before the patch?  I'll check, but I'm pretty sure it should work.
> 

I didn't bother to check, but it seems like this was the concern, or?  At any rate there should be something documented that didn't work before and now does.  Otherwise I don't quite get why we are removing the potential for passing in the variables here.



---

archive/issue_comments_067447.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like\n> {{{\n> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)\n> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)\n> }}}\n\nActually, the second example above produces the wrong image even after the patch is applied!",
    "created_at": "2010-01-04T16:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67447",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:2 kcrisman]:
> Looks like this is the only place equify is used, so I think this does not require any deprecation for the removed optional argument.  There should be another doctest in to show this works, though, like
> {{{
> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (x,-1.1, 1.1), (y,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> sage: region_plot([y>.3, x>0, x<sup>2+y</sup>2<1], (y,-1.1, 1.1), (x,-1.1, 1.1), plot_points = 400).show(aspect_ratio=1)
> }}}

Actually, the second example above produces the wrong image even after the patch is applied!



---

archive/issue_comments_067448.json:
```json
{
    "body": "Are you sure?  Are we always putting x on the horizontal axis?  This seems okay to me.",
    "created_at": "2010-01-04T16:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67448",
    "user": "https://github.com/kcrisman"
}
```

Are you sure?  Are we always putting x on the horizontal axis?  This seems okay to me.



---

archive/issue_comments_067449.json:
```json
{
    "body": "no, x shouldn't be on the horizontal axis always.  The first variable specified should be on the horizontal axis.  That would then be consistent.",
    "created_at": "2010-01-04T16:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67449",
    "user": "https://github.com/jasongrout"
}
```

no, x shouldn't be on the horizontal axis always.  The first variable specified should be on the horizontal axis.  That would then be consistent.



---

archive/issue_comments_067450.json:
```json
{
    "body": "Right, and in the second plot the first variable is on the horizontal axis - see attached graphic.   By the way, note the one-pixel issue still - aargh!  I wonder what the heck is causing that.",
    "created_at": "2010-01-04T16:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67450",
    "user": "https://github.com/kcrisman"
}
```

Right, and in the second plot the first variable is on the horizontal axis - see attached graphic.   By the way, note the one-pixel issue still - aargh!  I wonder what the heck is causing that.



---

archive/issue_comments_067451.json:
```json
{
    "body": "Attachment [plot.png](tarball://root/attachments/some-uuid/ticket7809/plot.png) by @jasongrout created at 2010-01-04 17:31:38\n\nOh, you're right.  It is correct.\n\nWell, I just rewrote the mangle_neg part anyway.  I'll attach a patch in a second.",
    "created_at": "2010-01-04T17:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67451",
    "user": "https://github.com/jasongrout"
}
```

Attachment [plot.png](tarball://root/attachments/some-uuid/ticket7809/plot.png) by @jasongrout created at 2010-01-04 17:31:38

Oh, you're right.  It is correct.

Well, I just rewrote the mangle_neg part anyway.  I'll attach a patch in a second.



---

archive/issue_comments_067452.json:
```json
{
    "body": "Before the simplify-negative-code:\n\n\n```\nsage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1)).show(aspect_ratio=1)\nCPU times: user 1.96 s, sys: 0.08 s, total: 2.04 s\nWall time: 2.38 s\nsage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1),plot_points=400).show(aspect_ratio=1)\nCPU times: user 5.92 s, sys: 0.08 s, total: 5.99 s\nWall time: 6.30 s\n```\n\n\nAfter:\n\n\n```\nsage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1)).show(aspect_ratio=1)\nCPU times: user 1.27 s, sys: 0.02 s, total: 1.29 s\nWall time: 1.36 s\nsage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1),plot_points=400).show(aspect_ratio=1)\nCPU times: user 2.49 s, sys: 0.04 s, total: 2.53 s\nWall time: 2.67 s\n```\n",
    "created_at": "2010-01-04T18:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67452",
    "user": "https://github.com/jasongrout"
}
```

Before the simplify-negative-code:


```
sage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1)).show(aspect_ratio=1)
CPU times: user 1.96 s, sys: 0.08 s, total: 2.04 s
Wall time: 2.38 s
sage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1),plot_points=400).show(aspect_ratio=1)
CPU times: user 5.92 s, sys: 0.08 s, total: 5.99 s
Wall time: 6.30 s
```


After:


```
sage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1)).show(aspect_ratio=1)
CPU times: user 1.27 s, sys: 0.02 s, total: 1.29 s
Wall time: 1.36 s
sage: %time region_plot([y>.3, x>0, x^2+y^2<1], (y,-1.1, 1.1), (x,-.5, 1.1),plot_points=400).show(aspect_ratio=1)
CPU times: user 2.49 s, sys: 0.04 s, total: 2.53 s
Wall time: 2.67 s
```




---

archive/issue_comments_067453.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2010-01-04T18:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67453",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_067454.json:
```json
{
    "body": "Attachment [trac-7809-simplify-negative-code.patch](tarball://root/attachments/some-uuid/ticket7809/trac-7809-simplify-negative-code.patch) by @kcrisman created at 2010-01-04 18:52:04\n\nToo bad about mangle_neg, but it was almost more confusing that way than in the code, I think you are right.  \n\nBe sure to include some test where the order of coordinates is switched.  Incidentally, you should also remove the #long time flag from that one test; it only takes one second on my machine, which I don't think counts as a long time any more.  The file takes nearly a half minute to test for me, though!\n\nOther than that, positive review.",
    "created_at": "2010-01-04T18:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67454",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac-7809-simplify-negative-code.patch](tarball://root/attachments/some-uuid/ticket7809/trac-7809-simplify-negative-code.patch) by @kcrisman created at 2010-01-04 18:52:04

Too bad about mangle_neg, but it was almost more confusing that way than in the code, I think you are right.  

Be sure to include some test where the order of coordinates is switched.  Incidentally, you should also remove the #long time flag from that one test; it only takes one second on my machine, which I don't think counts as a long time any more.  The file takes nearly a half minute to test for me, though!

Other than that, positive review.



---

archive/issue_comments_067455.json:
```json
{
    "body": "Replying to [comment:11 kcrisman]:\n\n> Be sure to include some test where the order of coordinates is switched. \n\nThe old code gave the correct result too, I think.  I consider this patch more a refactoring of code.  The error that I corrected didn't show up because I think we were more careful in another part of the code.\n\nJason",
    "created_at": "2010-01-04T19:11:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67455",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:11 kcrisman]:

> Be sure to include some test where the order of coordinates is switched. 

The old code gave the correct result too, I think.  I consider this patch more a refactoring of code.  The error that I corrected didn't show up because I think we were more careful in another part of the code.

Jason



---

archive/issue_comments_067456.json:
```json
{
    "body": "Attachment [trac-7809-variable-order.patch](tarball://root/attachments/some-uuid/ticket7809/trac-7809-variable-order.patch) by @jasongrout created at 2010-01-04 19:19:05\n\napply on top of previous patch",
    "created_at": "2010-01-04T19:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67456",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7809-variable-order.patch](tarball://root/attachments/some-uuid/ticket7809/trac-7809-variable-order.patch) by @jasongrout created at 2010-01-04 19:19:05

apply on top of previous patch



---

archive/issue_comments_067457.json:
```json
{
    "body": "Okay, I made the changes you requested to the doctests and attached a patch.  Can you mark this as positively reviewed?",
    "created_at": "2010-01-04T19:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67457",
    "user": "https://github.com/jasongrout"
}
```

Okay, I made the changes you requested to the doctests and attached a patch.  Can you mark this as positively reviewed?



---

archive/issue_comments_067458.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-04T19:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67458",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067459.json:
```json
{
    "body": "Looks good.  The use of s and t is good because then it's not so clear to the user from convention which one \"should\" be horizontal.  Positive review; apply in the order simplify-equify, simplify-negative-code, variable-order.",
    "created_at": "2010-01-04T19:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67459",
    "user": "https://github.com/kcrisman"
}
```

Looks good.  The use of s and t is good because then it's not so clear to the user from convention which one "should" be horizontal.  Positive review; apply in the order simplify-equify, simplify-negative-code, variable-order.



---

archive/issue_comments_067460.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-04T19:25:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67460",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067461.json:
```json
{
    "body": "This ticket also fixes #5885, so that should be closed when this is.\n\n(the deprecation warning is now printed).",
    "created_at": "2010-01-09T05:35:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67461",
    "user": "https://github.com/jasongrout"
}
```

This ticket also fixes #5885, so that should be closed when this is.

(the deprecation warning is now printed).



---

archive/issue_events_008023.json:
```json
{
    "actor": "@rlmill",
    "created_at": "2010-01-13T11:24:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7809#event-8023"
}
```



---

archive/issue_comments_067462.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T11:24:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7809",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7809#issuecomment-67462",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
