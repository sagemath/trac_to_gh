# Issue 8936: Expose facet inequalities for lattice polytopes

Issue created by migration from https://trac.sagemath.org/ticket/8936

Original creator: novoselt

Original creation time: 2010-05-09 04:24:47

Assignee: mhampton

CC:  vbraun

While lattice polytopes compute and store facet normals and shifts internally, there were no functions to access them. This patch adds functions facet_normal and facet_constant to fix the situation.

I have also fixed a typo in the docstring of ReflexivePolytope, which has probably occurred during automatic conversion of docstrings.


---

Comment by novoselt created at 2010-05-09 04:27:24

Changing status from new to needs_review.


---

Attachment

Fixed a mistake in the first version...


---

Comment by vbraun created at 2010-05-19 08:23:14

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2010-05-19 08:23:14

Straight-forward addition of new functionality to the LatticePolytope class. Please merge...


---

Comment by novoselt created at 2010-06-07 02:56:18

Changing type from defect to enhancement.


---

Comment by mhansen created at 2010-06-07 05:18:45

Resolution: fixed
