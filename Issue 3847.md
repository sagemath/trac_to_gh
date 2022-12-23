# Issue 3847: can't make vector of ints

Issue created by migration from https://trac.sagemath.org/ticket/3847

Original creator: saliola

Original creation time: 2008-08-14 04:24:35

Assignee: tbd

sage: vector([int(0)])
Traceback (most recent call last):
...
TypeError: unable to find a common ring for all elements

Shouldn't ints be coerced to Integers?


---

Attachment

This issue has also come up in other guises on sage-devel or sage-support (can't seem to be able to find the threads right now, though).

It all boils down to Sequence(), which takes a list of things and returns a sequence of things that lie in the same "universe", if canonical coercions are possible.  So if you give it a list containing an RDF, an Integer, and a Rational, it will give you back a sequence of three RDF's.  The problem is with the builtin Python types (int, long, float, complex), for which we of course have no coercions.  So given a bunch of ints, Sequence tries to see where in the Sage hierarchy they fit, finds nothing, and sends them back without a common "universe".  This makes vector() throw an exception, because a vector should be over a ring.

The patch fixes this by giving Sequence() an optional parameter use_sage_types, defaulting to False.  If the parameter is True, Sequence() catches the builtin Python types and makes them into the appropriate Sage objects, then carries on.  I am making vector() always pass use_sage_types=True to Sequence().  This fixes the unpleasant behavior reported in this ticket, and gives vector() a bit more flexibility -- see the new doctests for more examples.

Sequence() is a fairly fundamental class and I didn't want to change its default behavior for fear of speed degradation in places other than vector().


---

Comment by cremona created at 2008-09-08 13:23:44

Review: I think this has been done very well.   The default behaviour for Sequence() has not changed, so there should be no effect anywhere other than for the Vector constructor, which does what it should.

The patch applies cleanly to 3.1.2.rc0 and all doctests in sage.structure and sage.modules pass.

There may be other places where Sequence() is used where this functionality would be useful.


---

Comment by mabshoff created at 2008-09-14 13:43:30

Oops, this patch nearly escaped. Note that the two spaces between positive and review let this review escape from the report.

Cheers,

Michal


---

Comment by mabshoff created at 2008-09-15 03:54:27

Resolution: fixed


---

Comment by mabshoff created at 2008-09-15 03:54:27

Merged in Sage 3.1.2.rc4
