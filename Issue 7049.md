# Issue 7049: [with SPKG, needs review] GLPK, just minor changes

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-09-28 09:29:21

Assignee: tbd

CC:  mvngu

Hello !!!

Because of #7012, some functions in numerical.mip had to be renamed, and this package had to be modified as it uses them.

These are the only changes contained in the package located on : ~ncohen/glpk-4.38.p2.spkg (sagemath).


---

Comment by ncohen created at 2009-10-02 16:24:50

I just updated the SPKG. In ticket #7012, variable sense had been changed to maximization, and it had to be mentionned here.


---

Comment by mvngu created at 2009-10-21 22:31:59

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2009-10-21 22:31:59

Looks good. This should be merged in the optional packages repository.


---

Comment by mhansen created at 2009-10-23 09:09:51

Resolution: fixed
