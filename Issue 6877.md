# Issue 6877: Boolean function for crypto, small bugfixes and improvement

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-09-03 12:21:59

Assignee: somebody

CC:  malb

Not even in sage, but already a bug fix...

The bug comes from the different ordering for enumerating finite fields depending on the implementation (givaro or ntl in this case).

The improvements are:

- an option to output the truth table in hexadecimal
- the computation of the algebraic normal form


---

Attachment


---

Comment by ylchapuy created at 2009-09-03 12:26:41

you need to apply #6514 (both patches) first


---

Comment by malb created at 2009-09-03 14:22:48

*Review*
 * patch looks good
 * applies cleanly against 4.1.1 + #6514
 * doctests pass on sage.math


---

Comment by mvngu created at 2009-09-03 21:39:36

Resolution: fixed
