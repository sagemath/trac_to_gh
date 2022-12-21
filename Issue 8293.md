# Issue 8293: Include g77

Issue created by migration from Trac.

Original creator: magawake

Original creation time: 2010-02-17 12:36:02

Assignee: GeorgSWeber

CC:  magawake@gmail.com

I am not sure if this already exists but it would be nice if we can include the fortran compiler into the sage distribution. 

When packages like BLAS depend on fortran and other packages such as Octave prefer to use the same compiler.


---

Comment by mvngu created at 2010-02-17 14:19:47

Something important as this should be raised in the sage-devel mailing list. Sage previously had Fortran binaries for Linux, but then the binaries were dropped. You need to make the proposal in the sage-devel mailing list.


---

Comment by kcrisman created at 2013-04-26 01:47:31

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-04-26 01:47:31

This has essentially been done with the gcc spkg, right?


---

Comment by jdemeyer created at 2013-05-08 22:11:19

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-09 18:24:41

Resolution: wontfix
