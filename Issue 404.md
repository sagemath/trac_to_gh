# Issue 404: Can't create PSL(n,q) for q a prime power

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2007-07-19 23:57:34

Assignee: was

Somewhere along the line :-}, we added a requirement that GF(p^r) had to be created with a generator.
The code to create PSL(n,q) doesn't do this.



---

Comment by was created at 2007-07-27 19:35:44

Changing component from algebraic geometry to basic arithmetic.


---

Attachment

The patch trac404.patch fixes this bug, plus some related ones and adds doctests.
This will be in SAGE-2.7.2.

William


---

Comment by was created at 2007-07-27 19:35:44

Changing assignee from was to somebody.


---

Comment by was created at 2007-07-27 19:35:48

Resolution: fixed
