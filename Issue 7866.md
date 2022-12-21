# Issue 7866: zn_poly on Open Solaris reports  #error Not nails-safe yet

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-07 06:12:26

Assignee: drkirkby

CC:  jsp

## Build environment
 * Sun Ultra 27 3.333 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
 * OpenSolaris 2009.06 snv_111b X86
 * Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)
 * gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
 * 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. 
## The problem

```
zn_poly-0.9.p1/src/src/mul_fft.c
zn_poly-0.9.p1/src/src/ks_support.c
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
make[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/array.o -c src/array.c
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/invert.o -c src/invert.c
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/ks_support.o -c src/ks_support.c
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid.o -c src/mulmid.c
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid_ks.o -c src/mulmid_ks.c
src/mulmid_ks.c:402:2: error: #error Not nails-safe yet
make[2]: *** [src/mulmid_ks.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
./spkg-install: line 39: tune/tune: No such file or directory
make[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
gcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/array-DEBUG.o -c src/array.c
gcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/invert-DEBUG.o -c src/invert.c
gcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/ks_support-DEBUG.o -c src/ks_support.c
gcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/mulmid-DEBUG.o -c src/mulmid.c
gcc -g -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DDEBUG -o src/mulmid_ks-DEBUG.o -c src/mulmid_ks.c
src/mulmid_ks.c:402:2: error: #error Not nails-safe yet
make[2]: *** [src/mulmid_ks-DEBUG.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
make[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid_ks.o -c src/mulmid_ks.c
src/mulmid_ks.c:402:2: error: #error Not nails-safe yet
make[2]: *** [src/mulmid_ks.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
make[2]: Entering directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage-4.3.1.alpha1/local/include -I./include -DNDEBUG -o src/mulmid_ks.o -c src/mulmid_ks.c
src/mulmid_ks.c:402:2: error: #error Not nails-safe yet
make[2]: *** [src/mulmid_ks.o] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha1/spkg/build/zn_poly-0.9.p1/src'
Error building zn_poly shared library.

real	0m1.026s
user	0m0.860s
sys	0m0.144s
sage: An error occurred while installing zn_poly-0.9.p1
```


 == Likely explanation ==
It looks as though the -m64 bit flag is not passed properly, so that's the issue. 


---

Comment by drkirkby created at 2011-04-02 13:26:11

This can be closed. It was semi-fixed by #8178, but was not properly fixed until #9358 in sage-4.5.3.alpha1 

Dave


---

Comment by jdemeyer created at 2011-04-05 15:50:01

Resolution: duplicate
