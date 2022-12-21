# Issue 8068: New mpfr-2.4.1.p1.spkg works with Open Solaris 64 bit

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-01-25 23:41:29

Assignee: drkirkby

CC:  drkirby was

Let spkg-install handle SAGE64="yes" on Open Solaris 65 bit.


See here:
[http://boxen.math.washington.edu/home/jsp/ports/mpfr-2.4.1.p1.spkg](http://boxen.math.washington.edu/home/jsp/ports/mpfr-2.4.1.p1.spkg)




```
PASS: tpow_all
====================
All 148 tests passed
====================
make[2]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src/tests'
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src/tests'
make[1]: Entering directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src'
make[1]: Nothing to be done for `check-am'.
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.1/spkg/build/mpfr-2.4.1.p1/src'

real	2m15.371s
user	1m22.294s
sys	0m54.607s
Successfully installed mpfr-2.4.1.p1

```


Jaap


---

Comment by jsp created at 2010-01-25 23:41:43

Changing status from new to needs_review.


---

Attachment


---

Comment by drkirkby created at 2010-01-27 12:42:05

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-27 12:42:05

Changing type from enhancement to defect.


---

Comment by drkirkby created at 2010-01-27 12:42:05

This works fine. In fact, the library was already building 64-bit for me, without this patch, but I believe it is safer to have this. I suspect mpfr might actually ignore the CFLAGS and work out what it needs itself, as it is uses mpir, and that would already be configured 64-bit. But I would agree this is desirable to add this. 

Positive review.


---

Comment by mpatel created at 2010-02-11 15:17:33

Resolution: fixed
