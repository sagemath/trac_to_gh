# Issue 9938: Remove unnecessary .hgtags.orig, SConstruct.orig, and hgrc files

Issue created by migration from https://trac.sagemath.org/ticket/9939

Original creator: mpatel

Original creation time: 2010-09-18 00:10:31

Assignee: GeorgSWeber

CC:  mvngu

We can remove

 * `SAGE_ROOT/local/bin/.hg/hgrc`
 * `SAGE_ROOT/devel/sage-main/.hg/hgrc`
 * `SAGE_ROOT/local/bin/.hgtags.orig`
 * `SAGE_ROOT/devel/sage-main/c_lib/SConstruct.orig`

right?


---

Comment by mpatel created at 2010-09-18 00:11:57

Changing assignee from GeorgSWeber to jason.


---

Comment by mpatel created at 2010-09-18 00:11:57

Changing component from build to misc.


---

Comment by mpatel created at 2010-11-16 07:45:15

Can we also delete the (auto-)generated

 * `SAGE_DOC/output`
 * `SAGE_DOC/en/reference/sage`
 * `SAGE_DOC/en/reference/sagenb`

and not include them in `sage-VERSION.spkg`?


---

Comment by jdemeyer created at 2014-02-05 13:13:55

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2014-02-05 13:44:38

New commits:


---

Comment by mmezzarobba created at 2014-02-05 13:44:38

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-02-11 15:14:30

Resolution: fixed
