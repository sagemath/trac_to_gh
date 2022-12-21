# Issue 8086: numpy fails to build on Open Solaris x64 - 32 / 64-bit mixup

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-27 03:35:29

Assignee: drkirkby

CC:  jsp

## Build environment
 * Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
 * OpenSolaris 2009.06 snv_111b X86
 * Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)
 * gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
 * 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. 
## The problem
numpy is failing to build. It looks like there is a mix of 32 and 64-bit objects. 



```
numpy-1.3.0.p2/src/setup.py
numpy-1.3.0.p2/src/MANIFEST.in
numpy-1.3.0.p2/.hgtags
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
Running from numpy source directory.
F2PY Version 2
blas_opt_info:
blas_mkl_info:
  libraries mkl,vml,guide not found in /export/home/drkirkby/sage-4.3.1/local/lib
  NOT AVAILABLE

atlas_blas_threads_info:
Setting PTATLAS=ATLAS
  libraries ptf77blas,ptcblas,atlas not found in /export/home/drkirkby/sage-4.3.1/local/lib
  NOT AVAILABLE

atlas_blas_info:
  FOUND:
    libraries = ['f77blas', 'cblas', 'atlas']
    library_dirs = ['/export/home/drkirkby/sage-4.3.1/local/lib']
    language = c
    include_dirs = ['/export/home/drkirkby/sage-4.3.1/local/include']

/export/home/drkirkby/sage-4.3.1/spkg/build/numpy-1.3.0.p2/src/numpy/distutils/command/config.py:361: DeprecationWarning: 
+++++++++++++++++++++++++++++++++++++++++++++++++
Usage of get_output is deprecated: please do not 
use it anymore, and avoid configuration checks 
involving running executable on the target machine.
+++++++++++++++++++++++++++++++++++++++++++++++++

  DeprecationWarning)
customize Sage_FCompiler_1
customize Sage_FCompiler_1
customize Sage_FCompiler_1 using config
compiling '_configtest.c':

/* This file is generated from numpy/distutils/system_info.py */
void ATL_buildinfo(void);
int main(void) {
  ATL_buildinfo();
  return 0;
}
C compiler: gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC

compile options: '-c'
gcc: _configtest.c
gcc _configtest.o -L/export/home/drkirkby/sage-4.3.1/local/lib -lf77blas -lcblas -latlas -o _configtest
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libf77blas.so: wrong ELF class: ELFCLASS64
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libcblas.so: wrong ELF class: ELFCLASS64
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libatlas.so: wrong ELF class: ELFCLASS64
ld: fatal: file processing errors. No output written to _configtest
collect2: ld returned 1 exit status
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libf77blas.so: wrong ELF class: ELFCLASS64
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libcblas.so: wrong ELF class: ELFCLASS64
ld: fatal: file /export/home/drkirkby/sage-4.3.1/local/lib/libatlas.so: wrong ELF class: ELFCLASS64
ld: fatal: file processing errors. No output written to _configtest
collect2: ld returned 1 exit status
failure.
removing: _configtest.c _configtest.o
Status: 255
Output: 
  FOUND:
    libraries = ['f77blas', 'cblas', 'atlas']
    library_dirs = ['/export/home/drkirkby/sage-4.3.1/local/lib']
    language = c
    define_macros = [('NO_ATLAS_INFO', 2)]
    include_dirs = ['/export/home/drkirkby/sage-4.3.1/local/include']

lapack_opt_info:
lapack_mkl_info:
```



---

Comment by jsp created at 2010-01-27 10:45:19

I do have a working numpy on your machine.

There is a numpy-1.3.0.p3.spkg in trac waiting to be merged.

Here is a pre version of mine:
http://boxen.math.washington.edu/home/jsp/ports/numpy-1.3.0.p3.spkg

Works on Open Solaris.

Jaap


---

Comment by jsp created at 2010-01-27 15:59:05

Added patch file and updated spkg:

[http://boxen.math.washington.edu/home/jsp/ports/numpy-1.3.0.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/numpy-1.3.0.p3.spkg)

Jaap


---

Comment by jsp created at 2010-01-27 15:59:05

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-05-30 16:30:33

Changing status from needs_review to needs_info.


---

Comment by drkirkby created at 2010-05-30 16:30:33

Hi Jaap,

I'm having a problem with this. I got a message about "could not fork". I even rebooted the machine once, thinking something was wrong, but everything else seems to work. 


Is this bit of code in the patch right? It looks wrong to me:


```
echo "#! /usr/bin/env bash" > gcc 
echo "`which gcc` -m64 " | sed 's/$/\$`@`/' >> fake_gcc 
```


Should the first line not write to the file 'fake_gcc' rather than 'gcc'? If so, since it gets copied to $SAGE_LOCAL/bin/gcc, why not write it directly there? 

i.e.


```
echo "#! /usr/bin/env bash" > $SAGE_LOCAL/bin/gcc
echo "`which gcc` -m64 " | sed 's/$/\$`@`/' >> $SAGE_LOCAL/bin/gcc 
```


Also, why use 'sed'? If I understand your intentions correctly, 


```
echo "`which gcc` -m64 \$`@`"
```


would achieve the same, but without invoking 'sed'. 

I would also add that 'which' is not a POSIX command, whereas 'command -v' gives you the same information, but in a standards complient way. This can be important, especially on Solaris 10, as the return code of 'which' is undefined on there. 


```
drkirkby`@`hawk:~$ echo "`command -v gcc` -m64 \$`@`" 
/usr/local/gcc-4.4.4/bin/gcc -m64 $`@`
```


is more portable. 

However, I can't seem to get it to work. I'm not sure if I understand exactly what you are aiming to do here. Why do we need a fake gcc? 

Dave


---

Comment by drkirkby created at 2010-06-28 08:09:22

Jaap, 

I can't get your patch to work, so have reimplemented this. I've completely removed the file fake_gcc from Numpy, and instead create the fake file dynamically with the correct path. 

I've also reported the issue to the Numpy bug database. 

http://projects.scipy.org/numpy/ticket/1525

which should have been done years ago when the problem was first realised in OS X. 

Here's a package waiting for review, which I believe does fix the problem. 

http://boxen.math.washington.edu/home/kirkby/patches/numpy-1.3.0.p4.spkg

Dave


---

Comment by drkirkby created at 2010-06-28 08:12:02

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2010-07-30 09:00:46

## Great news

I've found a much simpler solution to this, which totally avoids using any fake gcc files. Just compile with

CC="gcc -m64"
export CC

and it works! I will attach a simpler patch in 15 minutes. I'm marking as "needs work" for now, as I need to do something else just now. 

Dave


---

Comment by drkirkby created at 2010-07-30 09:00:46

Changing status from needs_review to needs_work.


---

Attachment

Mercurial patch which solves the Numpy build issues without any sort of hack. I think this would work on OS X too, but I'm not changing the OS X code now.


---

Comment by drkirkby created at 2010-07-30 09:52:57

Here's the updated package. I believe this is a decent fix (at last). 

http://boxen.math.washington.edu/home/kirkby/patches/numpy-1.3.0.p4.spkg

I've reported this upstream 

http://projects.scipy.org/numpy/ticket/1525

Dave


---

Comment by drkirkby created at 2010-07-30 09:52:57

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-08-03 21:35:21

The changes look good.  The spkg builds on a number of different machines, both 32-bit and 64-bit, and doctests pass.

By the way, with the old spkg, numpy didn't build properly on 64-bit Solaris (either sparc -- t2 -- or x86 -- fulvia), so it's not exclusively an OpenSolaris issue.  With the new spkg, it works on fulvia.  I haven't gotten t2 (with SAGE64='yes') to build the prerequisite packages yet.  I'm working on that, and if there are issues building numpy, I'll revert the positive review.

(Tested on t2 (32-bit), mark2 (32-bit), Mac OS X 10.6 (64-bit), sage.math (both with SAGE64='yes' and with SAGE64 unset), taurus (both with SAGE64='yes' and SAGE64 unset), cicero (32-bit), fulvia (both settings for SAGE64), and iras (64-bit machine? but with SAGE64 unset).)


---

Comment by jhpalmieri created at 2010-08-03 21:35:21

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-08-07 22:35:14

## Note to the release manager

All changes are committed in the repository of the .spkg file. No library changes need to be made. Just drop in 

http://boxen.math.washington.edu/home/kirkby/patches/numpy-1.3.0.p4.spkg


---

Comment by mpatel created at 2010-08-09 09:37:27

Resolution: fixed
