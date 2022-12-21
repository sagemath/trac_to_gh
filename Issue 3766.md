# Issue 3766: move sage_fortran from fortran spkg to sage_scripts spkg

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-08-03 19:20:53

Assignee: mabshoff

We should move sage_fortran from the fortran spkg to the sage_scripts spkg, since sage packages need this script even if they are not installing the fortran spkg.


---

Comment by kcrisman created at 2012-06-01 18:12:04

Given that there is no longer a fortran spkg, that there is now a `sage_fortran` script in local/bin, and that this ticket hasn't had a comment in four years, I am recommending closure.


---

Comment by kcrisman created at 2012-06-01 18:12:04

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-07-05 16:16:51

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-07-05 16:16:51

Yeah, this should work properly fine now, and this was done already in that move.  Closing.


---

Comment by jdemeyer created at 2012-07-06 08:32:32

Resolution: invalid
