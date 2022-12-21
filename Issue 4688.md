# Issue 4688: wrap pari functions idealstar and ideallog

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-12-03 20:54:42

Assignee: was

CC:  m.t.aranes@warwick.ac.uk

If I is an ideal in the ring of integers R of a number field K, then the pari functions idealstar(K,I) returns the group `(R/I)^*` in the form of an abstract abelian group (order, invariants, and a list of generators).  And ideallog() computes the discrete log with respect to I, i.e. given a in K with valuation 0 at all primes dividing I, returns a vector representing a mod I as an element of that abstract abelian group.

It would be very useful to have these wrapped in Sage.  They appear in libs/pari/decl.pxi already so that should not be hard.



---

Attachment


---

Comment by AlexGhitza created at 2009-02-17 12:15:45

Maite Aranes wrote the code for wrapping the pari functions into Sage, and I reviewed it and added docstrings/doctests.

We need someone to review the docstrings, then this is ready to go.


---

Comment by cremona created at 2009-02-17 17:24:17

Postive review (and thanks to Alex for doing a good job on this).  the patch applies fine to 3.3.rc0 and the tests in sage/libs/pari pass.

It will be easy to test this properly until we have Sage-level functions to access them, but that is being worked on and will be in a separate ticket, so this patch should PASS.


---

Comment by cremona created at 2009-02-18 17:12:36

Ticket #5306 will handle the user interface to these from with Sage's own classes for number fields and ideals.


---

Comment by mabshoff created at 2009-02-20 06:06:40

Merged in Sage 3.3.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 06:06:40

Resolution: fixed
