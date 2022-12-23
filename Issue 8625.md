# Issue 8625: plot_scalar_field (a scalar version of plot_vector_field)

Issue created by migration from https://trac.sagemath.org/ticket/8625

Original creator: olazo

Original creation time: 2010-03-29 18:46:11

Assignee: olazo

CC:  jason

Keywords: scalar,plot

This should be a function that plots a two variable funtion as a group of isolines along a given place of the xy plane.


---

Comment by kcrisman created at 2010-07-27 17:47:50

Would this be like a density plot or contour plot?  Even after consulting the internet I'm not quite sure what the difference would be, though perhaps a shortcut would be useful (?).


---

Attachment


---

Attachment

I have just attatched two pictures of the intended results. Both are plots of electric potentials the first one comes with a plot_vector_field of the corresponding electric field.

I also attatched a picture of the 3d version, although I mean to make a new ticket for that once this one is finished.


---

Comment by kcrisman created at 2010-08-02 15:02:51

It sounds like you are looking for a contour plot (?).  Can you describe what command you used to create the first plot?  Maybe we could make a shortcut to the specific type of contour plot you need, which would give the functionality you are looking for.


---

Comment by olazo created at 2010-08-02 15:56:22

Yes! I had not seen that command. I used implicit_plot. Now that I've checked contour_plot it is exactly what I wanted.

The only thing I don't like is the automatic choosing of contour levels. They usually get too high values that concentrate around the poles of the function so that there are almost no curves in parts of the picture away from the poles. I'll make a patch to improve that.

Also, it seems like there's no contour_plot3d I'll also work on that.


---

Comment by kcrisman created at 2010-08-02 16:03:18

Replying to [comment:4 olazo]:
> Yes! I had not seen that command. I used implicit_plot. Now that I've checked contour_plot it is exactly what I wanted.

Great!

> The only thing I don't like is the automatic choosing of contour levels. They usually get too high values that concentrate around the poles of the function so that there are almost no curves in parts of the picture away from the poles. I'll make a patch to improve that.

What I would do is leave the current functionality alone, but add an option for the sorts of situations you encounter - or something like that.  You can also choose the contours you want - see

```
sage: contour_plot?
```



> Also, it seems like there's no contour_plot3d I'll also work on that.

Have you tried `implicit_plot3d`? Presumably one would use this to start.


---

Comment by kcrisman created at 2010-08-02 16:03:18

Changing priority from major to minor.


---

Comment by olazo created at 2010-08-02 16:10:42

Replying to [comment:5 kcrisman]:
> What I would do is leave the current functionality alone, but add an option for the sorts of situations you encounter - or something like that.  You can also choose the contours you want - see

Yes, that's what I was thinking of, add something like an `,avoid_poles=False` option. Yes, I have seen the option to choose the contours.

> Have you tried `implicit_plot3d`? Presumably one would use this to start.

Yes, that is what I used to produce the 3d picture. I have just made #9669


---

Attachment
