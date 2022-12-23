# Issue 9648: New feature: ModulesWithBasis allows module_morphism's to a wider class of codomains

archive/issues_009648.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat\n\nKeywords: ModulesWithBasis, module_morphism\n\nAt the moment, module morphisms are only allowed between modules with bases having the same base ring.\n\nThis patch allows a wider class of codomains, namely any parent with  a base ring having a coerce map from the base ring of domain:\n\n```\n    codomain.base_ring().has_coerce_map_from( domain.base_ring() )\n```\n\nis replaced by\n\n```\n    hasattr( codomain, 'base_ring' ) and\n        codomain.base_ring().has_coerce_map_from( domain.base_ring() )\n```\n\n\nAlso, module morphisms are not restricted anymore to having codomains being modules with basis but rings are allowed as well.\n\nHere are several examples included in the code:\n\nmodule morphisms from a module with basis to its base ring\n\n```\n                sage: X = CombinatorialFreeModule(QQ,[1,-1])\n                sage: phi = X.module_morphism( on_basis=lambda i: i, codomain=QQ )\n                sage: phi( 2 * X.monomial(1) + 3 * X.monomial(-1) )\n                -1\n```\n\n\nmodule morphisms from a module with basis to a base extension of its base ring\n\n```\n                sage: phi = X.module_morphism(on_basis= lambda i: i, codomain=RR )\n                sage: phi( 2 * X.monomial(1) + 3 * X.monomial(-1) )\n                -1.00000000000000\n```\n\n\nmodule morphisms from a module with basis to a module with basis over a base extension\n\n\n```\n                sage: R2 = CombinatorialFreeModule(RR,['x','y'])\n                sage: C  = CombinatorialFreeModule(CC,['z'])\n                sage: x  = X.monomial('x')\n                sage: y  = X.monomial('y')\n                sage: z  = Y.monomial('z')\n                sage: def on_basis( a ):\n                    if a == 'x':\n                        return CC(1) * z\n                    elif a == 'y':\n                        return CC(I) * z\n                ....:\n                sage: phi = R2.module_morphism( on_basis=on_basis, codomain=C )\n                sage: v = 3 * x + 2 * y\n                3.00000000000000*B['x'] + 2.00000000000000*B['y']\n                sage: phi(v)\n                (3.00000000000000+2.00000000000000*I)*B['z']\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9648\n\n",
    "created_at": "2010-07-30T18:19:22Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "New feature: ModulesWithBasis allows module_morphism's to a wider class of codomains",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9648",
    "user": "stumpc5"
}
```
Assignee: sage-combinat

CC:  sage-combinat

Keywords: ModulesWithBasis, module_morphism

At the moment, module morphisms are only allowed between modules with bases having the same base ring.

This patch allows a wider class of codomains, namely any parent with  a base ring having a coerce map from the base ring of domain:

```
    codomain.base_ring().has_coerce_map_from( domain.base_ring() )
```

is replaced by

```
    hasattr( codomain, 'base_ring' ) and
        codomain.base_ring().has_coerce_map_from( domain.base_ring() )
```


Also, module morphisms are not restricted anymore to having codomains being modules with basis but rings are allowed as well.

Here are several examples included in the code:

module morphisms from a module with basis to its base ring

```
                sage: X = CombinatorialFreeModule(QQ,[1,-1])
                sage: phi = X.module_morphism( on_basis=lambda i: i, codomain=QQ )
                sage: phi( 2 * X.monomial(1) + 3 * X.monomial(-1) )
                -1
```


module morphisms from a module with basis to a base extension of its base ring

```
                sage: phi = X.module_morphism(on_basis= lambda i: i, codomain=RR )
                sage: phi( 2 * X.monomial(1) + 3 * X.monomial(-1) )
                -1.00000000000000
```


module morphisms from a module with basis to a module with basis over a base extension


```
                sage: R2 = CombinatorialFreeModule(RR,['x','y'])
                sage: C  = CombinatorialFreeModule(CC,['z'])
                sage: x  = X.monomial('x')
                sage: y  = X.monomial('y')
                sage: z  = Y.monomial('z')
                sage: def on_basis( a ):
                    if a == 'x':
                        return CC(1) * z
                    elif a == 'y':
                        return CC(I) * z
                ....:
                sage: phi = R2.module_morphism( on_basis=on_basis, codomain=C )
                sage: v = 3 * x + 2 * y
                3.00000000000000*B['x'] + 2.00000000000000*B['y']
                sage: phi(v)
                (3.00000000000000+2.00000000000000*I)*B['z']
```



Issue created by migration from https://trac.sagemath.org/ticket/9648





---

archive/issue_comments_093555.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-30T18:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93555",
    "user": "stumpc5"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093556.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-30T18:24:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93556",
    "user": "stumpc5"
}
```

Attachment



---

archive/issue_comments_093557.json:
```json
{
    "body": "Effects Ticket #8589: would make the part on modules_with_basis.py in the provided patch in 8589 obsolete",
    "created_at": "2010-07-30T18:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93557",
    "user": "stumpc5"
}
```

Effects Ticket #8589: would make the part on modules_with_basis.py in the provided patch in 8589 obsolete



---

archive/issue_comments_093558.json:
```json
{
    "body": "I did the review with Christian here at FPSAC. Patch ready to go up to a final proofreading!",
    "created_at": "2010-08-04T18:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93558",
    "user": "nthiery"
}
```

I did the review with Christian here at FPSAC. Patch ready to go up to a final proofreading!



---

archive/issue_comments_093559.json:
```json
{
    "body": "Attachment\n\nAdded a test after request by Florent. Apply only this one.",
    "created_at": "2010-08-06T00:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93559",
    "user": "nthiery"
}
```

Attachment

Added a test after request by Florent. Apply only this one.



---

archive/issue_comments_093560.json:
```json
{
    "body": "All test pass with 4.5.1 and the following patches applied (all but the last one merged in 4.5.2):\n\n\n```\ntrac_8562-rebased.patch\ntrac_9256-set_in_category-fh.patch\ntrac_8984_crystals_alcove_path_model_bj.patch\ntrac_9250-crystalbug-as.patch\ntrac_9267-charge_jb.patch\ntrac_9485-strongly_connected_componnents_digraph-fix-nt.patch\ntrac_8810_stanley_symmetric_functions-sp-as.patch\ntrac_9259-combinatorialclass_doc_fix-fh.patch\ntrac_9215_doc_animate-sl.patch\ntrac_9216_doc_group_pyx-sl.patch\ntrac_8604_nfactor_enumerable-sl.patch\ntrac_8604-corrections-sl.patch\ntrac_9234_doc_texture-sl.patch\ntrac_9236_doc_sage_timeit-sl.patch\ntrac_9251-lazy_attribute_cython-fh.patch\ntrac_8413-Unknown_bool_value-fh.patch\nsage-5.0.patch\ntrac_9682_fix_perfectmatching_error_message_vf.patch\ntrac_9648_modulemorphism_codomain_extension.patch\n```\n",
    "created_at": "2010-08-06T00:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93560",
    "user": "nthiery"
}
```

All test pass with 4.5.1 and the following patches applied (all but the last one merged in 4.5.2):


```
trac_8562-rebased.patch
trac_9256-set_in_category-fh.patch
trac_8984_crystals_alcove_path_model_bj.patch
trac_9250-crystalbug-as.patch
trac_9267-charge_jb.patch
trac_9485-strongly_connected_componnents_digraph-fix-nt.patch
trac_8810_stanley_symmetric_functions-sp-as.patch
trac_9259-combinatorialclass_doc_fix-fh.patch
trac_9215_doc_animate-sl.patch
trac_9216_doc_group_pyx-sl.patch
trac_8604_nfactor_enumerable-sl.patch
trac_8604-corrections-sl.patch
trac_9234_doc_texture-sl.patch
trac_9236_doc_sage_timeit-sl.patch
trac_9251-lazy_attribute_cython-fh.patch
trac_8413-Unknown_bool_value-fh.patch
sage-5.0.patch
trac_9682_fix_perfectmatching_error_message_vf.patch
trac_9648_modulemorphism_codomain_extension.patch
```




---

archive/issue_comments_093561.json:
```json
{
    "body": "Replying to [comment:4 nthiery]:\n> All test pass with 4.5.1\n\nAll test pass with 4.5.3, except one sage.misc.sage_doc; however the later also fails with the main branch, so this must just be a quirk with my local installation.",
    "created_at": "2010-10-15T13:43:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93561",
    "user": "nthiery"
}
```

Replying to [comment:4 nthiery]:
> All test pass with 4.5.1

All test pass with 4.5.3, except one sage.misc.sage_doc; however the later also fails with the main branch, so this must just be a quirk with my local installation.



---

archive/issue_comments_093562.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-10-15T13:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93562",
    "user": "nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093563.json:
```json
{
    "body": "I get Sphinx errors, can you fix them?\n\n```\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha0/local/lib/python2.6/site-packages/sage/categories/modules_with_basis.py:docstring of sage.categories.modules_with_basis.ModulesWithBasis:21: (ERROR/3) Unexpected indentation.\n/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha0/local/lib/python2.6/site-packages/sage/categories/modules_with_basis.py:docstring of sage.categories.modules_with_basis.ModulesWithBasis.ParentMethods.module_morphism:85: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n```\n",
    "created_at": "2010-10-31T12:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93563",
    "user": "jdemeyer"
}
```

I get Sphinx errors, can you fix them?

```
/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha0/local/lib/python2.6/site-packages/sage/categories/modules_with_basis.py:docstring of sage.categories.modules_with_basis.ModulesWithBasis:21: (ERROR/3) Unexpected indentation.
/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha0/local/lib/python2.6/site-packages/sage/categories/modules_with_basis.py:docstring of sage.categories.modules_with_basis.ModulesWithBasis.ParentMethods.module_morphism:85: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```




---

archive/issue_comments_093564.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-10-31T12:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93564",
    "user": "jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093565.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-11-01T00:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93565",
    "user": "stumpc5"
}
```

Attachment



---

archive/issue_comments_093566.json:
```json
{
    "body": "> I get Sphinx errors, can you fix them?\n\nI hope, everything is fine now, some dots had the wrong indention...",
    "created_at": "2010-11-01T00:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93566",
    "user": "stumpc5"
}
```

> I get Sphinx errors, can you fix them?

I hope, everything is fine now, some dots had the wrong indention...



---

archive/issue_comments_093567.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-11-01T00:33:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93567",
    "user": "stumpc5"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_093568.json:
```json
{
    "body": "Reviewer patch, apply on top of previous",
    "created_at": "2010-11-01T21:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93568",
    "user": "jdemeyer"
}
```

Reviewer patch, apply on top of previous



---

archive/issue_comments_093569.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-01T21:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93569",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_093570.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-11-01T21:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9648#issuecomment-93570",
    "user": "jdemeyer"
}
```

Attachment
