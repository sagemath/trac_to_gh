# Issue 4462: contour_plot defaults changed to fill, affects implicit_plot

Issue created by migration from Trac.

Original creator: john_perry

Original creation time: 2008-11-07 16:48:30

Assignee: was

In Sage 3.1.1,

```
implicit_plot(x^2+y^2-1,(x,-1.1,1.1),(y,-1.1,1.1),plot_points=100).show(aspect_ratio=1)
```

produces a very nice circle.

In Sage 3.1.4, the same code produces a filled-in disc. Likewise, implicit_plot tries to fill in all curves;

```
implicit_plot(5*x^4-x^2-y^2,(x,-5,5),(y,-5,5))
```

looks odd.

The cause is contour_plot (called by implicit_plot): the default for the fill option is True. Feeding fill=False to implicit_plot produces the desired behavior:

```
implicit_plot(x^2+y^2-1,(x,-1.1,1.1),(y,-1.1,1.1),plot_points=100,fill=False).show(aspect_ratio=1)
```



---

Attachment

result of implicit_plot in sage 3.1.1


---

Comment by john_perry created at 2008-11-07 16:49:36

result of implicit_plot in sage 3.1.4


---

Attachment

The fix is easy: change line 2926 of site-packages/sage/plot/plot.py, which currently reads

```
`@`options(contours=(0,0))
```

to

```
`@`options(contours=(0,0),fill=False)
```



---

Comment by jason created at 2008-11-07 17:26:41

It looks like #4201 forgot to override that option of contour plot.  That's where the change was made.

I refereed that patch; my bad.


---

Attachment


---

Comment by jason created at 2008-11-07 18:34:07

John Perry should also receive credit for the patch, since he gave the actual fix in his comment.  I added documentation as well.


---

Comment by mhansen created at 2008-11-08 05:28:43

Looks good.


---

Comment by mabshoff created at 2008-11-08 07:13:31

Merged implicit-plot-no-fill.patch in Sage 3.2.rc0


---

Comment by mabshoff created at 2008-11-08 07:13:31

Resolution: fixed
