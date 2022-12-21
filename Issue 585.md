# Issue 585: Problem with PARI number field interface

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2007-09-04 00:34:20

Assignee: was

There are two issues with the PARI interface for number fields. The first is that it isn't clear what F._pari_ should return -- it currently returns the defining polynomial, but there are other objects that might be more appropriate. It's actually running very generic code for this; since number fields are about to be redone anyway, this is worth keeping in mind. The second is a printing problem:

sage: F = NumberField(x^3-2,'alpha')

sage: F
 Number Field in alpha with defining polynomial x^3 - 2

sage: F._pari_()
 NumberFieldinalphawithdefiningpolynomialx^3 - 2

This comes from the fact that the entire output of the second line gets passed into PARI's gp_read_str function, which isn't the right thing to do.




---

Attachment


---

Comment by was created at 2007-09-07 03:47:55

Resolution: fixed
