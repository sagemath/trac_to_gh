# Issue 5663: Infinite loop in multiplication of 0 (parent Symbolic Ring) and 1.0000000000000000 (parent Real Field with 60 bits of precision)!

Issue created by migration from https://trac.sagemath.org/ticket/5663

Original creator: ncalexan

Original creation time: 2009-04-02 03:20:32

Assignee: robertwb

CC:  robertwb

Keywords: coercion symbolic ring real field


```
sage: SR(0) * RealField(60)(1)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1027, 0))

---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/ncalexan/.sage/temp/sage.math.washington.edu/19397/_home_ncalexan__sage_init_sage_0.py in <module>()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/element.so in sage.stru\
cture.element.RingElement.__mul__ (sage/structure/element.c:10558)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.struc\
ture.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6543)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.struc\
ture.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:11646)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.struc\
ture.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12920)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.struc\
ture.parent.Parent.get_action (sage/structure/parent.c:11816)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\
tructure.parent_old.Parent._get_action_ (sage/structure/parent_old.c:8141)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\
tructure.parent_old.Parent.get_action_c (sage/structure/parent_old.c:2998)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\
tructure.parent_old.Parent.get_action_impl (sage/structure/parent_old.c:3333)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\
tructure.parent_old.Parent.get_action_c_impl (sage/structure/parent_old.c:4193)()

/home/ncalexan/sage-3.4.1.alpha0-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/parent_old.so in sage.s\
tructure.parent_old._register_pair (sage/structure/parent_old.c:9303)()

NotImplementedError: Infinite loop in multiplication of
                                       0 (parent Symbolic Ring) and 1.0000000000000000 (parent Real Field with 60 bits of precision)!
```



---

Comment by mhansen created at 2009-06-05 03:07:28

This is taken care of with the switch to the new symbolics:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: SR(0) * RealField(60)(1)
0
```



---

Comment by mhansen created at 2009-06-05 03:07:28

Resolution: invalid
