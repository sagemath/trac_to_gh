# Issue 7903: mixing a non-GNU Fortran compiler with GCC is not detected very early

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-12 06:42:07

Assignee: GeorgSWeber

Mixing compilers (say GNU and Sun), should not be permitted. There is code in prereq which carefully checks this for C and C++ compilers, and even checks the version numbers for gcc. But for Fortran the checks are not as well done. 

Mixing Sun Studio compilers with gfortran is detected in readline, but it should be done earlier. 

I'm the one to blame for this, as I've updated 'prereq' a few times. That said, it will catch a lot more errors than it used to do. 

Dave 


---

Comment by mvngu created at 2010-01-31 22:33:43

Resolution: fixed


---

Comment by mvngu created at 2010-01-31 22:33:43

Close as fixed by #8052.
