# Issue 9030: rubiks is building part 32-bit and part 64-bit on OpenSolaris x64.

Issue created by migration from https://trac.sagemath.org/ticket/9030

Original creator: drkirkby

Original creation time: 2010-05-24 07:52:15

Assignee: AlexGhitza

CC:  jsp

'rubiks' has code to attempt to build it 64-bit, but that does not seem to be fully functional, as parts are built 32-bit and parts are built 64-bit. 


```
rubiks-20070912.p10/dist/debian/changelog
rubiks-20070912.p10/spkg-install
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
Building a 64-bit version of rubiks
Code will be built with debugging information present. Set 'SAGE_DEBUG' to 'no' if you don't want that.
Using CC=gcc
Using CXX=g++
Using FC=
Using F77=
Using SAGE_FORTRAN=/usr/local/gcc-4.4.4/bin/gfortran
Using SAGE_FORTRAN_LIB=/usr/local/gcc-4.4.4/lib/amd64/libgfortran.so
The following environment variables will be exported
Using CFLAGS= -O2  -m64  -g  -Wall 
Using CXXFLAGS= -O2  -m64  -g  -Wall 
Using FCFLAGS= -O2  -m64  -g  -Wall 
Using F77FLAGS= -O2  -m64  -g  -Wall 
Using CPPFLAGS=
Using LDFLAGS= -m64 
Using ABI=
configure scripts and/or makefiles might override these later
 
Building Rubiks cube solvers
for dir in dietz/cu2 dietz/mcube dietz/solver dik reid; do \
		(cd ${dir} && make all)\
	done
make[1]: Entering directory `/export/home/drkirkby/sage-4.4.2/spkg/build/rubiks-20070912.p10/src/dietz/cu2'
g++  -O2  -m64  -g  -Wall  -c cu2.cpp
g++  -O2  -m64  -g  -Wall  -c main.cpp
g++  -O2  -m64  -g  -Wall   -o cubex  cubex.o main.o
<snip lots of 64-bit builds builds and lots of warnings>
gcc  -O2  -m64  -g  -Wall    -m64   optimal.c   -o optimal
gcc  -O2  -m64  -g  -Wall    -m64   twist.c   -o twist
<snip>
cp reid/optimal /export/home/drkirkby/sage-4.4.2/local/bin
cp dietz/solver/cubex /export/home/drkirkby/sage-4.4.2/local/bin
cp dietz/mcube/mcube /export/home/drkirkby/sage-4.4.2/local/bin
cp dietz/cu2/cu2 /export/home/drkirkby/sage-4.4.2/local/bin
cp dik/dikcube /export/home/drkirkby/sage-4.4.2/local/bin
cp dik/size222 /export/home/drkirkby/sage-4.4.2/local/bin
```


When we check files, I note some are built 32-bit and some are built 64-bit. 


```
drkirkby@hawk:~/sage-4.4.2$ file local/bin/size222 
local/bin/size222:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped, no debugging information available
drkirkby@hawk:~/sage-4.4.2$ file local/bin/optimal
local/bin/optimal:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped
```


I expect this would happen on any platform where the default is 32-bit, suggesting to me this never even worked 64-bit on OS X systems where 32-bit was the default. 

Dave


---

Comment by drkirkby created at 2010-05-24 18:22:43

Changing assignee from AlexGhitza to drkirkby.


---

Comment by drkirkby created at 2010-05-24 18:22:43

Changing component from algebra to solaris.


---

Comment by drkirkby created at 2010-05-24 18:22:43

For other OpenSolaris issues, see #9026


---

Comment by robertwb created at 2010-05-25 05:53:13

As this is never linked in directly, there is no need (or advantage, as far as I can tell) to build this 64-bit for a fully functional Sage.


---

Comment by drkirkby created at 2010-05-28 23:38:39

Replying to [comment:3 robertwb]:
> As this is never linked in directly, there is no need (or advantage, as far as I can tell) to build this 64-bit for a fully functional Sage. 

I agree there is no technical advantage in using rubiks 64-bit. 

However, it seems rather unprofessional to have 4 out of the 6 binaries building 64-bit, and two of them building 32-bit. Having all rubiks binaries made 64-bit allows one to quickly find any binaries from any packages that are not being built properly, using a command like


```
$ find local -exec file {} \; | grep 32-bit
```


as such, I believe it's desirable that a 64-bit build on OpenSolaris, Solaris or any other operating system for that matter creates only 64-bit objects.

A revised package, which add the -m64 flag to the makefile is at 

http://boxen.math.washington.edu/home/kirkby/patches/rubiks-20070912.p11.spkg

There were a lot of files not in the repository (I believe this was my fault months ago), which I've checked in. As such, the patch is a lot longer than it needs to be to fix this particular problem. 

The following line:


```
CFLAGS = -O -DLARGE_MEM -DVERBOSE
```

gets be changed to:

```
CFLAGS = ${CFLAG64} -O -DLARGE_MEM -DVERBOSE
```


using 'sed'. 

$CFLAG64 is then set to -m64 if building 64-bit, so the -m64 gets added to the makefile. 


After building *all* the rubiks binaries are 64-bit. i.e.


```
drkirkby@hawk:~/sage-4.4.2$ file local/bin/size222 
local/bin/size222:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
drkirkby@hawk:~/sage-4.4.2$ file local/bin/dikcube
local/bin/dikcube:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
```


Previously both were being built 32-bit (see the output of the find command shown above, where clearly there was a mix of 32-bit and 64-bit objects). 

This has been compiled on sage.math and bsd.math as well as my own Sun Ultra 27 running OpenSolaris. 

Dave


---

Comment by drkirkby created at 2010-05-28 23:38:52

Changing status from new to needs_review.


---

Attachment

Mercurial patch to ensure all files build 64-bit on OpenSolaris


---

Comment by jsp created at 2010-06-10 16:19:18

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-06-10 16:19:18

Is ok for me. Positive review.

Jaap


---

Comment by rlm created at 2010-06-25 15:48:31

Resolution: fixed
