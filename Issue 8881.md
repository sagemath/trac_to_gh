# Issue 8881: Functorial constructions in categories

archive/issues_008881.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: Functorial construction\n\nAdd functorial construction to categories. Examples include\n   Tensor products, Group/Monoids/*Algebras, Subquotient...\n\nIssue created by migration from https://trac.sagemath.org/ticket/8881\n\n",
    "created_at": "2010-05-05T02:20:49Z",
    "labels": [
        "component: categories"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Functorial constructions in categories",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8881",
    "user": "https://github.com/hivert"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: Functorial construction

Add functorial construction to categories. Examples include
   Tensor products, Group/Monoids/*Algebras, Subquotient...

Issue created by migration from https://trac.sagemath.org/ticket/8881





---

archive/issue_comments_081482.json:
```json
{
    "body": "The patch is on review on sage-combinat-queue and should be ready soon. Please Nicolas, can you fold my last review patch if you are ok with it and upload the bunch here. I'll probably put a positive review after a last re-reading (and at least 5 folded review patches) :-)\n\nFlorent",
    "created_at": "2010-06-01T17:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81482",
    "user": "https://github.com/hivert"
}
```

The patch is on review on sage-combinat-queue and should be ready soon. Please Nicolas, can you fold my last review patch if you are ok with it and upload the bunch here. I'll probably put a positive review after a last re-reading (and at least 5 folded review patches) :-)

Florent



---

archive/issue_comments_081483.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-01T17:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81483",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081484.json:
```json
{
    "body": "Changing keywords from \"Functorial construction\" to \"Functorial constructions\".",
    "created_at": "2010-06-01T20:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81484",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "Functorial construction" to "Functorial constructions".



---

archive/issue_comments_081485.json:
```json
{
    "body": "Replying to [comment:2 nthiery]:\n\nOne last remark, otherwise I'm ready to give positive review: there is a slight naming inconsistency:\n- `CartesianProductFunctor, CartesianProducts, CartesianProductsCategory, cartesian_product`\n- `TensorFunctor, TensorProducts, TensorProductsCategory, tensor`\n\nI'm just not 100% sure that we don't want `TensorProductFunctor` and `tensor_product`...\n\nAny arguments ? \n\nBy the way I put Priority=critical because they are at least a dozen of patch on sage-combinat which depend on this one...",
    "created_at": "2010-06-01T22:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81485",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:2 nthiery]:

One last remark, otherwise I'm ready to give positive review: there is a slight naming inconsistency:
- `CartesianProductFunctor, CartesianProducts, CartesianProductsCategory, cartesian_product`
- `TensorFunctor, TensorProducts, TensorProductsCategory, tensor`

I'm just not 100% sure that we don't want `TensorProductFunctor` and `tensor_product`...

Any arguments ? 

By the way I put Priority=critical because they are at least a dozen of patch on sage-combinat which depend on this one...



---

archive/issue_comments_081486.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-06-01T22:09:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81486",
    "user": "https://github.com/hivert"
}
```

Changing priority from major to critical.



---

archive/issue_comments_081487.json:
```json
{
    "body": "Renames TensorFunctor to TensorProductFunctor",
    "created_at": "2010-06-02T08:45:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81487",
    "user": "https://github.com/nthiery"
}
```

Renames TensorFunctor to TensorProductFunctor



---

archive/issue_comments_081488.json:
```json
{
    "body": "Attachment [diff](tarball://root/attachments/some-uuid/ticket8881/diff) by @nthiery created at 2010-06-02 08:46:07\n\nDiff to previous version of the patch",
    "created_at": "2010-06-02T08:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81488",
    "user": "https://github.com/nthiery"
}
```

Attachment [diff](tarball://root/attachments/some-uuid/ticket8881/diff) by @nthiery created at 2010-06-02 08:46:07

Diff to previous version of the patch



---

archive/issue_comments_081489.json:
```json
{
    "body": "Replying to [comment:3 hivert]:\n> One last remark, otherwise I'm ready to give positive review: there is a slight naming inconsistency:\n>  - `CartesianProductFunctor, CartesianProducts, CartesianProductsCategory, cartesian_product`\n>  - `TensorFunctor, TensorProducts, TensorProductsCategory, tensor`\n> \n> I'm just not 100% sure that we don't want `TensorProductFunctor` and `tensor_product`...\n> \n> Any arguments ?\n\nYup, we had discussed this with David Roe during the review of the\ncategory patches. And we had agreed that `tensor([A,B,C])` was\nshorter and more practical than `tensor_product([A,B,C])`, yet\nclear and unambiguous. On the other hand `cartesian([A,B,C])`\nwasn't that clear. So we decided to favor here practicality over\nconsistency.\n\nOn the other hand, I fixed TensorFunctor to TensorProductFunctor in\nthe updated patch.",
    "created_at": "2010-06-02T08:52:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81489",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:3 hivert]:
> One last remark, otherwise I'm ready to give positive review: there is a slight naming inconsistency:
>  - `CartesianProductFunctor, CartesianProducts, CartesianProductsCategory, cartesian_product`
>  - `TensorFunctor, TensorProducts, TensorProductsCategory, tensor`
> 
> I'm just not 100% sure that we don't want `TensorProductFunctor` and `tensor_product`...
> 
> Any arguments ?

Yup, we had discussed this with David Roe during the review of the
category patches. And we had agreed that `tensor([A,B,C])` was
shorter and more practical than `tensor_product([A,B,C])`, yet
clear and unambiguous. On the other hand `cartesian([A,B,C])`
wasn't that clear. So we decided to favor here practicality over
consistency.

On the other hand, I fixed TensorFunctor to TensorProductFunctor in
the updated patch.



---

archive/issue_comments_081490.json:
```json
{
    "body": "Excellent ! Positive review unless Massena find a new bug (which is VeryUnlikely(TM)).",
    "created_at": "2010-06-02T09:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81490",
    "user": "https://github.com/hivert"
}
```

Excellent ! Positive review unless Massena find a new bug (which is VeryUnlikely(TM)).



---

archive/issue_comments_081491.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-02T09:09:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81491",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081492.json:
```json
{
    "body": "Replying to [comment:5 hivert]:\n> Excellent ! Positive review unless Massena find a new bug (which is VeryUnlikely(TM)). \n\nThanks for all your work on this!",
    "created_at": "2010-06-02T13:36:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81492",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:5 hivert]:
> Excellent ! Positive review unless Massena find a new bug (which is VeryUnlikely(TM)). 

Thanks for all your work on this!



---

archive/issue_comments_081493.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-06-03T04:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81493",
    "user": "https://github.com/williamstein"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_081494.json:
```json
{
    "body": "This causes doctest failures, including the following. \n\n```\n\nsage -t  sage/categories/sets_cat.py\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/devel/sage-main/sage/categories/sets_cat.py\", line 624:\n    sage: A = Monoids().example().algebra(QQ); A\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_16[4]>\", line 1, in <module>\n        A = Monoids().example().algebra(QQ); A###line 624:\n    sage: A = Monoids().example().algebra(QQ); A\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/categories/sets_cat.py\", line 637, in algebra\n        return CombinatorialFreeModule(base_ring, self, category = category.Algebras(base_ring))\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/misc/classcall_metaclass.py\", line 256, in __call__\n        return cls.__classcall_private__(cls, *args, **options)\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/combinat/free_module.py\", line 850, in __classcall_private__\n        return super(CombinatorialFreeModule, cls).__classcall__(cls, *args, **keywords)\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/misc/cachefunc.py\", line 115, in __call__\n        w = self.f(*args, **kwds)\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/structure/unique_representation.py\", line 447, in __classcall__\n        instance = type.__call__(cls, *args, **options)\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/combinat/free_module.py\", line 892, in __init__\n        element_constructor = self._element_constructor_)\n      File \"parent.pyx\", line 457, in sage.structure.parent.Parent.__init__ (sage/structure/parent.c:3851)\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/categories/magmas.py\", line 115, in __init_extra__\n        if (self.product != self.product_from_element_class_mul) and hasattr(self, \"element_class\") and hasattr(self.element_class, \"_mul_parent\"):\n      File \"element.pyx\", line 860, in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:7061)\n      File \"element.pyx\", line 801, in sage.structure.element.Element._richcmp (sage/structure/element.c:6441)\n      File \"coerce.pyx\", line 907, in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:8537)\n      File \"sage_object.pyx\", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1370)\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/categories/homset.py\", line 302, in _repr_\n        self._domain, self._codomain, self.__category)\n      File \"sage_object.pyx\", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1370)\n      File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/combinat/free_module.py\", line 1163, in _repr_\n        return self._name + \" over %s\"%self.base_ring()\n      File \"parent.pyx\", line 676, in sage.structure.parent.Parent.__getattr__ (sage/structure/parent.c:5239)\n      File \"parent.pyx\", line 263, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2753)\n      File \"parent.pyx\", line 171, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2625)\n    AttributeError: 'CombinatorialFreeModule_with_category' object has no attribute '_name'\n**********************************************************************\nFile \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/devel/sage-main/sage/categories/sets_cat.py\", line 626:\n    sage: A.category()\nExpected:\n    Category of monoid algebras over Rational Field\nGot:\n    Category of set algebras over Rational Field\n**********************************************************************\n1 items had failures:\n   2 of   8 in __main__.example_16\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_sets_cat.py\n```\n",
    "created_at": "2010-06-03T04:26:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81494",
    "user": "https://github.com/williamstein"
}
```

This causes doctest failures, including the following. 

```

sage -t  sage/categories/sets_cat.py
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/devel/sage-main/sage/categories/sets_cat.py", line 624:
    sage: A = Monoids().example().algebra(QQ); A
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[4]>", line 1, in <module>
        A = Monoids().example().algebra(QQ); A###line 624:
    sage: A = Monoids().example().algebra(QQ); A
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/categories/sets_cat.py", line 637, in algebra
        return CombinatorialFreeModule(base_ring, self, category = category.Algebras(base_ring))
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/misc/classcall_metaclass.py", line 256, in __call__
        return cls.__classcall_private__(cls, *args, **options)
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/combinat/free_module.py", line 850, in __classcall_private__
        return super(CombinatorialFreeModule, cls).__classcall__(cls, *args, **keywords)
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/misc/cachefunc.py", line 115, in __call__
        w = self.f(*args, **kwds)
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/structure/unique_representation.py", line 447, in __classcall__
        instance = type.__call__(cls, *args, **options)
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/combinat/free_module.py", line 892, in __init__
        element_constructor = self._element_constructor_)
      File "parent.pyx", line 457, in sage.structure.parent.Parent.__init__ (sage/structure/parent.c:3851)
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/categories/magmas.py", line 115, in __init_extra__
        if (self.product != self.product_from_element_class_mul) and hasattr(self, "element_class") and hasattr(self.element_class, "_mul_parent"):
      File "element.pyx", line 860, in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:7061)
      File "element.pyx", line 801, in sage.structure.element.Element._richcmp (sage/structure/element.c:6441)
      File "coerce.pyx", line 907, in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:8537)
      File "sage_object.pyx", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1370)
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/categories/homset.py", line 302, in _repr_
        self._domain, self._codomain, self.__category)
      File "sage_object.pyx", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1370)
      File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/local/lib/python/site-packages/sage/combinat/free_module.py", line 1163, in _repr_
        return self._name + " over %s"%self.base_ring()
      File "parent.pyx", line 676, in sage.structure.parent.Parent.__getattr__ (sage/structure/parent.c:5239)
      File "parent.pyx", line 263, in sage.structure.parent.getattr_from_other_class (sage/structure/parent.c:2753)
      File "parent.pyx", line 171, in sage.structure.parent.raise_attribute_error (sage/structure/parent.c:2625)
    AttributeError: 'CombinatorialFreeModule_with_category' object has no attribute '_name'
**********************************************************************
File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/devel/sage-main/sage/categories/sets_cat.py", line 626:
    sage: A.category()
Expected:
    Category of monoid algebras over Rational Field
Got:
    Category of set algebras over Rational Field
**********************************************************************
1 items had failures:
   2 of   8 in __main__.example_16
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_sets_cat.py
```




---

archive/issue_comments_081495.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-03T06:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81495",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081496.json:
```json
{
    "body": "Replying to [comment:7 was]:\n> This causes doctest failures, including the following. \n\n```\n> \n> sage -t  sage/categories/sets_cat.py\n> **********************************************************************\n> File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/devel/sage-main/sage/categories/sets_cat.py\", line 624:\n>     sage: A = Monoids().example().algebra(QQ); A\n> Exception raised:\n. [...]\n>     AttributeError: 'CombinatorialFreeModule_with_category' object has no attribute '_name'\n> **********************************************************************\n> File \"/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/devel/sage-main/sage/categories/sets_cat.py\", line 626:\n>     sage: A.category()\n> Expected:\n>     Category of monoid algebras over Rational Field\n> Got:\n>     Category of set algebras over Rational Field\n> **********************************************************************\n```\n\n\nThis bug is fixed in #9104 but it does appear on 4.4.2 so I didn't think about a dependency. Sorry for this.",
    "created_at": "2010-06-03T06:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81496",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:7 was]:
> This causes doctest failures, including the following. 

```
> 
> sage -t  sage/categories/sets_cat.py
> **********************************************************************
> File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/devel/sage-main/sage/categories/sets_cat.py", line 624:
>     sage: A = Monoids().example().algebra(QQ); A
> Exception raised:
. [...]
>     AttributeError: 'CombinatorialFreeModule_with_category' object has no attribute '_name'
> **********************************************************************
> File "/mnt/usb1/scratch/wstein/build/release/4.4.3/sage-4.4.3.alpha2/devel/sage-main/sage/categories/sets_cat.py", line 626:
>     sage: A.category()
> Expected:
>     Category of monoid algebras over Rational Field
> Got:
>     Category of set algebras over Rational Field
> **********************************************************************
```


This bug is fixed in #9104 but it does appear on 4.4.2 so I didn't think about a dependency. Sorry for this.



---

archive/issue_comments_081497.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-03T06:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81497",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_081498.json:
```json
{
    "body": "Note: I put back positive review though I had no chance to test on `sage-4.4.3.alpha2`...",
    "created_at": "2010-06-03T06:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81498",
    "user": "https://github.com/hivert"
}
```

Note: I put back positive review though I had no chance to test on `sage-4.4.3.alpha2`...



---

archive/issue_comments_081499.json:
```json
{
    "body": "Replying to [comment:8 hivert]:\n> This bug is fixed in #9104 but it does appear on 4.4.2 so I didn't think about a dependency. Sorry for this. \n\nActually it did (see the note there), but I completely forgot about it. My mistake.",
    "created_at": "2010-06-03T06:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81499",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:8 hivert]:
> This bug is fixed in #9104 but it does appear on 4.4.2 so I didn't think about a dependency. Sorry for this. 

Actually it did (see the note there), but I completely forgot about it. My mistake.



---

archive/issue_comments_081500.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T21:44:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8881#issuecomment-81500",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_009038.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-05T21:44:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8881",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8881#event-9038"
}
```
