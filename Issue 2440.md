# Issue 2440: Doctests for rings/quotient_ring.py

Issue created by migration from https://trac.sagemath.org/ticket/2440

Original creator: cswiercz

Original creation time: 2008-03-09 18:38:38

Assignee: cswiercz

Keywords: docstring, doctest

Provide missing docstrings and doctests for rings/quotient_ring.py.


---

Comment by cswiercz created at 2008-03-09 19:01:34

When testing QuotientRing_generic.cover_ring, I ran into an issue with evaluating the cover ring of a polynomial quotient ring. Apparently, the PolynomialQuotientRings_field object doesn't have a "cover_ring" function! Can the class just "borrow" from the QuotientRing_generic class?


---

Comment by cswiercz created at 2008-03-09 19:02:17

The above observation was written as a TODO in rings/quotient_ring.py under the cover_ring function.


---

Comment by cswiercz created at 2008-03-09 19:08:39

Looking at the code for QuotientRing_generic.ideal, it seems that this is not the "general" code for creating an ideal in a ring. There are several Singular related calls. I'm not sure what some of these things mean so hopefully someone will be willing to take a look and provide some documentation.


---

Comment by cswiercz created at 2008-03-09 19:35:32

Docstrings and doctests for non-underscore functions in rings/quotient_ring.py. Some functions returning NotImplementedError have been documented as TODO items.


---

Attachment


---

Comment by cswiercz created at 2008-03-09 19:38:43

Changing status from new to assigned.


---

Comment by cremona created at 2008-03-09 20:37:24

Review:

Excellent.

About characteristic():  should not be hard to implement in at least one case:  Set c = self.base_ring().characteristic().  If c is prime then self's char is also p.  If c>0 but is not prime one could loop through divisors d of c to see if self(d)==self(0).   But if c==0 I cannot see an easy way of doing this.

About gens(): I agree that it is not nice having 0 in the list of gens, but deleting them would break the correspondance between the gens of R and the gens of R/I, which the user will probably expect.

I also noticed one thing which is not purely a docstring/test:  when R is a field you inserted a short-cut.  That looks fine to me.

Positive review, should be accepted.


---

Comment by mabshoff created at 2008-03-09 21:04:33

Merged in Sage 2.10.3.rc4


---

Comment by mabshoff created at 2008-03-09 21:04:33

Resolution: fixed
