# Issue 8568: can not simplify derivative of erf

Issue created by migration from Trac.

Original creator: gmcmanus

Original creation time: 2010-03-21 07:36:42

Assignee: burcin

CC:  jason burcin

Sometimes sage can differentiate erf, but if there are two variables involved it gets confused in simplification and passes too many arguments to erf in maxima.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: var('c x')
(c, x)
sage: diff(erf(x), x)
D[0](erf)(x)
sage: simplify(diff(erf(x), x))
2*e^(-x^2)/sqrt(pi)
sage: diff(erf(c * x), x)
c*D[0](erf)(c*x)
sage: simplify(diff(erf(c * x), x))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.3.3, Release Date: 2010-02-21                       |
| Type notebook() for the GUI, and license() for information.        |
/.../<ipython console> in <module>()

/.../sage-4.3.3-linux-64bit-ubuntu_9.10-x86_64-Linux/local/lib/python2.6/site-packages/sage/calculus/functional.pyc
in simplify(f)
     49     """
     50     try:
---> 51         return f.simplify()
     52     except AttributeError:
     53         return f

/.../sage-4.3.3-linux-64bit-ubuntu_9.10-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression.so
in sage.symbolic.expression.Expression.simplify (sage/symbolic/expression.cpp:21495)()

/.../sage-4.3.3-linux-64bit-ubuntu_9.10-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression.so
in sage.symbolic.expression.Expression._maxima_ (sage/symbolic/expression.cpp:3435)()

/.../sage-4.3.3-linux-64bit-ubuntu_9.10-x86_64-Linux/local/lib/python2.6/site-packages/sage/structure/sage_object.so
in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3501)()

/.../sage-4.3.3-linux-64bit-ubuntu_9.10-x86_64-Linux/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc
in __call__(self, x, name)
   1030             
   1031         if isinstance(x, basestring):
-> 1032             return cls(self, x, name=name)
   1033         try:
   1034             return self._coerce_from_special_method(x)

/.../sage-4.3.3-linux-64bit-ubuntu_9.10-x86_64-Linux/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc
in __init__(self, parent, value, is_name, name)
   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1450                 self._session_number = -1
-> 1451                 raise TypeError, x
   1452         self._session_number = parent._session_number
   1453 

TypeError: Error executing code in Maxima
CODE:
        sage4 : (c)*(diff('erf(c, x), c, 1))$
Maxima ERROR:
        
Wrong number of arguments to erf
 -- an error. To debug this try: debugmode(true);
```



---

Comment by kcrisman created at 2010-05-26 20:24:41


```
CODE:
        sage4 : (c)*(diff('erf(c, x), c, 1))$
Maxima ERROR:
```

This looks suspicious.  Why is it not erf(c*x)?  I will investigate.


---

Comment by kcrisman created at 2010-05-26 21:10:39

Another problem... note that the variable being used in differentiation is c, not x!


---

Comment by kcrisman created at 2010-05-26 21:25:48

Somehow it must be related to this inconsistency.

```
sage: a
c*D[0](erf)(c*x)
sage: a._maxima_init_()
"(c)*(diff('erf(c, x), c, 1))"
sage: a.operands()[1].operands()[0]
c*x
sage: a.operands()[1].operands()[0]._maxima_init_()
'(c)*(x)'
```

Any ideas?


---

Attachment


---

Comment by burcin created at 2010-05-27 10:45:19

I attached a patch which fixes the conversion to maxima. This doesn't fix the problem in the title of this ticket, "cannot simplify derivative of erf", since we cannot convert derivatives to maxima format if the arguments to the function are not variables.

In order to fix the problem reported here, we can add a `_derivative_` method to the `Function_erf()` class defined in `sage.functions.other`.


---

Comment by burcin created at 2010-05-27 10:45:19

Changing status from new to needs_work.


---

Comment by kcrisman created at 2010-05-27 15:30:33

That sounds like a great idea.  Patch coming up.


---

Comment by kcrisman created at 2010-05-27 15:46:35

Apply only this.


---

Attachment

This looks like a good change.  I did the other thing, and put the test of the original bug report in that file, since it seemed like it belonged there now that it works :)  Should pass all tests (only failures for me were related to Maxima upgrade).


---

Comment by kcrisman created at 2010-05-27 15:48:04

Changing status from needs_work to needs_review.


---

Attachment


---

Attachment

Thanks for the quick fix!

Your patch removes my commit message, which I tried hard to make long and explanatory. :) Please submit a separate patch in the future.

I uploaded two new patches, one including your changes to the `erf` function, and the other my fixes for `expression_conversions.py`.

Patches to be applied:
 * attachment:trac_8568-diff_conversion.take2.patch
 * attachment:trac_8568-erf-deriv.patch


---

Comment by burcin created at 2010-05-27 16:18:25

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-05-27 16:54:38

Sorry, Burcin, truthfully I hadn't even noticed that!  I was just trying to make a unified patch, because I hate all these five-patch tickets where they move things around from patch to patch - in this case, the actual test for the fix - since they are very hard for me to read.  But I'll be more careful now :)


---

Comment by mhansen created at 2010-06-06 01:27:12

Resolution: fixed


---

Comment by mhansen created at 2010-06-07 06:53:25

This actually causes a failure in sage/interfaces/maxima.py


---

Comment by mhansen created at 2010-06-07 06:53:25

Changing status from closed to needs_work.


---

Comment by kcrisman created at 2010-06-08 01:03:57

Here it is.  I'll try to fix it quickly, hopefully this can still get in 4.4.4.

```
File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/devel/sage/sage/interfaces/maxima.py", line 2245:
    sage: latex(maxima(derivative(ceil(x*y*d), d,x,x,y)))
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_70[4]>", line 1, in <module>
        latex(maxima(derivative(ceil(x*y*d), d,x,x,y)))###line 2245:
    sage: latex(maxima(derivative(ceil(x*y*d), d,x,x,y)))
      File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/local/lib/python/site-packages/sage/interfaces/expect.py", line 1034, in __call__
        return self._coerce_from_special_method(x)
      File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/local/lib/python/site-packages/sage/interfaces/expect.py", line 1058, in _coerce_from_special_method
        return (x.__getattribute__(s))(self)
      File "expression.pyx", line 435, in sage.symbolic.expression.Expression._maxima_ (sage/symbolic/expression.cpp:3420)
      File "sage_object.pyx", line 379, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3374)
      File "sage_object.pyx", line 468, in sage.structure.sage_object.SageObject._maxima_init_ (sage/structure/sage_object.c:5083)
      File "expression.pyx", line 458, in sage.symbolic.expression.Expression._interface_init_ (sage/symbolic/expression.cpp:3510)
      File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 214, in __call__
        return self.arithmetic(ex, operator)
      File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 515, in arithmetic
        args = ["(%s)"%self(op) for op in ex.operands()]
      File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 214, in __call__
        return self.arithmetic(ex, operator)
      File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 515, in arithmetic
        args = ["(%s)"%self(op) for op in ex.operands()]
      File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 218, in __call__
        return self.derivative(ex, operator)
      File "/mnt/usb1/scratch/kcrisman/sage-4.4.4.alpha0-boxen.math.washington.edu-x86_64-Linux/local/lib/python/site-packages/sage/symbolic/expression_conversions.py", line 495, in derivative
        raise NotImplementedError, "arguments must be distinct variables"
    NotImplementedError: arguments must be distinct variables
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_70
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/kcrisman/.sage//tmp/.doctest_maxima.py
	 [14.2 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "devel/sage/sage/interfaces/maxima.py"
```



---

Comment by kcrisman created at 2010-06-08 01:22:20

Or not.

```
sage: maxima(derivative(ceil(d),d))
'diff('ceil(d),d,1)
sage: maxima(derivative(ceil(x*d),d))
<same NotImplementedError>
```

So the problem is that Burcin's Maxima conversion change now doesn't work with

```
    493         if (not all(is_SymbolicVariable(v) for v in args) or
    494             len(args) != len(set(args))):
--> 495             raise NotImplementedError, "arguments must be distinct variables"
    496 
    497         f = operator.function()
```

in derivative().  In fact, he even included a doctest for it!

```
We can only convert to Maxima derivatives if the corresponding operand of the function is a variable:: 
sage: y = var('y') 
sage: t = f(x*y).diff(x) 
sage: m.derivative(t, t.operator()) 
Traceback (most recent call last): 
... 
NotImplementedError: arguments must be distinct variables 
```

This example could be fixed if one fixed

```
sage: derivative(ceil(x),x)
D[0](ceil)(x)
```

so that there isn't a derivative function defined for ceil.  I'm not sure exactly what would count, though... just the zero function?


---

Attachment


---

Comment by burcin created at 2010-09-08 11:48:48

Changing status from needs_work to needs_review.


---

Comment by burcin created at 2010-09-08 11:48:48

I attached a new patch which fixes the doctest failures in `interfaces/maxima.py`. The patch changes the test to use a symbolic function `f` instead of `ceil`, adds the error message that we need distinct arguments to convert to maxima and a test with an expression where the variables are indeed distinct arguments.

Adding a function to represent the derivative of `ceil()` and `floor()` is now #9874.

Patches should be applied in this order:

 * attachment:trac_8568-diff_conversion.take2.patch
 * attachment:trac_8568-erf-deriv.patch
 * attachment:trac_8568-fix_doctests.patch


---

Comment by kcrisman created at 2010-09-21 20:01:27

This all still applies fine to Sage 4.6.alpha1, and all doctests I could think of pass.  Everything else is the same - positive review!

By the way, thanks for opening that other ticket, Burcin - sometimes I get paralyzed trying to decide what the best course of action is on reviews.


---

Comment by kcrisman created at 2010-09-21 20:01:27

Changing status from needs_review to positive_review.
