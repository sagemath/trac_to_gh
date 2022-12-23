# Issue 8459: broken translatin of polylog from Maxima

Issue created by migration from https://trac.sagemath.org/ticket/8459

Original creator: robert.marik

Original creation time: 2010-03-06 21:41:27

Assignee: burcin

CC:  kcrisman burcin

Keywords: symbolics

Maixma's li[2](x) translates to polylog2(x) which is not defined in Sage

```
sage: maxima('li[1](x)').sage().subs(x=2).n() 
-3.14159265358979*I
sage: maxima('li[2](x)').sage().subs(x=2).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-4.3.3-i686-Linux/<ipython console> in <module>()

/opt/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()

TypeError: cannot evaluate symbolic expresssion numerically

sage: f(x)= integrate(log(1-x^2)/x, x); f(2).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-4.3.3-i686-Linux/<ipython console> in <module>()

/opt/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()

TypeError: cannot evaluate symbolic expresssion numerically

```


patch comes soon


---

Attachment

apply only this patch


---

Attachment

The patch is attached. Still have behavior which I do not understand:
log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1) evaluates numerically at x=1/2 only if it is obtained from direct input and not from Maxima.

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: f(x)=integrate(ln(1-x^2)/x,x)                       
sage: f
x |--> log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)
sage: g(x)=log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)
sage: g
x |--> log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)
sage: bool(f==g)                                          
False
sage: bool(f._repr_()==g._repr_())                        
True
sage: g(1/2).n()
0.688640713882747
sage: f(1/2).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
/opt/sage-4.3.3-i686-Linux/<ipython console> in <module>()

/opt/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()

TypeError: cannot evaluate symbolic expresssion numerically
sage:
```

Any idea what happens?


---

Comment by robert.marik created at 2010-03-06 22:32:42

Changing status from new to needs_review.


---

Comment by robert.marik created at 2010-03-07 14:01:25

And anther issue which I do not understand:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: polylog
sage: g(x)=integrate(ln(1-x^2)/x,x)
sage: g(1/2).n()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
/opt/sage-4.3.3/<ipython console> in <module>()

/opt/sage-4.3.3/local/lib/python2.6/site-packages/sage/symbolic/expression.so in                                              sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17036)()

TypeError: cannot evaluate symbolic expresssion numerically
sage: g(x)=eval(preparse(integrate(ln(1-x^2)/x,x)._repr_()))
sage: g(1/2).n()
0.688640713882747
sage: g
x |--> log(-x^2 + 1)*log(x) + 1/2*polylog(2, -x^2 + 1)
sage:
```

why are eval and _repr_ necessary?


---

Comment by robert.marik created at 2010-03-07 14:58:28

[sage-support](http://groups.google.cz/group/sage-support/browse_thread/thread/d1ef50cd207e0f76) question concerning the problem above


---

Comment by burcin created at 2010-04-05 10:51:47

Changing status from needs_review to positive_review.


---

Attachment

Thank you for the patch and pointing out the conversion problem Robert.

I fixed the problems reported in comment:2 in #7661.

attachment:trac_8459-doctest.patch adds a doctest to sage.functions.log.Function_polylog to check if the conversion works. It also moves the compilation of the regular expression out of the `symbolic_expression_from_maxima_string()` function.

Patches to be applied, in this order:
 * attachment:trac-8459.patch
 * attachment:trac_8459-doctest.patch

This ticket depends on #7661.


---

Comment by robert.marik created at 2010-04-09 07:47:56

Thanks for improving this, Burcin. 

To the release manager: Apply only the patches trac-8459* , the first patch was my mistake and it is not relevant in this ticket.


---

Comment by jhpalmieri created at 2010-04-15 23:20:55

After applying "trac-8459.patch" and "trac_8459-doctest.patch" to Sage 4.3.5, I get doctest errors for functions/log.py:

```
sage -t  "devel/sage/sage/functions/log.py"                 
**********************************************************************
File "/Applications/sage/devel/sage/sage/functions/log.py", line 305:
    sage: t.operator() == polylog
Expected:
    True
Got:
    False
**********************************************************************
File "/Applications/sage/devel/sage/sage/functions/log.py", line 307:
    sage: t.subs(x=.5).n()
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[17]>", line 1, in <module>
        t.subs(x=RealNumber('.5')).n()###line 307:
    sage: t.subs(x=.5).n()
      File "expression.pyx", line 3797, in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:17043)
    TypeError: cannot evaluate symbolic expression numerically
**********************************************************************
1 items had failures:
   2 of  18 in __main__.example_5
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/palmieri/.sage//tmp/.doctest_log.py
	 [7.6 s]
```



---

Comment by jhpalmieri created at 2010-04-15 23:20:55

Changing status from positive_review to needs_work.


---

Comment by burcin created at 2010-05-04 21:48:45

Replying to [comment:7 jhpalmieri]:
> After applying "trac-8459.patch" and "trac_8459-doctest.patch" to Sage 4.3.5, I get doctest errors for functions/log.py:
<snipped the error log>

These errors look like the patch attachment:trac_8459-doctest.patch was applied without #7661. That ticket was merged before this, so I have no idea what went wrong.

I applied these patches to Sage-4.4.1 and ran the tests. There were no errors. Switching this back to positive review, and keeping fingers crossed that there is no subtle bug hiding somewhere.


---

Comment by burcin created at 2010-05-04 21:48:45

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-05-04 21:49:07

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2010-05-04 21:49:07

Patches to be applied, in this order:

    * attachment:trac-8459.patch
    * attachment:trac_8459-doctest.patch


---

Comment by mvngu created at 2010-05-08 22:11:44

Resolution: fixed


---

Comment by mvngu created at 2010-05-08 22:11:44

Merged in this order:

 1. [trac-8459.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8459/trac-8459.patch)
 1. [trac_8459-doctest.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8459/trac_8459-doctest.patch)
