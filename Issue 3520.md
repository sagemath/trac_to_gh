# Issue 3520: bug in integrating sqrt

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-06-27 13:02:02

Assignee: gfurnish

CC:  burcin alexghitza mjo

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



---

Comment by schilly created at 2008-06-27 14:05:28

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

Comment by kcrisman created at 2009-09-15 19:42:12

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

Comment by kcrisman created at 2009-09-22 21:10:20

One may want to check the latest CVS of Maxima, where I believe some definitions relating to this have changed.


---

Comment by kcrisman created at 2009-12-22 17:00:44

Changing component from calculus to symbolics.


---

Comment by kcrisman created at 2009-12-22 17:00:44

Just updating.  This is still in 5.20.1, but it's not clear whether this is really a bug, since radical simplifications will in their nature sometimes change which square root of -1 they use, and perhaps it's not possible to do so consistently across multiplication or division.  Comments?


---

Comment by kcrisman created at 2010-02-05 20:09:06

Maxima devs have been discussing some things related to this, so it could be worth checking whether this has changed again in their CVS.


---

Comment by kcrisman created at 2011-09-23 14:46:07

What is really going on here is that `simplify_radical` uses `radcan` under the hood, which treats things as symbolic expressions, not functions, and just chooses a branch - consistently, but arbitrarily.  At least I think that is what is here.  See [the Maxima list thread starting here](http://www.math.utexas.edu/pipermail/maxima/2011/026097.html).


---

Comment by kcrisman created at 2014-11-17 17:31:22

It seems to be that this is probably a dup of #14305, #11912, and/or other such tickets.  Thoughts?


---

Comment by mjo created at 2014-11-17 17:52:12

Replying to [comment:12 kcrisman]:
> It seems to be that this is probably a dup of #14305, #11912, and/or other such tickets.  Thoughts?

Indeed, #11912 "fixes" it by renaming `simplify_radical` and updating its documentation so that it's very clear that this might happen.


---

Comment by kcrisman created at 2014-11-17 18:19:20

> > It seems to be that this is probably a dup of #14305, #11912, and/or other such tickets.  Thoughts?
> 
> Indeed, #11912 "fixes" it by renaming `simplify_radical` and updating its documentation so that it's very clear that this might happen.

In which case perhaps this integration example could be added there.


---

Comment by kcrisman created at 2014-11-17 18:19:20

Changing status from new to needs_review.


---

Comment by mjo created at 2014-11-17 20:00:50

Replying to [comment:14 kcrisman]:
> 
> In which case perhaps this integration example could be added there.

There are a lot of examples of problems with `simplify_radical`, but this one isn't particularly clear. It's not like someone is going to see the example in the description and go "oh, that affects me!"

I think this ultimately comes down to `sqrt(x^2)` anyway, and that is included as an example.

That was my reasoning anyway. If it will help get it reviewed faster, I'll add whatever you want =)


---

Comment by kcrisman created at 2014-11-18 02:41:56

> > In which case perhaps this integration example could be added there.
> 
> That was my reasoning anyway. If it will help get it reviewed faster, I'll add whatever you want =)

Well, I think that pointing out that things you might not think would be affected is not bad.


---

Comment by mjo created at 2014-11-18 15:22:49

Ok, I've just added this example to the branch at #11912.


---

Comment by kcrisman created at 2014-11-18 15:26:13

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2014-11-18 15:26:13

> Ok, I've just added this example to the branch at #11912.
Sweet.


---

Comment by vbraun created at 2014-11-28 18:38:12

Resolution: duplicate
