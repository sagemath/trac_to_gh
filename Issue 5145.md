# Issue 5145: increase default plot_points value for contour_plot

Issue created by migration from https://trac.sagemath.org/ticket/5145

Original creator: was

Original creation time: 2009-01-31 15:19:12

Assignee: tbd

Motivation: Somewhat regularly on sage-support we get emails like this:


```
Hi everyone,

I run into a very strange problem, that looks like critical to me.
Basically, I plot two functions that I know must be tangent at a given
point, and they are not.

First, the code:

x,y=var('x,y')
utility=y*x^2
budget = 24-x
cp=contour_plot(utility,(x,0,24),(y,
0,24),fill=False,cmap='cool',contours=(100,1000,2048,2700,3500))
bp=plot(budget,(x,0,24),color='red')
cp+bp

Now, the plot that comes after calling 'cp+bp' must have the following
property: the straight red line must be tangent to the contour of the
utility function evaluated at level utility=2048; and they must be
tangent at the point (16,8). In my system (Sage 3.2.3 on OpenSuse11.1)
they are NOT tangent; in fact, the sage plot indicates tangency at a
lower level, ~1820.
...
- Or else is it a calculation problem on the part of sage? I'd find
this absolutely strange. And critical: I want to trust Sage to do the
calculations correctly.

Can you reproduce it?

Thanks,
```


But putting plot_points=200 fixes things.   Right now the default is a mere 25, which seems absurdly small.   I think we should change the default plot_points parameter.  It was very low, I think, because evaluation of symbolic expressions used to be slow -- now it's extremely fast -- so we should increase the default number of points to at least 200. 


---

Comment by was created at 2009-01-31 16:58:57

From the OP: 

```
I second the idea of increaisng the default plot-points, at least to
100. On my not so recent intel duo it took less than a second with
200.
```



---

Comment by davidloeffler created at 2009-07-05 08:08:44

Changing assignee from tbd to was.


---

Comment by davidloeffler created at 2009-07-05 08:08:44

This should be in "graphics" I guess.


---

Comment by davidloeffler created at 2009-07-05 08:08:44

Changing component from algebra to graphics.


---

Comment by kcrisman created at 2009-08-27 03:05:18

This changes this to 100, except for implicit_plot, which is changed to 150 since it is usually used to see more detail.


---

Comment by jason created at 2009-09-10 15:23:06

Great work!  I'm glad to see this patch!

This needs to be rebased after #5448.  That patch changes the `@`options decorator for contour_plot, for example, and so there is a reject on applying this patch.


---

Comment by kcrisman created at 2009-09-10 15:45:45

Based on 4.1.1 and #5448


---

Attachment

Try this.


---

Comment by jason created at 2009-09-15 09:06:39

The code looks good; passes doctests in the affected file.


---

Comment by mvngu created at 2009-09-15 20:27:25

Resolution: fixed
