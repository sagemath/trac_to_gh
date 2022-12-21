# Issue 5774: running "make" on a -bdisted binary is broken

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-04-13 07:47:47

Assignee: mabshoff

To reproduce this build Sage, bdist, unpack the binary in a new place and run *make*':

```
mabshoff`@`sage:/scratch/mabshoff/sage-3.4.1.rc3$ make
cd spkg && ./install all 2>&1 | tee -a ../install.log
/bin/ls: cannot access bzip2-*-install: No such file or directory
/bin/ls: cannot access dir-*-install: No such file or directory
/bin/ls: cannot access prereq-*-install: No such file or directory
make[1]: Entering directory `/scratch/mabshoff/sage-3.4.1.rc3/spkg'
standard/deps:42: warning: overriding commands for target `installed/'
standard/deps:39: warning: ignoring old commands for target `installed/'
standard/deps:45: warning: overriding commands for target `installed/'
standard/deps:42: warning: ignoring old commands for target `installed/'
standard/deps:177: warning: overriding commands for target `installed/'
standard/deps:45: warning: ignoring old commands for target `installed/'
make[1]: Circular installed/python-2.5.2.p9 <- installed/ dependency dropped.
make[1]: Circular installed/python-2.5.2.p9 <- installed/ dependency dropped.
make[1]: Circular installed/python-2.5.2.p9 <- installed/ dependency dropped.
make[1]: Circular installed/zlib-1.2.3.p4 <- installed/ dependency dropped.
make[1]: Circular installed/zlib-1.2.3.p4 <- installed/ dependency dropped.
make[1]: Circular installed/zlib-1.2.3.p4 <- installed/ dependency dropped.
make[1]: Circular installed/termcap-1.3.1.p0 <- installed/ dependency dropped.
make[1]: Circular installed/termcap-1.3.1.p0 <- installed/ dependency dropped.
make[1]: Circular installed/termcap-1.3.1.p0 <- installed/ dependency dropped.
make[1]: Circular installed/readline-5.2.p6 <- installed/ dependency dropped.
make[1]: Circular installed/readline-5.2.p6 <- installed/ dependency dropped.
make[1]: Circular installed/readline-5.2.p6 <- installed/ dependency dropped.
make[1]: Circular installed/libpng-1.2.35 <- installed/ dependency dropped.
make[1]: Circular installed/libpng-1.2.35 <- installed/ dependency dropped.
make[1]: Circular installed/libpng-1.2.35 <- installed/ dependency dropped.
make[1]: Circular installed/ <- installed/ dependency dropped.
make[1]: Circular installed/ <- installed/ dependency dropped.
make[1]: Circular installed/ <- installed/ dependency dropped.
```


This is due to the directory *$SAGE_ROOT/spkg/base* not being picked up by -bdist.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-21 23:37:14

Well, this is only an issue of annoyance, so bumping it to 3.4.2.

Cheers,

Michael


---

Comment by was created at 2009-06-15 23:24:33

As a mere annoyance, it doesn't make sense to keep it as a blocker.


---

Comment by was created at 2009-06-15 23:24:33

Changing priority from blocker to critical.


---

Comment by jdemeyer created at 2012-05-17 22:02:08

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2012-05-17 22:02:08

This doesn't happen anymore.


---

Comment by jdemeyer created at 2012-05-17 22:02:17

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-05-21 08:05:59

Resolution: worksforme
