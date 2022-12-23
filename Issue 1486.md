# Issue 1486: singular-3-0-4-1-20071202 fails compilation on Slackware 12.0

Issue created by migration from https://trac.sagemath.org/ticket/1486

Original creator: mabshoff

Original creation time: 2007-12-13 17:18:12

Assignee: malb

Reported by John A. Murdie:

```
make[4]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/
singular-3-0-4-1-20071202/src/kernel'
make install in Singular
make[4]: Entering directory `/local/d0p6/john/sage-2.8.15/spkg/build/
singular-3-0-4-1-20071202/src/Singular'
...
g++ -fPIC -O3 -g -pipe -fno-implicit-templates -I. -I../kernel -I/
local/d0p6/john/sage-2.8.15/local/include  -DNDEBUG -DOM_NDEBUG -
Dix86_Linux -DHAVE_CONFIG_H -c walk_ip.cc
g++ -fPIC -O3 -g -pipe -fno-implicit-templates -I. -I../kernel -I/
local/d0p6/john/sage-2.8.15/local/include  -DNDEBUG -DOM_NDEBUG -
Dix86_Linux -DHAVE_CONFIG_H -c cntrlc.cc
/usr/include/asm/sigcontext.h:20: error: redefinition of 'struct
_fpreg'
/usr/include/bits/sigcontext.h:29: error: previous definition of
'struct _fpreg'
/usr/include/asm/sigcontext.h:25: error: redefinition of 'struct
_fpxreg'
/usr/include/bits/sigcontext.h:35: error: previous definition of
'struct _fpxreg'
/usr/include/asm/sigcontext.h:31: error: redefinition of 'struct
_xmmreg'
/usr/include/bits/sigcontext.h:42: error: previous definition of
'struct _xmmreg'
/usr/include/asm/sigcontext.h:35: error: redefinition of 'struct
_fpstate'
/usr/include/bits/sigcontext.h:51: error: previous definition of
'struct _fpstate'
/usr/include/asm/sigcontext.h:59: error: redefinition of 'struct
sigcontext'
/usr/include/bits/sigcontext.h:82: error: previous definition of
'struct sigcontext'
make[4]: *** [cntrlc.o] Error 1
make[4]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/
singular-3-0-4-1-20071202/src/Singular'
make[3]: *** [install] Error 1
make[3]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/
singular-3-0-4-1-20071202/src'
make[2]: *** [/local/d0p6/john/sage-2.8.15/local/bin/Singular-3-0-4]
Error 2
make[2]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg/build/
singular-3-0-4-1-20071202/src'
Unable to build Singular.
...
sage: An error occurred while installing singular-3-0-4-1-20071202
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /local/d0p6/john/sage-2.8.15/install.log.  Describe your computer,
operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/local/d0p6/john/sage-2.8.15/spkg/build/singular-3-0-4-1-20071202 and
type 'make'.
Instead type "/local/d0p6/john/sage-2.8.15/sage -sh"
in order to set all environment variables correctly, then cd to
/local/d0p6/john/sage-2.8.15/spkg/build/singular-3-0-4-1-20071202
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/singular-3-0-4-1-20071202] Error 1
make[1]: Leaving directory `/local/d0p6/john/sage-2.8.15/spkg' 
```


Cheers,

Michal


---

Comment by mabshoff created at 2007-12-14 23:04:05

Hans Schöneman from the Singular team suggest a fix that worked. It is part of 

http://sage.math.washington.edu/home/mabshoff/singular-3-0-4-1-20071209.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-15 01:03:06

Resolution: fixed


---

Comment by mabshoff created at 2007-12-15 01:03:06

Merged in 2.9.rc0.
