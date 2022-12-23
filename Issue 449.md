# Issue 449: lrank Solaris build fixes

Issue created by migration from https://trac.sagemath.org/ticket/449

Original creator: mabshoff

Original creation time: 2007-08-19 07:49:45

Assignee: mabshoff

* spkg-install: needs sh compability fix: DEFINES=""; export DEFINES
* llrint workaround needed for SunOS:
  #define llrint(d) ((long long)rint(d))
* ./include/getopt.h: line 147: do not define "extern int getopt ();"
on Solaris
* needs -liberty for symbol getopt_long when __sun is defined

In general: The Makefile sucks:

g++  -DINCLUDE_PARI   \
      -I/extra/home/mabshoff/SAGE-build/sage-2.8/local/include/pari \
      -I/extra/home/mabshoff/SAGE-build/sage-2.8/local/include \
      -I ../include/ -L/extra/home/mabshoff/SAGE-build/sage-2.8/local/
lib \
      cmdline.c \
      Lcommandline.cc Lcommandline_elliptic.cc Lcommandline_globals.cc
\
      Lcommandline_misc.cc Lcommandline_numbertheory.cc \
      Lcommandline_twist.cc Lcommandline_values_zeros.cc \
      Lgamma.cc Lglobals.cc Lmisc.cc Lriemannsiegel.cc \
            -o lcalc -lpari -lmpfr -lgmpxx -lgmp -liberty

Cleanup:
* compile each file individually
* crush gcc 4.2 warnings about const string to char*


---

Comment by mabshoff created at 2007-08-22 19:38:20

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-27 17:28:03

See also #932 and #1626.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-26 00:11:45

There are now patches at #1626 which fix the issue. This ticket can be closed once #1626 is merged.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-14 03:57:39

Fixed since #1626 has been merged in Sage 3.0.alpha5.


---

Comment by mabshoff created at 2008-04-14 03:57:39

Resolution: fixed
