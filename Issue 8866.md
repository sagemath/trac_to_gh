# Issue 8866: preparse vector-valued functions and derivatives

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-05-04 03:14:57

Assignee: burcin

CC:  mhansen burcin kcrisman rbeezer

Here is a rough patch which enables the following:


```
sage: T(r,theta)=[r*cos(theta),r*sin(theta)]
sage: T
((r, theta) |--> r*cos(theta), (r, theta) |--> r*sin(theta))
sage: T.diff() # Jacobian matrix
[   (r, theta) |--> cos(theta) (r, theta) |--> -r*sin(theta)]
[   (r, theta) |--> sin(theta)  (r, theta) |--> r*cos(theta)]
sage: diff(T) # Jacobian matrix
[   (r, theta) |--> cos(theta) (r, theta) |--> -r*sin(theta)]
[   (r, theta) |--> sin(theta)  (r, theta) |--> r*cos(theta)]
sage: T.diff().det() # Jacobian 
(r, theta) |--> r*sin(theta)^2 + r*cos(theta)^2

sage: f(x,y)=x^2+y
sage: f.diff() # gradient
((x, y) |--> 2*x, (x, y) |--> 1)
sage: f.diff().diff() # Hessian matrix
[(x, y) |--> 2 (x, y) |--> 0]
[(x, y) |--> 0 (x, y) |--> 0]
sage: r(t)=[cos(t),sin(t)]
sage: parametric_plot(r(t), (t,0,2*pi))

sage: # multivariable 2nd derivative test
sage: f(x,y)=x^2*y+y^2+y
sage: f.diff() # gradient
((x, y) |--> 2*x*y, (x, y) |--> x^2 + 2*y + 1)
sage: solve(list(f.diff()),[x,y])
[[x == -I, y == 0], [x == I, y == 0], [x == 0, y == (-1/2)]]
sage: f.diff(2)  # Hessian matrix
[(x, y) |--> 2*y (x, y) |--> 2*x]
[(x, y) |--> 2*x   (x, y) |--> 2]
sage: f.diff(2)(x=0,y=-1/2)
[-1  0]
[ 0  2]
sage: f.diff(2)(x=0,y=-1/2).eigenvalues()
[-1, 2]
sage: # we have a saddle point
```




---

Comment by jason created at 2010-05-04 03:18:05

Changing status from new to needs_work.


---

Comment by jason created at 2010-05-04 03:18:05

Right now, all the docs are wrong or missing for the added functionality.


---

Attachment


---

Comment by jason created at 2010-05-04 04:00:41

I added docs for each functionality that changed.


---

Comment by jason created at 2010-05-04 04:00:41

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-05-04 05:12:26

make ptestlong appears to pass on 4.4.1 (ubuntu 64-bit).


---

Comment by rbeezer created at 2010-05-05 05:07:00

I'm running tests right now.  In the meantime, could this be less ugly?  I realize that the naked '4's are not callable, so there is the deprecation warning, but the error warning seems severe.


```
sage: d=matrix(SR, [This is the Trac macro *4, 4* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#4, 4-macro))
sage: d(3)
/sage/dev/local/lib/python2.6/site-packages/IPython/iplib.py:2073: DeprecationWarning: Substitution using function-call syntax and unnamed arguments is deprecated and will be removed from a future release of Sage; you can use named arguments instead, like EXPR(x=..., y=...)
  exec code_obj in self.user_global_ns, self.user_ns
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/sage/dev/<ipython console> in <module>()

/sage/dev/local/lib/python2.6/site-packages/sage/matrix/matrix_symbolic_dense.so in sage.matrix.matrix_symbolic_dense.Matrix_symbolic_dense.__call__ (sage/matrix/matrix_symbolic_dense.c:3956)()

ValueError: the number of arguments must be less than or equal to 0
```


I didn't know you could create a vector space of functions.  Complete with a basis.  ;-)


```
sage: g(x,y)=x^2+y^3
sage: g
(x, y) |--> x^2 + y^3
sage: grad=g.diff()
sage: grad
((x, y) |--> 2*x, (x, y) |--> 3*y^2)
sage: grad.parent()
Vector space of dimension 2 over Callable function ring with arguments (x, y)
sage: grad.parent().basis()
[
((x, y) |--> 1, (x, y) |--> 0),
((x, y) |--> 0, (x, y) |--> 1)
]
```



---

Comment by jason created at 2010-05-05 06:17:25

Replying to [comment:4 rbeezer]:

> I'm running tests right now.  In the meantime, could this be less ugly?  I realize that the naked '4's are not callable, so there is the deprecation warning, but the error warning seems severe. 

That's stemming from this, of course:


```

sage: SR(4)(2)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/home/jason/<ipython console> in <module>()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.__call__ (sage/symbolic/expression.cpp:15477)()

/home/jason/sage/local/lib/python2.6/site-packages/sage/symbolic/ring.so in sage.symbolic.ring.SymbolicRing._call_element_ (sage/symbolic/ring.cpp:6523)()

ValueError: the number of arguments must be less than or equal to 0
```


I don't know what should be done about that to make it prettier.  Usually you wouldn't "call" an integer by itself (as just a symbolic integer is not a function...)

Note that making matrices callable is just extending the existing behavior for vectors.


>I didn't know you could create a vector space of functions.  Complete with a basis.  ;-) 

Yes, interesting.  That stems from callable expressions being just normal expressions with a bit of extra information (default variable order for calls).  Of course, it gave you back a basis for symbolic expressions.


---

Comment by rbeezer created at 2010-05-06 03:50:33

Replying to [comment:5 jason]:
> I don't know what should be done about that to make it prettier.

Me either.  ;-)  I guess I found it odd that there was a deprecation warning, then a failure.  But maybe that's just the way it goes.


---

Comment by rbeezer created at 2010-05-06 03:51:39

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-05-06 03:51:39

This all checks out fine: builds and runs, passes all tests, documentation is fine.

So, positive review.


---

Comment by mvngu created at 2010-05-08 04:21:44

same as previous but with ticket number in commit message


---

Comment by mvngu created at 2010-05-08 22:14:17

Resolution: fixed


---

Attachment
