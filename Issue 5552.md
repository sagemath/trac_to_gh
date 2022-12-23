# Issue 5552: plot_slope_field typo

Issue created by migration from https://trac.sagemath.org/ticket/5552

Original creator: kcrisman

Original creation time: 2009-03-17 20:45:26

Assignee: was


```
plot_slope_field((f, g), (xvar, xmin, xmax), (yvar, ymin, ymax)) 
```

should only have one function, not the two functions left over from plot_vector_field


---

Comment by kcrisman created at 2009-03-17 20:51:08

This is in the docs, not in the def, of course.


---

Attachment


---

Comment by jason created at 2009-03-18 17:11:07

This looks correct.  Positive review.


---

Comment by jason created at 2009-03-18 17:13:17

The patch cleanly applies as well.


---

Comment by mabshoff created at 2009-03-23 21:26:54

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-23 21:26:54

Resolution: fixed
