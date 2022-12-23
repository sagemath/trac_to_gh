# Issue 2678: modform -- a missing canonical coercion

Issue created by migration from https://trac.sagemath.org/ticket/2678

Original creator: was

Original creation time: 2008-03-26 18:05:58

Assignee: was


```

There are some canonical coercions that one *should* have in the context
of modular forms that aren't there, probably partly because this whole "canonical
coercions" business was after I wrote the modular forms code.  Here's
an example bug (=lack of a coercion that should be there):

sage: b=CuspForms(22).basis()
sage: sum(b, b[0].parent()(0))
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/Users/was/<ipython console> in <module>()

/Users/was/element.pyx in sage.structure.element.ModuleElement.__add__()

/Users/was/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()

<type 'exceptions.TypeError'>: unsupported operand parent(s) for '+': 'Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(22) of weight 2 over Rational Field' and 'Cuspidal subspace of dimension 2 of Modular Forms space of dimension 5 for Congruence Subgroup Gamma0(22) of weight 2 over Rational Field'
 -- William
```



---

Comment by craigcitro created at 2008-04-07 02:11:46

This was fixed with #2674.


---

Comment by craigcitro created at 2008-04-07 02:11:46

Resolution: fixed
