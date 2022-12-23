# Issue 6947: [with patch, needs review] make complex_plot() work for for fast_callable functions

Issue created by migration from https://trac.sagemath.org/ticket/6947

Original creator: bober

Original creation time: 2009-09-16 21:08:42

Assignee: was

This current behavior of Sage demonstrates a bug, which probably also affects other complex valued functions that cannot be converted into real valued functions.



```
sage: f(x) = x^2                               
sage: g = fast_callable(f, domain=CC, vars='x')
sage: P = complex_plot(f, (-10, 10), (-10, 10))
sage: Q = complex_plot(g, (-10, 10), (-10, 10))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (35, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/bober/.sage/temp/bober/1740/_home_bober__sage_init_sage_0.py in <module>()

/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
    133                 options['__original_opts'] = kwds
    134             options.update(kwds)
--> 135             return func(*args, **options)
    136 
    137         

/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/complex_plot.so in sage.plot.complex_plot.complex_plot (sage/plot/complex_plot.c:4104)()

/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/plot.pyc in setup_for_eval_on_grid(v, xrange, yrange, plot_points)
   2874             from sage.plot.plot3d.parametric_plot3d import adapt_to_callable
   2875             if xvar is None:
-> 2876                 k, _ = adapt_to_callable([f], 2)
   2877                 g.append(k[0])
   2878             else:

/home/bober/sage/local/lib/python2.6/site-packages/sage/plot/plot3d/parametric_plot3d.pyc in adapt_to_callable(f, nargs)
    649     except TypeError:
    650         vars = ()
--> 651         f = [fast_float_constant(x) for x in f]
    652     
    653     if nargs is not None and len(vars) != nargs:

/home/bober/sage/local/lib/python2.6/site-packages/sage/ext/fast_eval.so in sage.ext.fast_eval.fast_float_constant (sage/ext/fast_eval.c:8030)()

/home/bober/sage/local/lib/python2.6/site-packages/sage/ext/fast_eval.so in sage.ext.fast_eval.FastDoubleFunc.__init__ (sage/ext/fast_eval.c:3492)()

TypeError: a float is required
```



The attached patch fixes this. (It is a one character fix, but someone who knows the plotting code should make sure it is the right fix.)



---

Attachment

This looks great.  The reviewer patch just adds the tests above as doctests.

As another ticket, complex_plot really needs to convert it's arguments to fast_callable(..., domain=CDF).  See #6985 for timing examples.


---

Comment by jason created at 2009-09-22 14:34:36

apply on top of previous patch


---

Comment by mvngu created at 2009-09-23 07:10:10

Resolution: fixed


---

Attachment


---

Comment by mvngu created at 2009-09-27 09:51:02

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
