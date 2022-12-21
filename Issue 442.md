# Issue 442: RDF roots() function gives imprecise results

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2007-08-18 19:17:27

Assignee: rlm

For example:

sage: x = polygen(RDF)
sage: f = (x-1)^3
sage: f.roots()

[1.00000859959,
 0.999995700205 + 7.44736245561e-06*I,
 0.999995700205 - 7.44736245561e-06*I]



---

Comment by rlm created at 2007-08-18 19:44:05

in sage-2.8.1/local/lib/python2.5/site-packages/numpy/lib/polynomial.py,
line 116 appears to be casting whatever float type is given to just float.


---

Comment by rlm created at 2007-08-18 20:24:13

This is just as much an issue for eigen_left and eigen_right:
 
sage: g = Matrix(RDF, [[0, -9],[1,6]]); g
[ 0.0 -9.0]
[ 1.0  6.0]
sage: g.eigen_left()
([3.00000003183, 2.99999996817], .....


---

Comment by rlm created at 2007-08-18 20:33:44

Resolution: duplicate


---

Comment by rlm created at 2007-08-18 20:33:44

See ticket #211.
