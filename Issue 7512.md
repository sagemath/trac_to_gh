# Issue 7512: plot3d variable ranges should respect the named variable, if there is one

archive/issues_007512.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  wcauchois @robertwb @orlitzky\n\nThis is a somewhat subtle issue if the function is a pure python function (you'd need to analyze the argument names), but maybe a convention is that if variable names are specified, they must match up to argument names in the function, and then they are slotted into the function using a dictionary, so that no matter where in the variable range list the range for x appears, it always is sent to the function as f(x=value).\n\nSee http://sagenb.org/home/jason3/302/\n\nI think that each of these should return the same plot:\n\n```\nsage: var('x,y')\nsage: def f(x,y):\n...      return x*sin(y)\n...\nsage: plot3d(f, (x,0,3),(y,-6,6),viewer='tachyon')\nsage: plot3d(f, (y,-6,6),(x,0,3),viewer='tachyon')\nsage: g(x,y)= x*sin(y)\nsage: plot3d(g, (x,0,3),(y,-6,6),viewer='tachyon')\nsage: plot3d(g, (y,-6,6),(x,0,3),viewer='tachyon')\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7512\n\n",
    "created_at": "2009-11-22T03:49:46Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.8",
    "title": "plot3d variable ranges should respect the named variable, if there is one",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7512",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

CC:  wcauchois @robertwb @orlitzky

This is a somewhat subtle issue if the function is a pure python function (you'd need to analyze the argument names), but maybe a convention is that if variable names are specified, they must match up to argument names in the function, and then they are slotted into the function using a dictionary, so that no matter where in the variable range list the range for x appears, it always is sent to the function as f(x=value).

See http://sagenb.org/home/jason3/302/

I think that each of these should return the same plot:

```
sage: var('x,y')
sage: def f(x,y):
...      return x*sin(y)
...
sage: plot3d(f, (x,0,3),(y,-6,6),viewer='tachyon')
sage: plot3d(f, (y,-6,6),(x,0,3),viewer='tachyon')
sage: g(x,y)= x*sin(y)
sage: plot3d(g, (x,0,3),(y,-6,6),viewer='tachyon')
sage: plot3d(g, (y,-6,6),(x,0,3),viewer='tachyon')
```

Issue created by migration from https://trac.sagemath.org/ticket/7512





---

archive/issue_comments_063466.json:
```json
{
    "body": "Robert and I decided that the fourth plot should be the same as the second, but it is not.  The error is in the fourth plot.  The problem seems to be that in the fourth plot, the g(x,y) is really called as g(x=x_val, y=y_val), but should just be called as g(y_val, x_val) (i.e., not with named variables, but with just positional parameters).",
    "created_at": "2010-01-20T11:12:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63466",
    "user": "https://github.com/jasongrout"
}
```

Robert and I decided that the fourth plot should be the same as the second, but it is not.  The error is in the fourth plot.  The problem seems to be that in the fourth plot, the g(x,y) is really called as g(x=x_val, y=y_val), but should just be called as g(y_val, x_val) (i.e., not with named variables, but with just positional parameters).



---

archive/issue_comments_063467.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-20T13:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63467",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063468.json:
```json
{
    "body": "Attachment [trac-7512-fast_callable-callable_expressions.patch](tarball://root/attachments/some-uuid/ticket7512/trac-7512-fast_callable-callable_expressions.patch) by @jasongrout created at 2010-01-20 13:21:43",
    "created_at": "2010-01-20T13:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63468",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7512-fast_callable-callable_expressions.patch](tarball://root/attachments/some-uuid/ticket7512/trac-7512-fast_callable-callable_expressions.patch) by @jasongrout created at 2010-01-20 13:21:43



---

archive/issue_comments_063469.json:
```json
{
    "body": "We decided that this was just a symptom of a much deeper issue in fast_callable.  The patch fixes the issue in fast_callable.",
    "created_at": "2010-01-20T13:22:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63469",
    "user": "https://github.com/jasongrout"
}
```

We decided that this was just a symptom of a much deeper issue in fast_callable.  The patch fixes the issue in fast_callable.



---

archive/issue_comments_063470.json:
```json
{
    "body": "Applied patch trac-7512-fast_callable-callable_expressions.patch to sage-4.3.2-alpha0 and tried the exact commands below (in that order). I looked for all 4 plots to be the same (as per the ticket description) but only Plot3d No.1 was the same as Plot3d No.3 - AND - Plot3d No.2 was the same as Plot3d No.4. I tried to see if swapping the ranges of x and y, would give me a clue as to what might be going on (refer plot3d No.5 below) but that caused an exception \"ZeroDivisionError: float division\" (at line 954: count = (end-start)/step IN sage/misc/misc.pyc)\n\n```\nsage: var('x,y')                                                                                                                                         \n(x, y)\nsage: def f(x,y):\n....:     return x*sin(y)\n....: \nsage: g(x,y)= x*sin(y)\nsage: \nsage: plot3d(f, (x,0,3),(y,-6,6),viewer='tachyon')\n\nsage: plot3d(f, (y,-6,6),(x,0,3),viewer='tachyon')\n\nsage: plot3d(g, (x,0,3),(y,-6,6),viewer='tachyon')\n\nsage: plot3d(g, (y,-6,6),(x,0,3),viewer='tachyon')\n\nsage: plot3d(f, (x,-6,-6),(y,0,3),viewer='tachyon')  \n```",
    "created_at": "2010-01-31T05:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63470",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Applied patch trac-7512-fast_callable-callable_expressions.patch to sage-4.3.2-alpha0 and tried the exact commands below (in that order). I looked for all 4 plots to be the same (as per the ticket description) but only Plot3d No.1 was the same as Plot3d No.3 - AND - Plot3d No.2 was the same as Plot3d No.4. I tried to see if swapping the ranges of x and y, would give me a clue as to what might be going on (refer plot3d No.5 below) but that caused an exception "ZeroDivisionError: float division" (at line 954: count = (end-start)/step IN sage/misc/misc.pyc)

```
sage: var('x,y')                                                                                                                                         
(x, y)
sage: def f(x,y):
....:     return x*sin(y)
....: 
sage: g(x,y)= x*sin(y)
sage: 
sage: plot3d(f, (x,0,3),(y,-6,6),viewer='tachyon')

sage: plot3d(f, (y,-6,6),(x,0,3),viewer='tachyon')

sage: plot3d(g, (x,0,3),(y,-6,6),viewer='tachyon')

sage: plot3d(g, (y,-6,6),(x,0,3),viewer='tachyon')

sage: plot3d(f, (x,-6,-6),(y,0,3),viewer='tachyon')  
```



---

archive/issue_comments_063471.json:
```json
{
    "body": "rossk: we decided that the four plots shouldn't be equal after all; the first should be the same as the third, and the second should be the same as the fourth.\n\nping to robertwb: if you have time, it'd be great if you could review this too.",
    "created_at": "2010-02-27T10:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63471",
    "user": "https://github.com/jasongrout"
}
```

rossk: we decided that the four plots shouldn't be equal after all; the first should be the same as the third, and the second should be the same as the fourth.

ping to robertwb: if you have time, it'd be great if you could review this too.



---

archive/issue_comments_063472.json:
```json
{
    "body": "Played with some examples and can see that the examples below act like lambda functions now (regardless of variable name or variable order or function format - all plots came out the same as expected). Hope that helps speed up the review (someone will still have to do the code review)\n\n```\nvar('x y v w')\n\ndef f(x,y):\n    return x*sin(y)\n\ng(x,y)=x*sin(y)\n\nplot3d(f, (x,0,3), (y,-6,6), viewer='tachyon')\nplot3d(f, (y,0,3), (x,-6,6), viewer='tachyon')\nplot3d(f, (v,0,3), (w,-6,6), viewer='tachyon')\n\nplot3d(g, (x,0,3), (y,-6,6), viewer='tachyon')\nplot3d(g, (y,0,3), (x,-6,6), viewer='tachyon')\nplot3d(g, (v,0,3), (w,-6,6), viewer='tachyon')\n```",
    "created_at": "2010-02-28T09:47:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63472",
    "user": "https://trac.sagemath.org/admin/accounts/users/rossk"
}
```

Played with some examples and can see that the examples below act like lambda functions now (regardless of variable name or variable order or function format - all plots came out the same as expected). Hope that helps speed up the review (someone will still have to do the code review)

```
var('x y v w')

def f(x,y):
    return x*sin(y)

g(x,y)=x*sin(y)

plot3d(f, (x,0,3), (y,-6,6), viewer='tachyon')
plot3d(f, (y,0,3), (x,-6,6), viewer='tachyon')
plot3d(f, (v,0,3), (w,-6,6), viewer='tachyon')

plot3d(g, (x,0,3), (y,-6,6), viewer='tachyon')
plot3d(g, (y,0,3), (x,-6,6), viewer='tachyon')
plot3d(g, (v,0,3), (w,-6,6), viewer='tachyon')
```



---

archive/issue_comments_063473.json:
```json
{
    "body": "I have two dumb questions.  Not putting \"needs work\" in case someone else decides on the review.\n\n1. Aren't CallableSymbolicExpressions already Expressions?  How does this get into the else? \n\n```\n    if isinstance(x, Expression):\n        et = x\n        vars = et._etb._vars\n    else:\n        from sage.symbolic.callable import is_CallableSymbolicExpression\n        if is_CallableSymbolicExpression(x):\n            vars=x.args()\n```\n\n2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).",
    "created_at": "2010-05-26T18:42:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63473",
    "user": "https://github.com/kcrisman"
}
```

I have two dumb questions.  Not putting "needs work" in case someone else decides on the review.

1. Aren't CallableSymbolicExpressions already Expressions?  How does this get into the else? 

```
    if isinstance(x, Expression):
        et = x
        vars = et._etb._vars
    else:
        from sage.symbolic.callable import is_CallableSymbolicExpression
        if is_CallableSymbolicExpression(x):
            vars=x.args()
```

2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).



---

archive/issue_comments_063474.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n\n\n\n> 2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).\n\n\n\n\n\nWe do allow other variable names in callable expressions:\n\n```\nsage: f(x,y)=a*x+y\nsage: f(1,2)\na + 2\nsage: f(a=2)\n2*x + y\n```\n\n\nI'm also looking at your other points...",
    "created_at": "2010-05-26T18:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63474",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:10 kcrisman]:



> 2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).





We do allow other variable names in callable expressions:

```
sage: f(x,y)=a*x+y
sage: f(1,2)
a + 2
sage: f(a=2)
2*x + y
```


I'm also looking at your other points...



---

archive/issue_comments_063475.json:
```json
{
    "body": "> \n> > 2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).\n  \n> \n> \n> We do allow other variable names in callable expressions:\n> \n> \n> ```\n> sage: f(x,y)=a*x+y\n> sage: f(1,2)\n> a + 2\n> sage: f(a=2)\n> 2*x + y\n> ```\n> \n\n\nI meant that we aren't allowed to use another variable name to substitute for x and y, but rossk's examples indicate you can do this somehow (?) now since the variables are ignored.",
    "created_at": "2010-05-26T18:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63475",
    "user": "https://github.com/kcrisman"
}
```

> 
> > 2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).
  
> 
> 
> We do allow other variable names in callable expressions:
> 
> 
> ```
> sage: f(x,y)=a*x+y
> sage: f(1,2)
> a + 2
> sage: f(a=2)
> 2*x + y
> ```
> 


I meant that we aren't allowed to use another variable name to substitute for x and y, but rossk's examples indicate you can do this somehow (?) now since the variables are ignored.



---

archive/issue_comments_063476.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n\n\n> 2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).\n\n\nI think in retrospect, I agree that this patch does not have the right design decision.  Instead of throwing away the var values, we should make the default be the x.args() (so that someone doesn't need to specify the vars keyword if passing in a CallableSymbolicExpression).",
    "created_at": "2010-05-26T19:07:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63476",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:10 kcrisman]:


> 2. Why did you decide again that 1 and 3 should be different from 2 and 4?  I'm just curious, since this seems VERY counter-intuitive to me, since we go to the trouble of having g(x=1,y=2)==g(y=2,x=1) for callable guys and not allowing other variable names in them (this came up in the PREP workshop from a user question).


I think in retrospect, I agree that this patch does not have the right design decision.  Instead of throwing away the var values, we should make the default be the x.args() (so that someone doesn't need to specify the vars keyword if passing in a CallableSymbolicExpression).



---

archive/issue_comments_063477.json:
```json
{
    "body": "Replying to [comment:10 kcrisman]:\n> I have two dumb questions.  Not putting \"needs work\" in case someone else decides on the review.\n> \n> 1. Aren't CallableSymbolicExpressions already Expressions?  How does this get into the else? \n\n\nThe Expression in the code is different than Symbolic Expressions (instead, they are related to Expression trees, a fast callable construct.",
    "created_at": "2010-05-26T19:09:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63477",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:10 kcrisman]:
> I have two dumb questions.  Not putting "needs work" in case someone else decides on the review.
> 
> 1. Aren't CallableSymbolicExpressions already Expressions?  How does this get into the else? 


The Expression in the code is different than Symbolic Expressions (instead, they are related to Expression trees, a fast callable construct.



---

archive/issue_comments_063478.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-26T19:11:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63478",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063479.json:
```json
{
    "body": "I'm doing quite a bit of work on fast_callable over on #5572.  I think I'll try to take care of this issue (with the different design decision I just mentioned) over there.",
    "created_at": "2010-05-26T19:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63479",
    "user": "https://github.com/jasongrout"
}
```

I'm doing quite a bit of work on fast_callable over on #5572.  I think I'll try to take care of this issue (with the different design decision I just mentioned) over there.



---

archive/issue_comments_063480.json:
```json
{
    "body": "Changing to needs info, pending the decisions and work over on #5572 (i.e., the info needed is: is this ticket obsolete and invalid?)",
    "created_at": "2010-09-07T02:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63480",
    "user": "https://github.com/jasongrout"
}
```

Changing to needs info, pending the decisions and work over on #5572 (i.e., the info needed is: is this ticket obsolete and invalid?)



---

archive/issue_comments_063481.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-09-07T02:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63481",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_events_017806.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17806"
}
```



---

archive/issue_events_017807.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17807"
}
```



---

archive/issue_events_017808.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17808"
}
```



---

archive/issue_events_017809.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17809"
}
```



---

archive/issue_events_017810.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17810"
}
```



---

archive/issue_events_017811.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17811"
}
```



---

archive/issue_events_017812.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17812"
}
```



---

archive/issue_events_017813.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-07-22T00:57:19Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17813"
}
```



---

archive/issue_events_017814.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-07-22T00:57:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-9.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17814"
}
```



---

archive/issue_events_017815.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-08-09T21:07:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-9.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17815"
}
```



---

archive/issue_events_017816.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-08-09T21:07:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-9.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17816"
}
```



---

archive/issue_events_017817.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-12-18T19:53:12Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-9.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17817"
}
```



---

archive/issue_events_017818.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2021-12-18T19:53:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-9.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17818"
}
```



---

archive/issue_comments_063482.json:
```json
{
    "body": "Stalled in `needs_review` or `needs_info`; likely won't make it into Sage 9.5.",
    "created_at": "2021-12-18T19:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7512#issuecomment-63482",
    "user": "https://github.com/mkoeppe"
}
```

Stalled in `needs_review` or `needs_info`; likely won't make it into Sage 9.5.



---

archive/issue_events_017819.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-04-02T17:54:54Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-9.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17819"
}
```



---

archive/issue_events_017820.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-04-02T17:54:54Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-9.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17820"
}
```



---

archive/issue_events_017821.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-08-31T05:25:02Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-9.7",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17821"
}
```



---

archive/issue_events_017822.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2022-08-31T05:25:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7512",
    "milestone": "sage-9.8",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7512#event-17822"
}
```
