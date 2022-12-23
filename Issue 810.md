# Issue 810: [with patch] gens_reduced for general ideals

Issue created by migration from https://trac.sagemath.org/ticket/810

Original creator: dmharvey

Original creation time: 2007-10-03 16:39:57

Assignee: was

It's annoying that number field ideals have a `gens_reduced()` method, but ideals of ZZ do not. This patch fixes this by adding a `gens_reduced()` method to the base ideal class, whose default implementation just calls `gens()`.



---

Attachment


---

Comment by was created at 2007-10-04 15:15:23

Resolution: fixed
