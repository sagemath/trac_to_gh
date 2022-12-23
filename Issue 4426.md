# Issue 4426: Do not hard code RTLD_GLOBAL as 256 for libSingular

Issue created by migration from https://trac.sagemath.org/ticket/4426

Original creator: mabshoff

Original creation time: 2008-11-02 19:20:12

Assignee: mabshoff

CC:  malb

We currently hard code RTLD_GLOBAL as 256 when we dlopen libSingular. This is not true on AIX and Cygwin for example, so we should pull the value in from the system's dlfcn.h.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-02 19:25:33

Resolution: duplicate


---

Comment by mabshoff created at 2008-11-02 19:25:33

Ha, malb and I opened a ticket for the same issue, but since #4427 has a patch close this as a dupe.

Cheers,

Michael
