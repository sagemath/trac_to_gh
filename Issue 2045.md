# Issue 2045: unfriendly error message when plotting square roots of a function that is negative.

archive/issues_002045.json:
```json
{
    "body": "Assignee: was\n\nThis came up on IRC.  The error (something about floats being unsubscriptable) does not indicate that the problem is that you are trying to plot the square root of a function that is negative in the plot interval.  We should probably have a more friendly error message.\n\n\n```\nsage: plot((1-x^2)^(0.5),(x,1,10))\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/home/grout/download/sage-2.10.1.rc5/<ipython console> in <module>()\n\n/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)\n   3334             del kwds['show']\n   3335         if hasattr(funcs, 'plot'):\n-> 3336             G = funcs.plot(*args, **kwds)\n   3337         # if we are using the generic plotting method\n   3338         else:\n\n/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)\n    667         else:\n    668             f = self.function(param)\n--> 669         return plot(f, *args, **kwds)\n    670\n    671     def __lt__(self, right):\n\n/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)\n   3334             del kwds['show']\n   3335         if hasattr(funcs, 'plot'):\n-> 3336             G = funcs.plot(*args, **kwds)\n   3337         # if we are using the generic plotting method\n   3338         else:\n\n/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/calculus/calculus.py in plot(self, *args, **kwds)\n    667         else:\n    668             f = self.function(param)\n--> 669         return plot(f, *args, **kwds)\n    670\n    671     def __lt__(self, right):\n\n/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/plot/plot.py in __call__(self, funcs, *args, **kwds)\n   3343             # if there is one extra arg, then it had better be a tuple\n   3344             elif n == 1:\n-> 3345                 G = self._call(funcs, *args, **kwds)\n   3346             elif n == 2:\n   3347             # if ther eare two extra args, then pull them out and pass them as a tuple\n\n/home/grout/download/sage-2.10.1.rc5/local/lib/python2.5/site-packages/sage/plot/plot.py in _call(self, funcs, xrange, parametric, polar, label, **kwds)\n   3419         del options['plot_division']\n   3420         while i < len(data) - 1:\n-> 3421             if abs(data[i+1][1] - data[i][1]) > max_bend:\n   3422                 x = (data[i+1][0] + data[i][0])/2\n   3423                 try:\n\n<type 'exceptions.TypeError'>: 'float' object is unsubscriptable\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2045\n\n",
    "created_at": "2008-02-04T17:35:10Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "unfriendly error message when plotting square roots of a function that is negative.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2045",
    "user": "jason"
}
```
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



Issue created by migration from https://trac.sagemath.org/ticket/2045





---

archive/issue_comments_013247.json:
```json
{
    "body": "Or maybe we could even just put up a blank plot, but somehow print out a warning too that you are trying to plot imaginary numbers.",
    "created_at": "2008-02-04T17:36:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2045#issuecomment-13247",
    "user": "jason"
}
```

Or maybe we could even just put up a blank plot, but somehow print out a warning too that you are trying to plot imaginary numbers.



---

archive/issue_comments_013248.json:
```json
{
    "body": "This is a dupe of #2038.",
    "created_at": "2008-02-04T18:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2045#issuecomment-13248",
    "user": "was"
}
```

This is a dupe of #2038.



---

archive/issue_comments_013249.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-02-04T18:20:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2045",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2045#issuecomment-13249",
    "user": "was"
}
```

Resolution: duplicate
