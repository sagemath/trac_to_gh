# Issue 7535: Errors should be raised, not returned.

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2009-11-26 10:24:15

Assignee: tbd

Keywords: error return

The following issue was considered in at least two threads, the latest at [http://groups.google.com/group/sage-devel/browse_thread/thread/3661fde739474fdb](http://groups.google.com/group/sage-devel/browse_thread/thread/3661fde739474fdb).

There are several places in the Sage code where errors are not raised but returned. A hopefully exhaustive search brought up the following:

```
sage: import exceptions
sage: for E in dir(exceptions):
....:     if not E.startswith('__'):
....:         s = search_src("return "+E)
....:         if s:
....:             print s
....:
rings/finite_field_element.py:384:                return ArithmeticError, "Multiplicative order of 0 not defined."
rings/finite_field_givaro.pyx:1956:                return ArithmeticError, "Multiplicative order of 0 not defined."
structure/element.pyx:2601:            return ArithmeticError, "Multiplicative order of 0 not defined."

rings/ring.pyx:687:            return NotImplementedError
modular/hecke/module.py:706:        abstract base class, return NotImplementedError.
modular/arithgroup/congroup_gammaH.py:928:            return NotImplementedError
geometry/polyhedra.py:1068:            return NotImplementedError
symbolic/expression.pyx:1524:        return NotImplementedError
symbolic/expression_conversions.py:638:            return NotImplementedError("SymPy function '%s' doesn't exist" % f)

interfaces/gap.py:580:            return RuntimeError, "Error evaluating %s in %s"%(line, self)

modular/abvar/finite_subgroup.py:280:            return ValueError, "self and other must be in the same ambient Jacobian"
groups/perm_gps/permgroup_named.py:945:            return ValueError, "Degree must be 2."
groups/perm_gps/permgroup_named.py:988:            return ValueError, "Degree must be 2."
```


Of course, if an error is returned it can't be catched, which implies obvious problems.

I have no idea what component that ticket should be associated with. "Performance" seemed the least inappropriate description to me.

Is there any of the above cases in which the error should really be returned, not raised?



---

Comment by jhpalmieri created at 2009-11-26 15:45:19

See also #7532.


---

Comment by timdumol created at 2010-01-18 19:59:51

Changing component from performance to misc.


---

Comment by timdumol created at 2010-01-18 20:15:11

This should do the trick.


---

Comment by timdumol created at 2010-01-18 20:15:11

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-18 20:52:45

Makes all remaining returns of exceptions into raising.


---

Attachment

I'm not sure what you mean by "remaining", since there is no patch at #7532 (or elsewhere?) fixing any other instances of this.  I'm attaching a patch dealing with two more of these, leaving, I think, just the one in rings.pyx.  See #7532 for that one.

Positive review for timdumol's patch, so if mine is okay, this whole ticket can get a positive review.


---

Comment by jhpalmieri created at 2010-01-19 00:45:26

apply on top of the other patch


---

Attachment

I am about to add a patch to #7532 which fixes (for me) the remaining issue in schemes/elliptic_curves.


---

Comment by timdumol created at 2010-01-20 09:38:45

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-20 09:38:45

Doctests pass with the latter patch and the one in #7532, so I'll mark both as positive review.


---

Comment by mvngu created at 2010-01-23 19:54:29

Merged in this order:

 1. [trac_7535-errors-raise.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7535/trac_7535-errors-raise.patch) --- timdumol: please remember to put  your username in your patch. I have merged this patch in your name.
 1. [trac_7535-part2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7535/trac_7535-part2.patch)


---

Comment by mvngu created at 2010-01-23 19:54:29

Resolution: fixed
