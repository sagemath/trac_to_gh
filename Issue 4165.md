# Issue 4165: Doctest for lisp.py blows chunks on (some) Mac OS X systems

Issue created by migration from https://trac.sagemath.org/ticket/4165

Original creator: justin

Original creation time: 2008-09-22 02:03:51

Assignee: mabshoff

I have seen this on two Mac OS X systems, with 3.1.2 (but not 3.1.1):
 - Core Duo (10.5.5)
 - Dual Quad Xeon (10.5.4)

This is an "Expected/Got" problem.  The output from the test is 


```
sage -t  devel/sage/sage/interfaces/lisp.py 
**************************************************
File "/SandBox/Justin/sb/sage-3.1.2/tmp/lisp.py", line 290:
     sage: lisp.version()
Expected:
     GNU CLISP ... (...) (built ...) (memory ...)
     ...
Got:
     GNU CLISP 2.46 (2008-07-02) (built on Hasse-2.local [10.0.1.200])
     Software: GNU C 4.0.1 (Apple Inc. build 5465)
     gcc -O0 -g -I/SandBox/Justin/sb/sage-3.1.2/local/include/ -L/
SandBox/Justin/sb/sage-3.1.2/local/lib/ -W -Wswitch -Wcomment -
Wpointer-arith -Wimplicit -Wreturn-type -Wmissing-declarations -Wno-
sign-compare -O0 -fexpensive-optimizations -falign-functions=4 -
DUNIX_BINARY_DISTRIB -DUNICODE -DNO_SIGSEGV -I. -x none -lintl -Wl,-
framework -Wl,CoreFoundation -lreadline -lncurses  -liconv
     SAFETY=0 HEAPCODES STANDARD_HEAPCODES SPVW_BLOCKS SPVW_MIXED  
TRIVIALMAP_MEMORY
     libiconv 1.11
     libreadline 5.2
     Features:
     (REGEXP SYSCALLS I18N LOOP COMPILER CLOS MOP CLISP ANSI-CL COMMON-
LISP LISP=CL
      INTERPRETER SOCKETS GENERIC-STREAMS LOGICAL-PATHNAMES SCREEN  
GETTEXT UNICODE
      BASE-CHAR=CHARACTER UNIX MACOS)
     C Modules: (clisp i18n syscalls regexp)
     Installation directory: /SandBox/Justin/sb/sage-3.1.2/local/lib/
clisp-2.46/
     User language: ENGLISH
     Machine: I386 (I386) Hasse-2.local [127.0.0.1]
     <BLANKLINE>
**********************************************************************
```



---

Attachment

Justin,

can you test this patch?

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-22 03:56:32

Changing status from new to assigned.


---

Comment by justin created at 2008-09-22 04:23:30

I tried this out in 3.1.2; haven't leapt into the 3.1.3 morass yet.  Works like it oughtta!


---

Comment by mabshoff created at 2008-09-22 04:25:37

I assume his is a positive review then? lisp.py has not changed in 3.1.3.alpha0, so this ought to work.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-23 00:05:48

Resolution: fixed


---

Comment by mabshoff created at 2008-09-23 00:05:48

Merged in Sage 3.1.3.alpha1
