# Issue 3605: ell_finite_field.py: libSingular - "Use of uninitialised value of size 8"

Issue created by migration from https://trac.sagemath.org/ticket/3605

Original creator: mabshoff

Original creation time: 2008-07-08 11:46:34

Assignee: mabshoff


```

==12084== Use of uninitialised value of size 8
==12084==    at 0x66EFEDB: NTL::coeff(NTL::GF2X const&, long) (GF2.h:30)
==12084==    by 0x13738433: __pyx_f_4sage_4libs_8singular_8singular_10Conversion_sa2si_GFqNTLGF2E (singular.cpp:3249)
==12084==    by 0x13736F2F: __pyx_f_4sage_4libs_8singular_8singular_10Conversion_sa2si (singular.cpp:3951)
==12084==    by 0x1304DF98: __pyx_f_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular__rmul_c_impl(__pyx_obj_4sage_5rings_10polynomial_28multi_polynomial_libsingular_MPolynomial_libs
ingular*, __pyx_obj_4sage_9structure_7element_RingElement*) (multi_polynomial_libsingular.cpp:12176)
==12084==    by 0xA9A555D: __pyx_f_4sage_9structure_6coerce__rmul_c (coerce.c:2676)
==12084==    by 0xA9A520E: __pyx_f_4sage_9structure_6coerce_16LeftModuleAction__call_c_impl (coerce.c:13538)
==12084==    by 0xAAC442E: __pyx_f_4sage_10categories_6action_6Action__call_c (action.c:1771)
==12084==    by 0xA98592C: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:5305)
==12084==    by 0xA70C9C8: __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (element.c:8812)
==12084==    by 0x4179E7: binary_op1 (abstract.c:398)
==12084==    by 0x418600: PyNumber_Multiply (abstract.c:669)
==12084==    by 0x48C2D0: PyEval_EvalFrameEx (ceval.c:1073)

==12084== Conditional jump or move depends on uninitialised value(s)
==12084==    at 0x13327103: naInit(int) (longalg.cc:908)
==12084==    by 0x13738443: __pyx_f_4sage_4libs_8singular_8singular_10Conversion_sa2si_GFqNTLGF2E (singular.cpp:3249)
==12084==    by 0x13736F2F: __pyx_f_4sage_4libs_8singular_8singular_10Conversion_sa2si (singular.cpp:3951)
==12084==    by 0x1304DF98: __pyx_f_4sage_5rings_10polynomial_28multi_polynomial_libsingular_23MPolynomial_libsingular__rmul_c_impl(__pyx_obj_4sage_5rings_10polynomial_28multi_polynomial_libsingular_MPolynomial_libs
ingular*, __pyx_obj_4sage_9structure_7element_RingElement*) (multi_polynomial_libsingular.cpp:12176)
==12084==    by 0xA9A555D: __pyx_f_4sage_9structure_6coerce__rmul_c (coerce.c:2676)
==12084==    by 0xA9A520E: __pyx_f_4sage_9structure_6coerce_16LeftModuleAction__call_c_impl (coerce.c:13538)
==12084==    by 0xAAC442E: __pyx_f_4sage_10categories_6action_6Action__call_c (action.c:1771)
==12084==    by 0xA98592C: __pyx_f_4sage_9structure_6coerce_24CoercionModel_cache_maps_bin_op_c (coerce.c:5305)
==12084==    by 0xA70C9C8: __pyx_pf_4sage_9structure_7element_11RingElement___mul__ (element.c:8812)
==12084==    by 0x4179E7: binary_op1 (abstract.c:398)
==12084==    by 0x418600: PyNumber_Multiply (abstract.c:669)
==12084==    by 0x48C2D0: PyEval_EvalFrameEx (ceval.c:1073)
```



---

Comment by cremona created at 2008-08-09 20:52:29

Is there any clue which function in ell_finite_field.py is causing this?  John


---

Comment by mabshoff created at 2008-09-22 08:28:30

Replying to [comment:1 cremona]:
> Is there any clue which function in ell_finite_field.py is causing this?  John

Nope, I can only detect this in a doctest, but I will attempt to track this down this week.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-26 16:25:07

Resolution: fixed


---

Comment by mabshoff created at 2008-10-26 16:25:07

The problem is gone in Sage 3.1.4:

```
==30839==    /scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/.doctest_ell_finite_field.py
==30839== 
--30839-- DWARF2 CFI reader: unhandled CFI instruction 0:10
--30839-- DWARF2 CFI reader: unhandled CFI instruction 0:10
==30839== 
==30839== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 598 from 2)
```


Cheers,

Michael


---

Comment by cremona created at 2008-10-26 17:27:06

Replying to [comment:3 mabshoff]:
> The problem is gone in Sage 3.1.4:
> {{{
> ==30839==    /scratch/mabshoff/release-cycle/sage-3.1.3.final/tmp/.doctest_ell_finite_field.py
> ==30839== 
> --30839-- DWARF2 CFI reader: unhandled CFI instruction 0:10
> --30839-- DWARF2 CFI reader: unhandled CFI instruction 0:10
> ==30839== 
> ==30839== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 598 from 2)
> }}}
> 
> Cheers,
> 
> Michael

Yippee!
