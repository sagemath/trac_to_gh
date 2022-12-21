# Issue 6592: minimize_constrained only takes lambda functions as constraints

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-07-22 15:31:31

Assignee: jkantor

CC:  mforets

e.g.:

```
sage: var('x y')
sage: f = (100 - x) + (1000 - y)
sage: c = x + y - 479 # > 0
sage: minimize_constrained(f,[c],[100,300])
Traceback (most recent call last):
...
UnboundLocalError: local variable 'min' referenced before assignment
```



---

Comment by jason created at 2010-03-17 05:12:48

More clearly, here's the "bug" part of this.  The documentation says that the function takes a symbolic function, but clearly does not:


```
sage: f(x,y) = (100 - x) + (1000 - y)
sage: c = x + y - 479 
sage: minimize_constrained(f,[c],[100,300])
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)

/home/grout/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.6/site-packages/sage/numerical/optimize.pyc in minimize_constrained(func, cons, x0, gradient, algorithm, **args)
    408     elif isinstance(cons, function_type):
    409         min= optimize.fmin_cobyla(f,x0,cons,iprint=0,**args)
--> 410     return vector(RDF,min)
    411 
    412     

UnboundLocalError: local variable 'min' referenced before assignment


```



---

Comment by mforets created at 2017-05-28 05:34:23

New commits:


---

Comment by mforets created at 2017-05-28 05:34:36

Changing status from new to needs_review.


---

Comment by mforets created at 2017-05-28 07:21:59

This patch adds code branches for the cases when the constraints are one or more symbolic expressions. There is also some cleanup (PEP-8).


---

Comment by tscrim created at 2017-07-11 03:53:57

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2017-07-11 03:53:57

The code make sense and fixes the error.


---

Comment by mforets created at 2017-07-11 06:13:43

Replying to [comment:10 tscrim]:
> The code make sense and fixes the error.

thanks for reviewing :)


---

Comment by vbraun created at 2017-07-26 22:13:49

Resolution: fixed
