# Issue 3793: Some elliptic curve doctests fail when the optional database is installed

Issue created by migration from https://trac.sagemath.org/ticket/3793

Original creator: cremona

Original creation time: 2008-08-09 12:51:34

Assignee: was

A few of the doctests in `ell_rational_field.py` fail when the optional package database_cremona_ellcurve-20071019 is installed, mainly because for curves in the database the gens() as supplied by the database may differ from those computed on the fly.  (In almost all cases the generators are not uniquely determined, being the generators of a finitely-generated abelian group.  We have put some thought into how to make the generators canonical but have not yet succeeded.)



---

Attachment

To test this you should really test the doctests in ell_rational_field.py both before and after installing the database.


---

Comment by ncalexan created at 2008-08-10 20:57:03

I ran the tests on 3.0.6 before and after installing the database, *without* applying the patch, and both tests passed everything.  So... is this really necessary?

But I still think this looks good and should be applied, since it addresses some ambiguity that could be annoying.


---

Comment by cremona created at 2008-08-10 21:16:00

The point is that there was randomness in the old doctests:  whenever they use E.gens() where E is an elliptic curve we cannot guarantee that the same gens are computed (on different systems, etc).  As a special case of this ambiguity, the gens obtained from the database (which don't change! -- or at least ont very rarely, e.g. if they are found to be wrong)  may not agree with computed gens.

I dealt with this by either inserting "# random", or by using explicit points instead of gens().

I hope that with this explanation you can give this (admittedly rather trivial) patch a positive review.


---

Comment by cremona created at 2008-08-10 21:20:32

ok, so it already has a positive review!  Thanks!


---

Comment by mabshoff created at 2008-08-11 04:59:07

Resolution: fixed


---

Comment by mabshoff created at 2008-08-11 04:59:07

Merged in Sage 3.1.alpha1
