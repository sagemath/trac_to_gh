# Issue 8881: Functorial constructions in categories

Issue created by migration from https://trac.sagemath.org/ticket/8881

Original creator: hivert

Original creation time: 2010-05-05 02:20:49

Assignee: nthiery

CC:  sage-combinat

Keywords: Functorial construction

Add functorial construction to categories. Examples include
   Tensor products, Group/Monoids/*Algebras, Subquotient...


---

Comment by hivert created at 2010-06-01 17:04:49

The patch is on review on sage-combinat-queue and should be ready soon. Please Nicolas, can you fold my last review patch if you are ok with it and upload the bunch here. I'll probably put a positive review after a last re-reading (and at least 5 folded review patches) :-)

Florent


---

Comment by hivert created at 2010-06-01 17:04:49

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-06-01 20:19:06

Changing keywords from "Functorial construction" to "Functorial constructions".


---

Comment by hivert created at 2010-06-01 22:09:55

Replying to [comment:2 nthiery]:

One last remark, otherwise I'm ready to give positive review: there is a slight naming inconsistency:
 - `CartesianProductFunctor, CartesianProducts, CartesianProductsCategory, cartesian_product`
 - `TensorFunctor, TensorProducts, TensorProductsCategory, tensor`

I'm just not 100% sure that we don't want `TensorProductFunctor` and `tensor_product`...

Any arguments ? 

By the way I put Priority=critical because they are at least a dozen of patch on sage-combinat which depend on this one...


---

Comment by hivert created at 2010-06-01 22:09:55

Changing priority from major to critical.


---

Comment by nthiery created at 2010-06-02 08:45:32

Renames TensorFunctor to TensorProductFunctor


---

Attachment

Diff to previous version of the patch


---

Comment by nthiery created at 2010-06-02 08:52:07

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

Comment by hivert created at 2010-06-02 09:09:37

Excellent ! Positive review unless Massena find a new bug (which is VeryUnlikely(TM)).


---

Comment by hivert created at 2010-06-02 09:09:37

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-06-02 13:36:21

Replying to [comment:5 hivert]:
> Excellent ! Positive review unless Massena find a new bug (which is VeryUnlikely(TM)). 

Thanks for all your work on this!


---

Comment by was created at 2010-06-03 04:26:12

Changing status from positive_review to needs_work.


---

Comment by was created at 2010-06-03 04:26:12

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

Comment by hivert created at 2010-06-03 06:09:33

Changing status from needs_work to needs_review.


---

Comment by hivert created at 2010-06-03 06:09:33

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

Comment by hivert created at 2010-06-03 06:11:25

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2010-06-03 06:11:25

Note: I put back positive review though I had no chance to test on `sage-4.4.3.alpha2`...


---

Comment by hivert created at 2010-06-03 06:14:53

Replying to [comment:8 hivert]:
> This bug is fixed in #9104 but it does appear on 4.4.2 so I didn't think about a dependency. Sorry for this. 

Actually it did (see the note there), but I completely forgot about it. My mistake.


---

Comment by mhansen created at 2010-06-05 21:44:23

Resolution: fixed
