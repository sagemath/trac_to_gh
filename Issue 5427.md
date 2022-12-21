# Issue 5427: Evaluate the naming of (variable substitution) routines in Quadratic forms

Issue created by migration from Trac.

Original creator: jonhanke

Original creation time: 2009-03-03 12:40:48

Assignee: jonhanke

Compare the naming of methods in the QuadraticForm class for consistency with other Sage naming conventions.  In particular, it would be nice if there were a set of standard variable substitution methods for classes of objects involving variables (e.g. polynomials, quaternion algebras, Hermitian/symplectic/linear forms).


---

Comment by jonhanke created at 2009-03-03 12:44:53

Also decide about in-place or copying conventions for operations on quadratic forms.  I think that copying is the standard, so it would be good to add a compatible in-place routines according to the Sage naming standard.
