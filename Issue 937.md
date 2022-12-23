# Issue 937: If g is a graphics object then in doctest mode g.show() should save to a specific (always the same) temp file.

Issue created by migration from https://trac.sagemath.org/ticket/937

Original creator: was

Original creation time: 2007-10-20 03:17:10

Assignee: failure

Do what the summary says.  Then fix every single .show() related plot doctest to do this in all Sage.
There are many cases of either sage.: show's and .save('a.png')'s.  


---

Comment by was created at 2007-10-20 05:04:06

Resolution: fixed


---

Comment by was created at 2007-10-20 05:04:06

ok, I fixed this for the upcoming release.
