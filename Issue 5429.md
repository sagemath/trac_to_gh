# Issue 5429: Change the QuadraticForm base_ring to only define the equivalence, but not the ring for coefficients/values

Issue created by migration from https://trac.sagemath.org/ticket/5429

Original creator: jonhanke

Original creation time: 2009-03-03 13:37:46

Assignee: tbd

It is sometimes inconvenient to require that all quadratic_forms take values in their ring of equivalence.  This should be separated out into two parts, a coefficient_ring and an equivalence_ring.  

Perhaps for ease of tab-completion these should be called ring_* instead of *_ring?  Also, coefficient_ring could equally well be called value_ring, though that may be more confusing to find for the average user.

Calls to the base_ring() method should almost everywhere be replaced by calls to equivalence_ring(), with the notable exception of the constructor.

The default constructor would take only one ring, which would be the equivalence ring, and the inferred coefficient ring would be the fraction field/object of the given ring.


---

Comment by AlexGhitza created at 2010-01-01 23:09:45

Changing component from algebra to quadratic forms.
