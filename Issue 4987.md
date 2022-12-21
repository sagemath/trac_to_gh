# Issue 4987: [with spkg, not ready for review] Upgrade to Cython 0.11

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-01-16 09:01:33

Assignee: mabshoff

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/

Sage now compiles, most doctests pass. Memory profiling should be done as well.


---

Comment by robertwb created at 2009-01-16 10:29:07


```
The following tests failed:


        sage -t  "devel/sage/sage/coding/code_constructions.py"
        sage -t  "devel/sage/sage/coding/guava.py"
        sage -t  "devel/sage/sage/coding/linear_code.py"
        sage -t  "devel/sage/sage/crypto/mq/mpolynomialsystem.py"
        sage -t  "devel/sage/sage/crypto/mq/sbox.py"
        sage -t  "devel/sage/sage/crypto/mq/sr.py"
        sage -t  "devel/sage/sage/finance/fractal.pyx"
        sage -t  "devel/sage/sage/finance/time_series.pyx"
        sage -t  "devel/sage/sage/graphs/bipartite_graph.py"
        sage -t  "devel/sage/sage/groups/generic.py"
        sage -t  "devel/sage/sage/groups/matrix_gps/matrix_group.py"
        sage -t  "devel/sage/sage/interfaces/sage0.py"
        sage -t  "devel/sage/sage/interfaces/singular.py"
        sage -t  "devel/sage/sage/libs/ntl/ntl_GF2E.pyx"
        sage -t  "devel/sage/sage/libs/ntl/ntl_mat_GF2E.pyx"
        sage -t  "devel/sage/sage/libs/pari/gen.pyx"
        sage -t  "devel/sage/sage/matrix/matrix0.pyx"
        sage -t  "devel/sage/sage/matrix/matrix2.pyx"
        sage -t  "devel/sage/sage/matrix/matrix_integer_dense.pyx"
        sage -t  "devel/sage/sage/misc/randstate.pyx"
        sage -t  "devel/sage/sage/modular/abvar/abvar.py"
        sage -t  "devel/sage/sage/modular/abvar/abvar_newform.py"
        sage -t  "devel/sage/sage/modular/abvar/cuspidal_subgroup.py"
        sage -t  "devel/sage/sage/modular/abvar/finite_subgroup.py"
        sage -t  "devel/sage/sage/modular/abvar/homology.py"
        sage -t  "devel/sage/sage/modular/abvar/morphism.py"
        sage -t  "devel/sage/sage/modular/abvar/torsion_subgroup.py"
        sage -t  "devel/sage/sage/modular/dirichlet.py"
        sage -t  "devel/sage/sage/modular/hecke/ambient_module.py"
        sage -t  "devel/sage/sage/modular/hecke/module.py"
        sage -t  "devel/sage/sage/modular/hecke/submodule.py"
        sage -t  "devel/sage/sage/modular/modform/constructor.py"
        sage -t  "devel/sage/sage/modular/modform/element.py"
        sage -t  "devel/sage/sage/modular/modsym/ambient.py"
        sage -t  "devel/sage/sage/modular/modsym/modsym.py"
        sage -t  "devel/sage/sage/modular/modsym/space.py"
        sage -t  "devel/sage/sage/modular/ssmod/ssmod.py"
        sage -t  "devel/sage/sage/modules/free_module.py"
        sage -t  "devel/sage/sage/modules/quotient_module.py"
        sage -t  "devel/sage/sage/rings/arith.py"
        sage -t  "devel/sage/sage/rings/big_oh.py"
        sage -t  "devel/sage/sage/rings/complex_double.pyx"
        sage -t  "devel/sage/sage/rings/finite_field.py"
        sage -t  "devel/sage/sage/rings/finite_field_element.py"
        sage -t  "devel/sage/sage/rings/finite_field_givaro.pyx"
        sage -t  "devel/sage/sage/rings/finite_field_morphism.py"
        sage -t  "devel/sage/sage/rings/finite_field_ntl_gf2e.pyx"
        sage -t  "devel/sage/sage/rings/finite_field_prime_modn.py"
        sage -t  "devel/sage/sage/rings/ideal.py"
        sage -t  "devel/sage/sage/rings/laurent_series_ring.py"
        sage -t  "devel/sage/sage/rings/morphism.pyx"
        sage -t  "devel/sage/sage/rings/number_field/number_field.py"
        sage -t  "devel/sage/sage/rings/number_field/number_field_element.pyx"
        sage -t  "devel/sage/sage/rings/number_field/order.py"
        sage -t  "devel/sage/sage/rings/number_field/totallyreal.pyx"
        sage -t  "devel/sage/sage/rings/number_field/totallyreal_data.pyx"
        sage -t  "devel/sage/sage/rings/number_field/totallyreal_rel.py"
        sage -t  "devel/sage/sage/rings/padics/factory.py"
        sage -t  "devel/sage/sage/rings/padics/local_generic.py"
        sage -t  "devel/sage/sage/rings/padics/local_generic_element.pyx"
        sage -t  "devel/sage/sage/rings/padics/padic_capped_absolute_element.pyx"
        sage -t  "devel/sage/sage/rings/padics/padic_capped_relative_element.pyx"
        sage -t  "devel/sage/sage/rings/padics/padic_field_capped_relative.py"
        sage -t  "devel/sage/sage/rings/padics/padic_field_generic.py"
        sage -t  "devel/sage/sage/rings/padics/padic_field_lazy.py"
        sage -t  "devel/sage/sage/rings/padics/padic_fixed_mod_element.pyx"
        sage -t  "devel/sage/sage/rings/padics/padic_generic.py"
        sage -t  "devel/sage/sage/rings/padics/padic_generic_element.pyx"
        sage -t  "devel/sage/sage/rings/padics/padic_printing.pyx"
        sage -t  "devel/sage/sage/rings/padics/padic_ring_capped_absolute.py"
        sage -t  "devel/sage/sage/rings/padics/padic_ring_capped_relative.py"
        sage -t  "devel/sage/sage/rings/padics/padic_ring_fixed_mod.py"
        sage -t  "devel/sage/sage/rings/padics/padic_ring_generic.py"
        sage -t  "devel/sage/sage/rings/padics/padic_ring_lazy.py"
        sage -t  "devel/sage/sage/rings/padics/padic_ZZ_pX_CA_element.pyx"
        sage -t  "devel/sage/sage/rings/padics/padic_ZZ_pX_CR_element.pyx"
        sage -t  "devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx"
        sage -t  "devel/sage/sage/rings/padics/padic_ZZ_pX_FM_element.pyx"
        sage -t  "devel/sage/sage/rings/padics/pow_computer.pyx"
        sage -t  "devel/sage/sage/rings/padics/pow_computer_ext.pyx"
        sage -t  "devel/sage/sage/rings/padics/tests.py"
        sage -t  "devel/sage/sage/rings/padics/tutorial.py"
        sage -t  "devel/sage/sage/rings/polynomial/groebner_fan.py"
        sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial.pyx"
        sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
        sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx"
        sage -t  "devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py"
        sage -t  "devel/sage/sage/rings/polynomial/padics/polynomial_padic_flat.py"
        sage -t  "devel/sage/sage/rings/polynomial/polynomial_element.pyx"
        sage -t  "devel/sage/sage/rings/polynomial/polynomial_element_generic.py"
        sage -t  "devel/sage/sage/rings/polynomial/polynomial_integer_dense_flint.pyx"
        sage -t  "devel/sage/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx"
        sage -t  "devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py"
        sage -t  "devel/sage/sage/rings/polynomial/polynomial_quotient_ring_element.py"
        sage -t  "devel/sage/sage/rings/polynomial/polynomial_ring.py"
        sage -t  "devel/sage/sage/rings/polynomial/polynomial_singular_interface.py"
        sage -t  "devel/sage/sage/rings/polynomial/real_roots.pyx"
        sage -t  "devel/sage/sage/rings/power_series_ring_element.pyx"
        sage -t  "devel/sage/sage/rings/residue_field.pyx"
        sage -t  "devel/sage/sage/rings/ring.pyx"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_generic.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_number_field.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_padic_field.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_point.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_torsion.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/padic_lseries.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/padics.py"
        sage -t  "devel/sage/sage/schemes/elliptic_curves/sha_tate.py"
        sage -t  "devel/sage/sage/schemes/generic/scheme.py"
        sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/constructor.py"
        sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hypellfrob.pyx"
        sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py"
        sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py"
        sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py"
        sage -t  "devel/sage/sage/schemes/hyperelliptic_curves/jacobian_morphism.py"
        sage -t  "devel/sage/sage/structure/element.pyx"
        sage -t  "devel/sage/sage/structure/parent.pyx"
        sage -t  "devel/sage/sage/structure/parent_gens.pyx"
        sage -t  "devel/sage/sage/structure/sage_object.pyx"
        sage -t  "devel/sage/sage/tests/benchmark.py"
        sage -t  "devel/sage/sage/tests/book_stein_modform.py"
```


Most of them

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.


---

Comment by robertwb created at 2009-01-19 22:54:15

Down to 


```
        sage -t  "devel/sage/sage/finance/fractal.pyx"
        sage -t  "devel/sage/sage/finance/time_series.pyx"
        sage -t  "devel/sage/sage/interfaces/sage0.py"
        sage -t  "devel/sage/sage/misc/randstate.pyx"
        sage -t  "devel/sage/sage/rings/complex_double.pyx"
        sage -t  "devel/sage/sage/rings/number_field/totallyreal_data.pyx"

```



---

Comment by robertwb created at 2009-01-19 23:43:25

All of these are some kind of numerical error, but it looks more severe than your typical "numerical noise" so we'll need to look deeper.


---

Comment by robertwb created at 2009-01-20 02:29:27

I believe I've located the issue: 

http://trac.cython.org/cython_trac/ticket/190

Recompiling right now.


---

Comment by robertwb created at 2009-01-20 02:41:15

Yep, that fixes the files above.


---

Comment by robertwb created at 2009-02-20 10:49:04

Note the spkg is out of date, pull from cython-devel.


---

Comment by robertwb created at 2009-02-20 11:36:08

spkg in http://sage.math.washington.edu/home/robertwb/cython/ is up to date.


---

Comment by robertwb created at 2009-02-20 12:12:46

A lot of refnanny errors in the coercion code: 


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/rings/padics/padic_printing.cpp: __init__()
References leaked: 
  Acquired on lines: 4278, 4287, 4345, 4354, 4412, 4421
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent.c: convert_map_from()
NULL argument on line 10437
Too many decrefs on line 10458, reference acquired on lines []
sage/structure/parent_old.c: has_coerce_map_from_c()
NULL argument on line 6200
Too many decrefs on line 6221, reference acquired on lines []
sage/structure/parent_old.c: _coerce_c()
NULL argument on line 5157
Too many decrefs on line 5178, reference acquired on lines []
sage/structure/parent_old.c: _coerce_c()
NULL argument on line 5157
Too many decrefs on line 5178, reference acquired on lines []
sage/structure/parent_old.c: has_coerce_map_from_c()
NULL argument on line 6200
Too many decrefs on line 6221, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4766, reference acquired on lines []
sage/structure/parent_old.c: coerce_map_from_c()
NULL argument on line 1361
Too many decrefs on line 1382, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4766, reference acquired on lines []
sage/structure/parent_old.c: coerce_map_from_c()
NULL argument on line 1361
Too many decrefs on line 1382, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8053, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent_old.c: has_coerce_map_from_c()
NULL argument on line 6200
Too many decrefs on line 6221, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent_old.c: coerce_map_from_c()
NULL argument on line 1361
Too many decrefs on line 1382, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8053, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/element.c: _sub_()
NULL argument on line 7564
Too many decrefs on line 7577, reference acquired on lines []
sage/rings/polynomial/polynomial_element.c: _sub_()
NULL argument on line 42791
Too many decrefs on line 42813, reference acquired on lines []
sage/structure/factory.c: get_version()
NULL argument on line 1596
Too many decrefs on line 1617, reference acquired on lines []
sage/structure/factory.c: other_keys()
NULL argument on line 1924
Too many decrefs on line 1948, reference acquired on lines []
sage/structure/factory.c: get_object()
NULL argument on line 819
Too many decrefs on line 846, reference acquired on lines []
sage/structure/factory.c: get_version()
NULL argument on line 1596
Too many decrefs on line 1617, reference acquired on lines []
sage/structure/factory.c: get_object()
NULL argument on line 819
Too many decrefs on line 846, reference acquired on lines []
sage/structure/factory.c: get_version()
NULL argument on line 1596
Too many decrefs on line 1617, reference acquired on lines []
sage/structure/factory.c: other_keys()
NULL argument on line 1924
Too many decrefs on line 1940, reference acquired on lines []
sage/structure/factory.c: get_object()
NULL argument on line 819
Too many decrefs on line 846, reference acquired on lines []
References leaked: 
  Acquired on lines: 1048, 1114
  Acquired on lines: 1049, 1115
  Acquired on lines: 1050, 1116
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent_old.c: _an_element_()
NULL argument on line 8393
Too many decrefs on line 8400, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent_old.c: _coerce_c()
NULL argument on line 5157
Too many decrefs on line 5178, reference acquired on lines []
sage/structure/parent_old.c: has_coerce_map_from_c()
NULL argument on line 6200
Too many decrefs on line 6221, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4766, reference acquired on lines []
sage/structure/parent_old.c: coerce_map_from_c()
NULL argument on line 1361
Too many decrefs on line 1382, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8053, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent.c: _convert_map_from_()
NULL argument on line 11296
Too many decrefs on line 11317, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent_old.c: _generic_convert_map()
NULL argument on line 8540
Too many decrefs on line 8561, reference acquired on lines []
sage/structure/parent.c: convert_map_from()
NULL argument on line 10437
Too many decrefs on line 10458, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4766, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent.c: convert_map_from()
NULL argument on line 10437
Too many decrefs on line 10458, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent.c: has_coerce_map_from()
NULL argument on line 8562
Too many decrefs on line 8585, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent.c: convert_map_from()
NULL argument on line 10437
Too many decrefs on line 10458, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent.c: convert_map_from()
NULL argument on line 10437
Too many decrefs on line 10458, reference acquired on lines []
sage/structure/parent_old.c: _an_element_c()
NULL argument on line 7421
Too many decrefs on line 7434, reference acquired on lines []
sage/structure/parent_old.c: _an_element_()
NULL argument on line 8393
Too many decrefs on line 8406, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/rings/polynomial/polynomial_element.c: _mul_()
NULL argument on line 10869
Too many decrefs on line 10882, reference acquired on lines []
sage/rings/polynomial/polynomial_element.c: _lmul_()
NULL argument on line 5211
Too many decrefs on line 5233, reference acquired on lines []
sage/structure/parent_old.c: get_action_c()
NULL argument on line 2800
Too many decrefs on line 2831, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/rings/polynomial/polynomial_element.c: _mul_()
NULL argument on line 10869
Too many decrefs on line 10882, reference acquired on lines []
sage/rings/polynomial/polynomial_element.c: _lmul_()
NULL argument on line 5211
Too many decrefs on line 5233, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/rings/polynomial/polynomial_element.c: _mul_()
NULL argument on line 10869
Too many decrefs on line 10882, reference acquired on lines []
sage/rings/polynomial/polynomial_element.c: _lmul_()
NULL argument on line 5211
Too many decrefs on line 5233, reference acquired on lines []
sage/structure/parent_old.c: get_action_c()
NULL argument on line 2800
Too many decrefs on line 2831, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: get_action_c()
NULL argument on line 2800
Too many decrefs on line 2831, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/element.c: _add_()
NULL argument on line 7103
Too many decrefs on line 7116, reference acquired on lines []
sage/rings/polynomial/polynomial_element.c: _add_()
NULL argument on line 42088
Too many decrefs on line 42110, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent.c: has_coerce_map_from()
NULL argument on line 8562
Too many decrefs on line 8585, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent_old.c: _an_element_()
NULL argument on line 8393
Too many decrefs on line 8406, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent_old.c: _an_element_c()
NULL argument on line 7421
Too many decrefs on line 7434, reference acquired on lines []
sage/structure/parent_old.c: _an_element_()
NULL argument on line 8393
Too many decrefs on line 8406, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/structure/parent_old.c: get_action_c()
NULL argument on line 2800
Too many decrefs on line 2831, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8045, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent.c: an_element()
NULL argument on line 13813
Too many decrefs on line 13826, reference acquired on lines []
sage/structure/parent_old.c: _coerce_c()
NULL argument on line 5157
Too many decrefs on line 5178, reference acquired on lines []
sage/structure/parent_old.c: has_coerce_map_from_c()
NULL argument on line 6200
Too many decrefs on line 6221, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4775, reference acquired on lines []
sage/rings/ring.c: is_exact()
NULL argument on line 4760
Too many decrefs on line 4766, reference acquired on lines []
sage/structure/parent_old.c: coerce_map_from_c()
NULL argument on line 1361
Too many decrefs on line 1382, reference acquired on lines []
sage/structure/parent_old.c: _coerce_map_from_()
NULL argument on line 8032
Too many decrefs on line 8053, reference acquired on lines []
sage/structure/parent.c: coerce_map_from()
NULL argument on line 8916
Too many decrefs on line 8937, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
sage/structure/parent_old.c: get_action_c()
NULL argument on line 2800
Too many decrefs on line 2831, reference acquired on lines []
sage/structure/parent_old.c: _get_action_()
NULL argument on line 8182
Too many decrefs on line 8213, reference acquired on lines []
sage/structure/parent.c: get_action()
NULL argument on line 11428
Too many decrefs on line 11459, reference acquired on lines []
```



---

Comment by robertwb created at 2009-02-20 12:19:26

BTW


```
robert$ cat | sort | uniq | wc
      85     522    3808
```


So there are about 30 distinct places it complains about.


---

Comment by robertwb created at 2009-02-20 23:07:26

Fixed cpdef refnanny bug, now 


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage/rings/padics/padic_printing.cpp: __init__()
References leaked: 
  Acquired on lines: 4278, 4287, 4345, 4354, 4412, 4421
sage/structure/factory.c: get_object()
References leaked: 
  Acquired on lines: 1048, 1114
  Acquired on lines: 1049, 1115
  Acquired on lines: 1050, 1116
sage: 
Exiting SAGE (CPU time 0m0.07s, Wall time 2m13.31s).
Exception exceptions.AssertionError in  ignored
Exception exceptions.AssertionError in  ignored
Exception exceptions.AssertionError in /Users/robert/sage/sage-cython/local/bin/sage-sage: line 587: 16443 Bus error               sage-ipython "$`@`" -i
```



---

Comment by robertwb created at 2009-02-21 06:58:49

New spkg posted, Sage starts up fine, but still segfaults on exit.


---

Comment by mabshoff created at 2009-02-21 08:41:06

Replying to [comment:11 robertwb]:
> New spkg posted, Sage starts up fine, but still segfaults on exit. 

With this spkg building the Sage library og 3.3.alpha3 breaks on sage.math due to

```
/*
   I get really sick of typing unsigned long.
*/
typedef unsigned long  ulong;

```

in 

```
building 'sage.rings.polynomial.polynomial_zmod_flint' extension
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC 
-DCYTHON_REFNANNY=1 -I/scratch/mabshoff/sage-3.3.alpha3-vg/local/include/FLINT/ 
-I/scratch/mabshoff/sage-3.3.alpha3-vg/local//include -I/scratch/mabshoff/sage-
3.3.alpha3-vg/local//include/csage -I/scratch/mabshoff/sage-3.3.alpha3-vg/devel//sage
/sage/ext -I/scratch/mabshoff/sage-3.3.alpha3-vg/local/include/python2.5 -c sage/rings
/polynomial/polynomial_zmod_flint.c -o build/temp.linux-x86_64-2.5/sage/rings
/polynomial/polynomial_zmod_flint.o -std=c99 -D_XPG6 -w
In file included from sage/rings/polynomial/polynomial_zmod_flint.c:140:
/scratch/mabshoff/sage-3.3.alpha3-vg/local//include/zn_poly/zn_poly.h:72: error: duplicate ‘unsigned’
error: command 'gcc' failed with exit status 1
```



---

Attachment


---

Comment by robertwb created at 2009-02-26 05:50:23

Sage 3.3 compiles, starts, and exits without errors or segfauting with the attached patch, and the latest spkg.


---

Comment by mabshoff created at 2009-02-26 06:03:20

Replying to [comment:13 robertwb]:
> Sage 3.3 compiles, starts, and exits without errors or segfauting with the attached patch, and the latest spkg. 

Awesome. Is that also with the refnanny enabled?

I also saw something being fixed today in regard to another reference leak, so I am interesting in trying this.

How close is this to being ready? I don't want this in 3.4 for obvious reasons, but 3.4.1 seems like a strong possibility.

Cheers,

Michael


---

Comment by robertwb created at 2009-02-26 07:16:44

Yes, with the refnanny. 3.4.1 seems a likely target--I haven't run a testall yet, but the last testall has surprisingly few unique errors.


---

Comment by robertwb created at 2009-02-26 09:02:05

testall log at http://sage.math.washington.edu/home/robertwb/sage-3.3/devel/sage-main/log.txt

Is there a way to only log failed tests?


---

Comment by robertwb created at 2009-02-26 22:53:01

The only remaining errors are 


```
	./sage -t  "devel/sage/sage/coding/decoder.py"
	./sage -t  "devel/sage/sage/rings/bernmm.pyx"
	./sage -t  "devel/sage/sage/rings/qqbar.py"
	./sage -t  "devel/sage/sage/combinat/root_system/weyl_characters.py"
	./sage -t  "devel/sage/sage/modular/abvar/abvar.py"
	./sage -t  "devel/sage/sage/modular/abvar/homspace.py"
```


Which all timeout.


---

Comment by robertwb created at 2009-03-08 07:20:37

All tests pass, and we're getting close to a release. 

Note that the current patch enables the refnanny, which should be changed before release.


---

Attachment

Apply this one. (Exactly the same as above, but doesn't enable the refnanny.)


---

Comment by robertwb created at 2009-03-14 08:00:51

Sage compiles, passes all doctests, and Cython 0.11 is out. Time to ship.


---

Comment by cwitty created at 2009-03-19 02:14:22

Starting from Sage 3.4, I applied the patch, installed the Cython spkg, did "sage -ba", and did a full test run -- all tests passed.  Also, I read the patch, and it looked entirely reasonable.

So, positive review on the patch.  I did take a quick look at the spkg, but I didn't look closely enough to feel comfortable giving it a review; I did notice a couple of problems, though:

1) SPKG.txt has a mixture of line endings: some lines end with CR, some with LF

2) "cython -V" doesn't believe it's 0.11 final:

```
sage$ cython -V
Cython version 0.11.rc3
```



---

Comment by robertwb created at 2009-03-19 06:25:10

I posted a new spkg, fixing the newlines of SPKG.txt, and adding the final commit for 0.11 final (which only changed the version number). 

Given that everything builds and passes tests, I don't know how much more reviewing of the spkg itself is necessary--certainly no one is expecting reviewers to referee the entire upstream changes. It'd be nice if we can get this into 3.4.1.


---

Comment by mabshoff created at 2009-03-25 10:18:47

I am signing off on the spkg because I am sure that upstream has improved Cython. I did a complete build cycle of the Sage library and doctests pass after applying the patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 10:19:59

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 10:19:59

Resolution: fixed


---

Comment by robertwb created at 2009-04-10 09:23:37

Changing status from closed to reopened.


---

Comment by robertwb created at 2009-04-10 09:23:37

Resolution changed from fixed to 


---

Comment by robertwb created at 2009-04-10 09:23:37

Speed profiling should be done as well!

0.10.3

```
sage: sage: time set_random_seed(11); M = random_matrix(QQ, 100, 100); M.echelonize()
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.03 s
```


0.11

```
sage: time set_random_seed(11); M = random_matrix(QQ, 100, 100); M.echelonize()
CPU times: user 0.46 s, sys: 0.00 s, total: 0.46 s
Wall time: 0.46 s
```


This is a blocker for 0.11.1


---

Comment by mabshoff created at 2009-04-10 10:22:28

Resolution: fixed


---

Comment by mabshoff created at 2009-04-10 10:22:28

Hi Robert,

is is customary to open another ticket for an issue found in a closed ticket, so I am closing this again. Please open another ticket. I am surprised that there is a such a speed regression since no one has observed it.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-10 10:23:06

The spkg itself was fine, so I am changing the title back.

Cheers,

Michael


---

Comment by robertwb created at 2009-04-10 18:45:17

The point was to revert the spkg and not ship 0.11 in Sage 3.4.1, as I didn't think a fix would be out in time. However, I'm not seeing the speed regression in your rc, so I'm mystified but we can go ahead and leave this closed. 

BTW, the timings above were done with the 3.4 release, the only difference was moving Cython from 0.10.3 to 0.11.


---

Comment by robertwb created at 2009-04-10 19:08:14

Sorry for the noise--the refnanny was enabled on my 0.11 builds. Whew, I was really worried there for a bit.
