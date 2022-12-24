# Issue 3520: bug in integrating sqrt

archive/issues_003520.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  @burcin alexghitza @orlitzky\n\nThis is a problem:\n\n\n```\nsage: f = sqrt(25-x)*sqrt(1+1/(4*(25-x)))\nsage: f.integral(x,9,16)\nintegrate(sqrt(1/(4*(25 - x)) + 1)*sqrt(25 - x), x, 9, 16)\nsage: f.nintegral(x,9,16)\n(24.9153783348643, 2.7661626694613149e-13, 21, 0)\nsage: g = f.simplify_radical()\nsage: g.integral(x,9,16)\nI*(65*sqrt(65)*I/6 - 37*sqrt(37)*I/6)/2\nsage: ans = g.integral(x,9,16)\nsage: ans.real()\n(37*sqrt(37)/6 - 65*sqrt(65)/6)/2\nsage: RR(ans.real())\n-24.9153783348643\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3520\n\n",
    "created_at": "2008-06-27T13:02:02Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in integrating sqrt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3520",
    "user": "@wdjoyner"
}
```
Assignee: @garyfurnish

CC:  @burcin alexghitza @orlitzky

This is a problem:


```
sage: f = sqrt(25-x)*sqrt(1+1/(4*(25-x)))
sage: f.integral(x,9,16)
integrate(sqrt(1/(4*(25 - x)) + 1)*sqrt(25 - x), x, 9, 16)
sage: f.nintegral(x,9,16)
(24.9153783348643, 2.7661626694613149e-13, 21, 0)
sage: g = f.simplify_radical()
sage: g.integral(x,9,16)
I*(65*sqrt(65)*I/6 - 37*sqrt(37)*I/6)/2
sage: ans = g.integral(x,9,16)
sage: ans.real()
(37*sqrt(37)/6 - 65*sqrt(65)/6)/2
sage: RR(ans.real())
-24.9153783348643
```


Issue created by migration from https://trac.sagemath.org/ticket/3520





---

archive/issue_comments_024798.json:
```json
{
    "body": "Just for reference, the same with MMA6:\n\n\n```\nIn[3]:=\nf[x_] := Sqrt[25 - x]*Sqrt[1 + 1/(4*(25 - x))]\n\nIn[16]:=\ng[x_] := Integrate[f[x], x]; FullSimplify[g[x]]\n\nOut[16]=\n(-(1/12))*(4 + 1/(25 - x))^(3/2)*(25 - x)^(3/2)\n\nIn[15]:=\nFullSimplify[D[g[x], x] - f[x]]\n\nOut[15]=\n0\n\nIn[6]:=\nIntegrate[f[x], {x, 9, 16}]\n\nOut[6]=\n(1/12)*(-37*Sqrt[37] + 65*Sqrt[65])\n\nIn[8]:=\nNIntegrate[f[x], {x, 9, 16}, WorkingPrecision -> 40]\n\nOut[8]=\n24.915378334864299909236795241439053518882655529789`40.\n```\n",
    "created_at": "2008-06-27T14:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24798",
    "user": "@haraldschilly"
}
```

Just for reference, the same with MMA6:


```
In[3]:=
f[x_] := Sqrt[25 - x]*Sqrt[1 + 1/(4*(25 - x))]

In[16]:=
g[x_] := Integrate[f[x], x]; FullSimplify[g[x]]

Out[16]=
(-(1/12))*(4 + 1/(25 - x))^(3/2)*(25 - x)^(3/2)

In[15]:=
FullSimplify[D[g[x], x] - f[x]]

Out[15]=
0

In[6]:=
Integrate[f[x], {x, 9, 16}]

Out[6]=
(1/12)*(-37*Sqrt[37] + 65*Sqrt[65])

In[8]:=
NIntegrate[f[x], {x, 9, 16}, WorkingPrecision -> 40]

Out[8]=
24.915378334864299909236795241439053518882655529789`40.
```




---

archive/issue_comments_024799.json:
```json
{
    "body": "With the new symbolics and Maxima 5.19.1:\n\n```\nsage: sqrt(25-x)*sqrt(1+1/(4*(25-x)))\nsqrt(-1/4/(x - 25) + 1)*sqrt(-x + 25)\nsage: f = _\nsage: f.integral(x)\n1/12*(4*I*x - 101*I)*sqrt(4*x - 101)\nsage: f.integral(x,9,16)\n-37/12*sqrt(37) + 65/12*sqrt(65)\nsage: f.nintegral(x,9,16)\n(24.9153783348643, 2.7661626694613149e-13, 21, 0)\nsage: g = f.simplify_radical()\nsage: g.integral(x,9,16)\n37/12*sqrt(37) - 65/12*sqrt(65)\nsage: ans = g.integral(x,9,16)\nsage: ans.real()\n37/12*sqrt(37) - 65/12*sqrt(65)\nsage: RR(ans.real())\n-24.9153783348643\n```\n\nMaxima can now integrate the original one, but still gives the wrong simplification (?) of f.  It seems to be choosing the wrong square root of negative one, as it were, since\n\n```\nsage: j = -g\nsage: j.integrate(x,9,16)\n-37/12*sqrt(37) + 65/12*sqrt(65)\n```\n\nSo the real problem is in simplify_radical().",
    "created_at": "2009-09-15T19:42:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24799",
    "user": "@kcrisman"
}
```

With the new symbolics and Maxima 5.19.1:

```
sage: sqrt(25-x)*sqrt(1+1/(4*(25-x)))
sqrt(-1/4/(x - 25) + 1)*sqrt(-x + 25)
sage: f = _
sage: f.integral(x)
1/12*(4*I*x - 101*I)*sqrt(4*x - 101)
sage: f.integral(x,9,16)
-37/12*sqrt(37) + 65/12*sqrt(65)
sage: f.nintegral(x,9,16)
(24.9153783348643, 2.7661626694613149e-13, 21, 0)
sage: g = f.simplify_radical()
sage: g.integral(x,9,16)
37/12*sqrt(37) - 65/12*sqrt(65)
sage: ans = g.integral(x,9,16)
sage: ans.real()
37/12*sqrt(37) - 65/12*sqrt(65)
sage: RR(ans.real())
-24.9153783348643
```

Maxima can now integrate the original one, but still gives the wrong simplification (?) of f.  It seems to be choosing the wrong square root of negative one, as it were, since

```
sage: j = -g
sage: j.integrate(x,9,16)
-37/12*sqrt(37) + 65/12*sqrt(65)
```

So the real problem is in simplify_radical().



---

archive/issue_comments_024800.json:
```json
{
    "body": "One may want to check the latest CVS of Maxima, where I believe some definitions relating to this have changed.",
    "created_at": "2009-09-22T21:10:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24800",
    "user": "@kcrisman"
}
```

One may want to check the latest CVS of Maxima, where I believe some definitions relating to this have changed.



---

archive/issue_comments_024801.json:
```json
{
    "body": "Changing component from calculus to symbolics.",
    "created_at": "2009-12-22T17:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24801",
    "user": "@kcrisman"
}
```

Changing component from calculus to symbolics.



---

archive/issue_comments_024802.json:
```json
{
    "body": "Just updating.  This is still in 5.20.1, but it's not clear whether this is really a bug, since radical simplifications will in their nature sometimes change which square root of -1 they use, and perhaps it's not possible to do so consistently across multiplication or division.  Comments?",
    "created_at": "2009-12-22T17:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24802",
    "user": "@kcrisman"
}
```

Just updating.  This is still in 5.20.1, but it's not clear whether this is really a bug, since radical simplifications will in their nature sometimes change which square root of -1 they use, and perhaps it's not possible to do so consistently across multiplication or division.  Comments?



---

archive/issue_comments_024803.json:
```json
{
    "body": "Maxima devs have been discussing some things related to this, so it could be worth checking whether this has changed again in their CVS.",
    "created_at": "2010-02-05T20:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24803",
    "user": "@kcrisman"
}
```

Maxima devs have been discussing some things related to this, so it could be worth checking whether this has changed again in their CVS.



---

archive/issue_comments_024804.json:
```json
{
    "body": "What is really going on here is that `simplify_radical` uses `radcan` under the hood, which treats things as symbolic expressions, not functions, and just chooses a branch - consistently, but arbitrarily.  At least I think that is what is here.  See [the Maxima list thread starting here](http://www.math.utexas.edu/pipermail/maxima/2011/026097.html).",
    "created_at": "2011-09-23T14:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24804",
    "user": "@kcrisman"
}
```

What is really going on here is that `simplify_radical` uses `radcan` under the hood, which treats things as symbolic expressions, not functions, and just chooses a branch - consistently, but arbitrarily.  At least I think that is what is here.  See [the Maxima list thread starting here](http://www.math.utexas.edu/pipermail/maxima/2011/026097.html).



---

archive/issue_comments_024805.json:
```json
{
    "body": "It seems to be that this is probably a dup of #14305, #11912, and/or other such tickets.  Thoughts?",
    "created_at": "2014-11-17T17:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24805",
    "user": "@kcrisman"
}
```

It seems to be that this is probably a dup of #14305, #11912, and/or other such tickets.  Thoughts?



---

archive/issue_comments_024806.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> It seems to be that this is probably a dup of #14305, #11912, and/or other such tickets.  Thoughts?\n\nIndeed, #11912 \"fixes\" it by renaming `simplify_radical` and updating its documentation so that it's very clear that this might happen.",
    "created_at": "2014-11-17T17:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24806",
    "user": "@orlitzky"
}
```

Replying to [comment:12 kcrisman]:
> It seems to be that this is probably a dup of #14305, #11912, and/or other such tickets.  Thoughts?

Indeed, #11912 "fixes" it by renaming `simplify_radical` and updating its documentation so that it's very clear that this might happen.



---

archive/issue_comments_024807.json:
```json
{
    "body": "> > It seems to be that this is probably a dup of #14305, #11912, and/or other such tickets.  Thoughts?\n> \n> Indeed, #11912 \"fixes\" it by renaming `simplify_radical` and updating its documentation so that it's very clear that this might happen.\n\nIn which case perhaps this integration example could be added there.",
    "created_at": "2014-11-17T18:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24807",
    "user": "@kcrisman"
}
```

> > It seems to be that this is probably a dup of #14305, #11912, and/or other such tickets.  Thoughts?
> 
> Indeed, #11912 "fixes" it by renaming `simplify_radical` and updating its documentation so that it's very clear that this might happen.

In which case perhaps this integration example could be added there.



---

archive/issue_comments_024808.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-11-17T18:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24808",
    "user": "@kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_024809.json:
```json
{
    "body": "Replying to [comment:14 kcrisman]:\n> \n> In which case perhaps this integration example could be added there.\n\nThere are a lot of examples of problems with `simplify_radical`, but this one isn't particularly clear. It's not like someone is going to see the example in the description and go \"oh, that affects me!\"\n\nI think this ultimately comes down to `sqrt(x^2)` anyway, and that is included as an example.\n\nThat was my reasoning anyway. If it will help get it reviewed faster, I'll add whatever you want =)",
    "created_at": "2014-11-17T20:00:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24809",
    "user": "@orlitzky"
}
```

Replying to [comment:14 kcrisman]:
> 
> In which case perhaps this integration example could be added there.

There are a lot of examples of problems with `simplify_radical`, but this one isn't particularly clear. It's not like someone is going to see the example in the description and go "oh, that affects me!"

I think this ultimately comes down to `sqrt(x^2)` anyway, and that is included as an example.

That was my reasoning anyway. If it will help get it reviewed faster, I'll add whatever you want =)



---

archive/issue_comments_024810.json:
```json
{
    "body": "> > In which case perhaps this integration example could be added there.\n> \n> That was my reasoning anyway. If it will help get it reviewed faster, I'll add whatever you want =)\n\nWell, I think that pointing out that things you might not think would be affected is not bad.",
    "created_at": "2014-11-18T02:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24810",
    "user": "@kcrisman"
}
```

> > In which case perhaps this integration example could be added there.
> 
> That was my reasoning anyway. If it will help get it reviewed faster, I'll add whatever you want =)

Well, I think that pointing out that things you might not think would be affected is not bad.



---

archive/issue_comments_024811.json:
```json
{
    "body": "Ok, I've just added this example to the branch at #11912.",
    "created_at": "2014-11-18T15:22:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24811",
    "user": "@orlitzky"
}
```

Ok, I've just added this example to the branch at #11912.



---

archive/issue_comments_024812.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-11-18T15:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24812",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_024813.json:
```json
{
    "body": "> Ok, I've just added this example to the branch at #11912.\nSweet.",
    "created_at": "2014-11-18T15:26:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24813",
    "user": "@kcrisman"
}
```

> Ok, I've just added this example to the branch at #11912.
Sweet.



---

archive/issue_comments_024814.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2014-11-28T18:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3520",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3520#issuecomment-24814",
    "user": "@vbraun"
}
```

Resolution: duplicate
