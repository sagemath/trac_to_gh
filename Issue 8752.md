# Issue 8752: Can't evaluate numerically symbolic expression resulting from integral().

Issue created by migration from Trac.

Original creator: lfousse

Original creation time: 2010-04-23 15:33:48

Assignee: burcin

Keywords: integral, numerical conversion

Consider the following (in sage 4.3.5):


```
sage: integral(exp(-x^2), x, 17, 42)   
-1/2*sqrt(pi)*erf(17) + 1/2*sqrt(pi)*erf(42)
sage: N(-1/2*sqrt(pi)*erf(17) + 1/2*sqrt(pi)*erf(42))
0.000000000000000
```

But:

```
sage: N(integral(exp(-x^2), x, 17, 42))              
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-4.3.5/<ipython console> in <module>()

/opt/sage-4.3.5/local/lib/python2.6/site-packages/sage/misc/functional.pyc in numerical_approx(x, prec, digits)
   1161             prec = int((digits+1) * 3.32192) + 1
   1162     try:
-> 1163         return x.numerical_approx(prec)
   1164     except AttributeError:
   1165         from sage.rings.complex_double import is_ComplexDoubleElement

/opt/sage-4.3.5/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17043)()

TypeError: cannot evaluate symbolic expression numerically
```



---

Comment by jason created at 2010-04-23 18:21:47

Resolution: duplicate


---

Comment by jason created at 2010-04-23 18:21:47

In 4.4.alpha1:


```
sage: N(integral(exp(-x^2), x, 17, 42))   
0.000000000000000
```


I believe this was taken care of in #3863.


---

Comment by lfousse created at 2010-04-25 09:18:50

Indeed, it is fixed. Thanks for the prompt reply, sorry for the duplicate.
