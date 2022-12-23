# Issue 8899: Implement non commutative symmetric functions

archive/issues_008899.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat chrisjamesberg zabrocki aschilling\n\nPatch under dev. on the sage-combinat patch server\n\nIssue created by migration from https://trac.sagemath.org/ticket/8899\n\n",
    "created_at": "2010-05-05T23:39:46Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Implement non commutative symmetric functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8899",
    "user": "nthiery"
}
```
Assignee: sage-combinat

CC:  sage-combinat chrisjamesberg zabrocki aschilling

Patch under dev. on the sage-combinat patch server

Issue created by migration from https://trac.sagemath.org/ticket/8899





---

archive/issue_comments_081852.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-05T23:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81852",
    "user": "nthiery"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_081853.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-05-05T23:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81853",
    "user": "nthiery"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_081854.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-07-15T14:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81854",
    "user": "saliola"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081855.json:
```json
{
    "body": "Apply: trac_11929_8899-ncsf-qsym-folded-fs.patch, trac_11929_8899-additional_documentation-fs.patch \n\n(for the patchbot)",
    "created_at": "2012-07-15T14:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81855",
    "user": "saliola"
}
```

Apply: trac_11929_8899-ncsf-qsym-folded-fs.patch, trac_11929_8899-additional_documentation-fs.patch 

(for the patchbot)



---

archive/issue_comments_081856.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40\".",
    "created_at": "2012-07-15T14:30:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81856",
    "user": "saliola"
}
```

Changing keywords from "" to "sd40".



---

archive/issue_comments_081857.json:
```json
{
    "body": "A note on the patch coproduct_with_realizations-fs.patch: an earlier version of this patch was folded into the patch at #5457. So this patch is not needed if that ticket gets merged before this ticket. (I've included it here so that the patchbot can run all doctests.)\n\nIf this ticket gets merged before #5457, then an easy rebase of #5457 will be required.",
    "created_at": "2012-07-15T14:38:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81857",
    "user": "saliola"
}
```

A note on the patch coproduct_with_realizations-fs.patch: an earlier version of this patch was folded into the patch at #5457. So this patch is not needed if that ticket gets merged before this ticket. (I've included it here so that the patchbot can run all doctests.)

If this ticket gets merged before #5457, then an easy rebase of #5457 will be required.



---

archive/issue_comments_081858.json:
```json
{
    "body": "I put the author names in alphabetical order. I don't know the policy on this. I hope this is okay.",
    "created_at": "2012-07-15T14:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81858",
    "user": "saliola"
}
```

I put the author names in alphabetical order. I don't know the policy on this. I hope this is okay.



---

archive/issue_comments_081859.json:
```json
{
    "body": "(I think I learned something new about the patchbot: it ignores the order of the patches specified in the Apply directive and applies the patches in the order in which they get attached/updated.)",
    "created_at": "2012-07-15T15:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81859",
    "user": "saliola"
}
```

(I think I learned something new about the patchbot: it ignores the order of the patches specified in the Apply directive and applies the patches in the order in which they get attached/updated.)



---

archive/issue_comments_081860.json:
```json
{
    "body": "I think you guys need to add an entry in\n\ndoc/en/reference/combinat\n\nso that NSym and QSym are included in the documentation!\n\nAlso, I spotted an OUTPUT without the : behind it. Aren't we supposed to use\n\nINPUT:\n\n- ``x`` -- explanation\n\ni.e. a double dash after the variable to be explained?\n\nAnne",
    "created_at": "2012-07-19T23:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81860",
    "user": "aschilling"
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

archive/issue_comments_081861.json:
```json
{
    "body": "Thanks for catching these, Anne. We'll have to correct them.",
    "created_at": "2012-07-20T00:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81861",
    "user": "saliola"
}
```

Thanks for catching these, Anne. We'll have to correct them.



---

archive/issue_comments_081862.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-07-20T00:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81862",
    "user": "saliola"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081863.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-07-28T12:18:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81863",
    "user": "saliola"
}
```

Attachment



---

archive/issue_comments_081864.json:
```json
{
    "body": "I rebased [attachment:trac_11929_8899-ncsf-qsym-fs.patch] on #12959.\n\nChris, can you fix the documentation as explained by Anne:\n\n1. Add an entry in\n \n        `doc/en/reference/combinat`\n \n so that NSym and QSym are included in the documentation!\n \n2. Also, I spotted an OUTPUT without the : behind it.\n\n3. Proper syntax for INPUT blocks:\n \n        {{{\n        INPUT:\n \n        - ``x`` -- explanation\n        }}}\n \ni.e. a double dash after the variable to be explained [and a space after the initial dash]",
    "created_at": "2012-07-28T12:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81864",
    "user": "saliola"
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

archive/issue_comments_081865.json:
```json
{
    "body": "Attachment\n\nTwo new small patches.\n\n1. `trac_11929_8899-fix_skewby-fs.patch:` Fixes things so that the following raises an error:\n\n```\nF([2,1]).skew_by([1])\n```\n\n\n2. `trac_11929_8899-add_degree_to_elementmethods-fs.patch:` addes `ElementMethods.degree` and `ElementMethods.is_homogeneous` to `GradedAlgebrasWithBasis` (I extracted these from a separate patch on the sage-combinat queue).\n\n**Outstanding question about the degree of an element:** what do we want as the default behaviour? Should it:\na. raise an error if the element is not homogeneous; or\nb. return the maximum of the degrees of the homogeneous summands?",
    "created_at": "2012-08-13T20:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81865",
    "user": "saliola"
}
```

Attachment

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

archive/issue_comments_081866.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-08-14T14:18:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81866",
    "user": "saliola"
}
```

Attachment



---

archive/issue_comments_081867.json:
```json
{
    "body": "Replying to [comment:13 saliola]:\n> Two new small patches.\n> \n> 1. `trac_11929_8899-fix_skewby-fs.patch:` Fixes things so that the following raises an error:\n> {{{\n> F([2,1]).skew_by([1])\n> }}}\n> \n> 2. `trac_11929_8899-add_degree_to_elementmethods-fs.patch:` addes `ElementMethods.degree` and `ElementMethods.is_homogeneous` to `GradedAlgebrasWithBasis` (I extracted these from a separate patch on the sage-combinat queue).\n> \n> **Outstanding question about the degree of an element:** what do we want as the default behaviour? Should it:\n> a. raise an error if the element is not homogeneous; or\n> b. return the maximum of the degrees of the homogeneous summands?\n\nBased on the [discussion on sage-combinat-devel](https://groups.google.com/d/topic/sage-combinat-devel/pTjdBFeePWg/discussion), I updated [attachment:trac_11929_8899-add_degree_to_elementmethods-fs.patch]:\n- add methods `maximal_degree` and `homogeneous_degree` in `GradedAlgebrasWithBasis`\n- as a default in `GradedAlgebrasWithBasis`, set `degree = homogeneous_degree`\n- for NCSF/QSym, `degree` is redefined to be `maximal_degree`",
    "created_at": "2012-08-14T15:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81867",
    "user": "saliola"
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

archive/issue_comments_081868.json:
```json
{
    "body": "[attachment:trac_11929_8899-include_doc_in_reference_manual-fs.patch] deals with documentation:\n\n- added entries in reference manual\n- fixed markup to adhere to Sage standards and to build correctly without warnings",
    "created_at": "2012-08-14T15:43:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81868",
    "user": "saliola"
}
```

[attachment:trac_11929_8899-include_doc_in_reference_manual-fs.patch] deals with documentation:

- added entries in reference manual
- fixed markup to adhere to Sage standards and to build correctly without warnings



---

archive/issue_comments_081869.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-08-14T15:59:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81869",
    "user": "saliola"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081870.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-08-14T16:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81870",
    "user": "saliola"
}
```

Attachment



---

archive/issue_comments_081871.json:
```json
{
    "body": "Attachment\n\nThe patch [attachment: trac_11929_8899-modify_duality_method_names-fs.patch] modifies the duality method names to conform to #13372. Namely:\n\n- `object.dual` returns the dual object:\n\n```\nsage: N.dual()\nQuasisymmetric functions over the Rational Field\nsage: S.dual()\nQuasisymmetric functions over the Rational Field on the Monomial basis\nsage: R.dual()\nQuasisymmetric functions over the Rational Field on the Fundamental basis\n```\n\n\n- `dual_pairing` became `duality_pairing`",
    "created_at": "2012-08-15T15:35:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81871",
    "user": "saliola"
}
```

Attachment

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

archive/issue_comments_081872.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-08-16T21:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81872",
    "user": "saliola"
}
```

Attachment



---

archive/issue_comments_081873.json:
```json
{
    "body": "[attachment: trac_11929_8899-is_symmetric-fs.patch] : fixes a bug Mike found in `is_symmetric` and renames `to_sym`  to `to_symmetric_function`.",
    "created_at": "2012-08-16T21:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81873",
    "user": "saliola"
}
```

[attachment: trac_11929_8899-is_symmetric-fs.patch] : fixes a bug Mike found in `is_symmetric` and renames `to_sym`  to `to_symmetric_function`.



---

archive/issue_comments_081874.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-08-16T21:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81874",
    "user": "saliola"
}
```

Attachment



---

archive/issue_comments_081875.json:
```json
{
    "body": "[attachment:trac_11929_8899-internal_product_fix-fs.patch] fixes an issue with categories since we haven't defined an internal product for QSym.",
    "created_at": "2012-08-16T21:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81875",
    "user": "saliola"
}
```

[attachment:trac_11929_8899-internal_product_fix-fs.patch] fixes an issue with categories since we haven't defined an internal product for QSym.



---

archive/issue_comments_081876.json:
```json
{
    "body": "minor doc fixes and a quasi-symmetric function tutorial",
    "created_at": "2012-08-17T20:40:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81876",
    "user": "zabrocki"
}
```

minor doc fixes and a quasi-symmetric function tutorial



---

archive/issue_comments_081877.json:
```json
{
    "body": "Attachment\n\nMinor changes to documentation plus the addition of a tutorial for quasi-symmetric function and additional doc tests and examples.  The doc tests added use functionality that is in sage-5.3.beta2.",
    "created_at": "2012-08-17T20:44:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81877",
    "user": "zabrocki"
}
```

Attachment

Minor changes to documentation plus the addition of a tutorial for quasi-symmetric function and additional doc tests and examples.  The doc tests added use functionality that is in sage-5.3.beta2.



---

archive/issue_comments_081878.json:
```json
{
    "body": "Attachment\n\nrebased to 5.3.beta2",
    "created_at": "2012-08-18T02:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81878",
    "user": "saliola"
}
```

Attachment

rebased to 5.3.beta2



---

archive/issue_comments_081879.json:
```json
{
    "body": "Attachment\n\nextra doctests for coproduct and counit",
    "created_at": "2012-08-18T02:21:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81879",
    "user": "saliola"
}
```

Attachment

extra doctests for coproduct and counit



---

archive/issue_comments_081880.json:
```json
{
    "body": "For the patchbot\n\nApply: trac_11929_8899-ncsf-qsym-folded-fs.patch, trac_11929_8899-additional_documentation-fs.patch",
    "created_at": "2012-08-18T04:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81880",
    "user": "saliola"
}
```

For the patchbot

Apply: trac_11929_8899-ncsf-qsym-folded-fs.patch, trac_11929_8899-additional_documentation-fs.patch



---

archive/issue_comments_081881.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-08-18T04:50:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81881",
    "user": "saliola"
}
```

Attachment



---

archive/issue_comments_081882.json:
```json
{
    "body": "Hello Mike,\n\nThank you very much for your review, and your improvements to the documentation!\n\nI folded all the patches that you've seen, including your patch. And I created one more that makes changes to the documentation, adds some doctests, etc.\n\n*So please review this last patch: [attachment:trac_11929_8899-additional_documentation-fs.patch].*\n\nHere is a summary of the changes:\n\n- I noticed that some of the bases of NCSF and QSym had no documentation when one asks for the documentation using the command:\n\n  `NCSF.Ribbon?`\n\n  So I fixed that for all the bases.\n\n- In a few places, you used the letter F to refer to an arbitrary quasi-symmetric function. Since this is the prefix for the Fundamental basis, I decided to change this to another letter (I used H).\n\n- I made a some changes to your tutorial that I hope improve the exposition.",
    "created_at": "2012-08-18T05:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81882",
    "user": "saliola"
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

archive/issue_comments_081883.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-08-22T18:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81883",
    "user": "saliola"
}
```

Attachment



---

archive/issue_comments_081884.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-08-22T18:28:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81884",
    "user": "saliola"
}
```

Attachment



---

archive/issue_comments_081885.json:
```json
{
    "body": "I folded the additional documentation patches (mine and Mike's) into the main patch since Mike gave mine a positive review and I positively reviewed Mike's changes.\n\nAnd I posted one more patch that adds a new method `from_polynomial` to QSym.\n\nOnly the patch [attachment:trac_11929_8899-from_polynomial-fs.patch] needs review.",
    "created_at": "2012-08-22T18:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81885",
    "user": "saliola"
}
```

I folded the additional documentation patches (mine and Mike's) into the main patch since Mike gave mine a positive review and I positively reviewed Mike's changes.

And I posted one more patch that adds a new method `from_polynomial` to QSym.

Only the patch [attachment:trac_11929_8899-from_polynomial-fs.patch] needs review.



---

archive/issue_comments_081886.json:
```json
{
    "body": "Patchbot, please apply the following patches and tell me all tests pass!\n\nApply: trac_11929_8899-ncsf-qsym-folded-fs.patch,  trac_11929_8899-from_polynomial-fs.patch",
    "created_at": "2012-08-22T18:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81886",
    "user": "saliola"
}
```

Patchbot, please apply the following patches and tell me all tests pass!

Apply: trac_11929_8899-ncsf-qsym-folded-fs.patch,  trac_11929_8899-from_polynomial-fs.patch



---

archive/issue_comments_081887.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-22T21:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81887",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081888.json:
```json
{
    "body": "trac_11929_8899-from_polynomial-fs.patch looks good to me",
    "created_at": "2012-08-22T21:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81888",
    "user": "mhansen"
}
```

trac_11929_8899-from_polynomial-fs.patch looks good to me



---

archive/issue_comments_081889.json:
```json
{
    "body": "I have an issue with missing documentation.  For example, the method is_symmetric is not appearing in the documentation for qsym.py.  Can someone explain why?",
    "created_at": "2012-08-22T21:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81889",
    "user": "zabrocki"
}
```

I have an issue with missing documentation.  For example, the method is_symmetric is not appearing in the documentation for qsym.py.  Can someone explain why?



---

archive/issue_comments_081890.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2012-08-22T21:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81890",
    "user": "zabrocki"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081891.json:
```json
{
    "body": "My guess is #9107 (and related #11791).",
    "created_at": "2012-08-22T21:48:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81891",
    "user": "mhansen"
}
```

My guess is #9107 (and related #11791).



---

archive/issue_comments_081892.json:
```json
{
    "body": "Replying to [comment:30 mhansen]:\n> My guess is #9107 (and related #11791).\nThanks Mike! I just tested and confirm that when I apply the patch that is attached to #9107 and then recompile, the missing documentation for methods appears.  I will post a few more corrections to the documentation shortly (e.g. coproduct_on_generators() in ncsf.py is weird and that probably was one of the missing methods before).",
    "created_at": "2012-08-22T22:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81892",
    "user": "zabrocki"
}
```

Replying to [comment:30 mhansen]:
> My guess is #9107 (and related #11791).
Thanks Mike! I just tested and confirm that when I apply the patch that is attached to #9107 and then recompile, the missing documentation for methods appears.  I will post a few more corrections to the documentation shortly (e.g. coproduct_on_generators() in ncsf.py is weird and that probably was one of the missing methods before).



---

archive/issue_comments_081893.json:
```json
{
    "body": "Attachment",
    "created_at": "2012-08-22T22:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81893",
    "user": "zabrocki"
}
```

Attachment



---

archive/issue_comments_081894.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-08-22T22:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81894",
    "user": "zabrocki"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_081895.json:
```json
{
    "body": "added a patch which inserts two colons in ncsf.py to clean up the documentation of two methods.  I've tested these patches after #9107 is applied and all tests pass! (I was slightly worried that some tests were not being executed because #9107 was not applied)",
    "created_at": "2012-08-22T22:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81895",
    "user": "zabrocki"
}
```

added a patch which inserts two colons in ncsf.py to clean up the documentation of two methods.  I've tested these patches after #9107 is applied and all tests pass! (I was slightly worried that some tests were not being executed because #9107 was not applied)



---

archive/issue_comments_081896.json:
```json
{
    "body": "Replying to [comment:31 zabrocki]:\n> Replying to [comment:30 mhansen]:\n> > My guess is #9107 (and related #11791).\n> Thanks Mike! I just tested and confirm that when I apply the patch that is attached to #9107 and then recompile, the missing documentation for methods appears.\n\nDoes that mean #9107 should be a dependency?",
    "created_at": "2012-08-23T07:10:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81896",
    "user": "SimonKing"
}
```

Replying to [comment:31 zabrocki]:
> Replying to [comment:30 mhansen]:
> > My guess is #9107 (and related #11791).
> Thanks Mike! I just tested and confirm that when I apply the patch that is attached to #9107 and then recompile, the missing documentation for methods appears.

Does that mean #9107 should be a dependency?



---

archive/issue_comments_081897.json:
```json
{
    "body": "Replying to [comment:33 SimonKing]:\n> Does that mean #9107 should be a dependency?\n\nI would not bother. There are already plenty of spots in Sage where the documentation does not build properly because of improper support for nested classes; this just adds another occurence. And everything will be fixed at once when #9107 will be merged, with no action to be taken on those spots.\n\nCheers,\n               Nicolas",
    "created_at": "2012-08-23T08:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81897",
    "user": "nthiery"
}
```

Replying to [comment:33 SimonKing]:
> Does that mean #9107 should be a dependency?

I would not bother. There are already plenty of spots in Sage where the documentation does not build properly because of improper support for nested classes; this just adds another occurence. And everything will be fixed at once when #9107 will be merged, with no action to be taken on those spots.

Cheers,
               Nicolas



---

archive/issue_comments_081898.json:
```json
{
    "body": "APPLY ONLY THIS PATCH!",
    "created_at": "2012-08-23T14:02:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81898",
    "user": "saliola"
}
```

APPLY ONLY THIS PATCH!



---

archive/issue_comments_081899.json:
```json
{
    "body": "Attachment\n\nI folded these three patches together and cleaned up the commit message (so that that patchbot doesn't complain):\n* [attachment:trac_11929_8899-ncsf-qsym-folded-fs.patch]\n* [attachment:trac_11929_8899-from_polynomial-fs.patch]\n* [attachment:trac_11929_8899_minor_docfix-mz.patch]\n\nApply: [attachment:trac_11929_8899-ncsf-qsym-final.patch]",
    "created_at": "2012-08-23T14:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81899",
    "user": "saliola"
}
```

Attachment

I folded these three patches together and cleaned up the commit message (so that that patchbot doesn't complain):
* [attachment:trac_11929_8899-ncsf-qsym-folded-fs.patch]
* [attachment:trac_11929_8899-from_polynomial-fs.patch]
* [attachment:trac_11929_8899_minor_docfix-mz.patch]

Apply: [attachment:trac_11929_8899-ncsf-qsym-final.patch]



---

archive/issue_comments_081900.json:
```json
{
    "body": "Replying to [comment:34 nthiery]:\n> Replying to [comment:33 SimonKing]:\n> > Does that mean #9107 should be a dependency?\n> \n> I would not bother. There are already plenty of spots in Sage where the documentation does not build properly because of improper support for nested classes; this just adds another occurence. And everything will be fixed at once when #9107 will be merged, with no action to be taken on those spots.\n\nAnother reason not to: the docstrings for QSym / NCSF are detailed and most of the functionality is demonstrated in the examples there.",
    "created_at": "2012-08-23T14:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81900",
    "user": "saliola"
}
```

Replying to [comment:34 nthiery]:
> Replying to [comment:33 SimonKing]:
> > Does that mean #9107 should be a dependency?
> 
> I would not bother. There are already plenty of spots in Sage where the documentation does not build properly because of improper support for nested classes; this just adds another occurence. And everything will be fixed at once when #9107 will be merged, with no action to be taken on those spots.

Another reason not to: the docstrings for QSym / NCSF are detailed and most of the functionality is demonstrated in the examples there.



---

archive/issue_comments_081901.json:
```json
{
    "body": "This patch is ready to go, so I'm setting the milestone to sage-5.3 (instead of sage-wishlist).\n\nAn *unrelated* test failed on one of the patchbots, but I think this is just a glitch. I tried kicking it, so we'll see what happens. Is it necessary that all patchbots be happy before the patch is merged?",
    "created_at": "2012-08-24T16:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81901",
    "user": "saliola"
}
```

This patch is ready to go, so I'm setting the milestone to sage-5.3 (instead of sage-wishlist).

An *unrelated* test failed on one of the patchbots, but I think this is just a glitch. I tried kicking it, so we'll see what happens. Is it necessary that all patchbots be happy before the patch is merged?



---

archive/issue_comments_081902.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2012-09-02T15:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81902",
    "user": "saliola"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_081903.json:
```json
{
    "body": "Attachment\n\n[attachment:trac_11929_8899-ncsf-qsym-repr-fix-fs.patch] modifies `_repr_` to conform to the standards set out in #13404.\n\nNote: this patch does *not* depend on #13404.\n\nApply: trac_11929_8899-ncsf-qsym-final.patch, trac_11929_8899-ncsf-qsym-repr-fix-fs.patch",
    "created_at": "2012-09-02T15:04:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81903",
    "user": "saliola"
}
```

Attachment

[attachment:trac_11929_8899-ncsf-qsym-repr-fix-fs.patch] modifies `_repr_` to conform to the standards set out in #13404.

Note: this patch does *not* depend on #13404.

Apply: trac_11929_8899-ncsf-qsym-final.patch, trac_11929_8899-ncsf-qsym-repr-fix-fs.patch



---

archive/issue_comments_081904.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2012-09-02T15:05:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81904",
    "user": "saliola"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_081905.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2012-09-02T15:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81905",
    "user": "saliola"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081906.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-09-02T15:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81906",
    "user": "saliola"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081907.json:
```json
{
    "body": "I checked the patch, and am ok with it. Thanks Franco!\n\nAssuming that all tests pass (the failures currently reported by the patchbot seem unrelated), you can set it back to positive review on my behalf!\n\nCheers,\n                          Nicolas",
    "created_at": "2012-09-02T19:43:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81907",
    "user": "nthiery"
}
```

I checked the patch, and am ok with it. Thanks Franco!

Assuming that all tests pass (the failures currently reported by the patchbot seem unrelated), you can set it back to positive review on my behalf!

Cheers,
                          Nicolas



---

archive/issue_comments_081908.json:
```json
{
    "body": "All tests pass on sage-5.3.rc0 so I will give it a positive review.\nSince #5457 got de-merged from 5.3 and so you might need the patch coproduct_with_realizations-fs.patch if they are applied in the wrong order.  Should there be a dependency on #5457?",
    "created_at": "2012-09-02T21:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81908",
    "user": "zabrocki"
}
```

All tests pass on sage-5.3.rc0 so I will give it a positive review.
Since #5457 got de-merged from 5.3 and so you might need the patch coproduct_with_realizations-fs.patch if they are applied in the wrong order.  Should there be a dependency on #5457?



---

archive/issue_comments_081909.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-09-02T21:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81909",
    "user": "zabrocki"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081910.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-05T18:08:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81910",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_081911.json:
```json
{
    "body": "With the new version, but I'm seeing failures which didn't happen with earlier versions:\n\n```\nsage -t  -force_lib devel/sage/sage/combinat/ncsf_qsym/ncsf.py\n**********************************************************************\nFile \"/release/merger/sage-5.4.beta1/devel/sage-main/sage/combinat/ncsf_qsym/ncsf.py\", line 493:\n    sage: R.to_symmetric_function\nExpected:\n    Generic morphism:\n      From: Non-Commutative Symmetric Functions over the Rational Field in the Ribbon basis\n      To:   Symmetric Function Algebra over Rational Field, Schur symmetric functions as basis\nGot:\n    Generic morphism:\n      From: Non-Commutative Symmetric Functions over the Rational Field in the Ribbon basis\n      To:   Symmetric Functions over Rational Field in the Schur basis\n**********************************************************************\n```\n",
    "created_at": "2012-09-07T18:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81911",
    "user": "jdemeyer"
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

archive/issue_comments_081912.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2012-09-07T18:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81912",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_081913.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2012-09-07T18:20:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81913",
    "user": "jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_081914.json:
```json
{
    "body": "I double-checked, and the phrase \"in the Schur basis\" does not appear in the patches on this ticket.\n\nI know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.",
    "created_at": "2012-09-07T23:29:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81914",
    "user": "saliola"
}
```

I double-checked, and the phrase "in the Schur basis" does not appear in the patches on this ticket.

I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.



---

archive/issue_comments_081915.json:
```json
{
    "body": "Replying to [comment:48 saliola]:\n> \n> I double-checked, and the phrase \"in the Schur basis\" does not appear in the patches on this ticket.\n> \n> I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.\n\nFranco is right. I will fix this in 13404 and put a dependency on 8899 there.\n\nBest,\n\nAnne",
    "created_at": "2012-09-08T05:02:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81915",
    "user": "aschilling"
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

archive/issue_comments_081916.json:
```json
{
    "body": "Replying to [comment:48 saliola]:\n> \n> I double-checked, and the phrase \"in the Schur basis\" does not appear in the patches on this ticket.\n> \n> I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.\nI always test a bunch of tickets together, and in this case I included indeed #13404.  So I will remove #13404 for now.",
    "created_at": "2012-09-08T08:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81916",
    "user": "jdemeyer"
}
```

Replying to [comment:48 saliola]:
> 
> I double-checked, and the phrase "in the Schur basis" does not appear in the patches on this ticket.
> 
> I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.
I always test a bunch of tickets together, and in this case I included indeed #13404.  So I will remove #13404 for now.



---

archive/issue_comments_081917.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-08T08:59:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81917",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_081918.json:
```json
{
    "body": "This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.\n\nFor example:\n\n```\n                sage: R = NonCommutativeSymmetricFunctions(QQ).R()\n                sage: R.skew([2,1], [1])\n                Traceback (most recent call last):\n                ...\n                AssertionError: x must be an element of Non-Commutative Symmetric Functions over the Rational Field\n```\n\nThis is a simple user mistake, for which `assert` is not right.\n\nI think this must be fixed.",
    "created_at": "2012-09-24T07:11:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81918",
    "user": "jdemeyer"
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

archive/issue_comments_081919.json:
```json
{
    "body": "Replying to [comment:51 jdemeyer]:\n> This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.\n> \n> For example:\n> {{{\n>                 sage: R = NonCommutativeSymmetricFunctions(QQ).R()\n>                 sage: R.skew([2,1], [1])\n>                 Traceback (most recent call last):\n>                 ...\n>                 AssertionError: x must be an element of Non-Commutative Symmetric Functions over the Rational Field\n> }}}\n> This is a simple user mistake, for which `assert` is not right.\n> \n> I think this must be fixed.\n\nI guess that's ok after all. See the same comment on  #5457.",
    "created_at": "2012-09-24T09:17:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81919",
    "user": "nthiery"
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

archive/issue_comments_081920.json:
```json
{
    "body": "This is a better example from this patch on how *not* to use assert:\n\n```\n            try:\n                assert self.is_homogeneous()\n                return self.parent().degree_on_basis(self.leading_support())\n            except AssertionError:\n                raise ValueError(\"Element is not homogeneous.\")\n```\n\n\nAnd this is an easily made mistake, it should give a `TypeError`:\n\n```\ndef from_polynomial(self, f, check=True):\n    ...\n    assert self.base_ring() == f.base_ring()\n```\n\nYou could even do:\n\n```\nif check and self.base_ring() != f.base_ring():\n    raise TypeError(...)\n```\n",
    "created_at": "2012-09-24T10:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81920",
    "user": "jdemeyer"
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

archive/issue_comments_081921.json:
```json
{
    "body": "Changing keywords from \"sd40\" to \"sd40, days38\".",
    "created_at": "2012-10-02T13:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8899",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8899#issuecomment-81921",
    "user": "nthiery"
}
```

Changing keywords from "sd40" to "sd40, days38".
