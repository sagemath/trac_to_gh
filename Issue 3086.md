# Issue 3086: Update R to the 2.7 release and split off rpy.spkg

Issue created by migration from https://trac.sagemath.org/ticket/3086

Original creator: mabshoff

Original creation time: 2008-05-03 03:24:25

Assignee: mabshoff

CC:  jason

R 2.7 is out, so let's upgrade. We should also more rpy to its own top level spkg and update to rpy 1.0.2

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-03 16:58:16

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-03 16:58:16

R 2.6.1 is also broken on FC3:

```
gcc -std=gnu99 -I. -I../../src/include -I../../src/include -I/usr/local/include -DHAVE_CONFIG_H   -fpic  -I/root/sage-3.0/lo
cal/include -L/root/sage-3.0/local/lib/  -c signrank.c -o signrank.o
make[5]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/nmath'
make[4]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/nmath'
make[4]: Entering directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
config.status: creating src/unix/Makefile
make[4]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
make[4]: Entering directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
make[5]: Entering directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
making dynload.d from dynload.c
making edit.d from edit.c
making stubs.d from stubs.c
making system.d from system.c
making sys-unix.d from sys-unix.c
making sys-std.d from sys-std.c
sys-std.c:401:33: readline/readline.h: No such file or directory
sys-std.c:431:32: readline/history.h: No such file or directory
make[5]: *** [sys-std.d] Error 1
make[5]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
make[4]: *** [R] Error 2
make[4]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src/unix'
make[3]: *** [R] Error 1
make[3]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src/src'
make[2]: *** [R] Error 1
make[2]: Leaving directory `/root/sage-3.0/spkg/build/r-2.6.1.p15/src'
Error building R.
```

This is most likely cause by R not using Sage's readline. There is a similar issue with R not picking Sage's libpng, so fix both issues when updating to R 2.7.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-05 03:31:36

See also #3011 about the related RHOME issue.

Cheers,

Michael


---

Comment by jason created at 2009-09-16 13:41:16

Changing status from assigned to new.


---

Comment by jason created at 2009-09-16 13:41:16

Changing assignee from mabshoff to jason.


---

Comment by jason created at 2009-09-16 13:43:13

Also, R has its own C interface---I think rpy2 is using it, but if not, it might make sense for us to just write a Cython wrapper around the C interface.


---

Comment by jason created at 2009-09-17 04:46:01

My draft of an updated R and rpy2 spkg is at 
http://sage.math.washington.edu/home/jason/r-2.9.2.spkg.  There are 
unchecked-in changes in the spkg, and I just ignored a bunch of old 
patches to R because I wasn't sure they applied anymore, so the spkg is 
not finished.


---

Comment by jason created at 2009-09-21 13:15:26

See #6972 for a continuation of the updated spkg above.


---

Comment by mvngu created at 2009-09-22 17:02:49

Closing this ticket as a duplicate of #6972.


---

Comment by mvngu created at 2009-09-22 17:02:49

Resolution: duplicate
