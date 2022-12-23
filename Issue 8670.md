# Issue 8670: Provide projections methods for word paths

Issue created by migration from https://trac.sagemath.org/ticket/8670

Original creator: slabbe

Original creation time: 2010-04-11 12:10:06

Assignee: slabbe

CC:  abmasse vdelecroix robertwb tjolivet tmonteil

Nice mathematical objects can be obtained when projecting appropriately a discrete path (Rauzy fractals for instance).

This patch introduces 3 projection functions for word path. It also adds 1 function to `WordMorphism` and 2 matrix rotation functions to `sage/plot/plot3d/transforms.pyx`.

The first 1000 points of the Rauzy fractal :


```
    sage: s = WordMorphism('1->12,2->13,3->1')
    sage: D = s.fixed_point('1')
    sage: v = s.pisot_vector()
    sage: P = WordPaths('123',[(1,0,0),(0,1,0),(0,0,1)])
    sage: w = P(D[:1000])
    sage: w.projected_plot(v)
```


See more examples in doctests.


---

Comment by slabbe created at 2010-04-11 13:08:37

Changing status from new to needs_review.


---

Comment by slabbe created at 2010-04-13 11:44:16

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2010-04-13 11:44:16

There are some limit case problems :


```
sage: from sage.plot.plot3d.transform import *
sage: rotate_vector_on_axis((1,0,0), 0)
Traceback (most recent call last):
...
ZeroDivisionError: Rational division by zero
```


Will post a new patch soon.


---

Comment by slabbe created at 2010-04-18 19:39:15

I fixed the above problem in the updated patch. Needs review!

Since I am adding two functions to the file `sage/plot/plot3d/transform.pyx`, I am also adding Robert Bradshaw in cc of this ticket. He might have some comments to share.


---

Comment by slabbe created at 2010-04-18 19:39:15

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2010-04-27 15:58:48

Does not depend on any known patch. Applies on 4.3.4.


---

Attachment

1. Your definition of Pisot eigenvector is ambiguous.

```
Returns the left eigenvector of the incidence matrix associated
to the largest eigenvalue (in absolute value).
```

It is possible that there are multiple eigenvalues with the same absolute value:

```
sage: mu = WordMorphism('a->c,b->c,c->ab')
sage: m = matrix(mu); m
[0 0 1]
[0 0 1]
[1 1 0]
sage: m.eigenvalues()
[0, -1.414213562373095?, 1.414213562373095?]
```

It is not clear which eigenvector gets returned here.

Also, there may be more than one eigenvector associated to your "maximal" eigenvalue, and your method only returns one eigenvector:

```
sage: mu = WordMorphism('a->a,b->b,c->abc')
sage: mu.pisot_eigenvector_left()
(1, -1, 0)
sage: m = matrix(mu); m
[1 0 1]
[0 1 1]
[0 0 1]
sage: m.eigenspaces_left()
[
(1, Vector space of degree 3 and dimension 2 over Rational Field
User basis matrix:
[ 1 -1  0]
[ 0  0  1])
]
```


2. The method `directive_vector` should include a definition of what the directive vector is.

3. In your functions `rotate_ith_to_zero` and `rotate_vector_on_axis`, you first construct the matrix and then coerce it into the ring specified by the user. Why is this preferable to doing the computations directly in the ring? What about making this an option `compute_in_ring=False`? I think all you need to do is add the following line at the beginning:

```
if compute_in_ring is True:
    v = vector(ring, v)
```



---

Comment by saliola created at 2010-06-23 16:04:26

Changing status from needs_review to needs_work.


---

Comment by slabbe created at 2010-10-15 21:00:21

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2010-10-15 21:00:21

Needs review again!


---

Attachment

Applies over the precedent patch


---

Comment by tjolivet created at 2011-01-28 17:56:02

Changing status from needs_review to needs_work.


---

Comment by tjolivet created at 2011-01-28 17:56:02

Hi,

Here are a few remarks:

(1) There is a doctest failure:

  `File "/home/timo/sage-4.6.1/devel/sage-trac_8670/sage/plot/plot3d/transform.pyx", line 325:    sage: rotate_vector_on_axis(v, 0, ring=RealField(10)) * vExpected:    (5.5, 0.0020, 0.0020, 0.00)Got:    (5.5, 0.00098, 0.00098, 0.00)`

This should be fixed by using "`...`", and could be done for the other occurrences of printed floats.

(2) I think that the rotations matrices should be in a file in sage/matrix/. I remember having looked for something like `rotate_arbitrary`, but I didn't find it because it was in plot3d/ and not in matrix/.

(3) The documentation for `rotate_vector_on_axis` could be a little bit clearer (the description).

Otherwise this is a nice and useful patch.


---

Attachment

Applies over the precedent 2 patches


---

Comment by slabbe created at 2011-01-29 13:28:21

Thanks for the comments. I moved the two rotation matrix constructor to the file `sage/matrix/constructor.py`. I improved the docstrings and fixed the doctest failure (I was having the same).

Needs review.


---

Comment by slabbe created at 2011-01-29 13:28:21

Changing status from needs_work to needs_review.


---

Attachment

Apply only this one.


---

Comment by slabbe created at 2011-01-30 00:43:23

For the patchbot :

Apply trac_8670_folded-sl.patch


---

Comment by tjolivet created at 2011-02-07 12:36:27

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-03-17 19:22:34

Resolution: fixed
