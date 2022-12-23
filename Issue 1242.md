# Issue 1242: coercion problem in reduction of an elliptic curve at a prime ideal

Issue created by migration from https://trac.sagemath.org/ticket/1242

Original creator: wuthrich

Original creation time: 2007-11-22 17:27:58

Assignee: was

Keywords: elliptic curves

*The lines 


```
 K.<s> = NumberField(x^2+23)
 OK = K.ring_of_integers()
 E = EllipticCurve([0,0,0,K(1),K(5)])
 pp = K.factor_integer(13)[0][0]
 Fpp = OK.residue_field(pp)
 E.base_extend(Fpp)
```


produce the error

```
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call last)

/local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/<ipython console> in <module>()

/local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in base_extend(self, R)
    692
    693     def base_extend(self, R):
--> 694         return constructor.EllipticCurve(R, [R(a) for a in self.a_invariants()])
    695
    696     def base_ring(self):

/local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/constructor.py in EllipticCurve(x, y)
    104             return ell_rational_field.EllipticCurve_rational_field(x, y)
    105         elif rings.is_FiniteField(x):
--> 106             return ell_finite_field.EllipticCurve_finite_field(x, y)
    107         elif rings.is_pAdicField(x):
    108             return ell_padic_field.EllipticCurve_padic_field(x, y)

/local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py in __init__(self, x, y)
     53
     54         EllipticCurve_field.__init__(
---> 55             self, [field(x) for x in ainvs])
     56
     57         self._point_class = ell_point.EllipticCurvePoint_finite_field

/local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in __init__(self, ainvs, extra)
    100             ainvs = [K(0),K(0),K(0)] + ainvs
    101         self.__ainvs = ainvs
--> 102         if self.discriminant() == 0:
    103             raise ArithmeticError, \
    104                   "Invariants %s define a singular curve."%ainvs

/local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in discriminant(self)
    839         except AttributeError:
    840             b2, b4, b6, b8 = self.b_invariants()
--> 841             self.__discriminant = -b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
    842             return self.__discriminant
    843

/local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/element.pyx in sage.structure.element.RingElement.__mul__()

/local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()

/local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion_c()

/local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps._coercion_error()

<type 'exceptions.RuntimeError'>: There is a bug in the coercion code in SAGE.
Both x (=0) and y (=12) are supposed to have identical parents but they don't.
In fact, x has parent 'Residue field of Fractional ideal (13, s - 4)'
whereas y has parent 'Ring of integers modulo 13'

Original elements 0 (parent Residue field of Fractional ideal (13, s - 4)) and 12 (parent Ring of integers modulo 13) and morphisms
<type 'NoneType'> None
<type 'sage.rings.integer_mod.IntegerMod_to_IntegerMod'> Natural morphism:
  From: Ring of integers modulo 13
  To:   Residue field of Fractional ideal (13, s - 4)
```



---

Comment by wuthrich created at 2007-11-23 10:57:57

Replying to [ticket:1242 wuthrich]:
>  The lines 
> 
> {{{
>  K.<s> = NumberField(x^2+23)
>  OK = K.ring_of_integers()
>  E = EllipticCurve([0,0,0,K(1),K(5)])
>  pp = K.factor_integer(13)[0][0]
>  Fpp = OK.residue_field(pp)
>  E.base_extend(Fpp)
> }}}
> 
> produce the error
> {{{
> ---------------------------------------------------------------------------
> <type 'exceptions.RuntimeError'>          Traceback (most recent call last)
> 
> /local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/<ipython console> in <module>()
> 
> /local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in base_extend(self, R)
>     692
>     693     def base_extend(self, R):
> --> 694         return constructor.EllipticCurve(R, [R(a) for a in self.a_invariants()])
>     695
>     696     def base_ring(self):
> 
> /local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/constructor.py in EllipticCurve(x, y)
>     104             return ell_rational_field.EllipticCurve_rational_field(x, y)
>     105         elif rings.is_FiniteField(x):
> --> 106             return ell_finite_field.EllipticCurve_finite_field(x, y)
>     107         elif rings.is_pAdicField(x):
>     108             return ell_padic_field.EllipticCurve_padic_field(x, y)
> 
> /local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py in __init__(self, x, y)
>      53
>      54         EllipticCurve_field.__init__(
> ---> 55             self, [field(x) for x in ainvs])
>      56
>      57         self._point_class = ell_point.EllipticCurvePoint_finite_field
> 
> /local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in __init__(self, ainvs, extra)
>     100             ainvs = [K(0),K(0),K(0)] + ainvs
>     101         self.__ainvs = ainvs
> --> 102         if self.discriminant() == 0:
>     103             raise ArithmeticError, \
>     104                   "Invariants %s define a singular curve."%ainvs
> 
> /local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in discriminant(self)
>     839         except AttributeError:
>     840             b2, b4, b6, b8 = self.b_invariants()
> --> 841             self.__discriminant = -b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6
>     842             return self.__discriminant
>     843
> 
> /local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/element.pyx in sage.structure.element.RingElement.__mul__()
> 
> /local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()
> 
> /local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion_c()
> 
> /local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps._coercion_error()
> 
> <type 'exceptions.RuntimeError'>: There is a bug in the coercion code in SAGE.
> Both x (=0) and y (=12) are supposed to have identical parents but they don't.
> In fact, x has parent 'Residue field of Fractional ideal (13, s - 4)'
> whereas y has parent 'Ring of integers modulo 13'
> 
> Original elements 0 (parent Residue field of Fractional ideal (13, s - 4)) and 12 (parent Ring of integers modulo 13) and morphisms
> <type 'NoneType'> None
> <type 'sage.rings.integer_mod.IntegerMod_to_IntegerMod'> Natural morphism:
>   From: Ring of integers modulo 13
>   To:   Residue field of Fractional ideal (13, s - 4)
}}}

The problem comes from the coercion in Sequence :

```
ared = [Fpp(a) for a in E.a_invariants()]
[a.parent() for a in ared]
```

gives

```
[Residue field of Fractional ideal (13, s - 4), Residue field of
Fractional ideal (13, s - 4), Residue field of Fractional ideal (13, s -
4), Ring of integers modulo 13, Residue field of Fractional ideal (13, s
- 4)]
```

But

```
Sequence(ared)
```

fails.


---

Comment by was created at 2007-12-15 09:12:37

This will be fixed by #1183.


---

Comment by mabshoff created at 2007-12-15 13:43:54

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 13:43:54

resolved due to patch set from #1183
