# Issue 9097: c_lib in Sage library fails to build on OpenSolaris x64

Issue created by migration from https://trac.sagemath.org/ticket/9097

Original creator: drkirkby

Original creation time: 2010-05-31 00:49:01

Assignee: drkirkby

CC:  jsp f.r.bissey@massey.ac.nz

## Build environment
 * Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
 * OpenSolaris 2009.06 snv_111b X86
 * Sage 4.4.2
 * gcc 4.4.4

## How gcc 4.4.4 was configured
Since the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. 


```
drkirkby@hawk:~/sage-4.4.2$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
```


gcc 4.3.4 was failing to build iconv. 

## The problem


```
#error "LONG_BIT definition appears wrong for platform (bad gcc/glibc config?)."
scons: *** [src/interrupt.pic.o] Error 1
*** TOUCHING ALL CYTHON (.pyx) FILES ***
gcc -o src/interrupt.pic.o -c -fPIC -I/export/home/drkirkby/sage-4.4.2/local/include -I/export/home/drkirkby/sage-4.4.2/local/include/python2.6 -I/export/home/drkirkby/sage-4.4.2/local/include/NTL -Iinclude src/interrupt.c
In file included from /export/home/drkirkby/sage-4.4.2/local/include/python2.6/Python.h:58,
                 from include/stdsage.h:35,
                 from src/interrupt.c:12:
/export/home/drkirkby/sage-4.4.2/local/include/python2.6/pyport.h:685:2: error: #error "LONG_BIT definition appears wrong for platform (bad gcc/glibc config?)."
scons: *** [src/interrupt.pic.o] Error 1
Building Sage on Solaris in 64-bit mode
Creating SAGE_LOCAL/lib/sage-64.txt since it does not exist
Detected SAGE64 flag
Building Sage on Solaris in 64-bit mode

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
gcc -o src/interrupt.pic.o -c -fPIC -I/export/home/drkirkby/sage-4.4.2/local/include -I/export/home/drkirkby/sage-4.4.2/local/include/python2.6 -I/export/home/drkirkby/sage-4.4.2/local/include/NTL -Iinclude src/interrupt.c
In file included from /export/home/drkirkby/sage-4.4.2/local/include/python2.6/Python.h:58,
                 from include/stdsage.h:35,
                 from src/interrupt.c:12:
/export/home/drkirkby/sage-4.4.2/local/include/python2.6/pyport.h:685:2: error: #error "LONG_BIT definition appears wrong for platform (bad gcc/glibc config?)."
scons: *** [src/interrupt.pic.o] Error 1
ERROR: There was an error building c_lib.

ERROR installing SAGE

real	0m4.020s
user	0m1.014s
sys	0m2.138s
sage: An error occurred while installing sage-4.4.2
```


## Likely cause
It looks as though the -m64 option is not getting through to the library. Since that uses SCons to build, and I don't understand SCons (and very few people seem to), this could be a pig to fix. 


---

Comment by drkirkby created at 2010-06-14 17:28:09

Mercurial patch which adds -m64 when building c_lib.


---

Attachment

This is not a complete fix which enables the library to build, but it adds the flag -m64 on all platforms except OS X. (On OS X the flag is already added, but along with some other flags which I don't understand, and for now are best left). 

Dave


---

Comment by drkirkby created at 2010-06-14 17:30:05

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-07-01 00:09:08

Log file of building on OpenSolaris x64. The section where files are extracted from the tar file have been removed to save space.


---

Attachment

I'm attaching a log file which shows that this patch allows the build progress to go a long way. The log file for the build of the library `spkg/logs/sage-4.5.alpha1.log` is 958 KB in size, so clearly this gets a long way, where without the 4 lines


```
if env['PLATFORM'] != "darwin" and os.environ['SAGE64']=="yes": 
    env.Append( CFLAGS="-O2 -g -m64" ) 
    env.Append( CXXFLAGS="-O2 -g -m64" ) 
    env.Append( LINKFLAGS="-m64" ) 
```


the build fails after only 40 lines or so. 

There are some remaining issues to resolve, but this patch, which is only implemented if SAGE64 is set to yes and the operating system is *not* OS X, goes a long way towards helping a 64-bit port to OpenSolaris. 

Dave


---

Comment by fbissey created at 2010-07-01 01:38:11

I think the patch does the job. But I want to suggest the following patch (sorry I
have broken browsers right now because of a messy libpng update and I cannot use the
attachment form):


```
--- SConstruct.orig	2010-05-26 12:13:50.000000000 +1200
+++ SConstruct	2010-07-01 13:28:53.605754354 +1200
@@ -105,15 +105,15 @@
 ## The other two options control the way the linker creates a namespace
 ## for the dynamic library; check the man page for ld on a mac to see
 ## the details.
+if os.environ['SAGE64']=="yes":
+    # We want the debug and optimization flags, since debug symbols are so useful, etc.
+    print "MacIntel in 64 bit mode"
+    env.Append( CFLAGS="-O2 -g -m64" )
+    env.Append( CXXFLAGS="-O2 -g -m64" )
+    env.Append( LINKFLAGS="-m64" )
+
 if env['PLATFORM']=="darwin":
-    if os.environ['SAGE64']=="yes":
-        # We want the debug and optimization flags, since debug symbols are so useful, etc.
-        print "MacIntel in 64 bit mode"
-        env.Append( CFLAGS="-O2 -g -m64" )
-        env.Append( CXXFLAGS="-O2 -g -m64" )
-        env.Append( LINKFLAGS="-m64 -single_module -flat_namespace -undefined dynamic_lookup" )
-    else:
-        env.Append( LINKFLAGS="-single_module -flat_namespace -undefined dynamic_lookup" )
+    env.Append( LINKFLAGS="-single_module -flat_namespace -undefined dynamic_lookup" )
 
 # SCons doesn't automatically pull in system environment variables
 # However, we only need SAGE_LOCAL, so that's easy.
```

I think this simplify the logic. The building of extension afterwards is separate.


---

Comment by fbissey created at 2010-07-01 01:38:11

Changing assignee from drkirkby to fbissey.


---

Comment by fbissey created at 2010-07-01 09:37:02

Cleaner and proper patch with the same ideas previously shown


---

Attachment

Note that the space in

```
LINKFLAGS=" -single_module -flat_namespace -undefined dynamic_lookup"
```

is on purpose as scons concatenate strings. We don't want to end
up with "-m64-single_module".


---

Comment by drkirkby created at 2010-07-04 21:26:50

Thank you. 

I've put us both as reviews and both as authors. I understand this is OK. I know I initially asked you to remove me. That looks good. I am just about to test.


---

Comment by drkirkby created at 2010-07-05 09:53:02

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-07-05 09:53:02

Thank you very much. With this, patch applied, along with 

 * Applying #9399
 * Faking the install of maxima by touching spkg/installed/maxima-$version
 * Faking the install of R by touching /spkg/installed/R-$version

I'm able to get a 64-bit build on OpenSolaris. It does however crash at startup, so the port is not complete! But it is getting pretty close I think. 

Dave


---

Comment by fbissey created at 2010-07-05 10:04:19

Since this touch the OSX build as well do we have a tester for OSX 
that could try it? 32/64 bit should be irrelevant.


---

Comment by drkirkby created at 2010-07-05 15:58:19

Replying to [comment:8 fbissey]:
> Since this touch the OSX build as well do we have a tester for OSX 
> that could try it? 32/64 bit should be irrelevant.

I've tested this on OS X, and it works fine:


```
[kirkby@bsd sage-4.5.alpha1]$ uname -a 
Darwin bsd.local 10.4.0 Darwin Kernel Version 10.4.0: Fri Apr 23 18:28:53 PDT 2010; root:xnu-1504.7.4~1/RELEASE_I386 i386 i386 MacPro1,1 Darwin
[kirkby@bsd sage-4.5.alpha1]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: 1+1
2
sage: Quit
Exiting Sage (CPU time 0m0.04s, Wall time 0m4.44s).
[kirkby@bsd sage-4.5.alpha1]$ 
```

| Sage Version 4.5.alpha1, Release Date: 2010-06-29                  |
| Type notebook() for the GUI, and license() for information.        |
I agree your solution was cleaner than mine, but the reason I wrote it the way I did, was to guarantee that it could have no effect on OS X. 

I've also tested it on Linux (sage.math). 

Dave


---

Comment by rlm created at 2010-07-08 19:06:13

Resolution: fixed
