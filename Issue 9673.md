# Issue 9673: Referring to flag for doc-testing only changed files

Issue created by migration from Trac.

Original creator: jsrn

Original creation time: 2010-08-03 07:56:52

Assignee: mvngu

CC:  chapoton

Keywords: doctest

In the Developer's Guide there is no reference to the "-tnew" flag to the sage executable, which will instruct Sage to only doctest changed files. I suggest adding such a reference in "Walking through the development process" as well as "Parallel Testing the Sage Library".


---

Comment by jsrn created at 2010-08-03 07:59:21

Does anyone know how the "-tnew" flag works in detail? In particular, does it doctest every file that has been changed _as well as its dependencies_? If it is the case, this should be mentioned in the documentation. Otherwise, shouldn't it?


---

Comment by jsrn created at 2010-08-03 08:04:48

Of course, the above shouldn't say "its dependencies" but rather "the files depending on them".


---

Comment by jmantysalo created at 2016-04-22 10:43:08

This has been done, see http://doc.sagemath.org/html/en/developer/doctesting.html#testing-changed-files, so I suggest this one to be closed. Frédéric, please click _positive_review_ if you agree.


---

Comment by jmantysalo created at 2016-04-22 10:43:08

Changing status from new to needs_review.


---

Comment by chapoton created at 2016-04-22 11:32:44

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-06-12 12:02:30

Resolution: fixed
