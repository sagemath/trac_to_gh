# Issue 2665: error in coercion between CIF and SR

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-03-25 20:26:38

Assignee: robertwb

CC:  ncalexan

Keywords: symbolic SR complex interval field CIF


```
sage: SR(0) * CIF(I)
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/Users/ncalexan/Documents/School/MATH235/genus2cm/<ipython console> in <module>()

/Users/ncalexan/Documents/School/MATH235/genus2cm/element.pyx in sage.structure.element.RingElement.__mul__()

/Users/ncalexan/Documents/School/MATH235/genus2cm/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()

/Users/ncalexan/Documents/School/MATH235/genus2cm/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.get_action_c()

/Users/ncalexan/Documents/School/MATH235/genus2cm/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.discover_action_c()

/Users/ncalexan/Documents/School/MATH235/genus2cm/parent.pyx in sage.structure.parent.Parent.get_action_c()

/Users/ncalexan/Documents/School/MATH235/genus2cm/parent.pyx in sage.structure.parent.Parent.get_action_impl()

/Users/ncalexan/Documents/School/MATH235/genus2cm/parent.pyx in sage.structure.parent.Parent.get_action_c_impl()

/Users/ncalexan/Documents/School/MATH235/genus2cm/parent.pyx in sage.structure.parent._register_pair()

<type 'exceptions.NotImplementedError'>: Infinite loop in multiplication of [1.0000000000000000 .. 1.0000000000000000]*I (parent Complex Interval Field with 53 bits of precision) and 
                                       0 (parent Symbolic Ring)!}}}


---

Comment by mhansen created at 2008-09-19 06:56:43

I now get this:


```
sage: SR(0) * CIF(I)
0
sage: _.parent()
Complex Interval Field with 53 bits of precision
```


Is that the result you wanted?


---

Comment by roed created at 2009-01-22 10:08:10

I would say that this is still wrong.  In particular, the result

```
sage: CIF.has_coerce_map_from(SR)
True
```

is incorrect.  But fixing that needs to wait on more general coercion rewrites.

Replying to [comment:1 mhansen]:
> I now get this:
> 
> {{{
> sage: SR(0) * CIF(I)
> 0
> sage: _.parent()
> Complex Interval Field with 53 bits of precision
> }}}
> 
> Is that the result you wanted?


---

Comment by robertwb created at 2009-01-22 18:33:11

If there is a coercion, surly this is the only direction it goes, right?


---

Comment by mhansen created at 2009-06-05 01:55:58

This now works correctly with the update to pynac:


```
sage: SR(0) * CIF(I)
0
sage: a = _
sage: a.parent()
Symbolic Ring
sage: a.pyobject().parent()
Complex Interval Field with 53 bits of precision
```



---

Comment by mhansen created at 2009-06-05 01:55:58

Resolution: invalid
