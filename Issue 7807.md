# Issue 7807: region_plot does not pass extra arguments to show

Issue created by migration from https://trac.sagemath.org/ticket/7807

Original creator: jason

Original creation time: 2010-01-01 18:19:43

Assignee: was

This is inconsistent with other plotting functions.


```
sage: region_plot([x^2+y^2<1, x<y], (x,-2,2), (y,-2,2),aspect_ratio=1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/tiny/2531/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/downloads/sage-4.3/local/lib/python2.6/site-packages/sage/plot/misc.pyc in wrapper(*args, **kwds)
    136                 options['__original_opts'] = kwds
    137             options.update(kwds)
--> 138             return func(*args, **options)
    139 
    140         

TypeError: region_plot() got an unexpected keyword argument 'aspect_ratio'
```



---

Comment by jason created at 2010-01-20 00:14:14

The patch at #8004 resolves this.


---

Comment by jason created at 2010-01-20 00:14:21

Changing status from new to needs_review.


---

Comment by rossk created at 2010-01-31 06:20:57

Changing status from needs_review to positive_review.


---

Comment by rossk created at 2010-01-31 06:20:57


```
# works as advertised
sage: region_plot([x^2+y^2<1, x<y], (x,-2,2), (y,-2,2),aspect_ratio=1)  

# (Correctly) doesnt complain about a single function
sage: region_plot([x^2+y^2<1], (x,-2,2), (y,-2,2),aspect_ratio=1) 

# using many functions is ok
sage: region_plot([x^2+y^2<1, x<y, x>-1/2, y>0], (x,-2,2), (y,-2,2),aspect_ratio=1)

# displays a portion of the last example properly
sage: region_plot([x^2+y^2<1, x<y, x>-1/2, y>0], (x,0,2), (y,-2,2),aspect_ratio=1) 

# a little computer art - my picture of a whale ;-) 
sage: region_plot([x^2+y^2<10, y< sin(x)], (x,-5,5), (y,-4,4),aspect_ratio=1)
```



---

Comment by mpatel created at 2010-02-11 14:58:55

Fixed by #8004.


---

Comment by mpatel created at 2010-02-11 14:58:55

Resolution: fixed
