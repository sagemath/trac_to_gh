# Issue 3899: massive unpickle problems

archive/issues_003899.json:
```json
{
    "body": "Assignee: cwitty\n\nI grabbed the 3.0.5 pickle jar from #3482, and tried it in 3.1.1.  The following all fail to unpickle.\n\n```\n** failed:  _class__sage_modular_modform_element_ModularFormElement__.sobj\n** failed:  _class__sage_modular_abvar_finite_subgroup_TorsionPoint__.sobj\n** failed:  _class__sage_combinat_crystals_tensor_product_TensorProductOfCrystals__.sobj\n** failed:  _class__sage_modular_modform_eisenstein_submodule_EisensteinSubmodule_g0_Q__.sobj\n** failed:  _class__sage_combinat_root_system_weyl_group_WeylGroupElement__.sobj\n** failed:  _class__sage_modular_modform_element_ModularFormElement_elliptic_curve__.sobj\n** failed:  _class__sage_modular_modform_ambient_g0_ModularFormsAmbient_g0_Q__.sobj\n** failed:  _class__sage_modular_abvar_abvar_ambient_jacobian_ModAbVar_ambient_jacobian_class__.sobj\n** failed:  _class__sage_modular_modform_ambient_g1_ModularFormsAmbient_g1_Q__.sobj\n** failed:  _class__sage_modular_modform_numerical_NumericalEigenforms__.sobj\n** failed:  _class__sage_modular_abvar_finite_subgroup_FiniteSubgroup_lattice__.sobj\n** failed:  _class__sage_modular_abvar_lseries_Lseries_complex__.sobj\n** failed:  _class__sage_combinat_root_system_weyl_group_WeylGroup_gens__.sobj\n** failed:  _class__sage_modular_abvar_homology_RationalHomology__.sobj\n** failed:  _class__sage_modular_abvar_lseries_Lseries_padic__.sobj\n** failed:  _class__sage_modular_abvar_torsion_subgroup_RationalTorsionSubgroup__.sobj\n** failed:  _class__sage_modular_modsym_ambient_ModularSymbolsAmbient_wtk_g0__.sobj\n** failed:  _class__sage_structure_sequence_Sequence__.sobj\n** failed:  _class__sage_modular_abvar_homology_IntegralHomology__.sobj\n** failed:  _class__sage_combinat_root_system_weyl_characters_WeylCharacter__.sobj\n** failed:  _class__sage_modular_modform_cuspidal_submodule_CuspidalSubmodule_g1_Q__.sobj\n** failed:  _class__sage_modular_abvar_homology_Homology_over_base__.sobj\n** failed:  _class__sage_combinat_root_system_weyl_characters_WeightRing__.sobj\n** failed:  _class__sage_modular_modsym_subspace_ModularSymbolsSubspace__.sobj\n** failed:  _class__sage_modular_modform_ambient_eps_ModularFormsAmbient_eps__.sobj\n** failed:  _class__sage_modular_modform_ambient_R_ModularFormsAmbient_R__.sobj\n** failed:  _class__sage_modular_abvar_abvar_newform_ModularAbelianVariety_newform__.sobj\n** failed:  _class__sage_combinat_root_system_weyl_characters_WeylCharacterRing_class__.sobj\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/3899\n\n",
    "closed_at": "2017-03-08T13:18:03Z",
    "created_at": "2008-08-19T17:44:49Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "massive unpickle problems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3899",
    "user": "https://github.com/williamstein"
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

archive/issue_comments_027837.json:
```json
{
    "body": "Any of the sage objects at http://www.rlmiller.org/de_codes/ also fail to unpickle. I have already unpickled and repickled this data painfully several times to keep up.....",
    "created_at": "2008-08-20T20:46:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3899#issuecomment-27837",
    "user": "https://github.com/rlmill"
}
```

Any of the sage objects at http://www.rlmiller.org/de_codes/ also fail to unpickle. I have already unpickled and repickled this data painfully several times to keep up.....



---

archive/issue_comments_027838.json:
```json
{
    "body": "Oops, different problem. Please ignore my last comment... :-)",
    "created_at": "2008-08-20T20:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3899#issuecomment-27838",
    "user": "https://github.com/rlmill"
}
```

Oops, different problem. Please ignore my last comment... :-)



---

archive/issue_events_008937.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3899#event-8937"
}
```



---

archive/issue_events_008938.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3899#event-8938"
}
```



---

archive/issue_events_008939.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3899#event-8939"
}
```



---

archive/issue_events_008940.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3899#event-8940"
}
```



---

archive/issue_events_008941.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3899#event-8941"
}
```



---

archive/issue_events_008942.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3899#event-8942"
}
```



---

archive/issue_events_008943.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3899#event-8943"
}
```



---

archive/issue_comments_027839.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2017-03-08T13:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3899#issuecomment-27839",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid



---

archive/issue_comments_027840.json:
```json
{
    "body": "Closing as obsolete...",
    "created_at": "2017-03-08T13:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3899#issuecomment-27840",
    "user": "https://github.com/jdemeyer"
}
```

Closing as obsolete...



---

archive/issue_events_008944.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-03-08T13:18:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3899#event-8944"
}
```



---

archive/issue_events_008945.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-03-08T13:18:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3899#event-8945"
}
```



---

archive/issue_events_008946.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2017-03-08T13:18:03Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3899#event-8946"
}
```
