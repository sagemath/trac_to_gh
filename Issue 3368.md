# Issue 3368: bug in CartesianProduct

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-04 22:07:22

Assignee: mhansen

CC:  sage-combinat

Hi,

The following is a bug that Bill Page found in Sage.  It is in the combinatorial
classes code  (mostly) by Mike Hansen, so maybe he'll fix it. 


```
In: http://modular.math.washington.edu/msri06/work/kohel/msri_magma.pdf

 "A Brief Magma Tutorial" by David R. Kohel gives this example:

----------

The parent structure of a tuple is more important than in the case
of sequences or sets.
> C := CartesianProduct(Integers(),RationalField());
> t := C!<1,1>;
> Parent(t[2]);
Rational Field

----------

The analogous computation in Sage 3.0.2 yields:

sage: C = CartesianProduct(Integers(),RationalField())

# case 1
sage: t=C([1,1/2])
sage: parent(t[0])
Integer Ring
sage: parent(t[1])
Rational Field

# case 2
sage: t=C([1,1])
sage: parent(t[0])
Integer Ring
sage: parent(t[1])
Integer Ring

---------

Notice that the parent of t[1] is incorrect in the 2nd case.
```



---

Comment by mhansen created at 2008-06-04 22:10:32

This was never the intended functionality of CartesianProduct -- it is different than the CartesianProduct of Magma.  It was mainly intended to iterator over the cartesian product of a bunch of iterables in Python.  Maybe the name should be changed.


---

Comment by vdelecroix created at 2016-08-31 15:37:46

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2016-08-31 15:37:46

This is now fixed (and moreover `CartesianProduct` is now deprecated)!


---

Comment by nthiery created at 2016-08-31 16:05:43

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2016-08-31 16:05:43

Confirmed:


```
sage: C = cartesian_product([Integers(),RationalField()])
sage: c = C([1,1])
sage: c
(1, 1)
sage: c[0].parent()
Integer Ring
sage: c[1].parent()
Rational Field

sage: C = CartesianProduct(Integers(),RationalField())
/opt/sage-git/src/bin/sage-ipython:1: DeprecationWarning: CartesianProduct is deprecated. Use cartesian_product instead
See http://trac.sagemath.org/18411 for details.
  #!/usr/bin/env python
sage: c = C([1,1])
sage: c[0].parent()
Integer Ring
sage: c[1].parent()
Rational Field
```


Yeah, let's close a 4 digits eight years old combinat ticket for cheap :-)


---

Comment by vbraun created at 2017-01-21 18:03:11

Resolution: invalid
