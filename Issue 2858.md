# Issue 2858: parametric_plot3d doesn't like "-u"

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-08 21:08:25

Assignee: was

The following two plots should give the same thing.


```
sage: parametric_plot3d((u,-u,v), (-10,10),(-10,10))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/grout/.sage/sage_notebook/worksheets/admin/43/code/101.py", line 6, in <module>
    parametric_plot3d((u,-u,v), (-Integer(10),Integer(10)),(-Integer(10),Integer(10)))
  File "/home/grout/sage/local/lib/python2.5/site-packages/sympy/plotting/", line 1, in <module>
    
  File "/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py", line 362, in parametric_plot3d
    G = parametric_plot3d_surface(f, urange, vrange, plot_points, **kwds)
  File "/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py", line 423, in parametric_plot3d_surface
    g, (u,v) = adapt_to_callable(f, 2)
  File "/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py", line 492, in adapt_to_callable
    return fast_float(f, *vars), vars
  File "fast_eval.pyx", line 1276, in sage.ext.fast_eval.fast_float
  File "fast_eval.pyx", line 1288, in sage.ext.fast_eval.fast_float
  File "/home/grout/sage/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 5102, in _fast_float_
    raise ValueError, "free variable: %s" % self._name
ValueError: free variable: u

sage: parametric_plot3d((u,(-2*u+2)/2-1,v), (-10,10),(-10,10))
(this works)
```




---

Comment by mabshoff created at 2008-04-09 01:02:53

Resolution: duplicate


---

Comment by mabshoff created at 2008-04-09 01:02:53

This is a duplicate of #1877. I think it should be possible to use a variable mutliple times in the range, i.e. `x,x` or also `x,-x`. Since this description is far from precise, i.e. one would never find it looking for the issue, I am closing this.

Jason: feel free to reopen if you disagree. 

Cheers,

Michael


---

Comment by jason created at 2008-04-09 01:30:51

Resolution changed from duplicate to 


---

Comment by jason created at 2008-04-09 01:30:51

Changing status from closed to reopened.


---

Comment by jason created at 2008-04-09 01:30:51

To my understanding, the issue in #1877 was the specifying of the same variable in two different ranges.  This issue is different: when I use "-u", I get an error, but when I use an expression that is equivalent to "-u", I don't get an error.  In either case, I'm not specifying two of the same variable for the ranges.

I think these issues are different.  They may be symptoms of the same thing, but I doubt it.


---

Comment by jason created at 2008-04-09 01:38:03

Changing the issue title to be more descriptive.

To elaborate on the reopening: the issue here is not with the ranges (to my knowledge, it isn't even possible to specify variables for the ranges in parametric_plot3d).  The issue here is with the components of the function being plotted.


---

Comment by mabshoff created at 2008-04-09 01:51:05

Ok, agreed that this is a different bug than #1877:

```
sage: var('u v t')
(u, v, t)
sage: parametric_plot3d((u,-v,t), (-10,10),(-10,10))
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/<ipython console> in <module>()

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py in parametric_plot3d(f, urange, vrange, plot_points, **kwds)
    360         if plot_points == "automatic":
    361             plot_points = [40,40]
--> 362         G = parametric_plot3d_surface(f, urange, vrange, plot_points, **kwds)
    363     G._set_extra_kwds(kwds)
    364     return G

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py in parametric_plot3d_surface(f, urange, vrange, plot_points, **kwds)
    421
    422         try:
--> 423             g, (u,v) = adapt_to_callable(f, 2)
    424         except TypeError:
    425             g = tuple(f)

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/plot/plot3d/parametric_plot3d.py in adapt_to_callable(f, nargs)
    488
    489     if nargs is not None and len(vars) != nargs:
    490         vars = (vars + ('_',)*nargs)[:nargs]
    491
--> 492     return fast_float(f, *vars), vars

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/fast_eval.pyx in sage.ext.fast_eval.fast_float()

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/fast_eval.pyx in sage.ext.fast_eval.fast_float()

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _fast_float_(self, *vars)
   4598             1.0
   4599         """
-> 4600         fops = [op._fast_float_(*vars) for op in self._operands]
   4601         return self._operator(*fops)
   4602

/scratch/mabshoff/release-cycle/sage-3.0.alpha3/local/lib/python2.5/site-packages/sage/calculus/calculus.py in _fast_float_(self, *vars)
   5112             return fast_float.fast_float_constant(float(self))
   5113         except TypeError:
-> 5114             raise ValueError, "free variable: %s" % self._name
   5115
   5116     def _recursive_sub(self, kwds):

<type 'exceptions.ValueError'>: free variable: v
sage:
```

Using u twice in the range might have obscured the real bug from my POV. Mea culpa.

+1 on the better description.

Cheers,

Michael


---

Comment by jason created at 2008-04-09 02:11:32

The problem seems to be in parametric_plot3d.py in adapt_to_callable, in the line "s=sum(f)".  If there is a u and a -u as components of f, then sum(f) cancels these and the variable disappears.


---

Attachment

mike found one bug which this fixes.


---

Attachment


---

Comment by mhansen created at 2009-01-24 11:46:02

Looks good to me.


---

Comment by mabshoff created at 2009-01-28 14:11:00

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 14:11:00

Merged both patches in Sage 3.3.alpha3
