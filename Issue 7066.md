# Issue 7066: sympow ignores CC and uses gcc even when CC is set to Sun's compiler

Issue created by migration from https://trac.sagemath.org/ticket/7066

Original creator: drkirkby

Original creation time: 2009-09-29 12:42:13

Assignee: tbd

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used (#7021) 

Despite CC being set to Sun's compiler, sympow ignores this. 


```
sympow-1.018.1.p6/src/Configure
sympow-1.018.1.p6/.hgignore
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
RM = rm
GREP = grep
GP = gp
SED = sed
SH = sh
UNAME = uname
using gcc
CC = gcc
You do not appear to have an x86 based system --- not using fpu.c
CP = cp
MKDIR = mkdir
TOUCH = touch
TAR = tar
Makefile has been re-made. Use make if you wish to build SYMPOW

**ATTENTION** If you wish build SYMPOW, please ensure beforehand
that the various licenses of your C compiler, linker, assembler, etc.
allow you to create a derived work based on SYMPOW and your C libraries
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/sympow-1.018.1.p6/src'
gcc -O3   -c -o analrank.o analrank.c
gcc -O3   -c -o analytic.o analytic.c
gcc -O3   -c -o compute.o compute.c
gcc -O3   -c -o compute2.o compute2.c
```



---

Comment by drkirkby created at 2009-11-09 14:04:25

Changing component from algebra to solaris.


---

Comment by mjo created at 2012-02-10 06:06:31

It looks like Jeroen took care of this in the last sympow bump, #11920.


---

Comment by mjo created at 2012-02-10 06:06:31

Changing status from new to needs_review.


---

Comment by ohanar created at 2012-03-18 01:12:19

Changing status from needs_review to positive_review.


---

Comment by ohanar created at 2012-03-18 01:12:19

Changing keywords from "" to "rd2".


---

Comment by ohanar created at 2012-03-18 01:12:19

yup, that appears to be the case


---

Comment by jdemeyer created at 2012-03-21 11:36:43

Resolution: worksforme
