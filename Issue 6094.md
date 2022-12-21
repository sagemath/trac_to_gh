# Issue 6094: Change all occurrences of "method" to "algorithm"

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-05-20 18:28:10

Assignee: rlm

CC:  wdj

In a discussion with David, we realized that he's been using "method" for "algorithm" in several places. This fix will follow up on #5701, and will probably depend on the patches there.


---

Comment by jason created at 2009-05-20 22:06:28

"method" is not only easier to say, but it's easier to spell, and probably is more memorable to people...


---

Comment by rlm created at 2009-05-21 14:23:09

Replying to [comment:1 jason]:
> "method" is not only easier to say, but it's easier to spell, and probably is more memorable to people...

It is also *not* the standard arg name. If you think method is better, take it to the mailing list.


---

Comment by jason created at 2009-05-21 19:00:40

okay, I didn't realize there was a standard.  The weight of history changes the situation a bit.


---

Comment by rlm created at 2009-05-22 04:39:43

Replying to [comment:3 jason]:
> okay, I didn't realize there was a standard...

Actually, neither did I. But when David and I did a search for "method=", most of what we found were places where he was using that name.

In fact, here is a complete (I think) list of the functions which use this (4.0.alpha0):


```
calculus/desolvers.py: eulers_method, eulers_method_2x2
coding/decoder.py: decode
coding/linear_code.py: decode, is_permutation_equivalent, permutation_automorphism_group, spectrum
finance/easter.py: easter
combinat/designs/block_design.py: ProjectiveGeometryDesign
combinat/designs/covering_design.py: __init__, method
combinat/designs/incidence_structures.py: dual_incidence_structure
groups/matrix_gps/matrix_group.py: as_permutation_group, module_composition_factors
schemes/elliptic_curves/padic_lseries.py: frobenius
matrix/matrix_double_dense.pyx: exp
matrix/matrix_modn_sparse.pyx: _rank_linbox
rings/polynomial/polynomial_compiled.pyx: __init__
```



---

Comment by wdj created at 2009-05-25 15:34:42

Thanks. I'll get to these when #5701 is applied unless someone says I should just create a patch based on the patches there.


---

Comment by wdj created at 2009-05-27 10:15:22

based on 4.0.rc0 and all patches in #5701


---

Attachment

The current patch passes sage -testall with guava removed and all patched on #5701 applied.


---

Comment by jhpalmieri created at 2009-06-09 03:42:32

Fails to apply cleanly to Sage 4.0.1.

```
applying /home/palmieri/trac_6094-method-vs-algorithm.patch
patching file sage/coding/linear_code.py
Hunk #1 FAILED at 315
Hunk #2 FAILED at 341
Hunk #3 FAILED at 351
Hunk #5 FAILED at 1144
Hunk #6 FAILED at 1165
Hunk #11 FAILED at 1636
Hunk #12 FAILED at 1651
Hunk #13 FAILED at 1668
Hunk #15 FAILED at 1758
Hunk #22 FAILED at 2179
10 out of 23 hunks FAILED -- saving rejects to file sage/coding/linear_code.py.rej
patching file sage/combinat/designs/block_design.py
Hunk #2 FAILED at 89
1 out of 3 hunks FAILED -- saving rejects to file sage/combinat/designs/block_design.py.rej
abort: patch failed to apply
```



---

Comment by wdj created at 2009-09-15 21:06:19

I don't know how to rebase. Can someone point me to a reference? I might be able to do it this weekend.


---

Attachment

I rebased this against 4.3.1.rc0.


---

Comment by was created at 2010-01-18 04:38:12

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-01-18 05:14:17

Passes all tests.  There are more instances of the use of `method=` in coding/code_bounds.py which will have a patch at #7971.  Positive review.


---

Comment by rbeezer created at 2010-01-18 05:14:17

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-01-18 09:16:36

It was pointed out by people in our status reports session that this patch violates our deprecation policy.  Yuck.  I.e., technically we should do

```
def f(algorithm='default', method=None):
    if method is not None:
        deprecation('...')
        algorithm = method
```

basically *everywhere*, then remove them all in a year.  Hmmmm....


---

Comment by rbeezer created at 2010-01-18 21:19:10

Changing status from positive_review to needs_work.


---

Comment by rbeezer created at 2010-01-18 21:19:10

I've sent this back to "needs work" to await deprecation warnings.  With more to do, include the changes in ccoding/code_bounds.py here as part of this ticket (see #7971).


---

Comment by was created at 2010-01-18 21:56:50

I wonder if it could be done with a decorator?

```
`@`deprecate_method
def f(..., method="foo"):
    ...

```



---

Comment by jason created at 2010-05-11 18:37:21

Replying to [comment:15 was]:
> I wonder if it could be done with a decorator?

Yep.  See the already-merged #8607.


---

Attachment

Rebased for 4.5.1. Change to more files and at more places as well as documentation. Added deprecation warnings.


---

Comment by jsrn created at 2010-09-15 13:27:27

I wrote a new patch which uses the decorator mentioned above. *This patch assumes applying the patch for Trac #9907!*

I basically rewrote the patch, so it works for Sage 4.5.3 (accidentally wrote 4.5.1 in the patch message).

I also did a grep on all Sage source which uncovered more places where method should be replaced with algorithm (I assume). I also changed the doc-texts to refer to "algorithms" instead of "methods" for the relevant functions changed.

Hope I can get a fast review on this; I plan to do major relocations to the coding theory library soon, and this trac touches a lot of code in a lot of places :-)

Cheers,
Johan


---

Comment by jsrn created at 2010-09-15 13:27:27

Changing status from needs_work to needs_review.


---

Attachment

Rebased, renamed, commit message edited


---

Comment by rbeezer created at 2010-09-16 04:57:24

With #9907 applied, this applied to a 4.5.3 version with one failure (docstring change in `sage/schemes/elliptic_curves/padic_lseries.py, frobenius()`, which I fixed.  Also changed references to 4.5.1 to 4.5.3.  Finally, the filename needs a `.patch` extension to display nicely in the web page view.  All in a new attachment, preserving original author's ID.

With rebase, builds just fine.  Works as expected in trials with `as_permutation_group()` in `sage/matrix_gps/matrix_group.py`.  Running full tests right now.

Minor complaint about how the decorator works, I'll put this on #9907.  More here once tests finish.


---

Comment by rbeezer created at 2010-09-16 05:05:21

Decorator complaint is bigger than these tickets.  Its on sage-devel.

sage -tp 4 devel/sage yields:


```
        sage -t  devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 1 doctests failed
        sage -t  devel/sage/sage/misc/sagedoc.py # 3 doctests failed
        sage -t  devel/sage/sage/structure/sage_object.pyx # 1 doctests failed
```


which are all reproducible on my machine.

First is an easy fix, extra deprecation warning in a doctest elsewhere when using `frobenius()`.

Second is just me.  I nuked all my documentation while testing the new color scheme.  Ignore it.

Third looks like something is pickling the two decorators and once they get moved the pickle breaks, so maybe this really belongs on #9907?  Complaint follows.  Parts look mysterious to me, other parts look like they involve these decorators.  It could be a false alarm from my development setup.


```
rob`@`wave:/sage/dev$ ./sage -t  devel/sage/sage/structure/sage_object.pyx
sage -t  "devel/sage/sage/structure/sage_object.pyx"        
**********************************************************************
File "/sage/dev/devel/sage/sage/structure/sage_object.pyx", line 1001:
    sage: print "x"; sage.structure.sage_object.unpickle_all(std)
Expected:
    x...
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    x
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead
    ** failed:  _class__sage_plot_misc_options__.sobj
    ** failed:  _class__sage_plot_misc_rename_keyword__.sobj
    Failed:
    _class__sage_plot_misc_options__.sobj
    _class__sage_plot_misc_rename_keyword__.sobj
    Successfully unpickled 584 objects.
    Failed to unpickle 2 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_23
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/rob/.sage//tmp/.doctest_sage_object.py
         [5.2 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/structure/sage_object.pyx"

```



---

Comment by rbeezer created at 2010-09-16 05:05:21

Changing status from needs_review to needs_work.


---

Comment by jsrn created at 2010-09-16 06:40:03

Hi Rob
Great, thanks for looking into this. Sorry about the rudimentary stuff on the patch; I'm still learning the ropes.

sage_object.pyx also fails on my machine -- don't know how I missed that when testing. I'll look into that and your sage-devel thread.

Cheers, Johan


---

Comment by rbeezer created at 2010-09-16 07:08:05

Replying to [comment:20 jsrn]:
> Great, thanks for looking into this. Sorry about the rudimentary stuff on the patch; I'm still learning the ropes.

No problem.  Just holler if you want to learn some new ropes.

> sage_object.pyx also fails on my machine -- don't know how I missed that when testing. I'll look into that and your sage-devel thread.

If you see how to contribute to the sage-devel thread, that would be great.  But don't let it delay this.

Pickling is a rat's nest.  #9907 is well-intentioned, but not strictly necessary.  You may not want this to depend on it?  In other words, can you proceed without the move and the fix for classes?  You really just want to ultimately do coding theory, right?

Rob


---

Comment by jsrn created at 2010-09-16 14:25:01

Replying to [comment:21 rbeezer]:
> Replying to [comment:20 jsrn]:
> > Great, thanks for looking into this. Sorry about the rudimentary stuff on the patch; I'm still learning the ropes.
> 
> No problem.  Just holler if you want to learn some new ropes.
> 
> > sage_object.pyx also fails on my machine -- don't know how I missed that when testing. I'll look into that and your sage-devel thread.
> 
> If you see how to contribute to the sage-devel thread, that would be great.  But don't let it delay this.
> 
> Pickling is a rat's nest.  #9907 is well-intentioned, but not strictly necessary.  You may not want this to depend on it?  In other words, can you proceed without the move and the fix for classes?  You really just want to ultimately do coding theory, right?
> 
> Rob

I'm also interested in cleaning up and improving Sage ;-) But you're right. This opened up a can of worms, I didn't expect. I've created a new Trac #9919 for making the workaround mentioned in #9907 general by patching sage_wraps. Then I can make this patch depend only on #9919. The future of #9907 can then be decided later (the current patch there would then have to be dependent on this patch and include patching the files patched here).


---

Comment by rbeezer created at 2010-09-16 17:20:25

Replying to [comment:22 jsrn]:
> I'm also interested in cleaning up and improving Sage ;-) But you're right. This opened up a can of worms, I didn't expect. 

Of course - cleanup is definitely to be encouraged!  But too many times the clean-up and cans of worms are unavoidable.  When you can, best to avoid trouble and isolate the problem like you are doing.


---

Comment by jsrn created at 2010-09-17 08:26:27

Ok, now it gets hairy (and annoying). In plot.misc, several functions from sage.ext.fast_eval are imported; these in turn imports all sorts of stuff (e.g. rings), which means that there will be circular references from e.g. polynomial_ring when applying this patch. This just underlines the importance of moving the decorators to a general place in Trac #9907. It also means that unless e.g. this patch the one for Trac #9919 is expanded to (illogically) move the sage.ext.fast_eval import statements down into the functions in which they are used, this patch will have to depend on #9907 (which should now probably depend on #9919). Ye gods  -- isolating problems are nice in theory, but...

On the upside, I am pretty sure that the problem with #9907 is easily solved -- it seems to come down to how to update the standard pickle jar. I might be wrong in this, of course.


---

Attachment

Rebased for 4.5.3. Change to more files and at more places as well as documentation. Added deprecation warnings.  Fixed frobenius doctest


---

Comment by jsrn created at 2010-09-23 14:08:27

Changing status from needs_work to needs_review.


---

Comment by jsrn created at 2010-09-23 14:08:27

Ok, so now I've posted fixes for Trac #9919 and #9907. I decided to assume both of those, as it seemed hard to get around either. So, assuming both of those, the just uploaded patch gives (me) no errors. The just uploaded is like yours, Rob, but with the frobenius() doctest fixed.

As I posted on sage.devel, I also wrote a patch for the decorator-complaints in Trac #9976.

Cheers, Johan


---

Comment by jsrn created at 2010-10-20 11:44:22

By the way, this patch contains all changes which were at one point suggested to be contained in Trac #7971. That trac can therefore be closed/invalidated.


---

Comment by rlm created at 2010-11-09 20:22:31

If I apply #6094, #9907, #9919, and #10107 together on top of sage-4.6, all long tests pass. The code looks good.

I have also closed #7971.


---

Comment by rlm created at 2010-11-09 20:22:31

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-11-10 09:43:15

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2010-11-10 09:43:15

The patch needs to be rebased to sage-4.6.1.alpha0:

```
patching file doc/en/constructions/linear_codes.rst
patching file sage/calculus/desolvers.py
Hunk #1 succeeded at 61 (offset 3 lines).
Hunk #2 succeeded at 829 (offset 117 lines).
Hunk #3 succeeded at 854 (offset 117 lines).
Hunk #4 succeeded at 886 (offset 117 lines).
Hunk #5 succeeded at 900 (offset 117 lines).
Hunk #6 succeeded at 938 (offset 117 lines).
Hunk #7 succeeded at 994 (offset 117 lines).
patching file sage/coding/code_bounds.py
patching file sage/coding/decoder.py
patching file sage/coding/linear_code.py
Hunk #1 succeeded at 202 (offset 2 lines).
Hunk #2 succeeded at 322 (offset 2 lines).
Hunk #3 succeeded at 359 (offset 2 lines).
Hunk #4 succeeded at 369 (offset 2 lines).
Hunk #5 succeeded at 1115 (offset 2 lines).
Hunk #6 succeeded at 1143 (offset 2 lines).
Hunk #7 succeeded at 1164 (offset 2 lines).
Hunk #8 succeeded at 1174 (offset 2 lines).
Hunk #9 succeeded at 1535 (offset 2 lines).
Hunk #10 succeeded at 1556 (offset 2 lines).
Hunk #11 succeeded at 1580 (offset 2 lines).
Hunk #12 succeeded at 1716 (offset 2 lines).
Hunk #13 succeeded at 1731 (offset 2 lines).
Hunk #14 succeeded at 1745 (offset 2 lines).
Hunk #15 succeeded at 1775 (offset 2 lines).
Hunk #16 succeeded at 1814 (offset 2 lines).
Hunk #17 succeeded at 1871 (offset 2 lines).
Hunk #18 succeeded at 1891 (offset 2 lines).
Hunk #19 succeeded at 1905 (offset 2 lines).
Hunk #20 succeeded at 1937 (offset 2 lines).
Hunk #21 succeeded at 1954 (offset 2 lines).
Hunk #22 succeeded at 2289 (offset 13 lines).
Hunk #23 succeeded at 2307 (offset 13 lines).
Hunk #24 succeeded at 2326 (offset 13 lines).
Hunk #25 succeeded at 2387 (offset 13 lines).
patching file sage/combinat/designs/block_design.py
patching file sage/combinat/designs/incidence_structures.py
patching file sage/finance/easter.py
patching file sage/groups/matrix_gps/matrix_group.py
patching file sage/interfaces/ecm.py
patching file sage/matrix/matrix_double_dense.pyx
Hunk #4 FAILED at 1524.
Hunk #5 succeeded at 1544 (offset 1 line).
Hunk #6 succeeded at 1567 (offset 1 line).
1 out of 6 hunks FAILED -- saving rejects to file sage/matrix/matrix_double_dense.pyx.rej
patching file sage/matrix/matrix_modn_sparse.pyx
Hunk #2 succeeded at 778 with fuzz 2.
Hunk #3 succeeded at 791 with fuzz 2.
patching file sage/rings/polynomial/polynomial_compiled.pyx
patching file sage/schemes/elliptic_curves/padic_lseries.py
patching file sage/symbolic/expression.pyx
Hunk #2 succeeded at 6443 (offset 745 lines).
Hunk #3 succeeded at 6452 (offset 745 lines).
Hunk #4 succeeded at 6504 (offset 745 lines).
Hunk #5 succeeded at 6642 (offset 745 lines).
Hunk #6 succeeded at 6651 (offset 745 lines).
Hunk #7 succeeded at 6698 (offset 745 lines).
Hunk #8 succeeded at 6718 (offset 745 lines).
Hunk #9 succeeded at 6734 (offset 745 lines).
Hunk #10 succeeded at 6760 (offset 745 lines).
Hunk #11 succeeded at 6827 (offset 745 lines).
Hunk #12 succeeded at 6864 (offset 745 lines).
```



---

Comment by jsrn created at 2010-11-16 09:59:31

Rebased for 4.6.1.alpha0. Still requires patches for #9919 and #9907 (in that order)


---

Attachment


---

Comment by jsrn created at 2010-11-16 10:00:02

Changing status from needs_work to needs_review.


---

Comment by jsrn created at 2010-11-16 10:01:27

Robert Miller already gave the green light to the old version, so the review is only for the minor change in sage.matrix.matrix_double_dense made for rebasing.


---

Comment by rlm created at 2010-11-26 13:13:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2010-12-02 16:08:59

Resolution: fixed
