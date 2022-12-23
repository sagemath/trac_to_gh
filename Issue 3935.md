# Issue 3935: ode_solver __init__ method ignores many parameters

Issue created by migration from https://trac.sagemath.org/ticket/3935

Original creator: jwmerrill

Original creation time: 2008-08-23 18:38:38

Assignee: jkantor

The following example comes from the in-source documentation for ode_solver:


```
sage: T = ode_solver()
sage: g_1= lambda t,y: [y[1]*y[2],-y[0]*y[2],-0.51*y[0]*y[1]]
sage: T.function=g_1
sage: T.y_0=[0,1,1]
sage: T.scale_abs=[1e-4,1e-4,1e-5]
sage: T.error_rel=1e-4
sage: T.ode_solve(t_span=[0,12],num_points=100)
sage: f = T.interpolate_solution()
sage: f(pi)              # slightly random precision
0.53794725135406318
```


It should be possible to set these attributes using arguments to the constructor, but this fails:


```
sage: T = ode_solver(g_1,y_0=[0,1,1],scale_abs=[1e-4,1e-4,1e-5],error_rel=1e-4)
sage: T.ode_solve(t_span=[0,12],num_points=100)
sage: f = T.interpolate_solution()
sage: f(pi)
Traceback (click to the left for traceback)
...
TypeError: object of type 'NoneType' has no len()
```



---

Attachment

Adds a doctest and fixes the __init__ method


---

Comment by jwmerrill created at 2008-08-23 18:41:59

One thing I'm worried about is that the tests for ode.pyx already take a long time (more than two minutes), and this makes them take even longer.


---

Comment by jason created at 2008-08-27 15:43:29

This seems to work and doctests pass.  However, the given example is not the same as the example before (as the docs claim), since the algorithm used is different.  The referee patch adds an algorithm keyword to make it the same.  Apply the referee patch after the original patch and then it is positive review.


---

Attachment

jwmerrill, related to the docs of ode_solver, could you review #3966?  Thanks.


---

Comment by mabshoff created at 2008-08-27 22:08:33

Resolution: fixed


---

Comment by mabshoff created at 2008-08-27 22:08:33

Merged both patches in Sage 3.1.2.alpha2
