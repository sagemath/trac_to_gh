# Issue 2549: Implement VectorSpace over symbolic function ring

Issue created by migration from https://trac.sagemath.org/ticket/2549

Original creator: edrex

Original creation time: 2008-03-16 17:26:41

Assignee: cwitty

I'd like to be able to create a vector space over a symbolic function ring:

```
var('x,y,z');VS=VectorSpace(CallableSymbolicExpressionRing((x,y,z)),2)
    raise TypeError, "K must be a field"
<type 'exceptions.NotImplementedError'>:
```

I suppose the result of calling an element of K may be a field element or not, depending on what arguments are passed. Note that this is glossed-over in the case or SR, since `VectorSpace(SR,2)` works.

Perhaps what is needed is a new type of object, a symbolic mapping whose signature is explicit, like:

```
f(x,y,z, RR)
}}} or {{{
g(x,y,z, (RR, RR, ZZ))
```

where the first syntax defines a mapping whose arguments are all in RR, the second a mapping with the last argument in ZZ.

This specifies the domain of the mapping but not the range. I suppose you could validate the output of the mapping to make sure that it was in (or coerced to?) the specified range (say RR or ZZ). Perhaps something like this is on the horizon, since it seems like a fairly deep architectural change?


---

Comment by edrex created at 2008-03-20 23:01:25

This is really a feature request for a type of object which can be used to represent a real vector field, which is effectively a mapping from R<sup>n</sup> to R<sup>n</sup>. The object should 
 * have convenience methods for 
  * producing a quiver plot (via vector_field_plot)
  * solving numerically (via ode_solver) and plotting solutions of the autonomous 1st-order differential equation represented by the vector field, with initial condition (x1,..,xn)
 * be callable (what is the vector at this point of the field?)
 * be have a fast float version which uses the fast-float versions of its component functions

Since vector fields are just a special case of R<sup>m</sup> to R<sup>n</sup> maps (which are in turn special cases of ..., which is where my brain shuts off), perhaps VectorField should just be a special case/implementation of a more generic class of object.

Here is the quick-n-dirty n-d VectorField class I have been using for my graduate-level diffeq hw, which implements the items above in a stand-alone, non-derived class: https://www.sagenb.org/home/pub/1745/


---

Comment by edrex created at 2008-03-20 23:01:25

Changing type from defect to enhancement.


---

Comment by jason created at 2009-02-13 17:43:55

See #2546 for a related ticket.


---

Comment by jason created at 2009-02-13 17:45:02

edrex, sagenb has been reset, which means your class is not available anymore.  Could you post it here so that whoever wants to tackle this ticket may have a place to start from?


---

Comment by mmezzarobba created at 2014-03-15 18:05:02

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2014-03-15 18:05:02

Can this ticket be closed? The specific feature it was asking for now (sort of) exists:

```
sage: var('x,y,z');VS=VectorSpace(CallableSymbolicExpressionRing((x,y,z)),2)
(x, y, z)
sage: VS.an_element()
(x, y, z) |--> (1, 0)
```

and work on various kinds of tensor fields is ongoing as part of SageManifolds (#14865, #15916).


---

Comment by chapoton created at 2014-03-18 09:00:27

I agree that this can be closed.


---

Comment by chapoton created at 2014-03-18 09:00:27

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-19 04:35:24

Resolution: fixed
