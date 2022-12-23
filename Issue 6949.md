# Issue 6949: add symbolic max and min functions

Issue created by migration from https://trac.sagemath.org/ticket/6949

Original creator: burcin

Original creation time: 2009-09-17 14:04:24

CC:  jason

Matt Riesler wrote on sage-support:


```
Is it possible to have max behave as you would expect with a symbolic
expression, i.e. wait until you evaluate it or restrict the domain  to
check what is the maximum of the two or more values.
```


Then kcrisman:


```
Might there be a way to do something that doesn't conflict with the
builtin max function in the same way as the (nearly reviewed) #3587
seems to avoid conflict with the builtin sum function?  This would be
pretty useful, as currently:

sage: var('x,y')
(x, y)
sage: max(x,y)
x
sage: f(x)=1+x;g(x)=2-x
sage: max(f,g)
x |--> x + 1

which last result is... debatable.
```


Here is a the thread, which has a simple minded implementation for symbolic max:

http://groups.google.com/group/sage-support/browse_thread/thread/aead15de586984d8


We should make sure the symbolic implementations don't slow down the current builtin python `max()` and `min()` too much. If they do, these functions should still be available under a different name.


---

Comment by zimmerma created at 2010-03-12 19:41:53

see also #8508


---

Comment by burcin created at 2010-04-02 21:33:15

Changing status from new to needs_review.


---

Comment by burcin created at 2010-04-02 21:33:15

attachment:trac_6949-symbolic_min_max.patch provides basic implementations of `max_symbolic()` and `min_symbolic()` functions that work as expected when the input contains symbolic expressions.

The symbolic versions are significantly slower than Python's builtin `min()` and `max()`, so replacing the builtin functions with these is not possible at this point.


---

Attachment


---

Comment by burcin created at 2010-04-06 15:26:01

Set assignee to burcin.


---

Comment by burcin created at 2010-04-06 15:26:01

I updated attachment:trac_6949-symbolic_min_max.patch to fix a minor doctest error in sage/symbolic/ring.pyx.


---

Comment by lfousse created at 2010-04-29 13:55:36

I applied the patch on top of 4.3.5:

```
sage: f(x) = max_symbolic(sin(x), cos(x))
sage: f(0)
1
sage: f
x |--> max(sin(x), cos(x))
sage: f(1)
max(sin(1), cos(1))
```

So far, so good. But:

```
sage: N(f(1))
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

Comment by lfousse created at 2010-04-29 13:55:36

Changing status from needs_review to needs_work.


---

Comment by burcin created at 2010-05-05 04:19:32

add evalf methods, put common eval and __call__ methods to base class


---

Comment by burcin created at 2010-05-05 04:23:30

Changing status from needs_work to needs_review.


---

Attachment

Thanks for the review.

The new patch attachment:trac_6949-symbolic_min_max.take2.patch replaces the previous one, and implements `_evalf_()` methods for numeric evaluation. I also created a base class with the common code from `__call__()` and `_eval_()` methods.

Can you take another look?


---

Comment by lfousse created at 2010-05-05 07:32:38

Thanks for the updated patch. I applied it on top of 4.4. I can verify the previously reported problem for numerical evaluation works. I have however a new problem:

```
sage: f(x) = max_symbolic(sin(x), cos(x))
sage: N(integral(f, x, 0, 1))
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/opt/sage-4.4/<ipython console> in <module>()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/misc/functional.pyc in numerical_approx(x, prec, digits)
   1163             prec = int((digits+1) * 3.32192) + 1
   1164     try:
-> 1165         return x.numerical_approx(prec)
   1166     except AttributeError:
   1167         from sage.rings.complex_double import is_ComplexDoubleElement

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:16928)()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._convert (sage/symbolic/expression.cpp:4677)()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in _evalf_(self, *args, **kwds)
    155             TypeError: cannot evaluate symbolic expression numerically
    156         """
--> 157         return max_symbolic(args)
    158
    159 max_symbolic = MaxSymbolic()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in __call__(self, *args, **kwds)
     79                 return args
     80
---> 81         return BuiltinFunction.__call__(self, *args, **kwds)
     82
     83 class MaxSymbolic(MinMax_base):

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4359)()

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in _eval_(self, *args)
    136             ValueError: number of arguments must be > 0
    137         """
--> 138         return self.eval_helper(max_symbolic, builtin_max, None, args)
    139
    140     def _evalf_(self, *args, **kwds):

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in eval_helper(self, this_f, builtin_f, initial_val, args)
     51
     52         symb_args.append(res)
---> 53         return this_f(*symb_args)
     54
     55     def __call__(self, *args, **kwds):

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/functions/min_max.pyc in __call__(self, *args, **kwds)
     79                 return args
     80
---> 81         return BuiltinFunction.__call__(self, *args, **kwds)
     82
     83 class MaxSymbolic(MinMax_base):

/opt/sage-4.4/local/lib/python2.6/site-packages/sage/symbolic/function.so in sage.symbolic.function.Function.__call__ (sage/symbolic/function.cpp:4192)()

TypeError: cannot coerce arguments: no canonical coercion from <type 'NoneType'> to Symbolic Ring
```

I don't know if the problem is with integrate or max_symbolic.


---

Attachment

apply only this patch


---

Comment by burcin created at 2010-05-05 15:33:13

Thanks a lot for testing this. I uploaded a new patch in attachment:trac_6949-symbolic_min_max.take3.patch which should cover many corner cases not handled properly before. The aim is to make `{max,min}_symbolic()` behave almost identical to the builtin `min()` and `max()`.

Can you try and break it again? :)


---

Comment by lfousse created at 2010-05-06 05:36:33

Applied on top of 4.4.1 this time. I could not break it with my tests, and I also checked -testall, -coverage etc. as per the patch review guidelines. So that would be a positive review. Thanks!


---

Comment by lfousse created at 2010-05-06 05:36:33

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-08 22:07:12

Resolution: fixed


---

Comment by mvngu created at 2010-05-08 22:07:12

Merged [trac_6949-symbolic_min_max.take3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/6949/trac_6949-symbolic_min_max.take3.patch).


---

Comment by kcrisman created at 2012-12-21 14:06:30

See #13857 for adding this to the reference manual, which somehow never happened but would be worthy considering how many emails we still get about this situation.
