# Issue 7442: Update scipy to the latest version (0.7.1)

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-11-12 07:05:11

Assignee: tbd

CC:  jason




---

Comment by jason created at 2009-11-12 07:22:43

spkg up at http://sage.math.washington.edu/home/jason/scipy-0.7.1.spkg


---

Comment by jason created at 2009-11-12 07:22:43

Changing status from new to needs_review.


---

Comment by jason created at 2010-01-20 08:48:14

The exact same issue is addressed in #6914.


---

Comment by timdumol created at 2010-01-20 10:46:24

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-20 10:46:24

LGTM.


---

Comment by mvngu created at 2010-01-24 23:48:08

The package [scipy-0.7.1.spkg](http://sage.math.washington.edu/home/jason/scipy-0.7.1.spkg) contains some changes not yet checked in:

```
[mvngu`@`sage scipy-0.7.1]$ hg status
? .copy_patches.pl.swp
? patches/setup.py.special.orig
```

Is `patches/setup.py.special.orig` meant to be under revision control? The file `.copy_patches.pl.swp` looks like a junk file. If so, it needs to be deleted.


---

Comment by mpatel created at 2010-02-10 11:03:48

Changing status from positive_review to needs_work.


---

Comment by jason created at 2011-10-18 18:32:20

Resolution: invalid


---

Comment by jason created at 2011-10-18 18:32:20

Somehow we are at scipy 0.9 now, so this ticket should be closed as invalid now.
