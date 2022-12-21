# Issue 8091: sympow builds 32-bit mode on Open Solaris x64

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-27 04:49:30

Assignee: drkirkby

CC:  jas

## Build environment
 * Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
 * OpenSolaris 2009.06 snv_111b X86
 * Sage 4.3.1 (with a few packages hacked to work on 64-bit)
 * gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
 * 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. 

## The problem

```
sympow-1.018.1.p6/.hgignore
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_111b i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.3.4 (GCC) 
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
make[2]: Entering directory `/export/home/drkirkby/sage-4.3.1/spkg/build/sympow-1.018.1.p6/src'
gcc -O3   -c -o analrank.o analrank.c
gcc -O3   -c -o analytic.o analytic.c
```


It does finally build, but obviously as a 32-bit object, not a 64-bit one. 

It believes the hardware is not x86. so disables the assembly. This is untrue of course, as this is an Intel Xeon processor. 


---

Comment by jsp created at 2010-02-01 19:47:52

I also have a 32 bit executable. I wonder is this a real problem.

Tachyon builds as a 32 bit executable too. But runs as well.



```
jaap`@`opensolaris:~/Downloads/sage-4.3.2.alpha0/local$  find . -exec file {} \; | grep "ELF 32"
./bin/tachyon:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, stripped
./bin/size222:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped, no debugging information available
./bin/class.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
./bin/nef.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
./bin/poly.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
./bin/dikcube:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped, no debugging information available
./bin/cws.x:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
./lib/omalloc.o:	ELF 32-bit LSB relocatable 80386 Version 1
./lib/sympow/sympow:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
./lib/omalloc_debug.o:	ELF 32-bit LSB relocatable 80386 Version 1
jaap`@`opensolaris:~/Downloads/sage-4.3.2.alpha0/local$ 


```



Jaap


---

Comment by drkirkby created at 2010-08-12 14:30:02

Resolution: fixed


---

Comment by drkirkby created at 2010-08-12 14:30:02

sympow seems to still present its fair share of problems on Solaris 10 x86 (#9703), Cygwin amd OpenSolaris, but this particular problem was fixed by #9029 in sage-4.4.4.
