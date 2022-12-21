# Issue 8500: Add number_of_transitive_group function

Issue created by migration from Trac.

Original creator: nborie

Original creation time: 2010-03-11 20:49:20

Assignee: nborie

CC:  sage-combinat

Keywords: transitive group

TransitiveGroup are already in Sage and work only if you have the right database installed. As I offen test systematicly over all transitive groups, I will be happy to get this number in Sage.


```
sage: TransitiveGroup(7,7)
Transitive group number 7 of degree 7
sage: TransitiveGroup(7,8)
verbose 0 (846: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
Transitive group number 8 of degree 7
```



---

Comment by nborie created at 2010-03-11 21:34:28

Changing status from new to needs_review.


---

Comment by nborie created at 2010-03-12 07:23:26

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2010-03-12 23:58:11

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-03-13 09:01:48

Wow,that was quick, thanks!

I browsed through the patch, which looks good. Some minor comments before I do the final review:

 - Change "trac 8500 Add the finite enumerated set of TransitiveGroups" to "#8500 Add the enumerated set of TransitiveGroups"

 - Keep number_of_transitive_groups a private function (i.e. not in all.py)

 - TransitiveGroups() would better model the mathematical set of all transitive groups, even if this is only partially implemented. Hence TransitiveGroups() should be in InfiniteEnumeratedSets (and therefore TransitiveGroups().cardinality() will return infinity). As a side effect, the #long time should not be needed anymore for the TestSuite(TransitiveGroups()).run().

 - You may actually want to implement TransitiveGroups() as a DisjointUnionOfEnumeratedSets, which should essentially do all the work for you.

 -


---

Comment by nthiery created at 2010-03-13 09:01:48

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2010-03-13 09:18:40

Hi,

* Commit message : will do!

* Private function : Why not? There is no reference page built for permgroup_named.py... It will be used by the very private club...

* Ok, Do you prefer a StopIteration or a NotImplementedError for the __iter__ method ?

* DisjointUnionOfEnumeratedSets????? I don't know this toy but I already like the name. Will play with it (and hope it is robust (like children, when I play....))

Thanks for these advises...


---

Comment by nthiery created at 2010-03-13 11:38:57

Replying to [comment:6 nborie]:
> * Ok, Do you prefer a StopIteration or a NotImplementedError for the __iter__ method ?

Hmm, I guess NotImplementedError. And I assume that should be what occurs by default with DisjointUnionOfEnumeratedSets.

> 
> * DisjointUnionOfEnumeratedSets????? I don't know this toy but I already like the name. Will play with it (and hope it is robust (like children, when I play....))

Note: you'll have a micro-issue with classcall, which Florent is supposed to fix shortly (he stumbled into it yesterday.

Oh, by the way: what gap is providing you is actually an unrank function (see enumeratedSets). You just need to implement TransitiveGroups(3).unrank(5), and __iter__ will be provided to you for free.

> Thanks for these advises...

You are welcome!


---

Comment by nborie created at 2010-03-15 12:28:58

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2010-03-15 13:38:29

I included all yours recommendations. I just didn't remove the # long time for the test :
TestSuite(TransitiveGroups()).run()
Even it is now an Infinite Enumerated Set, the test still need around 20 seconds.


---

Attachment


---

Comment by nborie created at 2010-03-15 15:03:08

I just update the patch : I forgot some # optional. Done..


---

Attachment


---

Comment by nthiery created at 2010-04-18 20:01:54

All test pass on Sage 4.3.4 and 4.4-alpha0.

That will be a useful feature! Thanks for handling this!

Please check my reviewer's patch, and if it's fine, go ahead and set a positive review.


---

Comment by nborie created at 2010-04-18 21:30:33

I applied the two patches with the dependency. Everything is ok  except the sentence in the doc of the class TransitiveGroupsAll, the set is not finite!

```
sage.groups.perm_gps.permgroup_named.TransitiveGroupsAll¶

    The finite set of all transitive groups.
```

That's my fault from my patch... Who fix that ? modulo the two letter "in" before finite, it is a positive review....


---

Attachment


---

Comment by nborie created at 2010-04-19 08:16:51

I clearly set a positive review on your reviewer patch!

I had a failure in :
sage -t sage/groups/perm_gps/permgroup_named.py --optional --long

```
sage -t --optional --long "devel/sage-review/sage/groups/perm_gps/permgroup_named.py"
**********************************************************************
File "/opt/sage/devel/sage-review/sage/groups/perm_gps/permgroup_named.py", line 884:
    sage: TransitiveGroup(5,0)                 # requires optional database_gap
Expected:
    Traceback (most recent call last):
    ...
    AssertionError: n should be in {1,..,5}
Got:
    Traceback (most recent call last):
    ...
        assert n > 0
    AssertionError
```


Thus I propose you a final patch (very easy to review) with a fix of the doc of TransitiveGroupsAll and a move of an assert on the index of a transitive group.

Now, all tests long and optional passes. I hope we don't leave any error in the doc too.


---

Comment by nthiery created at 2010-04-19 17:25:31

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-04-19 17:25:31

Replying to [comment:14 nborie]:
> I clearly set a positive review on your reviewer patch!

Ok, thanks for checking!

> I had a failure in :
> sage -t sage/groups/perm_gps/permgroup_named.py --optional --long

Oops, I let that one slip through. Thanks for the report!

> Thus I propose you a final patch (very easy to review) with a fix of the doc of TransitiveGroupsAll and a move of an assert on the index of a transitive group.

I merged your doc fix in my patch. For the assertion, I fixed the doctest instead. The message is not as nice, but using assert n>0 has the (admittedly limited) advantage of failing even if the database is not there.

With this the patch is good to go. Positive review. Thanks for your work on this!

I'll now fold the two patches together and upload the final version here.


---

Comment by nthiery created at 2010-04-19 17:28:43

Apply only this one


---

Comment by nthiery created at 2010-04-19 17:33:14

Changing keywords from "transitive group" to "transitive groups".


---

Attachment


---

Comment by jhpalmieri created at 2010-04-22 02:08:05

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2010-04-22 02:08:05

If I apply "trac_8500_transitive_groups-final.patch" on top of 4.4.alpha1, all tests pass.  If I instead apply the patch from #8549, all tests pass.  If I apply _both_ patches, though, then on my Mac (OS X 10.6.3), I get a doctest failure:

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

Comment by nthiery created at 2010-04-22 06:25:34

Replying to [comment:17 jhpalmieri]:
> If I apply "trac_8500_transitive_groups-final.patch" on top of 4.4.alpha1, all tests pass.  If I instead apply the patch from #8549, all tests pass.  If I apply _both_ patches, though, then on my Mac (OS X 10.6.3), I get a doctest failure:

Ouch?!?!? How can two patches that add isolated features possibly break something so unrelated???

I am totally clueless on how to attack this. Is there a mac somewhere online where I could login to play around? Is the gap-database installed on that mac?

Thanks!


---

Comment by jhpalmieri created at 2010-04-22 22:02:35

Replying to [comment:18 nthiery]:
>
> Ouch?!?!? How can two patches that add isolated features possibly break something so unrelated???

I don't know, but it was quite repeatable: apply either patch first, no doctest failure, then apply the second one, and boom.  (Although it took me a little while to track down that two independent tickets seemed to be causing the problem.)  I just confirmed this on a second mac.  It seems to require 4.4.alpha1, not 4.4.alpha0, so it must also be related to one of the tickets already merged there: see [http://trac.sagemath.org/sage_trac/query?order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&merged=%7Esage-4.4.alpha1](http://trac.sagemath.org/sage_trac/query?order=priority&col=id&col=summary&col=status&col=type&col=priority&col=milestone&col=component&merged=%7Esage-4.4.alpha1) for a list. Of course, none of those touch the file schemes/hyperelliptic_curves/hyperelliptic_finite_field.py, either.  At least #8496, #8505, and #8557 have something to do with schemes...
 
> I am totally clueless on how to attack this. Is there a mac somewhere online where I could login to play around? Is the gap-database installed on that mac?

As far as I know, bsd.math.washington.edu is a mac which is used for Sage development.  You will need a separate account on it: an account on sage.math doesn't automatically give you one on bsd.math.  Ask William (or maybe Tom Boothby?) about that.


---

Comment by rbeezer created at 2010-05-29 04:56:26

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-05-29 04:56:26

I asked Jason Grout via IRC to test #8500 and #8549 on hyperelliptic_finite_field.py with OSX 10.6 and the file passed tests.  Slightly edited IRC discussion.


```
[21:34] <rbeezer> jason-: ping
[21:34] <jason-> pong
[21:35] <rbeezer> could you do a simple OSX 10.6 test?
[21:35] <rbeezer> #8500, #8549, apply one patch from each, then
[21:35] <rbeezer> sage -t -long "devel/sage/sage/schemes/hyperelliptic_curves/hyperelliptic_finite_field.py"
[21:35] <rbeezer> ???
[21:36] <jason-> Let me see
[21:37] <rbeezer> thanks - this particular combo is holding up both tickets
[21:39] <jason-> all tests passed!
[21:40] <rbeezer> thanks
[21:41] <jason-> rbeezer: that's osx 10.6
```


Same combination passed all long tests on 64-bit Ubuntu 9.04, in addition to the one file passing tests for Mike Hansen.

I ran long tests on `devel/sage/sage/groups/perm_gps/permgroup_named.py` with the gap database installed and it all passed tests.

Given that this seemed ready for a positive review and now passes tests on the OSX combination, I am going to set this to positive review and add Jason to the reviewer list.

Rob


---

Comment by rbeezer created at 2010-05-29 04:57:14

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-05-31 10:53:25

I just tried on bsd.sagemath.org, with 4.4.2 and just those two patches, and all test pass as well.


---

Comment by mhansen created at 2010-06-05 22:28:58

Resolution: fixed
