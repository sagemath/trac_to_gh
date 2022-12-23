# Issue 2452: heaviside step function needed

archive/issues_002452.json:
```json
{
    "body": "Assignee: was\n\nCC:  gmhossain\n\nSymbolic heaviside step function is needed for ease of plotting.  Right now you must \n\n\n```\nsage: def u(x):\n    if(x<0):\n        return 0\n    else:\n        return 1*cos(x)\nsage: plot(u,-5,5)\n```\n\ninstead of\n\n```\n plot(heaviside(t)*cos(t),t,-5,5)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2452\n\n",
    "created_at": "2008-03-10T07:52:27Z",
    "labels": [
        "calculus",
        "critical",
        "enhancement"
    ],
    "title": "heaviside step function needed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2452",
    "user": "gfurnish"
}
```
Assignee: was

CC:  gmhossain

Symbolic heaviside step function is needed for ease of plotting.  Right now you must 


```
sage: def u(x):
    if(x<0):
        return 0
    else:
        return 1*cos(x)
sage: plot(u,-5,5)
```

instead of

```
 plot(heaviside(t)*cos(t),t,-5,5)
```


Issue created by migration from https://trac.sagemath.org/ticket/2452





---

archive/issue_comments_016575.json:
```json
{
    "body": "You can make a Heaviside function with Piecewise. \nsage: f0 = lambda x: 0; f1 = lambda x:x^0; Heaviside = Piecewise([[(-infinity,0),f0],[(0,infinity),f1]])\nsage: Heaviside(3)\n1\nsage: Heaviside(-23)\n0\nHowever, plotting is broken. You have to make a truncated function to plot:\nsage: f0 = lambda x: 0; f1 = lambda x:x^0; Heaviside = Piecewise([[(-10,0),f0],[(0,10),f1]])\nsage: Heaviside.plot()\nworks.\nOf course, improvements to Piecewise would be great...",
    "created_at": "2008-03-10T11:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16575",
    "user": "wdj"
}
```

You can make a Heaviside function with Piecewise. 
sage: f0 = lambda x: 0; f1 = lambda x:x^0; Heaviside = Piecewise([[(-infinity,0),f0],[(0,infinity),f1]])
sage: Heaviside(3)
1
sage: Heaviside(-23)
0
However, plotting is broken. You have to make a truncated function to plot:
sage: f0 = lambda x: 0; f1 = lambda x:x^0; Heaviside = Piecewise([[(-10,0),f0],[(0,10),f1]])
sage: Heaviside.plot()
works.
Of course, improvements to Piecewise would be great...



---

archive/issue_comments_016576.json:
```json
{
    "body": "Changing assignee from was to gfurnish.",
    "created_at": "2008-03-16T20:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16576",
    "user": "gfurnish"
}
```

Changing assignee from was to gfurnish.



---

archive/issue_comments_016577.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-16T20:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16577",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_016578.json:
```json
{
    "body": "What is the status of this?  I noticed something else when trying to do a diffeq lesson:\n\n\n```\nsage: def unit_step(c):\n....:         return piecewise( [( (-oo,c), 0), ((c, oo), 1)] )\n....:\nsage: unit_step(2)\nPiecewise defined function with 2 parts, [((-Infinity, 2), 0), ((2, +Infinity), 1)]\nsage: unit_step(2)*unit_step(3)\nPiecewise defined function with 3 parts, [[(2, 3), 0], [(3, -Infinity), 0], [(-Infinity, +Infinity), 1]]\n```\n\n\nThat last multiplication just plain does not make sense.  Even the intervals are all messed up.",
    "created_at": "2008-10-21T16:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16578",
    "user": "jason"
}
```

What is the status of this?  I noticed something else when trying to do a diffeq lesson:


```
sage: def unit_step(c):
....:         return piecewise( [( (-oo,c), 0), ((c, oo), 1)] )
....:
sage: unit_step(2)
Piecewise defined function with 2 parts, [((-Infinity, 2), 0), ((2, +Infinity), 1)]
sage: unit_step(2)*unit_step(3)
Piecewise defined function with 3 parts, [[(2, 3), 0], [(3, -Infinity), 0], [(-Infinity, +Infinity), 1]]
```


That last multiplication just plain does not make sense.  Even the intervals are all messed up.



---

archive/issue_comments_016579.json:
```json
{
    "body": "This might explain the problem:\n\n\n```\nsage: def unit_step(c):\n    return piecewise( [( (-Infinity,c), 0), ((c, Infinity), 1)] )\n....:\nsage: unit_step(1)\nPiecewise defined function with 2 parts, [((-Infinity, 1), 0), ((1, +Infinity), 1)]\nsage: unit_step(1)(1/2)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/wdj/sagefiles/sage-3.2.alpha0/<ipython console> in <module>()\n\n/home/wdj/sagefiles/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/functions/piecewise.pyc in __call__(self, x0)\n    591         for i in range(n):\n    592             if endpts[i] < x0 < endpts[i+1]:\n--> 593                 return self.functions()[i](x0)\n    594         raise ValueError,\"Value not defined outside of domain.\"\n    595\n\nTypeError: 'sage.rings.integer.Integer' object is not callable\n```\n",
    "created_at": "2008-10-21T17:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16579",
    "user": "wdj"
}
```

This might explain the problem:


```
sage: def unit_step(c):
    return piecewise( [( (-Infinity,c), 0), ((c, Infinity), 1)] )
....:
sage: unit_step(1)
Piecewise defined function with 2 parts, [((-Infinity, 1), 0), ((1, +Infinity), 1)]
sage: unit_step(1)(1/2)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/wdj/sagefiles/sage-3.2.alpha0/<ipython console> in <module>()

/home/wdj/sagefiles/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/functions/piecewise.pyc in __call__(self, x0)
    591         for i in range(n):
    592             if endpts[i] < x0 < endpts[i+1]:
--> 593                 return self.functions()[i](x0)
    594         raise ValueError,"Value not defined outside of domain."
    595

TypeError: 'sage.rings.integer.Integer' object is not callable
```




---

archive/issue_comments_016580.json:
```json
{
    "body": "Descriptions/title are updated and a patch (sage-4.0.2) implementing Dirac delta, Heaviside step and Unit step function is attached.",
    "created_at": "2009-06-28T11:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16580",
    "user": "gmhossain"
}
```

Descriptions/title are updated and a patch (sage-4.0.2) implementing Dirac delta, Heaviside step and Unit step function is attached.



---

archive/issue_comments_016581.json:
```json
{
    "body": "Changing component from calculus to symbolics.",
    "created_at": "2009-06-28T11:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16581",
    "user": "gmhossain"
}
```

Changing component from calculus to symbolics.



---

archive/issue_comments_016582.json:
```json
{
    "body": "Patch applies to 3.1.alpha1. Running tests now.\n\nOne possible problem: Is\n\n\n```\nsage: dirac_delta.integral(0)\nheaviside(0)\n```\n\nmathematically correct?",
    "created_at": "2009-06-28T11:53:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16582",
    "user": "wdj"
}
```

Patch applies to 3.1.alpha1. Running tests now.

One possible problem: Is


```
sage: dirac_delta.integral(0)
heaviside(0)
```

mathematically correct?



---

archive/issue_comments_016583.json:
```json
{
    "body": "Replying to [comment:7 wdj]:\n> Is\n> \n\n```\nsage: dirac_delta.integral(0)\nheaviside(0)\n```\n\n> mathematically correct?\n> \n\nThanks, its a good point. I agree, it is ambiguous at best. I guess, it may be a good \nidea to remove .integral() methods from their definitions. Specialized integration \nalgorithm involving these functions will handle the situation much better.\nI will wait for your remaining comments before updating the patch.",
    "created_at": "2009-06-28T12:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16583",
    "user": "gmhossain"
}
```

Replying to [comment:7 wdj]:
> Is
> 

```
sage: dirac_delta.integral(0)
heaviside(0)
```

> mathematically correct?
> 

Thanks, its a good point. I agree, it is ambiguous at best. I guess, it may be a good 
idea to remove .integral() methods from their definitions. Specialized integration 
algorithm involving these functions will handle the situation much better.
I will wait for your remaining comments before updating the patch.



---

archive/issue_comments_016584.json:
```json
{
    "body": "The testing didn't reveal any failures related to the patch. However, I'm also wondering about\nthis output:\n\n\n```\nsage: f(x) = heaviside(x)+dirac_delta(x)\nsage: f(1)\ndirac_delta(1) + heaviside(1)\nsage: f = heaviside+dirac_delta\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/wdj/.sage/temp/hera/14949/_home_wdj__sage_init_sage_0.py in <module>()\n\nTypeError: unsupported operand type(s) for +: 'FunctionHeaviside' and 'FunctionDiracDelta'\n```\n\neven though it has no problem evaluating them:\n\n\n```\nsage: heaviside(1); dirac_delta(1)\n1\n0\n```\n\n\nI don't see a problem with the integral methods but I'd prefer definite integrals over indefinite ones.\nIn any case, \n\n\n```\nsage: dirac_delta.integral(0)\nheaviside(0)\n```\n\nseems odd. \n\nIf you can address these comments I'd be happy to look at it again.",
    "created_at": "2009-06-28T17:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16584",
    "user": "wdj"
}
```

The testing didn't reveal any failures related to the patch. However, I'm also wondering about
this output:


```
sage: f(x) = heaviside(x)+dirac_delta(x)
sage: f(1)
dirac_delta(1) + heaviside(1)
sage: f = heaviside+dirac_delta
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/wdj/.sage/temp/hera/14949/_home_wdj__sage_init_sage_0.py in <module>()

TypeError: unsupported operand type(s) for +: 'FunctionHeaviside' and 'FunctionDiracDelta'
```

even though it has no problem evaluating them:


```
sage: heaviside(1); dirac_delta(1)
1
0
```


I don't see a problem with the integral methods but I'd prefer definite integrals over indefinite ones.
In any case, 


```
sage: dirac_delta.integral(0)
heaviside(0)
```

seems odd. 

If you can address these comments I'd be happy to look at it again.



---

archive/issue_comments_016585.json:
```json
{
    "body": "Thanks David,\n\n> The testing didn't reveal any failures related to the patch. However, I'm also wondering about\n> this output:\n\n```\nsage: f(x) = heaviside(x)+dirac_delta(x)\nsage: f(1)\ndirac_delta(1) + heaviside(1)\n```\n\n\nIt seems, you have hit a bug in new symbolics. The similar non-evaluation\nof symbolic function is happening even with other functions such as sin, cos. \nI posted this issue here\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/3936d1290ee933a6\n\nBurcin wrote that this is a bug and it is to be fixed in the new version of pynac.\n\n>\n\n```\nsage: f = heaviside+dirac_delta\n...\nTypeError\n```\n\n>\nIt seems in new symbolics, arithmetic of bare-bone functions is no-longer allowed. \nFor example, if I try\n\n```\nf = sin + cos \n```\n\nthen I get the same error. \n\n> I don't see a problem with the integral methods but I'd prefer definite integrals over indefinite ones.\n> In any case,  \n\n```\nsage: dirac_delta.integral(0)\nheaviside(0)\n```\n\n> seems odd. \n\nI agree this is odd. I have removed the integral methods from this patch. Integration algorithm\nthat I am implementing will do both definite and indefinite integrals involving these functions.\nSo I guess, it is better to avoid code-duplication.\n\nApart from above, I have clarified two sentences in doc-strings. The updated patch is attached.",
    "created_at": "2009-06-29T14:45:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16585",
    "user": "gmhossain"
}
```

Thanks David,

> The testing didn't reveal any failures related to the patch. However, I'm also wondering about
> this output:

```
sage: f(x) = heaviside(x)+dirac_delta(x)
sage: f(1)
dirac_delta(1) + heaviside(1)
```


It seems, you have hit a bug in new symbolics. The similar non-evaluation
of symbolic function is happening even with other functions such as sin, cos. 
I posted this issue here

http://groups.google.com/group/sage-devel/browse_thread/thread/3936d1290ee933a6

Burcin wrote that this is a bug and it is to be fixed in the new version of pynac.

>

```
sage: f = heaviside+dirac_delta
...
TypeError
```

>
It seems in new symbolics, arithmetic of bare-bone functions is no-longer allowed. 
For example, if I try

```
f = sin + cos 
```

then I get the same error. 

> I don't see a problem with the integral methods but I'd prefer definite integrals over indefinite ones.
> In any case,  

```
sage: dirac_delta.integral(0)
heaviside(0)
```

> seems odd. 

I agree this is odd. I have removed the integral methods from this patch. Integration algorithm
that I am implementing will do both definite and indefinite integrals involving these functions.
So I guess, it is better to avoid code-duplication.

Apart from above, I have clarified two sentences in doc-strings. The updated patch is attached.



---

archive/issue_comments_016586.json:
```json
{
    "body": "Changing priority from critical to major.",
    "created_at": "2009-06-29T17:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16586",
    "user": "burcin"
}
```

Changing priority from critical to major.



---

archive/issue_comments_016587.json:
```json
{
    "body": "Replying to [comment:11 gmhossain]:\n> > The testing didn't reveal any failures related to the patch. However, I'm also wondering about\n> > this output:\n {{{\n sage: f(x) = heaviside(x)+dirac_delta(x)\n sage: f(1)\n dirac_delta(1) + heaviside(1)\n }}}\n> \n> It seems, you have hit a bug in new symbolics. The similar non-evaluation\n> of symbolic function is happening even with other functions such as sin, cos. \n> I posted this issue here\n> \n> http://groups.google.com/group/sage-devel/browse_thread/thread/3936d1290ee933a6\n> \n> Burcin wrote that this is a bug and it is to be fixed in the new version of pynac.\n\nThis is a different issue than the one you posted on sage-devel. \n\nIn your patch, you are not telling pynac how to evaluate the function you define. This is done by defining an `_eval_` method, so if you move the contents of your `__call__` function to `_eval_` and remove the last `SFunction.__call__` line things should work fine. I agree that this is confusing. It's one of the main points I wanted to address while refactoring symbolic functions.\n\nI would also like to see a `.sub()` test added, since this is the easiest way to test if the `_eval_` function is defined properly. E.g.,\n\n\n```\nsage: dirac_delta(x).sub(x=1)\n0\nsage: heaviside(x).sub(x=1)\n1\n```\n",
    "created_at": "2009-06-29T17:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16587",
    "user": "burcin"
}
```

Replying to [comment:11 gmhossain]:
> > The testing didn't reveal any failures related to the patch. However, I'm also wondering about
> > this output:
 {{{
 sage: f(x) = heaviside(x)+dirac_delta(x)
 sage: f(1)
 dirac_delta(1) + heaviside(1)
 }}}
> 
> It seems, you have hit a bug in new symbolics. The similar non-evaluation
> of symbolic function is happening even with other functions such as sin, cos. 
> I posted this issue here
> 
> http://groups.google.com/group/sage-devel/browse_thread/thread/3936d1290ee933a6
> 
> Burcin wrote that this is a bug and it is to be fixed in the new version of pynac.

This is a different issue than the one you posted on sage-devel. 

In your patch, you are not telling pynac how to evaluate the function you define. This is done by defining an `_eval_` method, so if you move the contents of your `__call__` function to `_eval_` and remove the last `SFunction.__call__` line things should work fine. I agree that this is confusing. It's one of the main points I wanted to address while refactoring symbolic functions.

I would also like to see a `.sub()` test added, since this is the easiest way to test if the `_eval_` function is defined properly. E.g.,


```
sage: dirac_delta(x).sub(x=1)
0
sage: heaviside(x).sub(x=1)
1
```




---

archive/issue_comments_016588.json:
```json
{
    "body": "I finished testing the patch. It seems to pass tests okay but I totally agree with Burcin's comments above and would appreciate it if you could try to address them. Thanks!",
    "created_at": "2009-06-29T20:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16588",
    "user": "wdj"
}
```

I finished testing the patch. It seems to pass tests okay but I totally agree with Burcin's comments above and would appreciate it if you could try to address them. Thanks!



---

archive/issue_comments_016589.json:
```json
{
    "body": "Replying to [comment:12 burcin]:\n\n**(1)**\n> so if you move the contents of your `__call__` function to `_eval_` and \n> remove the last `SFunction.__call__` line things should work fine. \n\nThanks Burcin! Thats what it needed. As you suggested, I have made those changes and\nexplicit evaluation is now working.\n\n\n**(2)**\n> I would also like to see a `.sub()` test added, \n\nI am assuming you meant \".subs()\". Several new tests are added as you \nsuggested.\n\n\n**(3)** Doctstrings are updated suitably as `__call__` methods are now removed.",
    "created_at": "2009-06-29T21:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16589",
    "user": "gmhossain"
}
```

Replying to [comment:12 burcin]:

**(1)**
> so if you move the contents of your `__call__` function to `_eval_` and 
> remove the last `SFunction.__call__` line things should work fine. 

Thanks Burcin! Thats what it needed. As you suggested, I have made those changes and
explicit evaluation is now working.


**(2)**
> I would also like to see a `.sub()` test added, 

I am assuming you meant ".subs()". Several new tests are added as you 
suggested.


**(3)** Doctstrings are updated suitably as `__call__` methods are now removed.



---

archive/issue_comments_016590.json:
```json
{
    "body": "Sorry for doing this in such small pieces, but I have one more suggestion. \n\nYou can change the calls to the `_is_real()` function by `x in RR` where you import `RR` from `sage.rings.real_mpfr`. The semantics of the `__contains__()` method in Sage is similar to your `_is_real()`, though it also checks that `approx_x == x` in your code.\n\nBTW, the reason `exp(-100000000000)` is evaluated to be 0 is that we don't use interval fields to do the numerical approximation. This is also ##5993.",
    "created_at": "2009-06-30T10:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16590",
    "user": "burcin"
}
```

Sorry for doing this in such small pieces, but I have one more suggestion. 

You can change the calls to the `_is_real()` function by `x in RR` where you import `RR` from `sage.rings.real_mpfr`. The semantics of the `__contains__()` method in Sage is similar to your `_is_real()`, though it also checks that `approx_x == x` in your code.

BTW, the reason `exp(-100000000000)` is evaluated to be 0 is that we don't use interval fields to do the numerical approximation. This is also ##5993.



---

archive/issue_comments_016591.json:
```json
{
    "body": "Replying to [comment:15 burcin]:\n> Sorry for doing this in such small pieces, but I have one more suggestion. \n> \n> You can change the calls to the `_is_real()` function by `x in RR` where you import `RR` from `sage.rings.real_mpfr`. \n> The semantics of the `__contains__()` method in Sage is similar to your `_is_real()`, though it also checks that `approx_x == x` in your code.\n\nHi Burcin. I tried your suggestion. I am not sure whats going wrong but it slows down massively. Could\nyou please check this out?\n\n**With: `_is_real(x)`**\n\n\n```\nsage: timeit( 'dirac_delta(1 + I*exp(-10000))')\n125 loops, best of 3: 6.47 ms per loop\nsage: timeit( 'dirac_delta(1 + I*exp(-10000000000000000))')\n125 loops, best of 3: 6.23 ms per loop\n```\n\n\n**with: `x in RR`**\n \n\n```\nsage: timeit( 'dirac_delta(1 + I*exp(-10000))')\n125 loops, best of 3: 6.56 ms per loop\nsage: timeit( 'dirac_delta(1 + I*exp(-10000000000000000))')\n5 loops, best of 3: 154 ms per loop\n```\n\n\nThanks,",
    "created_at": "2009-06-30T13:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16591",
    "user": "gmhossain"
}
```

Replying to [comment:15 burcin]:
> Sorry for doing this in such small pieces, but I have one more suggestion. 
> 
> You can change the calls to the `_is_real()` function by `x in RR` where you import `RR` from `sage.rings.real_mpfr`. 
> The semantics of the `__contains__()` method in Sage is similar to your `_is_real()`, though it also checks that `approx_x == x` in your code.

Hi Burcin. I tried your suggestion. I am not sure whats going wrong but it slows down massively. Could
you please check this out?

**With: `_is_real(x)`**


```
sage: timeit( 'dirac_delta(1 + I*exp(-10000))')
125 loops, best of 3: 6.47 ms per loop
sage: timeit( 'dirac_delta(1 + I*exp(-10000000000000000))')
125 loops, best of 3: 6.23 ms per loop
```


**with: `x in RR`**
 

```
sage: timeit( 'dirac_delta(1 + I*exp(-10000))')
125 loops, best of 3: 6.56 ms per loop
sage: timeit( 'dirac_delta(1 + I*exp(-10000000000000000))')
5 loops, best of 3: 154 ms per loop
```


Thanks,



---

archive/issue_comments_016592.json:
```json
{
    "body": "Hi Golam,\n\nYou're right! When using high precision we start calling maxima to decide if two expressions are equal. This kills performance as you observed.\n\nNow I suggest using `CIF(x).imag() == 0` where `x` is the element you want to test for. This is consistent in timings, and produces correct results:\n\n\n```\nsage: u = 1 + I*exp(-10000000000000000)\nsage: CIF(u).imag() == 0\nFalse\nsage: timeit('b = (CIF(u).imag() == 0)')\n625 loops, best of 3: 761 \u00b5s per loop\nsage: t = 1 + I*exp(-10000)\nsage: CIF(t).imag() == 0\nFalse\nsage: timeit('b = (CIF(t).imag() == 0)')\n625 loops, best of 3: 784 \u00b5s per loop\n```\n\n\nThanks.",
    "created_at": "2009-06-30T19:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16592",
    "user": "burcin"
}
```

Hi Golam,

You're right! When using high precision we start calling maxima to decide if two expressions are equal. This kills performance as you observed.

Now I suggest using `CIF(x).imag() == 0` where `x` is the element you want to test for. This is consistent in timings, and produces correct results:


```
sage: u = 1 + I*exp(-10000000000000000)
sage: CIF(u).imag() == 0
False
sage: timeit('b = (CIF(u).imag() == 0)')
625 loops, best of 3: 761 µs per loop
sage: t = 1 + I*exp(-10000)
sage: CIF(t).imag() == 0
False
sage: timeit('b = (CIF(t).imag() == 0)')
625 loops, best of 3: 784 µs per loop
```


Thanks.



---

archive/issue_comments_016593.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-07-01T00:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16593",
    "user": "gmhossain"
}
```

Attachment



---

archive/issue_comments_016594.json:
```json
{
    "body": "Replying to [comment:17 burcin]:\n> Now I suggest using `CIF(x).imag() == 0` where `x` is the element you want to test for. \n\nThats great. It now works much faster even for very very small numbers. Here are the \nchanges in the updated patch:\n\n**(1)**:  _is_real(x) removed\n\n**(2)**:  CIF(x) is now being used\n\n**(3)**: Notes on finite precision size removed.\n\n**(4)**: new doctests for very small numbers added",
    "created_at": "2009-07-01T00:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16594",
    "user": "gmhossain"
}
```

Replying to [comment:17 burcin]:
> Now I suggest using `CIF(x).imag() == 0` where `x` is the element you want to test for. 

Thats great. It now works much faster even for very very small numbers. Here are the 
changes in the updated patch:

**(1)**:  _is_real(x) removed

**(2)**:  CIF(x) is now being used

**(3)**: Notes on finite precision size removed.

**(4)**: new doctests for very small numbers added



---

archive/issue_comments_016595.json:
```json
{
    "body": "This applies to 4.1.alpha1 on an amd64 ubuntu 9.04 machine and passes all tests except for three which seem unrelated (darwin_utilities, random_tests, and the French programming tutorial).\n\n```\nsage: t = var(\"t\")\nsage: plot(heaviside(t)+2*heaviside(t-1),t,-5,5)\nsage: P1 = plot(t*heaviside(t)+(2-t)*heaviside(t-1),t,-5,5)\nsage: P2 = plot(heaviside(t)*cos(t),t,-5,5, linestyle=\"--\", rgbcolor=(1,0,0), thickness=3)\nsage: show(P1+P2)\n\n```\n\nI like the fact that plotting like this works so well!",
    "created_at": "2009-07-01T13:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16595",
    "user": "wdj"
}
```

This applies to 4.1.alpha1 on an amd64 ubuntu 9.04 machine and passes all tests except for three which seem unrelated (darwin_utilities, random_tests, and the French programming tutorial).

```
sage: t = var("t")
sage: plot(heaviside(t)+2*heaviside(t-1),t,-5,5)
sage: P1 = plot(t*heaviside(t)+(2-t)*heaviside(t-1),t,-5,5)
sage: P2 = plot(heaviside(t)*cos(t),t,-5,5, linestyle="--", rgbcolor=(1,0,0), thickness=3)
sage: show(P1+P2)

```

I like the fact that plotting like this works so well!



---

archive/issue_comments_016596.json:
```json
{
    "body": "fix doctests in random_tests.py",
    "created_at": "2009-07-02T09:53:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16596",
    "user": "burcin"
}
```

fix doctests in random_tests.py



---

archive/issue_comments_016597.json:
```json
{
    "body": "Attachment\n\nThe failing doctests in sage/symbolic/random_tests.py is caused by this ticket. That function constructs a random expression, given all the symbolic functions defined in Sage. Since this patch adds new functions, the probability distribution, hence the result changes.\n\nI attached a small patch to fix these doctests.",
    "created_at": "2009-07-02T09:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16597",
    "user": "burcin"
}
```

Attachment

The failing doctests in sage/symbolic/random_tests.py is caused by this ticket. That function constructs a random expression, given all the symbolic functions defined in Sage. Since this patch adds new functions, the probability distribution, hence the result changes.

I attached a small patch to fix these doctests.



---

archive/issue_comments_016598.json:
```json
{
    "body": "The second patch needs to be rebased. The following hunk fails, applying to my 4.1.rc0 branch:\n\n```\n--- random_tests.py\n+++ random_tests.py\n@@ -202,12 +202,11 @@\n\n         sage: from sage.symbolic.random_tests import *\n         sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)\n-        ceil(arctanh(-sinh(v2)/floor(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + floor(-(0.708874026302\n - 0.954135400334*I)*v3)))^sinh(arctan2(arcsinh((0.723896589334 + 0.799038508886*I)*(v2 + 0.913564344312 + 0.08980401603\n36*I)*v2), -1/v3)/(v3/v2 + 1.36062750308 - 1.05383406182*I))\n+        arctanh(sinh(-arcsech(v2)/floor(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + floor(-(0.708874026\n302 - 0.954135400334*I)*v3)))^arcsech(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^(-(0.723896589334 - 0.799\n038508886*I)*v2),-v1 - v3))/sin(-(0.0263902659909 + 0.153261789843*I)*arctan2(pi, e^pi)))\n         sage: random_expr(5, verbose=True)\n-        About to apply sec to [1]\n-        About to apply exp to [sec(1)]\n-        About to apply <built-in function mul> to [e^sec(1), v1]\n-        v1*e^sec(1)\n+        About to apply <built-in function add> to [v1, v1]\n+        About to apply <built-in function div> to [-1/3, 2*v1]\n+        -1/6/v1\n     \"\"\"\n     vars = [(1.0, sage.calculus.calculus.var('v%d' % (n+1))) for n in range(nvars)]\n     if ncoeffs is None:\n```\n",
    "created_at": "2009-07-03T17:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16598",
    "user": "rlm"
}
```

The second patch needs to be rebased. The following hunk fails, applying to my 4.1.rc0 branch:

```
--- random_tests.py
+++ random_tests.py
@@ -202,12 +202,11 @@

         sage: from sage.symbolic.random_tests import *
         sage: random_expr(50, nvars=3, coeff_generator=CDF.random_element)
-        ceil(arctanh(-sinh(v2)/floor(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + floor(-(0.708874026302
 - 0.954135400334*I)*v3)))^sinh(arctan2(arcsinh((0.723896589334 + 0.799038508886*I)*(v2 + 0.913564344312 + 0.08980401603
36*I)*v2), -1/v3)/(v3/v2 + 1.36062750308 - 1.05383406182*I))
+        arctanh(sinh(-arcsech(v2)/floor(-(0.615863165633 + 0.879368031485*I)*v1^2*v3) - gamma(pi) + floor(-(0.708874026
302 - 0.954135400334*I)*v3)))^arcsech(-cosh(-polylog((v2 + 0.913564344312 + 0.0898040160336*I)^(-(0.723896589334 - 0.799
038508886*I)*v2),-v1 - v3))/sin(-(0.0263902659909 + 0.153261789843*I)*arctan2(pi, e^pi)))
         sage: random_expr(5, verbose=True)
-        About to apply sec to [1]
-        About to apply exp to [sec(1)]
-        About to apply <built-in function mul> to [e^sec(1), v1]
-        v1*e^sec(1)
+        About to apply <built-in function add> to [v1, v1]
+        About to apply <built-in function div> to [-1/3, 2*v1]
+        -1/6/v1
     """
     vars = [(1.0, sage.calculus.calculus.var('v%d' % (n+1))) for n in range(nvars)]
     if ncoeffs is None:
```




---

archive/issue_comments_016599.json:
```json
{
    "body": "The second patch depends on #6421. Since #6421 was merged in 4.1.rc0, this can be applied without problems.\n\nSorry for the inconvenience.",
    "created_at": "2009-07-04T07:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16599",
    "user": "burcin"
}
```

The second patch depends on #6421. Since #6421 was merged in 4.1.rc0, this can be applied without problems.

Sorry for the inconvenience.



---

archive/issue_comments_016600.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-04T19:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2452",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2452#issuecomment-16600",
    "user": "rlm"
}
```

Resolution: fixed
