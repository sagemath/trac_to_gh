# Issue 9393: symbolic sum cannot handle python ints

Issue created by migration from https://trac.sagemath.org/ticket/9393

Original creator: burcin

Original creation time: 2010-06-30 11:52:27

Assignee: burcin

CC:  whuss mjo

Reported by Tobias Katz on sage-support:


```
sage: sum(x, x, 1r, 5r)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
.../<ipython console> in <module>()
.../local/lib/python2.6/site-packages/sage/misc/functional.pyc in symbolic_sum(expression, *args, **kwds)
    657     """
    658     if hasattr(expression, 'sum'):
--> 659         return expression.sum(*args, **kwds)
    660     elif len(args) <= 1:
    661         return sum(expression, *args)

.../local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.sum (sage/symbolic/expression.cpp:28895)()

.../local/lib/python2.6/site-packages/sage/calculus/calculus.pyc in symbolic_sum(expression, v, a, b, algorithm)
    482 
    483     if algorithm == 'maxima':
--> 484         sum  = "'sum(%s, %s, %s, %s)" % tuple([repr(expr._maxima_()) for expr in (expression, v, a, b)])
    485         try:
    486             result = maxima.simplify_sum(sum)

AttributeError: 'int' object has no attribute '_maxima_'
```



---

Comment by mjo created at 2012-01-09 04:27:31

Add a doctest for the fix.


---

Attachment

This is fixed, so I've added a doctest for it.


---

Comment by mjo created at 2012-01-09 04:28:53

Changing status from new to needs_review.


---

Comment by burcin created at 2012-01-16 09:12:27

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2012-01-16 09:12:27

Looks good to me.

Thanks for looking into this.


---

Comment by jdemeyer created at 2012-01-18 08:13:41

Resolution: fixed
