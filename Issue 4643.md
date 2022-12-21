# Issue 4643: build system uses leftover .so files

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-11-28 08:29:39

Assignee: mabshoff

CC:  robertwb

As it stands, if you remove a Cython extension from `module_list.py`, and remove all associated files in the sage library, everything builds fine. However, the `.so` files are still there. In particular, if you try to load a pickled object from a class that was defined in that `.pyx` file, it still loads just fine -- in fact, it loads the `.so` and uses that code. 

Unfortunately, I don't see an easy fix for this offhand. The problem is that we don't manage the `.so` files ourselves -- we leave that to distutils. If someone has a good idea for how to fix this, I'm happy to help implement it.


---

Comment by jdemeyer created at 2014-08-19 14:49:21

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-08-19 14:49:21

Fixed by #16431.


---

Comment by jdemeyer created at 2014-08-19 14:49:26

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-08-20 20:37:36

Resolution: fixed
