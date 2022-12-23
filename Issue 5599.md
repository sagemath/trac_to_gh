# Issue 5599: density_plot not centered correctly

Issue created by migration from https://trac.sagemath.org/ticket/5599

Original creator: robertwb

Original creation time: 2009-03-24 10:28:46

Assignee: was

CC:  wcauchois


```
sage: var('x,y')
(x, y)
sage: density_plot(1/(x^10+y^10), (x, -10, 10), (y, -10, 10))

```


clearly illustrates this problem


---

Comment by jason created at 2009-03-24 21:08:42

The patch fixes the error and also fixes the same error several other places in the plotting code.


---

Comment by robertwb created at 2009-04-16 06:18:38

Yep, that fixes the issue.


---

Comment by mabshoff created at 2009-04-16 11:49:40

Unfortunately this patch has bitrotted, so please rebase against 3.4.1.rc3.

```
sage-3.4.1.rc3/devel/sage$ patch -p1 < trac_5599-plot-center.patch 
patching file sage/plot/contour_plot.py
Hunk #1 succeeded at 149 (offset 1 line).
Hunk #2 FAILED at 246.
Hunk #3 FAILED at 264.
Hunk #4 succeeded at 285 (offset 14 lines).
2 out of 4 hunks FAILED -- saving rejects to file sage/plot/contour_plot.py.rej
patching file sage/plot/density_plot.py
Hunk #1 succeeded at 117 with fuzz 2.
```

Once it is rebased the postive review can be reinstated provided the rejects are trivial to resolve. 

Cheers,

Michael


---

Attachment


---

Comment by jason created at 2009-05-30 08:24:51

I've rebased the patch against 4.0.  Bill, can you review it?


---

Comment by jason created at 2009-05-30 08:28:48

Or Robert, can you review it?


---

Comment by wcauchois created at 2009-06-02 09:11:09

REFEREE REPORT

Applies fine to Sage 4.0.rc0, and the changes look good. I tested some other plots as well, and they seemed fine. Positive review.


---

Comment by mhansen created at 2009-06-03 18:38:08

Merged in 4.0.1.rc0.


---

Comment by mhansen created at 2009-06-03 18:38:08

Resolution: fixed
