# Issue 7179: HP-UX sympow-1.018.1.p6 fail to find atoll(). Will atol() do?

Issue created by migration from https://trac.sagemath.org/ticket/7179

Original creator: drkirkby

Original creation time: 2009-10-10 09:18:36

Assignee: tbd

CC:  mkoeppe

Keywords: HP-UX atoll

See below for the results of an attempted build on HP-UX 11i. Note it cant find the function atoll, which I can't seem to find in any of them system directories on HP-UX 11i. 

Could atol() be used instead, or do you really need long long support. Here is the man pages for atoll() on *Solaris*. It _'does not exist on HP-UX 11i_.

A developer can have access to the machine if he/she wishes.  


```
    long atol(const char *str);
    long long atoll(const char *str);

}}

{{{
6.spkg ...
-rw-r--r--   1 drkirkby   users      2201897 Jul 31 22:45 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/sympow-1.018.1.p6.spkg
Finished extraction
****************************************************
Host system
uname -a:
HP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: hppa1.1-hp-hpux11.11
Configured with: /tmp/gcc-4.4.0.tar.gz/gcc-4.4.0/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.4.0 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11
Thread model: posix
gcc version 4.4.0 (GCC)
****************************************************
RM = rm
GREP = grep
GP = gp
SED = sed
SH = sh
UNAME = uname
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
        gcc -O -c analrank.c
        gcc -O -c analytic.c
        gcc -O -c compute.c
        gcc -O -c compute2.c
        gcc -O -c fpu.c
        gcc -O -c help.c
        gcc -O -c conductors.c
        gcc -O -c disk.c
        gcc -O -c ec_ap.c
        gcc -O -c ec_ap_bsgs.c
        gcc -O -c ec_ap_large.c
        gcc -O -c eulerfactors.c
        gcc -O -c factor.c
        gcc -O -c generate.c
        gcc -O -c init_curve.c
        gcc -O -c main.c
        gcc -O -c moddeg.c
        gcc -O -c periods.c
        gcc -O -c prepare.c
        gcc -O -c QD.c
        gcc -O -c rootno.c
        gcc -O -c util.c
        mkdir -p datafiles
        touch datafiles/param_data
        gcc -O3 -O -o sympow  analrank.o analytic.o compute.o compute2.o fpu.o help.o conductors.o disk.o ec_ap.o ec_ap_bsgs.o ec_ap_large.o eulerfactors.o factor.o generate.o init_curve.o main.o moddeg.o periods.o prepare.o QD.o rootno.o util.o
/usr/ccs/bin/ld: Unsatisfied symbols:
   atoll (first referenced in init_curve.o) (code)
collect2: ld returned 1 exit status
*** Error exit code 1

Stop.
Error building sympow
Trying again without possibility of using assembler
RM = rm
GREP = grep
GP = gp
SED = sed
SH = sh
UNAME = uname
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
        mkdir -p datafiles
        touch datafiles/param_data
        gcc -O3 -O -o sympow  analrank.o analytic.o compute.o compute2.o fpu.o help.o conductors.o disk.o ec_ap.o ec_ap_bsgs.o ec_ap_large.o eulerfactors.o factor.o generate.o init_curve.o main.o moddeg.o periods.o prepare.o QD.o rootno.o util.o
/usr/ccs/bin/ld: Unsatisfied symbols:
   atoll (first referenced in init_curve.o) (code)
collect2: ld returned 1 exit status
*** Error exit code 1

Stop.
Error building sympow (even without assembler)

real    0m20.982s
user    0m19.670s
sys     0m1.120s
sage: An error occurred while installing sympow-1.018.1.p6
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/drkirkby/sage-4.1.2.rc0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/home/drkirkby/sage-4.1.2.rc0/spkg/build/sympow-1.018.1.p6 and type 'make'.
Instead type "/home/drkirkby/sage-4.1.2.rc0/sage -sh"
in order to set all environment variables correctly, then cd to
/home/drkirkby/sage-4.1.2.rc0/spkg/build/sympow-1.018.1.p6
(When you are done debugging, you can type "exit" to leave the
subshell.)
*** Error exit code 1

Stop.

real    0m26.217s
user    0m24.550s
sys     0m1.430s
Error building Sage.

}}}


---

Comment by drkirkby created at 2009-11-23 00:48:25

I reported this issue upstream by email to Mark Watkins <watkins`@`maths.usyd.edu.au>


---

Comment by drkirkby created at 2009-11-25 01:18:58

Mark thinks atol() may be ok, though it could potentially introduce some limitations, which would in my opinion be undesirable. 

[http://p2p.wrox.com/c-programming/16319-string-long-long-without-using-atoll.html](http://p2p.wrox.com/c-programming/16319-string-long-long-without-using-atoll.html)

has this bit of code which implements atoll()



```
long long my_atoll(char *instr)
{
  long long retval;
  int i;

  retval = 0;
  for (; *instr; instr++) {
    retval = 10*retval + (*instr - '0');
  }
  return retval;
}
```



---

Comment by jdemeyer created at 2015-09-08 12:45:40

Changing component from build to porting: AIX or HP-UX.


---

Comment by chapoton created at 2020-06-25 13:36:18

close as obsolete ?


---

Comment by chapoton created at 2020-06-25 13:36:18

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-06-25 17:10:21

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-06-25 17:22:22

Resolution: invalid
