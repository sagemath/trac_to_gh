# Issue 8179: configure Mercurial to ignore two binaries by cddlib

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-02-03 19:41:59

Assignee: tbd

CC:  vbraun mhampton

The package cddlib-094f.p?.spkg places two new binaries under the directory $SAGE_LOCAL/bin, in particular:

```
[mvngu`@`mod bin]$ pwd
/scratch/mvngu/release/sage-4.3.2.alpha1/local/bin
[mvngu`@`mod bin]$ hg st
? cdd_both_reps
? cdd_both_reps_gmp
```

These are required by the rewritten polyhedra package at #7109. A patch to $SAGE_LOCAL/bin/.hgignore is attached.


---

Comment by mvngu created at 2010-02-03 19:43:14

apply to script repository


---

Comment by mvngu created at 2010-02-03 19:45:00

Changing status from new to needs_review.


---

Attachment


---

Comment by mvngu created at 2010-02-03 22:11:00

Looks good to me.


---

Comment by mvngu created at 2010-02-03 22:11:00

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-03 22:12:02

Resolution: fixed


---

Comment by mvngu created at 2010-02-03 22:12:02

Merged [trac_8179-cddlib-local-bin-hgignore.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8179/trac_8179-cddlib-local-bin-hgignore.patch). vbraun --- please remember to put your username and the ticket number on your patches. I have committed the above patch in your name.
