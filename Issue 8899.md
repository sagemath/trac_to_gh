# Issue 8899: Implement non commutative symmetric functions

archive/issues_008899.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat chrisjamesberg @zabrocki @anneschilling\n\nPatch under dev. on the sage-combinat patch server\n\nIssue created by migration from https://trac.sagemath.org/ticket/8899\n\n",
    "created_at": "2010-05-05T23:39:46Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.4",
    "title": "Implement non commutative symmetric functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8899",
    "user": "https://github.com/nthiery"
}
```
Assignee: sage-combinat

CC:  sage-combinat chrisjamesberg @zabrocki @anneschilling

Patch under dev. on the sage-combinat patch server

Issue created by migration from https://trac.sagemath.org/ticket/8899





---

archive/issue_comments_081718.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-05T23:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81718",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_081719.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-05-05T23:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81719",
    "user": "https://github.com/nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_081720.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-07-15T14:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81720",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081721.json:
```json
{
    "body": "Apply: trac_11929_8899-ncsf-qsym-folded-fs.patch, trac_11929_8899-additional_documentation-fs.patch \n\n(for the patchbot)",
    "created_at": "2012-07-15T14:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81721",
    "user": "https://github.com/saliola"
}
```

Apply: trac_11929_8899-ncsf-qsym-folded-fs.patch, trac_11929_8899-additional_documentation-fs.patch 

(for the patchbot)



---

archive/issue_comments_081722.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40\".",
    "created_at": "2012-07-15T14:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81722",
    "user": "https://github.com/saliola"
}
```

Changing keywords from "" to "sd40".



---

archive/issue_comments_081723.json:
```json
{
    "body": "A note on the patch coproduct_with_realizations-fs.patch: an earlier version of this patch was folded into the patch at #5457. So this patch is not needed if that ticket gets merged before this ticket. (I've included it here so that the patchbot can run all doctests.)\n\nIf this ticket gets merged before #5457, then an easy rebase of #5457 will be required.",
    "created_at": "2012-07-15T14:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81723",
    "user": "https://github.com/saliola"
}
```

A note on the patch coproduct_with_realizations-fs.patch: an earlier version of this patch was folded into the patch at #5457. So this patch is not needed if that ticket gets merged before this ticket. (I've included it here so that the patchbot can run all doctests.)

If this ticket gets merged before #5457, then an easy rebase of #5457 will be required.



---

archive/issue_comments_081724.json:
```json
{
    "body": "I put the author names in alphabetical order. I don't know the policy on this. I hope this is okay.",
    "created_at": "2012-07-15T14:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81724",
    "user": "https://github.com/saliola"
}
```

I put the author names in alphabetical order. I don't know the policy on this. I hope this is okay.



---

archive/issue_comments_081725.json:
```json
{
    "body": "(I think I learned something new about the patchbot: it ignores the order of the patches specified in the Apply directive and applies the patches in the order in which they get attached/updated.)",
    "created_at": "2012-07-15T15:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81725",
    "user": "https://github.com/saliola"
}
```

(I think I learned something new about the patchbot: it ignores the order of the patches specified in the Apply directive and applies the patches in the order in which they get attached/updated.)



---

archive/issue_comments_081726.json:
```json
{
    "body": "I think you guys need to add an entry in\n\ndoc/en/reference/combinat\n\nso that NSym and QSym are included in the documentation!\n\nAlso, I spotted an OUTPUT without the : behind it. Aren't we supposed to use\n\nINPUT:\n\n- ``x`` -- explanation\n\ni.e. a double dash after the variable to be explained?\n\nAnne",
    "created_at": "2012-07-19T23:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81726",
    "user": "https://github.com/anneschilling"
}
```

I think you guys need to add an entry in

doc/en/reference/combinat

so that NSym and QSym are included in the documentation!

Also, I spotted an OUTPUT without the : behind it. Aren't we supposed to use

INPUT:

- ``x`` -- explanation

i.e. a double dash after the variable to be explained?

Anne



---

archive/issue_comments_081727.json:
```json
{
    "body": "Thanks for catching these, Anne. We'll have to correct them.",
    "created_at": "2012-07-20T00:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81727",
    "user": "https://github.com/saliola"
}
```

Thanks for catching these, Anne. We'll have to correct them.



---

archive/issue_comments_081728.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-07-20T00:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81728",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081729.json:
```json
{
    "body": "Attachment [trac_11929_8899-ncsf-qsym-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-ncsf-qsym-fs.patch) by @saliola created at 2012-07-28 12:18:01",
    "created_at": "2012-07-28T12:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81729",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-ncsf-qsym-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-ncsf-qsym-fs.patch) by @saliola created at 2012-07-28 12:18:01



---

archive/issue_comments_081730.json:
```json
{
    "body": "I rebased [attachment:trac_11929_8899-ncsf-qsym-fs.patch] on #12959.\n\nChris, can you fix the documentation as explained by Anne:\n\n1. Add an entry in\n \n        `doc/en/reference/combinat`\n \n so that NSym and QSym are included in the documentation!\n \n2. Also, I spotted an OUTPUT without the : behind it.\n\n3. Proper syntax for INPUT blocks:\n \n        {{{\n        INPUT:\n \n        - ``x`` -- explanation\n        }}}\n \ni.e. a double dash after the variable to be explained [and a space after the initial dash]",
    "created_at": "2012-07-28T12:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81730",
    "user": "https://github.com/saliola"
}
```

I rebased [attachment:trac_11929_8899-ncsf-qsym-fs.patch] on #12959.

Chris, can you fix the documentation as explained by Anne:

1. Add an entry in
 
        `doc/en/reference/combinat`
 
 so that NSym and QSym are included in the documentation!
 
2. Also, I spotted an OUTPUT without the : behind it.

3. Proper syntax for INPUT blocks:
 
        {{{
        INPUT:
 
        - ``x`` -- explanation
        }}}
 
i.e. a double dash after the variable to be explained [and a space after the initial dash]



---

archive/issue_comments_081731.json:
```json
{
    "body": "Attachment [trac_11929_8899-fix_skewby-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-fix_skewby-fs.patch) by @saliola created at 2012-08-13 20:46:41\n\nTwo new small patches.\n\n1. `trac_11929_8899-fix_skewby-fs.patch:` Fixes things so that the following raises an error:\n\n```\nF([2,1]).skew_by([1])\n```\n\n\n2. `trac_11929_8899-add_degree_to_elementmethods-fs.patch:` addes `ElementMethods.degree` and `ElementMethods.is_homogeneous` to `GradedAlgebrasWithBasis` (I extracted these from a separate patch on the sage-combinat queue).\n\n**Outstanding question about the degree of an element:** what do we want as the default behaviour? Should it:\na. raise an error if the element is not homogeneous; or\nb. return the maximum of the degrees of the homogeneous summands?",
    "created_at": "2012-08-13T20:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81731",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-fix_skewby-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-fix_skewby-fs.patch) by @saliola created at 2012-08-13 20:46:41

Two new small patches.

1. `trac_11929_8899-fix_skewby-fs.patch:` Fixes things so that the following raises an error:

```
F([2,1]).skew_by([1])
```


2. `trac_11929_8899-add_degree_to_elementmethods-fs.patch:` addes `ElementMethods.degree` and `ElementMethods.is_homogeneous` to `GradedAlgebrasWithBasis` (I extracted these from a separate patch on the sage-combinat queue).

**Outstanding question about the degree of an element:** what do we want as the default behaviour? Should it:
a. raise an error if the element is not homogeneous; or
b. return the maximum of the degrees of the homogeneous summands?



---

archive/issue_comments_081732.json:
```json
{
    "body": "Attachment [trac_11929_8899-add_degree_to_elementmethods-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-add_degree_to_elementmethods-fs.patch) by @saliola created at 2012-08-14 14:18:26",
    "created_at": "2012-08-14T14:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81732",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-add_degree_to_elementmethods-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-add_degree_to_elementmethods-fs.patch) by @saliola created at 2012-08-14 14:18:26



---

archive/issue_comments_081733.json:
```json
{
    "body": "Replying to [comment:13 saliola]:\n> Two new small patches.\n> \n> 1. `trac_11929_8899-fix_skewby-fs.patch:` Fixes things so that the following raises an error:\n> {{{\n> F([2,1]).skew_by([1])\n> }}}\n> \n> 2. `trac_11929_8899-add_degree_to_elementmethods-fs.patch:` addes `ElementMethods.degree` and `ElementMethods.is_homogeneous` to `GradedAlgebrasWithBasis` (I extracted these from a separate patch on the sage-combinat queue).\n> \n> **Outstanding question about the degree of an element:** what do we want as the default behaviour? Should it:\n> a. raise an error if the element is not homogeneous; or\n> b. return the maximum of the degrees of the homogeneous summands?\n\nBased on the [discussion on sage-combinat-devel](https://groups.google.com/d/topic/sage-combinat-devel/pTjdBFeePWg/discussion), I updated [attachment:trac_11929_8899-add_degree_to_elementmethods-fs.patch]:\n- add methods `maximal_degree` and `homogeneous_degree` in `GradedAlgebrasWithBasis`\n- as a default in `GradedAlgebrasWithBasis`, set `degree = homogeneous_degree`\n- for NCSF/QSym, `degree` is redefined to be `maximal_degree`",
    "created_at": "2012-08-14T15:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81733",
    "user": "https://github.com/saliola"
}
```

Replying to [comment:13 saliola]:
> Two new small patches.
> 
> 1. `trac_11929_8899-fix_skewby-fs.patch:` Fixes things so that the following raises an error:
> {{{
> F([2,1]).skew_by([1])
> }}}
> 
> 2. `trac_11929_8899-add_degree_to_elementmethods-fs.patch:` addes `ElementMethods.degree` and `ElementMethods.is_homogeneous` to `GradedAlgebrasWithBasis` (I extracted these from a separate patch on the sage-combinat queue).
> 
> **Outstanding question about the degree of an element:** what do we want as the default behaviour? Should it:
> a. raise an error if the element is not homogeneous; or
> b. return the maximum of the degrees of the homogeneous summands?

Based on the [discussion on sage-combinat-devel](https://groups.google.com/d/topic/sage-combinat-devel/pTjdBFeePWg/discussion), I updated [attachment:trac_11929_8899-add_degree_to_elementmethods-fs.patch]:
- add methods `maximal_degree` and `homogeneous_degree` in `GradedAlgebrasWithBasis`
- as a default in `GradedAlgebrasWithBasis`, set `degree = homogeneous_degree`
- for NCSF/QSym, `degree` is redefined to be `maximal_degree`



---

archive/issue_comments_081734.json:
```json
{
    "body": "[attachment:trac_11929_8899-include_doc_in_reference_manual-fs.patch] deals with documentation:\n\n- added entries in reference manual\n- fixed markup to adhere to Sage standards and to build correctly without warnings",
    "created_at": "2012-08-14T15:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81734",
    "user": "https://github.com/saliola"
}
```

[attachment:trac_11929_8899-include_doc_in_reference_manual-fs.patch] deals with documentation:

- added entries in reference manual
- fixed markup to adhere to Sage standards and to build correctly without warnings



---

archive/issue_comments_081735.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-14T15:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81735",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081736.json:
```json
{
    "body": "Attachment [trac_11929_8899-include_doc_in_reference_manual-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-include_doc_in_reference_manual-fs.patch) by @saliola created at 2012-08-14 16:02:43",
    "created_at": "2012-08-14T16:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81736",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-include_doc_in_reference_manual-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-include_doc_in_reference_manual-fs.patch) by @saliola created at 2012-08-14 16:02:43



---

archive/issue_comments_081737.json:
```json
{
    "body": "Attachment [trac_11929_8899-modify_duality_method_names-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-modify_duality_method_names-fs.patch) by @saliola created at 2012-08-15 15:35:25\n\nThe patch [attachment: trac_11929_8899-modify_duality_method_names-fs.patch] modifies the duality method names to conform to #13372. Namely:\n\n- `object.dual` returns the dual object:\n\n```\nsage: N.dual()\nQuasisymmetric functions over the Rational Field\nsage: S.dual()\nQuasisymmetric functions over the Rational Field on the Monomial basis\nsage: R.dual()\nQuasisymmetric functions over the Rational Field on the Fundamental basis\n```\n\n\n- `dual_pairing` became `duality_pairing`",
    "created_at": "2012-08-15T15:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81737",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-modify_duality_method_names-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-modify_duality_method_names-fs.patch) by @saliola created at 2012-08-15 15:35:25

The patch [attachment: trac_11929_8899-modify_duality_method_names-fs.patch] modifies the duality method names to conform to #13372. Namely:

- `object.dual` returns the dual object:

```
sage: N.dual()
Quasisymmetric functions over the Rational Field
sage: S.dual()
Quasisymmetric functions over the Rational Field on the Monomial basis
sage: R.dual()
Quasisymmetric functions over the Rational Field on the Fundamental basis
```


- `dual_pairing` became `duality_pairing`



---

archive/issue_comments_081738.json:
```json
{
    "body": "Attachment [trac_11929_8899-is_symmetric-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-is_symmetric-fs.patch) by @saliola created at 2012-08-16 21:08:47",
    "created_at": "2012-08-16T21:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81738",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-is_symmetric-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-is_symmetric-fs.patch) by @saliola created at 2012-08-16 21:08:47



---

archive/issue_comments_081739.json:
```json
{
    "body": "[attachment: trac_11929_8899-is_symmetric-fs.patch] : fixes a bug Mike found in `is_symmetric` and renames `to_sym`  to `to_symmetric_function`.",
    "created_at": "2012-08-16T21:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81739",
    "user": "https://github.com/saliola"
}
```

[attachment: trac_11929_8899-is_symmetric-fs.patch] : fixes a bug Mike found in `is_symmetric` and renames `to_sym`  to `to_symmetric_function`.



---

archive/issue_comments_081740.json:
```json
{
    "body": "Attachment [trac_11929_8899-internal_product_fix-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-internal_product_fix-fs.patch) by @saliola created at 2012-08-16 21:27:00",
    "created_at": "2012-08-16T21:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81740",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-internal_product_fix-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-internal_product_fix-fs.patch) by @saliola created at 2012-08-16 21:27:00



---

archive/issue_comments_081741.json:
```json
{
    "body": "[attachment:trac_11929_8899-internal_product_fix-fs.patch] fixes an issue with categories since we haven't defined an internal product for QSym.",
    "created_at": "2012-08-16T21:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81741",
    "user": "https://github.com/saliola"
}
```

[attachment:trac_11929_8899-internal_product_fix-fs.patch] fixes an issue with categories since we haven't defined an internal product for QSym.



---

archive/issue_comments_081742.json:
```json
{
    "body": "minor doc fixes and a quasi-symmetric function tutorial",
    "created_at": "2012-08-17T20:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81742",
    "user": "https://github.com/zabrocki"
}
```

minor doc fixes and a quasi-symmetric function tutorial



---

archive/issue_comments_081743.json:
```json
{
    "body": "Attachment [trac_11929_8899-additional_documentation-mz.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-additional_documentation-mz.patch) by @zabrocki created at 2012-08-17 20:44:25\n\nMinor changes to documentation plus the addition of a tutorial for quasi-symmetric function and additional doc tests and examples.  The doc tests added use functionality that is in sage-5.3.beta2.",
    "created_at": "2012-08-17T20:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81743",
    "user": "https://github.com/zabrocki"
}
```

Attachment [trac_11929_8899-additional_documentation-mz.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-additional_documentation-mz.patch) by @zabrocki created at 2012-08-17 20:44:25

Minor changes to documentation plus the addition of a tutorial for quasi-symmetric function and additional doc tests and examples.  The doc tests added use functionality that is in sage-5.3.beta2.



---

archive/issue_comments_081744.json:
```json
{
    "body": "Attachment [trac_11929_8899-antipode_by_coercion_in_category-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-antipode_by_coercion_in_category-fs.patch) by @saliola created at 2012-08-18 02:05:55\n\nrebased to 5.3.beta2",
    "created_at": "2012-08-18T02:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81744",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-antipode_by_coercion_in_category-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-antipode_by_coercion_in_category-fs.patch) by @saliola created at 2012-08-18 02:05:55

rebased to 5.3.beta2



---

archive/issue_comments_081745.json:
```json
{
    "body": "Attachment [coproduct_with_realizations-fs.patch](tarball://root/attachments/some-uuid/ticket8899/coproduct_with_realizations-fs.patch) by @saliola created at 2012-08-18 02:21:19\n\nextra doctests for coproduct and counit",
    "created_at": "2012-08-18T02:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81745",
    "user": "https://github.com/saliola"
}
```

Attachment [coproduct_with_realizations-fs.patch](tarball://root/attachments/some-uuid/ticket8899/coproduct_with_realizations-fs.patch) by @saliola created at 2012-08-18 02:21:19

extra doctests for coproduct and counit



---

archive/issue_comments_081746.json:
```json
{
    "body": "For the patchbot\n\nApply: trac_11929_8899-ncsf-qsym-folded-fs.patch, trac_11929_8899-additional_documentation-fs.patch",
    "created_at": "2012-08-18T04:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81746",
    "user": "https://github.com/saliola"
}
```

For the patchbot

Apply: trac_11929_8899-ncsf-qsym-folded-fs.patch, trac_11929_8899-additional_documentation-fs.patch



---

archive/issue_comments_081747.json:
```json
{
    "body": "Attachment [trac_11929_8899-additional_documentation-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-additional_documentation-fs.patch) by @saliola created at 2012-08-18 04:50:12",
    "created_at": "2012-08-18T04:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81747",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-additional_documentation-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-additional_documentation-fs.patch) by @saliola created at 2012-08-18 04:50:12



---

archive/issue_comments_081748.json:
```json
{
    "body": "Hello Mike,\n\nThank you very much for your review, and your improvements to the documentation!\n\nI folded all the patches that you've seen, including your patch. And I created one more that makes changes to the documentation, adds some doctests, etc.\n\n*So please review this last patch: [attachment:trac_11929_8899-additional_documentation-fs.patch].*\n\nHere is a summary of the changes:\n\n- I noticed that some of the bases of NCSF and QSym had no documentation when one asks for the documentation using the command:\n\n  `NCSF.Ribbon?`\n\n  So I fixed that for all the bases.\n\n- In a few places, you used the letter F to refer to an arbitrary quasi-symmetric function. Since this is the prefix for the Fundamental basis, I decided to change this to another letter (I used H).\n\n- I made a some changes to your tutorial that I hope improve the exposition.",
    "created_at": "2012-08-18T05:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81748",
    "user": "https://github.com/saliola"
}
```

Hello Mike,

Thank you very much for your review, and your improvements to the documentation!

I folded all the patches that you've seen, including your patch. And I created one more that makes changes to the documentation, adds some doctests, etc.

*So please review this last patch: [attachment:trac_11929_8899-additional_documentation-fs.patch].*

Here is a summary of the changes:

- I noticed that some of the bases of NCSF and QSym had no documentation when one asks for the documentation using the command:

  `NCSF.Ribbon?`

  So I fixed that for all the bases.

- In a few places, you used the letter F to refer to an arbitrary quasi-symmetric function. Since this is the prefix for the Fundamental basis, I decided to change this to another letter (I used H).

- I made a some changes to your tutorial that I hope improve the exposition.



---

archive/issue_comments_081749.json:
```json
{
    "body": "Attachment [additional-addional-documentation-mz.patch](tarball://root/attachments/some-uuid/ticket8899/additional-addional-documentation-mz.patch) by @saliola created at 2012-08-22 18:02:43",
    "created_at": "2012-08-22T18:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81749",
    "user": "https://github.com/saliola"
}
```

Attachment [additional-addional-documentation-mz.patch](tarball://root/attachments/some-uuid/ticket8899/additional-addional-documentation-mz.patch) by @saliola created at 2012-08-22 18:02:43



---

archive/issue_comments_081750.json:
```json
{
    "body": "Attachment [trac_11929_8899-from_polynomial-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-from_polynomial-fs.patch) by @saliola created at 2012-08-22 18:28:33",
    "created_at": "2012-08-22T18:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81750",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-from_polynomial-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-from_polynomial-fs.patch) by @saliola created at 2012-08-22 18:28:33



---

archive/issue_comments_081751.json:
```json
{
    "body": "I folded the additional documentation patches (mine and Mike's) into the main patch since Mike gave mine a positive review and I positively reviewed Mike's changes.\n\nAnd I posted one more patch that adds a new method `from_polynomial` to QSym.\n\nOnly the patch [attachment:trac_11929_8899-from_polynomial-fs.patch] needs review.",
    "created_at": "2012-08-22T18:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81751",
    "user": "https://github.com/saliola"
}
```

I folded the additional documentation patches (mine and Mike's) into the main patch since Mike gave mine a positive review and I positively reviewed Mike's changes.

And I posted one more patch that adds a new method `from_polynomial` to QSym.

Only the patch [attachment:trac_11929_8899-from_polynomial-fs.patch] needs review.



---

archive/issue_comments_081752.json:
```json
{
    "body": "Patchbot, please apply the following patches and tell me all tests pass!\n\nApply: trac_11929_8899-ncsf-qsym-folded-fs.patch,  trac_11929_8899-from_polynomial-fs.patch",
    "created_at": "2012-08-22T18:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81752",
    "user": "https://github.com/saliola"
}
```

Patchbot, please apply the following patches and tell me all tests pass!

Apply: trac_11929_8899-ncsf-qsym-folded-fs.patch,  trac_11929_8899-from_polynomial-fs.patch



---

archive/issue_comments_081753.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-22T21:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81753",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081754.json:
```json
{
    "body": "trac_11929_8899-from_polynomial-fs.patch looks good to me",
    "created_at": "2012-08-22T21:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81754",
    "user": "https://github.com/mwhansen"
}
```

trac_11929_8899-from_polynomial-fs.patch looks good to me



---

archive/issue_comments_081755.json:
```json
{
    "body": "I have an issue with missing documentation.  For example, the method is_symmetric is not appearing in the documentation for qsym.py.  Can someone explain why?",
    "created_at": "2012-08-22T21:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81755",
    "user": "https://github.com/zabrocki"
}
```

I have an issue with missing documentation.  For example, the method is_symmetric is not appearing in the documentation for qsym.py.  Can someone explain why?



---

archive/issue_comments_081756.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-08-22T21:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81756",
    "user": "https://github.com/zabrocki"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081757.json:
```json
{
    "body": "My guess is #9107 (and related #11791).",
    "created_at": "2012-08-22T21:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81757",
    "user": "https://github.com/mwhansen"
}
```

My guess is #9107 (and related #11791).



---

archive/issue_comments_081758.json:
```json
{
    "body": "Replying to [comment:30 mhansen]:\n> My guess is #9107 (and related #11791).\nThanks Mike! I just tested and confirm that when I apply the patch that is attached to #9107 and then recompile, the missing documentation for methods appears.  I will post a few more corrections to the documentation shortly (e.g. coproduct_on_generators() in ncsf.py is weird and that probably was one of the missing methods before).",
    "created_at": "2012-08-22T22:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81758",
    "user": "https://github.com/zabrocki"
}
```

Replying to [comment:30 mhansen]:
> My guess is #9107 (and related #11791).
Thanks Mike! I just tested and confirm that when I apply the patch that is attached to #9107 and then recompile, the missing documentation for methods appears.  I will post a few more corrections to the documentation shortly (e.g. coproduct_on_generators() in ncsf.py is weird and that probably was one of the missing methods before).



---

archive/issue_comments_081759.json:
```json
{
    "body": "Attachment [trac_11929_8899_minor_docfix-mz.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899_minor_docfix-mz.patch) by @zabrocki created at 2012-08-22 22:33:06",
    "created_at": "2012-08-22T22:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81759",
    "user": "https://github.com/zabrocki"
}
```

Attachment [trac_11929_8899_minor_docfix-mz.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899_minor_docfix-mz.patch) by @zabrocki created at 2012-08-22 22:33:06



---

archive/issue_comments_081760.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-08-22T22:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81760",
    "user": "https://github.com/zabrocki"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_081761.json:
```json
{
    "body": "added a patch which inserts two colons in ncsf.py to clean up the documentation of two methods.  I've tested these patches after #9107 is applied and all tests pass! (I was slightly worried that some tests were not being executed because #9107 was not applied)",
    "created_at": "2012-08-22T22:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81761",
    "user": "https://github.com/zabrocki"
}
```

added a patch which inserts two colons in ncsf.py to clean up the documentation of two methods.  I've tested these patches after #9107 is applied and all tests pass! (I was slightly worried that some tests were not being executed because #9107 was not applied)



---

archive/issue_comments_081762.json:
```json
{
    "body": "Replying to [comment:31 zabrocki]:\n> Replying to [comment:30 mhansen]:\n> > My guess is #9107 (and related #11791).\n> Thanks Mike! I just tested and confirm that when I apply the patch that is attached to #9107 and then recompile, the missing documentation for methods appears.\n\nDoes that mean #9107 should be a dependency?",
    "created_at": "2012-08-23T07:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81762",
    "user": "https://github.com/simon-king-jena"
}
```

Replying to [comment:31 zabrocki]:
> Replying to [comment:30 mhansen]:
> > My guess is #9107 (and related #11791).
> Thanks Mike! I just tested and confirm that when I apply the patch that is attached to #9107 and then recompile, the missing documentation for methods appears.

Does that mean #9107 should be a dependency?



---

archive/issue_comments_081763.json:
```json
{
    "body": "Replying to [comment:33 SimonKing]:\n> Does that mean #9107 should be a dependency?\n\nI would not bother. There are already plenty of spots in Sage where the documentation does not build properly because of improper support for nested classes; this just adds another occurence. And everything will be fixed at once when #9107 will be merged, with no action to be taken on those spots.\n\nCheers,\n               Nicolas",
    "created_at": "2012-08-23T08:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81763",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:33 SimonKing]:
> Does that mean #9107 should be a dependency?

I would not bother. There are already plenty of spots in Sage where the documentation does not build properly because of improper support for nested classes; this just adds another occurence. And everything will be fixed at once when #9107 will be merged, with no action to be taken on those spots.

Cheers,
               Nicolas



---

archive/issue_comments_081764.json:
```json
{
    "body": "APPLY ONLY THIS PATCH!",
    "created_at": "2012-08-23T14:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81764",
    "user": "https://github.com/saliola"
}
```

APPLY ONLY THIS PATCH!



---

archive/issue_comments_081765.json:
```json
{
    "body": "Attachment [trac_11929_8899-ncsf-qsym-final.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-ncsf-qsym-final.patch) by @saliola created at 2012-08-23 14:06:26\n\nI folded these three patches together and cleaned up the commit message (so that that patchbot doesn't complain):\n* [attachment:trac_11929_8899-ncsf-qsym-folded-fs.patch]\n* [attachment:trac_11929_8899-from_polynomial-fs.patch]\n* [attachment:trac_11929_8899_minor_docfix-mz.patch]\n\nApply: [attachment:trac_11929_8899-ncsf-qsym-final.patch]",
    "created_at": "2012-08-23T14:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81765",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-ncsf-qsym-final.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-ncsf-qsym-final.patch) by @saliola created at 2012-08-23 14:06:26

I folded these three patches together and cleaned up the commit message (so that that patchbot doesn't complain):
* [attachment:trac_11929_8899-ncsf-qsym-folded-fs.patch]
* [attachment:trac_11929_8899-from_polynomial-fs.patch]
* [attachment:trac_11929_8899_minor_docfix-mz.patch]

Apply: [attachment:trac_11929_8899-ncsf-qsym-final.patch]



---

archive/issue_comments_081766.json:
```json
{
    "body": "Replying to [comment:34 nthiery]:\n> Replying to [comment:33 SimonKing]:\n> > Does that mean #9107 should be a dependency?\n> \n> I would not bother. There are already plenty of spots in Sage where the documentation does not build properly because of improper support for nested classes; this just adds another occurence. And everything will be fixed at once when #9107 will be merged, with no action to be taken on those spots.\n\nAnother reason not to: the docstrings for QSym / NCSF are detailed and most of the functionality is demonstrated in the examples there.",
    "created_at": "2012-08-23T14:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81766",
    "user": "https://github.com/saliola"
}
```

Replying to [comment:34 nthiery]:
> Replying to [comment:33 SimonKing]:
> > Does that mean #9107 should be a dependency?
> 
> I would not bother. There are already plenty of spots in Sage where the documentation does not build properly because of improper support for nested classes; this just adds another occurence. And everything will be fixed at once when #9107 will be merged, with no action to be taken on those spots.

Another reason not to: the docstrings for QSym / NCSF are detailed and most of the functionality is demonstrated in the examples there.



---

archive/issue_comments_081767.json:
```json
{
    "body": "This patch is ready to go, so I'm setting the milestone to sage-5.3 (instead of sage-wishlist).\n\nAn *unrelated* test failed on one of the patchbots, but I think this is just a glitch. I tried kicking it, so we'll see what happens. Is it necessary that all patchbots be happy before the patch is merged?",
    "created_at": "2012-08-24T16:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81767",
    "user": "https://github.com/saliola"
}
```

This patch is ready to go, so I'm setting the milestone to sage-5.3 (instead of sage-wishlist).

An *unrelated* test failed on one of the patchbots, but I think this is just a glitch. I tried kicking it, so we'll see what happens. Is it necessary that all patchbots be happy before the patch is merged?



---

archive/issue_comments_081768.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2012-09-02T15:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81768",
    "user": "https://github.com/saliola"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_081769.json:
```json
{
    "body": "Attachment [trac_11929_8899-ncsf-qsym-repr-fix-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-ncsf-qsym-repr-fix-fs.patch) by @saliola created at 2012-09-02 15:04:45\n\n[attachment:trac_11929_8899-ncsf-qsym-repr-fix-fs.patch] modifies `_repr_` to conform to the standards set out in #13404.\n\nNote: this patch does *not* depend on #13404.\n\nApply: trac_11929_8899-ncsf-qsym-final.patch, trac_11929_8899-ncsf-qsym-repr-fix-fs.patch",
    "created_at": "2012-09-02T15:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81769",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_11929_8899-ncsf-qsym-repr-fix-fs.patch](tarball://root/attachments/some-uuid/ticket8899/trac_11929_8899-ncsf-qsym-repr-fix-fs.patch) by @saliola created at 2012-09-02 15:04:45

[attachment:trac_11929_8899-ncsf-qsym-repr-fix-fs.patch] modifies `_repr_` to conform to the standards set out in #13404.

Note: this patch does *not* depend on #13404.

Apply: trac_11929_8899-ncsf-qsym-final.patch, trac_11929_8899-ncsf-qsym-repr-fix-fs.patch



---

archive/issue_comments_081770.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-09-02T15:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81770",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_081771.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-09-02T15:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81771",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081772.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-09-02T15:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81772",
    "user": "https://github.com/saliola"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081773.json:
```json
{
    "body": "I checked the patch, and am ok with it. Thanks Franco!\n\nAssuming that all tests pass (the failures currently reported by the patchbot seem unrelated), you can set it back to positive review on my behalf!\n\nCheers,\n                          Nicolas",
    "created_at": "2012-09-02T19:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81773",
    "user": "https://github.com/nthiery"
}
```

I checked the patch, and am ok with it. Thanks Franco!

Assuming that all tests pass (the failures currently reported by the patchbot seem unrelated), you can set it back to positive review on my behalf!

Cheers,
                          Nicolas



---

archive/issue_comments_081774.json:
```json
{
    "body": "All tests pass on sage-5.3.rc0 so I will give it a positive review.\nSince #5457 got de-merged from 5.3 and so you might need the patch coproduct_with_realizations-fs.patch if they are applied in the wrong order.  Should there be a dependency on #5457?",
    "created_at": "2012-09-02T21:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81774",
    "user": "https://github.com/zabrocki"
}
```

All tests pass on sage-5.3.rc0 so I will give it a positive review.
Since #5457 got de-merged from 5.3 and so you might need the patch coproduct_with_realizations-fs.patch if they are applied in the wrong order.  Should there be a dependency on #5457?



---

archive/issue_comments_081775.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-09-02T21:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81775",
    "user": "https://github.com/zabrocki"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081776.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-05T18:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81776",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009054.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-09-05T18:08:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8899#event-9054"
}
```



---

archive/issue_comments_081777.json:
```json
{
    "body": "With the new version, but I'm seeing failures which didn't happen with earlier versions:\n\n```\nsage -t  -force_lib devel/sage/sage/combinat/ncsf_qsym/ncsf.py\n**********************************************************************\nFile \"/release/merger/sage-5.4.beta1/devel/sage-main/sage/combinat/ncsf_qsym/ncsf.py\", line 493:\n    sage: R.to_symmetric_function\nExpected:\n    Generic morphism:\n      From: Non-Commutative Symmetric Functions over the Rational Field in the Ribbon basis\n      To:   Symmetric Function Algebra over Rational Field, Schur symmetric functions as basis\nGot:\n    Generic morphism:\n      From: Non-Commutative Symmetric Functions over the Rational Field in the Ribbon basis\n      To:   Symmetric Functions over Rational Field in the Schur basis\n**********************************************************************\n```\n",
    "created_at": "2012-09-07T18:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81777",
    "user": "https://github.com/jdemeyer"
}
```

With the new version, but I'm seeing failures which didn't happen with earlier versions:

```
sage -t  -force_lib devel/sage/sage/combinat/ncsf_qsym/ncsf.py
**********************************************************************
File "/release/merger/sage-5.4.beta1/devel/sage-main/sage/combinat/ncsf_qsym/ncsf.py", line 493:
    sage: R.to_symmetric_function
Expected:
    Generic morphism:
      From: Non-Commutative Symmetric Functions over the Rational Field in the Ribbon basis
      To:   Symmetric Function Algebra over Rational Field, Schur symmetric functions as basis
Got:
    Generic morphism:
      From: Non-Commutative Symmetric Functions over the Rational Field in the Ribbon basis
      To:   Symmetric Functions over Rational Field in the Schur basis
**********************************************************************
```




---

archive/issue_comments_081778.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2012-09-07T18:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81778",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_events_009055.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-09-07T18:20:12Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8899#event-9055"
}
```



---

archive/issue_comments_081779.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2012-09-07T18:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81779",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_081780.json:
```json
{
    "body": "I double-checked, and the phrase \"in the Schur basis\" does not appear in the patches on this ticket.\n\nI know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.",
    "created_at": "2012-09-07T23:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81780",
    "user": "https://github.com/saliola"
}
```

I double-checked, and the phrase "in the Schur basis" does not appear in the patches on this ticket.

I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.



---

archive/issue_comments_081781.json:
```json
{
    "body": "Replying to [comment:48 saliola]:\n> \n> I double-checked, and the phrase \"in the Schur basis\" does not appear in the patches on this ticket.\n> \n> I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.\n\nFranco is right. I will fix this in 13404 and put a dependency on 8899 there.\n\nBest,\n\nAnne",
    "created_at": "2012-09-08T05:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81781",
    "user": "https://github.com/anneschilling"
}
```

Replying to [comment:48 saliola]:
> 
> I double-checked, and the phrase "in the Schur basis" does not appear in the patches on this ticket.
> 
> I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.

Franco is right. I will fix this in 13404 and put a dependency on 8899 there.

Best,

Anne



---

archive/issue_comments_081782.json:
```json
{
    "body": "Replying to [comment:48 saliola]:\n> \n> I double-checked, and the phrase \"in the Schur basis\" does not appear in the patches on this ticket.\n> \n> I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.\nI always test a bunch of tickets together, and in this case I included indeed #13404.  So I will remove #13404 for now.",
    "created_at": "2012-09-08T08:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81782",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:48 saliola]:
> 
> I double-checked, and the phrase "in the Schur basis" does not appear in the patches on this ticket.
> 
> I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.
I always test a bunch of tickets together, and in this case I included indeed #13404.  So I will remove #13404 for now.



---

archive/issue_comments_081783.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-08T08:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81783",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009056.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-09-08T08:59:04Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8899#event-9056"
}
```



---

archive/issue_comments_081784.json:
```json
{
    "body": "This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.\n\nFor example:\n\n```\n                sage: R = NonCommutativeSymmetricFunctions(QQ).R()\n                sage: R.skew([2,1], [1])\n                Traceback (most recent call last):\n                ...\n                AssertionError: x must be an element of Non-Commutative Symmetric Functions over the Rational Field\n```\n\nThis is a simple user mistake, for which `assert` is not right.\n\nI think this must be fixed.",
    "created_at": "2012-09-24T07:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81784",
    "user": "https://github.com/jdemeyer"
}
```

This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.

For example:

```
                sage: R = NonCommutativeSymmetricFunctions(QQ).R()
                sage: R.skew([2,1], [1])
                Traceback (most recent call last):
                ...
                AssertionError: x must be an element of Non-Commutative Symmetric Functions over the Rational Field
```

This is a simple user mistake, for which `assert` is not right.

I think this must be fixed.



---

archive/issue_comments_081785.json:
```json
{
    "body": "Replying to [comment:51 jdemeyer]:\n> This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.\n> \n> For example:\n> {{{\n>                 sage: R = NonCommutativeSymmetricFunctions(QQ).R()\n>                 sage: R.skew([2,1], [1])\n>                 Traceback (most recent call last):\n>                 ...\n>                 AssertionError: x must be an element of Non-Commutative Symmetric Functions over the Rational Field\n> }}}\n> This is a simple user mistake, for which `assert` is not right.\n> \n> I think this must be fixed.\n\nI guess that's ok after all. See the same comment on  #5457.",
    "created_at": "2012-09-24T09:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81785",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:51 jdemeyer]:
> This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.
> 
> For example:
> {{{
>                 sage: R = NonCommutativeSymmetricFunctions(QQ).R()
>                 sage: R.skew([2,1], [1])
>                 Traceback (most recent call last):
>                 ...
>                 AssertionError: x must be an element of Non-Commutative Symmetric Functions over the Rational Field
> }}}
> This is a simple user mistake, for which `assert` is not right.
> 
> I think this must be fixed.

I guess that's ok after all. See the same comment on  #5457.



---

archive/issue_comments_081786.json:
```json
{
    "body": "This is a better example from this patch on how *not* to use assert:\n\n```\n            try:\n                assert self.is_homogeneous()\n                return self.parent().degree_on_basis(self.leading_support())\n            except AssertionError:\n                raise ValueError(\"Element is not homogeneous.\")\n```\n\n\nAnd this is an easily made mistake, it should give a `TypeError`:\n\n```\ndef from_polynomial(self, f, check=True):\n    ...\n    assert self.base_ring() == f.base_ring()\n```\n\nYou could even do:\n\n```\nif check and self.base_ring() != f.base_ring():\n    raise TypeError(...)\n```\n",
    "created_at": "2012-09-24T10:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81786",
    "user": "https://github.com/jdemeyer"
}
```

This is a better example from this patch on how *not* to use assert:

```
            try:
                assert self.is_homogeneous()
                return self.parent().degree_on_basis(self.leading_support())
            except AssertionError:
                raise ValueError("Element is not homogeneous.")
```


And this is an easily made mistake, it should give a `TypeError`:

```
def from_polynomial(self, f, check=True):
    ...
    assert self.base_ring() == f.base_ring()
```

You could even do:

```
if check and self.base_ring() != f.base_ring():
    raise TypeError(...)
```




---

archive/issue_comments_081787.json:
```json
{
    "body": "Changing keywords from \"sd40\" to \"sd40, days38\".",
    "created_at": "2012-10-02T13:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81787",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "sd40" to "sd40, days38".
