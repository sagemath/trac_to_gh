# Issue 8004: region_plot does not handle lambda functions

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-01-19 22:59:50

Assignee: was

CC:  kcrisman


```
sage: sage: region_plot(lambda x,y: x>y, (-4,4), (-4,4))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/devel/sage-main/sage/<ipython console> in <module>()

/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
    136                 options['__original_opts'] = kwds
    137             options.update(kwds)
--> 138             return func(*args, **options)
    139 
    140         

/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/local/lib/python2.6/site-packages/sage/plot/contour_plot.pyc in region_plot(f, xrange, yrange, plot_points, incol, outcol, bordercol, borderstyle, borderwidth)
    561         f = [f]
    562 
--> 563     f = [equify(g) for g in f]
    564 
    565     g, ranges = setup_for_eval_on_grid(f, [xrange, yrange], plot_points)

/mnt/usb1/scratch/jason/sage-4.3.1.rc1-x86_64-Linux/local/lib/python2.6/site-packages/sage/plot/contour_plot.pyc in equify(f)
    626     import operator
    627     from sage.calculus.all import symbolic_expression
--> 628     op = f.operator()
    629     if op is operator.gt or op is operator.ge:
    630         return symbolic_expression(f.rhs() - f.lhs())

AttributeError: 'function' object has no attribute 'operator'
```



---

Attachment


---

Comment by jason created at 2010-01-20 00:14:02

Changing status from new to needs_review.


---

Comment by jason created at 2010-01-20 00:14:02

This also resolves #7807


---

Comment by kcrisman created at 2010-01-20 02:33:45

See also #4677 for a related issue.


---

Comment by rossk created at 2010-01-31 09:37:37

Changing status from needs_review to positive_review.


---

Comment by rossk created at 2010-01-31 09:37:37

Despite a depreciation message, this worked as expected for all the cases I tried.


```
sage: var('x y')
(x, y)

sage: region_plot(lambda x,y: x>y, (-4,4), (-4,4)) # works

sage: region_plot([lambda x,y: x>y, lambda x,y: x^2+y^2<10], (-4,4), (-4,4)) # a list of lambdas also work

#
# Tried mixing the forms of the functions (one being a lamba and one an expression)
# - got a depreciation message! (But still displayed the plot correctly) 
#
sage: region_plot([lambda x,y: x>y, x^2+y^2<10], (-4,4), (-4,4))
/home/ross/sage-4.3.2.alpha0/local/lib/python2.6/site-packages/sage/plot/contour_plot.py:569: DeprecationWarning: Unnamed ranges for more than one variable is deprecated and will be removed from a future release of Sage; you can used named ranges instead, like (x,0,2)
  g, ranges = setup_for_eval_on_grid(f, [xrange, yrange], plot_points)

# ...but parentheses also produced the same plot correctly without the message 
sage: region_plot([(lambda x,y: x>y), (x^2+y^2<10)], (-4,4), (-4,4))

# tried the former example again - no depreciated message this time (!?)
# (Does sage only show depreciations once?) 
sage: region_plot([lambda x,y: x>y, x^2+y^2<10], (-4,4), (-4,4))

# this worked too
sage: region_plot([lambda x,y: x>y, lambda x,y: x^2+y^2<10], (-4,4), (-4,4), aspect_ratio=1)
```



---

Comment by mpatel created at 2010-02-10 15:27:55

I've refreshed the commit string to

```
#8004: Make region_plot accept lambda functions
```

in the queue for 4.3.3.alpha0.


---

Comment by mpatel created at 2010-02-11 14:58:13

Resolution: fixed
