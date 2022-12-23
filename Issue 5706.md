# Issue 5706: implicit_plot totally sucks when input an equation

Issue created by migration from https://trac.sagemath.org/ticket/5706

Original creator: was

Original creation time: 2009-04-07 17:36:29

Assignee: was

Make Sage hurt:

```
var('x,y')
implicit_plot(x^2+y^2 == 1, (x,-2,2), (y,-2,2))
```


The problem is that implicit_plot takes a function, not a symbolic equation, so it views "x<sup>2+y</sup>2 == 1" as a function --- and that is very painful.  

SOLUTION: Check if the input is an equation, and if so, make RHS zero, and plot corresponding function equal to 0.



---

Attachment


---

Comment by mabshoff created at 2009-04-09 06:23:29

There is one doctest failure in here:

```
sage -t -long "devel/sage/sage/plot/contour_plot.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.4.1.rc2/devel/sage/sage/plot/contour_plot.py", line 195:
    sage: implicit_plot(x^2+y^2 == 2, (-3,3), (-3,3)).show(aspect_ratio=1)
Expected nothing
Got:
    doctest:2846: DeprecationWarning: Substitution using function-call syntax and 
unnamed arguments is deprecated and will be removed from a future release of Sage; you 
can use named arguments instead, like EXPR(x=..., y=...)
**********************************************************************
1 items had failures:
```


Cheers,

Michael


---

Attachment

Slightly fixed up version of William's patch due to deprecation of substitution (see #5413)


---

Comment by mabshoff created at 2009-04-09 06:40:59

Resolution: fixed


---

Comment by mabshoff created at 2009-04-09 06:40:59

Merged trac_5706.2.patch in Sage 3.4.1.rc2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-09 06:49:45

Ooops, didn't change the review status.

Cheers,

Michael
