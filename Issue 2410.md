# Issue 2410: parametric_plot and constants

Issue created by migration from https://trac.sagemath.org/ticket/2410

Original creator: jbmohler

Original creation time: 2008-03-06 20:48:30

Assignee: was

This is a companion to #2409


```
sage: parametric_plot((t^2,t),-12,12)
```

works as expected, but 

```
sage: parametric_plot((1,t),-12,12)
...
<type 'exceptions.TypeError'>: 'float' object is unsubscriptable
```

does not.

More generally, I would like to see the following syntax supported 

```
sage: parametric_plot((1,t),(t,-12,12))
```

which is much cleaner mathematically (no hidden reliance on variable name 't') and is also very analogous to 

```
sage: plot(t,(t,-12,12))
```




---

Comment by jason created at 2008-08-25 21:53:43

For reference:

parametric_plot3d automatically calls fast_float on its arguments correctly, so parametric_plot3d((1,t,2), (t,-1,3)), for example, just works.

Why are we not calling fast_float on functions in plot() or parametric_plot?  Probably because noone has had time to implement it; contour plots and vector plots both do it.  I'll open a new ticket.

Here, I'll post a patch which corrects a bug in how exceptions are handled in plot.  Currently, the TypeError that is being triggered is then ignored when plot tries to access the non-existent data point (the data[i][1] line).  This changes the error in this case from a nonsensical indexing error to a sensible "Can't call an Integer" error (from trying to evaluate 1(-12).


---

Attachment


---

Comment by jason created at 2008-08-25 22:02:22

See #3952 for the fast_float request.


---

Comment by mhansen created at 2008-08-26 01:59:46

The other issues will be fixed in #3952.


---

Attachment

Apply trac_2140.patch _after_ #3853


---

Comment by mabshoff created at 2008-08-26 03:44:48

Merged trac_2140.patch in Sage 3.1.2.alpha1


---

Comment by mabshoff created at 2008-08-26 03:44:48

Resolution: fixed
