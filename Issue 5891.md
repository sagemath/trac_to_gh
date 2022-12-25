# Issue 5891: Categories for the working mathematics programmer

archive/issues_005891.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat @roed314 @saliola\n\nKeywords: categories parents\n\nThis (series of) patch(es) extends the Sage category framework as a\ndesign pattern for organizing generic code.\n\nUnder development on combinat.sagemath.org/patches:\n\n- categories-nt.patch:    the category framework itself\n                        + updates to combinatorial free modules (will be split before submission)\n\nRelated patches (will need to be applied to recover all previous functionalities):\n- family_enumset-fh.patch\n- enumset_unions-fh.patch\n- categories-sf-nt.patch \tSymmetric functions\n- ncsf-nt.patch\t\tNon commutative Symmetric Functions\n- root_systems-4326-nt.patch\n\nSmall technical patches they depend on:\n- unique_representation-5120-submitted.patch\n- lazy_attributes-fixes-5783-final.patch\n- element_wrapper-nt.patch\n- 5598-coerce-declare.patch\n- cached_in_parent_method-5449.new\n- explain-pickle-v1.patch\n- cPickle-copy_reg_classes-nt.patch\n- cPickle-nested-classes-nt.patch\n- dynamic_class-nt.patch\n- compositions-cleanup-5600-nt.patch\n- transitive_ideal-nt.patch\n\n\nCurrent status:\n\n* Documentation:\n  sage.categories?         Category quickref card\n  sage.categories.primer?  Element/Parent/Category primer (in writing)\n  Category?                Technical background on categories\n  Semigroups().example()?? A template of semigroup\n  See also the discussion on sage-devel in November 2009:\n  http://groups.google.com/group/sage-devel/msg/d4065154e2e8cbd9\n\n* Real life applications:\n  see related patches, automatic monoids, ...\n\n* Categories:\n  - All the mathematical categories of Axiom and MuPAD\n  - EnumeratedSets         (with example)\n  - Semigroups             (with example, basic methods, subquotients)\n  - FiniteSemigroups       (with example, cayley graphs, basic representation theory, ...)\n  - ModulesWithBasis       (with example, morphisms)\n  - HopfAlgebras & friends (with example)\n  - Cleanup:\n    - Have unique representation by default (no need to inherit from Category_uniq)\n    - Have construction / reduce by default\n\n* Functorial constructions:\n  - direct sum\n  - tensor product\n  - cartesian product (todo)\n  - dual (in progress)\n  - subquotient, subset, quotient (in progress)\n  - isomorphism type (todo)\n\n* Homomorphisms\n  - Integrates with current sage morphisms\n  - Adds morphisms for some categories\n  - Some general infrastructure\n\n* Generic test framework\n  - Functional, final design clear, needs cleanup (2/3 hours)\n\n* Combinatorial free modules\n  * Have unique representation\n\n* Reorganization of the Sage library to start using the category framework:\n  * Fixed some import loops\n  * Added temporary list() methods to:\n    - FreeModule_generic\n    - MatrixSpace_generic\n    - Set_object_enumerated\n    - ParentWithAdditiveAbelianGens\n    - ParentWithMultiplicativeAbelianGens\n    They should eventually be inherited from the EnumeratedSets() category\n  * ...\n\n* Todo:\n  * Naming cleanup:\n    * Parent -> ParentMethods (or _ParentMethods? or ?)\n    * Element -> ElementMethods + move them as a nested class of ParentMethods\n    * super_categories should be a method\n    * zero, one should be methods\n    * standardize the names: mult / product / multiplication / multiply?\n    * check -> test\n    * self.tester(**keywords)\n    * intrusive cat.tensor_category / ...\n    * cat.example() -> /an_example/an_object/... ?\n    * class.an_instance() ?\n    * all_weakly_super_categories -> ?\n  * Category graph picture\n\n  * Fixes:\n    * Pickling: essentially works; polish the remaining\n    * Integration in the Sage library: some tests are broken. Help welcome!\n    * Pickling from old sage: technically feasible. Need help!\n    * Inheritance from category for Cython classes: technically feasible. Need help!\n\n  * Hom is *not* a functorial construction, the design and user\n    interface needs to be discussed\n\n  * Support for multivariate morphims, i.e. morphisms A x B -> C where\n    the specializations A x b -> C are morphisms for a given category\n    and a x B -> C are morphisms for a possibly different category\n\n* Discussion:\n  * Defining new inline operators, at least within the sage interpreter\n\nIssue created by migration from https://trac.sagemath.org/ticket/5891\n\n",
    "created_at": "2009-04-25T06:38:51Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Categories for the working mathematics programmer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5891",
    "user": "https://github.com/nthiery"
}
```
Assignee: @nthiery

CC:  sage-combinat @roed314 @saliola

Keywords: categories parents

This (series of) patch(es) extends the Sage category framework as a
design pattern for organizing generic code.

Under development on combinat.sagemath.org/patches:

- categories-nt.patch:    the category framework itself
                        + updates to combinatorial free modules (will be split before submission)

Related patches (will need to be applied to recover all previous functionalities):
- family_enumset-fh.patch
- enumset_unions-fh.patch
- categories-sf-nt.patch 	Symmetric functions
- ncsf-nt.patch		Non commutative Symmetric Functions
- root_systems-4326-nt.patch

Small technical patches they depend on:
- unique_representation-5120-submitted.patch
- lazy_attributes-fixes-5783-final.patch
- element_wrapper-nt.patch
- 5598-coerce-declare.patch
- cached_in_parent_method-5449.new
- explain-pickle-v1.patch
- cPickle-copy_reg_classes-nt.patch
- cPickle-nested-classes-nt.patch
- dynamic_class-nt.patch
- compositions-cleanup-5600-nt.patch
- transitive_ideal-nt.patch


Current status:

* Documentation:
  sage.categories?         Category quickref card
  sage.categories.primer?  Element/Parent/Category primer (in writing)
  Category?                Technical background on categories
  Semigroups().example()?? A template of semigroup
  See also the discussion on sage-devel in November 2009:
  http://groups.google.com/group/sage-devel/msg/d4065154e2e8cbd9

* Real life applications:
  see related patches, automatic monoids, ...

* Categories:
  - All the mathematical categories of Axiom and MuPAD
  - EnumeratedSets         (with example)
  - Semigroups             (with example, basic methods, subquotients)
  - FiniteSemigroups       (with example, cayley graphs, basic representation theory, ...)
  - ModulesWithBasis       (with example, morphisms)
  - HopfAlgebras & friends (with example)
  - Cleanup:
    - Have unique representation by default (no need to inherit from Category_uniq)
    - Have construction / reduce by default

* Functorial constructions:
  - direct sum
  - tensor product
  - cartesian product (todo)
  - dual (in progress)
  - subquotient, subset, quotient (in progress)
  - isomorphism type (todo)

* Homomorphisms
  - Integrates with current sage morphisms
  - Adds morphisms for some categories
  - Some general infrastructure

* Generic test framework
  - Functional, final design clear, needs cleanup (2/3 hours)

* Combinatorial free modules
  * Have unique representation

* Reorganization of the Sage library to start using the category framework:
  * Fixed some import loops
  * Added temporary list() methods to:
    - FreeModule_generic
    - MatrixSpace_generic
    - Set_object_enumerated
    - ParentWithAdditiveAbelianGens
    - ParentWithMultiplicativeAbelianGens
    They should eventually be inherited from the EnumeratedSets() category
  * ...

* Todo:
  * Naming cleanup:
    * Parent -> ParentMethods (or _ParentMethods? or ?)
    * Element -> ElementMethods + move them as a nested class of ParentMethods
    * super_categories should be a method
    * zero, one should be methods
    * standardize the names: mult / product / multiplication / multiply?
    * check -> test
    * self.tester(**keywords)
    * intrusive cat.tensor_category / ...
    * cat.example() -> /an_example/an_object/... ?
    * class.an_instance() ?
    * all_weakly_super_categories -> ?
  * Category graph picture

  * Fixes:
    * Pickling: essentially works; polish the remaining
    * Integration in the Sage library: some tests are broken. Help welcome!
    * Pickling from old sage: technically feasible. Need help!
    * Inheritance from category for Cython classes: technically feasible. Need help!

  * Hom is *not* a functorial construction, the design and user
    interface needs to be discussed

  * Support for multivariate morphims, i.e. morphisms A x B -> C where
    the specializations A x b -> C are morphisms for a given category
    and a x B -> C are morphisms for a possibly different category

* Discussion:
  * Defining new inline operators, at least within the sage interpreter

Issue created by migration from https://trac.sagemath.org/ticket/5891





---

archive/issue_comments_046491.json:
```json
{
    "body": "Where is categories-nt.patch itself?",
    "created_at": "2009-05-14T23:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46491",
    "user": "https://github.com/robertwb"
}
```

Where is categories-nt.patch itself?



---

archive/issue_comments_046492.json:
```json
{
    "body": "Replying to [comment:8 robertwb]:\n> Where is categories-nt.patch itself? \n\n\nOn the sage-combinat patch server. It changes too often to keep it updated on trac.\nI highlighted the link on top of the description (and improved the ReSTing)",
    "created_at": "2009-05-14T23:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46492",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:8 robertwb]:
> Where is categories-nt.patch itself? 


On the sage-combinat patch server. It changes too often to keep it updated on trac.
I highlighted the link on top of the description (and improved the ReSTing)



---

archive/issue_comments_046493.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-19T06:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46493",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046494.json:
```json
{
    "body": "Attachment [categories-framework-nt.patch](tarball://root/attachments/some-uuid/ticket5891/categories-framework-nt.patch) by @nthiery created at 2009-05-21 18:54:47",
    "created_at": "2009-05-21T18:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46494",
    "user": "https://github.com/nthiery"
}
```

Attachment [categories-framework-nt.patch](tarball://root/attachments/some-uuid/ticket5891/categories-framework-nt.patch) by @nthiery created at 2009-05-21 18:54:47



---

archive/issue_comments_046495.json:
```json
{
    "body": "Attachment [categories-fixsagelib-nt.patch](tarball://root/attachments/some-uuid/ticket5891/categories-fixsagelib-nt.patch) by @nthiery created at 2009-05-21 18:56:51",
    "created_at": "2009-05-21T18:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46495",
    "user": "https://github.com/nthiery"
}
```

Attachment [categories-fixsagelib-nt.patch](tarball://root/attachments/some-uuid/ticket5891/categories-fixsagelib-nt.patch) by @nthiery created at 2009-05-21 18:56:51



---

archive/issue_comments_046496.json:
```json
{
    "body": "Attachment [categories-enumeratedsets-nt.patch](tarball://root/attachments/some-uuid/ticket5891/categories-enumeratedsets-nt.patch) by @nthiery created at 2009-05-21 18:57:12",
    "created_at": "2009-05-21T18:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46496",
    "user": "https://github.com/nthiery"
}
```

Attachment [categories-enumeratedsets-nt.patch](tarball://root/attachments/some-uuid/ticket5891/categories-enumeratedsets-nt.patch) by @nthiery created at 2009-05-21 18:57:12



---

archive/issue_comments_046497.json:
```json
{
    "body": "Attachment [categories-combinat-nt.patch](tarball://root/attachments/some-uuid/ticket5891/categories-combinat-nt.patch) by @nthiery created at 2009-05-21 18:57:27",
    "created_at": "2009-05-21T18:57:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46497",
    "user": "https://github.com/nthiery"
}
```

Attachment [categories-combinat-nt.patch](tarball://root/attachments/some-uuid/ticket5891/categories-combinat-nt.patch) by @nthiery created at 2009-05-21 18:57:27



---

archive/issue_comments_046498.json:
```json
{
    "body": "Attachment [categories-numberfield_homset-nt.patch](tarball://root/attachments/some-uuid/ticket5891/categories-numberfield_homset-nt.patch) by @nthiery created at 2009-05-21 18:57:48",
    "created_at": "2009-05-21T18:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46498",
    "user": "https://github.com/nthiery"
}
```

Attachment [categories-numberfield_homset-nt.patch](tarball://root/attachments/some-uuid/ticket5891/categories-numberfield_homset-nt.patch) by @nthiery created at 2009-05-21 18:57:48



---

archive/issue_comments_046499.json:
```json
{
    "body": "There are the patches. They are file-orthogonal, so they should apply in any order.",
    "created_at": "2009-05-21T18:58:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46499",
    "user": "https://github.com/nthiery"
}
```

There are the patches. They are file-orthogonal, so they should apply in any order.



---

archive/issue_comments_046500.json:
```json
{
    "body": "Note: to get the latest version, please use the patch server.",
    "created_at": "2009-05-21T18:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46500",
    "user": "https://github.com/nthiery"
}
```

Note: to get the latest version, please use the patch server.



---

archive/issue_comments_046501.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2009-11-10T06:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46501",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_046502.json:
```json
{
    "body": "NOTES:\n\n  (1) Post the latest version here -- I don't want to mess with the patch server.\n\n  (2) It says \"Experts: please redefine this properly and/or put CC/RR/... in NumberFields()\".  I number field is by definition a finite extension of QQ, but CC and RR are infinite extensions of QQ.  So we can't put them in that category.   Having a function is_NumberFieldHomsetCodomain does seem like a good workaround for now.\n\n  (3) The function is_NumberFieldHomsetCodomain in the patch posted here doesn't have any documentation or doctests. Please add them. \n\n  (4) I would change these two lines:\n\n```\n        143\t        if is_Field(codomain): \n \t144\t            return True \n```\nto the single line \n\n```\n        143\t        return is_Field(codomain)\n```\nwhich should be functionally the same, and clearer to read. \n\n   (5) in a similar spirit, I would change\n\n```\n        145\t    except: \n \t146\t        pass     \n \t147\t    return False \n```\nto just\n\n```\n        145\t    except: \n \t146\t        return False\n```\nwhich is again clearer and equivalent. \n\n    (6) I'm puzzled by this in your number_field_rel.py patch:\n\n```\n\t543\t            return NotImplemented \n```\n\nWhat is NotImplemented? It's not defined in the number_field_rel.py file in sage-4.2.",
    "created_at": "2009-11-10T06:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46502",
    "user": "https://github.com/williamstein"
}
```

NOTES:

  (1) Post the latest version here -- I don't want to mess with the patch server.

  (2) It says "Experts: please redefine this properly and/or put CC/RR/... in NumberFields()".  I number field is by definition a finite extension of QQ, but CC and RR are infinite extensions of QQ.  So we can't put them in that category.   Having a function is_NumberFieldHomsetCodomain does seem like a good workaround for now.

  (3) The function is_NumberFieldHomsetCodomain in the patch posted here doesn't have any documentation or doctests. Please add them. 

  (4) I would change these two lines:

```
        143	        if is_Field(codomain): 
 	144	            return True 
```
to the single line 

```
        143	        return is_Field(codomain)
```
which should be functionally the same, and clearer to read. 

   (5) in a similar spirit, I would change

```
        145	    except: 
 	146	        pass     
 	147	    return False 
```
to just

```
        145	    except: 
 	146	        return False
```
which is again clearer and equivalent. 

    (6) I'm puzzled by this in your number_field_rel.py patch:

```
	543	            return NotImplemented 
```

What is NotImplemented? It's not defined in the number_field_rel.py file in sage-4.2.



---

archive/issue_comments_046503.json:
```json
{
    "body": "Replying to [comment:17 was]:\n> NOTES:\n> \n>   (1) Post the latest version here -- I don't want to mess with the patch server.\n\n\nI just added direct links in the description. I will post the patches shortly when they will be final.\n\n> \n>   (2) It says \"Experts: please redefine this properly and/or put CC/RR/... in NumberFields()\".  I number field is by definition a finite extension of QQ, but CC and RR are infinite extensions of QQ.  So we can't put them in that category.   Having a function is_NumberFieldHomsetCodomain does seem like a good workaround for now.\n\n\nOk.\n\n>   (3) The function is_NumberFieldHomsetCodomain in the patch posted here doesn't have any documentation or doctests. Please add them.\n\n\nOops. Will do.\n\n>   (4) (5) (6)\n\n\nYes better. Will do.\n\n>     (6) I'm puzzled by this in your number_field_rel.py patch:\n\n> {{{\n> \t543\t            return NotImplemented \n\n> }}}\n> \n> What is NotImplemented? It's not defined in the number_field_rel.py file in sage-4.2.\n\n\nIt's a builtin python object. Anyway, the function now raises a TypeError, per the latest _Hom_ protocol.",
    "created_at": "2009-11-10T10:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46503",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:17 was]:
> NOTES:
> 
>   (1) Post the latest version here -- I don't want to mess with the patch server.


I just added direct links in the description. I will post the patches shortly when they will be final.

> 
>   (2) It says "Experts: please redefine this properly and/or put CC/RR/... in NumberFields()".  I number field is by definition a finite extension of QQ, but CC and RR are infinite extensions of QQ.  So we can't put them in that category.   Having a function is_NumberFieldHomsetCodomain does seem like a good workaround for now.


Ok.

>   (3) The function is_NumberFieldHomsetCodomain in the patch posted here doesn't have any documentation or doctests. Please add them.


Oops. Will do.

>   (4) (5) (6)


Yes better. Will do.

>     (6) I'm puzzled by this in your number_field_rel.py patch:

> {{{
> 	543	            return NotImplemented 

> }}}
> 
> What is NotImplemented? It's not defined in the number_field_rel.py file in sage-4.2.


It's a builtin python object. Anyway, the function now raises a TypeError, per the latest _Hom_ protocol.



---

archive/issue_comments_046504.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-10T10:46:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46504",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046505.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-10T10:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46505",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_046506.json:
```json
{
    "body": "Changing component from misc to algebra.",
    "created_at": "2009-11-10T10:53:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46506",
    "user": "https://github.com/nthiery"
}
```

Changing component from misc to algebra.



---

archive/issue_comments_046507.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-10T12:43:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46507",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_046508.json:
```json
{
    "body": "Replying to [comment:19 nthiery]:\n> Replying to [comment:17 was]:\n> ...\n\nDone! See the linked to patch.\n\nI used the occasion to move the field containment logic into Fields where it belongs.",
    "created_at": "2009-11-10T12:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46508",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:19 nthiery]:
> Replying to [comment:17 was]:
> ...

Done! See the linked to patch.

I used the occasion to move the field containment logic into Fields where it belongs.



---

archive/issue_comments_046509.json:
```json
{
    "body": "Changing component from algebra to categories.",
    "created_at": "2009-11-15T10:21:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46509",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to categories.



---

archive/issue_comments_046510.json:
```json
{
    "body": "Merged the patches from changeset e70487186111.  They'll be posted on here in a bit.",
    "created_at": "2009-11-19T16:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46510",
    "user": "https://github.com/mwhansen"
}
```

Merged the patches from changeset e70487186111.  They'll be posted on here in a bit.



---

archive/issue_comments_046511.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-19T16:56:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46511",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_013836.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-19T16:56:33Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5891#event-13836"
}
```



---

archive/issue_events_013837.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-11-20T00:10:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5891#event-13837"
}
```



---

archive/issue_comments_046512.json:
```json
{
    "body": "Does anybody here remember the reason for the `is_extension_type()` condition in\n\n```python\n    def __make_element_class__(self, cls, name = None, inherit = None):\n        \"\"\"\n        A utility to construct classes for the elements of this\n        parent, with appropriate inheritance from the element class of\n        the category (only for pure python types so far).\n        \"\"\"\n        if name is None:\n            name = \"%s_with_category\"%cls.__name__\n        # By default, don't fiddle with extension types yet; inheritance from\n        # categories will probably be achieved in a different way\n        if inherit is None:\n            inherit = not is_extension_type(cls)\n        if inherit:\n            return dynamic_class(name, (cls, self.category().element_class))\n        else:\n            return cls\n```\nI just tried replacing `inherit = not is_extension_type(cls)` by `inherit = True` and there is almost nothing which breaks.",
    "created_at": "2017-07-14T09:04:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5891",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5891#issuecomment-46512",
    "user": "https://github.com/jdemeyer"
}
```

Does anybody here remember the reason for the `is_extension_type()` condition in

```python
    def __make_element_class__(self, cls, name = None, inherit = None):
        """
        A utility to construct classes for the elements of this
        parent, with appropriate inheritance from the element class of
        the category (only for pure python types so far).
        """
        if name is None:
            name = "%s_with_category"%cls.__name__
        # By default, don't fiddle with extension types yet; inheritance from
        # categories will probably be achieved in a different way
        if inherit is None:
            inherit = not is_extension_type(cls)
        if inherit:
            return dynamic_class(name, (cls, self.category().element_class))
        else:
            return cls
```
I just tried replacing `inherit = not is_extension_type(cls)` by `inherit = True` and there is almost nothing which breaks.
