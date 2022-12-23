# Issue 5417: Fix some more deepcopy issues (followup to #5403)

Issue created by migration from https://trac.sagemath.org/ticket/5417

Original creator: mabshoff

Original creation time: 2009-03-02 03:52:41

Assignee: justin

Gonzalo found some problem in the QF code when working on #5403. These problems are related to deepcopy.

Cheers,

Michael


---

Comment by tornaria created at 2009-03-02 04:21:41

The patch in #5403 fixes the function `scale_by_factor` in `quadratic_form__variable_substitutions.py`, by replacing the use of `copy.deepcopy` + `__init__` by a call to the constructor.

The issue with this is that the caches for some functions are copied, hence the results may be incorrect. There seem to be more instances of this bug in the quadratic_forms code, hence this ticket, but that one is the only one currently triggered by the following doctest (this only happens _after_ applying the `import *` fix in #5403 without the `deepcopy` fix):

```
        sage: Q = QuadraticForm(ZZ, 3, [2, -2, 0, 3, -5, 4])
        sage: Q.jordan_blocks_in_unimodular_list_by_scale_power(2)
        Traceback (most recent call last):
        ...
        TypeError: Oops!  The given quadratic form has a Jordan component with a negative scale exponent!
        This routine requires an integer-matrix quadratic form for the output indexing to work properly!

        sage: Q.scale_by_factor(2).jordan_blocks_in_unimodular_list_by_scale_power(2)
        [Quadratic form in 2 variables over Integer Ring with coefficients: 
        [ 0 2 ]
        [ * 0 ]
        ,
        Quadratic form in 0 variables over Integer Ring with coefficients: 
        ,
        Quadratic form in 1 variables over Integer Ring with coefficients: 
        [ 345 ]
        ]
```

In this example, after the first call to `jordan_blocks_in_unimodular_list_by_scale_power`, the result is cached, and the function `scale_by_factor` copies this cached result, so that the second call returns the answer for the original quadratic form.


---

Comment by jdemeyer created at 2015-08-28 09:58:27

Exactly what is the problem here? The description is very vague...
