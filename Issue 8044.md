# Issue 8044: Categories for finite (permutation) groups

Issue created by migration from https://trac.sagemath.org/ticket/8044

Original creator: nthiery

Original creation time: 2010-01-23 10:29:04

Assignee: nthiery

CC:  sage-combinat vengoroso@gmail.com

Keywords: Finite groups, permutation groups

This patch:

 - Introduces two new categories, FiniteGroups and FinitePermutationGroups
 - Deprecates the class sage.groups.group.FiniteGroup
   (content moved to the FiniteGroups category; this is essentially
   the cayley_graph method)
 - Puts all permutation groups and most other finite groups in the
   corresponding categories
 - As a result, this standardizes the interface of those groups
   (cardinality, one, ...), and reveals lots of failures in the
   completely undocumented PariGroup (category not set properly yet)
 - Makes a minor improvement to FiniteEnumeratedSets tests for
   large finite enumerated sets


---

Comment by nthiery created at 2010-01-23 10:32:53

Non finalized patch on: http://combinat.sagemath.org/hgwebdir.cgi/patches/file/tip/trac_8044-categories_finite_groups-nt.patch


---

Comment by nthiery created at 2010-01-27 22:02:01

Changing type from defect to enhancement.


---

Comment by nthiery created at 2010-01-27 22:02:01

Changing status from new to needs_review.


---

Comment by nthiery created at 2010-01-27 22:05:36

Changing keywords from "Finite groups, permutation groups" to "Finite groups, permutation groups, symmetric groups".


---

Comment by nthiery created at 2010-01-27 22:05:36

The attached patch passes all tests on 4.3.1 + the sage-combinat patches already merged in 4.3.2: !#7976 #7921 #7938 !#8028 #8001 !#5524


---

Comment by slabbe created at 2010-01-29 16:07:53

Applies over the precedent patch.


---

Attachment

I just added a patch which adds some examples of cayley graphs.

It also adds `FiniteGroup` to the base classes of `MatrixGroup_gap_finite_field`.


---

Comment by wdj created at 2010-01-31 14:11:51

Applies fine to 4.3.2.a0 and passes sage -t (except those 2 apparently singular-related tests which failed before).

I did not test sage -optional nor did I look carefully at how the category framework fits in with the rest of the category 
stuff (eg, Weyl groups). I did look at the permutation group aspect and positive review for that part. Was someone else going to look at the rest (Javier, vengoroso`@`gmail.com)? If not, please let me know.


---

Comment by nthiery created at 2010-01-31 20:27:06

Replying to [comment:7 wdj]:
> Applies fine to 4.3.2.a0 and passes sage -t (except those 2 apparently singular-related tests which failed before).
> 
> I did not test sage -optional nor did I look carefully at how the category framework fits in with the rest of the category 
> stuff (eg, Weyl groups). I did look at the permutation group aspect and positive review for that part. Was someone else going to look at the rest (Javier, vengoroso`@`gmail.com)? If not, please let me know.

Thanks much for your review!

Florent: could you have a look at the Weyl group + Cayley graph part?
David: did you check the matrix part? If not, do you mind handling it?
Javier: could you look at the category part?


---

Comment by wdj created at 2010-01-31 22:25:33

Replying to [comment:8 nthiery]:
> Replying to [comment:7 wdj]:
> > Applies fine to 4.3.2.a0 and passes sage -t (except those 2 apparently singular-related tests which failed before).
> > 
> > I did not test sage -optional nor did I look carefully at how the category framework fits in with the rest of the category 
> > stuff (eg, Weyl groups). I did look at the permutation group aspect and positive review for that part. Was someone else going to look at the rest (Javier, vengoroso`@`gmail.com)? If not, please let me know.
> 
> Thanks much for your review!
> 
> Florent: could you have a look at the Weyl group + Cayley graph part?
> David: did you check the matrix part? If not, do you mind handling it?


Yes, I looked at it and also give that part a positive review. I like the way you handled 
over different fields.


> Javier: could you look at the category part?
>


---

Comment by nthiery created at 2010-01-31 22:36:39

Replying to [comment:9 wdj]:
> > David: did you check the matrix part? If not, do you mind handling it?
> 
> Yes, I looked at it and also give that part a positive review. 

Thanks!

> I like the way you handled over different fields.

:-) 

Being able to choose at run time the category, and therefore the class hierarchy, as we could do in MuPAD, was one of my big incentive for writing the category code, and going for dynamic classes.


---

Comment by jlopez created at 2010-02-01 09:44:18

The category part looks fine to me. This is an amazing patch, btw!

I am getting some doctests failures:



```
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/doc/en/tutorial/tour_advanced.rst"
        sage -t  "devel/sage/doc/fr/tutorial/tour_advanced.rst"
        sage -t  "devel/sage/sage/categories/finite_groups.py"
        sage -t  "devel/sage/sage/categories/finite_permutation_groups.py"
        sage -t  "devel/sage/sage/groups/pari_group.py"
        sage -t  "devel/sage/sage/groups/perm_gps/permgroup_named.py"
        sage -t  "devel/sage/sage/interfaces/r.py"
        sage -t  "devel/sage/sage/rings/polynomial/groebner_fan.py"
        sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
```


though they don't seem too serious.

There are a couple of "The category of (multiplicative) finite semigroups" in the docstrings that should be corrected.

For the rest, assuming that the doctest pass (it might be something with my sage, will try with a clean install at the office in a couple of hours), positive review.


---

Attachment

Apply only this one


---

Comment by nthiery created at 2010-02-01 10:04:41

Replying to [comment:11 jlopez]:
> The category part looks fine to me. This is an amazing patch, btw!

:-)

> I am getting some doctests failures:
> 
> 
> {{{
> ----------------------------------------------------------------------
> The following tests failed:
> 
> 
>         sage -t  "devel/sage/doc/en/tutorial/tour_advanced.rst"
>         sage -t  "devel/sage/doc/fr/tutorial/tour_advanced.rst"
>         sage -t  "devel/sage/sage/categories/finite_groups.py"
>         sage -t  "devel/sage/sage/categories/finite_permutation_groups.py"
>         sage -t  "devel/sage/sage/groups/pari_group.py"
>         sage -t  "devel/sage/sage/groups/perm_gps/permgroup_named.py"
>         sage -t  "devel/sage/sage/interfaces/r.py"
>         sage -t  "devel/sage/sage/rings/polynomial/groebner_fan.py"
>         sage -t  "devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py"
> }}}
> 
> though they don't seem too serious.
> (it might be something with my sage, will try with a clean install at the office in a couple of hours),

For the record, could you please post or attach here the complete log of the failures, even if it works at your office?

> There are a couple of "The category of (multiplicative) finite semigroups" in the docstrings that should be corrected.

Oops, good catch. The updated patch fixes this.

> For the rest, assuming that the doctest pass positive review.

Thanks!


---

Comment by jlopez created at 2010-02-01 14:06:07

Changing status from needs_review to positive_review.


---

Comment by jlopez created at 2010-02-01 14:06:07

All tests pass on a clean install, so most probably my previous failure was due to too much fiddling with patches and source files (will upload the failures later anyway). Postive review.


---

Comment by mpatel created at 2010-02-11 14:45:54

Resolution: fixed
