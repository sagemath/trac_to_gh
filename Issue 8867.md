# Issue 8867: speed up the riemann mapping functionality

archive/issues_008867.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  evanandel @kcrisman\n\nThis patch speeds up the riemann mapping functionality by automatically trying to call fast_callable on the functions passed in.  This depends on #5572 (patch \"improve_fast_callable.patch\")\n\nIssue created by migration from https://trac.sagemath.org/ticket/8867\n\n",
    "created_at": "2010-05-04T04:55:56Z",
    "labels": [
        "calculus",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "speed up the riemann mapping functionality",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8867",
    "user": "@jasongrout"
}
```
Assignee: @burcin

CC:  evanandel @kcrisman

This patch speeds up the riemann mapping functionality by automatically trying to call fast_callable on the functions passed in.  This depends on #5572 (patch "improve_fast_callable.patch")

Issue created by migration from https://trac.sagemath.org/ticket/8867





---

archive/issue_comments_081487.json:
```json
{
    "body": "Attachment [trac-8867-riemann-fastcallable.patch](tarball://root/attachments/some-uuid/ticket8867/trac-8867-riemann-fastcallable.patch) by @jasongrout created at 2010-05-04 05:24:06",
    "created_at": "2010-05-04T05:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81487",
    "user": "@jasongrout"
}
```

Attachment [trac-8867-riemann-fastcallable.patch](tarball://root/attachments/some-uuid/ticket8867/trac-8867-riemann-fastcallable.patch) by @jasongrout created at 2010-05-04 05:24:06



---

archive/issue_comments_081488.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-04T05:24:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81488",
    "user": "@jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_081489.json:
```json
{
    "body": "The doctests are *much* faster now; I hope I didn't introduce any bugs!  The patch isn't finished yet, I don't think.",
    "created_at": "2010-05-04T05:25:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81489",
    "user": "@jasongrout"
}
```

The doctests are *much* faster now; I hope I didn't introduce any bugs!  The patch isn't finished yet, I don't think.



---

archive/issue_comments_081490.json:
```json
{
    "body": "(I don't think I can work on this a lot more, but at least this is a start to making this faster)\n\nThis is very timely---another faculty member was just asking me a few weeks ago about how to use Sage to visualize Riemann mappings.  That's why I thought I'd work on it for a few minutes to speed it up.",
    "created_at": "2010-05-04T05:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81490",
    "user": "@jasongrout"
}
```

(I don't think I can work on this a lot more, but at least this is a start to making this faster)

This is very timely---another faculty member was just asking me a few weeks ago about how to use Sage to visualize Riemann mappings.  That's why I thought I'd work on it for a few minutes to speed it up.



---

archive/issue_comments_081491.json:
```json
{
    "body": "Excellent Jason, thanks. Let me know if there's anything else that would help you guys.",
    "created_at": "2010-05-04T15:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81491",
    "user": "evanandel"
}
```

Excellent Jason, thanks. Let me know if there's anything else that would help you guys.



---

archive/issue_comments_081492.json:
```json
{
    "body": "What is the status of this patch? I'm working on speeding up the Riemann as a whole, and this would be a good component to have. I see that it depends on the main fast_callable patch",
    "created_at": "2010-11-30T17:18:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81492",
    "user": "evanandel"
}
```

What is the status of this patch? I'm working on speeding up the Riemann as a whole, and this would be a good component to have. I see that it depends on the main fast_callable patch



---

archive/issue_comments_081493.json:
```json
{
    "body": "Whoops, changed description on accident, comment should have read:\n\n What is the status of this patch? I'm working on speeding up the Riemann as a whole, and this would be a good component to have. I see that it depends on the main fast_callable patch, do you have any idea when that is expected to finish? \n \nNot at all trying to rush you, just curious for my own purposes if this is coming through soon.",
    "created_at": "2010-11-30T17:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81493",
    "user": "evanandel"
}
```

Whoops, changed description on accident, comment should have read:

 What is the status of this patch? I'm working on speeding up the Riemann as a whole, and this would be a good component to have. I see that it depends on the main fast_callable patch, do you have any idea when that is expected to finish? 
 
Not at all trying to rush you, just curious for my own purposes if this is coming through soon.



---

archive/issue_comments_081494.json:
```json
{
    "body": "No guarantees, but I'd like to finish the fast_callable patch over Christmas break (so before the middle of January).",
    "created_at": "2010-11-30T17:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81494",
    "user": "@jasongrout"
}
```

No guarantees, but I'd like to finish the fast_callable patch over Christmas break (so before the middle of January).



---

archive/issue_comments_081495.json:
```json
{
    "body": "Actually, I just tried applying this patch without #5572 and things seem to work just fine.  You might try testing this patch anyway and reviewing it.",
    "created_at": "2010-12-01T04:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81495",
    "user": "@jasongrout"
}
```

Actually, I just tried applying this patch without #5572 and things seem to work just fine.  You might try testing this patch anyway and reviewing it.



---

archive/issue_comments_081496.json:
```json
{
    "body": "So I don't think this depends on #5572 anymore.",
    "created_at": "2010-12-01T04:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81496",
    "user": "@jasongrout"
}
```

So I don't think this depends on #5572 anymore.



---

archive/issue_comments_081497.json:
```json
{
    "body": "Did all of the tests work for you? The riemann tests go fine, but the interpolators do this:\n\n\n```\nFile \"/home/ethan/sage-4.5.3/devel/sage/sage/calculus/interpolators.pyx\", line 52:\n\n  sage: m = Riemann_Map([lambda x: ps.value(real(x))], [lambda x: ps.derivative(real(x))],0)\n\nException raised:\n\n  Traceback (most recent call last):\n    File \"/home/ethan/sage-4.5.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n      self.run_one_example(test, example, filename, compileflags)\n    File \"/home/ethan/sage-4.5.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n      OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n    File \"/home/ethan/sage-4.5.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n      compileflags, 1) in test.globs\n    File \"<doctest __main__.example_1[7]>\", line 1, in <module>\n      m = Riemann_Map([lambda x: ps.value(real(x))], [lambda x: ps.derivative(real(x))],Integer(0))###line 52:\n  sage: m = Riemann_Map([lambda x: ps.value(real(x))], [lambda x: ps.derivative(real(x))],0)\n    File \"riemann.pyx\", line 164, in sage.calculus.riemann.Riemann_Map.__init__ (sage/calculus/riemann.c:1443) File \"fast_callable.pyx\", line 399, in sage.ext.fast_callable.fast_callable (sage/ext/fast_callable.c:2668)\n  AttributeError: 'function' object has no attribute 'variables'\n```\n\n\nI can solve this by wrapping the fast-callable casts in a try except block, but of course that means that it isn't using them for unusual functions like the interpolators.",
    "created_at": "2010-12-17T19:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81497",
    "user": "evanandel"
}
```

Did all of the tests work for you? The riemann tests go fine, but the interpolators do this:


```
File "/home/ethan/sage-4.5.3/devel/sage/sage/calculus/interpolators.pyx", line 52:

  sage: m = Riemann_Map([lambda x: ps.value(real(x))], [lambda x: ps.derivative(real(x))],0)

Exception raised:

  Traceback (most recent call last):
    File "/home/ethan/sage-4.5.3/local/bin/ncadoctest.py", line 1231, in run_one_test
      self.run_one_example(test, example, filename, compileflags)
    File "/home/ethan/sage-4.5.3/local/bin/sagedoctest.py", line 38, in run_one_example
      OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
    File "/home/ethan/sage-4.5.3/local/bin/ncadoctest.py", line 1172, in run_one_example
      compileflags, 1) in test.globs
    File "<doctest __main__.example_1[7]>", line 1, in <module>
      m = Riemann_Map([lambda x: ps.value(real(x))], [lambda x: ps.derivative(real(x))],Integer(0))###line 52:
  sage: m = Riemann_Map([lambda x: ps.value(real(x))], [lambda x: ps.derivative(real(x))],0)
    File "riemann.pyx", line 164, in sage.calculus.riemann.Riemann_Map.__init__ (sage/calculus/riemann.c:1443) File "fast_callable.pyx", line 399, in sage.ext.fast_callable.fast_callable (sage/ext/fast_callable.c:2668)
  AttributeError: 'function' object has no attribute 'variables'
```


I can solve this by wrapping the fast-callable casts in a try except block, but of course that means that it isn't using them for unusual functions like the interpolators.



---

archive/issue_comments_081498.json:
```json
{
    "body": "fast_callable won't do anything to speed up a lambda function anyway.  It just blindly wraps them in a python call.  So I don't think there's any loss in having a try-except block.",
    "created_at": "2010-12-17T19:34:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81498",
    "user": "@jasongrout"
}
```

fast_callable won't do anything to speed up a lambda function anyway.  It just blindly wraps them in a python call.  So I don't think there's any loss in having a try-except block.



---

archive/issue_comments_081499.json:
```json
{
    "body": "My big patch to fast_callable should also be able to handle the error, but it probably won't be finished or ready for testing for at least another couple of weeks, so if you have time now, don't wait for it.",
    "created_at": "2010-12-17T19:38:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81499",
    "user": "@jasongrout"
}
```

My big patch to fast_callable should also be able to handle the error, but it probably won't be finished or ready for testing for at least another couple of weeks, so if you have time now, don't wait for it.



---

archive/issue_comments_081500.json:
```json
{
    "body": "Updated to dodge lambdas and work with new doctests",
    "created_at": "2011-03-22T03:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81500",
    "user": "evanandel"
}
```

Updated to dodge lambdas and work with new doctests



---

archive/issue_comments_081501.json:
```json
{
    "body": "Attachment [trac-8867-riemann-fastcallable.2.patch](tarball://root/attachments/some-uuid/ticket8867/trac-8867-riemann-fastcallable.2.patch) by evanandel created at 2011-03-22 03:39:51\n\nI've uploaded a new version of the fast_callable patch. It now properly avoids failing with lambda functions, although it doesn't work optimally for them. I'll add some notes on that in\u00a0#10945. It also is updated to work properly with the numpy 1.5.1 version. Therefore tickets\u00a0#10792\u00a0and\u00a0#10821\u00a0should be applied first. I don't think the current patch is dependent on #5572, although I'm sure that faster fast_callables would help.",
    "created_at": "2011-03-22T03:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81501",
    "user": "evanandel"
}
```

Attachment [trac-8867-riemann-fastcallable.2.patch](tarball://root/attachments/some-uuid/ticket8867/trac-8867-riemann-fastcallable.2.patch) by evanandel created at 2011-03-22 03:39:51

I've uploaded a new version of the fast_callable patch. It now properly avoids failing with lambda functions, although it doesn't work optimally for them. I'll add some notes on that in #10945. It also is updated to work properly with the numpy 1.5.1 version. Therefore tickets #10792 and #10821 should be applied first. I don't think the current patch is dependent on #5572, although I'm sure that faster fast_callables would help.



---

archive/issue_comments_081502.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-22T03:39:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81502",
    "user": "evanandel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081503.json:
```json
{
    "body": "This seems to be faster and less buggy than before, although I still have a pretty easy time tripping it up.  For example, the following crescent region causes problems if its not translated as I do below, but even when its translated so that 0 is in the interior the spiderweb plot looks wrong:\n\n\n```\nnpi = N(pi)\ncrescent = [(cos(t)+.9,sin(t)) for t in srange(npi/2,3*npi/2,npi/12)]\ncrescent = crescent + [(5.0*cos(t)/6+.9,sin(t)) for t in srange(3*npi/2,npi/2,-npi/12)]\nps = polygon_spline(crescent) \nf = lambda t: ps.value(real(t)) \nfprime = lambda t: ps.derivative(real(t)) \nm = Riemann_Map([f], [fprime], 0.25, ncorners=24) \nshow(m.plot_colored() + m.plot_spiderweb(pts=100),figsize=[6,6])\n```\n \n\nBut maybe that sort of problem should be in a seperate ticket.",
    "created_at": "2011-04-27T22:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81503",
    "user": "mhampton"
}
```

This seems to be faster and less buggy than before, although I still have a pretty easy time tripping it up.  For example, the following crescent region causes problems if its not translated as I do below, but even when its translated so that 0 is in the interior the spiderweb plot looks wrong:


```
npi = N(pi)
crescent = [(cos(t)+.9,sin(t)) for t in srange(npi/2,3*npi/2,npi/12)]
crescent = crescent + [(5.0*cos(t)/6+.9,sin(t)) for t in srange(3*npi/2,npi/2,-npi/12)]
ps = polygon_spline(crescent) 
f = lambda t: ps.value(real(t)) 
fprime = lambda t: ps.derivative(real(t)) 
m = Riemann_Map([f], [fprime], 0.25, ncorners=24) 
show(m.plot_colored() + m.plot_spiderweb(pts=100),figsize=[6,6])
```
 

But maybe that sort of problem should be in a seperate ticket.



---

archive/issue_comments_081504.json:
```json
{
    "body": "Remove assignee @burcin.",
    "created_at": "2011-04-27T22:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81504",
    "user": "mhampton"
}
```

Remove assignee @burcin.



---

archive/issue_comments_081505.json:
```json
{
    "body": "Yeah, if you think this is good to go (i.e., correct and doesn't make functionality worse), you can give it positive review.  If you can open a ticket with things like this plot and the untranslated one, that would be great.  It sounds like Ethan is working on it a fair amount right now (?), so it would be good to have it on the burner.",
    "created_at": "2011-04-28T02:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81505",
    "user": "@kcrisman"
}
```

Yeah, if you think this is good to go (i.e., correct and doesn't make functionality worse), you can give it positive review.  If you can open a ticket with things like this plot and the untranslated one, that would be great.  It sounds like Ethan is working on it a fair amount right now (?), so it would be good to have it on the burner.



---

archive/issue_comments_081506.json:
```json
{
    "body": "The example given is naturally a problematic one. With the center located outside (a = .25) of the region, it is mathematically nonsensical, thus any output that you get will be bizarre. For the a = 0 case, the spiderweb plot is indeed slightly erratic (caused by the natural inaccuracy of the numerical integration near the boundary). This can be solved by decreasing the linescale parameter. This is documented, but I can see now that it isn't quite clear enough. I'll elaborate as part of the major documentation changes described in #10945.\n\nI'm curious, what were you trying to accomplish by setting ncorners to 24 when this region only has 2? Is this poorly documented?\n\nTo elaborate, none of the behavior seen in this example is incorrect. Let me know if there are any other doc changes I can make to make this easier (I'm working on that already).",
    "created_at": "2011-04-28T03:34:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81506",
    "user": "evanandel"
}
```

The example given is naturally a problematic one. With the center located outside (a = .25) of the region, it is mathematically nonsensical, thus any output that you get will be bizarre. For the a = 0 case, the spiderweb plot is indeed slightly erratic (caused by the natural inaccuracy of the numerical integration near the boundary). This can be solved by decreasing the linescale parameter. This is documented, but I can see now that it isn't quite clear enough. I'll elaborate as part of the major documentation changes described in #10945.

I'm curious, what were you trying to accomplish by setting ncorners to 24 when this region only has 2? Is this poorly documented?

To elaborate, none of the behavior seen in this example is incorrect. Let me know if there are any other doc changes I can make to make this easier (I'm working on that already).



---

archive/issue_comments_081507.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-28T14:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81507",
    "user": "mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081508.json:
```json
{
    "body": "The crescent is a polygon with 24 vertices, so I thought using ncorners=24 would make sense.\n\nTo be honest, I didn't read the documentation very carefully.  This is a good simulation of general users :)  Now that I have, I am happy with the behavior of this function.",
    "created_at": "2011-04-28T14:18:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81508",
    "user": "mhampton"
}
```

The crescent is a polygon with 24 vertices, so I thought using ncorners=24 would make sense.

To be honest, I didn't read the documentation very carefully.  This is a good simulation of general users :)  Now that I have, I am happy with the behavior of this function.



---

archive/issue_comments_081509.json:
```json
{
    "body": "Ah, good point. I'll clarify that in the docs.",
    "created_at": "2011-04-28T14:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81509",
    "user": "evanandel"
}
```

Ah, good point. I'll clarify that in the docs.



---

archive/issue_comments_081510.json:
```json
{
    "body": "Specifically in the major revision I'm working on, not here.",
    "created_at": "2011-04-28T14:42:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81510",
    "user": "evanandel"
}
```

Specifically in the major revision I'm working on, not here.



---

archive/issue_comments_081511.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-31T17:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8867",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8867#issuecomment-81511",
    "user": "@jdemeyer"
}
```

Resolution: fixed
