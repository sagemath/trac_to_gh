# Issue 282: Add matrix() class to FiniteFields and FiniteField extensions

Issue created by migration from https://trac.sagemath.org/ticket/282

Original creator: ncalexan

Original creation time: 2007-02-23 20:02:37

Assignee: somebody

Keywords: finitefield extension matrix polynomial

NumberFields support a matrix() class, very handy.  FiniteFields and FiniteField extensions should also support such a beast.  In fact, all algebraic extensions should provide such functionality, but at this time there is no generic AlgebraicExtension class in which to put such functionality.  Damn you, Pyrex and multiple inheritance!


---

Comment by was created at 2007-02-24 02:29:08

I don't understand what you're talking about, what you want, or why this is a defect and not
an enhancement.  Please clarify this trac issue.


---

Comment by malb created at 2007-09-18 12:43:54

Changing status from new to assigned.


---

Comment by malb created at 2007-09-18 12:43:54

Changing assignee from somebody to malb.


---

Comment by malb created at 2007-09-18 12:43:54

This ticket means that the method matrix() which is described as: "The matrix of right multiplication by the element on the power basis $1, x, x^2, \ldots, x^{d-1}$ for the number field.  Thus the {\em rows} of this matrix give the images of each of the $x^i$." should be added to finite extension fields. Also, (my addition) the method vector() of GFq should proably be added to number field elements.


---

Attachment


---

Comment by malb created at 2007-10-20 22:46:58

The attached patch implements this.


---

Comment by malb created at 2007-10-20 22:47:07

Changing status from assigned to new.


---

Comment by malb created at 2007-10-21 22:44:40

Changing status from new to assigned.


---

Comment by malb created at 2007-10-23 19:51:22

Resolution: fixed


---

Comment by malb created at 2007-10-23 19:51:22

applied to 2.8.9.alpha0
