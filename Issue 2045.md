# Issue 2045: unfriendly error message when plotting square roots of a function that is negative.

Issue created by migration from https://trac.sagemath.org/ticket/2045

Original creator: jason

Original creation time: 2008-02-04 17:35:10

Assignee: was

This came up on IRC.  The error (something about floats being unsubscriptable) does not indicate that the problem is that you are trying to plot the square root of a function that is negative in the plot interval.  We should probably have a more friendly error message.


```
sage: plot((1-x^2)^(0.5),(x,1,10))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/home/grout/download/sage-2.10.1.rc5/<ipython console> in <module>()

/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   3334             del kwds['show']
   3335         if hasattr(funcs, 'plot'):
-> 3336             G = funcs.plot(*args, **kwds)
   3337         # if we are using the generic plotting method
   3338         else:

/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)
    667         else:
    668             f = self.function(param)
--> 669         return plot(f, *args, **kwds)
    670
    671     def __lt__(self, right):

/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   3334             del kwds['show']
   3335         if hasattr(funcs, 'plot'):
-> 3336             G = funcs.plot(*args, **kwds)
   3337         # if we are using the generic plotting method
   3338         else:

/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)
    667         else:
    668             f = self.function(param)
--> 669         return plot(f, *args, **kwds)
    670
    671     def __lt__(self, right):

/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)
   3343             # if there is one extra arg, then it had better be a tuple
   3344             elif n == 1:
-> 3345                 G = self._call(funcs, *args, **kwds)
   3346             elif n == 2:
   3347             # if ther eare two extra args, then pull them out and pass them as a tuple

/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/plot/plot.py in _call(self, funcs, xrange, parametric, polar, label, **kwds)
   3419         del options['plot_division']
   3420         while i < len(data) - 1:
-> 3421             if abs(data[i+1][1] - data[i][1]) > max_bend:
   3422                 x = (data[i+1][0] + data[i][0])/2
   3423                 try:

<type 'exceptions.TypeError'>: 'float' object is unsubscriptable
```




---

Comment by jason created at 2008-02-04 17:36:54

Or maybe we could even just put up a blank plot, but somehow print out a warning too that you are trying to plot imaginary numbers.


---

Comment by was created at 2008-02-04 18:20:34

This is a dupe of #2038.


---

Comment by was created at 2008-02-04 18:20:34

Resolution: duplicate
