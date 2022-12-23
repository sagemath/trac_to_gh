# Issue 9520: scipy_sandbox does not exit if there are build failures, but spkg-install looks OK

Issue created by migration from https://trac.sagemath.org/ticket/9520

Original creator: drkirkby

Original creation time: 2010-07-16 22:57:14

Assignee: GeorgSWeber

CC:  leif mpatel mvngu jhpalmieri

Building Sage 4.5 on a Sun Blade 2000, with dual UltraSPARC III+ processors in 64-bit mode, the build process produces some obvious *error* messages when building scipy_sandbox-20071020.p5. These are not warnings, but errors. 


```
scipy_sandbox-20071020.p5/spkg-debian
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_141444-09 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.4.4/configure --with-pkgversion='GCC-4.4.4 with GMP-5.0.1 and MPFR-2.4.2-p2' --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/ccs/bin/as --with-ld=/usr/cc
s/bin/ld
Thread model: posix
gcc version 4.4.4 (GCC-4.4.4 with GMP-5.0.1 and MPFR-2.4.2-p2)
****************************************************
/export/home/drkirkby/64/sage-4.5/local/lib/python2.6/site-packages/numpy/distutils/command/config.py:361: DeprecationWarning:
+++++++++++++++++++++++++++++++++++++++++++++++++
Usage of get_output is deprecated: please do not
use it anymore, and avoid configuration checks
involving running executable on the target machine.
+++++++++++++++++++++++++++++++++++++++++++++++++

  DeprecationWarning)
ld: fatal: file _configtest.o: wrong ELF class: ELFCLASS64
ld: fatal: File processing errors. No output written to _configtest
collect2: ld returned 1 exit status
compiling '_configtest.c':
```


`wrong ELF class:` messages mean an attempt was made to link a mixture of 32-bit and 64-bit object files. 

But the build process still goes on to report that scipy_sandbox-20071020.p5 has installed OK. 

What is odd, is that `spkg-install` looks to be OK to me. 


```
python setup.py install

if [ $? -ne 0 ]; then
    echo "Error building arpack \n"
    exit 1
fi

cd ..
cd delaunay
python setup.py install

if [ $? -ne 0 ]; then
    echo "Error building delaunay triangulation code \n"
    exit 1
fi
```


Has anyone got any ideas? Could it be that the _configtest tries various ways to compile, so despite these being errors, this is actually OK? I somewhat doubt that is the case, but I don't know. 

Like a very similar issue with scipy (#9519), I'm not sure if this is an upstream bug or not. I suspect it is. 

Dave 


---

Comment by kcrisman created at 2013-04-26 01:44:03

This spkg is now only in the list of archived packages, so we're all done.


---

Comment by kcrisman created at 2013-04-26 01:44:03

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-04-26 01:44:32

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-04-28 12:47:17

Resolution: invalid
