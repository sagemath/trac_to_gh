# Issue 8298: GLPK 4.42 + error message

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2010-02-18 14:03:46

Assignee: tbd

CC:  schilly mvngu

The user has to run sage -b after installing GLPK or CBC because of recent modifications in the mip.pyx file.... As he may not be aware of it, Harald Schilly suggested a *** LARGE *** message, which will be printed after the package is installed.

On the way, I also updated the sources of glpk, as the most recent is the 4.42 while we were using 4.38

It can be downloaded on sage.math at :

~/ncohen/glpk-4.42.p0.spkg

* The package 4.38 will have to be removed when this one is made available *

Nathann


---

Comment by ncohen created at 2010-02-27 13:30:50

Changing status from new to needs_review.


---

Comment by dimpase created at 2010-04-09 08:03:26

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2010-04-09 08:03:26

Replying to [comment:1 ncohen]:

OK, works (Linux x86_64 Debian, and Sparc Solaris 2.10), doctests pass, positive review.


---

Comment by jhpalmieri created at 2010-04-20 22:55:49

Merged 2010/04/20.


---

Comment by jhpalmieri created at 2010-04-20 22:55:49

Resolution: fixed
