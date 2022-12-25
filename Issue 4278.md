# Issue 4278: [with patch, needs review] Old parent's don't correctly handle coerce maps from Python's native types.

archive/issues_004278.json:
```json
{
    "body": "Assignee: @robertwb\n\nCC:  @mwhansen\n\nBefore\n\n\n```\nsage: QQ['q,t'].coerce_map_from(int)\nsage:\n```\n\n\nAfter\n\n\n```\nComposite map:\n  From: Set of Python objects of type 'int'\n  To:   Multivariate Polynomial Ring in q, t over Rational Field\n  Defn:   Native morphism:\n          From: Set of Python objects of type 'int'\n          To:   Integer Ring\n        then\n          Call morphism:\n          From: Integer Ring\n          To:   Multivariate Polynomial Ring in q, t over Rational Field\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4278\n\n",
    "created_at": "2008-10-13T21:24:42Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] Old parent's don't correctly handle coerce maps from Python's native types.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4278",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @robertwb

CC:  @mwhansen

Before


```
sage: QQ['q,t'].coerce_map_from(int)
sage:
```


After


```
Composite map:
  From: Set of Python objects of type 'int'
  To:   Multivariate Polynomial Ring in q, t over Rational Field
  Defn:   Native morphism:
          From: Set of Python objects of type 'int'
          To:   Integer Ring
        then
          Call morphism:
          From: Integer Ring
          To:   Multivariate Polynomial Ring in q, t over Rational Field
```


Issue created by migration from https://trac.sagemath.org/ticket/4278





---

archive/issue_comments_031220.json:
```json
{
    "body": "Attachment [trac_4278.patch](tarball://root/attachments/some-uuid/ticket4278/trac_4278.patch) by @robertwb created at 2008-10-14 10:59:59\n\nLooks good to me.",
    "created_at": "2008-10-14T10:59:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31220",
    "user": "https://github.com/robertwb"
}
```

Attachment [trac_4278.patch](tarball://root/attachments/some-uuid/ticket4278/trac_4278.patch) by @robertwb created at 2008-10-14 10:59:59

Looks good to me.



---

archive/issue_comments_031221.json:
```json
{
    "body": "Somehow this one snuck into a closed milestone due to (a) robertwb having admin power in trac and (b) caching via the browser. It will be merged in 3.2 shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-14T20:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31221",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Somehow this one snuck into a closed milestone due to (a) robertwb having admin power in trac and (b) caching via the browser. It will be merged in 3.2 shortly.

Cheers,

Michael



---

archive/issue_comments_031222.json:
```json
{
    "body": "And probably (c) trying to use trac at le Maison de Chercheurs and leaving several windows open \"to do when I get decent internet.\"\n\nThanks for catching this.",
    "created_at": "2008-10-14T20:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31222",
    "user": "https://github.com/robertwb"
}
```

And probably (c) trying to use trac at le Maison de Chercheurs and leaving several windows open "to do when I get decent internet."

Thanks for catching this.



---

archive/issue_comments_031223.json:
```json
{
    "body": "I am seeing failures of the following kind:\n\n```\nsage -t  devel/sage/sage/structure/factorization.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.alpha0/tmp/factorization.py\", line 114:\n    sage: F = ModularSymbols(11,4).factorization()\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[35]>\", line 1, in <module>\n        F = ModularSymbols(Integer(11),Integer(4)).factorization()###line 114:\n    sage: F = ModularSymbols(11,4).factorization()\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py\", line 1120, in factorization\n        cond = 1 if chi is None   else   chi.conductor()\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/modular/dirichlet.py\", line 476, in conductor\n        if self.modulus() == 1 or self.is_trivial():\n      File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/modular/dirichlet.py\", line 899, in is_trivial\n        z = self.element() == 0\n      File \"free_module_element.pyx\", line 737, in sage.modules.free_module_element.FreeModuleElement.__richcmp__ (sage/modules/free_module_element.c:5884)\n      File \"element.pyx\", line 498, in sage.structure.element.Element._richcmp (sage/structure/element.c:4392)\n        _left, _right = coercion_model.canonical_coercion(left, right)\n      File \"coerce.pyx\", line 737, in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:5743)\n        coercions = self.coercion_maps(xp, yp)\n      File \"coerce.pyx\", line 876, in sage.structure.coerce.CoercionModel_cache_maps.coercion_maps (sage/structure/coerce.c:6842)\n        homs = self.discover_coercion(R, S)\n      File \"coerce.pyx\", line 1011, in sage.structure.coerce.CoercionModel_cache_maps.discover_coercion (sage/structure/coerce.c:8090)\n        mor = (<Parent>R).coerce_map_from(S)\n      File \"parent.pyx\", line 923, in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:7576)\n        mor = self.discover_coerce_map_from(S)\n      File \"parent.pyx\", line 967, in sage.structure.parent.Parent.discover_coerce_map_from (sage/structure/parent.c:7860)\n        cdef map.Map mor = self._coerce_map_from_(S)\n      File \"parent_old.pyx\", line 584, in sage.structure.parent_old.Parent._coerce_map_from_ (sage/structure/parent_old.c:5989)\n        return self.coerce_map_from_c(S)\n      File \"parent_old.pyx\", line 147, in sage.structure.parent_old.Parent.coerce_map_from_c (sage/structure/parent_old.c:1653)\n        mor = mor*sage_type_mor\n      File \"map.pyx\", line 162, in sage.categories.map.Map.__mul__ (sage/categories/map.c:3177)\n    AttributeError: 'NoneType' object has no attribute 'domain'\n**********************************************************************\n```\n\n\nA more complete list once doctesting finishes.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T09:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31223",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I am seeing failures of the following kind:

```
sage -t  devel/sage/sage/structure/factorization.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.alpha0/tmp/factorization.py", line 114:
    sage: F = ModularSymbols(11,4).factorization()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[35]>", line 1, in <module>
        F = ModularSymbols(Integer(11),Integer(4)).factorization()###line 114:
    sage: F = ModularSymbols(11,4).factorization()
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/modular/modsym/ambient.py", line 1120, in factorization
        cond = 1 if chi is None   else   chi.conductor()
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/modular/dirichlet.py", line 476, in conductor
        if self.modulus() == 1 or self.is_trivial():
      File "/scratch/mabshoff/release-cycle/sage-3.2.alpha0/local/lib/python2.5/site-packages/sage/modular/dirichlet.py", line 899, in is_trivial
        z = self.element() == 0
      File "free_module_element.pyx", line 737, in sage.modules.free_module_element.FreeModuleElement.__richcmp__ (sage/modules/free_module_element.c:5884)
      File "element.pyx", line 498, in sage.structure.element.Element._richcmp (sage/structure/element.c:4392)
        _left, _right = coercion_model.canonical_coercion(left, right)
      File "coerce.pyx", line 737, in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:5743)
        coercions = self.coercion_maps(xp, yp)
      File "coerce.pyx", line 876, in sage.structure.coerce.CoercionModel_cache_maps.coercion_maps (sage/structure/coerce.c:6842)
        homs = self.discover_coercion(R, S)
      File "coerce.pyx", line 1011, in sage.structure.coerce.CoercionModel_cache_maps.discover_coercion (sage/structure/coerce.c:8090)
        mor = (<Parent>R).coerce_map_from(S)
      File "parent.pyx", line 923, in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:7576)
        mor = self.discover_coerce_map_from(S)
      File "parent.pyx", line 967, in sage.structure.parent.Parent.discover_coerce_map_from (sage/structure/parent.c:7860)
        cdef map.Map mor = self._coerce_map_from_(S)
      File "parent_old.pyx", line 584, in sage.structure.parent_old.Parent._coerce_map_from_ (sage/structure/parent_old.c:5989)
        return self.coerce_map_from_c(S)
      File "parent_old.pyx", line 147, in sage.structure.parent_old.Parent.coerce_map_from_c (sage/structure/parent_old.c:1653)
        mor = mor*sage_type_mor
      File "map.pyx", line 162, in sage.categories.map.Map.__mul__ (sage/categories/map.c:3177)
    AttributeError: 'NoneType' object has no attribute 'domain'
**********************************************************************
```


A more complete list once doctesting finishes.

Cheers,

Michael



---

archive/issue_comments_031224.json:
```json
{
    "body": "oops:\n\n```\n\tsage -t  devel/sage/sage/tests/benchmark.py # 1 doctests failed\n\tsage -t  devel/sage/sage/structure/factorization.py # 5 doctests failed\n\tsage -t  devel/sage/sage/schemes/generic/homset.py # 1 doctests failed\n\tsage -t  devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py # 1 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/gp_simon.py # 1 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 26 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/ell_padic_field.py # 1 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py # 2 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/ell_torsion.py # 11 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 2 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/padics.py # 9 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 7 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 3 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 5 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/ell_number_field.py # 16 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py # 3 doctests failed\n\tsage -t  devel/sage/sage/rings/polynomial/polydict.pyx # 1 doctests failed\n\tsage -t  devel/sage/sage/rings/polynomial/pbori.pyx # 2 doctests failed\n\tsage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 17 doctests failed\n\tsage -t  devel/sage/sage/rings/padics/padic_base_generic.py # 1 doctests failed\n\tsage -t  devel/sage/sage/rings/number_field/number_field_ideal.py # 6 doctests failed\n\tsage -t  devel/sage/sage/rings/number_field/order.py # 31 doctests failed\n\tsage -t  devel/sage/sage/rings/number_field/number_field_element.pyx # 8 doctests failed\n\tsage -t  devel/sage/sage/rings/real_rqdf.pyx # 1 doctests failed\n\tsage -t  devel/sage/sage/rings/ring.pyx # 1 doctests failed\n\tsage -t  devel/sage/sage/rings/residue_field.pyx # 15 doctests failed\n\tsage -t  devel/sage/sage/rings/integer_mod_ring.py # 1 doctests failed\n\tsage -t  devel/sage/sage/rings/number_field/number_field.py # 12 doctests failed\n\tsage -t  devel/sage/sage/rings/integer_ring.pyx # 2 doctests failed\n\tsage -t  devel/sage/sage/plot/plot3d/shapes2.py # 1 doctests failed\n\tsage -t  devel/sage/sage/plot/plot3d/shapes.pyx # 2 doctests failed\n\tsage -t  devel/sage/sage/plot/plot3d/platonic.py # 1 doctests failed\n\tsage -t  devel/sage/sage/plot/plot3d/parametric_plot3d.py # 1 doctests failed\n\tsage -t  devel/sage/sage/plot/plot3d/plot3d.py # 2 doctests failed\n\tsage -t  devel/sage/sage/numerical/optimize.py # 2 doctests failed\n\tsage -t  devel/sage/sage/modules/misc.py # 6 doctests failed\n\tsage -t  devel/sage/sage/modules/free_quadratic_module.py # 5 doctests failed\n\tsage -t  devel/sage/sage/modular/modsym/tests.py # 9 doctests failed\n\tsage -t  devel/sage/sage/modules/free_module.py # 15 doctests failed\n\tsage -t  devel/sage/sage/modules/free_module_element.pyx # 2 doctests failed\n\tsage -t  devel/sage/sage/plot/tachyon.py # 1 doctests failed\n\tsage -t  devel/sage/sage/modular/modsym/heilbronn.pyx # 15 doctests failed\n\tsage -t  devel/sage/sage/modular/modsym/subspace.py # 26 doctests failed\n\tsage -t  devel/sage/sage/modular/modsym/hecke_operator.py # 1 doctests failed\n\tsage -t  devel/sage/sage/modular/modsym/modsym.py # 11 doctests failed\n\tsage -t  devel/sage/sage/modular/modsym/space.py # 106 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/tests.py # 2 doctests failed\n\tsage -t  devel/sage/sage/modular/modsym/boundary.py # 28 doctests failed\n\tsage -t  devel/sage/sage/modular/modsym/ambient.py # 30 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/submodule.py # 1 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/half_integral.py # 6 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/space.py # 26 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/hecke_operator_on_qexp.py # 2 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/eis_series.py # 6 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/cuspidal_submodule.py # 23 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/ambient_g1.py # 1 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/constructor.py # 12 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/eisenstein_submodule.py # 20 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/ambient_eps.py # 27 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/ambient_R.py # 2 doctests failed\n\tsage -t  devel/sage/sage/modular/hecke/submodule.py # 15 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/ambient.py # 15 doctests failed\n\tsage -t  devel/sage/sage/modular/modform/element.py # 28 doctests failed\n\tsage -t  devel/sage/sage/modular/hecke/hecke_operator.py # 3 doctests failed\n\tsage -t  devel/sage/sage/modular/hecke/degenmap.py # 3 doctests failed\n\tsage -t  devel/sage/sage/modular/hecke/ambient_module.py # 20 doctests failed\n\tsage -t  devel/sage/sage/modular/hecke/module.py # 46 doctests failed\n\tsage -t  devel/sage/sage/modular/abvar/lseries.py # 16 doctests failed\n\tsage -t  devel/sage/sage/modular/abvar/torsion_subgroup.py # 27 doctests failed\n\tsage -t  devel/sage/sage/modular/abvar/cuspidal_subgroup.py # 30 doctests failed\n\tsage -t  devel/sage/sage/modular/abvar/homology.py # 26 doctests failed\n\tsage -t  devel/sage/sage/modular/abvar/constructor.py # 4 doctests failed\n\tsage -t  devel/sage/sage/modular/abvar/abvar_newform.py # 31 doctests failed\n\tsage -t  devel/sage/sage/modular/abvar/homspace.py # 65 doctests failed\n\tsage -t  devel/sage/sage/modular/abvar/abvar_ambient_jacobian.py # 13 doctests failed\n\tsage -t  devel/sage/sage/modular/abvar/finite_subgroup.py # 93 doctests failed\n\tsage -t  devel/sage/sage/modular/cusps.py # 1 doctests failed\n\tsage -t  devel/sage/sage/modular/dirichlet.py # 13 doctests failed\n\tsage -t  devel/sage/sage/modular/dims.py # 17 doctests failed\n\tsage -t  devel/sage/sage/modular/abvar/morphism.py # 70 doctests failed\n\tsage -t  devel/sage/sage/modular/buzzard.py # 4 doctests failed\n\tsage -t  devel/sage/sage/misc/misc.py # 1 doctests failed\n\tsage -t  devel/sage/sage/modular/abvar/abvar.py # 120 doctests failed\n\tsage -t  devel/sage/sage/matrix/tests.py # 1 doctests failed\n\tsage -t  devel/sage/sage/matrix/matrix_window_modn_dense.pyx # 1 doctests failed\n\tsage -t  devel/sage/sage/matrix/matrix_space.py # 1 doctests failed\n\tsage -t  devel/sage/sage/matrix/matrix_integer_dense_saturation.py # 10 doctests failed\n\tsage -t  devel/sage/sage/matrix/matrix_integer_dense_hnf.py # 6 doctests failed\n\tsage -t  devel/sage/sage/matrix/matrix0.pyx # 2 doctests failed\n\tsage -t  devel/sage/sage/matrix/matrix_integer_dense.pyx # 21 doctests failed\n\tsage -t  devel/sage/sage/matrix/action.pyx # 1 doctests failed\n\tsage -t  devel/sage/sage/matrix/matrix_cyclo_dense.pyx # 2 doctests failed\n\tsage -t  devel/sage/sage/matrix/matrix2.pyx # 12 doctests failed\n\tsage -t  devel/sage/sage/interfaces/sage0.py # 2 doctests failed\n\tsage -t  devel/sage/sage/libs/fplll/fplll.pyx # 6 doctests failed\n\tsage -t  devel/sage/sage/plot/plot.py # 1 doctests failed\n\tsage -t  devel/sage/sage/groups/matrix_gps/matrix_group_element.py # 2 doctests failed\n\tsage -t  devel/sage/sage/groups/abelian_gps/abelian_group.py # 5 doctests failed\n\tsage -t  devel/sage/sage/groups/group.pyx # 1 doctests failed\n\tsage -t  devel/sage/sage/graphs/bipartite_graph.py # 2 doctests failed\n\tsage -t  devel/sage/sage/groups/matrix_gps/matrix_group.py # 1 doctests failed\n\tsage -t  devel/sage/sage/geometry/lattice_polytope.py # 8 doctests failed\n\tsage -t  devel/sage/sage/graphs/graph.py # 1 doctests failed\n\tsage -t  devel/sage/sage/crypto/mq/mpolynomialsystem.py # 39 doctests failed\n\tsage -t  devel/sage/sage/crypto/mq/sr.py # 3 doctests failed\n\tsage -t  devel/sage/sage/combinat/root_system/weight_lattice_realization.py # 3 doctests failed\n\tsage -t  devel/sage/sage/combinat/root_system/weyl_group.py # 5 doctests failed\n\tsage -t  devel/sage/sage/combinat/root_system/type_G.py # 1 doctests failed\n\tsage -t  devel/sage/sage/combinat/root_system/type_F.py # 1 doctests failed\n\tsage -t  devel/sage/sage/combinat/root_system/type_E.py # 5 doctests failed\n\tsage -t  devel/sage/sage/combinat/root_system/root_system.py # 8 doctests failed\n\tsage -t  devel/sage/sage/combinat/root_system/root_lattice_realization.py # 1 doctests failed\n\tsage -t  devel/sage/sage/combinat/crystals/spins.py # 2 doctests failed\n\tsage -t  devel/sage/sage/combinat/crystals/letters.py # 5 doctests failed\n\tsage -t  devel/sage/sage/combinat/crystals/tensor_product.py # 9 doctests failed\n\tsage -t  devel/sage/sage/combinat/crystals/fast_crystals.py # 14 doctests failed\n\tsage -t  devel/sage/sage/combinat/crystals/crystals.py # 15 doctests failed\n\tsage -t  devel/sage/sage/coding/sd_codes.py # 2 doctests failed\n\tsage -t  devel/sage/sage/coding/code_constructions.py # 7 doctests failed\n\tsage -t  devel/sage/sage/coding/linear_code.py # 3 doctests failed\n\tsage -t  devel/sage/sage/combinat/root_system/weyl_characters.py # 30 doctests failed\n\tsage -t  devel/sage/sage/calculus/calculus.py # 1 doctests failed\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-10-18T09:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31224",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

oops:

```
	sage -t  devel/sage/sage/tests/benchmark.py # 1 doctests failed
	sage -t  devel/sage/sage/structure/factorization.py # 5 doctests failed
	sage -t  devel/sage/sage/schemes/generic/homset.py # 1 doctests failed
	sage -t  devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_padic_field.py # 1 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/gp_simon.py # 1 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 26 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/ell_padic_field.py # 1 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/ell_tate_curve.py # 2 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/ell_torsion.py # 11 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 2 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/padics.py # 9 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/ell_point.py # 7 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 3 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/ell_generic.py # 5 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/ell_number_field.py # 16 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/ell_finite_field.py # 3 doctests failed
	sage -t  devel/sage/sage/rings/polynomial/polydict.pyx # 1 doctests failed
	sage -t  devel/sage/sage/rings/polynomial/pbori.pyx # 2 doctests failed
	sage -t  devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 17 doctests failed
	sage -t  devel/sage/sage/rings/padics/padic_base_generic.py # 1 doctests failed
	sage -t  devel/sage/sage/rings/number_field/number_field_ideal.py # 6 doctests failed
	sage -t  devel/sage/sage/rings/number_field/order.py # 31 doctests failed
	sage -t  devel/sage/sage/rings/number_field/number_field_element.pyx # 8 doctests failed
	sage -t  devel/sage/sage/rings/real_rqdf.pyx # 1 doctests failed
	sage -t  devel/sage/sage/rings/ring.pyx # 1 doctests failed
	sage -t  devel/sage/sage/rings/residue_field.pyx # 15 doctests failed
	sage -t  devel/sage/sage/rings/integer_mod_ring.py # 1 doctests failed
	sage -t  devel/sage/sage/rings/number_field/number_field.py # 12 doctests failed
	sage -t  devel/sage/sage/rings/integer_ring.pyx # 2 doctests failed
	sage -t  devel/sage/sage/plot/plot3d/shapes2.py # 1 doctests failed
	sage -t  devel/sage/sage/plot/plot3d/shapes.pyx # 2 doctests failed
	sage -t  devel/sage/sage/plot/plot3d/platonic.py # 1 doctests failed
	sage -t  devel/sage/sage/plot/plot3d/parametric_plot3d.py # 1 doctests failed
	sage -t  devel/sage/sage/plot/plot3d/plot3d.py # 2 doctests failed
	sage -t  devel/sage/sage/numerical/optimize.py # 2 doctests failed
	sage -t  devel/sage/sage/modules/misc.py # 6 doctests failed
	sage -t  devel/sage/sage/modules/free_quadratic_module.py # 5 doctests failed
	sage -t  devel/sage/sage/modular/modsym/tests.py # 9 doctests failed
	sage -t  devel/sage/sage/modules/free_module.py # 15 doctests failed
	sage -t  devel/sage/sage/modules/free_module_element.pyx # 2 doctests failed
	sage -t  devel/sage/sage/plot/tachyon.py # 1 doctests failed
	sage -t  devel/sage/sage/modular/modsym/heilbronn.pyx # 15 doctests failed
	sage -t  devel/sage/sage/modular/modsym/subspace.py # 26 doctests failed
	sage -t  devel/sage/sage/modular/modsym/hecke_operator.py # 1 doctests failed
	sage -t  devel/sage/sage/modular/modsym/modsym.py # 11 doctests failed
	sage -t  devel/sage/sage/modular/modsym/space.py # 106 doctests failed
	sage -t  devel/sage/sage/modular/modform/tests.py # 2 doctests failed
	sage -t  devel/sage/sage/modular/modsym/boundary.py # 28 doctests failed
	sage -t  devel/sage/sage/modular/modsym/ambient.py # 30 doctests failed
	sage -t  devel/sage/sage/modular/modform/submodule.py # 1 doctests failed
	sage -t  devel/sage/sage/modular/modform/half_integral.py # 6 doctests failed
	sage -t  devel/sage/sage/modular/modform/space.py # 26 doctests failed
	sage -t  devel/sage/sage/modular/modform/hecke_operator_on_qexp.py # 2 doctests failed
	sage -t  devel/sage/sage/modular/modform/eis_series.py # 6 doctests failed
	sage -t  devel/sage/sage/modular/modform/cuspidal_submodule.py # 23 doctests failed
	sage -t  devel/sage/sage/modular/modform/ambient_g1.py # 1 doctests failed
	sage -t  devel/sage/sage/modular/modform/constructor.py # 12 doctests failed
	sage -t  devel/sage/sage/modular/modform/eisenstein_submodule.py # 20 doctests failed
	sage -t  devel/sage/sage/modular/modform/ambient_eps.py # 27 doctests failed
	sage -t  devel/sage/sage/modular/modform/ambient_R.py # 2 doctests failed
	sage -t  devel/sage/sage/modular/hecke/submodule.py # 15 doctests failed
	sage -t  devel/sage/sage/modular/modform/ambient.py # 15 doctests failed
	sage -t  devel/sage/sage/modular/modform/element.py # 28 doctests failed
	sage -t  devel/sage/sage/modular/hecke/hecke_operator.py # 3 doctests failed
	sage -t  devel/sage/sage/modular/hecke/degenmap.py # 3 doctests failed
	sage -t  devel/sage/sage/modular/hecke/ambient_module.py # 20 doctests failed
	sage -t  devel/sage/sage/modular/hecke/module.py # 46 doctests failed
	sage -t  devel/sage/sage/modular/abvar/lseries.py # 16 doctests failed
	sage -t  devel/sage/sage/modular/abvar/torsion_subgroup.py # 27 doctests failed
	sage -t  devel/sage/sage/modular/abvar/cuspidal_subgroup.py # 30 doctests failed
	sage -t  devel/sage/sage/modular/abvar/homology.py # 26 doctests failed
	sage -t  devel/sage/sage/modular/abvar/constructor.py # 4 doctests failed
	sage -t  devel/sage/sage/modular/abvar/abvar_newform.py # 31 doctests failed
	sage -t  devel/sage/sage/modular/abvar/homspace.py # 65 doctests failed
	sage -t  devel/sage/sage/modular/abvar/abvar_ambient_jacobian.py # 13 doctests failed
	sage -t  devel/sage/sage/modular/abvar/finite_subgroup.py # 93 doctests failed
	sage -t  devel/sage/sage/modular/cusps.py # 1 doctests failed
	sage -t  devel/sage/sage/modular/dirichlet.py # 13 doctests failed
	sage -t  devel/sage/sage/modular/dims.py # 17 doctests failed
	sage -t  devel/sage/sage/modular/abvar/morphism.py # 70 doctests failed
	sage -t  devel/sage/sage/modular/buzzard.py # 4 doctests failed
	sage -t  devel/sage/sage/misc/misc.py # 1 doctests failed
	sage -t  devel/sage/sage/modular/abvar/abvar.py # 120 doctests failed
	sage -t  devel/sage/sage/matrix/tests.py # 1 doctests failed
	sage -t  devel/sage/sage/matrix/matrix_window_modn_dense.pyx # 1 doctests failed
	sage -t  devel/sage/sage/matrix/matrix_space.py # 1 doctests failed
	sage -t  devel/sage/sage/matrix/matrix_integer_dense_saturation.py # 10 doctests failed
	sage -t  devel/sage/sage/matrix/matrix_integer_dense_hnf.py # 6 doctests failed
	sage -t  devel/sage/sage/matrix/matrix0.pyx # 2 doctests failed
	sage -t  devel/sage/sage/matrix/matrix_integer_dense.pyx # 21 doctests failed
	sage -t  devel/sage/sage/matrix/action.pyx # 1 doctests failed
	sage -t  devel/sage/sage/matrix/matrix_cyclo_dense.pyx # 2 doctests failed
	sage -t  devel/sage/sage/matrix/matrix2.pyx # 12 doctests failed
	sage -t  devel/sage/sage/interfaces/sage0.py # 2 doctests failed
	sage -t  devel/sage/sage/libs/fplll/fplll.pyx # 6 doctests failed
	sage -t  devel/sage/sage/plot/plot.py # 1 doctests failed
	sage -t  devel/sage/sage/groups/matrix_gps/matrix_group_element.py # 2 doctests failed
	sage -t  devel/sage/sage/groups/abelian_gps/abelian_group.py # 5 doctests failed
	sage -t  devel/sage/sage/groups/group.pyx # 1 doctests failed
	sage -t  devel/sage/sage/graphs/bipartite_graph.py # 2 doctests failed
	sage -t  devel/sage/sage/groups/matrix_gps/matrix_group.py # 1 doctests failed
	sage -t  devel/sage/sage/geometry/lattice_polytope.py # 8 doctests failed
	sage -t  devel/sage/sage/graphs/graph.py # 1 doctests failed
	sage -t  devel/sage/sage/crypto/mq/mpolynomialsystem.py # 39 doctests failed
	sage -t  devel/sage/sage/crypto/mq/sr.py # 3 doctests failed
	sage -t  devel/sage/sage/combinat/root_system/weight_lattice_realization.py # 3 doctests failed
	sage -t  devel/sage/sage/combinat/root_system/weyl_group.py # 5 doctests failed
	sage -t  devel/sage/sage/combinat/root_system/type_G.py # 1 doctests failed
	sage -t  devel/sage/sage/combinat/root_system/type_F.py # 1 doctests failed
	sage -t  devel/sage/sage/combinat/root_system/type_E.py # 5 doctests failed
	sage -t  devel/sage/sage/combinat/root_system/root_system.py # 8 doctests failed
	sage -t  devel/sage/sage/combinat/root_system/root_lattice_realization.py # 1 doctests failed
	sage -t  devel/sage/sage/combinat/crystals/spins.py # 2 doctests failed
	sage -t  devel/sage/sage/combinat/crystals/letters.py # 5 doctests failed
	sage -t  devel/sage/sage/combinat/crystals/tensor_product.py # 9 doctests failed
	sage -t  devel/sage/sage/combinat/crystals/fast_crystals.py # 14 doctests failed
	sage -t  devel/sage/sage/combinat/crystals/crystals.py # 15 doctests failed
	sage -t  devel/sage/sage/coding/sd_codes.py # 2 doctests failed
	sage -t  devel/sage/sage/coding/code_constructions.py # 7 doctests failed
	sage -t  devel/sage/sage/coding/linear_code.py # 3 doctests failed
	sage -t  devel/sage/sage/combinat/root_system/weyl_characters.py # 30 doctests failed
	sage -t  devel/sage/sage/calculus/calculus.py # 1 doctests failed
```


Cheers,

Michael



---

archive/issue_comments_031225.json:
```json
{
    "body": "attachment:trac_4278_2.patch should fix the problems with the first patch.",
    "created_at": "2008-10-23T17:42:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31225",
    "user": "https://github.com/burcin"
}
```

attachment:trac_4278_2.patch should fix the problems with the first patch.



---

archive/issue_comments_031226.json:
```json
{
    "body": "Attachment [trac_4278_2.patch](tarball://root/attachments/some-uuid/ticket4278/trac_4278_2.patch) by @mwhansen created at 2008-10-24 02:52:26\n\n+1 for Burcin's patch.",
    "created_at": "2008-10-24T02:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31226",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4278_2.patch](tarball://root/attachments/some-uuid/ticket4278/trac_4278_2.patch) by @mwhansen created at 2008-10-24 02:52:26

+1 for Burcin's patch.



---

archive/issue_comments_031227.json:
```json
{
    "body": "This patch causes a segfault in\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha1$ ./sage -t -long devel/sage/sage/modular/modsym/ambient.py\nsage -t -long devel/sage/sage/modular/modsym/ambient.py     \n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\t [3.9 s]\nexit code: 768\n```\n\nI am not sure if a `-ba` might not fix this, but I will investigate. Does this patch depend on anything else?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T00:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31227",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch causes a segfault in

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.2.alpha1$ ./sage -t -long devel/sage/sage/modular/modsym/ambient.py
sage -t -long devel/sage/sage/modular/modsym/ambient.py     

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------


A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
	 [3.9 s]
exit code: 768
```

I am not sure if a `-ba` might not fix this, but I will investigate. Does this patch depend on anything else?

Cheers,

Michael



---

archive/issue_comments_031228.json:
```json
{
    "body": "Mike: 1389-tut.patch touches tut.tex.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T12:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31228",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Mike: 1389-tut.patch touches tut.tex.

Cheers,

Michael



---

archive/issue_comments_031229.json:
```json
{
    "body": "oops, wrong ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-26T12:52:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31229",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

oops, wrong ticket.

Cheers,

Michael



---

archive/issue_comments_031230.json:
```json
{
    "body": "I am unable to reproduce this from the command line, but it does happen when testing :(.",
    "created_at": "2008-11-14T02:04:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31230",
    "user": "https://github.com/robertwb"
}
```

I am unable to reproduce this from the command line, but it does happen when testing :(.



---

archive/issue_comments_031231.json:
```json
{
    "body": "And here's the \"traceback\"\n\npython(4662) malloc: *** error for object 0x1: pointer being reallocated was not allocated\npython(4662) malloc: *** set a breakpoint in szone_error to debug\n\nProgram received signal EXC_BAD_ACCESS, Could not access memory.\nReason: KERN_PROTECTION_FAILURE at address: 0x00000000\n0x00732b71 in __gmpn_copyi ()\n(gdb) bt\n#0  0x00732b71 in __gmpn_copyi ()\n#1  0x00719cb0 in __gmpz_set ()\nPrevious frame inner to this frame (corrupt stack?)\n\nSo I'm really at a loss how to begin debugging this.",
    "created_at": "2008-11-14T02:12:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31231",
    "user": "https://github.com/robertwb"
}
```

And here's the "traceback"

python(4662) malloc: *** error for object 0x1: pointer being reallocated was not allocated
python(4662) malloc: *** set a breakpoint in szone_error to debug

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_PROTECTION_FAILURE at address: 0x00000000
0x00732b71 in __gmpn_copyi ()
(gdb) bt
#0  0x00732b71 in __gmpn_copyi ()
#1  0x00719cb0 in __gmpz_set ()
Previous frame inner to this frame (corrupt stack?)

So I'm really at a loss how to begin debugging this.



---

archive/issue_comments_031232.json:
```json
{
    "body": "Sorry, here's the traceback again \n\n\n```\npython(4662) malloc: *** error for object 0x1: pointer being reallocated was not allocated\npython(4662) malloc: *** set a breakpoint in szone_error to debug\n\nProgram received signal EXC_BAD_ACCESS, Could not access memory.\nReason: KERN_PROTECTION_FAILURE at address: 0x00000000\n0x00732b71 in __gmpn_copyi ()\n(gdb) bt\n#0  0x00732b71 in __gmpn_copyi ()\n#1  0x00719cb0 in __gmpz_set ()\nPrevious frame inner to this frame (corrupt stack?)\n```\n",
    "created_at": "2008-11-14T02:12:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31232",
    "user": "https://github.com/robertwb"
}
```

Sorry, here's the traceback again 


```
python(4662) malloc: *** error for object 0x1: pointer being reallocated was not allocated
python(4662) malloc: *** set a breakpoint in szone_error to debug

Program received signal EXC_BAD_ACCESS, Could not access memory.
Reason: KERN_PROTECTION_FAILURE at address: 0x00000000
0x00732b71 in __gmpn_copyi ()
(gdb) bt
#0  0x00732b71 in __gmpn_copyi ()
#1  0x00719cb0 in __gmpz_set ()
Previous frame inner to this frame (corrupt stack?)
```




---

archive/issue_comments_031233.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2008-11-14T07:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31233",
    "user": "https://github.com/robertwb"
}
```

apply only this patch



---

archive/issue_comments_031234.json:
```json
{
    "body": "Attachment [4278-final.patch](tarball://root/attachments/some-uuid/ticket4278/4278-final.patch) by @robertwb created at 2008-11-14 07:09:22\n\nThe segfault was due to #4520, and in the process I streamlined this patch.",
    "created_at": "2008-11-14T07:09:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31234",
    "user": "https://github.com/robertwb"
}
```

Attachment [4278-final.patch](tarball://root/attachments/some-uuid/ticket4278/4278-final.patch) by @robertwb created at 2008-11-14 07:09:22

The segfault was due to #4520, and in the process I streamlined this patch.



---

archive/issue_comments_031235.json:
```json
{
    "body": "Looks good to me. All tests pass.",
    "created_at": "2008-11-14T09:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31235",
    "user": "https://github.com/burcin"
}
```

Looks good to me. All tests pass.



---

archive/issue_comments_031236.json:
```json
{
    "body": "Merged 4278-final.patch in Sage 3.2.rc1",
    "created_at": "2008-11-14T18:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31236",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 4278-final.patch in Sage 3.2.rc1



---

archive/issue_comments_031237.json:
```json
{
    "body": "Merged 4278-final.patch in Sage 3.2.rc1",
    "created_at": "2008-11-14T18:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31237",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 4278-final.patch in Sage 3.2.rc1



---

archive/issue_comments_031238.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-14T18:20:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4278",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4278#issuecomment-31238",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
