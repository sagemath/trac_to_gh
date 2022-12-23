# Issue 4827: [with patch, needs review] add L-BFGS-B bound constraint solver to minimize_constraint

Issue created by migration from https://trac.sagemath.org/ticket/4827

Original creator: schilly

Original creation time: 2008-12-18 17:31:56

Assignee: jkantor

adding [scipy's l-bfgs-b](http://www.scipy.org/doc/api_docs/SciPy.optimize.lbfgsb.html#fmin_l_bfgs_b) large scale bound constraint solver, small change in docstring: bounds are better off in tuples.


---

Attachment

adds lbfgsb to minimize_constraint


---

Attachment

apply on top of previous patch


---

Comment by jason created at 2009-01-28 19:34:26

Looks good to me.

For another ticket: the minimize_constrained arguments should have x0 before cons to parallel the argument structure of the other minimze functions.  Also, we should maybe look into using openopt at some point since the syntax is then unified.

The small doc patch I attached makes the documentation of the function arguments in the same order as the function arguments.  I don't think it needs to be reviewed.


---

Comment by schilly created at 2009-01-28 20:00:28

Replying to [comment:1 jason]:
>  Also, we should maybe look into using openopt at some point since the syntax is then unified.

yeahr, tell me if somebody is working on that or you need help. maybe i can look into it. probably the most difficult part is to detect/register optional solvers inside sage, or talking to installed ones...

> 
> The small doc patch I attached makes the documentation of the function arguments in the same order as the function arguments.  I don't think it needs to be reviewed.

well, fwiw, +1 from me ;)


---

Comment by mabshoff created at 2009-01-29 00:27:21

Resolution: fixed


---

Comment by mabshoff created at 2009-01-29 00:27:21

Merged both patches in Sage 3.3.alpha3.

Cheers,

Michael
