# Issue 9648: New feature: ModulesWithBasis allows module_morphism's to a wider class of codomains

Issue created by migration from https://trac.sagemath.org/ticket/9648

Original creator: stumpc5

Original creation time: 2010-07-30 18:19:22

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




---

Comment by stumpc5 created at 2010-07-30 18:24:09

Changing status from new to needs_review.


---

Attachment


---

Comment by stumpc5 created at 2010-07-30 18:27:32

Effects Ticket #8589: would make the part on modules_with_basis.py in the provided patch in 8589 obsolete


---

Comment by nthiery created at 2010-08-04 18:05:08

I did the review with Christian here at FPSAC. Patch ready to go up to a final proofreading!


---

Attachment

Added a test after request by Florent. Apply only this one.


---

Comment by nthiery created at 2010-08-06 00:06:23

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

Comment by nthiery created at 2010-10-15 13:43:17

Replying to [comment:4 nthiery]:
> All test pass with 4.5.1

All test pass with 4.5.3, except one sage.misc.sage_doc; however the later also fails with the main branch, so this must just be a quirk with my local installation.


---

Comment by nthiery created at 2010-10-15 13:44:58

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-10-31 12:38:47

I get Sphinx errors, can you fix them?

```
/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha0/local/lib/python2.6/site-packages/sage/categories/modules_with_basis.py:docstring of sage.categories.modules_with_basis.ModulesWithBasis:21: (ERROR/3) Unexpected indentation.
/mnt/usb1/scratch/jdemeyer/merger/sage-4.6.1.alpha0/local/lib/python2.6/site-packages/sage/categories/modules_with_basis.py:docstring of sage.categories.modules_with_basis.ModulesWithBasis.ParentMethods.module_morphism:85: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```



---

Comment by jdemeyer created at 2010-10-31 12:38:47

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by stumpc5 created at 2010-11-01 00:33:09

> I get Sphinx errors, can you fix them?

I hope, everything is fine now, some dots had the wrong indention...


---

Comment by stumpc5 created at 2010-11-01 00:33:09

Changing status from needs_work to positive_review.


---

Comment by jdemeyer created at 2010-11-01 21:42:26

Reviewer patch, apply on top of previous


---

Comment by jdemeyer created at 2010-11-01 21:43:38

Resolution: fixed


---

Attachment
