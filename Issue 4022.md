# Issue 4022: [with patch, needs review] Gröbner bases over Z and Z/nZ

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-08-31 17:13:50

Assignee: malb

The attached patch implements -- in a slow, lame way -- Gröbner bases over `ZZ` and `IntegerModRing` as defined in the Becker & Weispfenning. This code should be replaced by the new Singular code soon-ish, but it can't hurt to have a clean toy implementation.

While I think that the `d_basis` implementation is correct, I recommend somebody double checks. Particularly, the `MPolynomial_libsingular.reduce` implementation  for ZZ should receive some careful examination.


---

Attachment


---

Comment by malb created at 2008-08-31 17:16:42

Quite likely the attached patch depends on #4021, I didn't check though whether it works stand alone too.


---

Comment by malb created at 2008-09-20 15:47:20

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2008-09-28 07:00:32

Applies cleanly on top of 3.1.3.alpha1 + patches at #686 and #4021.

I *really* like the examples.


---

Comment by mabshoff created at 2008-09-28 18:15:39

Merged in Sage 3.1.3.alpha2


---

Comment by mabshoff created at 2008-09-28 18:15:39

Resolution: fixed
