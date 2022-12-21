# Issue 9290: Implement Coxeter groups in their geometric representation

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-06-21 07:49:19

Assignee: sage-combinat

CC:  sage-combinat




---

Comment by nthiery created at 2010-06-21 07:50:15

Partially depends on #8237


---

Comment by chapoton created at 2012-11-19 16:59:51

Changing keywords from "" to "coxeter".


---

Comment by chapoton created at 2013-07-25 15:14:51

see also the code in the ticket #14816


---

Comment by tscrim created at 2013-09-11 02:21:32

Changing status from new to needs_review.


---

Comment by tscrim created at 2013-09-11 02:21:32

Here's a patch which should take care of all except the second point since I thought Dynkin diagrams where separate from Coxeter diagrams except when there are 1,2,3, or 4 bonds (and even then, we're ignoring the arrows).

Base patch is from #15137, but now uses the UCF as the default field.


---

Comment by chapoton created at 2013-09-15 16:41:21

there are some failing doctests

EDIT: hmm, it rather seems to be a problem with the patchbot..


---

Comment by chapoton created at 2013-09-15 16:41:21

Changing status from needs_review to needs_work.


---

Comment by tscrim created at 2013-09-16 14:09:54

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2013-09-16 14:09:54

Yep, something is up with the patchbot, so I gave it a kick.

```
sage -t ../combinat/root_system/cartan_matrix.py
    [97 tests, 15.77 s]
sage -t matrix_gps/coxeter_group.py
    [72 tests, 0.36 s]
sage -t ../combinat/root_system/coxeter_group.py
    [28 tests, 18.65 s]
----------------------------------------------------------------------
All tests passed!
----------------------------------------------------------------------
Total time for all tests: 18.8 seconds
    cpu time: 26.2 seconds
    cumulative wall time: 34.8 seconds
```



---

Comment by chapoton created at 2013-09-17 18:42:12

one doctest failing


```
File "/home/chapoton/sage-5.12.beta5/devel/sage/sage/groups/matrix_gps/coxeter_group.py", line 278, in sage.groups.matrix_gps.coxeter_group.CoxeterMatrixGroup.__init__
Failed example:
    TestSuite(W).run(max_runs=30) # long time
Expected nothing
Got:
    Failure in _test_matrix_generators:
    Traceback (most recent call last):
      File "/home/chapoton/sage-5.12.beta5/local/lib/python2.7/site-packages/sage/misc/sage_unittest.py", line 282, in run
        test_method(tester = tester)
      File "/home/chapoton/sage-5.12.beta5/local/lib/python2.7/site-packages/sage/groups/matrix_gps/finitely_generated.py", line 376, in _test_matrix_generators
        tester.assertEqual(g.matrix(), h.matrix())
      File "cachefunc.pyx", line 1774, in sage.misc.cachefunc.CachedMethodCallerNoArgs.__call__ (sage/misc/cachefunc.c:9546)
      File "/home/chapoton/sage-5.12.beta5/local/lib/python2.7/site-packages/sage/groups/matrix_gps/group_element.py", line 447, in matrix
        m = g.matrix(self.base_ring())
      File "element.pyx", line 1076, in sage.libs.gap.element.GapElement.matrix (sage/libs/gap/element.c:8618)
      File "element.pyx", line 1473, in sage.libs.gap.element.GapElement_Cyclotomic.sage (sage/libs/gap/element.c:10511)
      File "parent.pyx", line 761, in sage.structure.parent.Parent.__getattr__ (sage/structure/parent.c:6823)
      File "misc.pyx", line 251, in sage.structure.misc.getattr_from_other_class (sage/structure/misc.c:1606)
    AttributeError: 'UniversalCyclotomicField_with_category' object has no attribute '_n'
    ------------------------------------------------------------
    The following tests failed: _test_matrix_generators
```



---

Comment by tscrim created at 2013-09-17 19:24:36

The problem was the conversion from gap's cyclotomics to sage by using the UCF. This is fixed in #15204.

```
sage: W = CoxeterGroup([[1,3,2],[3,1,6],[2,6,1]])
sage: W._test_matrix_generators()
```



---

Comment by chapoton created at 2013-09-21 16:22:12

Hello, I have a few comments and questions

"assert implementation" : I think this use of assert to check input is not encouraged

"lazy_import('sage.groups.raag', 'RightAngledArtinGroup')" : has this something to do in this ticket ?

What are the changes "sage/groups/matrix_gps/finitely_generated.py" for ?


---

Comment by tscrim created at 2013-09-21 17:10:25

Hey Frederic,

Replying to [comment:11 chapoton]:
> "assert implementation" : I think this use of assert to check input is not encouraged

This was a hold-over from the previous implementation, but this is definitely a good time to get rid of it. Fixed.

> "lazy_import('sage.groups.raag', 'RightAngledArtinGroup')" : has this something to do in this ticket ?

Because I didn't split it cleanly with #15137. Fixed.

> What are the changes "sage/groups/matrix_gps/finitely_generated.py" for ?

I need to pass the `CoxeterGroups` category up during the initialization, so I had to make those changes.

Thanks for catching that,

Travis


---

Comment by chapoton created at 2013-09-22 11:11:24

Well, it seems that the patch triggers the import of numpy at startup. I have not tried to investigate where this happens.


---

Comment by chapoton created at 2013-09-22 11:24:21

Changing status from needs_review to needs_work.


---

Attachment

I made `CoxeterMatrixGroup` lazy import in to fix the numpy startup import.


---

Comment by tscrim created at 2013-09-23 02:20:41

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by chapoton created at 2013-10-20 20:33:10

Hello Travis,

I have made a cosmetic review patch, that you can fold into yours if you want.

This almost looks good to go, but I was a bit disappointed when I tried:

```
sage: K = NumberField(x**2+5,'t')
sage: CoxeterGroup(['H',3],base_ring=K)
```

and it failed. If there is a way to make that work, it would be great !


---

Comment by chapoton created at 2013-10-21 18:32:02

ok, I can see no easy way to do that. Let us forget this for the moment.

Good to go ?


---

Comment by tscrim created at 2013-10-22 21:32:34

Changing status from needs_review to positive_review.


---

Comment by tscrim created at 2013-10-22 21:32:34

Hey Frederic,

I can't see an easy way to do so either. There might be a solution, but it'll probably be either complicated or cumbersome.

Thanks for doing the review,

Travis


---

Comment by jdemeyer created at 2013-10-31 19:15:44

Resolution: fixed
