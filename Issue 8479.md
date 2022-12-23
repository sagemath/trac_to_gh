# Issue 8479: [with patch, needs review] numpy support for more basic functions

Issue created by migration from https://trac.sagemath.org/ticket/8479

Original creator: whuss

Original creation time: 2010-03-07 21:19:39

Assignee: AlexGhitza

CC:  jason

Keywords: numpy

The attached patch adds numpy support for the functions:

coth, sech, csch, arccoth, arcsech, arccsch, ceil, floor,
sqrt, real_part, imag_part, sec, csc, cot, arccot, arccsc,
arcsec


---

Comment by jason created at 2010-03-17 05:07:26

Changing type from defect to enhancement.


---

Comment by burcin created at 2010-04-09 18:47:31

I hadn't seen this before! It's an enhancement to symbolic functions, so I'm changing the component to `symbolics`. 

We don't use tags on the subject line to mark tickets for review anymore, see the `Action` options right above the `Submit` button.


---

Comment by burcin created at 2010-04-09 18:47:31

Changing status from new to needs_review.


---

Comment by burcin created at 2010-04-09 18:47:31

Changing component from basic arithmetic to symbolics.


---

Comment by burcin created at 2010-05-06 21:19:54

Changing status from needs_review to needs_info.


---

Comment by burcin created at 2010-05-06 21:19:54

The patch looks really good and addresses an important problem. I have a few minor remarks/questions before I give a positive review:

 * Can we change the test in sage.functions.other.sqrt() to work without importing numpy? I didn't check the effects on performance, but `sqrt()` gets used a lot, so keeping it free of `numpy` unless absolutely necessary would be good.
 * All the examples in the doctests are for functions with a single argument. Is there any reason to move the check in `sage.symbolic.function.Function.__call__()` to try all arguments? We should also consider moving this check to `sage.symbolic.function.BuiltinFunction.__call__()`.


---

Attachment


---

Comment by whuss created at 2010-05-07 09:20:08

Replying to [comment:4 burcin]:

> * Can we change the test in sage.functions.other.sqrt() to work without importing numpy?

done in the new patch

> * All the examples in the doctests are for functions with a single argument. Is there any reason to move the check in `sage.symbolic.function.Function.__call__()` to try all arguments?

In the original patch I forgot to add tests for atan2, which also didn't work with numpy before. The tests are now included.

> We should also consider moving this check to `sage.symbolic.function.BuiltinFunction.__call__()`.

Why would this be better? It currently does not have a `__call__` method.


---

Comment by whuss created at 2010-05-07 09:20:08

Changing status from needs_info to needs_review.


---

Comment by burcin created at 2010-05-07 14:26:54

apply only this patch


---

Comment by burcin created at 2010-05-07 14:53:45

Changing status from needs_review to positive_review.


---

Attachment

Thanks for the quick response.

Replying to [comment:5 whuss]:
> Replying to [comment:4 burcin]:
> 
> > * Can we change the test in sage.functions.other.sqrt() to work without importing numpy?
> 
> done in the new patch

Thanks!

> > * All the examples in the doctests are for functions with a single argument. Is there any reason to move the check in `sage.symbolic.function.Function.__call__()` to try all arguments?
> 
> In the original patch I forgot to add tests for atan2, which also didn't work with numpy before. The tests are now included.

Fair enough.

> > We should also consider moving this check to `sage.symbolic.function.BuiltinFunction.__call__()`.
> 
> Why would this be better? 

This code path is speed critical since it gets called thousands of times for many applications like plotting. Checking the type of each argument introduces a penalty for functions with a single argument.

> It currently does not have a `__call__` method.

Sorry about that. I confused it with the `__call__()` method of `GinacFunction`, which also checks if there is only one argument, and it has a method with the same name as the function. Now I wonder why isn't that in `BuiltinFunction`...


Your patch was missing an empty line after line 165 in `sage/functions/other.py`. attachment:trac-8479-numpy_functions.take2.patch fixes this. Only attachment:trac-8479-numpy_functions.take2.patch should be applied.


Great work!


---

Comment by mvngu created at 2010-05-08 22:13:14

Resolution: fixed


---

Comment by mvngu created at 2010-05-08 22:13:14

Merged [trac-8479-numpy_functions.take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8479/trac-8479-numpy_functions.take2.patch).
