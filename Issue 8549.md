# Issue 8549: Add a cycle enumerator for Permutation Group

Issue created by migration from Trac.

Original creator: nborie

Original creation time: 2010-03-16 20:07:53

Assignee: nborie

CC:  sage-combinat

Keywords: permutation, cycle, enumeration

Let G a permutation group. Each permutation of G has a cycle type. The goal of this ticket is to add a method for permutation group which return a dictionary associating for each cycle pattern, the number of permutation in G having this pattern.


---

Comment by nborie created at 2010-03-16 23:07:04

This should allow to do some plethysm very easily.

Suggestion welcome to improve the latex math line and make it more nice and understandable.


---

Comment by nborie created at 2010-03-16 23:07:04

Changing status from new to needs_review.


---

Comment by nborie created at 2010-04-21 13:34:05

After face to face discussion, this patch is ready for review!


---

Comment by nthiery created at 2010-04-21 13:35:34

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-04-21 13:35:34

Changing keywords from "permutation, cycle, enumeration" to "permutation groups, cycle index, Polya enumeration".


---

Comment by jhpalmieri created at 2010-04-22 02:07:14

If I apply "trac_8549_cycle_enumerator-nb.patch" on top of 4.4.alpha1, all tests pass.  If I instead apply the patch from #8500, all tests pass.  If I apply _both_ patches, though, then I get a doctest failure:

```
sage -t -long "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py"
**********************************************************************
File "/Applications/sage_builds/sage-4.4.alpha1/devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py", line 315:
    sage: len(C.points())
Exception raised:
    Traceback (most recent call last):
      File "/Applications/sage_builds/sage-4.4.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[7]>", line 1, in <module>
        len(C.points())###line 315:
    sage: len(C.points())
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py", line 327, in points
        self.__points = self._points_fast_sqrt() # this is fast using Zech logarithms
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py", line 239, in _points_fast_sqrt
        points.append(self.point([x, v+sqrtD, one], check=True))
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/scheme.py", line 256, in point
        return self._point_class(self, v, check=check)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/algebraic_scheme.py", line 196, in _point_class
        return self.__A._point_class(*args, **kwds)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/projective_space.py", line 535, in _point_class
        return morphism.SchemeMorphism_projective_coordinates_field(*args, **kwds)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/morphism.py", line 608, in __init__
        X.codomain()._check_satisfies_equations(v)
      File "/Applications/sage_builds/sage-4.4.alpha1/local/lib/python/site-packages/sage/schemes/generic/algebraic_scheme.py", line 465, in _check_satisfies_equations
        raise TypeError, "Coordinates %s do not define a point on %s"%(list(v),self)
    TypeError: Coordinates [7*a + 9, 2*a + 2, 1] do not define a point on Hyperelliptic Curve over Finite Field in a of size 11^2 defined by y^2 + (x^2 + 2)*y = x^5 + x + 10
**********************************************************************
1 items had failures:
   1 of   8 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/palmieri/.sage//tmp/.doctest_hyperelliptic_finite_field.py
	 [8.2 s]
```



---

Comment by jhpalmieri created at 2010-04-22 02:07:14

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2010-04-22 02:08:47

I'm sorry, I forgot to say that I've only seen this on a Mac (OS X 10.6.3).  On sage.math, all tests pass.


---

Comment by rbeezer created at 2010-05-28 15:04:42

Replying to [comment:7 jhpalmieri]:
> I'm sorry, I forgot to say that I've only seen this on a Mac (OS X 10.6.3).  On sage.math, all tests pass.

#8500 and #8549 together pass all long tests on 64-bit Ubuntu 9.04.  I also saw Mike Hansen at Sage Days 21 test just the file `sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py` with both patches and it passed all tests as well.  I'll be working on a review at some point today.


---

Comment by rbeezer created at 2010-05-29 04:14:42

Nicolas(s),

This is a nice addition, and I can already think of a use for it in a classroom example.

Some small comments/suggestions:

1.  One small bit of language, in


```
Here are the cycle index of some permutation groups
```


I would write the plural as "cycle indices."  Nicely written otherwise.


2.  Would there be some way to qualify a value for the parent keyword as being legitimate?  For example, with `D=DihedralGroup(7)`, `14*D.cycle_index(parent=QQ)` goes boom.  It doesn't seem that there is a simple type to test on (but maybe I'm wrong on this), but it does look like parent need only implement  term() and sum().  Would it work to put something like  `parent.term(Partition([1]), 1)` in a try/except block?


3.  Documentation.

(a)  Do you want to add this into the reference manual?

(b)  Last doctest block needs a preceding "::" to make it render as verbatim.

(c)  Two instances of "cycle_type" near the top print weird due to the underscore.


Important stuff:  builds and passes long tests, works as advertised.  So I'm ready to give this a positive review subject to the above minor items.

Rob


---

Comment by rbeezer created at 2010-05-29 04:58:29

See #8500 for the results of further OSX testing on this combination.


---

Comment by nthiery created at 2010-06-01 09:16:23

Hi,

I just wrote a quick patch in the queue implementing the requested changes, and adding FinitePermutationGroups to the ref manual where it was missing. Nicolas, please double check, fold, and reupload.


---

Attachment

Thanks very much for these fix.

All tests pass for sage, all tests long and optionnal pass for the finite_permutation_groups, the doc is well built... New comments for parent argument make also more clear the doc.

Positive Review from me. Thanks you Rob for pointing improvements and fix.


---

Comment by nborie created at 2010-06-01 11:30:39

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2010-06-01 11:31:17

Changing status from needs_review to positive_review.


---

Comment by nborie created at 2010-06-01 11:38:46

I change two times the status of this patch but I precise the last change come from Nicolas Thiéry.

This positive review is also modulo the comment 

> If I apply "trac_8549_cycle_enumerator-nb.patch" on top of 4.4.alpha1, all tests pass. If I instead apply the patch from #8500, all tests pass. If I apply both patches, though, then I get a doctest failure

I currently have no possible access to any OS X machine. All my tests was computing from Ubuntu machines.


---

Comment by mhansen created at 2010-06-05 22:29:25

Resolution: fixed
