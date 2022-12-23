# Issue 1183: Residue fields are broken

Issue created by migration from https://trac.sagemath.org/ticket/1183

Original creator: roed

Original creation time: 2007-11-16 02:35:39

Assignee: was

The current implementation of residue fields for number fields is broken.  It just takes the defining polynomial for the number field, factors it over Z/pZ, picks one factor and creates an extension using that factor.  This breaks because elements of the ring of integers, when expressed in terms of the power basis of the number field can have denominators divisible by p.

The solution is to create a p-maximal order and do some linear algebra to come up with a map that doesn't break on denominators divisible by p.  Pari's nfinit has a way to give it a partial factorization of the discriminant that will produce a p-maximal order.

If you want to implement this, talk to William Stein or David Roe for more details.


---

Comment by mabshoff created at 2007-11-16 11:14:25

Ifti did open #1185 for his specific problem. So in case this is solved and the status of #1183 remains unchanged please resolve that ticket, also.

Cheers,

Michael


---

Attachment


---

Attachment


---

Comment by was created at 2007-12-02 13:15:41

further work, but still some issues....


---

Attachment

NOT ready to be released yet.


---

Comment by was created at 2007-12-13 22:16:18

NOTE!!  Be sure to also apply

http://trac.sagemath.org/sage_trac/ticket/1494


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2007-12-15 13:40:29

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 13:40:29

Resolution: fixed
