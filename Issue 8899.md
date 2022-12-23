# Issue 8899: Implement non commutative symmetric functions

Issue created by migration from https://trac.sagemath.org/ticket/8899

Original creator: nthiery

Original creation time: 2010-05-05 23:39:46

Assignee: sage-combinat

CC:  sage-combinat chrisjamesberg zabrocki aschilling

Patch under dev. on the sage-combinat patch server


---

Comment by nthiery created at 2010-05-05 23:40:05

Changing status from new to needs_work.


---

Comment by nthiery created at 2010-05-05 23:40:14

Changing type from defect to enhancement.


---

Comment by saliola created at 2012-07-15 14:30:34

Changing status from needs_work to needs_review.


---

Comment by saliola created at 2012-07-15 14:30:34

Apply: trac_11929_8899-ncsf-qsym-folded-fs.patch, trac_11929_8899-additional_documentation-fs.patch 

(for the patchbot)


---

Comment by saliola created at 2012-07-15 14:30:34

Changing keywords from "" to "sd40".


---

Comment by saliola created at 2012-07-15 14:38:50

A note on the patch coproduct_with_realizations-fs.patch: an earlier version of this patch was folded into the patch at #5457. So this patch is not needed if that ticket gets merged before this ticket. (I've included it here so that the patchbot can run all doctests.)

If this ticket gets merged before #5457, then an easy rebase of #5457 will be required.


---

Comment by saliola created at 2012-07-15 14:42:08

I put the author names in alphabetical order. I don't know the policy on this. I hope this is okay.


---

Comment by saliola created at 2012-07-15 15:22:39

(I think I learned something new about the patchbot: it ignores the order of the patches specified in the Apply directive and applies the patches in the order in which they get attached/updated.)


---

Comment by aschilling created at 2012-07-19 23:37:08

I think you guys need to add an entry in

doc/en/reference/combinat

so that NSym and QSym are included in the documentation!

Also, I spotted an OUTPUT without the : behind it. Aren't we supposed to use

INPUT:

- ``x`` -- explanation

i.e. a double dash after the variable to be explained?

Anne


---

Comment by saliola created at 2012-07-20 00:51:44

Thanks for catching these, Anne. We'll have to correct them.


---

Comment by saliola created at 2012-07-20 00:51:44

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by saliola created at 2012-07-28 12:31:29

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

Attachment

Two new small patches.

1. `trac_11929_8899-fix_skewby-fs.patch:` Fixes things so that the following raises an error:

```
F([2,1]).skew_by([1])
```


2. `trac_11929_8899-add_degree_to_elementmethods-fs.patch:` addes `ElementMethods.degree` and `ElementMethods.is_homogeneous` to `GradedAlgebrasWithBasis` (I extracted these from a separate patch on the sage-combinat queue).

*Outstanding question about the degree of an element:* what do we want as the default behaviour? Should it:
a. raise an error if the element is not homogeneous; or
b. return the maximum of the degrees of the homogeneous summands?


---

Attachment


---

Comment by saliola created at 2012-08-14 15:38:59

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
> *Outstanding question about the degree of an element:* what do we want as the default behaviour? Should it:
> a. raise an error if the element is not homogeneous; or
> b. return the maximum of the degrees of the homogeneous summands?

Based on the [discussion on sage-combinat-devel](https://groups.google.com/d/topic/sage-combinat-devel/pTjdBFeePWg/discussion), I updated [attachment:trac_11929_8899-add_degree_to_elementmethods-fs.patch]:
- add methods `maximal_degree` and `homogeneous_degree` in `GradedAlgebrasWithBasis`
- as a default in `GradedAlgebrasWithBasis`, set `degree = homogeneous_degree`
- for NCSF/QSym, `degree` is redefined to be `maximal_degree`


---

Comment by saliola created at 2012-08-14 15:43:29

[attachment:trac_11929_8899-include_doc_in_reference_manual-fs.patch] deals with documentation:

- added entries in reference manual
- fixed markup to adhere to Sage standards and to build correctly without warnings


---

Comment by saliola created at 2012-08-14 15:59:25

Changing status from needs_work to needs_review.


---

Attachment


---

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

Attachment


---

Comment by saliola created at 2012-08-16 21:10:14

[attachment: trac_11929_8899-is_symmetric-fs.patch] : fixes a bug Mike found in `is_symmetric` and renames `to_sym`  to `to_symmetric_function`.


---

Attachment


---

Comment by saliola created at 2012-08-16 21:29:25

[attachment:trac_11929_8899-internal_product_fix-fs.patch] fixes an issue with categories since we haven't defined an internal product for QSym.


---

Comment by zabrocki created at 2012-08-17 20:40:18

minor doc fixes and a quasi-symmetric function tutorial


---

Attachment

Minor changes to documentation plus the addition of a tutorial for quasi-symmetric function and additional doc tests and examples.  The doc tests added use functionality that is in sage-5.3.beta2.


---

Attachment

rebased to 5.3.beta2


---

Attachment

extra doctests for coproduct and counit


---

Comment by saliola created at 2012-08-18 04:41:04

For the patchbot

Apply: trac_11929_8899-ncsf-qsym-folded-fs.patch, trac_11929_8899-additional_documentation-fs.patch


---

Attachment


---

Comment by saliola created at 2012-08-18 05:05:38

Hello Mike,

Thank you very much for your review, and your improvements to the documentation!

I folded all the patches that you've seen, including your patch. And I created one more that makes changes to the documentation, adds some doctests, etc.

_So please review this last patch: [attachment:trac_11929_8899-additional_documentation-fs.patch]._

Here is a summary of the changes:

- I noticed that some of the bases of NCSF and QSym had no documentation when one asks for the documentation using the command:

  `NCSF.Ribbon?`

  So I fixed that for all the bases.

- In a few places, you used the letter F to refer to an arbitrary quasi-symmetric function. Since this is the prefix for the Fundamental basis, I decided to change this to another letter (I used H).

- I made a some changes to your tutorial that I hope improve the exposition.


---

Attachment


---

Attachment


---

Comment by saliola created at 2012-08-22 18:35:43

I folded the additional documentation patches (mine and Mike's) into the main patch since Mike gave mine a positive review and I positively reviewed Mike's changes.

And I posted one more patch that adds a new method `from_polynomial` to QSym.

Only the patch [attachment:trac_11929_8899-from_polynomial-fs.patch] needs review.


---

Comment by saliola created at 2012-08-22 18:39:32

Patchbot, please apply the following patches and tell me all tests pass!

Apply: trac_11929_8899-ncsf-qsym-folded-fs.patch,  trac_11929_8899-from_polynomial-fs.patch


---

Comment by mhansen created at 2012-08-22 21:19:15

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2012-08-22 21:19:15

trac_11929_8899-from_polynomial-fs.patch looks good to me


---

Comment by zabrocki created at 2012-08-22 21:35:35

I have an issue with missing documentation.  For example, the method is_symmetric is not appearing in the documentation for qsym.py.  Can someone explain why?


---

Comment by zabrocki created at 2012-08-22 21:35:35

Changing status from positive_review to needs_work.


---

Comment by mhansen created at 2012-08-22 21:48:34

My guess is #9107 (and related #11791).


---

Comment by zabrocki created at 2012-08-22 22:09:39

Replying to [comment:30 mhansen]:
> My guess is #9107 (and related #11791).
Thanks Mike! I just tested and confirm that when I apply the patch that is attached to #9107 and then recompile, the missing documentation for methods appears.  I will post a few more corrections to the documentation shortly (e.g. coproduct_on_generators() in ncsf.py is weird and that probably was one of the missing methods before).


---

Attachment


---

Comment by zabrocki created at 2012-08-22 22:39:59

Changing status from needs_work to positive_review.


---

Comment by zabrocki created at 2012-08-22 22:39:59

added a patch which inserts two colons in ncsf.py to clean up the documentation of two methods.  I've tested these patches after #9107 is applied and all tests pass! (I was slightly worried that some tests were not being executed because #9107 was not applied)


---

Comment by SimonKing created at 2012-08-23 07:10:43

Replying to [comment:31 zabrocki]:
> Replying to [comment:30 mhansen]:
> > My guess is #9107 (and related #11791).
> Thanks Mike! I just tested and confirm that when I apply the patch that is attached to #9107 and then recompile, the missing documentation for methods appears.

Does that mean #9107 should be a dependency?


---

Comment by nthiery created at 2012-08-23 08:02:22

Replying to [comment:33 SimonKing]:
> Does that mean #9107 should be a dependency?

I would not bother. There are already plenty of spots in Sage where the documentation does not build properly because of improper support for nested classes; this just adds another occurence. And everything will be fixed at once when #9107 will be merged, with no action to be taken on those spots.

Cheers,
               Nicolas


---

Comment by saliola created at 2012-08-23 14:02:35

APPLY ONLY THIS PATCH!


---

Attachment

I folded these three patches together and cleaned up the commit message (so that that patchbot doesn't complain):
    * [attachment:trac_11929_8899-ncsf-qsym-folded-fs.patch]
    * [attachment:trac_11929_8899-from_polynomial-fs.patch]
    * [attachment:trac_11929_8899_minor_docfix-mz.patch]

Apply: [attachment:trac_11929_8899-ncsf-qsym-final.patch]


---

Comment by saliola created at 2012-08-23 14:10:13

Replying to [comment:34 nthiery]:
> Replying to [comment:33 SimonKing]:
> > Does that mean #9107 should be a dependency?
> 
> I would not bother. There are already plenty of spots in Sage where the documentation does not build properly because of improper support for nested classes; this just adds another occurence. And everything will be fixed at once when #9107 will be merged, with no action to be taken on those spots.

Another reason not to: the docstrings for QSym / NCSF are detailed and most of the functionality is demonstrated in the examples there.


---

Comment by saliola created at 2012-08-24 16:16:51

This patch is ready to go, so I'm setting the milestone to sage-5.3 (instead of sage-wishlist).

An _unrelated_ test failed on one of the patchbots, but I think this is just a glitch. I tried kicking it, so we'll see what happens. Is it necessary that all patchbots be happy before the patch is merged?


---

Comment by saliola created at 2012-09-02 15:04:45

Changing status from positive_review to needs_info.


---

Attachment

[attachment:trac_11929_8899-ncsf-qsym-repr-fix-fs.patch] modifies `_repr_` to conform to the standards set out in #13404.

Note: this patch does _not_ depend on #13404.

Apply: trac_11929_8899-ncsf-qsym-final.patch, trac_11929_8899-ncsf-qsym-repr-fix-fs.patch


---

Comment by saliola created at 2012-09-02 15:05:09

Changing status from needs_info to needs_review.


---

Comment by saliola created at 2012-09-02 15:18:43

Changing status from needs_review to needs_work.


---

Comment by saliola created at 2012-09-02 15:30:40

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2012-09-02 19:43:24

I checked the patch, and am ok with it. Thanks Franco!

Assuming that all tests pass (the failures currently reported by the patchbot seem unrelated), you can set it back to positive review on my behalf!

Cheers,
                          Nicolas


---

Comment by zabrocki created at 2012-09-02 21:46:06

All tests pass on sage-5.3.rc0 so I will give it a positive review.
Since #5457 got de-merged from 5.3 and so you might need the patch coproduct_with_realizations-fs.patch if they are applied in the wrong order.  Should there be a dependency on #5457?


---

Comment by zabrocki created at 2012-09-02 21:46:06

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-09-05 18:08:29

Resolution: fixed


---

Comment by jdemeyer created at 2012-09-07 18:20:12

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

Comment by jdemeyer created at 2012-09-07 18:20:12

Changing status from closed to new.


---

Comment by jdemeyer created at 2012-09-07 18:20:12

Resolution changed from fixed to 


---

Comment by saliola created at 2012-09-07 23:29:33

I double-checked, and the phrase "in the Schur basis" does not appear in the patches on this ticket.

I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.


---

Comment by aschilling created at 2012-09-08 05:02:56

Replying to [comment:48 saliola]:
> 
> I double-checked, and the phrase "in the Schur basis" does not appear in the patches on this ticket.
> 
> I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.

Franco is right. I will fix this in 13404 and put a dependency on 8899 there.

Best,

Anne


---

Comment by jdemeyer created at 2012-09-08 08:59:04

Replying to [comment:48 saliola]:
> 
> I double-checked, and the phrase "in the Schur basis" does not appear in the patches on this ticket.
> 
> I know that #13404 claims not to have been merged yet, but did you happen to merge it in sage-5.4.beta1? I think that ticket would have caused this change in the `_repr_`.
I always test a bunch of tickets together, and in this case I included indeed #13404.  So I will remove #13404 for now.


---

Comment by jdemeyer created at 2012-09-08 08:59:04

Resolution: fixed


---

Comment by jdemeyer created at 2012-09-24 07:11:35

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

Comment by nthiery created at 2012-09-24 09:17:40

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

Comment by jdemeyer created at 2012-09-24 10:07:00

This is a better example from this patch on how _not_ to use assert:

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

Comment by nthiery created at 2012-10-02 13:31:00

Changing keywords from "sd40" to "sd40, days38".
