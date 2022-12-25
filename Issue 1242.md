# Issue 1242: coercion problem in reduction of an elliptic curve at a prime ideal

archive/issues_001242.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: elliptic curves\n\n The lines \n\n```\n K.<s> = NumberField(x^2+23)\n OK = K.ring_of_integers()\n E = EllipticCurve([0,0,0,K(1),K(5)])\n pp = K.factor_integer(13)[0][0]\n Fpp = OK.residue_field(pp)\n E.base_extend(Fpp)\n```\n\nproduce the error\n\n```\n---------------------------------------------------------------------------\n<type 'exceptions.RuntimeError'>          Traceback (most recent call last)\n\n/local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/<ipython console> in <module>()\n\n/local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in base_extend(self, R)\n    692\n    693     def base_extend(self, R):\n--> 694         return constructor.EllipticCurve(R, [R(a) for a in self.a_invariants()])\n    695\n    696     def base_ring(self):\n\n/local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/constructor.py in EllipticCurve(x, y)\n    104             return ell_rational_field.EllipticCurve_rational_field(x, y)\n    105         elif rings.is_FiniteField(x):\n--> 106             return ell_finite_field.EllipticCurve_finite_field(x, y)\n    107         elif rings.is_pAdicField(x):\n    108             return ell_padic_field.EllipticCurve_padic_field(x, y)\n\n/local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py in __init__(self, x, y)\n     53\n     54         EllipticCurve_field.__init__(\n---> 55             self, [field(x) for x in ainvs])\n     56\n     57         self._point_class = ell_point.EllipticCurvePoint_finite_field\n\n/local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in __init__(self, ainvs, extra)\n    100             ainvs = [K(0),K(0),K(0)] + ainvs\n    101         self.__ainvs = ainvs\n--> 102         if self.discriminant() == 0:\n    103             raise ArithmeticError, \\\n    104                   \"Invariants %s define a singular curve.\"%ainvs\n\n/local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in discriminant(self)\n    839         except AttributeError:\n    840             b2, b4, b6, b8 = self.b_invariants()\n--> 841             self.__discriminant = -b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6\n    842             return self.__discriminant\n    843\n\n/local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/element.pyx in sage.structure.element.RingElement.__mul__()\n\n/local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()\n\n/local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion_c()\n\n/local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps._coercion_error()\n\n<type 'exceptions.RuntimeError'>: There is a bug in the coercion code in SAGE.\nBoth x (=0) and y (=12) are supposed to have identical parents but they don't.\nIn fact, x has parent 'Residue field of Fractional ideal (13, s - 4)'\nwhereas y has parent 'Ring of integers modulo 13'\n\nOriginal elements 0 (parent Residue field of Fractional ideal (13, s - 4)) and 12 (parent Ring of integers modulo 13) and morphisms\n<type 'NoneType'> None\n<type 'sage.rings.integer_mod.IntegerMod_to_IntegerMod'> Natural morphism:\n  From: Ring of integers modulo 13\n  To:   Residue field of Fractional ideal (13, s - 4)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/1242\n\n",
    "closed_at": "2007-12-15T13:43:54Z",
    "created_at": "2007-11-22T17:27:58Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "coercion problem in reduction of an elliptic curve at a prime ideal",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1242",
    "user": "https://github.com/categorie"
}
```
Assignee: @williamstein

Keywords: elliptic curves

 The lines 

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

Issue created by migration from https://trac.sagemath.org/ticket/1242





---

archive/issue_events_003285.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-11-23T00:13:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1242",
    "milestone": "sage-2.8.14",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1242#event-3285"
}
```



---

archive/issue_comments_007755.json:
```json
{
    "body": "Replying to [ticket:1242 wuthrich]:\n>  The lines \n\n> \n> {{{\n>  K.<s> = NumberField(x^2+23)\n>  OK = K.ring_of_integers()\n>  E = EllipticCurve([0,0,0,K(1),K(5)])\n>  pp = K.factor_integer(13)[0][0]\n>  Fpp = OK.residue_field(pp)\n>  E.base_extend(Fpp)\n> }}}\n> \n> produce the error\n> \n> ```\n> ---------------------------------------------------------------------------\n> <type 'exceptions.RuntimeError'>          Traceback (most recent call last)\n> \n> /local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/<ipython console> in <module>()\n> \n> /local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in base_extend(self, R)\n>     692\n>     693     def base_extend(self, R):\n> --> 694         return constructor.EllipticCurve(R, [R(a) for a in self.a_invariants()])\n>     695\n>     696     def base_ring(self):\n> \n> /local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/constructor.py in EllipticCurve(x, y)\n>     104             return ell_rational_field.EllipticCurve_rational_field(x, y)\n>     105         elif rings.is_FiniteField(x):\n> --> 106             return ell_finite_field.EllipticCurve_finite_field(x, y)\n>     107         elif rings.is_pAdicField(x):\n>     108             return ell_padic_field.EllipticCurve_padic_field(x, y)\n> \n> /local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_finite_field.py in __init__(self, x, y)\n>      53\n>      54         EllipticCurve_field.__init__(\n> ---> 55             self, [field(x) for x in ainvs])\n>      56\n>      57         self._point_class = ell_point.EllipticCurvePoint_finite_field\n> \n> /local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in __init__(self, ainvs, extra)\n>     100             ainvs = [K(0),K(0),K(0)] + ainvs\n>     101         self.__ainvs = ainvs\n> --> 102         if self.discriminant() == 0:\n>     103             raise ArithmeticError, \\\n>     104                   \"Invariants %s define a singular curve.\"%ainvs\n> \n> /local/pmzcw/prog/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.py in discriminant(self)\n>     839         except AttributeError:\n>     840             b2, b4, b6, b8 = self.b_invariants()\n> --> 841             self.__discriminant = -b2**2*b8 - 8*b4**3 - 27*b6**2 + 9*b2*b4*b6\n>     842             return self.__discriminant\n>     843\n> \n> /local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/element.pyx in sage.structure.element.RingElement.__mul__()\n> \n> /local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c()\n> \n> /local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion_c()\n> \n> /local/pmzcw/prog/sage-2.8.5.1/devel/sage-mine/sage/schemes/elliptic_curves/coerce.pyx in sage.structure.coerce.CoercionModel_cache_maps._coercion_error()\n> \n> <type 'exceptions.RuntimeError'>: There is a bug in the coercion code in SAGE.\n> Both x (=0) and y (=12) are supposed to have identical parents but they don't.\n> In fact, x has parent 'Residue field of Fractional ideal (13, s - 4)'\n> whereas y has parent 'Ring of integers modulo 13'\n> \n> Original elements 0 (parent Residue field of Fractional ideal (13, s - 4)) and 12 (parent Ring of integers modulo 13) and morphisms\n> <type 'NoneType'> None\n> <type 'sage.rings.integer_mod.IntegerMod_to_IntegerMod'> Natural morphism:\n>   From: Ring of integers modulo 13\n>   To:   Residue field of Fractional ideal (13, s - 4)\n\n}}}\n\nThe problem comes from the coercion in Sequence :\n{{{\nared = [Fpp(a) for a in E.a_invariants()]\n[a.parent() for a in ared]\n}}}\ngives\n{{{\n[Residue field of Fractional ideal (13, s - 4), Residue field of\nFractional ideal (13, s - 4), Residue field of Fractional ideal (13, s -\n4), Ring of integers modulo 13, Residue field of Fractional ideal (13, s\n- 4)]\n}}}\nBut\n{{{\nSequence(ared)\n}}}\nfails.",
    "created_at": "2007-11-23T10:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1242#issuecomment-7755",
    "user": "https://github.com/categorie"
}
```

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
> 
> ```
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
{{{
ared = [Fpp(a) for a in E.a_invariants()]
[a.parent() for a in ared]
}}}
gives
{{{
[Residue field of Fractional ideal (13, s - 4), Residue field of
Fractional ideal (13, s - 4), Residue field of Fractional ideal (13, s -
4), Ring of integers modulo 13, Residue field of Fractional ideal (13, s
- 4)]
}}}
But
{{{
Sequence(ared)
}}}
fails.



---

archive/issue_comments_007756.json:
```json
{
    "body": "This will be fixed by #1183.",
    "created_at": "2007-12-15T09:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1242#issuecomment-7756",
    "user": "https://github.com/williamstein"
}
```

This will be fixed by #1183.



---

archive/issue_comments_007757.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T13:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1242#issuecomment-7757",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_007758.json:
```json
{
    "body": "resolved due to patch set from #1183",
    "created_at": "2007-12-15T13:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1242#issuecomment-7758",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

resolved due to patch set from #1183



---

archive/issue_events_003286.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T13:43:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1242",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1242#event-3286"
}
```
