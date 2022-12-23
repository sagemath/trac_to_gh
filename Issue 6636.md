# Issue 6636: Simplification of factorials and binomial coefficients is not very good

Issue created by migration from https://trac.sagemath.org/ticket/6636

Original creator: jbandlow

Original creation time: 2009-07-27 11:34:50

CC:  jbandlow burcin mhansen

Keywords: symbolics, factorials, binomial coefficients

Maple can simplify all but the first of the following examples:


```
%maple
print(simplify(binomial(n,2)+binomial(n+1,2)));
print(simplify(factorial(n)/factorial(n-2)/2 + factorial(n+1)/factorial(n-1)/2));
print(simplify(factorial(n+1)/factorial(n)));
print(simplify(binomial(n,k)*factorial(k)*factorial(n-k)));
```


returns

```
binomial(n,2)+binomial(n+1,2)
n^2
n+1
n!
```


Sage can simplify only the first:

```
var('n,k')
print (binomial(n,2) + binomial(n+1,2)).simplify_full()
print (factorial(n)/factorial(n-2)/2 + factorial(n+1)/factorial(n)/2).simplify_full()
print (factorial(n+1)/factorial(n)).simplify_full()
print (binomial(n,k)*factorial(k)*factorial(n-k)).simplify_full()
```


returns

```
n^2
1/2*(factorial(n - 2)*factorial(n + 1) + factorial(n)^2)/(factorial(n - 2)*factorial(n))
factorial(n + 1)/factorial(n)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/jason/.sage/sage_notebook/worksheets/admin/10/code/49.py", line 11, in <module>
    exec compile(ur'print (binomial(n,k)*factorial(k)*factorial(n-k)).simplify_full()' + '\n', '', 'single')
  File "", line 1, in <module>
    
  File "expression.pyx", line 4837, in sage.symbolic.expression.Expression.simplify_full (sage/symbolic/expression.cpp:19979)
  File "expression.pyx", line 4864, in sage.symbolic.expression.Expression.simplify_trig (sage/symbolic/expression.cpp:20076)
  File "expression.pyx", line 418, in sage.symbolic.expression.Expression._maxima_ (sage/symbolic/expression.cpp:3415)
  File "sage_object.pyx", line 364, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3384)
  File "sage_object.pyx", line 451, in sage.structure.sage_object.SageObject._maxima_init_ (sage/structure/sage_object.c:5065)
  File "expression.pyx", line 443, in sage.symbolic.expression.Expression._interface_init_ (sage/symbolic/expression.cpp:3544)
  File "/home/jason/sage-4.0/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py", line 214, in __call__
    return self.arithmetic(ex, operator)
  File "/home/jason/sage-4.0/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py", line 497, in arithmetic
    args = ["(%s)"%self(op) for op in ex.operands()]
  File "/home/jason/sage-4.0/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py", line 206, in __call__
    operator = ex.operator()
  File "expression.pyx", line 3088, in sage.symbolic.expression.Expression.operator (sage/symbolic/expression.cpp:15127)
RuntimeError: cannot find SFunction in table
```





---

Comment by kcrisman created at 2009-09-02 14:58:54

A related discussion on sage-devel is [http://groups.google.com/group/sage-devel/browse_thread/thread/58db110fc55b11e5](http://groups.google.com/group/sage-devel/browse_thread/thread/58db110fc55b11e5).

The lack of simplification is a bug, or at least very poorly exposed functionality, in Maxima.  One would think that simplify would include this... but instead one needs to expose Maxima's *minfactorial*:

```
(%i1) fullratsimp(factorial(n)/factorial(n-1));
                                      n!
(%o1)                              --------
                                   (n - 1)!
(%i2) minfactorial(factorial(n)/factorial(n-1));
(%o2)                                  n
```

This should not be hard to add to simplify_full, though.

Also note that the last issue is addressed by #6197.


---

Comment by kcrisman created at 2009-09-02 17:30:34

The following patch should fix all of the issues on this ticket - Maxima has quite a bit of simplifying capability, but prefers to leave things unsimplified for further processing, as a rule.  See examples for what now works.   I have also changed simplify_full() to take this in, and hope that simplification of binomials and factorials first is best.  This needs the patch at #6197 to function properly, since otherwise binomial isn't recognized by sage as something it can pass to Maxima.


---

Attachment

Needs #6197


---

Comment by kcrisman created at 2009-09-08 13:55:53

This has been slightly changed because the doctest fix here actually belonged in #6197.  Otherwise still ready for review!


---

Comment by mhansen created at 2009-09-08 19:42:24

Looks good to me.

We might want to improve simplify_full so that we don't have 4 round trips to Maxima (convert to maxima, run all of the simplification commands on the MaximaElement, and then finally convert back to an Expression.)


---

Comment by kcrisman created at 2009-09-08 19:55:59

> We might want to improve simplify_full so that we don't have 4 round trips to Maxima (convert to maxima, run all of the simplification commands on the MaximaElement, and then finally convert back to an Expression.)

That makes a lot of sense.  Once this is merged, do you mind opening a ticket on that?


---

Comment by mhansen created at 2009-09-08 20:11:55

Sure thing.


---

Comment by mvngu created at 2009-09-09 09:23:51

Resolution: fixed
