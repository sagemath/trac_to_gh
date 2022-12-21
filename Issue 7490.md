# Issue 7490: refactor symbolic functions

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-11-19 00:31:45

Assignee: burcin

CC:  mhansen jason

Keywords: pynac

Attached patch refactors the symbolic function code in `sage/symbolic/function.pyx`.

 * `evalf()` now accepts a parent argument instead of a precision
  This allows us to use the numeric evaluation framework in ginac for
  evaluating things with `RIF`, `CIF` as well, not just `RealField`, or `ComplexField` with the given precision.

 * python arguments passed to custom methods of sfunctions are not
   wrapped in `Expression` objects any more. No need to call `.pyobject()`
   to unwrap these.

 * custom methods support calling methods on `self`.
  This would be useful if you need access to other function of the
  defining class, or store tables of data calculated on demand.

 * `__call__` method supports hold parameter
  This works:

```
	sage: exp(log(x))
        x
        sage: exp(log(x), hold=True)
        e^log(x)
```


 * Custom methods for symbolic functions (`_eval_`, `_evalf_`, `_conjugate_`,
   `_derivative_`, etc.) can be
   written in Cython for builtin functions (that are provided by the
   Sage library)

 * New class hiearchy:

```
Function
  GinacFunction
  CustomizableFunction
    BuiltinFunction
    SymbolicFunction
```

 We have 4 different types of functions, those defined by
  * ginac (sin, cos, ...),
  * the Sage library (cot)
  * the user (in a python file, subclassing the new
    SymbolicFunction)
  * the command line function_factory (by calling function('f') )
 
 Things we need to do for these functions different for each of these,
 perhaps similar for the last two. Normally initializing a function
 means checking if it's already defined, if not, initializing a
 structure from ginac called function_options, and registering this in
 a table. There are also issues with pickling.
 
 For ginac functions, we don't need any of this, since we can't change
 it at python level. We only need to look up the serial number (the
 indicator in the table) of the function. We don't need to do anything
 to pickle or unpickle these either.
 
 Pickling and unpickling library functions only needs an identifier
 for the class to initialize it again if necessary. 
 
 User defined functions need to lookup if there is an existing
 function in the table, since we should try to keep the table small.
 
 There is also a new `function_factory()` function in `sage.symbolic.function_factory`
 (it needs to be in a python file) that creates `NewSymbolicFunction`
 classes on the fly for the function() calls from the command line.


The pynac package here is required for this patch:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.a0.spkg


---

Comment by jason created at 2009-11-19 04:06:39

After applying:


```
sage: integrate(e^x,(x,0,2),hold=True)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/.sage/temp/good/20605/_home_grout__sage_init_sage_0.py in <module>()

/home/grout/sage/local/lib/python2.6/site-packages/sage/misc/functional.pyc in integral(x, *args, **kwds)
    566     """
    567     if hasattr(x, 'integral'):
--> 568         return x.integral(*args, **kwds)
    569     else:
    570         from sage.symbolic.ring import SR

/home/grout/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:25362)()

TypeError: integral() got an unexpected keyword argument 'hold'
```



---

Comment by burcin created at 2009-11-19 11:46:10

refactor symbolic functions


---

Attachment

Hi Jason,

This patch does not add a hold method to `integrate()` since it is not a _symbolic function_. Golam did some work in this direction at #6465, but more effort is needed to polish those patches.

Cheers,

Burcin


---

Comment by burcin created at 2009-11-19 12:11:22

I uploaded a new patch with a doctest fix in `sage.rings.arith`. The patch applies cleanly to 4.2.1 and passes all doctests (even long!). I think it is ready for review.

This also fixes #6523 and #6286. It should provide a basis to #6949, #6961, #6220 and #6465.

Note that the patch touches 42 files. I would appreciate it if we can get it in 4.3.

Mike, while working on this, I had to tackle many of the problems you must have encountered during the symbolics switch. Can you take a look to see if I forgot anything/messed things up?


---

Comment by burcin created at 2009-11-19 12:11:22

Changing status from new to needs_review.


---

Comment by burcin created at 2009-11-23 12:11:26

rebased to 4.3.alpha0


---

Attachment

I rebased the patch to 4.3.alpha0:

attachment:trac_7490-refactor_symbolic_functions.rebase-4.3.alpha0.patch


---

Comment by mhansen created at 2009-11-23 12:21:18

Thanks Burcin.  I'll tried to get it reviewed ASAP and have it the next thing in.


---

Comment by mhansen created at 2009-11-29 07:01:42

Changing status from needs_review to needs_work.


---

Comment by mhansen created at 2009-11-29 07:01:42

Here's my review.

There are a number of things which break old code -- they should be deprecated first.


```
- exp(2,prec=100), gamma(pi,prec=100), etc.

- sage: Q.<i> = NumberField(x^2+1) 
  sage: gamma(i) 
  sage: gamma(QQbar(I))
```


Conversion of polylog to maxima is broken:

```
sage: polylog(2, x)._maxima_init_()
'polylog(2,x)'
```

instead of `'li[2](x)'`.

Some doctests are missing:

```
sage/interfaces/maxima.py: _symbolic_
sage/rings/number_field/number_field_element.pyx: _mpfr_, __complex__
```


Why do you have to use

```
f = CallableConvertMap(RR, RR, lambda x: x.exp(), parent_as_first_arg=False) 
```

instead of

```
f = CallableConvertMap(RR, RR, exp, parent_as_first_arg=False) 
```

, which is more natural?

In expression.pyx, some things are missing from the _convert docstring.  Also, f._convert(int) gives `-0.989992496600445*sqrt(2)` which seems unexpected.  Maybe the docstring can be clarified further?

Finally, there are some numerical issues it seems with evaluations: complex(I) gives 0.99999999999999967j instead of 1j.  I'm not sure where the discrepancy is occurring.


---

Comment by burcin created at 2009-12-03 14:03:14

revised patch based on 4.3.alpha0


---

Attachment

Thanks for your comments Mike.

Replying to [comment:7 mhansen]:
> Here's my review.
> 
> There are a number of things which break old code -- they should be deprecated first.
>
 {{{
 - exp(2,prec=100), gamma(pi,prec=100), etc.
 
 - sage: Q.<i> = NumberField(x^2+1) 
   sage: gamma(i) 
   sage: gamma(QQbar(I))
 }}}

Done:


```
sage: exp(2,prec=100)
...:...: DeprecationWarning: The prec keyword argument is deprecated. Explicitly set the precision of the input, for example exp(RealField(300)(1)), or use the prec argument to .n() for exact inputs, e.g., exp(1).n(300), instead.
  # -*- coding: utf-8 -*-
7.3890560989306502272304274606

sage: gamma(2.5, prec=100)
...:...: DeprecationWarning: The prec keyword argument is deprecated. Explicitly set the precision of the input, for example gamma(RealField(300)(1)), or use the prec argument to .n() for exact inputs, e.g., gamma(1).n(300), instead.
  # -*- coding: utf-8 -*-
1.3293403881791370224618731299

sage: gamma(QQbar(I))
-0.154949828301811 - 0.498015668118356*I

sage: Q.<i> = NumberField(x^2+1)
sage: gamma(i)
...:...: DeprecationWarning: Calling symbolic functions with arguments that cannot be coerced into symbolic expressions is deprecated.
  # -*- coding: utf-8 -*-
-0.154949828301811 - 0.498015668118356*I
```


> Conversion of polylog to maxima is broken:
 {{{
 sage: polylog(2, x)._maxima_init_()
 'polylog(2,x)'
 }}}
> instead of `'li[2](x)'`.

I don't know why I left `_maxima_init_evaled_()` commented. It works now:


```
sage: polylog(2, x)._maxima_()
li[2](x)
sage: polylog(4, x)._maxima_()
polylog(4,x)
```

 
> Some doctests are missing:
 {{{
 sage/interfaces/maxima.py: _symbolic_
 sage/rings/number_field/number_field_element.pyx: _mpfr_, __complex__
 }}}

Done.

> Why do you have to use
 {{{
 f = CallableConvertMap(RR, RR, lambda x: x.exp(), parent_as_first_arg=False) 
 }}}
> instead of
 {{{
 f = CallableConvertMap(RR, RR, exp, parent_as_first_arg=False) 
 }}}
> , which is more natural?

I converted the doctest back to the original form. Return values of `exp()` could be `int` for some inputs, even for arguments in `RR`. For example, `exp(RR(0))` used to return an `int(1)`. I added some code to wrap return values from GiNaC and convert them to something sensible in `sage.symbolic.function.GinacFunction.__call__()`.

> In expression.pyx, some things are missing from the _convert docstring.  Also, f._convert(int) gives `-0.989992496600445*sqrt(2)` which seems unexpected.  Maybe the docstring can be clarified further?

I wrote a little more for the docstring and added a few examples. The fact that GiNaC leaves the `power` objects exact is confusing, but I don't see any easy way to get around this.

> Finally, there are some numerical issues it seems with evaluations: complex(I) gives 0.99999999999999967j instead of 1j.  I'm not sure where the discrepancy is occurring.

This seems to be an issue with complex embeddings of number field elements:


```
sage: complex(CDF.0)
1j
sage: complex(CC.0)
1j
sage: complex(CDF.0)
1j
sage: Q.<i> = NumberField(x^2+1)
sage: complex(i)
0.99999999999999967j
```


Of course, I added the last method that gets called for `complex(i)`, but all it does is to `return complex(self.complex_embedding())`. 

I suggest we open a separate ticket about this since it's independent of the symbolics code and someone who knows the number field code should take a look at it.


---

Comment by burcin created at 2009-12-03 14:27:23

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2009-12-04 05:35:47

Resolution: fixed


---

Comment by mhansen created at 2009-12-04 05:35:47

Looks good to me.  Thanks for making those changes.  I've made the number field embedding #7598.
