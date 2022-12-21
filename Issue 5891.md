# Issue 5891: Categories for the working mathematics programmer

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-04-25 06:38:51

Assignee: nthiery

CC:  sage-combinat roed saliola

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


---

Comment by robertwb created at 2009-05-14 23:01:45

Where is categories-nt.patch itself?


---

Comment by nthiery created at 2009-05-14 23:32:20

Replying to [comment:8 robertwb]:
> Where is categories-nt.patch itself? 

On the sage-combinat patch server. It changes too often to keep it updated on trac.
I highlighted the link on top of the description (and improved the ReSTing)


---

Comment by nthiery created at 2009-05-19 06:24:42

Changing status from new to assigned.


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by nthiery created at 2009-05-21 18:58:55

There are the patches. They are file-orthogonal, so they should apply in any order.


---

Comment by nthiery created at 2009-05-21 18:59:44

Note: to get the latest version, please use the patch server.


---

Comment by was created at 2009-11-10 06:50:41

Changing status from new to needs_work.


---

Comment by was created at 2009-11-10 06:50:41

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

Comment by nthiery created at 2009-11-10 10:46:42

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

Comment by nthiery created at 2009-11-10 10:46:42

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2009-11-10 10:53:01

Changing status from needs_review to needs_work.


---

Comment by nthiery created at 2009-11-10 10:53:01

Changing component from misc to algebra.


---

Comment by nthiery created at 2009-11-10 12:43:11

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2009-11-10 12:47:08

Replying to [comment:19 nthiery]:
> Replying to [comment:17 was]:
> ...
Done! See the linked to patch.

I used the occasion to move the field containment logic into Fields where it belongs.


---

Comment by AlexGhitza created at 2009-11-15 10:21:52

Changing component from algebra to categories.


---

Comment by mhansen created at 2009-11-19 16:56:33

Merged the patches from changeset e70487186111.  They'll be posted on here in a bit.


---

Comment by mhansen created at 2009-11-19 16:56:33

Resolution: fixed


---

Comment by jdemeyer created at 2017-07-14 09:04:32

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
