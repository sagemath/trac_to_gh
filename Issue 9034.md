# Issue 9034: flintqs builds as 32-bit despite SAGE64=yes on OpenSolaris x64

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-24 11:54:06

Assignee: drkirkby

CC:  jsp

## Build environment
 * Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
 * OpenSolaris 2009.06 snv_111b X86
 * Sage 4.4.2
 * gcc 4.4.4

## How gcc 4.4.4 was configured
Since the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. 


```
drkirkby`@`hawk:~/sage-4.4.2$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
```


gcc 4.3.4 was failing to build iconv on OpenSolaris x64, suggesting it may be essential to have a very recent gcc in order to build Sage on OpenSolaris. 

## How the Sage build was attempted
 * 64-bit build. SAGE64 was set to "yes"
 * #9008 update zlib to latest upstream release to allow a 64-bit library to be built. 
 * #9009 update mercurial spkg to build 64-bit.
 * #7982 update sage_fortran so it can build 64-bit binaries.
 * Run 'make -k' to find as many issues as possible quickly on OpenSolaris - see #9026 for a list of the issues known to date. 

## The problem with flintqs

```
flintqs-20070817.p4/src/._TonelliShanks.h
flintqs-20070817.p4/src/TonelliShanks.h
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
****************************************************
g++ -ansi -c lprels.c -o lprels.o -I/export/home/drkirkby/sage-4.4.2/local/include -Wall -Wno-sign-compare -fomit-frame-pointer -O3
lprels.c: In function ‘FILE* flint_fopen(char*, char*)’:
<snip>
Successfully installed flintqs-20070817.p4
```


So no '-m64' flag is added to the g++ command line, so not surprisingly 'flintqs' does not build as a 64-bit binary. The output from the 'file' command confirms this:


```
drkirkby`@`hawk:~/sage-4.4.2$ file  local/bin/QuadraticSieve
local/bin/QuadraticSieve:       ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped, no debugging information available
```


## The likely reason for the flintqs problem

spkg-install has this bit of code:


```
if [ `uname -m` = "x86_64" ]; then
    $CP makefile.opteron makefile
else
    if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
        $CP makefile.osx64 makefile
    else
        $CP makefile.sage makefile
    fi
fi
```


A cursory glance would suggest the 'makefile.osx64' would work for OpenSolaris, Solaris or most other Unix operating systems, though this has not been tested yet.


---

Comment by drkirkby created at 2010-05-24 13:33:42

Note that the Debian 'dist' subdirectory also exists on this package, and should be removed - see #5903


---

Attachment

Mercurial patch to build 64-bit


---

Comment by drkirkby created at 2010-05-24 15:56:14

The attached patch resolves this issue. A new package can be found at:

http://boxen.math.washington.edu/home/kirkby/patches/flintqs-20070817.p5.spkg

Now the -m64 flag is added to the compiler


```
g++ -ansi -m64 lprels.o ModuloArith.o TonelliShanks.o F2matrix.o lanczos.o QS.o  -o "QuadraticSieve" -L/export/home/drkirkby/sage-4.4.2/local/lib -lgmp

real    0m0.952s
user    0m0.737s
sys     0m0.108s
Successfully installed flintqs-20070817.p5
```


and the binary is built as 64-bit. 


```
drkirkby`@`hawk:~/sage-4.4.2$ file  local/bin/QuadraticSieve
local/bin/QuadraticSieve:       ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
drkirkby`@`hawk:~/sage-4.4.2$ 
```



---

Comment by drkirkby created at 2010-05-24 15:56:14

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-05-24 18:21:20

For other OpenSolaris issues, see #9026


---

Comment by drkirkby created at 2010-05-24 23:25:18

This is quite an old version of flintqs, so I'm not going to report this upstream as a bug. Someone who wants a later version and has the expertese to test it, is welcome to update the version of flintqs in Sage, but for now, I just want to get it working properly on OpenSolaris. 

Dave


---

Comment by jsp created at 2010-06-10 16:30:22

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-06-10 16:30:22

It is not strictly needed, but it works ok when SAGE64=yes. Looks ok.

Positive review.

Jaap


---

Comment by rlm created at 2010-06-25 15:48:50

Resolution: fixed
