# Issue 9541: optimize number field arithmetic using flint and singular

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-07-18 19:16:41

Assignee: davidloeffler

CC:  cwitty




---

Comment by spancratz created at 2010-07-18 19:19:27

C code for rational polynomials based on FLINT1


---

Attachment


---

Attachment

basic refactoring of number fields elements -- only arithmetic with absolute fields works now.


---

Attachment

Including basic support for flint


---

Comment by was created at 2010-07-20 00:58:20

flattened of everything. apply only this.


---

Attachment

I will start posting part1, part2, etc.  Then when all is done, a flattened version of it all.


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment

Note to self: turn cdef poly* normal_form(self, poly* p) into a singular_polynomial_normal_form() function to make it easier to use.


---

Attachment


---

Attachment


---

Comment by was created at 2011-03-20 18:29:25

I've decided not to work on this further anytime soon.  If somebody else wants to take it up, that would be fantastic.
