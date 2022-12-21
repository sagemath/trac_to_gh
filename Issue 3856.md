# Issue 3856: Multiply between QQ and GF(7) gives exception

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-08-14 20:53:11

Assignee: robertwb


```
sage: 1/4*GF(7)['t'](1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/gfurnish/coercion-test/sage-3.1.alpha2-sage.math-only-x86_64-Linux/<ipython console> in <module>()

/home/gfurnish/coercion-test/sage-3.1.alpha2-sage.math-only-x86_64-Linux/element.pyx in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:9190)()

/home/gfurnish/coercion-test/sage-3.1.alpha2-sage.math-only-x86_64-Linux/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6288)()

TypeError: unsupported operand parent(s) for '*': 'Rational Field' and 'Univariate Polynomial Ring in t over Finite Field of size 7'
```

This is implied to work by the following doctest in coercion_maps.pyx

```
            sage: mor = NamedConvertMap(SR, GF(7)[This is the Trac macro *'t'* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#'t'-macro), '_polynomial_')
            sage: mor(x^2/4+1)
            1 + 2*t^2
```



---

Comment by robertwb created at 2008-08-14 21:31:51

I don't think this is a bug, this should *not* work. Conversion != Coercion.


---

Comment by gfurnish created at 2008-08-15 19:31:25

So _polynomial_ should also create any underlying conversions needed?


---

Comment by mabshoff created at 2008-08-26 09:58:32

Resolution: invalid


---

Comment by mabshoff created at 2008-08-26 09:58:32

Replying to [comment:1 robertwb]:
> I don't think this is a bug, this should *not* work. Conversion != Coercion. 

Hence this is invalid.

Cheers,

Michael
