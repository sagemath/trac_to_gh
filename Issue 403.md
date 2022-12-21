# Issue 403: polymake deadlocks from popen3 call

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2007-07-12 11:43:48

Assignee: was

Keywords: polymake, polytope

When doing large enough calculations, popen3 deadlocks in the cmd method of the Polytope class.  The attached patch fixes this by using the subprocess module instead.


---

Attachment


---

Comment by was created at 2007-08-23 01:46:28

Changing priority from major to minor.


---

Comment by was created at 2007-08-23 01:46:28

I changed the priority to minor because polymake is an optional package.


---

Comment by was created at 2007-08-29 01:55:33

This is applied now for sage-2.8.3.


---

Comment by was created at 2007-08-29 01:55:33

Resolution: fixed
