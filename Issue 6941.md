# Issue 6941: GCD, XGCD for polynomial rings with templating

Issue created by migration from https://trac.sagemath.org/ticket/6941

Original creator: spancratz

Original creation time: 2009-09-15 22:39:51

Assignee: tbd

CC:  rws jpflori

GCD and XGCD methods should return *monic* greatest common divisors.  However, at the moment these two methods in the template file ``sage/rings/polynomial/polynomial_template.pxi`` prevent this by enforcing that ``gcd(a,0) == a`` and ``gcd(0,b) == b``.

I suggest that the code for these two methods in the template file should only refer to the corresponding ``celement_foo`` methods of the actual implementation.  This way, all the logic is in the ``celement_foo`` methods, rather than being split between the two levels.

The patch for this should touch the template file as well as the two linkage files for GF2X and zmod polynomials.


---

Attachment

The patch looks good, applies cleanly and doctests pass. However, do we really need to mimic the old behaviour?


---

Comment by spancratz created at 2009-09-19 19:25:36

Replying to [comment:1 malb]:
> The patch looks good, applies cleanly and doctests pass. However, do we really need to mimic the old behaviour?

I assume you are referring to the hyperelliptic curves part?  Yes, I think so.  Otherwise, some doctests fail.  I haven't tried to fully understand the mathematics of that part, but it seems to depend on the assumption gcd(a,0) == a.

Sebastian


---

Comment by malb created at 2009-09-29 08:07:26

Maybe we can ask the person who wrote that code?


---

Comment by mhansen created at 2009-11-04 08:29:42

Changing status from needs_review to needs_info.


---

Comment by robertwb created at 2010-05-27 22:04:39

If we need to mimic the old xgcd behavior, it would be much better to abstract that out into its own function with a docstring and some tests.


---

Comment by robertwb created at 2010-05-27 22:04:39

Changing status from needs_info to needs_work.
