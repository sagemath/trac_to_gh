# Issue 9470: Switch toric varieties to enhanced fans

Issue created by migration from https://trac.sagemath.org/ticket/9470

Original creator: novoselt

Original creation time: 2010-07-10 05:52:15

Assignee: AlexGhitza

CC:  vbraun

As indicated in #9326, it is desirable for fans and cones associated to toric varieties to know these toric varieties. The framework for such an association was already designed (with a view towards morphisms), this patch puts it to work.

I have written it on top of #9245, which is the last patch in the chain with positive review.


---

Comment by novoselt created at 2010-07-10 06:27:20

Hi Volker,

This patch should let you to easily add cohomology methods to cones and have everything together in the `toric_variety` module.

I have modified the code of `EnhancedCone` a little with the idea that if you have a chain of enhanced fans

Fan ---> EFan1 ---> EFan2

and, say, intersect two cones belonging to `EFan2`, then three cones will be created replicating the same chain

Cone ---> ECone1 ---> ECone2

I am not completely sure if this is necessary, but it will be consistent in the sense that "base cone" of ECone2 will belong to "base fan" of its fan.

Thank you,
Andrey


---

Comment by novoselt created at 2010-07-10 06:27:20

Changing status from new to needs_review.


---

Comment by vbraun created at 2010-07-23 20:02:48

Changing status from needs_review to needs_work.


---

Comment by vbraun created at 2010-07-23 20:02:48

The `cone_containing` method of a `Fan_of_toric_variety` should also return a `Cone_of_toric_variety`, but right now:

```
sage: P2=toric_varieties.P2()
sage: fan=P2.fan()
sage: [ type(c) for c in fan ]
[<class 'sage.schemes.generic.toric_variety.Cone_of_toric_variety'>, <class 'sage.schemes.generic.toric_variety.Cone_of_toric_variety'>, <class 'sage.schemes.generic.toric_variety.Cone_of_toric_variety'>]
sage: N=fan.lattice()
sage: c = fan.cone_containing( N(0,1) ); c
1-d cone in 2-d lattice N
sage: type(c)
<class 'sage.geometry.cone.ConvexRationalPolyhedralCone'>
sage: c.ambient()
1-d cone in 2-d lattice N
```



---

Comment by novoselt created at 2010-07-24 07:28:44

Changing status from needs_work to needs_review.


---

Attachment

Changed line 2232 in `fan` (I missed explicit setting of the ambient fan). I have added a doctest for the above case into `Fan_of_toric_variety.__init__`.


---

Comment by vbraun created at 2010-07-27 16:03:00

Looks good now!


---

Comment by vbraun created at 2010-07-27 16:03:00

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-09 09:48:32

Resolution: fixed
