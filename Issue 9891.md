# Issue 9891: Eliminate (or minimize) #include <pari/paripriv.h>

Issue created by migration from https://trac.sagemath.org/ticket/9892

Original creator: jdemeyer

Original creation time: 2010-09-10 21:26:38

Assignee: tbd

The file `include/pari/paripriv.h` is supposed to contain functions which are meant to be used only by PARI/GP itself.  One should check whether the use of `paripriv.h` can be eliminated.  If so, we can also remove the patch for `paripriv.h` for the pari spkg.


---

Comment by jdemeyer created at 2010-09-14 07:50:22

Changing component from packages to interfaces.


---

Comment by jdemeyer created at 2010-09-14 07:50:22

Changing assignee from tbd to was.


---

Comment by jdemeyer created at 2015-09-23 10:01:55

Changing assignee from was to jdemeyer.


---

Comment by jdemeyer created at 2015-09-23 10:01:55

Changing component from interfaces to cython.


---

Comment by jdemeyer created at 2015-09-23 11:08:12

New commits:


---

Comment by jdemeyer created at 2015-09-23 11:08:12

Changing status from new to needs_review.


---

Comment by chapoton created at 2016-03-08 12:55:27

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2016-03-08 12:55:27

ok, the bot is happy.


---

Comment by vbraun created at 2016-03-08 23:30:54

Resolution: fixed
