# Issue 1981: NTL fails to build with DEB_BUILD_HARDENING=1

Issue created by migration from https://trac.sagemath.org/ticket/1981

Original creator: malb

Original creation time: 2008-01-30 10:34:24

Assignee: mabshoff

Error message:


```
ld.real: FFT.o: relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC
FFT.o: could not read symbols: Bad value
collect2: ld returned 1 exit status
make[3]: *** [libntl.so] Error 1
make[3]: Leaving directory `/tmp/sage-2.10.1.rc2-hardening-wrapper/spkg/build/ntl-5.4.1.p10/src/src'
make[2]: *** [lib] Error 2
make[2]: Leaving directory `/tmp/sage-2.10.1.rc2-hardening-wrapper/spkg/build/ntl-5.4.1.p10/src/src'
Error creating ntl shared library.
```


How to reproduce (Debian only!):

```
apt-get install hardening-wrapper
export DEB_BUILD_HARDENING=1
cd <SAGE_ROOT>
make
```


See http://wiki.debian.org/Hardening and http://lists.debian.org/debian-devel-announce/2008/01/msg00006.html for rationale of hardening. 



---

Comment by jdemeyer created at 2013-06-13 12:33:36

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2013-06-13 12:33:36

Very outdated.


---

Comment by jdemeyer created at 2013-06-13 12:33:43

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-06-19 12:21:13

Resolution: invalid
