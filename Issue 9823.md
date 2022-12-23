# Issue 9823: desolve_system ignores initial conditions

archive/issues_009823.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  robert.marik\n\nKeywords: calculus, maxima, symbolics\n\ndesolve_system apparently ignores initial conditions.  Notice the identical results in the two calls in the following example.\n\n\n```\nsage: t = var('t')\nsage: epsilon = var('epsilon')\nsage: x1 = function('x1', t)\nsage: x2 = function('x2', t)\nsage: de1 = diff(x1,t) == epsilon\nsage: de2 = diff(x2,t) == -2\nsage: desolve_system([de1, de2], [x1, x2], ivar=t)\n[x1(t) == epsilon*t + x1(0), x2(t) == -2*t + x2(0)]\nsage: desolve_system([de1, de2], [x1, x2], ics=[1,1], ivar=t)\n[x1(t) == epsilon*t + x1(0), x2(t) == -2*t + x2(0)] \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9824\n\n",
    "created_at": "2010-08-27T16:42:45Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "desolve_system ignores initial conditions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9823",
    "user": "rhinton"
}
```
Assignee: burcin

CC:  robert.marik

Keywords: calculus, maxima, symbolics

desolve_system apparently ignores initial conditions.  Notice the identical results in the two calls in the following example.


```
sage: t = var('t')
sage: epsilon = var('epsilon')
sage: x1 = function('x1', t)
sage: x2 = function('x2', t)
sage: de1 = diff(x1,t) == epsilon
sage: de2 = diff(x2,t) == -2
sage: desolve_system([de1, de2], [x1, x2], ivar=t)
[x1(t) == epsilon*t + x1(0), x2(t) == -2*t + x2(0)]
sage: desolve_system([de1, de2], [x1, x2], ics=[1,1], ivar=t)
[x1(t) == epsilon*t + x1(0), x2(t) == -2*t + x2(0)] 
```


Issue created by migration from https://trac.sagemath.org/ticket/9824





---

archive/issue_comments_096885.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-08-29T20:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9823#issuecomment-96885",
    "user": "robert.marik"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_096886.json:
```json
{
    "body": "As I observed from documentation, the ics have to be in the form [x0,x1(x0),x2(x0)]\n\nThe following works.\n\n```\nsage: t = var('t')\nsage: epsilon = var('epsilon')\nsage: x1 = function('x1', t)\nsage: x2 = function('x2', t)\nsage: de1 = diff(x1,t) == epsilon\nsage: de2 = diff(x2,t) == -2\nsage: desolve_system([de1, de2], [x1, x2], ivar=t)\n[x1(t) == epsilon*t + x1(0), x2(t) == -2*t + x2(0)]\nsage: desolve_system([de1, de2], [x1, x2], ics=[0,1,1], ivar=t)\n[x1(t) == epsilon*t + 1, x2(t) == -2*t + 1]\n```\n\n\nO.K. what to do with this?\n\nUpdate documentation to mention this explicitly?\n\nAssume (silently or with a warning) that ivar=0 for initial condition whenever the number of dependent variables equals the number of initial conditions?",
    "created_at": "2010-08-29T20:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9823#issuecomment-96886",
    "user": "robert.marik"
}
```

As I observed from documentation, the ics have to be in the form [x0,x1(x0),x2(x0)]

The following works.

```
sage: t = var('t')
sage: epsilon = var('epsilon')
sage: x1 = function('x1', t)
sage: x2 = function('x2', t)
sage: de1 = diff(x1,t) == epsilon
sage: de2 = diff(x2,t) == -2
sage: desolve_system([de1, de2], [x1, x2], ivar=t)
[x1(t) == epsilon*t + x1(0), x2(t) == -2*t + x2(0)]
sage: desolve_system([de1, de2], [x1, x2], ics=[0,1,1], ivar=t)
[x1(t) == epsilon*t + 1, x2(t) == -2*t + 1]
```


O.K. what to do with this?

Update documentation to mention this explicitly?

Assume (silently or with a warning) that ivar=0 for initial condition whenever the number of dependent variables equals the number of initial conditions?



---

archive/issue_comments_096887.json:
```json
{
    "body": "Thanks for pointing out my mistake!\n\nI think updating the documentation is a great idea.  I think we should raise a ValueError exception if `ics` is incomplete.  Assuming an initial value of 0 is not horrible, but Python and Sage seem to prefer explicit-ness.\n\nReplying to [comment:1 robert.marik]:\n> As I observed from documentation, the ics have to be in the form [x0,x1(x0),x2(x0)]\n> \n> The following works.\n> {{{\n> sage: t = var('t')\n> sage: epsilon = var('epsilon')\n> sage: x1 = function('x1', t)\n> sage: x2 = function('x2', t)\n> sage: de1 = diff(x1,t) == epsilon\n> sage: de2 = diff(x2,t) == -2\n> sage: desolve_system([de1, de2], [x1, x2], ivar=t)\n> [x1(t) == epsilon*t + x1(0), x2(t) == -2*t + x2(0)]\n> sage: desolve_system([de1, de2], [x1, x2], ics=[0,1,1], ivar=t)\n> [x1(t) == epsilon*t + 1, x2(t) == -2*t + 1]\n> }}}\n> \n> O.K. what to do with this?\n> \n> Update documentation to mention this explicitly?\n> \n> Assume (silently or with a warning) that ivar=0 for initial condition whenever the number of dependent variables equals the number of initial conditions?",
    "created_at": "2010-08-31T03:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9823#issuecomment-96887",
    "user": "rhinton"
}
```

Thanks for pointing out my mistake!

I think updating the documentation is a great idea.  I think we should raise a ValueError exception if `ics` is incomplete.  Assuming an initial value of 0 is not horrible, but Python and Sage seem to prefer explicit-ness.

Replying to [comment:1 robert.marik]:
> As I observed from documentation, the ics have to be in the form [x0,x1(x0),x2(x0)]
> 
> The following works.
> {{{
> sage: t = var('t')
> sage: epsilon = var('epsilon')
> sage: x1 = function('x1', t)
> sage: x2 = function('x2', t)
> sage: de1 = diff(x1,t) == epsilon
> sage: de2 = diff(x2,t) == -2
> sage: desolve_system([de1, de2], [x1, x2], ivar=t)
> [x1(t) == epsilon*t + x1(0), x2(t) == -2*t + x2(0)]
> sage: desolve_system([de1, de2], [x1, x2], ics=[0,1,1], ivar=t)
> [x1(t) == epsilon*t + 1, x2(t) == -2*t + 1]
> }}}
> 
> O.K. what to do with this?
> 
> Update documentation to mention this explicitly?
> 
> Assume (silently or with a warning) that ivar=0 for initial condition whenever the number of dependent variables equals the number of initial conditions?



---

archive/issue_comments_096888.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-08-31T03:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9823#issuecomment-96888",
    "user": "rhinton"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_096889.json:
```json
{
    "body": "I agree that we should be explicit here.  There is no obvious default for a diffeq; initial condition of zero is not the same as starting to count at 0 or 1.  Yes, updating the documentation would be great for this.",
    "created_at": "2011-03-14T20:49:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9823#issuecomment-96889",
    "user": "kcrisman"
}
```

I agree that we should be explicit here.  There is no obvious default for a diffeq; initial condition of zero is not the same as starting to count at 0 or 1.  Yes, updating the documentation would be great for this.



---

archive/issue_comments_096890.json:
```json
{
    "body": "Changing keywords from \"calculus, maxima, symbolics\" to \"calculus, maxima, symbolics, beginner\".",
    "created_at": "2011-06-14T15:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9823#issuecomment-96890",
    "user": "kcrisman"
}
```

Changing keywords from "calculus, maxima, symbolics" to "calculus, maxima, symbolics, beginner".



---

archive/issue_comments_096891.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-12-17T12:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9823#issuecomment-96891",
    "user": "captaintrunky"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_096892.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-12-17T12:41:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9823#issuecomment-96892",
    "user": "captaintrunky"
}
```

New commits:



---

archive/issue_comments_096893.json:
```json
{
    "body": "This looks good.  \n\nWhile testing this (it doesn't always work, but only in cases of user error like not specifying each function as also a variable to be solved for (at least, I think that is user error?)), I got the following mysterious error.\n\n```\nsage:         sage: t = var('t')\nsage:         sage: u = var('u')\nsage:         sage: x = function('x', t)\nsage:         sage: y = function('y', t)\nsage:         sage: de1 = diff(x,t) + y - 1 == 0\nsage:         sage: de2 = diff(y,t) - x + u == 0\nsage:         sage: des = [de1,de2]\nsage:         sage: ics = [0,1,-1]\nsage:         sage: vars = [x,y]\nsage:         sage: sol = desolve_system(des, vars, ics, u); sol\nTypeError: ECL says: Error executing code in Maxima: \n```\n\nI get similar errors if Maxima just can't solve the system, but with a *message*.  While it's true that `u` isn't one of the variables differentiated by or of the functions `u`, at least it should give an error message that the system doesn't make sense; this could easily happen as a typo for something that works fine.\n\n```\nsage:         sage: sol = desolve_system(des, vars, ics, t); sol\n[x(t) == -(u - 1)*cos(t) + u + 2*sin(t),\n y(t) == -(u - 1)*sin(t) - 2*cos(t) + 1]\n```\n\nPerhaps for another ticket.",
    "created_at": "2014-12-17T16:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9823#issuecomment-96893",
    "user": "kcrisman"
}
```

This looks good.  

While testing this (it doesn't always work, but only in cases of user error like not specifying each function as also a variable to be solved for (at least, I think that is user error?)), I got the following mysterious error.

```
sage:         sage: t = var('t')
sage:         sage: u = var('u')
sage:         sage: x = function('x', t)
sage:         sage: y = function('y', t)
sage:         sage: de1 = diff(x,t) + y - 1 == 0
sage:         sage: de2 = diff(y,t) - x + u == 0
sage:         sage: des = [de1,de2]
sage:         sage: ics = [0,1,-1]
sage:         sage: vars = [x,y]
sage:         sage: sol = desolve_system(des, vars, ics, u); sol
TypeError: ECL says: Error executing code in Maxima: 
```

I get similar errors if Maxima just can't solve the system, but with a *message*.  While it's true that `u` isn't one of the variables differentiated by or of the functions `u`, at least it should give an error message that the system doesn't make sense; this could easily happen as a typo for something that works fine.

```
sage:         sage: sol = desolve_system(des, vars, ics, t); sol
[x(t) == -(u - 1)*cos(t) + u + 2*sin(t),
 y(t) == -(u - 1)*sin(t) - 2*cos(t) + 1]
```

Perhaps for another ticket.



---

archive/issue_comments_096894.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-17T16:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9823#issuecomment-96894",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_096895.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-12-18T00:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9823#issuecomment-96895",
    "user": "vbraun"
}
```

Resolution: fixed
