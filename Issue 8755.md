# Issue 8755: modify sagenb-*/src/sagenb/spkg-dist to produce valid spkg's

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-24 21:38:40

Assignee: jason, was

The spkg format for Sage requires that:

   (1) the sagenb-*/ directory (that contains spkg-install, SPKG.txt, etc.) has its own hg report, which has spkg-install and SPKG.txt checked in.

   (2) SPKG.txt gets regularly updated with a log message for each new spkg release.

The goal of this ticket it to change the file src/sagenb/spkg-dist, so that when it it run to create a new spkg, the resulting spkg is *valid* as explained above.  That's it. 


---

Comment by kcrisman created at 2014-09-17 02:16:31

This is no longer valid given all the changes in how sagenb is incorporated in Sage.


---

Comment by kcrisman created at 2014-09-17 02:16:31

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-09-17 02:16:41

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-09-18 17:59:02

Resolution: invalid
