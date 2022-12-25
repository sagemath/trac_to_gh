# Issue 8624: integral of abs(cos(x))*sin(x) gives false results

archive/issues_008624.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @kcrisman\n\nThe integral of abs(cos(x))*sin(x) returns the result as if abs() is ignored:\n\n```\nsage: integral(abs(cos(x))*sin(x),(x,pi/2,pi))\n-1/2\n```\nwhile\n\n```\nsage: numerical_integral(abs(cos(x))*sin(x),pi/2,pi)\n(0.49999999999999994, 5.5511151231257819e-15)\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8624\n\n",
    "closed_at": "2010-12-06T12:11:44Z",
    "created_at": "2010-03-29T16:04:59Z",
    "labels": [
        "component: calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "integral of abs(cos(x))*sin(x) gives false results",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8624",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeroen"
}
```
Assignee: @burcin

CC:  @kcrisman

The integral of abs(cos(x))*sin(x) returns the result as if abs() is ignored:

```
sage: integral(abs(cos(x))*sin(x),(x,pi/2,pi))
-1/2
```
while

```
sage: numerical_integral(abs(cos(x))*sin(x),pi/2,pi)
(0.49999999999999994, 5.5511151231257819e-15)
```


Issue created by migration from https://trac.sagemath.org/ticket/8624





---

archive/issue_comments_078044.json:
```json
{
    "body": "This might be related to this bug, which should be somewhere on trac:\n\n```\nsage: integrate(sqrt(cos(x)^2+sin(x)^2), x,0,2*pi)       \npi\n```",
    "created_at": "2010-03-29T17:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78044",
    "user": "https://github.com/jasongrout"
}
```

This might be related to this bug, which should be somewhere on trac:

```
sage: integrate(sqrt(cos(x)^2+sin(x)^2), x,0,2*pi)       
pi
```



---

archive/issue_comments_078045.json:
```json
{
    "body": "#8729 may point to a solution",
    "created_at": "2010-04-20T16:53:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78045",
    "user": "https://github.com/jasongrout"
}
```

#8729 may point to a solution



---

archive/issue_comments_078046.json:
```json
{
    "body": "Changing assignee from @aghitza to @burcin.",
    "created_at": "2010-04-20T16:54:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78046",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @aghitza to @burcin.



---

archive/issue_events_020863.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2010-04-20T16:54:08Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "milestone": "sage-4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8624#event-20863"
}
```



---

archive/issue_comments_078047.json:
```json
{
    "body": "Changing component from algebra to calculus.",
    "created_at": "2010-04-20T16:54:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78047",
    "user": "https://github.com/jasongrout"
}
```

Changing component from algebra to calculus.



---

archive/issue_comments_078048.json:
```json
{
    "body": "This patch fixes the problem, but introduces some other doctest errors that should be fixed.",
    "created_at": "2010-04-20T20:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78048",
    "user": "https://github.com/jasongrout"
}
```

This patch fixes the problem, but introduces some other doctest errors that should be fixed.



---

archive/issue_comments_078049.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-04-20T20:12:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78049",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_078050.json:
```json
{
    "body": "Make sure it doesn't introduce any errors - sometimes loading extra Maxima packages causes trouble. Also note that elsewhere there are complaints about Maxima start time, which this would contribute to.",
    "created_at": "2010-04-20T20:40:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78050",
    "user": "https://github.com/kcrisman"
}
```

Make sure it doesn't introduce any errors - sometimes loading extra Maxima packages causes trouble. Also note that elsewhere there are complaints about Maxima start time, which this would contribute to.



---

archive/issue_comments_078051.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n> Also note that elsewhere there are complaints about Maxima start time, which this would contribute to.\n\n\n\nSure, but it was *wrong* before, and correctness trumps maxima startup time.  Unless we can detect what kind of integrals need this package loaded and load it dynamically, I think the best thing is to load it up front.",
    "created_at": "2010-05-13T04:40:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78051",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:5 kcrisman]:
> Also note that elsewhere there are complaints about Maxima start time, which this would contribute to.



Sure, but it was *wrong* before, and correctness trumps maxima startup time.  Unless we can detect what kind of integrals need this package loaded and load it dynamically, I think the best thing is to load it up front.



---

archive/issue_comments_078052.json:
```json
{
    "body": "Attachment [trac-8624-abs-integration.patch](tarball://root/attachments/some-uuid/ticket8624/trac-8624-abs-integration.patch) by @jasongrout created at 2010-05-13 06:48:51",
    "created_at": "2010-05-13T06:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78052",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8624-abs-integration.patch](tarball://root/attachments/some-uuid/ticket8624/trac-8624-abs-integration.patch) by @jasongrout created at 2010-05-13 06:48:51



---

archive/issue_comments_078053.json:
```json
{
    "body": "I think I caught the failing doctests...",
    "created_at": "2010-05-13T06:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78053",
    "user": "https://github.com/jasongrout"
}
```

I think I caught the failing doctests...



---

archive/issue_comments_078054.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-13T06:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78054",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_078055.json:
```json
{
    "body": "I don't like replacing the z85 etc. with z... stuff.  The output is not random, it just changes whenever we change those doctests.  Until we find a way to have Sage parse that and replace it with our own variables (if we even want to do that, which I'm not convinced of), it seems reasonable to just change them.",
    "created_at": "2010-05-13T12:52:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78055",
    "user": "https://github.com/kcrisman"
}
```

I don't like replacing the z85 etc. with z... stuff.  The output is not random, it just changes whenever we change those doctests.  Until we find a way to have Sage parse that and replace it with our own variables (if we even want to do that, which I'm not convinced of), it seems reasonable to just change them.



---

archive/issue_comments_078056.json:
```json
{
    "body": "It's exciting to see that we can handle one more of the Wester tests. Thanks for the patch Jason.\n\n\nI get the following errors after applying attachment:trac-8624-abs-integration.patch to 4.4.2:\n\n```\n**********************************************************************\nFile \".../devel/sage-t/sage/functions/piecewise.py\", line 780:\n    sage: f.integral()\nExpected:\n    Piecewise defined function with 1 parts, [[(-Infinity, +Infinity), x |--> -integrate(e^(-abs(x)), x, x, +Infinity)]]\nGot:\n    Piecewise defined function with 1 parts, [[(-Infinity, +Infinity), x |--> -1/2*((sgn(x) - 1)*e^(2*x) - 2*e^x*sgn(x) + sgn(x) + 1)*e^(-x) - 1]]\n**********************************************************************\n```\nMaple simply gives 2 for this one:\n\n```\n> integrate(exp(-abs(x)), x=-infinity..infinity);\nmemory used=3.8MB, alloc=3.1MB, time=0.15\n                                       2\n```\n\n---\n\n```\n**********************************************************************\nFile \".../devel/sage-t/sage/misc/functional.py\", line 705:\n    sage: h = integral(sin(x)/x^2, (x, 1, pi/2)); h\nExpected:\n    integrate(sin(x)/x^2, x, 1, 1/2*pi)\nGot:\n    1/2*gamma(-1, -1/2*I*pi) + 1/2*gamma(-1, 1/2*I*pi) - 1/2*gamma(-1, -I) - 1/2*gamma(-1, I)\n**********************************************************************\nFile \".../devel/sage-t/sage/misc/functional.py\", line 707:\n    sage: h.n()\nExpected:\n    0.339447940978915...\nGot:\n    0.339447940978884\n**********************************************************************\n```\n\nHere's the Maple output:\n\n```\n> integrate(sin(x)/x^2, x=1..1/2*Pi);\nmemory used=7.6MB, alloc=5.1MB, time=0.33\n                                               Pi\n                    sin(1) Pi - Ci(1) Pi + Ci(----) Pi - 2\n                                               2\n                    --------------------------------------\n                                      Pi\n```\n\nIt would be interesting to see how this is transformed to the expression with the incomplete gamma function above.\n\n---\n\n```\n**********************************************************************\nFile \".../devel/sage-t/sage/symbolic/integration/integral.py\", line 429:\n    sage: A = integral(1/ ((x-4) * (x^3+2*x+1)), x); A\nExpected:\n    1/73*log(x - 4) - 1/73*integrate((x^2 + 4*x + 18)/(x^3 + 2*x + 1), x)\nGot:\n    1/73*log(x - 4) - 1/73*integrate(x^2/(x^3 + 2*x + 1), x) - 4/73*integrate(x/(x^3 + 2*x + 1), x) - 18/73*integrate(1/(x^3 + 2*x + 1), x)\n```\n\nThis just distributes the integral to the polynomial in the numerator. It's interesting to see that maxima cannot handle results with algebraic numbers.\n\n---\n\n```\n**********************************************************************\nFile \".../devel/sage-t/sage/symbolic/integration/integral.py\", line 464:\n    sage: integrate(sin(x)*cos(10*x)*log(x), x)\nExpected:\n    1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)\nGot:\n    1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)\n```\nHere is the result from Maple:\n\n```\n> integrate(sin(x)*cos(10*x)*log(x), x);\n1/18 ln(x) cos(9 x) - 1/22 ln(x) cos(11 x) - 1/18 Ci(9 x) - 1/198 I Pi\n\n     + 1/198 I Pi csgn(x) + 1/22 Ci(11 x)\n```\nThis looks OK to me.\n\n---\n\n```\n**********************************************************************\nFile \".../devel/sage-t/sage/symbolic/integration/integral.py\", line 186:\n    sage: h = definite_integral(sin(x)/x^2, x, 1, 2); h\nExpected:\n    integrate(sin(x)/x^2, x, 1, 2)\nGot:\n    1/2*gamma(-1, -2*I) - 1/2*gamma(-1, -I) - 1/2*gamma(-1, I) + 1/2*gamma(-1, 2*I)\n**********************************************************************\nFile \".../devel/sage-t/sage/symbolic/integration/integral.py\", line 188:\n    sage: h.n() # indirect doctest\nExpected:\n    0.4723991772689525...\nGot:\n    0.472399177268906\n**********************************************************************\n```\nWe saw this in `sage/misc/functional.py` already.",
    "created_at": "2010-05-22T10:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78056",
    "user": "https://github.com/burcin"
}
```

It's exciting to see that we can handle one more of the Wester tests. Thanks for the patch Jason.


I get the following errors after applying attachment:trac-8624-abs-integration.patch to 4.4.2:

```
**********************************************************************
File ".../devel/sage-t/sage/functions/piecewise.py", line 780:
    sage: f.integral()
Expected:
    Piecewise defined function with 1 parts, [[(-Infinity, +Infinity), x |--> -integrate(e^(-abs(x)), x, x, +Infinity)]]
Got:
    Piecewise defined function with 1 parts, [[(-Infinity, +Infinity), x |--> -1/2*((sgn(x) - 1)*e^(2*x) - 2*e^x*sgn(x) + sgn(x) + 1)*e^(-x) - 1]]
**********************************************************************
```
Maple simply gives 2 for this one:

```
> integrate(exp(-abs(x)), x=-infinity..infinity);
memory used=3.8MB, alloc=3.1MB, time=0.15
                                       2
```

---

```
**********************************************************************
File ".../devel/sage-t/sage/misc/functional.py", line 705:
    sage: h = integral(sin(x)/x^2, (x, 1, pi/2)); h
Expected:
    integrate(sin(x)/x^2, x, 1, 1/2*pi)
Got:
    1/2*gamma(-1, -1/2*I*pi) + 1/2*gamma(-1, 1/2*I*pi) - 1/2*gamma(-1, -I) - 1/2*gamma(-1, I)
**********************************************************************
File ".../devel/sage-t/sage/misc/functional.py", line 707:
    sage: h.n()
Expected:
    0.339447940978915...
Got:
    0.339447940978884
**********************************************************************
```

Here's the Maple output:

```
> integrate(sin(x)/x^2, x=1..1/2*Pi);
memory used=7.6MB, alloc=5.1MB, time=0.33
                                               Pi
                    sin(1) Pi - Ci(1) Pi + Ci(----) Pi - 2
                                               2
                    --------------------------------------
                                      Pi
```

It would be interesting to see how this is transformed to the expression with the incomplete gamma function above.

---

```
**********************************************************************
File ".../devel/sage-t/sage/symbolic/integration/integral.py", line 429:
    sage: A = integral(1/ ((x-4) * (x^3+2*x+1)), x); A
Expected:
    1/73*log(x - 4) - 1/73*integrate((x^2 + 4*x + 18)/(x^3 + 2*x + 1), x)
Got:
    1/73*log(x - 4) - 1/73*integrate(x^2/(x^3 + 2*x + 1), x) - 4/73*integrate(x/(x^3 + 2*x + 1), x) - 18/73*integrate(1/(x^3 + 2*x + 1), x)
```

This just distributes the integral to the polynomial in the numerator. It's interesting to see that maxima cannot handle results with algebraic numbers.

---

```
**********************************************************************
File ".../devel/sage-t/sage/symbolic/integration/integral.py", line 464:
    sage: integrate(sin(x)*cos(10*x)*log(x), x)
Expected:
    1/18*log(x)*cos(9*x) - 1/22*log(x)*cos(11*x) - 1/18*integrate(cos(9*x)/x, x) + 1/22*integrate(cos(11*x)/x, x)
Got:
    1/198*(11*cos(9*x) - 9*cos(11*x))*log(x) + 1/44*Ei(-11*I*x) - 1/36*Ei(-9*I*x) - 1/36*Ei(9*I*x) + 1/44*Ei(11*I*x)
```
Here is the result from Maple:

```
> integrate(sin(x)*cos(10*x)*log(x), x);
1/18 ln(x) cos(9 x) - 1/22 ln(x) cos(11 x) - 1/18 Ci(9 x) - 1/198 I Pi

     + 1/198 I Pi csgn(x) + 1/22 Ci(11 x)
```
This looks OK to me.

---

```
**********************************************************************
File ".../devel/sage-t/sage/symbolic/integration/integral.py", line 186:
    sage: h = definite_integral(sin(x)/x^2, x, 1, 2); h
Expected:
    integrate(sin(x)/x^2, x, 1, 2)
Got:
    1/2*gamma(-1, -2*I) - 1/2*gamma(-1, -I) - 1/2*gamma(-1, I) + 1/2*gamma(-1, 2*I)
**********************************************************************
File ".../devel/sage-t/sage/symbolic/integration/integral.py", line 188:
    sage: h.n() # indirect doctest
Expected:
    0.4723991772689525...
Got:
    0.472399177268906
**********************************************************************
```
We saw this in `sage/misc/functional.py` already.



---

archive/issue_comments_078057.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-22T10:27:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78057",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_078058.json:
```json
{
    "body": "> ---\n> \n> ```\n> **********************************************************************\n> File \".../devel/sage-t/sage/misc/functional.py\", line 705:\n>     sage: h = integral(sin(x)/x^2, (x, 1, pi/2)); h\n> Expected:\n>     integrate(sin(x)/x^2, x, 1, 1/2*pi)\n> Got:\n>     1/2*gamma(-1, -1/2*I*pi) + 1/2*gamma(-1, 1/2*I*pi) - 1/2*gamma(-1, -I) - 1/2*gamma(-1, I)\n> **********************************************************************\n> File \".../devel/sage-t/sage/misc/functional.py\", line 707:\n>     sage: h.n()\n> Expected:\n>     0.339447940978915...\n> Got:\n>     0.339447940978884\n> **********************************************************************\n> ```\n\n\nHmm, did you have the new Maxima package at #8731 already installed?  This is dealt with there.\n\n> \n> Here's the Maple output:\n> \n> ```\n> > integrate(sin(x)/x^2, x=1..1/2*Pi);\n> memory used=7.6MB, alloc=5.1MB, time=0.33\n>                                                Pi\n>                     sin(1) Pi - Ci(1) Pi + Ci(----) Pi - 2\n>                                                2\n>                     --------------------------------------\n>                                       Pi\n> ```\n> \n> It would be interesting to see how this is transformed to the expression with the incomplete gamma function above.\n> \n\n\nApparently via Gamma(-1,x)=Ei(-x)+e^(-x)/x+1/2 (log(-1/x)-log(-x))+log(x) and the connection between Ei and Ci.  But it does check out!",
    "created_at": "2010-05-25T16:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78058",
    "user": "https://github.com/kcrisman"
}
```

> ---
> 
> ```
> **********************************************************************
> File ".../devel/sage-t/sage/misc/functional.py", line 705:
>     sage: h = integral(sin(x)/x^2, (x, 1, pi/2)); h
> Expected:
>     integrate(sin(x)/x^2, x, 1, 1/2*pi)
> Got:
>     1/2*gamma(-1, -1/2*I*pi) + 1/2*gamma(-1, 1/2*I*pi) - 1/2*gamma(-1, -I) - 1/2*gamma(-1, I)
> **********************************************************************
> File ".../devel/sage-t/sage/misc/functional.py", line 707:
>     sage: h.n()
> Expected:
>     0.339447940978915...
> Got:
>     0.339447940978884
> **********************************************************************
> ```


Hmm, did you have the new Maxima package at #8731 already installed?  This is dealt with there.

> 
> Here's the Maple output:
> 
> ```
> > integrate(sin(x)/x^2, x=1..1/2*Pi);
> memory used=7.6MB, alloc=5.1MB, time=0.33
>                                                Pi
>                     sin(1) Pi - Ci(1) Pi + Ci(----) Pi - 2
>                                                2
>                     --------------------------------------
>                                       Pi
> ```
> 
> It would be interesting to see how this is transformed to the expression with the incomplete gamma function above.
> 


Apparently via Gamma(-1,x)=Ei(-x)+e^(-x)/x+1/2 (log(-1/x)-log(-x))+log(x) and the connection between Ei and Ci.  But it does check out!



---

archive/issue_comments_078059.json:
```json
{
    "body": "> {{{\n> **********************************************************************\n> File \".../devel/sage-t/sage/functions/piecewise.py\", line 780:\n>     sage: f.integral()\n> Expected:\n>     Piecewise defined function with 1 parts, [This is the Trac macro ** that was inherited from the migration called with arguments (-Infinity, +Infinity), x )](https://trac.sagemath.org/wiki/WikiMacros#-macro)\n> Got:\n>     Piecewise defined function with 1 parts, [This is the Trac macro ** that was inherited from the migration called with arguments (-Infinity, +Infinity), x )](https://trac.sagemath.org/wiki/WikiMacros#-macro)\n> **********************************************************************\n> }}}\n\n\nThis is actually ok, because it is supposed to return an antiderivative, not a definite integral.  It is fantastically more complicated than it has to be, but it would simplify to\n\n```\nx>0: x --> -e^(-x)\nx<0: x --> e^x\n```\nwhich is indeed the correct antiderivative.\n\n> Maple simply gives 2 for this one:\n\n\nWhich is clearly correct, and indeed given by the previous line in the file:\n\n```\n            sage: f.integral(definite=True)\n            2\n```\n\nSo if this really is all the errors (I will check this with the new Maxima package momentarily), then I would say positive review once the z... are reverted to actual numbers.  I thought of another reason for this - the user reading documentation might be confused about that if they didn't see the actual output.",
    "created_at": "2010-05-25T16:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78059",
    "user": "https://github.com/kcrisman"
}
```

> {{{
> **********************************************************************
> File ".../devel/sage-t/sage/functions/piecewise.py", line 780:
>     sage: f.integral()
> Expected:
>     Piecewise defined function with 1 parts, [This is the Trac macro ** that was inherited from the migration called with arguments (-Infinity, +Infinity), x )](https://trac.sagemath.org/wiki/WikiMacros#-macro)
> Got:
>     Piecewise defined function with 1 parts, [This is the Trac macro ** that was inherited from the migration called with arguments (-Infinity, +Infinity), x )](https://trac.sagemath.org/wiki/WikiMacros#-macro)
> **********************************************************************
> }}}


This is actually ok, because it is supposed to return an antiderivative, not a definite integral.  It is fantastically more complicated than it has to be, but it would simplify to

```
x>0: x --> -e^(-x)
x<0: x --> e^x
```
which is indeed the correct antiderivative.

> Maple simply gives 2 for this one:


Which is clearly correct, and indeed given by the previous line in the file:

```
            sage: f.integral(definite=True)
            2
```

So if this really is all the errors (I will check this with the new Maxima package momentarily), then I would say positive review once the z... are reverted to actual numbers.  I thought of another reason for this - the user reading documentation might be confused about that if they didn't see the actual output.



---

archive/issue_comments_078060.json:
```json
{
    "body": "One more thing; this patch will have a failure in doctest due to the semicolon in line 334 of calculus/calculus.py, which suppresses the output in Sage, of course.  Otherwise I think that (with #8731) this will be a good improvement.",
    "created_at": "2010-05-25T17:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78060",
    "user": "https://github.com/kcrisman"
}
```

One more thing; this patch will have a failure in doctest due to the semicolon in line 334 of calculus/calculus.py, which suppresses the output in Sage, of course.  Otherwise I think that (with #8731) this will be a good improvement.



---

archive/issue_comments_078061.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-12-06T12:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78061",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_078062.json:
```json
{
    "body": "This is fixed at ticket #10187 by upgrading Maxima to version 5.22.1:\n\n```\n[mvngu@sage sage-4.6.1.alpha3]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: integral(abs(cos(x))*sin(x),(x,pi/2,pi))\n1/2\nsage: numerical_integral(abs(cos(x))*sin(x),pi/2,pi)\n(0.49999999999999994, 5.5511151231257819e-15)\nsage: integrate(sqrt(cos(x)^2+sin(x)^2), x,0,2*pi)\n2*pi\n```\n| Sage Version 4.6.1.alpha3, Release Date: 2010-12-05                |\n| Type notebook() for the GUI, and license() for information.        |\nMathematica 6.0 also agrees:\n\n```\nMathematica 6.0 for Linux x86 (64-bit)\nCopyright 1988-2007 Wolfram Research, Inc.\n\nIn[1]:= Integrate[Abs[Cos[x]] * Sin[x], {x,Pi/2,Pi}]\n\n        1\nOut[1]= -\n        2\n\nIn[2]:= Integrate[Sqrt[Cos[x]^2 + Sin[x]^2], {x,0,2*Pi}]\n\nOut[2]= 2 Pi\n```\n\nSo I'm closing this ticket as fixed.",
    "created_at": "2010-12-06T12:11:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78062",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This is fixed at ticket #10187 by upgrading Maxima to version 5.22.1:

```
[mvngu@sage sage-4.6.1.alpha3]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: integral(abs(cos(x))*sin(x),(x,pi/2,pi))
1/2
sage: numerical_integral(abs(cos(x))*sin(x),pi/2,pi)
(0.49999999999999994, 5.5511151231257819e-15)
sage: integrate(sqrt(cos(x)^2+sin(x)^2), x,0,2*pi)
2*pi
```
| Sage Version 4.6.1.alpha3, Release Date: 2010-12-05                |
| Type notebook() for the GUI, and license() for information.        |
Mathematica 6.0 also agrees:

```
Mathematica 6.0 for Linux x86 (64-bit)
Copyright 1988-2007 Wolfram Research, Inc.

In[1]:= Integrate[Abs[Cos[x]] * Sin[x], {x,Pi/2,Pi}]

        1
Out[1]= -
        2

In[2]:= Integrate[Sqrt[Cos[x]^2 + Sin[x]^2], {x,0,2*Pi}]

Out[2]= 2 Pi
```

So I'm closing this ticket as fixed.



---

archive/issue_events_020864.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-12-06T12:11:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8624#event-20864"
}
```



---

archive/issue_comments_078063.json:
```json
{
    "body": "Is that doctested in the patches for #10187?",
    "created_at": "2010-12-06T13:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78063",
    "user": "https://github.com/kcrisman"
}
```

Is that doctested in the patches for #10187?



---

archive/issue_comments_078064.json:
```json
{
    "body": "What about the other integrals that the patch adds to the doctests?  Do those integrals work now too?  If not, we should reopen this ticket or make a new one for those integrals.",
    "created_at": "2010-12-06T13:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78064",
    "user": "https://github.com/jasongrout"
}
```

What about the other integrals that the patch adds to the doctests?  Do those integrals work now too?  If not, we should reopen this ticket or make a new one for those integrals.



---

archive/issue_comments_078065.json:
```json
{
    "body": "Replying to [comment:15 jason]:\n> What about the other integrals that the patch adds to the doctests?  Do those integrals work now too?  If not, we should reopen this ticket or make a new one for those integrals.\n\n\nNo. But it shouldn't be difficult to write a documentation patch with doctests in the current ticket. The Sage 4.6.1 release cycle is now in feature freeze, but I think documentation patches are OK for merging in the upcoming release candidates. See #10434 for a follow-up documentation ticket.",
    "created_at": "2010-12-06T13:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78065",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:15 jason]:
> What about the other integrals that the patch adds to the doctests?  Do those integrals work now too?  If not, we should reopen this ticket or make a new one for those integrals.


No. But it shouldn't be difficult to write a documentation patch with doctests in the current ticket. The Sage 4.6.1 release cycle is now in feature freeze, but I think documentation patches are OK for merging in the upcoming release candidates. See #10434 for a follow-up documentation ticket.



---

archive/issue_comments_078066.json:
```json
{
    "body": "So... how's 'bout reopenin' this ticket with a changed title as suggested at #10434?  I don't want to get in trouble with someone, but I might do it myself...",
    "created_at": "2010-12-10T20:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78066",
    "user": "https://github.com/kcrisman"
}
```

So... how's 'bout reopenin' this ticket with a changed title as suggested at #10434?  I don't want to get in trouble with someone, but I might do it myself...



---

archive/issue_comments_078067.json:
```json
{
    "body": "See #11483, since reopening is now not allowed for non-release managers :)",
    "created_at": "2011-06-14T18:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8624#issuecomment-78067",
    "user": "https://github.com/kcrisman"
}
```

See #11483, since reopening is now not allowed for non-release managers :)
