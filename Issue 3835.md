# Issue 3835: Make an algebraic closure function

Issue created by migration from https://trac.sagemath.org/ticket/3835

Original creator: jason

Original creation time: 2008-08-13 15:03:21

Assignee: tbd

CC:  ncalexan

It would be nice to be able to construct the algebraic closure of an object.  For example, QQ.algebraic_closure() should return QQbar.


---

Comment by cremona created at 2009-08-30 20:34:29

Applies to 4.1.1


---

Attachment

The attached patch implements this in the trivial cases now possible:  for a number field (including QQ) return QQbar;  for RR return CC, with the same precision (this was already implemented);  for CC, return the same field;  for finite fields, raise NotImplementedError; else raise NotImplementedError.

I'm not sure if this is what Jason intended, but it would be a major undertaking to implement this in any other cases (finite fields, p-adic fields, function fields. ...)


---

Comment by cremona created at 2009-08-30 20:36:33

Changing keywords from "" to "fields".


---

Comment by jason created at 2009-08-31 13:05:37

My use-case at the time was QQ -> QQbar, I think.


---

Comment by mhansen created at 2009-09-08 03:06:36

Looks good to me.


---

Comment by mvngu created at 2009-09-08 10:17:08

Resolution: fixed
