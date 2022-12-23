# Issue 3754: Would it be possible to add some functionality to sage.rings.number_field.galois_group.GaloisGroup?

Issue created by migration from https://trac.sagemath.org/ticket/3754

Original creator: ljpk

Original creation time: 2008-08-01 15:46:41

Assignee: joyner

If K is a number field, then K.galois_group() gives a group with very little functionality. One can get an abstract group with more functionality by calling K.galois_group().group(), but it would be nice to be able to access the functionality of the group type without having to forget the metadata attached to the Galois group (its number field, etc). Would this be difficult?


---

Comment by mabshoff created at 2008-08-02 00:23:32

This is not something that should be a ticket in trac since it is too undefined. The summary does not accurately describe a solvable ticket, so something like this should go to sage-devel before opening a ticket.

I am tempted to invalidate this ticket. William?

Cheers,

Michael


---

Comment by davidloeffler created at 2009-05-11 19:28:03

My work at #5159 hopefully provides something a bit closer to what Lloyd was after. In any case it invalidates his description above :-) Shall we close this one now?


---

Comment by mabshoff created at 2009-05-12 01:39:45

Resolution: duplicate


---

Comment by mabshoff created at 2009-05-12 01:39:45

Fixed via #5159. Any sort of feature request should go to sage-devel or sage-nt anyway since the visibility of tickets tends to be quite low.

Thanks David for following up :)

Cheers,

Michael
