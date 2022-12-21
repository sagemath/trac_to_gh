# Issue 2358: phi(I) for phi a ring morphism and I an ideal should work (IMHO); it used to and now it doesn't because of new-ish arithmetic architecture stuff

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-01 05:15:24

Assignee: somebody


```
Who rewrote the ring morphism code so that if phi is a
ring morphism, then phi(I) no longer works, for an ideal I?
Oh, David Roed in changeset 6772 (for me) from a few
months ago did this:

  "Cython'ed sage/rings/morphism.py, actually added wrapper_parent (even though I claimed to in the previous commit)."

I think that feature, i.e., that phi(I) works, was very nice
and is standard notation in mathematics, and I want
it back.   Then the codepath that leads to the above weird
bug wouldn't exist.

I think the way to fix this is:
  (1) Rethink the assumption you're forcing on morphisms that they
can only apply to elements in the domain.   This overloading of
calling a morphism on (sub)objects is very standard in mathematics.
  (2) Change the architecture of __call__ as a result of (1).

 -- William
```



---

Comment by roed created at 2009-01-23 13:36:49

Resolution: worksforme


---

Comment by roed created at 2009-01-23 13:36:49

This was previously fixed.  See sage.categories.map.Map.__call__
