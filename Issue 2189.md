# Issue 2189: improve functionality of matrix_plot

Issue created by migration from https://trac.sagemath.org/ticket/2189

Original creator: was

Original creation time: 2008-02-17 06:34:18

Assignee: was

CC:  jason kcrisman


```


On Feb 16, 2008 10:19 PM, inerkor@gmail.com <inerkor@gmail.com> wrote:
> 
> Hello all.
> 
> I have a Matrix of, say, 64x64 and I plot it using matrix_plot(). It
> is a fractal that fills the square [0,1]x[0,1] so I want to keep a 2D
> view. I would like to change the x,y axes ranging values to be in the
> interval [0,1] rather than in {0, ..., 63}. I don't know how to do it.
> Maybe using another plotting function?.
> 

Nobody has implemented a simple clean way to do that in Sage yet,
though it would be easy to do.  Here is a hackish way to do exactly
what you want:

sage: a = random_matrix(RDF,64)
sage: import numpy
sage: m = matrix_plot(a)
sage: m[0].xrange =numpy.array([0,1],dtype=float)   # key part of all this
sage: m[0].yrange =numpy.array([0,1],dtype=float)
sage: m.xmax(1); m.ymax(1)
sage: m.show()

The above will be helpful to whoever does implement this.

 -- William
```



---

Comment by whuss created at 2008-12-11 17:27:25

Changing assignee from was to whuss.


---

Comment by whuss created at 2008-12-11 17:27:25

The patch implements custom ranges, and adds the
options interpolation and alpha to matrix_plot.

It also fixes a few small bugs in the axes code
for matrix_plot.

Cheers,
Wilfried


---

Comment by kcrisman created at 2009-01-22 15:47:54

Attempted to apply this to 3.3.alpha0 but in the meantime _render_on_subplot method of class MatrixPlot (due to #4884) and the documentation for matrix_plot have both changed, so does not apply cleanly.  Needs a rebase.

Nitpicks:
1. I think this patch might fix the crazy overlap between "49" and "50" in one of the first examples of matrix_plot,

```
sage: matrix_plot(random_matrix(RDF, 50), cmap='hsv')
```

which looks horrible, but that should be checked when this is rebased.  
2. In axes.py, it would be great to fix the misspelling of "evaluate".
3. Possible request for improvement: the current behavior on the custom range seems to be floating point (is that correct?). Would it be possible to include custom ranges that were integer ranges, and (maybe) even ranges that actually labeled all integer values (as an option only, of course!)?  This would be very helpful for examples such as plotting a non-random matrix over GF(p), such as a colored multiplication table or power table.

This will be very helpful, though, when complete, so thanks for the work!


---

Attachment

rebased for sage-3.3.alpha1


---

Comment by whuss created at 2009-01-23 15:44:50

Replying to [comment:3 kcrisman]:
> Attempted to apply this to 3.3.alpha0 but in the meantime _render_on_subplot method of class MatrixPlot (due to #4884) and the documentation for matrix_plot have both changed, so does not apply cleanly.  Needs a rebase.

I added a new patch based on 3.3.alpha1
 
> Nitpicks:
> 1. I think this patch might fix the crazy overlap between "49" and "50" in one of the first examples of matrix_plot,
> {{{
> sage: matrix_plot(random_matrix(RDF, 50), cmap='hsv')
> }}}
> which looks horrible, but that should be checked when this is rebased.

Yes, the patch fixes the overlapping labels.

> 2. In axes.py, it would be great to fix the misspelling of "evaluate".

Done.

> 3. Possible request for improvement: the current behavior on the custom range seems to be floating point (is that correct?). Would it be possible to include custom ranges that were integer ranges,

You already can use integer ranges. Maybe I am misunderstanding what you mean.

> and (maybe) even ranges that actually labeled all integer values (as an option only, of course!)?  This would be very helpful for examples such as plotting a non-random matrix over GF(p), such as a colored multiplication table or power table.

There is already a ticket for this: #1431

> This will be very helpful, though, when complete, so thanks for the work!


---

Comment by kcrisman created at 2009-01-23 19:48:42

> There is already a ticket for this: #1431

Yes, you are correct - I forgot about that ticket because it's not specifically about matrices.

Any reviewer should keep in mind that patch at #4884 has introduced a new way to handle the colormap options, i.e.

```
cmap         -- a colormap (type cmap_help() for more information).
```

and that should probably be incorporated in this patch as well.


---

Comment by kcrisman created at 2009-01-24 02:33:15

For the examples given, this is nice - I have figured out what the purpose in the custom ranges is.

One trivial typo - in the sine bicubic example, the srange should be -pi to pi, not -pi to -pi.

More weird is the behavior of 

```
sage: matrix_plot(random_matrix(RDF, 2, 2), xrange=(-100,100), yrange=(0,1))
sage: matrix_plot(random_matrix(RDF, 2, 2), xrange=(-.01, .01), yrange=(0,1))
```

which both give extremely narrow plots - because of the aspect_ratio scaling technique, maybe?   Anyway, somehow it seems like the idea of a custom range is for labelling purposes (and that's a nice feature), not necessarily for scaling purposes.  If it's at least partly for labelling purposes only, a 2x2 matrix probably shouldn't look like this; an aspect ratio of more or less 1 seems most reasonable in that case.


---

Comment by kcrisman created at 2009-11-16 16:20:23

Assuming that #1431 is finished any time soon, an update should use it for implementation.


---

Comment by kcrisman created at 2010-07-23 01:56:14

#9578 might also be relevant.
