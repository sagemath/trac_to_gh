# Issue 7490: refactor symbolic functions

archive/issues_007490.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @mwhansen @jasongrout\n\nKeywords: pynac\n\nAttached patch refactors the symbolic function code in `sage/symbolic/function.pyx`.\n\n* `evalf()` now accepts a parent argument instead of a precision\n  This allows us to use the numeric evaluation framework in ginac for\n  evaluating things with `RIF`, `CIF` as well, not just `RealField`, or `ComplexField` with the given precision.\n\n* python arguments passed to custom methods of sfunctions are not\n  wrapped in `Expression` objects any more. No need to call `.pyobject()`\n  to unwrap these.\n\n* custom methods support calling methods on `self`.\n  This would be useful if you need access to other function of the\n  defining class, or store tables of data calculated on demand.\n\n* `__call__` method supports hold parameter\n  This works:\n\n```\n        sage: exp(log(x))\n        x\n        sage: exp(log(x), hold=True)\n        e^log(x)\n```\n\n* Custom methods for symbolic functions (`_eval_`, `_evalf_`, `_conjugate_`,\n  `_derivative_`, etc.) can be\n  written in Cython for builtin functions (that are provided by the\n  Sage library)\n\n* New class hiearchy:\n\n```\nFunction\n  GinacFunction\n  CustomizableFunction\n    BuiltinFunction\n    SymbolicFunction\n```\n We have 4 different types of functions, those defined by\n* ginac (sin, cos, ...),\n* the Sage library (cot)\n* the user (in a python file, subclassing the new\n  SymbolicFunction)\n* the command line function_factory (by calling function('f') )\n \n Things we need to do for these functions different for each of these,\n perhaps similar for the last two. Normally initializing a function\n means checking if it's already defined, if not, initializing a\n structure from ginac called function_options, and registering this in\n a table. There are also issues with pickling.\n \n For ginac functions, we don't need any of this, since we can't change\n it at python level. We only need to look up the serial number (the\n indicator in the table) of the function. We don't need to do anything\n to pickle or unpickle these either.\n \n Pickling and unpickling library functions only needs an identifier\n for the class to initialize it again if necessary. \n \n User defined functions need to lookup if there is an existing\n function in the table, since we should try to keep the table small.\n \n There is also a new `function_factory()` function in `sage.symbolic.function_factory`\n (it needs to be in a python file) that creates `NewSymbolicFunction`\n classes on the fly for the function() calls from the command line.\n\n\nThe pynac package here is required for this patch:\n\nhttp://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.10.a0.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/7490\n\n",
    "closed_at": "2009-12-04T05:35:47Z",
    "created_at": "2009-11-19T00:31:45Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "refactor symbolic functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7490",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

CC:  @mwhansen @jasongrout

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

Issue created by migration from https://trac.sagemath.org/ticket/7490





---

archive/issue_comments_063141.json:
```json
{
    "body": "After applying:\n\n```\nsage: integrate(e^x,(x,0,2),hold=True)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/grout/.sage/temp/good/20605/_home_grout__sage_init_sage_0.py in <module>()\n\n/home/grout/sage/local/lib/python2.6/site-packages/sage/misc/functional.pyc in integral(x, *args, **kwds)\n    566     \"\"\"\n    567     if hasattr(x, 'integral'):\n--> 568         return x.integral(*args, **kwds)\n    569     else:\n    570         from sage.symbolic.ring import SR\n\n/home/grout/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.integral (sage/symbolic/expression.cpp:25362)()\n\nTypeError: integral() got an unexpected keyword argument 'hold'\n```",
    "created_at": "2009-11-19T04:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63141",
    "user": "https://github.com/jasongrout"
}
```

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

archive/issue_comments_063142.json:
```json
{
    "body": "refactor symbolic functions",
    "created_at": "2009-11-19T11:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63142",
    "user": "https://github.com/burcin"
}
```

refactor symbolic functions



---

archive/issue_comments_063143.json:
```json
{
    "body": "Attachment [trac_7490-refactor_symbolic_functions.patch](tarball://root/attachments/some-uuid/ticket7490/trac_7490-refactor_symbolic_functions.patch) by @burcin created at 2009-11-19 11:58:58\n\nHi Jason,\n\nThis patch does not add a hold method to `integrate()` since it is not a *symbolic function*. Golam did some work in this direction at #6465, but more effort is needed to polish those patches.\n\nCheers,\n\nBurcin",
    "created_at": "2009-11-19T11:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63143",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7490-refactor_symbolic_functions.patch](tarball://root/attachments/some-uuid/ticket7490/trac_7490-refactor_symbolic_functions.patch) by @burcin created at 2009-11-19 11:58:58

Hi Jason,

This patch does not add a hold method to `integrate()` since it is not a *symbolic function*. Golam did some work in this direction at #6465, but more effort is needed to polish those patches.

Cheers,

Burcin



---

archive/issue_comments_063144.json:
```json
{
    "body": "I uploaded a new patch with a doctest fix in `sage.rings.arith`. The patch applies cleanly to 4.2.1 and passes all doctests (even long!). I think it is ready for review.\n\nThis also fixes #6523 and #6286. It should provide a basis to #6949, #6961, #6220 and #6465.\n\nNote that the patch touches 42 files. I would appreciate it if we can get it in 4.3.\n\nMike, while working on this, I had to tackle many of the problems you must have encountered during the symbolics switch. Can you take a look to see if I forgot anything/messed things up?",
    "created_at": "2009-11-19T12:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63144",
    "user": "https://github.com/burcin"
}
```

I uploaded a new patch with a doctest fix in `sage.rings.arith`. The patch applies cleanly to 4.2.1 and passes all doctests (even long!). I think it is ready for review.

This also fixes #6523 and #6286. It should provide a basis to #6949, #6961, #6220 and #6465.

Note that the patch touches 42 files. I would appreciate it if we can get it in 4.3.

Mike, while working on this, I had to tackle many of the problems you must have encountered during the symbolics switch. Can you take a look to see if I forgot anything/messed things up?



---

archive/issue_comments_063145.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-19T12:11:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63145",
    "user": "https://github.com/burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063146.json:
```json
{
    "body": "rebased to 4.3.alpha0",
    "created_at": "2009-11-23T12:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63146",
    "user": "https://github.com/burcin"
}
```

rebased to 4.3.alpha0



---

archive/issue_comments_063147.json:
```json
{
    "body": "Attachment [trac_7490-refactor_symbolic_functions.rebase-4.3.alpha0.patch](tarball://root/attachments/some-uuid/ticket7490/trac_7490-refactor_symbolic_functions.rebase-4.3.alpha0.patch) by @burcin created at 2009-11-23 12:13:18\n\nI rebased the patch to 4.3.alpha0:\n\nattachment:trac_7490-refactor_symbolic_functions.rebase-4.3.alpha0.patch",
    "created_at": "2009-11-23T12:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63147",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7490-refactor_symbolic_functions.rebase-4.3.alpha0.patch](tarball://root/attachments/some-uuid/ticket7490/trac_7490-refactor_symbolic_functions.rebase-4.3.alpha0.patch) by @burcin created at 2009-11-23 12:13:18

I rebased the patch to 4.3.alpha0:

attachment:trac_7490-refactor_symbolic_functions.rebase-4.3.alpha0.patch



---

archive/issue_comments_063148.json:
```json
{
    "body": "Thanks Burcin.  I'll tried to get it reviewed ASAP and have it the next thing in.",
    "created_at": "2009-11-23T12:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63148",
    "user": "https://github.com/mwhansen"
}
```

Thanks Burcin.  I'll tried to get it reviewed ASAP and have it the next thing in.



---

archive/issue_comments_063149.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-29T07:01:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63149",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_063150.json:
```json
{
    "body": "Here's my review.\n\nThere are a number of things which break old code -- they should be deprecated first.\n\n```\n- exp(2,prec=100), gamma(pi,prec=100), etc.\n\n- sage: Q.<i> = NumberField(x^2+1) \n  sage: gamma(i) \n  sage: gamma(QQbar(I))\n```\n\nConversion of polylog to maxima is broken:\n\n```\nsage: polylog(2, x)._maxima_init_()\n'polylog(2,x)'\n```\ninstead of `'li[2](x)'`.\n\nSome doctests are missing:\n\n```\nsage/interfaces/maxima.py: _symbolic_\nsage/rings/number_field/number_field_element.pyx: _mpfr_, __complex__\n```\n\nWhy do you have to use\n\n```\nf = CallableConvertMap(RR, RR, lambda x: x.exp(), parent_as_first_arg=False) \n```\ninstead of\n\n```\nf = CallableConvertMap(RR, RR, exp, parent_as_first_arg=False) \n```\n, which is more natural?\n\nIn expression.pyx, some things are missing from the _convert docstring.  Also, f._convert(int) gives `-0.989992496600445*sqrt(2)` which seems unexpected.  Maybe the docstring can be clarified further?\n\nFinally, there are some numerical issues it seems with evaluations: complex(I) gives 0.99999999999999967j instead of 1j.  I'm not sure where the discrepancy is occurring.",
    "created_at": "2009-11-29T07:01:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63150",
    "user": "https://github.com/mwhansen"
}
```

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

archive/issue_comments_063151.json:
```json
{
    "body": "revised patch based on 4.3.alpha0",
    "created_at": "2009-12-03T14:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63151",
    "user": "https://github.com/burcin"
}
```

revised patch based on 4.3.alpha0



---

archive/issue_comments_063152.json:
```json
{
    "body": "Attachment [trac_7490-refactor_symbolic_functions.take2.patch](tarball://root/attachments/some-uuid/ticket7490/trac_7490-refactor_symbolic_functions.take2.patch) by @burcin created at 2009-12-03 14:27:23\n\nThanks for your comments Mike.\n\nReplying to [comment:7 mhansen]:\n> Here's my review.\n> \n> There are a number of things which break old code -- they should be deprecated first.\n\n>\n {{{\n- exp(2,prec=100), gamma(pi,prec=100), etc.\n \n- sage: Q.<i> = NumberField(x^2+1) \n  sage: gamma(i) \n  sage: gamma(QQbar(I))\n }}}\n\nDone:\n\n```\nsage: exp(2,prec=100)\n...:...: DeprecationWarning: The prec keyword argument is deprecated. Explicitly set the precision of the input, for example exp(RealField(300)(1)), or use the prec argument to .n() for exact inputs, e.g., exp(1).n(300), instead.\n  # -*- coding: utf-8 -*-\n7.3890560989306502272304274606\n\nsage: gamma(2.5, prec=100)\n...:...: DeprecationWarning: The prec keyword argument is deprecated. Explicitly set the precision of the input, for example gamma(RealField(300)(1)), or use the prec argument to .n() for exact inputs, e.g., gamma(1).n(300), instead.\n  # -*- coding: utf-8 -*-\n1.3293403881791370224618731299\n\nsage: gamma(QQbar(I))\n-0.154949828301811 - 0.498015668118356*I\n\nsage: Q.<i> = NumberField(x^2+1)\nsage: gamma(i)\n...:...: DeprecationWarning: Calling symbolic functions with arguments that cannot be coerced into symbolic expressions is deprecated.\n  # -*- coding: utf-8 -*-\n-0.154949828301811 - 0.498015668118356*I\n```\n\n> Conversion of polylog to maxima is broken:\n\n {{{\n sage: polylog(2, x)._maxima_init_()\n 'polylog(2,x)'\n }}}\n> instead of `'li[2](x)'`.\n\n\nI don't know why I left `_maxima_init_evaled_()` commented. It works now:\n\n```\nsage: polylog(2, x)._maxima_()\nli[2](x)\nsage: polylog(4, x)._maxima_()\npolylog(4,x)\n```\n \n> Some doctests are missing:\n\n {{{\n sage/interfaces/maxima.py: _symbolic_\n sage/rings/number_field/number_field_element.pyx: _mpfr_, __complex__\n }}}\n\nDone.\n\n> Why do you have to use\n\n {{{\n f = CallableConvertMap(RR, RR, lambda x: x.exp(), parent_as_first_arg=False) \n }}}\n> instead of\n\n {{{\n f = CallableConvertMap(RR, RR, exp, parent_as_first_arg=False) \n }}}\n> , which is more natural?\n\n\nI converted the doctest back to the original form. Return values of `exp()` could be `int` for some inputs, even for arguments in `RR`. For example, `exp(RR(0))` used to return an `int(1)`. I added some code to wrap return values from GiNaC and convert them to something sensible in `sage.symbolic.function.GinacFunction.__call__()`.\n\n> In expression.pyx, some things are missing from the _convert docstring.  Also, f._convert(int) gives `-0.989992496600445*sqrt(2)` which seems unexpected.  Maybe the docstring can be clarified further?\n\n\nI wrote a little more for the docstring and added a few examples. The fact that GiNaC leaves the `power` objects exact is confusing, but I don't see any easy way to get around this.\n\n> Finally, there are some numerical issues it seems with evaluations: complex(I) gives 0.99999999999999967j instead of 1j.  I'm not sure where the discrepancy is occurring.\n\n\nThis seems to be an issue with complex embeddings of number field elements:\n\n```\nsage: complex(CDF.0)\n1j\nsage: complex(CC.0)\n1j\nsage: complex(CDF.0)\n1j\nsage: Q.<i> = NumberField(x^2+1)\nsage: complex(i)\n0.99999999999999967j\n```\n\nOf course, I added the last method that gets called for `complex(i)`, but all it does is to `return complex(self.complex_embedding())`. \n\nI suggest we open a separate ticket about this since it's independent of the symbolics code and someone who knows the number field code should take a look at it.",
    "created_at": "2009-12-03T14:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63152",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_7490-refactor_symbolic_functions.take2.patch](tarball://root/attachments/some-uuid/ticket7490/trac_7490-refactor_symbolic_functions.take2.patch) by @burcin created at 2009-12-03 14:27:23

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

archive/issue_comments_063153.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-03T14:27:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63153",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_events_017757.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-04T05:35:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7490#event-17757"
}
```



---

archive/issue_comments_063154.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-04T05:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63154",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_063155.json:
```json
{
    "body": "Looks good to me.  Thanks for making those changes.  I've made the number field embedding #7598.",
    "created_at": "2009-12-04T05:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7490",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7490#issuecomment-63155",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  Thanks for making those changes.  I've made the number field embedding #7598.
