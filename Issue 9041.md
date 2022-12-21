# Issue 9041: python fails to build _socket on OpenSolaris x64, so pygments fails to build.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-25 01:01:29

Assignee: drkirkby

CC:  jsp robertwb

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


gcc 4.3.4 was failing to build iconv. 

## How the Sage build was attempted
 * 64-bit build. SAGE64 was set to "yes"
 * #9008 update zlib to latest upstream release to allow a 64-bit library to be built. 
 * #9009 update mercurial spkg to build 64-bit.
 * #7982 update sage_fortran so it can build 64-bit binaries.
 * Run 'make -k' to skip over errors, to allow one to find the errors quickly. 


## The problem
This a problem with python rather than pygments and is *very* similar to #9022. Since python is not building _socket, so some other parts of Sage fail to build if they need _socket. 


```
ygments-0.11.1.p0/.hg/undo.branch
pygments-0.11.1.p0/.hg/00changelog.i
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
Traceback (most recent call last):
  File "setup.py", line 4, in <module>
    ez_setup.use_setuptools()
  File "/export/home/drkirkby/sage-4.4.2/spkg/build/pygments-0.11.1.p0/src/ez_setup.py", line 78, in use_setuptools
    egg = download_setuptools(version, download_base, to_dir, download_delay)
  File "/export/home/drkirkby/sage-4.4.2/spkg/build/pygments-0.11.1.p0/src/ez_setup.py", line 105, in download_setuptools
    import urllib2, shutil
  File "/export/home/drkirkby/sage-4.4.2/local/lib/python/urllib2.py", line 92, in <module>
    import httplib
  File "/export/home/drkirkby/sage-4.4.2/local/lib/python/httplib.py", line 70, in <module>
    import socket
  File "/export/home/drkirkby/sage-4.4.2/local/lib/python/socket.py", line 46, in <module>
    import _socket
ImportError: No module named _socket
Error installing Pygments.

real    0m0.028s
user    0m0.013s
sys     0m0.014s
sage: An error occurred while installing pygments-0.11.1.p0
```



---

Comment by drkirkby created at 2010-05-30 05:48:52

I've since reported this as a bug

http://bugs.python.org/issue8852

and with the aid of a Python developer, I have managed to find a workaround.


---

Comment by drkirkby created at 2010-05-30 05:56:58

The failure of _socket to build is also causing ipython to fail to build - see #9022. Once I've produced a patch, hopefully both ipython and pygments will build ok. 

Dave


---

Comment by drkirkby created at 2010-05-30 09:01:12

The updated spkg is now ready for review at 

http://boxen.math.washington.edu/home/kirkby/patches/python-2.6.4.p9.spkg

The attached patch looks huge, since it includes a huge C file (patches/Modules.socketmodule.c) which is largely untouched from the original Python file (Modules/socketmodule.c) Only the following 3 files really need to be looked at 
 * SPKG.txt
 * spkg-install
 * patches/Modules.socketmodule.diff (the diff from the original python file). 

This contains a fix from Robert Bradsure for #9042, which I've given positive review to. 

The new python package has been tested on the following platforms, and found to work ok. 

 == Testing on OS X (bsd.math) ==
The test was performed using Sage 4.4.2

```
Sleeping for three seconds before testing python
math module OK
hashlib module imported

real	5m26.771s
user	2m13.789s
sys	0m40.901s
Successfully installed python-2.6.4.p9
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python-2.6.4.p9.spkg
```

I've checked that _socket builds - it is not listed in the list of either:
 * Modules where Python could not find the necessary parts, *or*
 * Modules which failed to build

 == Testing on Linux (sage.math) ==
The test was performed using Sage 4.4.2

```
Sleeping for three seconds before testing python
math module OK
hashlib module imported

real	4m5.736s
user	2m21.730s
sys	0m39.420s
Successfully installed python-2.6.4.p9
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python-2.6.4.p9.spkg
```

Again, the _socket module builds. 

 == Testing on OpenSolaris 06/2009 build 134 on my Sun Ultra 27 (Xeon processor) ==
The test was performed using Sage 4.4.2.

```
math module OK
hashlib module imported

real	1m35.872s
user	1m17.241s
sys	0m12.711s
Successfully installed python-2.6.4.p9
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.2/spkg/build/python-2.6.4.p9
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing python-2.6.4.p9.spkg
```

Obviously _socket builds there, otherwise I would not be submitted this as a patch!

## Testing on Solaris 10 on SPARC (my own Sun Blade 1000)
The test was performed using Sage 4.4.rc0. Any differences between 4.4.rc0 and 4.4.2 should not affect the building of the python package. 

I've not bothered testing on the SPARC-based Sun T5240 't2.math', as I don't have a build of Sage on 't2'. But my own Sun Blade 1000 (SPARC based) has an older release of Solaris 10. The fact the python module builds on that, should ensure it builds on any later release of Solaris 10 on SPARC. 


```
Sleeping for three seconds before testing python
math module OK
hashlib module imported

real    14m32.311s
user    11m15.781s
sys     2m22.087s
Successfully installed python-2.6.4.p9
```

Again, the _socket module builds ok. 


## Notes to the release manager
1) This package includes the fix from Robert Bradsure #9042. The patch must be applied after that at #9042. The package here at 
http://boxen.math.washington.edu/home/kirkby/patches/python-2.6.4.p9.spkg can replace Robert's python-2.6.4.p8.spkg

2) Once this is closed #9022 can be closed too, since the root cause of the problem at #9022 is the same as here. A python module failed to build, so two parts of Sage would not build. 

Dave


---

Comment by drkirkby created at 2010-05-30 09:01:12

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-05-30 21:56:32

Since Mike Hansen had already created a python-2.6.4.p8.spkg which is in sage-4.4.3.alpha0, I've updated the python-2.6.4.p8.spkg from sage-4.4.3.alpha0 to include
 
 * Roberts changes
 * My own changes. 

It is ready for review at http://boxen.math.washington.edu/home/kirkby/patches/python-2.6.4.p9.spkg


---

Comment by drkirkby created at 2010-05-30 22:13:19

Mercurial patch to get _socket to build on OpenSolaris


---

Attachment

Tested on OpenSolaris x86 and Fedora 12. With all other tests given, this is ok.

Positive review.

Jaap


---

Comment by jsp created at 2010-06-12 12:16:52

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-21 20:05:59

#9295, which has received positive review, contains the changes here, and also add an spkg-check file. As such, there is no need for this to be merged. As soon as #9295 is closed, so this can be closed. 

Dave


---

Comment by rlm created at 2010-06-25 15:49:12

Resolution: fixed


---

Comment by rlm created at 2010-06-25 15:50:54

To give proper credit, I'm closing this as if I've merged the changes here. See #9295.
