# Issue 9781: Enhanced fans fail for complicated cases

Issue created by migration from https://trac.sagemath.org/ticket/9782

Original creator: vbraun

Original creation time: 2010-08-22 21:20:49

Assignee: novoselt

CC:  novoselt

Fans of toric varieties do not work correctly, for example see the following:

```
sage: f = Fan([(0, 2, 4), (0, 4, 5), (0, 3, 5), (0, 1, 3), (0, 1, 2), (2, 4, 6), (4, 5, 6), (3, 5, 6), (1, 3, 6), (1, 2, 6)], [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (0, 1, 2), (0, 1, 3), (1, 0, 4)])
sage: f.is_complete()
True
sage: X = ToricVariety(f)
sage: X.fan().is_complete()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)

/home/vbraun/opt/sage-4.5.2/devel/sage-main/<ipython console> in <module>()

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in is_complete(self)
   1742         # Then boundary cones are (d-1)-dimensional.
   1743         for cone in self(codim=1):
-> 1744             if len(cone.star_generator_indices()) != 2:
   1745                 self._is_complete = False
   1746                 return False

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in __call__(self, dim, codim)
    816         else:
    817             return self.cones(dim, codim)
--> 818 
    819     def __cmp__(self, right):
    820         r"""

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in cones(self, dim, codim)
   1547                 if len(top_cones) == self.ngenerating_cones():
   1548                     top_cones.sort(key=lambda cone:
-> 1549                                             cone.star_generator_indices()[0])
   1550                 levels[-1] = top_cones
   1551             if len(levels) >= 2: # We have rays

/home/vbraun/Sage/sage/local/lib/python2.6/site-packages/sage/geometry/fan.pyc in <lambda>(cone)
   1548                     top_cones.sort(key=lambda cone:
   1549                                             cone.star_generator_indices()[0])
-> 1550                 levels[-1] = top_cones
   1551             if len(levels) >= 2: # We have rays
   1552                 rays = list(levels[1])

IndexError: tuple index out of range
```

I'm pretty sure it is a bug in Andrey's switch to enhanced cones for toric varieties (`trac_9470_toric_variety_fans.patch`). If I back out that patch it works fine. Unfortunately we didn't catch that in our doctests, we should add tests for complicated toric varieties and mark them as `# long time`


---

Comment by novoselt created at 2010-08-22 22:39:37

Working on it!


---

Attachment


---

Comment by novoselt created at 2010-08-23 00:28:15

Changing status from new to needs_review.


---

Comment by novoselt created at 2010-08-23 00:28:15

It was a silly typo in generic fans (I confused the number of rays with the number of cones). We definitely need more doctests, but so far adding new functionality serves as one of the sources ;-) I have added your example from this ticket to documentation of the function which had the error. It adds about 2 seconds to the test time so I put it in without #long so far - checking completeness uses quite a few functions, so it is a nice one to have.

Anyway - the patch is "one-worder" plus doctest, ready for review!


---

Comment by vbraun created at 2010-08-23 11:55:40

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2010-08-23 11:55:40

Thanks, this fixes it and explains why it hasn't surfaced earlier: Tests usually use toric surfaces where the number of rays equals the number of number of generators. But that only holds for 2D complete fans.


---

Comment by mpatel created at 2010-09-15 09:56:47

Resolution: fixed
