# Issue 827: nfrootsof1 from Pari

Issue created by migration from Trac.

Original creator: jvoight

Original creation time: 2007-10-05 00:00:23

Assignee: was

Import nfrootsof1 from Pari so as to count the number of roots of unity in a number field.


---

Attachment

It appears that nfrootsof1 is available, i.e. via K.pari_nf().nfrootsof1.  This just uses it, and fixes (what I think is) a small bug in CyclotomicField(7).zeta(14).


---

Attachment


---

Comment by mabshoff created at 2008-01-20 00:42:38

Resolution: fixed


---

Comment by mabshoff created at 2008-01-20 00:42:38

Merged in Sage 2.10.1.alpha0
