# Issue 1508: axes_label in plot() broken

Issue created by migration from https://trac.sagemath.org/ticket/1508

Original creator: was

Original creation time: 2007-12-14 18:04:33

Assignee: was


```
Notice, if you tab-complete plot( or list_plot( the docs do not
mention the option for axes_label.  However, the option is available.

Also, if you use them, the text for the x-axis is truncated off the
right edge of the plot.

Simple example:

p = plot(sin, 0, 10)
p.show(axes_label=['x-axis','y-axis'])
```



---

Comment by was created at 2008-01-19 15:17:38

Changing status from new to assigned.


---

Attachment

fixes a mistake in const.tex


---

Attachment


---

Comment by mhansen created at 2008-01-20 23:53:33

Looks good to me.


---

Comment by mabshoff created at 2008-01-21 02:07:20

I am having reject issues with this against Sage 2.10.1.alpha0

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-21 03:17:47

Merged in Sage 2.10.1.alpha1. The reject mentioned above was caused by interaction from #1859 - I resolved those manually.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-21 03:17:47

Resolution: fixed
