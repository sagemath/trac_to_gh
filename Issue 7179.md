# Issue 7179: HP-UX sympow-1.018.1.p6 fail to find atoll(). Will atol() do?

archive/issues_007179.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @mkoeppe\n\nKeywords: HP-UX atoll\n\nSee below for the results of an attempted build on HP-UX 11i. Note it cant find the function atoll, which I can't seem to find in any of them system directories on HP-UX 11i. \n\nCould atol() be used instead, or do you really need long long support. Here is the man pages for atoll() on **Solaris**. It *'does not exist on HP-UX 11i*.\n\nA developer can have access to the machine if he/she wishes.  \n\n\n```\n    long atol(const char *str);\n    long long atoll(const char *str);\n\n}}\n\n{{{\n6.spkg ...\n-rw-r--r--   1 drkirkby   users      2201897 Jul 31 22:45 /home/drkirkby/sage-4.1.2.rc0/spkg/standard/sympow-1.018.1.p6.spkg\nFinished extraction\n****************************************************\nHost system\nuname -a:\nHP-UX hpbox B.11.11 U 9000/785 2016698240 unlimited-user license\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: hppa1.1-hp-hpux11.11\nConfigured with: /tmp/gcc-4.4.0.tar.gz/gcc-4.4.0/configure --host=hppa1.1-hp-hpux11.11 --target=hppa1.1-hp-hpux11.11 --build=hppa1.1-hp-hpux11.11 --prefix=/opt/hp-gcc-4.4.0 --with-gnu-as --without-gnu-ld --enable-threads=posix --enable-languages=c,c++ --with-gmp=/proj/opensrc/be/hppa1.1-hp-hpux11.11 --with-mpfr=/proj/opensrc/be/hppa1.1-hp-hpux11.11\nThread model: posix\ngcc version 4.4.0 (GCC)\n****************************************************\nRM = rm\nGREP = grep\nGP = gp\nSED = sed\nSH = sh\nUNAME = uname\nCC = gcc\nYou do not appear to have an x86 based system --- not using fpu.c\nCP = cp\nMKDIR = mkdir\nTOUCH = touch\nTAR = tar\nMakefile has been re-made. Use make if you wish to build SYMPOW\n\n**ATTENTION** If you wish build SYMPOW, please ensure beforehand\nthat the various licenses of your C compiler, linker, assembler, etc.\nallow you to create a derived work based on SYMPOW and your C libraries\n        gcc -O -c analrank.c\n        gcc -O -c analytic.c\n        gcc -O -c compute.c\n        gcc -O -c compute2.c\n        gcc -O -c fpu.c\n        gcc -O -c help.c\n        gcc -O -c conductors.c\n        gcc -O -c disk.c\n        gcc -O -c ec_ap.c\n        gcc -O -c ec_ap_bsgs.c\n        gcc -O -c ec_ap_large.c\n        gcc -O -c eulerfactors.c\n        gcc -O -c factor.c\n        gcc -O -c generate.c\n        gcc -O -c init_curve.c\n        gcc -O -c main.c\n        gcc -O -c moddeg.c\n        gcc -O -c periods.c\n        gcc -O -c prepare.c\n        gcc -O -c QD.c\n        gcc -O -c rootno.c\n        gcc -O -c util.c\n        mkdir -p datafiles\n        touch datafiles/param_data\n        gcc -O3 -O -o sympow  analrank.o analytic.o compute.o compute2.o fpu.o help.o conductors.o disk.o ec_ap.o ec_ap_bsgs.o ec_ap_large.o eulerfactors.o factor.o generate.o init_curve.o main.o moddeg.o periods.o prepare.o QD.o rootno.o util.o\n/usr/ccs/bin/ld: Unsatisfied symbols:\n   atoll (first referenced in init_curve.o) (code)\ncollect2: ld returned 1 exit status\n*** Error exit code 1\n\nStop.\nError building sympow\nTrying again without possibility of using assembler\nRM = rm\nGREP = grep\nGP = gp\nSED = sed\nSH = sh\nUNAME = uname\nCC = gcc\nYou do not appear to have an x86 based system --- not using fpu.c\nCP = cp\nMKDIR = mkdir\nTOUCH = touch\nTAR = tar\nMakefile has been re-made. Use make if you wish to build SYMPOW\n\n**ATTENTION** If you wish build SYMPOW, please ensure beforehand\nthat the various licenses of your C compiler, linker, assembler, etc.\nallow you to create a derived work based on SYMPOW and your C libraries\n        mkdir -p datafiles\n        touch datafiles/param_data\n        gcc -O3 -O -o sympow  analrank.o analytic.o compute.o compute2.o fpu.o help.o conductors.o disk.o ec_ap.o ec_ap_bsgs.o ec_ap_large.o eulerfactors.o factor.o generate.o init_curve.o main.o moddeg.o periods.o prepare.o QD.o rootno.o util.o\n/usr/ccs/bin/ld: Unsatisfied symbols:\n   atoll (first referenced in init_curve.o) (code)\ncollect2: ld returned 1 exit status\n*** Error exit code 1\n\nStop.\nError building sympow (even without assembler)\n\nreal    0m20.982s\nuser    0m19.670s\nsys     0m1.120s\nsage: An error occurred while installing sympow-1.018.1.p6\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /home/drkirkby/sage-4.1.2.rc0/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem yourself, *don't* just cd to\n/home/drkirkby/sage-4.1.2.rc0/spkg/build/sympow-1.018.1.p6 and type 'make'.\nInstead type \"/home/drkirkby/sage-4.1.2.rc0/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/home/drkirkby/sage-4.1.2.rc0/spkg/build/sympow-1.018.1.p6\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\n*** Error exit code 1\n\nStop.\n\nreal    0m26.217s\nuser    0m24.550s\nsys     0m1.430s\nError building Sage.\n\n}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/7179\n\n",
    "created_at": "2009-10-10T09:18:36Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "HP-UX sympow-1.018.1.p6 fail to find atoll(). Will atol() do?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7179",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @mkoeppe

Keywords: HP-UX atoll

See below for the results of an attempted build on HP-UX 11i. Note it cant find the function atoll, which I can't seem to find in any of them system directories on HP-UX 11i. 

Could atol() be used instead, or do you really need long long support. Here is the man pages for atoll() on **Solaris**. It *'does not exist on HP-UX 11i*.

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

Issue created by migration from https://trac.sagemath.org/ticket/7179





---

archive/issue_comments_059354.json:
```json
{
    "body": "I reported this issue upstream by email to Mark Watkins <watkins`@`maths.usyd.edu.au>",
    "created_at": "2009-11-23T00:48:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7179#issuecomment-59354",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I reported this issue upstream by email to Mark Watkins <watkins`@`maths.usyd.edu.au>



---

archive/issue_comments_059355.json:
```json
{
    "body": "Mark thinks atol() may be ok, though it could potentially introduce some limitations, which would in my opinion be undesirable. \n\n[http://p2p.wrox.com/c-programming/16319-string-long-long-without-using-atoll.html](http://p2p.wrox.com/c-programming/16319-string-long-long-without-using-atoll.html)\n\nhas this bit of code which implements atoll()\n\n\n\n```\nlong long my_atoll(char *instr)\n{\n  long long retval;\n  int i;\n\n  retval = 0;\n  for (; *instr; instr++) {\n    retval = 10*retval + (*instr - '0');\n  }\n  return retval;\n}\n```\n",
    "created_at": "2009-11-25T01:18:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7179#issuecomment-59355",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

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

archive/issue_comments_059356.json:
```json
{
    "body": "Changing component from build to porting: AIX or HP-UX.",
    "created_at": "2015-09-08T12:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7179#issuecomment-59356",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from build to porting: AIX or HP-UX.



---

archive/issue_comments_059357.json:
```json
{
    "body": "close as obsolete ?",
    "created_at": "2020-06-25T13:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7179#issuecomment-59357",
    "user": "https://github.com/fchapoton"
}
```

close as obsolete ?



---

archive/issue_comments_059358.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-06-25T13:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7179#issuecomment-59358",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059359.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-06-25T17:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7179#issuecomment-59359",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059360.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-06-25T17:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7179",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7179#issuecomment-59360",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_007398.json:
```json
{
    "actor": "@fchapoton",
    "created_at": "2020-06-25T17:22:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7179",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7179#event-7398"
}
```
