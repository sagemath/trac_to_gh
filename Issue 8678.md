# Issue 8678: Improvements for morphisms of ModulesWithBasis

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-04-12 21:20:15

Assignee: nthiery

CC:  sage-combinat

Keywords: homsest

The upcoming patch in the Sage-Combinat queue will implement:
 - inverses for morphisms of finite dimensional vector spaces
 - tensor products of morphisms

At this occasion, it will start a bit of cleanup in the category framework for homsets


---

Comment by nthiery created at 2010-07-13 19:45:57

Changing status from new to needs_work.


---

Comment by nthiery created at 2010-07-13 19:45:57

Changing keywords from "homsest" to "homsets, module morphisms".


---

Comment by saraedum created at 2013-09-11 12:39:03

This is is a very old ticket. Anyway, can I find the patch that fixes `_test_category` somewhere? This also fails for #15154. Or should I just disable these tests?


---

Comment by saraedum created at 2013-09-26 23:55:29

Replying to [comment:3 saraedum]:
> This is is a very old ticket. Anyway, can I find the patch that fixes `_test_category` somewhere? This also fails for #15154. Or should I just disable these tests?

Since there is no reply here, I created a partial fix at #15232.


---

Comment by git created at 2014-06-29 05:16:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-06-29 05:37:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-07-01 22:00:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-07-03 01:19:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-07-11 11:58:44

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-07-11 12:00:50

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-07-11 12:54:05

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-07-11 12:58:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-07-11 13:38:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-07-11 14:34:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nthiery created at 2014-07-11 14:37:04

Now mosts tests pass. The remaining failing ones are because of some finite dimensional algebras over a finite field become finite, hence finite semigroups. And currently finite semigroups are automatically made into enumerated sets using their generators; however those generators are not always available.


---

Comment by git created at 2014-07-11 14:50:21

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-15 10:44:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-18 09:31:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-18 09:33:37

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-08-20 04:24:13

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2014-08-20 05:17:24

From the diff, you've accidentally removed the `i += 1`, so it should run forever (provided the 0th component is non-trivial). Ah what I wouldn't give for a python builtin `do-while` loop...


---

Comment by git created at 2014-08-28 20:17:47

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by virmaux created at 2014-09-01 17:20:09

Humph, so two points:

1- The last push correct a bug in TriangularModuleMorphism with on_basis.

2- I did not know that my push would have change the branch (but I should as it is a 'private' one) and do not know how to replace back the right branch, which is _u/nthiery/categories/module-morphisms-8678_. Sorry for the noise :s

At least, if my correction is wrong it should be very easy to reset :)
----
New commits:


---

Comment by git created at 2014-10-15 15:13:30

Branch pushed to git repo; I updated commit sha1. Last 10 new commits:


---

Comment by SimonKing created at 2014-10-15 15:14:12

Last 10 new commits:


---

Comment by nthiery created at 2014-10-15 15:15:26

#17160 I am working on now should fix the failing tests.


---

Comment by git created at 2015-03-05 18:26:28

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-06 22:32:30

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-07 08:34:15

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-10 13:13:47

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-10 14:08:47

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-10 20:56:56

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-10 22:23:46

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-10 22:41:11

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-10 22:55:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-10 23:35:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-11 09:38:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-11 09:39:20

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-14 02:38:50

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-14 05:10:58

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nthiery created at 2015-03-14 05:17:41

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2015-03-14 05:20:09

Hi Franco,

I believe I have taken care of everything we discussed on Monday. So back to needs review!
There remains to little points to be discussed in Davis:

   - Should the user documentation about triangular morphisms
     be in the class or in module_morphism?

   - triangular=True led to triangular="lower" while the
     default value for triangular is "upper"

Cheers from warm Davis!
                                                    Nicolas


---

Comment by git created at 2015-03-14 14:08:34

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-14 14:24:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-14 15:02:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by darij created at 2015-03-14 15:04:28

Needs review, but depends on a blue ticket, and work issues listed?


---

Comment by nthiery created at 2015-03-14 15:05:27

Just a tip: given the many modifications here and there, and the new classes, it's might be simpler to review directly the whole new file src/sage/modules/module_with_basis_morphism.py rather than looking at its diff. Otherwise, I took care of the moving of the code from modules_with_basis.py in a separate commit, so that you can diff from there.


---

Comment by nthiery created at 2015-03-14 15:08:25

I had forgotten to clear the issue. #17160 is just waiting for feedback on the sage mailing list to be finalized. In any cases both tickets are rather independent, so the review of the code of this one can start right away. Of course it will be necessary to rerun the tests once the failures coming from #17160 will be fixed


---

Comment by git created at 2015-03-15 05:31:44

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-17 06:46:09

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by saliola created at 2015-03-18 22:24:17

Changing keywords from "homsets, module morphisms" to "homsets, module morphisms, days64".


---

Comment by saliola created at 2015-03-18 22:24:17

Changing status from needs_review to needs_info.


---

Comment by saliola created at 2015-03-18 22:24:17

Here is my review. I pushed some typo fixes, improved some of the documentation and added a few doctests. Here are a few issues and questions:

- I don't understand the comment in ``src/sage/categories/finitely_generated_semigroups.py``:

```
# TODO: update transitive ideal
```


- a couple of doctests include the following line:

```
sage: import __main__; __main__.f = f  
```

can you explain why this is necessary?

- line 1015 of ``src/sage/modules/module_with_basis_morphism.py``: the doc says this should work over an ring, so perhaps the following is not a valid assumption?

```
c = c / s[j]  # the base ring is a field
```


- the doctests don't pass, but this seems to be related to #17160
----
New commits:


---

Comment by git created at 2015-03-19 08:10:49

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-19 08:16:56

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by nthiery created at 2015-03-19 08:32:02

Hi Franco!

Replying to [comment:60 saliola]:

> Here is my review.  I pushed some typo fixes, improved some of the
> documentation and added a few doctests.

Thanks! I double checked your changes and am happy with them. This
prompted a second pass of little things here and there to make the doc
more uniform. I also implemented the two we had discussed.

> Here are a few issues and questions:
> 
> - I don't understand the comment in ``src/sage/categories/finitely_generated_semigroups.py``:
> {{{
> # TODO: update transitive ideal
> }}}

The code uses TransitiveIdeal which is being deprecated in favor of
RecursivelyEnumeratedSet. I have added this as comment on #17160.

> - a couple of doctests include the following line:
> {{{
> sage: import __main__; __main__.f = f  
> }}}
> can you explain why this is necessary?

A function defined interactively is not picklable, which prevents us
from using it to test the pickling of objects built upon them. This
classical trick fakes f being defined in a Python module.

> - line 1015 of ``src/sage/modules/module_with_basis_morphism.py``: the doc says this should work over an ring, so perhaps the following is not a valid assumption?
> {{{
> c = c / s[j]  # the base ring is a field
> }}}

The documentation mentions:

```
        - ``self`` -- a triangular morphism over a field, or a
          unitriangular morphism over a ring
```

which is tested a couple lines above:

```
        if G.base_ring() not in Fields and not self._unitriangular:
            raise NotImplementedError, "coreduce for a triangular but not unitriangular morphism over a ring"
```


> - the doctests don't pass, but this seems to be related to #17160

Yup. Next step is to cleanup #17160. And then we will know better if
there are a couple trivial doctests that need to be updated here.

Cheers,
                                Nicolas


---

Comment by saliola created at 2015-03-19 15:13:07

The latest branch causes some problems:

```
> git trac pull
> sage -br
**********************************************************************

Oops, Sage crashed. We do our best to make it stable, but...
```


The error message in the crash report is:

```
ImportError: No module named modules_with_basis.morphism
```



---

Comment by saliola created at 2015-03-19 15:16:04

I wanted to make the following change:

```
+            sage: ult = lambda i: sum(  y[j] for j in range(i,4)  ) # uni-upper
+            sage: phi = X.module_morphism(ult, triangular="lower", codomain=Y)
```

The comment `# uni-upper` should be uni-lower.


---

Comment by git created at 2015-03-19 15:51:02

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-19 15:53:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by saliola created at 2015-03-19 21:23:04

Hello Nicolas. Thanks for the answers and the fixes. This looks good to me now. I'm ready to set this to positive review once #17160 is finalized (i.e., once all doctests here pass).


---

Comment by git created at 2015-03-20 04:37:12

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-20 08:15:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-20 20:46:25

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by saliola created at 2015-03-20 20:48:33

I've looked over all the recent changes, too. Positive review, once all doctests pass (which they appear to do here).


---

Comment by git created at 2015-03-21 07:03:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2015-03-21 17:03:51

FYI - #17160 is finalized.


---

Comment by nthiery created at 2015-03-23 21:46:50

Changing status from needs_info to positive_review.


---

Comment by nthiery created at 2015-03-23 21:46:50

On {{{Linux sagange 3.2.0-4-amd64 #1 SMP Debian 3.2.63-2+deb7u1 x86_64
GNU/Linux}}}, and after merging in 6.6.rc0, I am getting only those
errors with `make ptestlong`:

```
sage -t --long src/sage/doctest/control.py  # 1 doctest failed
sage -t --long src/sage/calculus/calculus.py  # 1 doctest failed
sage -t --long src/sage/misc/trace.py  # 2 doctests failed
sage -t --long src/sage/modular/arithgroup/arithgroup_perm.py  # Timed out
sage -t --long src/sage/homology/simplicial_complex.py  # 1 doctest failed
```


Sounds like they are all maxima related, and I doubt there is any
relation to this ticket; rc0 fails similarly. Hence I am setting
this to positive review on behalf of Franco.


---

Comment by nthiery created at 2015-03-24 00:12:38

Changing type from defect to enhancement.


---

Comment by vbraun created at 2015-04-14 19:43:34

Resolution: fixed
