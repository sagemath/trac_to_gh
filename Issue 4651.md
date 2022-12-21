# Issue 4651: re-enable caching of cython dependencies during build

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-11-29 07:05:55

Assignee: craigcitro

We decided to temporarily disable the caching of the cython dependencies during the build, simply because it was causing so much grief. However, this should be re-enabled once someone takes the time to sit down and work out the last kinks. In particular, *removing* files from the sage tree and rebuilding tends to cause exceptions.

See `$SAGE_ROOT/devel/sage/setup.py` for some comments, and to play with this.


---

Comment by jdemeyer created at 2013-05-19 13:09:12

Dependency checking is in upstream Cython now.


---

Comment by jdemeyer created at 2013-05-19 13:09:12

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-05-19 13:09:17

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-21 07:24:08

Resolution: invalid
