# Issue 4987: [with spkg, not ready for review] Upgrade to Cython 0.11

archive/issues_004987.json:
```json
{
    "body": "Assignee: mabshoff\n\nSpkg up at http://sage.math.washington.edu/home/robertwb/cython/\n\nSage now compiles, most doctests pass. Memory profiling should be done as well.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4987\n\n",
    "created_at": "2009-01-16T09:01:33Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with spkg, not ready for review] Upgrade to Cython 0.11",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4987",
    "user": "@robertwb"
}
```
Assignee: mabshoff

Spkg up at http://sage.math.washington.edu/home/robertwb/cython/

Sage now compiles, most doctests pass. Memory profiling should be done as well.

Issue created by migration from https://trac.sagemath.org/ticket/4987





---

archive/issue_comments_038035.json:
```json
{
    "body": "\n```\nThe following tests failed:\n\n\n        sage -t  \"devel/sage/sage/coding/code_constructions.py\"\n        sage -t  \"devel/sage/sage/coding/guava.py\"\n        sage -t  \"devel/sage/sage/coding/linear_code.py\"\n        sage -t  \"devel/sage/sage/crypto/mq/mpolynomialsystem.py\"\n        sage -t  \"devel/sage/sage/crypto/mq/sbox.py\"\n        sage -t  \"devel/sage/sage/crypto/mq/sr.py\"\n        sage -t  \"devel/sage/sage/finance/fractal.pyx\"\n        sage -t  \"devel/sage/sage/finance/time_series.pyx\"\n        sage -t  \"devel/sage/sage/graphs/bipartite_graph.py\"\n        sage -t  \"devel/sage/sage/groups/generic.py\"\n        sage -t  \"devel/sage/sage/groups/matrix_gps/matrix_group.py\"\n        sage -t  \"devel/sage/sage/interfaces/sage0.py\"\n        sage -t  \"devel/sage/sage/interfaces/singular.py\"\n        sage -t  \"devel/sage/sage/libs/ntl/ntl_GF2E.pyx\"\n        sage -t  \"devel/sage/sage/libs/ntl/ntl_mat_GF2E.pyx\"\n        sage -t  \"devel/sage/sage/libs/pari/gen.pyx\"\n        sage -t  \"devel/sage/sage/matrix/matrix0.pyx\"\n        sage -t  \"devel/sage/sage/matrix/matrix2.pyx\"\n        sage -t  \"devel/sage/sage/matrix/matrix_integer_dense.pyx\"\n        sage -t  \"devel/sage/sage/misc/randstate.pyx\"\n        sage -t  \"devel/sage/sage/modular/abvar/abvar.py\"\n        sage -t  \"devel/sage/sage/modular/abvar/abvar_newform.py\"\n        sage -t  \"devel/sage/sage/modular/abvar/cuspidal_subgroup.py\"\n        sage -t  \"devel/sage/sage/modular/abvar/finite_subgroup.py\"\n        sage -t  \"devel/sage/sage/modular/abvar/homology.py\"\n        sage -t  \"devel/sage/sage/modular/abvar/morphism.py\"\n        sage -t  \"devel/sage/sage/modular/abvar/torsion_subgroup.py\"\n        sage -t  \"devel/sage/sage/modular/dirichlet.py\"\n        sage -t  \"devel/sage/sage/modular/hecke/ambient_module.py\"\n        sage -t  \"devel/sage/sage/modular/hecke/module.py\"\n        sage -t  \"devel/sage/sage/modular/hecke/submodule.py\"\n        sage -t  \"devel/sage/sage/modular/modform/constructor.py\"\n        sage -t  \"devel/sage/sage/modular/modform/element.py\"\n        sage -t  \"devel/sage/sage/modular/modsym/ambient.py\"\n        sage -t  \"devel/sage/sage/modular/modsym/modsym.py\"\n        sage -t  \"devel/sage/sage/modular/modsym/space.py\"\n        sage -t  \"devel/sage/sage/modular/ssmod/ssmod.py\"\n        sage -t  \"devel/sage/sage/modules/free_module.py\"\n        sage -t  \"devel/sage/sage/modules/quotient_module.py\"\n        sage -t  \"devel/sage/sage/rings/arith.py\"\n        sage -t  \"devel/sage/sage/rings/big_oh.py\"\n        sage -t  \"devel/sage/sage/rings/complex_double.pyx\"\n        sage -t  \"devel/sage/sage/rings/finite_field.py\"\n        sage -t  \"devel/sage/sage/rings/finite_field_element.py\"\n        sage -t  \"devel/sage/sage/rings/finite_field_givaro.pyx\"\n        sage -t  \"devel/sage/sage/rings/finite_field_morphism.py\"\n        sage -t  \"devel/sage/sage/rings/finite_field_ntl_gf2e.pyx\"\n        sage -t  \"devel/sage/sage/rings/finite_field_prime_modn.py\"\n        sage -t  \"devel/sage/sage/rings/ideal.py\"\n        sage -t  \"devel/sage/sage/rings/laurent_series_ring.py\"\n        sage -t  \"devel/sage/sage/rings/morphism.pyx\"\n        sage -t  \"devel/sage/sage/rings/number_field/number_field.py\"\n        sage -t  \"devel/sage/sage/rings/number_field/number_field_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/number_field/order.py\"\n        sage -t  \"devel/sage/sage/rings/number_field/totallyreal.pyx\"\n        sage -t  \"devel/sage/sage/rings/number_field/totallyreal_data.pyx\"\n        sage -t  \"devel/sage/sage/rings/number_field/totallyreal_rel.py\"\n        sage -t  \"devel/sage/sage/rings/padics/factory.py\"\n        sage -t  \"devel/sage/sage/rings/padics/local_generic.py\"\n        sage -t  \"devel/sage/sage/rings/padics/local_generic_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_capped_absolute_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_capped_relative_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_field_capped_relative.py\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_field_generic.py\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_field_lazy.py\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_fixed_mod_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_generic.py\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_generic_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_printing.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_ring_capped_absolute.py\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_ring_capped_relative.py\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_ring_fixed_mod.py\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_ring_generic.py\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_ring_lazy.py\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_ZZ_pX_CA_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_ZZ_pX_CR_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_ZZ_pX_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/padic_ZZ_pX_FM_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/pow_computer.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/pow_computer_ext.pyx\"\n        sage -t  \"devel/sage/sage/rings/padics/tests.py\"\n        sage -t  \"devel/sage/sage/rings/padics/tutorial.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/groebner_fan.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial.pyx\"\n        sage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/multi_polynomial_libsingular.pyx\"\n        sage -t  \"devel/sage/sage/rings/polynomial/padics/polynomial_padic_capped_relative_dense.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/padics/polynomial_padic_flat.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/polynomial_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/polynomial/polynomial_element_generic.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/polynomial_integer_dense_flint.pyx\"\n        sage -t  \"devel/sage/sage/rings/polynomial/polynomial_integer_dense_ntl.pyx\"\n        sage -t  \"devel/sage/sage/rings/polynomial/polynomial_quotient_ring.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/polynomial_quotient_ring_element.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/polynomial_ring.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/polynomial_singular_interface.py\"\n        sage -t  \"devel/sage/sage/rings/polynomial/real_roots.pyx\"\n        sage -t  \"devel/sage/sage/rings/power_series_ring_element.pyx\"\n        sage -t  \"devel/sage/sage/rings/residue_field.pyx\"\n        sage -t  \"devel/sage/sage/rings/ring.pyx\"\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py\"\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_generic.py\"\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_number_field.py\"\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_padic_field.py\"\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_point.py\"\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py\"\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_torsion.py\"\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/padic_lseries.py\"\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/padics.py\"\n        sage -t  \"devel/sage/sage/schemes/elliptic_curves/sha_tate.py\"\n        sage -t  \"devel/sage/sage/schemes/generic/scheme.py\"\n        sage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/constructor.py\"\n        sage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/hypellfrob.pyx\"\n        sage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py\"\n        sage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_generic.py\"\n        sage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py\"\n        sage -t  \"devel/sage/sage/schemes/hyperelliptic_curves/jacobian_morphism.py\"\n        sage -t  \"devel/sage/sage/structure/element.pyx\"\n        sage -t  \"devel/sage/sage/structure/parent.pyx\"\n        sage -t  \"devel/sage/sage/structure/parent_gens.pyx\"\n        sage -t  \"devel/sage/sage/structure/sage_object.pyx\"\n        sage -t  \"devel/sage/sage/tests/benchmark.py\"\n        sage -t  \"devel/sage/sage/tests/book_stein_modform.py\"\n```\n\n\nMost of them\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.",
    "created_at": "2009-01-16T10:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38035",
    "user": "@robertwb"
}
```


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

archive/issue_comments_038036.json:
```json
{
    "body": "Down to \n\n\n```\n        sage -t  \"devel/sage/sage/finance/fractal.pyx\"\n        sage -t  \"devel/sage/sage/finance/time_series.pyx\"\n        sage -t  \"devel/sage/sage/interfaces/sage0.py\"\n        sage -t  \"devel/sage/sage/misc/randstate.pyx\"\n        sage -t  \"devel/sage/sage/rings/complex_double.pyx\"\n        sage -t  \"devel/sage/sage/rings/number_field/totallyreal_data.pyx\"\n\n```\n",
    "created_at": "2009-01-19T22:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38036",
    "user": "@robertwb"
}
```

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

archive/issue_comments_038037.json:
```json
{
    "body": "All of these are some kind of numerical error, but it looks more severe than your typical \"numerical noise\" so we'll need to look deeper.",
    "created_at": "2009-01-19T23:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38037",
    "user": "@robertwb"
}
```

All of these are some kind of numerical error, but it looks more severe than your typical "numerical noise" so we'll need to look deeper.



---

archive/issue_comments_038038.json:
```json
{
    "body": "I believe I've located the issue: \n\nhttp://trac.cython.org/cython_trac/ticket/190\n\nRecompiling right now.",
    "created_at": "2009-01-20T02:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38038",
    "user": "@robertwb"
}
```

I believe I've located the issue: 

http://trac.cython.org/cython_trac/ticket/190

Recompiling right now.



---

archive/issue_comments_038039.json:
```json
{
    "body": "Yep, that fixes the files above.",
    "created_at": "2009-01-20T02:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38039",
    "user": "@robertwb"
}
```

Yep, that fixes the files above.



---

archive/issue_comments_038040.json:
```json
{
    "body": "Note the spkg is out of date, pull from cython-devel.",
    "created_at": "2009-02-20T10:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38040",
    "user": "@robertwb"
}
```

Note the spkg is out of date, pull from cython-devel.



---

archive/issue_comments_038041.json:
```json
{
    "body": "spkg in http://sage.math.washington.edu/home/robertwb/cython/ is up to date.",
    "created_at": "2009-02-20T11:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38041",
    "user": "@robertwb"
}
```

spkg in http://sage.math.washington.edu/home/robertwb/cython/ is up to date.



---

archive/issue_comments_038042.json:
```json
{
    "body": "A lot of refnanny errors in the coercion code: \n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/rings/padics/padic_printing.cpp: __init__()\nReferences leaked: \n  Acquired on lines: 4278, 4287, 4345, 4354, 4412, 4421\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent.c: convert_map_from()\nNULL argument on line 10437\nToo many decrefs on line 10458, reference acquired on lines []\nsage/structure/parent_old.c: has_coerce_map_from_c()\nNULL argument on line 6200\nToo many decrefs on line 6221, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_c()\nNULL argument on line 5157\nToo many decrefs on line 5178, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_c()\nNULL argument on line 5157\nToo many decrefs on line 5178, reference acquired on lines []\nsage/structure/parent_old.c: has_coerce_map_from_c()\nNULL argument on line 6200\nToo many decrefs on line 6221, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4766, reference acquired on lines []\nsage/structure/parent_old.c: coerce_map_from_c()\nNULL argument on line 1361\nToo many decrefs on line 1382, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4766, reference acquired on lines []\nsage/structure/parent_old.c: coerce_map_from_c()\nNULL argument on line 1361\nToo many decrefs on line 1382, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8053, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent_old.c: has_coerce_map_from_c()\nNULL argument on line 6200\nToo many decrefs on line 6221, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent_old.c: coerce_map_from_c()\nNULL argument on line 1361\nToo many decrefs on line 1382, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8053, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/element.c: _sub_()\nNULL argument on line 7564\nToo many decrefs on line 7577, reference acquired on lines []\nsage/rings/polynomial/polynomial_element.c: _sub_()\nNULL argument on line 42791\nToo many decrefs on line 42813, reference acquired on lines []\nsage/structure/factory.c: get_version()\nNULL argument on line 1596\nToo many decrefs on line 1617, reference acquired on lines []\nsage/structure/factory.c: other_keys()\nNULL argument on line 1924\nToo many decrefs on line 1948, reference acquired on lines []\nsage/structure/factory.c: get_object()\nNULL argument on line 819\nToo many decrefs on line 846, reference acquired on lines []\nsage/structure/factory.c: get_version()\nNULL argument on line 1596\nToo many decrefs on line 1617, reference acquired on lines []\nsage/structure/factory.c: get_object()\nNULL argument on line 819\nToo many decrefs on line 846, reference acquired on lines []\nsage/structure/factory.c: get_version()\nNULL argument on line 1596\nToo many decrefs on line 1617, reference acquired on lines []\nsage/structure/factory.c: other_keys()\nNULL argument on line 1924\nToo many decrefs on line 1940, reference acquired on lines []\nsage/structure/factory.c: get_object()\nNULL argument on line 819\nToo many decrefs on line 846, reference acquired on lines []\nReferences leaked: \n  Acquired on lines: 1048, 1114\n  Acquired on lines: 1049, 1115\n  Acquired on lines: 1050, 1116\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent_old.c: _an_element_()\nNULL argument on line 8393\nToo many decrefs on line 8400, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_c()\nNULL argument on line 5157\nToo many decrefs on line 5178, reference acquired on lines []\nsage/structure/parent_old.c: has_coerce_map_from_c()\nNULL argument on line 6200\nToo many decrefs on line 6221, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4766, reference acquired on lines []\nsage/structure/parent_old.c: coerce_map_from_c()\nNULL argument on line 1361\nToo many decrefs on line 1382, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8053, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent.c: _convert_map_from_()\nNULL argument on line 11296\nToo many decrefs on line 11317, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent_old.c: _generic_convert_map()\nNULL argument on line 8540\nToo many decrefs on line 8561, reference acquired on lines []\nsage/structure/parent.c: convert_map_from()\nNULL argument on line 10437\nToo many decrefs on line 10458, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4766, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent.c: convert_map_from()\nNULL argument on line 10437\nToo many decrefs on line 10458, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent.c: has_coerce_map_from()\nNULL argument on line 8562\nToo many decrefs on line 8585, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent.c: convert_map_from()\nNULL argument on line 10437\nToo many decrefs on line 10458, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent.c: convert_map_from()\nNULL argument on line 10437\nToo many decrefs on line 10458, reference acquired on lines []\nsage/structure/parent_old.c: _an_element_c()\nNULL argument on line 7421\nToo many decrefs on line 7434, reference acquired on lines []\nsage/structure/parent_old.c: _an_element_()\nNULL argument on line 8393\nToo many decrefs on line 8406, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/rings/polynomial/polynomial_element.c: _mul_()\nNULL argument on line 10869\nToo many decrefs on line 10882, reference acquired on lines []\nsage/rings/polynomial/polynomial_element.c: _lmul_()\nNULL argument on line 5211\nToo many decrefs on line 5233, reference acquired on lines []\nsage/structure/parent_old.c: get_action_c()\nNULL argument on line 2800\nToo many decrefs on line 2831, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/rings/polynomial/polynomial_element.c: _mul_()\nNULL argument on line 10869\nToo many decrefs on line 10882, reference acquired on lines []\nsage/rings/polynomial/polynomial_element.c: _lmul_()\nNULL argument on line 5211\nToo many decrefs on line 5233, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/rings/polynomial/polynomial_element.c: _mul_()\nNULL argument on line 10869\nToo many decrefs on line 10882, reference acquired on lines []\nsage/rings/polynomial/polynomial_element.c: _lmul_()\nNULL argument on line 5211\nToo many decrefs on line 5233, reference acquired on lines []\nsage/structure/parent_old.c: get_action_c()\nNULL argument on line 2800\nToo many decrefs on line 2831, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: get_action_c()\nNULL argument on line 2800\nToo many decrefs on line 2831, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/element.c: _add_()\nNULL argument on line 7103\nToo many decrefs on line 7116, reference acquired on lines []\nsage/rings/polynomial/polynomial_element.c: _add_()\nNULL argument on line 42088\nToo many decrefs on line 42110, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent.c: has_coerce_map_from()\nNULL argument on line 8562\nToo many decrefs on line 8585, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent_old.c: _an_element_()\nNULL argument on line 8393\nToo many decrefs on line 8406, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent_old.c: _an_element_c()\nNULL argument on line 7421\nToo many decrefs on line 7434, reference acquired on lines []\nsage/structure/parent_old.c: _an_element_()\nNULL argument on line 8393\nToo many decrefs on line 8406, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/structure/parent_old.c: get_action_c()\nNULL argument on line 2800\nToo many decrefs on line 2831, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8045, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent.c: an_element()\nNULL argument on line 13813\nToo many decrefs on line 13826, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_c()\nNULL argument on line 5157\nToo many decrefs on line 5178, reference acquired on lines []\nsage/structure/parent_old.c: has_coerce_map_from_c()\nNULL argument on line 6200\nToo many decrefs on line 6221, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4775, reference acquired on lines []\nsage/rings/ring.c: is_exact()\nNULL argument on line 4760\nToo many decrefs on line 4766, reference acquired on lines []\nsage/structure/parent_old.c: coerce_map_from_c()\nNULL argument on line 1361\nToo many decrefs on line 1382, reference acquired on lines []\nsage/structure/parent_old.c: _coerce_map_from_()\nNULL argument on line 8032\nToo many decrefs on line 8053, reference acquired on lines []\nsage/structure/parent.c: coerce_map_from()\nNULL argument on line 8916\nToo many decrefs on line 8937, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\nsage/structure/parent_old.c: get_action_c()\nNULL argument on line 2800\nToo many decrefs on line 2831, reference acquired on lines []\nsage/structure/parent_old.c: _get_action_()\nNULL argument on line 8182\nToo many decrefs on line 8213, reference acquired on lines []\nsage/structure/parent.c: get_action()\nNULL argument on line 11428\nToo many decrefs on line 11459, reference acquired on lines []\n```\n",
    "created_at": "2009-02-20T12:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38042",
    "user": "@robertwb"
}
```

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

archive/issue_comments_038043.json:
```json
{
    "body": "BTW\n\n\n```\nrobert$ cat | sort | uniq | wc\n      85     522    3808\n```\n\n\nSo there are about 30 distinct places it complains about.",
    "created_at": "2009-02-20T12:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38043",
    "user": "@robertwb"
}
```

BTW


```
robert$ cat | sort | uniq | wc
      85     522    3808
```


So there are about 30 distinct places it complains about.



---

archive/issue_comments_038044.json:
```json
{
    "body": "Fixed cpdef refnanny bug, now \n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage/rings/padics/padic_printing.cpp: __init__()\nReferences leaked: \n  Acquired on lines: 4278, 4287, 4345, 4354, 4412, 4421\nsage/structure/factory.c: get_object()\nReferences leaked: \n  Acquired on lines: 1048, 1114\n  Acquired on lines: 1049, 1115\n  Acquired on lines: 1050, 1116\nsage: \nExiting SAGE (CPU time 0m0.07s, Wall time 2m13.31s).\nException exceptions.AssertionError in  ignored\nException exceptions.AssertionError in  ignored\nException exceptions.AssertionError in /Users/robert/sage/sage-cython/local/bin/sage-sage: line 587: 16443 Bus error               sage-ipython \"$@\" -i\n```\n",
    "created_at": "2009-02-20T23:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38044",
    "user": "@robertwb"
}
```

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
Exception exceptions.AssertionError in /Users/robert/sage/sage-cython/local/bin/sage-sage: line 587: 16443 Bus error               sage-ipython "$@" -i
```




---

archive/issue_comments_038045.json:
```json
{
    "body": "New spkg posted, Sage starts up fine, but still segfaults on exit.",
    "created_at": "2009-02-21T06:58:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38045",
    "user": "@robertwb"
}
```

New spkg posted, Sage starts up fine, but still segfaults on exit.



---

archive/issue_comments_038046.json:
```json
{
    "body": "Replying to [comment:11 robertwb]:\n> New spkg posted, Sage starts up fine, but still segfaults on exit. \n\nWith this spkg building the Sage library og 3.3.alpha3 breaks on sage.math due to\n\n```\n/*\n   I get really sick of typing unsigned long.\n*/\ntypedef unsigned long  ulong;\n\n```\n\nin \n\n```\nbuilding 'sage.rings.polynomial.polynomial_zmod_flint' extension\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC \n-DCYTHON_REFNANNY=1 -I/scratch/mabshoff/sage-3.3.alpha3-vg/local/include/FLINT/ \n-I/scratch/mabshoff/sage-3.3.alpha3-vg/local//include -I/scratch/mabshoff/sage-\n3.3.alpha3-vg/local//include/csage -I/scratch/mabshoff/sage-3.3.alpha3-vg/devel//sage\n/sage/ext -I/scratch/mabshoff/sage-3.3.alpha3-vg/local/include/python2.5 -c sage/rings\n/polynomial/polynomial_zmod_flint.c -o build/temp.linux-x86_64-2.5/sage/rings\n/polynomial/polynomial_zmod_flint.o -std=c99 -D_XPG6 -w\nIn file included from sage/rings/polynomial/polynomial_zmod_flint.c:140:\n/scratch/mabshoff/sage-3.3.alpha3-vg/local//include/zn_poly/zn_poly.h:72: error: duplicate \u2018unsigned\u2019\nerror: command 'gcc' failed with exit status 1\n```\n",
    "created_at": "2009-02-21T08:41:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38046",
    "user": "mabshoff"
}
```

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

archive/issue_comments_038047.json:
```json
{
    "body": "Attachment [4987-cython-0.11.patch](tarball://root/attachments/some-uuid/ticket4987/4987-cython-0.11.patch) by @robertwb created at 2009-02-26 05:48:54",
    "created_at": "2009-02-26T05:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38047",
    "user": "@robertwb"
}
```

Attachment [4987-cython-0.11.patch](tarball://root/attachments/some-uuid/ticket4987/4987-cython-0.11.patch) by @robertwb created at 2009-02-26 05:48:54



---

archive/issue_comments_038048.json:
```json
{
    "body": "Sage 3.3 compiles, starts, and exits without errors or segfauting with the attached patch, and the latest spkg.",
    "created_at": "2009-02-26T05:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38048",
    "user": "@robertwb"
}
```

Sage 3.3 compiles, starts, and exits without errors or segfauting with the attached patch, and the latest spkg.



---

archive/issue_comments_038049.json:
```json
{
    "body": "Replying to [comment:13 robertwb]:\n> Sage 3.3 compiles, starts, and exits without errors or segfauting with the attached patch, and the latest spkg. \n\nAwesome. Is that also with the refnanny enabled?\n\nI also saw something being fixed today in regard to another reference leak, so I am interesting in trying this.\n\nHow close is this to being ready? I don't want this in 3.4 for obvious reasons, but 3.4.1 seems like a strong possibility.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-26T06:03:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38049",
    "user": "mabshoff"
}
```

Replying to [comment:13 robertwb]:
> Sage 3.3 compiles, starts, and exits without errors or segfauting with the attached patch, and the latest spkg. 

Awesome. Is that also with the refnanny enabled?

I also saw something being fixed today in regard to another reference leak, so I am interesting in trying this.

How close is this to being ready? I don't want this in 3.4 for obvious reasons, but 3.4.1 seems like a strong possibility.

Cheers,

Michael



---

archive/issue_comments_038050.json:
```json
{
    "body": "Yes, with the refnanny. 3.4.1 seems a likely target--I haven't run a testall yet, but the last testall has surprisingly few unique errors.",
    "created_at": "2009-02-26T07:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38050",
    "user": "@robertwb"
}
```

Yes, with the refnanny. 3.4.1 seems a likely target--I haven't run a testall yet, but the last testall has surprisingly few unique errors.



---

archive/issue_comments_038051.json:
```json
{
    "body": "testall log at http://sage.math.washington.edu/home/robertwb/sage-3.3/devel/sage-main/log.txt\n\nIs there a way to only log failed tests?",
    "created_at": "2009-02-26T09:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38051",
    "user": "@robertwb"
}
```

testall log at http://sage.math.washington.edu/home/robertwb/sage-3.3/devel/sage-main/log.txt

Is there a way to only log failed tests?



---

archive/issue_comments_038052.json:
```json
{
    "body": "The only remaining errors are \n\n\n```\n\t./sage -t  \"devel/sage/sage/coding/decoder.py\"\n\t./sage -t  \"devel/sage/sage/rings/bernmm.pyx\"\n\t./sage -t  \"devel/sage/sage/rings/qqbar.py\"\n\t./sage -t  \"devel/sage/sage/combinat/root_system/weyl_characters.py\"\n\t./sage -t  \"devel/sage/sage/modular/abvar/abvar.py\"\n\t./sage -t  \"devel/sage/sage/modular/abvar/homspace.py\"\n```\n\n\nWhich all timeout.",
    "created_at": "2009-02-26T22:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38052",
    "user": "@robertwb"
}
```

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

archive/issue_comments_038053.json:
```json
{
    "body": "All tests pass, and we're getting close to a release. \n\nNote that the current patch enables the refnanny, which should be changed before release.",
    "created_at": "2009-03-08T07:20:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38053",
    "user": "@robertwb"
}
```

All tests pass, and we're getting close to a release. 

Note that the current patch enables the refnanny, which should be changed before release.



---

archive/issue_comments_038054.json:
```json
{
    "body": "Attachment [4987-cython-0.11-final.patch](tarball://root/attachments/some-uuid/ticket4987/4987-cython-0.11-final.patch) by @robertwb created at 2009-03-14 08:00:08\n\nApply this one. (Exactly the same as above, but doesn't enable the refnanny.)",
    "created_at": "2009-03-14T08:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38054",
    "user": "@robertwb"
}
```

Attachment [4987-cython-0.11-final.patch](tarball://root/attachments/some-uuid/ticket4987/4987-cython-0.11-final.patch) by @robertwb created at 2009-03-14 08:00:08

Apply this one. (Exactly the same as above, but doesn't enable the refnanny.)



---

archive/issue_comments_038055.json:
```json
{
    "body": "Sage compiles, passes all doctests, and Cython 0.11 is out. Time to ship.",
    "created_at": "2009-03-14T08:00:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38055",
    "user": "@robertwb"
}
```

Sage compiles, passes all doctests, and Cython 0.11 is out. Time to ship.



---

archive/issue_comments_038056.json:
```json
{
    "body": "Starting from Sage 3.4, I applied the patch, installed the Cython spkg, did \"sage -ba\", and did a full test run -- all tests passed.  Also, I read the patch, and it looked entirely reasonable.\n\nSo, positive review on the patch.  I did take a quick look at the spkg, but I didn't look closely enough to feel comfortable giving it a review; I did notice a couple of problems, though:\n\n1) SPKG.txt has a mixture of line endings: some lines end with CR, some with LF\n\n2) \"cython -V\" doesn't believe it's 0.11 final:\n\n```\nsage$ cython -V\nCython version 0.11.rc3\n```\n",
    "created_at": "2009-03-19T02:14:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38056",
    "user": "cwitty"
}
```

Starting from Sage 3.4, I applied the patch, installed the Cython spkg, did "sage -ba", and did a full test run -- all tests passed.  Also, I read the patch, and it looked entirely reasonable.

So, positive review on the patch.  I did take a quick look at the spkg, but I didn't look closely enough to feel comfortable giving it a review; I did notice a couple of problems, though:

1) SPKG.txt has a mixture of line endings: some lines end with CR, some with LF

2) "cython -V" doesn't believe it's 0.11 final:

```
sage$ cython -V
Cython version 0.11.rc3
```




---

archive/issue_comments_038057.json:
```json
{
    "body": "I posted a new spkg, fixing the newlines of SPKG.txt, and adding the final commit for 0.11 final (which only changed the version number). \n\nGiven that everything builds and passes tests, I don't know how much more reviewing of the spkg itself is necessary--certainly no one is expecting reviewers to referee the entire upstream changes. It'd be nice if we can get this into 3.4.1.",
    "created_at": "2009-03-19T06:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38057",
    "user": "@robertwb"
}
```

I posted a new spkg, fixing the newlines of SPKG.txt, and adding the final commit for 0.11 final (which only changed the version number). 

Given that everything builds and passes tests, I don't know how much more reviewing of the spkg itself is necessary--certainly no one is expecting reviewers to referee the entire upstream changes. It'd be nice if we can get this into 3.4.1.



---

archive/issue_comments_038058.json:
```json
{
    "body": "I am signing off on the spkg because I am sure that upstream has improved Cython. I did a complete build cycle of the Sage library and doctests pass after applying the patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T10:18:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38058",
    "user": "mabshoff"
}
```

I am signing off on the spkg because I am sure that upstream has improved Cython. I did a complete build cycle of the Sage library and doctests pass after applying the patch.

Cheers,

Michael



---

archive/issue_comments_038059.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T10:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38059",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_038060.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T10:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38060",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038061.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-04-10T09:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38061",
    "user": "@robertwb"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_038062.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-04-10T09:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38062",
    "user": "@robertwb"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_038063.json:
```json
{
    "body": "Speed profiling should be done as well!\n\n0.10.3\n\n```\nsage: sage: time set_random_seed(11); M = random_matrix(QQ, 100, 100); M.echelonize()\nCPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s\nWall time: 0.03 s\n```\n\n\n0.11\n\n```\nsage: time set_random_seed(11); M = random_matrix(QQ, 100, 100); M.echelonize()\nCPU times: user 0.46 s, sys: 0.00 s, total: 0.46 s\nWall time: 0.46 s\n```\n\n\nThis is a blocker for 0.11.1",
    "created_at": "2009-04-10T09:23:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38063",
    "user": "@robertwb"
}
```

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

archive/issue_comments_038064.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-10T10:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38064",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038065.json:
```json
{
    "body": "Hi Robert,\n\nis is customary to open another ticket for an issue found in a closed ticket, so I am closing this again. Please open another ticket. I am surprised that there is a such a speed regression since no one has observed it.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T10:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38065",
    "user": "mabshoff"
}
```

Hi Robert,

is is customary to open another ticket for an issue found in a closed ticket, so I am closing this again. Please open another ticket. I am surprised that there is a such a speed regression since no one has observed it.

Cheers,

Michael



---

archive/issue_comments_038066.json:
```json
{
    "body": "The spkg itself was fine, so I am changing the title back.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T10:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38066",
    "user": "mabshoff"
}
```

The spkg itself was fine, so I am changing the title back.

Cheers,

Michael



---

archive/issue_comments_038067.json:
```json
{
    "body": "The point was to revert the spkg and not ship 0.11 in Sage 3.4.1, as I didn't think a fix would be out in time. However, I'm not seeing the speed regression in your rc, so I'm mystified but we can go ahead and leave this closed. \n\nBTW, the timings above were done with the 3.4 release, the only difference was moving Cython from 0.10.3 to 0.11.",
    "created_at": "2009-04-10T18:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38067",
    "user": "@robertwb"
}
```

The point was to revert the spkg and not ship 0.11 in Sage 3.4.1, as I didn't think a fix would be out in time. However, I'm not seeing the speed regression in your rc, so I'm mystified but we can go ahead and leave this closed. 

BTW, the timings above were done with the 3.4 release, the only difference was moving Cython from 0.10.3 to 0.11.



---

archive/issue_comments_038068.json:
```json
{
    "body": "Sorry for the noise--the refnanny was enabled on my 0.11 builds. Whew, I was really worried there for a bit.",
    "created_at": "2009-04-10T19:08:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4987",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4987#issuecomment-38068",
    "user": "@robertwb"
}
```

Sorry for the noise--the refnanny was enabled on my 0.11 builds. Whew, I was really worried there for a bit.
