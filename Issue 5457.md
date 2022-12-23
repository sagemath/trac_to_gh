# Issue 5457: Refactor symmetric functions

Issue created by migration from https://trac.sagemath.org/ticket/5457

Original creator: nthiery

Original creation time: 2009-03-08 20:53:00

Assignee: mhansen

CC:  sage-combinat saliola bump chrisjamesberg zabrocki simonking

Refactor symmetric functions to:
 - use a single entry point, as in MuPAD-Combinat. Something like:
        S = SymmetricFunctions(field)
        S.schur
        S.jack(t).P
        S.macdonald(t,q).Q
        S.kSchur(3).H
 - use the coercion framework
 - use the category framework

See also:http://groups.google.com/group/sage-devel/msg/a49f3288fca1b75c


---

Comment by aschilling created at 2012-07-15 04:38:50

Changing keywords from "" to "symmetric functions, sd38, sd40".


---

Comment by aschilling created at 2012-07-15 04:55:57

Changing status from new to needs_review.


---

Comment by aschilling created at 2012-07-15 04:56:08

Changing status from needs_review to needs_work.


---

Comment by aschilling created at 2012-07-15 04:59:53

Hi Mike,

I finished the doctests for the following files:

- schur.py

- homogeneous.py

- elementrary.py

- powersum.py

- monomial.py

- classical.py

- dual.py

- multiplicative.py

- orthotriang.py

- sf.py

In particular, at the beginning of sf.py I incorporated the tutorial that Jason and Nicolas
wrote (which was further down the queue) and updated it. I marked them there as coauthors in
that file.

This leaves the doctests for 

- hall_littlewood.py

- jack.py

- llt.py

- macdonald.py

- ns_macdonald.py

- sfa.py

which I suppose you will do in the next couple of days?
In particular, in the sfa.py the deprecation warnings need to be activated which I have
not yet done.

Best,

Anne


---

Comment by aschilling created at 2012-07-17 06:34:38

Hi Mike,

I completed the doctests for sfa.py and also rebased everything on top of 13109. Please put your changes to 

    * hall_littlewood.py 

    * jack.py 

    * llt.py 

    * macdonald.py 

on top of the current patch trac_5457-symmetric_functions-mz.patch. Unfortunately we need to abandon the sage-combinat queue for the moment since it would be very cumbersome to keep it backward compatible with 13109. I will send you a separate e-mail on how to proceed.

Cheers,

Anne


---

Comment by aschilling created at 2012-07-19 06:52:29

Ok, patch is ready for review! It should apply and run cleanly on sage.5.2.rc0!

Anne


---

Comment by aschilling created at 2012-07-19 06:52:52

Changing status from needs_work to needs_review.


---

Comment by aschilling created at 2012-07-19 07:45:15

Apply [attachment:trac_5457-symmetric_functions-mz.patch]


---

Comment by aschilling created at 2012-07-24 22:35:23

Hi Dan!

Thank you very much for your comments on the failing doctests in 

* devel/sage/sage/algebras/nil_coxeter_algebra.py

* devel/sage/sage/categories/realizations.py

They are fixed in the updated version of the patch. I do not get failures for 

* devel/sage/sage/sandpiles/sandpile.py

on my machine.

lolita-4:sandpiles anne$ sage -t sandpile.py 
sage -t  "devel/sage-sf/sage/sandpiles/sandpile.py"         
	 [19.0 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 19.0 seconds


Anne


---

Comment by bump created at 2012-07-24 23:48:52

Replying to [comment:20 aschilling]:
> Hi Dan!
> 
> Thank you very much for your comments on the failing doctests in 
> 
> * devel/sage/sage/algebras/nil_coxeter_algebra.py
> 
> * devel/sage/sage/categories/realizations.py
> 
> They are fixed in the updated version of the patch. I do not get failures for 
> 
> * devel/sage/sage/sandpiles/sandpile.py
> 
> on my machine.

I also get a doctest failure in sandpile.py with unpatched sage-5.2.rc0 so this failure is not caused by the patch.


---

Comment by bump created at 2012-07-30 18:31:23

Applies cleanly to sage-5.2 and passes all tests.


---

Comment by aschilling created at 2012-07-30 21:28:46

The attached review patch trac_5457-review-as.patch incorporates most of the comments that Dan Bump raised in e-mail conversations.

Anne


---

Comment by bump created at 2012-07-30 21:46:28

Changing status from needs_review to positive_review.


---

Comment by bump created at 2012-07-30 21:46:28

This patch is a huge step forward for symmetric functions.

In addition to normal testing I spent quite a bit of time and privately sent comments (mainly on documentation) that have been taken into account in trac_5457-review-as.patch. I'm changing the status to positive review.


---

Comment by aschilling created at 2012-07-31 01:37:26

Replying to [comment:25 bump]:
> This patch is a huge step forward for symmetric functions.
> 
> In addition to normal testing I spent quite a bit of time and privately sent comments (mainly on documentation) that have been taken into account in trac_5457-review-as.patch. I'm changing the status to positive review.

Dear Dan, Thank you so much for your thorough and quick review of this huge patch! Mike and I just finished the review patch. Tests pass on both of our machines.

Anne


---

Comment by bump created at 2012-07-31 02:20:25

I have reviewed the latest version of the patch and it still has positive review.


---

Comment by aschilling created at 2012-08-01 12:31:43

Since http://trac.sagemath.org/sage_trac/ticket/12969 just got merged into sage-5.3.beta0, please also apply the attachment trac12969_rel_5457.patch on the ticket 12969 to this patch. Otherwise there will be doctest failures.

Thanks,

Anne


---

Comment by jdemeyer created at 2012-08-01 18:14:26

This needs to be rebased to sage-5.3.beta0 (not yet released):

```
patching file sage/categories/realizations.py
Hunk #1 FAILED at 74
1 out of 1 hunks FAILED -- saving rejects to file sage/categories/realizations.py.rej
patching file sage/combinat/sf/classical.py
Hunk #3 FAILED at 88
1 out of 9 hunks FAILED -- saving rejects to file sage/combinat/sf/classical.py.rej
patching file sage/combinat/sf/sfa.py
Hunk #61 FAILED at 2589
1 out of 63 hunks FAILED -- saving rejects to file sage/combinat/sf/sfa.py.rej
abort: patch failed to apply
```



---

Comment by jdemeyer created at 2012-08-01 18:15:04

Changing status from positive_review to needs_work.


---

Comment by aschilling created at 2012-08-02 23:18:00

I rebased and folded the three patches with respect to sage-5.3.beta0 from yesterday.
It should apply cleanly now.

Mike and I are still going to fix one math bug that someone at FPSAC found.

Anne


---

Comment by aschilling created at 2012-08-03 06:51:51

Hi Dan,

Our new rebased patch is attached. You only need to apply trac_5457-symmetric_functions-mz.patch. Note that we did not fix apply_linear_morphism in /category/module_with_basis.py yet since Nicolas seems to have a review patch for this, but unfortunately his tests did not pass. Either he needs to fix his review patch or we will add your suggestion from the e-mail.

Anne


---

Comment by aschilling created at 2012-08-03 06:52:08

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2012-08-03 17:28:24

Note: I inserted in the queue the latest patch rebased for 5.3 beta0 from here. My review patch is also there, ready to be folded if you are happy with it.


---

Comment by aschilling created at 2012-08-04 00:10:31

Dear Dan and Nicolas,

Thank you so much for your reviews and work on this patch! I incorporated the changes that Dan suggested by e-mail and folded Nicolas' review patch. In addition, Mike had some minor improvements in the documentation of llt.py which are incorporated.

The new patch should apply cleanly on sage-5.3.beta0.

Anne


---

Comment by bump created at 2012-08-04 13:20:49

All tests pass with sage-5.3.beta0. The changes discussed over the last few days have all been incorporated. I think this is ready to go.


---

Comment by bump created at 2012-08-04 13:21:21

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-08-08 12:30:10

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-08-08 12:30:10

This fails on arando (32-bit i386 Linux):

```
sage -t --long "devel/sage/sage/combinat/sf/llt.py"
**********************************************************************
File "/var/lib/buildbot/build/sage/arando-1/arando_full/build/sage-5.3.beta1/devel/sage/sage/combinat/sf/llt.py", line 329:
    sage: cmp(L3Q, L3Z)
Expected:
    -1
Got:
    1
**********************************************************************
```



---

Comment by aschilling created at 2012-08-08 20:25:49

Changing status from needs_work to needs_review.


---

Comment by aschilling created at 2012-08-08 20:27:27

Hi Jeroen,

Hmm, this is hard for us to check since we are not running our code on that operating system. We attached a patch which will hopefully fix the problem

Apply

 * [attachment:trac_5457-symmetric_functions-mz.patch]
 * [attachment:trac_5457_docfix-mz.patch]

Thanks,

Anne


---

Comment by aschilling created at 2012-08-08 20:27:41

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-08-09 06:27:12

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-08-09 06:27:39

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2012-08-09 06:27:39

I think one of the original reviewers should review this additional patch.


---

Comment by bump created at 2012-08-09 16:47:04

Changing status from needs_review to positive_review.


---

Comment by bump created at 2012-08-09 16:47:04

> I think one of the original reviewers should review this additional patch.

This adds a __cmp__ method for SymmetricFunctions, which was missing, and that
was uncovered by the test in llt.py. Two SymmetricFunctions instances are
compared equal if and only if they have the same base ring, which is as it
should be.

Unless I'm missing something the patch is obviously correct. I ran --testall --long
in the sf directory and all tests passed.


---

Comment by nthiery created at 2012-08-09 18:11:17

There is no compelling reason to have a cmp function for symmetric functions (nor its bases). The order has no meaning, and equality testing should be taken care of by UniqueRepresentation.

So altogether, I'd rather not add a cmp function, and instead would rather replace the failing test by:

    sage: cmp(L3Q, L3Z) != 0

which is platform independent, and is all we care about. We could even just discard this test.

Now, I don't want to slow down the integration of this patch, so I am happy leaving this issue for a latter ticket, at the author's choice.

Cheers,
                   Nicolas


---

Comment by zabrocki created at 2012-08-10 20:39:06

As per Nicolas' suggestion, we are deleting the __cmp__ function from llt and moving and modifying the doctests elsewhere in the llt.py file.


---

Comment by zabrocki created at 2012-08-10 20:39:06

Changing status from positive_review to needs_work.


---

Comment by zabrocki created at 2012-08-10 20:52:47

This new patch deletes the function cmp from llt.py and inserts doctests into init in llt.py


---

Comment by zabrocki created at 2012-08-10 20:52:47

Changing status from needs_work to needs_review.


---

Comment by aschilling created at 2012-08-10 22:00:20

sage -testall passes on both mine and Mike's machine (both MacOS) with trac_5457-symmetric_functions-mz.patch and trac_5457_docfix2-mz.patch applied.

Dan and/or Nicolas, please set a positive review if you are happy with the changes.

Thanks!

Anne


---

Comment by bump created at 2012-08-11 00:05:31

Nicolas argued that there is no real reason for Sym to have a `__cmp__`
method and there is no reason for the test to be deterministic. We don't
care if two rings or ring elements are > or < than each other, just whether they are distinct.
Therefore the test that failed can be rewritten and the `__cmp___` method
is not needed.

This patch removes the `__cmp__` method from llt polynomials instead
of adding one for sf. In fact, `SymmetricFunctions` should not have had a
`__cmp__` method because it already inherits one from `UniqueRepresentation`.
(Tested!) On the other hand, there is no reason for the test as previously written
to be deterministic. So this is the correct approach.


---

Comment by bump created at 2012-08-11 00:05:31

Changing status from needs_review to positive_review.


---

Comment by bump created at 2012-08-11 00:12:11

Changing status from positive_review to needs_work.


---

Comment by bump created at 2012-08-11 12:40:22

Changing status from needs_work to positive_review.


---

Comment by aschilling created at 2012-08-11 15:17:59

Thank you Dan for the review!

Anne


---

Comment by aschilling created at 2012-08-12 22:44:24

Folded patches.


---

Comment by jdemeyer created at 2012-08-14 07:01:34

Resolution: fixed


---

Comment by aschilling created at 2012-08-14 14:19:33

Replying to [comment:60 jdemeyer]:

Wow, unbelievable!! Thank you everyone for your work on this!

Anne


---

Comment by nthiery created at 2012-08-19 18:35:59

Replying to [comment:61 aschilling]:
> Wow, unbelievable!! Thank you everyone for your work on this!

Congratulations!

And thanks on behalf of all symmetric function users!

                                 Nicolas


---

Comment by nthiery created at 2012-08-23 15:41:15

Changing keywords from "symmetric functions, sd38, sd40" to "symmetric functions, days38, sd40".


---

Comment by jdemeyer created at 2012-08-31 21:41:12

*Additional patch* [attachment:5457_long_time.patch] needs review.


---

Comment by jdemeyer created at 2012-09-01 09:13:54

Additional patch is a blocker, please review.


---

Comment by jdemeyer created at 2012-09-01 09:13:54

Changing priority from major to blocker.


---

Comment by zabrocki created at 2012-09-01 11:49:09

the patch looks good and works properly.  I tested it on sage-5.3.rc0 using both --long and not --long and all tests pass.  I give it a positive review.


---

Comment by jdemeyer created at 2012-09-01 13:01:43

Changing priority from blocker to major.


---

Comment by jdemeyer created at 2012-09-01 13:01:43

Resolution changed from fixed to 


---

Comment by jdemeyer created at 2012-09-01 13:01:43

Changing status from closed to new.


---

Comment by jdemeyer created at 2012-09-01 13:01:43

I hate to be the bringer of bad news, but after playing a bit with this patch, I think I found an actual bug:

```
sage: HS3t2 = SymmetricFunctions(QQ).llt(3,t=2).hspin()
sage: TestSuite(HS3t2).run()
Failure in _test_associativity:
Traceback (most recent call last):
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 275, in run
    test_method(tester = tester)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/semigroups.py", line 120, in _test_associativity
    tester.assert_((x * y) * z == x * (y * z))
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/algebras.py", line 202, in __mul__
    return self._mul_(right)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/magmas.py", line 361, in _mul_parent
    return self.parent().product(self, other)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/categories/algebras_with_basis.py", line 351, in _product_from_combinatorial_algebra_multiply
    m = self._multiply(left, right)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/llt.py", line 683, in _multiply
    return self( self._m(left) * self._m(right) )
  File "parent.pyx", line 804, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7228)
  File "morphism.pyx", line 243, in sage.categories.morphism.SetMorphism._call_ (sage/categories/morphism.c:4412)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/llt.py", line 617, in _self_to_m
    return self._m._from_cache(x, self._m_cache, self._self_to_m_cache, t = self.t)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/sfa.py", line 857, in _from_cache
    cache_function(sum(part))
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/llt.py", line 714, in _m_cache
    self._m_to_self_cache, to_other_function = self._to_m)
  File "/release/sage-5.3.rc1/local/lib/python2.7/site-packages/sage/combinat/sf/sfa.py", line 1057, in _invert_morphism
    known_matrix_n[i,j] = value
  File "matrix0.pyx", line 1415, in sage.matrix.matrix0.Matrix.__setitem__ (sage/matrix/matrix0.c:6745)
  File "matrix0.pyx", line 1520, in sage.matrix.matrix0.Matrix._coerce_element (sage/matrix/matrix0.c:7937)
  File "parent.pyx", line 804, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7228)
  File "coerce_maps.pyx", line 82, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3547)
  File "coerce_maps.pyx", line 77, in sage.structure.coerce_maps.DefaultConvertMap_unique._call_ (sage/structure/coerce_maps.c:3449)
  File "rational.pyx", line 371, in sage.rings.rational.Rational.__init__ (sage/rings/rational.c:6534)
  File "rational.pyx", line 484, in sage.rings.rational.Rational.__set_value (sage/rings/rational.c:7337)
  File "fraction_field_element.pyx", line 736, in sage.rings.fraction_field_element.FractionFieldElement._rational_ (sage/rings/fraction_field_element.c:7197)
  File "parent.pyx", line 804, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:7228)
  File "polynomial_element.pyx", line 6521, in sage.rings.polynomial.polynomial_element.ConstantPolynomialSection._call_ (sage/rings/polynomial/polynomial_element.c:46753)
TypeError: not a constant polynomial
------------------------------------------------------------
Failure in _test_distributivity:
[...]
TypeError: not a constant polynomial
------------------------------------------------------------
Failure in _test_one:
[...]
TypeError: not a constant polynomial
------------------------------------------------------------
Failure in _test_prod:
[...]
TypeError: not a constant polynomial
------------------------------------------------------------
The following tests failed: _test_associativity, _test_distributivity, _test_one, _test_prod
```



---

Comment by jdemeyer created at 2012-09-01 13:01:50

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2012-09-01 13:01:56

Changing status from needs_review to needs_work.


---

Comment by zabrocki created at 2012-09-01 15:37:44

Just an FYI, this does not seem to be a new bug introduced by this patch.  Doc tests currently do not seem to test extensively enough to catch this (but once I knew the bug existed I was able to trigger it in all kinds of ways).  I think that I've tracked down the problem.  Here is a one line fix (class LLT_generic, method _m_cache):

`-        self._invert_morphism(n, self.base_ring(), self._self_to_m_cache, \`

`+        self._invert_morphism(n, QQt, self._self_to_m_cache, \`

I will post a patch later today when I am confident that this actually fixes the problem and that there aren't similar bugs in jack/hall_littlewood/macdonald.


---

Comment by zabrocki created at 2012-09-01 17:25:56

I also found that the tests that are currently in llt.py will fail if they are run separately.


```
sage: HSp3 = SymmetricFunctions(FractionField(QQ['t'])).llt(3).hspin()
sage: TestSuite(HSp3).run(skip = ["_test_associativity", "_test_distributivity", "_test_prod"])
sage: HS3t2 = SymmetricFunctions(QQ).llt(3,t=2).hspin()
sage: TestSuite(HS3t2).run(skip = ["_test_associativity", "_test_distributivity", "_test_prod"])
```


Executes without errors (even without the 'skip's).  However, if you delete the first two lines then these tests fail.  I will fix this by putting these tests in their own block.


---

Comment by zabrocki created at 2012-09-01 18:21:16

The new attachment fixes the bug and makes the document changes that will test for the bug.  I removed the `skip` commands from two of the `TestSuite` commands since they weren't particularly long executions before, but they should have been the very tests which caught this bug.


---

Comment by zabrocki created at 2012-09-01 18:21:16

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2012-09-01 18:52:49

Replying to [comment:70 zabrocki]:
> Just an FYI, this does not seem to be a new bug introduced by this patch.
What do you mean?  The doctest is testing code which did not exist before.  So I would say the bug was introduced by this patch.


---

Attachment

Additional patch


---

Attachment

I rebased the three patches (there was some fuzz) and made some additional changes to [attachment:5457_long_time.patch] (so that patch needs review again).


---

Comment by aschilling created at 2012-09-01 20:14:21

Replying to [comment:73 jdemeyer]:
> Replying to [comment:70 zabrocki]:
> > Just an FYI, this does not seem to be a new bug introduced by this patch.
> What do you mean?  The doctest is testing code which did not exist before.  So I would say the bug was introduced by this patch.

The failures are related to failures that already existed before this patch.
On sage 5.0.1 (plain) one obtains

```
sage: LLTHSpin(QQ,3,t=2)
LLT polynomials in the HSp basis at level 3 with t=2 over Rational Field
sage: H = LLTHSpin(QQ,3,t=2)
sage: s = SFASchur(QQ)
sage: s(H([2,1]))
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1760, 0))
```


Anne


---

Comment by aschilling created at 2012-09-02 03:17:15

I reviewed and tested both patches (by applying 5457_long_time.patch and then trac_5457_llt_doc_and_bug_fix-mz.patch in this order). Tests pass and the bug seems to be fix (if I only apply  5457_long_time.patch tests do not pass, so the patches should be applied together).

Jeroen, I have a question. trac_5457-symmetric_functions-mz.patch was already merged into sage-5.2.beta2. Why did you rebase that patch again? Will it be merged again in a different version of sage? I am asking since in the sage-combinat queue it is currently guarded by sage-5.3.beta2.

Thanks,

Anne


---

Comment by aschilling created at 2012-09-02 03:17:29

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-09-02 21:39:40

Replying to [comment:76 aschilling]:
> Will it be merged again in a different version of sage?
Yes, I don't want to merge any more new patches in sage-5.3 so it will be removed from sage-5.3 and then merged again in sage-5.4 such that it can be tested better.  Does this cause trouble?


---

Comment by aschilling created at 2012-09-03 00:55:21

Replying to [comment:78 jdemeyer]:
> Replying to [comment:76 aschilling]:
> > Will it be merged again in a different version of sage?
> Yes, I don't want to merge any more new patches in sage-5.3 so it will be removed from sage-5.3 and then merged again in sage-5.4 such that it can be tested better.  Does this cause trouble?

Mike's patch fixes a bug that is actually in the current version of Sage (as I outlined above). Wouldn't it be better to merge the two extra patches into sage-5.3 instead? Quite a lot of other patches depend on this patch (plus an upcoming book).

Thanks,

Anne


---

Comment by jdemeyer created at 2012-09-03 06:47:37

Replying to [comment:79 aschilling]:
> Mike's patch fixes a bug that is actually in the current version of Sage (as I outlined above). Wouldn't it be better to merge the two extra patches into sage-5.3 instead? Quite a lot of other patches depend on this patch (plus an upcoming book).
I believe everything you say in this paragraph, but I see no arguments to merge it in sage-5.3.

You have to convince me that this patch will absolutely not break anything on any system, nor cause doctest timeouts.


---

Comment by nthiery created at 2012-09-03 11:09:19

Ah shoot, my comment did not get through yesterday; well, it's a bit outaded, but here it is anyway ...

Replying to [comment:78 jdemeyer]:
> Replying to [comment:76 aschilling]:
> > Will it be merged again in a different version of sage?
> Yes, I don't want to merge any more new patches in sage-5.3 so it will be removed from sage-5.3 and then merged again in sage-5.4 such that it can be tested better.  Does this cause trouble?

Technically, the Sage-Combinat queue can't handle patches that are merged and then unmerged. Now, this just means that we will have to everyone using a 5.3 beta to switch to 5.3 final; not a big deal.

Anne, Mike: are there specific deadlines (e.g. the book or meetings) for which waiting for 5.4 could be a bother?

Other than that, it's quite a big patch, on a very central feature for people in algebraic combinatorics; and the authors (Mike and Anne mostly) did put quite a lot of work and energy into it. So it will be quite frustrating for theim to not be able to cross it out of their TODO list while the semester starts. But that's life ...

Cheers,
                              Nicolas


---

Comment by jdemeyer created at 2012-09-03 11:26:36

Replying to [comment:81 nthiery]:
> So it will be quite frustrating for theim to not be able to cross it out of their TODO list while the semester starts.
But if the patch has _positive review_, then it is effectively off the TODO list, right?  Personally, I don't think it makes a big difference for a patch Author whether a patch gets merged in sage-5.3 or sage-5.4.


---

Comment by zabrocki created at 2012-09-03 11:41:16

My only worry is that several patches with positive reviews (#8899, #13399, #13404) were all reviewed on versions of sage where #5457 was already integrated.  Until last night #8899 and #13399 didn't have #5457 as a dependency (but should have) and #13404 depends on #13399.  I hope that there aren't other patches that are not similarly needed to be pushed forward that I am unaware of.


---

Comment by jdemeyer created at 2012-09-03 11:50:55

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-09-03 11:50:55

A small detail: the last patch needs a proper commit message.


---

Comment by zabrocki created at 2012-09-03 12:35:22

I'm not sure what you want in the commit message and I don't have permission to replace the previous version.  If you are satisfied with that change then please adjust the "apply" list so that the second version is the one that is used.


---

Comment by jdemeyer created at 2012-09-03 12:44:30

Replying to [comment:85 zabrocki]:
> I'm not sure what you want in the commit message
Well, I don't want anything refering to `[mq]` or the patch name.  So if you delete the second line of the commit message in your patch, that will be fine.


---

Comment by zabrocki created at 2012-09-03 12:53:13

same patch with commit message


---

Attachment

I think that does it.  Sorry I don't know what the [mq] is or how it got there.


---

Comment by jdemeyer created at 2012-09-03 13:15:55

Changing status from needs_work to positive_review.


---

Comment by saliola created at 2012-09-03 13:21:28

Replying to [comment:87 zabrocki]:
> Sorry I don't know what the [mq] is or how it got there.

The [mq] is short for mercurial queue; it is automatically placed there by hg.


---

Comment by aschilling created at 2012-09-03 14:14:31

Hi Nicolas,

> Technically, the Sage-Combinat queue can't handle patches that are merged and then unmerged. Now, this just means that we will have to everyone using a 5.3 beta to switch to 5.3 final; not a big deal.

I have no idea how to handle the sage-combinat queue now. Do nothing until sage-5.3 comes out and then force everyone to move to sage-5.3?

> Anne, Mike: are there specific deadlines (e.g. the book or meetings) for which waiting for 5.4 could be a bother?

Beginning for the quarter for the book since my students are supposed to use it and sage!

Cheers,

Anne


---

Comment by aschilling created at 2012-09-03 14:30:15

As far as I know this patch does not commute with #9265 which was just merged into sage. I hope Jeroen will rebase #5457 since I won't have time to do so!!!

Anne


---

Comment by chapoton created at 2012-09-03 18:46:31

Apply trac_5457-symmetric_functions-mz.patch, 5457_long_time.patch, trac_5457_llt_doc_and_bug_fix-mz.2.patch


---

Comment by jdemeyer created at 2012-09-04 08:39:49

Resolution: fixed


---

Comment by jdemeyer created at 2012-09-21 09:21:07

Second additional patch


---

Attachment

My second additional patch [attachment:5457_long_time_2.patch] needs review (just mention the review in the comments, don't change the status).


---

Comment by nthiery created at 2012-09-21 09:32:37

Replying to [comment:95 jdemeyer]:
> My second additional patch [attachment:5457_long_time_2.patch] needs review (just mention the review in the comments, don't change the status).

Positive review! Thanks!


---

Comment by jdemeyer created at 2012-09-24 07:12:59

This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.

For example:

```
            sage: f.skew_by([1])
            Traceback (most recent call last):
            ...
            AssertionError: x needs to be a symmetric function
```

This is a simple user mistake, for which `assert` is not right.

I think this must be fixed.


---

Comment by nthiery created at 2012-09-24 09:16:19

Hi Jeroen,

Replying to [comment:97 jdemeyer]:
> This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.
> 
> For example:
> {{{
>             sage: f.skew_by([1])
>             Traceback (most recent call last):
>             ...
>             AssertionError: x needs to be a symmetric function
> }}}
> This is a simple user mistake, for which `assert` is not right.
> 
> I think this must be fixed

Given the discussion on sage-devel, do we agree that there is no control flow involved and it's a not so common function, so it's ok to use assert?

Cheers,
                    Nicolas


---

Comment by aschilling created at 2012-09-24 14:30:56

Replying to [comment:97 jdemeyer]:
> This patch abuses `assert` and `AssertionError`. `assert` should not be used for control flow. An `assert` checks something which should always be true, a failed assertion is always a bug in the program.
> 
> For example:
> {{{
>             sage: f.skew_by([1])
>             Traceback (most recent call last):
>             ...
>             AssertionError: x needs to be a symmetric function
> }}}
> This is a simple user mistake, for which `assert` is not right.
> 
> I think this must be fixed.

We had a user who used this method wrongly at FPSAC (he used a partition instead of a symmetric function). That's why we added this (since this can potentially be a common user mistake). If this should be done differently, feel free to change it!

Anne


---

Comment by jdemeyer created at 2012-09-24 18:35:57

Replying to [comment:99 aschilling]:
> That's why we added this (since this can potentially be a common user mistake). If this should be done differently, feel free to change it!
Yes, it should be done differently.  The correct way would be:

```
if not needed_condition:
    raise ValueError("Error message")
```


As I said: `assert` is only meant to catch _bugs_, not user errors.  Although, as Nicolas Thiéry argued, something `assert` is acceptible.  See also the sage-devel thread.


---

Attachment


---

Comment by aschilling created at 2012-09-25 00:45:06

I folded the patches and made the required change.

Apply: trac_5457-symmetric_functions-mz.2.patch

Anne


---

Comment by nthiery created at 2012-09-26 14:24:51

Hi Jeroen,

I am confused: was your intention to request that this change be made for this ticket?

(meaning that you'd have to unmerge / remerge it)


---

Comment by jdemeyer created at 2012-09-26 14:45:53

Short story: for me it was far more important *that* the problem got
fixed, not *how* it got fixed.

A situation where a ticket is merged but then problems are discovered is
a difficult situation to handle.  In the past, I would have re-opened
the ticket and set it to needs_work but that seems to upset people (they
think it will postpone the merging of their patch).  So this time, I
decided not to reopen the ticket but my intention was indeed for the
chances to be made on the same ticket.  However, ideally it would have
been done in a separate additional patch, leaving the original
already-merged patch alone.  But I certainly would have been happy also
with a new ticket.

I have no idea how any of this affect sage-combinat.


Jeroen.
