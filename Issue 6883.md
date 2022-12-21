# Issue 6883: ECL 9.8.4 fails to build in 64-bit mode, OS X 10.5.8

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-09-04 06:36:43

Assignee: mabshoff

CC:  mvngu

I got the following failure when compiling Sage 4.1.2.alpha0:

```
checking for __gmpz_init in -lgmp... no
configure: error: System gmp library requested but not found.
Failed to configure ECL ... exiting

real    0m3.427s
user    0m1.095s
sys     0m2.049s
sage: An error occurred while installing ecl-9.8.4
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /scratch/mvngu/sandbox-64/sage-4.1.2.alpha0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/scratch/mvngu/sandbox-64/sage-4.1.2.alpha0/spkg/build/ecl-9.8.4 and type 'make'.
Instead type "/scratch/mvngu/sandbox-64/sage-4.1.2.alpha0/sage -sh"
in order to set all environment variables correctly, then cd to
/scratch/mvngu/sandbox-64/sage-4.1.2.alpha0/spkg/build/ecl-9.8.4
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/ecl-9.8.4] Error 1

real    0m7.189s
user    0m2.507s
sys     0m3.197s
Error building Sage.
```

This was on Mac OS X 10.5.8 (bsd.math.washington.edu), compiling in 64-bit mode.


---

Comment by drkirkby created at 2009-09-05 11:47:45

Log file of failed ECL build on OS X 64-bit.


---

Attachment

I'm not surprised you got the failure, as I had updated the spkg after you tested it. That was my fault. 

But I copiled the version of the .spkg from Alex's directory, which is where you said you copied yours from, and it still failed for me. 

I have created an updated one at 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4.p0/ecl-9.8.4.p0.spkg 

which fixes the issue you had (not finding the gmp library), but it still fails to build for me. 

I also downloaded the one from Alex's directory, which is where you copied yours from. That does not build for me either. So I'm somewhat surprised you managed to build this anyway.  

Dave


---

Comment by mvngu created at 2009-09-06 06:12:57

One of the problems is the following line in the file `spkg-install` of the ECL spkg:

```
./configure --prefix=$SAGE_LOCAL --with-system-gmp --enable-boehm=system
```

Deleting the argument `--with-system-gmp` and the build would go OK, but then it would fail on t2.math. Deleting `--enable-boehm=system` and the build would go fine. I have created an updated spkg at



http://sage.math.washington.edu/home/mvngu/release/spkg/standard/ecl-9.8.4.p0.spkg



whose file `spkg-install` now only has this configuration line:

```
./configure --prefix=$SAGE_LOCAL
```

I also did some general clean up such as removing the empty directory `build` and reformatting comments so that they are no more than 80 characters in length. I'm now building Sage 4.1.2.alpha0 from scratch with the above updated ECL package. The machines sage.math, mod.math, and geom.math are all near capacity so I have been experiencing difficulty getting Sage to compile on those machines since ATLAS complained about errors while tuning itself. Here are the platforms on which I'm currently compiling Sage 4.1.2.alpha0 from scratch with my updated ecl-9.8.4.p0.spkg:

 * bsd.math in 32-bit mode
 * bsd.math in 64-bit mode
 * t2.math
 * cicero on SkyNet (x86 Fedora 9 with GCC 4.4.1)
 * eno on SkyNet (x86_64 Fedora 9 with GCC 4.4.1)
 * lena on SkyNet (x86_64 RHEL Server 5.3 with GeForce GPUs and GCC 4.4.1)

For bsd.math, I have copied fortran-OSX64-20090120.spkg and ecl-9.8.4.p0.spkg to the directory /Users/mvngu/apps/. Here are the steps I took to start building Sage 4.1.2.alpha0 in 64-bit mode with ecl-9.8.4.p0.spkg:

```
[mvngu`@`bsd ~]$ pwd
/Users/mvngu
[mvngu`@`bsd ~]$ tar -xf apps/sage-4.1.2.alpha0.tar -C /scratch/mvngu/sandbox-64/alpha/
[mvngu`@`bsd ~]$ cd /scratch/mvngu/sandbox-64/alpha/sage-4.1.2.alpha0/
[mvngu`@`bsd sage-4.1.2.alpha0]$ rm -rf spkg/standard/fortran-20071120.p5.spkg
[mvngu`@`bsd sage-4.1.2.alpha0]$ cp -rf /Users/mvngu/apps/fortran-OSX64-20090120.spkg spkg/standard/
[mvngu`@`bsd sage-4.1.2.alpha0]$ rm -rf spkg/standard/ecl-9.8.4.spkg 
[mvngu`@`bsd sage-4.1.2.alpha0]$ cp -rf /Users/mvngu/apps/ecl-9.8.4.p0.spkg spkg/standard/
[mvngu`@`bsd sage-4.1.2.alpha0]$ export SAGE64=yes
[mvngu`@`bsd sage-4.1.2.alpha0]$ make
```

When `make` terminates, it would report success. But actually if you then start Sage with

```
./sage -br main
```

you would get many errors. You now need to open the file

```
SAGE_ROOT/devel/sage-main/sage/graphs/all.py
```

and comment out the line

```
from sage.graphs.cliquer import *
```

Then start `make` again:

```
make
```

When it terminates, start Sage again with

```
./sage -br main
```

This time, Sage should load fine without any errors.


---

Comment by mvngu created at 2009-09-06 11:16:04

David Kirkby's updated spkg with changes committed in his name:

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/ecl-9.8.4.p0.spkg


---

Comment by mvngu created at 2009-09-07 04:23:07

Replying to [comment:3 mvngu]:
> David Kirkby's updated spkg with changes committed in his name:
http://sage.math.washington.edu/home/mvngu/release/spkg/standard/ecl-9.8.4.p0.spkg



kirkby's 4th attempt at an updated spkg is up at this same place. All changes have been committed in this name.


---

Comment by jhpalmieri created at 2009-09-07 05:04:50

With the most recent spkg ("kirby's 4th attempt"), I get a failure right after configuring in 64-bit OS X:

```
Configuration complete. To build ECL, issue make in this directory.
cd build; make
cp /Applications/sage_builds/sage-4.1.2.alpha0-64bit/spkg/build/ecl-9.8.4.p0/src/src/util/gdbinit .gdbinit
if (echo c gc gmp | grep gmp); then \
	  cd gmp && make install && \
	  cd .. && mv include/gmp.h ecl/ && rmdir include &&  \
	  mv ./libgmp.a ./libeclgmp.a; \
	fi
c gc gmp
make[2]: *** No rule to make target `install'.  Stop.
make[1]: *** [libeclgmp.a] Error 2
```

It seems to build successfully in 32-bit OS X.

After executing "export MAKE='make -j2' ", it fails in 32-bit OS X:

```
----------------------------------------------------------------------
Libraries have been installed in:
   /Applications/sage_builds/sage-4.1.2.alpha0/spkg/build/ecl-9.8.4.p0/src/build

If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the `-LLIBDIR'
flag during linking and do at least one of the following:
   - add LIBDIR to the `DYLD_LIBRARY_PATH' environment variable
     during execution

See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.
----------------------------------------------------------------------
cd c; make -j2
make[2]: warning: -jN forced in submake: disabling jobserver mode.
cat /Applications/sage_builds/sage-4.1.2.alpha0/spkg/build/ecl-9.8.4.p0/src/src/c/symbols_list.h | \
	sed -e 's%{\([A-Z ]*.*".*"\),[^,]*,[ ]*NULL,.*}%{\1,NULL}%g' \
	    -e 's%{\([A-Z ]*.*".*"\),[^,]*,[ ]*\([^,]*\),.*}%{\1,"\2"}%g' \
	    -e 's%{NULL.*%{NULL,NULL}};%' > /Applications/sage_builds/sage-4.1.2.alpha0/spkg/build/ecl-9.8.4.p0/src/src/c/symbols_list2.h
if test -f ../CROSS-DPP ; then ../CROSS-DPP /Applications/sage_builds/sage-4.1.2.alpha0/spkg/build/ecl-9.8.4.p0/src/src/c/main.d main.c ; else ./dpp /Applications/sage_builds/sage-4.1.2.alpha0/spkg/build/ecl-9.8.4.p0/src/src/c/main.d main.c ; fi
/bin/sh: ./dpp: No such file or directory
make[2]: *** [main.c] Error 127
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [libeclmin.a] Error 2
make: *** [all] Error 2
```



---

Comment by drkirkby created at 2009-09-15 11:17:32

Changing keywords from "" to "os x ecl cvs".


---

Comment by drkirkby created at 2009-09-15 11:17:32

This is now solved I believe. I have tested a revised .spkg on 

 * 32-bit OS X (bsd.math)
 * 64-bit OS X (bsd.math)
 * 32-bit Solaris (Sun of mine)
 * 64-bit Solaris (Sun of mine)
 * 64-bit linux (sage.math)

The basic problem was that ecl 9.8.4 would not build on OS X in 64-bit mode. That is acknowledged by the main ECL developer. Hence no changes to spkg-install alone will solve that. 

This is a package I created from a CVS snapshot of ECL. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ecl-9.8.4-cvs-13th-Sept-2009-3rd-try/ecl-9.8.4-cvs-13th-Sept-2009.spkg

The snapshot was taken on 13th September (as indicated by the name). It incorporates changes by Minh Nguyen too, so now the configure line is simply:


```
./configure --prefix=$SAGE_LOCAL
```

 
Here's the build results from 64-bit OS X (the subject of this ticket), but it also works on the other systems I have tried it on. 


```
Extracting package /Users/kirkby/64/sage-4.1.2.alpha1/spkg/standard/ecl-9.8.4-cvs-13th-Sept-2009.spkg ...
-rw-r--r-- 1 kirkby staff 4797805 Sep 15 00:08 /Users/kirkby/64/sage-4.1.2.alpha1/spkg/standard/ecl-9.8.4-cvs-13th-Sept-2009.spkg
ecl-9.8.4-cvs-13th-Sept-2009/
ecl-9.8.4-cvs-13th-Sept-2009/build/
ecl-9.8.4-cvs-13th-Sept-2009/build/build/
<SNIP>
ecl-9.8.4-cvs-13th-Sept-2009/spkg-install
ecl-9.8.4-cvs-13th-Sept-2009/ecl-9.8.4-cvs-13th-Sept-2009.spkg
Finished extraction
****************************************************
Host system
uname -a:
Darwin bsd.local 9.8.0 Darwin Kernel Version 9.8.0: Wed Jul 15 16:55:01 PDT 2009; root:xnu-1228.15.4~1/RELEASE_I386 i386 i386 MacPro1,1 Darwin
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin9
Configured with: /var/tmp/gcc/gcc-5493~1/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/lib --build=i686-apple-darwin9 --with-arch=apple --with-tune=generic --host=i686-apple-darwin9 --target=i686-apple-darwin9
Thread model: posix
gcc version 4.0.1 (Apple Inc. build 5493)
****************************************************
Building a 64-bit version of ECL
Code will be built with debugging information present. Set 'SAGE_DEBUG' to 'no' if you don't want that.
No Fortran compiler has been defined. This is not normally a problem.
Using CC=gcc
Using CXX=g++
Using FC=
Using F77=
Using SAGE_FORTRAN=
Using SAGE_FORTRAN_LIB=
The following environment variables will be exported
Using CFLAGS= -O2  -m64  -g  -Wall
Using CXXFLAGS= -O2  -m64  -g  -Wall
Using FCFLAGS= -O2  -m64  -g  -Wall
Using F77FLAGS= -O2  -m64  -g  -Wall
Using CPPFLAGS= -I/Users/kirkby/64/sage-4.1.2.alpha1/local/include
Using LDFLAGS= -L/Users/kirkby/64/sage-4.1.2.alpha1/local/lib -m64
Using ABI=64
configure scripts and/or makefiles might override these later

Creating directory `build'
Switching to directory `build' to continue configuration.
checking build system type... pentium3-apple-darwin9.8.0
checking host system type... pentium3-apple-darwin9.8.0
checking for gcc... gcc
<SNIP>
for i in *.asd; do /Users/mvngu/usr/bin/install -c -m 644 ${i} /Users/kirkby/64/sage-4.1.2.alpha1/local/lib/ecl-9.8.4/; done
for i in c/dpp ecl_min `cat MODULES`; do \
          case $i in \
            *.fas) /Users/mvngu/usr/bin/install -c $i /Users/kirkby/64/sage-4.1.2.alpha1/local/lib/ecl-9.8.4/;; \
            *) /Users/mvngu/usr/bin/install -c -m 644 $i /Users/kirkby/64/sage-4.1.2.alpha1/local/lib/ecl-9.8.4/;; \
          esac \
        done

real    2m34.619s
user    1m50.851s
sys     0m41.021s
Successfully installed ecl-9.8.4-cvs-13th-Sept-2009
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing ecl-9.8.4-cvs-13th-Sept-2009.spkg
```



---

Comment by mvngu created at 2009-09-15 15:02:36

Here is David Kirkby's updated ECL package with all changes checked in his name:

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/ecl-9.8.4-cvs-13th-Sept-2009.spkg

I deleted the empty directory "build" and the file "ecl-9.8.4-cvs-13th-Sept-2009.spkg", which is about 46 bytes. As I'm listed as an author, someone other than David and myself should review this ticket. A thorough test would be to compile the latest alpha release of Sage from source with this updated ECL package, on various platforms including t2.


---

Comment by jhpalmieri created at 2009-09-15 23:35:24

I didn't build from scratch: just "sage -f ecl...spkg" followed by "sage -f spkg/standard/maxima...spkg".   This is with Sage 4.1.2.alpha1.

On 32-bit Mac OS X, compiled successfully.  One nonrepeatable test failure: "sage -t -long "devel/sage/sage/graphs/graph_plot.py".  I'm not going to worry about it, because it passes tests when I do it again.

On 64-bit Mac OS X, compiled successfully.  Apart from the test failures because of the lack of cliquer, one failure: 

```
sage -t -long "devel/sage/sage/interfaces/maxima.py"        
**********************************************************************
File "/Applications/sage_builds/sage-4.1.2.alpha1-64bit/devel/sage/sage/interfaces/maxima.py", line 2108:
    sage: list(v)
Expected:
    [0, x, 2*x^2, 3*x^3, 4*x^4, 5*x^5]
Got:
    [0, x, , 3*x^3, 4*x^4, 5*x^5]
**********************************************************************
```

Is this a serious issue, or just something to do with the new version of maxima?  Why do I only get it in a 64-bit build?


---

Attachment

based on Sage 4.1.2.alpha1


---

Comment by mvngu created at 2009-09-16 02:06:16

Replying to [comment:8 jhpalmieri]:
> Is this a serious issue, or just something to do with the new version of maxima? 
It's an issue with data representation. On the surface you see nothing wrong, even on sage.math:

```
sage: v = maxima('create_list(i*x^i,i,0,5)')
sage: L = list(v)
sage: [e for e in L]
[0, x, 2*x^2, 3*x^3, 4*x^4, 5*x^5]
sage: L
[0, x, 2*x^2, 3*x^3, 4*x^4, 5*x^5]
```

Each member of the list `L` is a `MaximaElement` object. So we should use the method `_sage_()` to convert these objects to Sage objects:

```
sage: [type(e) for e in L]
[<class 'sage.interfaces.maxima.MaximaElement'>,
 <class 'sage.interfaces.maxima.MaximaElement'>,
 <class 'sage.interfaces.maxima.MaximaElement'>,
 <class 'sage.interfaces.maxima.MaximaElement'>,
 <class 'sage.interfaces.maxima.MaximaElement'>,
 <class 'sage.interfaces.maxima.MaximaElement'>]
sage: [e._sage_() for e in L]
[0, x, 2*x^2, 3*x^3, 4*x^4, 5*x^5]
```

Displaying `MaximaElement` objects as is can be dangerous because sometimes they have escape sequences, which result in unexpected behaviours:

```
sage: [str(e) for e in L]

['                                       0',
 '                                       x',
 '                                        2\r\n                                     2 x',
 '                                        3\r\n                                     3 x',
 '                                        4\r\n                                     4 x',
 '                                        5\r\n                                     5 x']
sage: [latex(e) for e in L]
[0, x, 2\,x^2, 3\,x^3, 4\,x^4, 5\,x^5]
```

The patch `trac_6883-proper-display.patch` should fix the doctest problem on 64-bit OS X 10.5.


---

Comment by mvngu created at 2009-09-27 02:39:40

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:58:34

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
