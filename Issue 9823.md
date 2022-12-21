# Issue 9823: desolve_system ignores initial conditions

Issue created by migration from Trac.

Original creator: rhinton

Original creation time: 2010-08-27 16:42:45

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



---

Comment by robert.marik created at 2010-08-29 20:36:21

Changing status from new to needs_info.


---

Comment by robert.marik created at 2010-08-29 20:36:21

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

Comment by rhinton created at 2010-08-31 03:01:01

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

Comment by rhinton created at 2010-08-31 03:01:01

Changing status from needs_info to needs_work.


---

Comment by kcrisman created at 2011-03-14 20:49:59

I agree that we should be explicit here.  There is no obvious default for a diffeq; initial condition of zero is not the same as starting to count at 0 or 1.  Yes, updating the documentation would be great for this.


---

Comment by kcrisman created at 2011-06-14 15:29:09

Changing keywords from "calculus, maxima, symbolics" to "calculus, maxima, symbolics, beginner".


---

Comment by captaintrunky created at 2014-12-17 12:41:55

Changing status from needs_work to needs_review.


---

Comment by captaintrunky created at 2014-12-17 12:41:55

New commits:


---

Comment by kcrisman created at 2014-12-17 16:41:08

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

I get similar errors if Maxima just can't solve the system, but with a _message_.  While it's true that `u` isn't one of the variables differentiated by or of the functions `u`, at least it should give an error message that the system doesn't make sense; this could easily happen as a typo for something that works fine.

```
sage:         sage: sol = desolve_system(des, vars, ics, t); sol
[x(t) == -(u - 1)*cos(t) + u + 2*sin(t),
 y(t) == -(u - 1)*sin(t) - 2*cos(t) + 1]
```

Perhaps for another ticket.


---

Comment by kcrisman created at 2014-12-17 16:41:31

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-12-18 00:57:19

Resolution: fixed
