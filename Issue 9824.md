# Issue 9824: desolve_system unable to interpret Maxima's temporary variables

Issue created by migration from https://trac.sagemath.org/ticket/9825

Original creator: rhinton

Original creation time: 2010-08-27 16:44:47

Assignee: burcin

CC:  robert.marik

Keywords: calculus, maxima, symbolics

desolve_system sometimes generates a Maxima result that includes temporary variables that Sage does not parse correctly.


```
sage: t = var('t')
sage: x1 = function('x1', t)
sage: x2 = function('x2', t)
sage: de1 = (diff(x1,t) == -3*(x2^2-1))
sage: de2 = (diff(x2,t) == 1)
sage: desolve_system([de1, de2], [x1, x2], ivar=t)
...
TypeError: unable to make sense of Maxima expression 'x1(t)=ilt(-((3*laplace(x2(t)^2,t,?g1543)-x1(0))*?g1543-3)/?g1543^2,?g1543,t)' in Sage 
```




---

Comment by kcrisman created at 2011-03-15 02:50:57

On [ this Maxima list thread] we get the original system in Maxima notation - thanks to Stavros Macrackis:

```
de1: diff(x1(t),t)=-3*(x2(t)^2-1);
de2: diff(x2(t),t)=1;
desolve([de1,de2],[x1(t),x2(t)]);
```

He also provides a simpler example which does this:

```
desolve([diff(f(x),x)=f(x^2)],[f(x)]);
```

The suggestion is that the ilt should be replacing the `?g1234` type variables (which are indeed dummy variables, but native Lisp ones) by Maxima-type ones, so I am putting to reported upstream, developers acknowledge bug.  However, my feeling is that we should fix this by parsing these things as well, should they come up again.


---

Comment by kcrisman created at 2011-03-15 02:52:03

Replying to [comment:1 kcrisman]:
> On [ this Maxima list thread] we get the original system in Maxima notation - thanks to Stavros Macrackis:

Meaning [this thread](http://www.math.utexas.edu/pipermail/maxima/2011/024573.html).


---

Comment by kcrisman created at 2012-05-17 12:56:45

I've followed up again at [this new thread](http://www.math.utexas.edu/pipermail/maxima/2012/028833.html) - apparently it never actually made it to their bug tracker?


---

Comment by kcrisman created at 2012-11-30 14:01:31

See also [this ask.sagemath question](http://ask.sagemath.org/question/2039/desolve_system-error-unable-to-make-sense-of).


---

Comment by kcrisman created at 2013-07-03 15:48:43

And [this ask.sagemath question](http://ask.sagemath.org/question/2773/desolve_system-problem-with-expe), though here Maxima is actually asking a question about these variables!


---

Comment by kcrisman created at 2014-06-30 13:18:32

Did you report it upstream to their bug tracker?  I never heard on either of these emails, so I think this is how it will have to be reported.


---

Comment by rws created at 2014-06-30 14:03:13

I took your repeated mail to the list as report.


---

Comment by kcrisman created at 2014-06-30 14:14:59

Sadly, that isn't always enough :(  Reported upstream [here](https://sourceforge.net/p/maxima/bugs/2774/), however, just now.  There was internal discussion in the original Maxima thread so I took it that the experts had several possible resolutions.


---

Comment by kcrisman created at 2014-11-03 14:04:00

[Upstream](https://sourceforge.net/p/maxima/bugs/2774/#c37e) seems to have made a change that would do something about this.  Anyone want to give it a whirl?


---

Comment by rws created at 2015-02-01 10:25:38

This now returns `[x1(t) == ilt(-(3*g3390*laplace(x2(t)^2, t, g3390) - g3390*x1(0) - 3)/g3390^2, g3390, t), x2(t) == t + x2(0)]` so it becomes an issue to fix our Maxima interface.


---

Comment by nbruin created at 2015-02-01 17:39:53

Replying to [comment:15 rws]:
> This now returns `[x1(t) == ilt(-(3*g3390*laplace(x2(t)^2, t, g3390) - g3390*x1(0) - 3)/g3390^2, g3390, t), x2(t) == t + x2(0)]` so it becomes an issue to fix our Maxima interface.

According to the documentation of `inverse_laplace` this is probably more or less correct. We might want to do something about "ilt" so that it is more closely tied to `inverse_laplace`, though.


---

Comment by charpent created at 2021-03-13 13:18:40

Changing status from new to needs_review.


---

Comment by charpent created at 2021-03-13 13:18:40

This is now fixed (probably due to upstream upgrade) :


```
sage: x1, x2=function("x1, x2")
sage: de1=x1(t).diff(t)==-3*(x2(t)-1)
sage: de2=x2(t).diff(t)==1
sage: Sol=desolve_system([de1, de2],[x1(t),x2(t)],ivar=t) ; Sol
[x1(t) == -3/2*t^2 - 3*t*x2(0) + 3*t + x1(0), x2(t) == t + x2(0)]
```


==> invalidation of the bug and review query in order to get this bug closed.

HTH,


---

Comment by kcrisman created at 2021-03-13 13:26:04

I guess as usual doctest needed?  Looks like it was a combination of their upstream fix and something we did to parse it right.


---

Comment by kcrisman created at 2021-03-13 13:26:04

Changing status from needs_review to needs_work.


---

Comment by charpent created at 2021-03-14 10:26:43

Changing status from needs_work to needs_review.


---

Comment by charpent created at 2021-03-14 10:26:43

Doctest added.

HTH,
----
New commits:


---

Comment by kcrisman created at 2021-03-17 14:38:57

Thanks, this is great.  Despite patchbot not yet reporting and my own Sage install being too brittle to test, [Cell server](https://sagecell.sagemath.org/?z=eJwrTkxPtVIoSyzSUC9R1-TlKgbzKwx1FCqMbNNK85JLMvPzNJQgAkpwBSmphrYVhholmnopmWlpQNrWVtdYS6PCCMjUNURSZmQLFkMoM4TJBefn2KakFufnlKXGF1cWl6TmakQDjdUBaYrViQabrgPWHKuTCXSgbYmmgjVIFwBUFzUS&lang=sage&interacts=eJyLjgUAARUAuQ==) says it's fine so let's do it.


---

Comment by kcrisman created at 2021-03-17 14:38:57

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2021-03-20 15:27:45

Resolution: fixed
