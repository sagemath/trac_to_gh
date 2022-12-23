# Issue 400: QuaternionAlgebraWithGramMatrix() does not work

Issue created by migration from https://trac.sagemath.org/ticket/400

Original creator: justin

Original creation time: 2007-07-08 04:17:40

Assignee: was

There are numerous small problems in the code.  The first is that class Matrix is not known in this module.  The second is that is_symmetric() is not defined.  There are others, but this is a start.



---

Comment by justin created at 2007-07-08 04:33:09

HG Bundle with fix


---

Attachment


---

Comment by was created at 2007-08-29 01:37:54

fixes this trac issue


---

Comment by was created at 2007-08-29 01:51:09

Resolution: fixed


---

Attachment

Fixed for sage-2.8.3.
