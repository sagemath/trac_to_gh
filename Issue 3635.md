# Issue 3635: If m is a matrix, then m.plot() should call matrix_plot

Issue created by migration from https://trac.sagemath.org/ticket/3635

Original creator: jason

Original creation time: 2008-07-10 20:41:22

Assignee: was

Currently this just puts the text description on an empty set of axes.


---

Attachment

The attached patch implements the requested behavior. Jason, do you want to review it?


---

Comment by kcrisman created at 2008-08-20 01:35:15

Whoever reviews it and/or malb should note that the patches to #3853 would imply the call to MatrixPlotFactory is superfluous (though something may still have to be imported), but of course that patch has not yet been merged either.


---

Attachment


---

Comment by jason created at 2008-08-27 14:46:00

Apply the rebased patch *AFTER* the first patch.  Sorry, I should have used a better word that rebased.

Works great. Positive review.


---

Comment by jason created at 2008-08-27 14:47:16

Doctests in matrix/matrix2.pyx pass after both patches have been applied.


---

Comment by mabshoff created at 2008-08-27 22:08:24

Resolution: fixed


---

Comment by mabshoff created at 2008-08-27 22:08:24

Merged both patches in Sage 3.1.2.alpha2
