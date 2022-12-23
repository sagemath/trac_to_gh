# Issue 430: RDF poly's don't factor

Issue created by migration from https://trac.sagemath.org/ticket/430

Original creator: rlm

Original creation time: 2007-08-16 03:10:55

Assignee: rlm

Keywords: RDF factor

polynomial_element.Polynomial.factor doesn't
know what to do with the RDF ring.

http://www.gnu.org/software/gsl/manual/html_node/Polynomials.html

sage: import numpy

sage:  numpy.roots?

The values in the rank-1 array p are coefficients of a polynomial. If the length of p is n+1 then the polynomial is

p[0] * x**n + p[1] * x**(n-1) + ... + p[n-1]*x + p[n]

sage: a=numpy.array([1,0,1],dtype=float)
sage: numpy.roots(a) 


---

Comment by rlm created at 2007-08-18 16:34:07

Changing status from new to assigned.


---

Comment by rlm created at 2007-08-18 19:15:30

Resolution: worksforme


---

Comment by rlm created at 2007-08-18 19:15:30

The factoring now works, but it depends on root finding, which currently sucks. A new ticket will be made for the root problem.
