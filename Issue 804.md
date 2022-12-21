# Issue 804: Matrix should not inherit from AlgebraElement

Issue created by migration from Trac.

Original creator: roed

Original creation time: 2007-10-03 08:30:30

Assignee: was

CC:  jason pbruin

Keywords: AlgebraElement, Matrix

People just don't want to fix it because you'll have to rebuild everything after editing element.pxd.


---

Comment by mabshoff created at 2007-12-04 14:26:12

Maybe now is a good time to do it?

Cheers,

Michael


---

Comment by mhansen created at 2007-12-05 19:12:48

What are the reasons for the change in organization?


---

Comment by AlexGhitza created at 2008-01-24 09:01:58

Changing component from algebraic geometry to linear algebra.


---

Comment by robertwb created at 2008-11-14 06:30:48

The reason for the change is that not all matrices are Algebra Elements.


---

Comment by kcrisman created at 2009-12-30 05:37:48

What should it inherit from instead?  This is a naive question, but perhaps someone with not much skill but much patience could fix this :)


---

Comment by robertwb created at 2009-12-30 08:04:28

ModuleElement


---

Comment by pbruin created at 2014-04-02 00:33:13

Changing status from new to needs_review.


---

Comment by pbruin created at 2014-04-02 00:33:13

Given that this ticket has been open for more than seven years, it turned out to be surprisingly straightforward.  There is one small simplification: `Matrix` used to have two identical methods `_mul_()` and `__mul__()`, now it only needs `__mul__()`.  On the other hand, new (but very straightforward) `__pow__()` and `__div__()` methods were required.


---

Comment by kcrisman created at 2014-04-02 02:34:59

Wow, nice necromancy!  Dumb question - any other translations of tutorials have this bit which would need to be translated?


---

Comment by pbruin created at 2014-04-02 09:24:50

Replying to [comment:12 kcrisman]:
> any other translations of tutorials have this bit which would need to be translated?
It seems not; `grep RingElement src/doc/*/tutorial/*` only finds the English and French ones.


---

Comment by kcrisman created at 2014-04-02 13:51:43

> > any other translations of tutorials have this bit which would need to be translated?
> It seems not; `grep RingElement src/doc/*/tutorial/*` only finds the English and French ones.
Interesting - apparently that must have been added after the other translations were made.


---

Comment by vdelecroix created at 2014-05-05 07:01:04

Hi,

At first glance, I thought this ticket would help to build tropical matrices as discussed in #14507... but no, the "base ring" for tropical matrix is a [semiring](http://en.wikipedia.org/wiki/Semiring) and not a ring (no requirement of an additive inverse). Am I right?

Vincent


---

Comment by pbruin created at 2014-05-05 09:13:26

Replying to [comment:15 vdelecroix]:
> At first glance, I thought this ticket would help to build tropical matrices as discussed in #14507... but no, the "base ring" for tropical matrix is a [semiring](http://en.wikipedia.org/wiki/Semiring) and not a ring (no requirement of an additive inverse). Am I right?
I think you are.  Everywhere in Sage, matrices and vectors are assumed to have coefficients in some base ring.  This would probably be much harder to change than the inheritance issue addressed in this ticket.  If enough people want tropical matrices, then it seems we need new classes `Matrix_semiring` and `Vector_semiring`, possibly inheriting from some `ModuleElement_semiring`...


---

Comment by pbruin created at 2014-05-14 20:44:28


```
sage -t --long src/sage/structure/element.pyx  # 2 doctests failed
```



---

Comment by pbruin created at 2014-05-14 20:44:28

Changing status from needs_review to needs_work.


---

Comment by git created at 2014-05-14 21:17:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by pbruin created at 2014-05-14 21:18:23

Changing status from needs_work to needs_review.


---

Comment by lftabera created at 2014-07-18 11:52:04

Looks good to me. I also think that tropical matrices should have their own classes.

My copy did not compile against 6.3.beta3 but was probably more an issue with the beta since it failed before attempting to build the sage library. With 6.3.beta5 it works like a charm.


---

Comment by lftabera created at 2014-07-18 11:52:04

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-07-19 04:57:49

Resolution: fixed
