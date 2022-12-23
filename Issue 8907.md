# Issue 8907: build Python as a shared library

Issue created by migration from https://trac.sagemath.org/ticket/8907

Original creator: mhansen

Original creation time: 2010-05-06 17:10:55

Assignee: AlexGhitza

This is needed by #8542 .  There is an spkg at http://sage.math.washington.edu/home/mhansen/python-2.6.4.p8.spkg but it requires lots of testing.  Also, the changes are not committed to the repository.


---

Comment by mhansen created at 2010-05-06 17:11:26

Changing component from algebra to cygwin.


---

Comment by mhansen created at 2010-05-06 17:11:26

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-05-06 17:57:28

Check on OS X, we don't need --enable-shared.  I'm check on t2 now.  The spkg will have to be updated accordingly.


---

Comment by mhansen created at 2010-05-25 05:47:26

--enabled-shared fails on t2 because of http://bugs.python.org/issue1628484 .  We need to apply the patch there.


---

Comment by was created at 2010-05-26 00:44:22

Resolution: fixed
