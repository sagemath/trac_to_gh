# Issue 3899: massive unpickle problems

Issue created by migration from https://trac.sagemath.org/ticket/3899

Original creator: was

Original creation time: 2008-08-19 17:44:49

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



---

Comment by rlm created at 2008-08-20 20:46:31

Any of the sage objects at http://www.rlmiller.org/de_codes/ also fail to unpickle. I have already unpickled and repickled this data painfully several times to keep up.....


---

Comment by rlm created at 2008-08-20 20:57:12

Oops, different problem. Please ignore my last comment... :-)


---

Comment by jdemeyer created at 2017-03-08 13:18:03

Resolution: invalid


---

Comment by jdemeyer created at 2017-03-08 13:18:03

Closing as obsolete...
