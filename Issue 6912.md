# Issue 6912: parametric regions

Issue created by migration from https://trac.sagemath.org/ticket/6912

Original creator: jason

Original creation time: 2009-09-10 07:15:44

Assignee: was

Mathematica can plot parametric regions:

```
ParametricPlot[r^2 { Sqrt[t] Cos[t], Sin[t]}, {t, 0, 3 Pi/2}, {r, 1, 2}]
```


See http://reference.wolfram.com/mathematica/ref/ParametricPlot.html for output.  We should be able to do this too.


---

Comment by chapoton created at 2019-06-15 07:25:22

Still not done

```
sage: var('x,y')
(x, y)
sage: parametric_plot((x,y),(x,-1,1),(y,-1,1))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-5-fad28512a87c> in <module>()
----> 1 parametric_plot((x,y),(x,-Integer(1),Integer(1)),(y,-Integer(1),Integer(1)))

/home/chapoton/sage3/local/lib/python3.7/site-packages/sage/misc/decorators.py in wrapper(*args, **kwds)
    491                 options['__original_opts'] = kwds
    492             options.update(kwds)
--> 493             return func(*args, **options)
    494 
    495         #Add the options specified by @options to the signature of the wrapped

/home/chapoton/sage3/local/lib/python3.7/site-packages/sage/plot/plot.py in parametric_plot(funcs, *args, **kwargs)
   2623         return sage.plot.plot3d.parametric_plot3d.parametric_plot3d(funcs, *args, **kwargs)
   2624     else:
-> 2625         raise ValueError("the number of functions and the number of variable ranges is not a supported combination for a 2d or 3d parametric plots")
   2626 
   2627 @options(aspect_ratio=1.0)

ValueError: the number of functions and the number of variable ranges is not a supported combination for a 2d or 3d parametric plots
```

