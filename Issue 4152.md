# Issue 4152: parametric_plot should take the variable range as (var, min, max) like plot

Issue created by migration from https://trac.sagemath.org/ticket/4152

Original creator: jason

Original creation time: 2008-09-19 16:35:56

Assignee: was

This should work to be consistent with plot:


```
sage: parametric_plot((2*x, x^2+1), (x,0,1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

TypeError: parametric_plot() takes exactly 3 arguments (2 given)
```




---

Comment by jason created at 2008-09-19 19:20:53

This was also mentioned in #2410, but was not a fundamental part of that ticket.


---

Comment by mhansen created at 2009-01-22 08:27:42

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2009-01-22 08:27:42

Changing assignee from was to mhansen.


---

Comment by jason created at 2009-01-22 14:20:06

apply on top of previous patch


---

Attachment

positive review for mhansen's patch.  My patch further adds to the documentation and makes the parametric plot function dispatch the 3d version when needed.  My patch needs to be reviewed.


---

Comment by mhansen created at 2009-01-22 14:31:11

Positive review for Jason's part.


---

Comment by mabshoff created at 2009-01-23 10:02:01

Resolution: fixed


---

Comment by mabshoff created at 2009-01-23 10:02:01

Merged both patches in Sage 3.3.alpha0

Cheers,

Michael
