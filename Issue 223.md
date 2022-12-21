# Issue 223: problem plotting piecewise defined functions

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-01-27 08:19:21

Assignee: was



```
x = PolynomialRing(RationalField(), 'x').gen()
f1 = x^0
f2 = 1-x
f3 = 2*x
f4 = 10*x-x^2
f = Piecewise([[(0,1),f1],[(1,2),f2],[(2,3),f3],[(3,10),f4]])
plot(f)
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/was/sage_notebook/worksheets/doc_browser/code/35.py", line 10, in <module>
    exec compile(ur'plot(f)' + '\n', '', 'single')
  File "/Users/was/", line 1, in <module>
    
  File "/Users/was/s/local/lib/python2.5/site-packages/sage/plot/plot.py", line 2132, in __call__
    G = funcs.plot(xmin=xmin, xmax=xmax, **kwds)
  File "/Users/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 707, in plot
    return sum([plot(p[1], p[0][0], p[0][1], **kwds ) for p in self.list()])
TypeError: __call__() got multiple values for keyword argument 'xmin'
```



---

Comment by was created at 2007-01-27 08:19:39

Changing priority from major to minor.


---

Comment by was created at 2007-01-27 08:19:39

Changing component from algebraic geometry to calculus.


---

Comment by mabshoff created at 2007-08-21 12:36:39

Resolution: worksforme


---

Comment by mabshoff created at 2007-08-21 12:36:39

With Sage 2.8.2pre this works for me:

```
sage: x = PolynomialRing(RationalField(), 'x').gen()
sage: f1 = x^0
sage: f2 = 1-x
sage: f3 = 2*x
sage: f4 = 10*x-x^2
sage: f = Piecewise([[(0,1),f1],[(1,2),f2],[(2,3),f3],[(3,10),f4]])
sage: plot(f)
Graphics object consisting of 4 graphics primitives
```

