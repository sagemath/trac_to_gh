# Issue 7970: Make `hg` interfaces use `subprocess.Popen` and return exit code

Issue created by migration from https://trac.sagemath.org/ticket/7970

Original creator: craigcitro

Original creation time: 2010-01-17 23:48:44

Assignee: GeorgSWeber

CC:  mhansen

As mentioned on #7760, it would be nice if the `hg_sage`, etc. returned the exit code from the `__call__` method. We'd have to switch `os.popen3` to `subprocess.Popen` to do this, which isn't so bad, and is worth it in the long run (since `os.popen3` is deprecated). 


---

Comment by jdemeyer created at 2013-12-19 12:08:47

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-12-19 12:08:54

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2013-12-19 22:37:36

Resolution: wontfix
