# Issue 3899: massive unpickle problems

archive/issues_003899.json:
```json
{
    "body": "Assignee: cwitty\n\nI grabbed the 3.0.5 pickle jar from #3482, and tried it in 3.1.1.  The following all fail to unpickle.\n\n\n```\n** failed:  _class__sage_modular_modform_element_ModularFormElement__.sobj\n** failed:  _class__sage_modular_abvar_finite_subgroup_TorsionPoint__.sobj\n** failed:  _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj\n** failed:  _class__sage_modular_modform_eisenstein_submodule_EisensteinSubmodule_g0_Q__.sobj\n** failed:  _class__sage_combinat_root_system_weyl_group_WeylGroupElement__.sobj\n** failed:  _class__sage_modular_modform_element_ModularFormElement_elliptic_curve__.sobj\n** failed:  _class__sage_modular_modform_ambient_g0_ModularFormsAmbient_g0_Q__.sobj\n** failed:  _class__sage_modular_abvar_abvar_ambient_jacobian_ModAbVar_ambient_jacobian_class__.sobj\n** failed:  _class__sage_modular_modform_ambient_g1_ModularFormsAmbient_g1_Q__.sobj\n** failed:  _class__sage_modular_modform_numerical_NumericalEigenforms__.sobj\n** failed:  _class__sage_modular_abvar_finite_subgroup_FiniteSubgroup_lattice__.sobj\n** failed:  _class__sage_modular_abvar_lseries_Lseries_complex__.sobj\n** failed:  _class__sage_combinat_root_system_weyl_group_WeylGroup_gens__.sobj\n** failed:  _class__sage_modular_abvar_homology_RationalHomology__.sobj\n** failed:  _class__sage_modular_abvar_lseries_Lseries_padic__.sobj\n** failed:  _class__sage_modular_abvar_torsion_subgroup_RationalTorsionSubgroup__.sobj\n** failed:  _class__sage_modular_modsym_ambient_ModularSymbolsAmbient_wtk_g0__.sobj\n** failed:  _class__sage_structure_sequence_Sequence__.sobj\n** failed:  _class__sage_modular_abvar_homology_IntegralHomology__.sobj\n** failed:  _class__sage_combinat_root_system_weyl_characters_WeylCharacter__.sobj\n** failed:  _class__sage_modular_modform_cuspidal_submodule_CuspidalSubmodule_g1_Q__.sobj\n** failed:  _class__sage_modular_abvar_homology_Homology_over_base__.sobj\n** failed:  _class__sage_combinat_root_system_weyl_characters_WeightRing__.sobj\n** failed:  _class__sage_modular_modsym_subspace_ModularSymbolsSubspace__.sobj\n** failed:  _class__sage_modular_modform_ambient_eps_ModularFormsAmbient_eps__.sobj\n** failed:  _class__sage_modular_modform_ambient_R_ModularFormsAmbient_R__.sobj\n** failed:  _class__sage_modular_abvar_abvar_newform_ModularAbelianVariety_newform__.sobj\n** failed:  _class__sage_combinat_root_system_weyl_characters_WeylCharacterRing_class__.sobj\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3899\n\n",
    "created_at": "2008-08-19T17:44:49Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "massive unpickle problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3899",
    "user": "@williamstein"
}
```
Assignee: cwitty

I grabbed the 3.0.5 pickle jar from #3482, and tried it in 3.1.1.  The following all fail to unpickle.


```
** failed:  _class__sage_modular_modform_element_ModularFormElement__.sobj
** failed:  _class__sage_modular_abvar_finite_subgroup_TorsionPoint__.sobj
** failed:  _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj
** failed:  _class__sage_modular_modform_eisenstein_submodule_EisensteinSubmodule_g0_Q__.sobj
** failed:  _class__sage_combinat_root_system_weyl_group_WeylGroupElement__.sobj
** failed:  _class__sage_modular_modform_element_ModularFormElement_elliptic_curve__.sobj
** failed:  _class__sage_modular_modform_ambient_g0_ModularFormsAmbient_g0_Q__.sobj
** failed:  _class__sage_modular_abvar_abvar_ambient_jacobian_ModAbVar_ambient_jacobian_class__.sobj
** failed:  _class__sage_modular_modform_ambient_g1_ModularFormsAmbient_g1_Q__.sobj
** failed:  _class__sage_modular_modform_numerical_NumericalEigenforms__.sobj
** failed:  _class__sage_modular_abvar_finite_subgroup_FiniteSubgroup_lattice__.sobj
** failed:  _class__sage_modular_abvar_lseries_Lseries_complex__.sobj
** failed:  _class__sage_combinat_root_system_weyl_group_WeylGroup_gens__.sobj
** failed:  _class__sage_modular_abvar_homology_RationalHomology__.sobj
** failed:  _class__sage_modular_abvar_lseries_Lseries_padic__.sobj
** failed:  _class__sage_modular_abvar_torsion_subgroup_RationalTorsionSubgroup__.sobj
** failed:  _class__sage_modular_modsym_ambient_ModularSymbolsAmbient_wtk_g0__.sobj
** failed:  _class__sage_structure_sequence_Sequence__.sobj
** failed:  _class__sage_modular_abvar_homology_IntegralHomology__.sobj
** failed:  _class__sage_combinat_root_system_weyl_characters_WeylCharacter__.sobj
** failed:  _class__sage_modular_modform_cuspidal_submodule_CuspidalSubmodule_g1_Q__.sobj
** failed:  _class__sage_modular_abvar_homology_Homology_over_base__.sobj
** failed:  _class__sage_combinat_root_system_weyl_characters_WeightRing__.sobj
** failed:  _class__sage_modular_modsym_subspace_ModularSymbolsSubspace__.sobj
** failed:  _class__sage_modular_modform_ambient_eps_ModularFormsAmbient_eps__.sobj
** failed:  _class__sage_modular_modform_ambient_R_ModularFormsAmbient_R__.sobj
** failed:  _class__sage_modular_abvar_abvar_newform_ModularAbelianVariety_newform__.sobj
** failed:  _class__sage_combinat_root_system_weyl_characters_WeylCharacterRing_class__.sobj
```


Issue created by migration from https://trac.sagemath.org/ticket/3899





---

archive/issue_comments_027895.json:
```json
{
    "body": "Any of the sage objects at http://www.rlmiller.org/de_codes/ also fail to unpickle. I have already unpickled and repickled this data painfully several times to keep up.....",
    "created_at": "2008-08-20T20:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3899#issuecomment-27895",
    "user": "@rlmill"
}
```

Any of the sage objects at http://www.rlmiller.org/de_codes/ also fail to unpickle. I have already unpickled and repickled this data painfully several times to keep up.....



---

archive/issue_comments_027896.json:
```json
{
    "body": "Oops, different problem. Please ignore my last comment... :-)",
    "created_at": "2008-08-20T20:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3899#issuecomment-27896",
    "user": "@rlmill"
}
```

Oops, different problem. Please ignore my last comment... :-)



---

archive/issue_comments_027897.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2017-03-08T13:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3899#issuecomment-27897",
    "user": "@jdemeyer"
}
```

Resolution: invalid



---

archive/issue_comments_027898.json:
```json
{
    "body": "Closing as obsolete...",
    "created_at": "2017-03-08T13:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3899#issuecomment-27898",
    "user": "@jdemeyer"
}
```

Closing as obsolete...
