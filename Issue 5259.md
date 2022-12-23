# Issue 5259: invalid array elements sent to matplotlib quiver, causing blank plot

Issue created by migration from https://trac.sagemath.org/ticket/5259

Original creator: jason

Original creation time: 2009-02-13 20:50:21

Assignee: was

A student noticed that sometimes, when a function evaluation gave Inf or NaN, the vector field plot was blank.  Discussing this on the matplotlib-users list revealed that we ought to mask our arrays before sending them to the matplotlib quiver function.  This patch corrects this, so that the plot:


```
plot_vector_field( (-x/sqrt(x^2+y^2), -y/sqrt(x^2+y^2)), (x, -10, 10), (y, -10, 10))
```


now plots (before it was a blank plot, now it just skips the problematic vectors).



---

Comment by jason created at 2009-02-13 20:55:33

Changing status from new to assigned.


---

Comment by jason created at 2009-02-13 20:55:33

To test this, you might try the following plots before and after the patch:


```
        sage: var('x,y')
        sage: plot_vector_field( (-x/sqrt(x^2+y^2), -y/sqrt(x^2+y^2)), (x, -10, 10), (y, -10, 10))
        sage: plot_vector_field( (-x/sqrt(x+y), -y/sqrt(x+y)), (x, -10, 10), (y, -10, 10))
```



---

Comment by jason created at 2009-02-13 20:55:33

Changing assignee from was to jason.


---

Comment by jason created at 2009-02-13 21:00:45

For the matplotlib-users discussion, see the messages with subject "quiver and Inf values" here: http://sourceforge.net/mailarchive/forum.php?forum_name=matplotlib-users&max_rows=25&style=ultimate&viewmonth=200902&viewday=13


---

Attachment

updated patch corrects the silly mistake in the doctest (I didn't account for the output of var('x,y')).  Now doctests pass in plot/*.py.


---

Comment by hivert created at 2009-02-13 22:09:04

Everything look good !


---

Comment by jason created at 2009-02-13 22:16:14

Robert Nelson should be listed as the reporter of this bug.


---

Comment by mabshoff created at 2009-02-14 09:03:46

Resolution: fixed


---

Comment by mabshoff created at 2009-02-14 09:03:46

Merged in Sage 3.3.rc1.

Cheers,

Michael
