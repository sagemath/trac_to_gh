# Issue 9832: fatal relocation error with Cliquer library on 64-bit Solaris and OpenSolaris

Issue created by migration from https://trac.sagemath.org/ticket/9833

Original creator: drkirkby

Original creation time: 2010-08-28 19:19:25

Assignee: drkirkby

CC:  jhpalmieri ncohen jason jsp mvngu mpatel

If a 64-bit version of Sage is built on OpenSolaris, Sage reports an error as soon as it is started. 


```
drkirkby@hawk:~$ 64/sage-4.5.3.alpha2/sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
| Sage Version 4.5.3.alpha2, Release Date: 2010-08-23                |
| Type notebook() for the GUI, and license() for information.        |
<snip>

ImportError: ld.so.1: python: fatal: relocation error: R_AMD64_PC32: file /export/home/drkirkby/64/sage-4.5.3.alpha2/local/lib//libcliquer.so: symbol main: value 0x28152e8c7d4 does not fit
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```


The problem of fatal relocation errors is discussed on this [Sun blog](http://blogs.sun.com/rie/entry/my_relocations_don_t_fit) by Rod Evans. 

A shared library should show no output from the following command:


```
$ elfdump -d library | fgrep TEXTREL
```


But in a 64-bit builds of Sage on both OpenSolaris x64 and Solaris 10 on SPARC, but show output. The following is from an OpenSolaris machine, but similar is seen on a 64-bit SPARC build of Sage. 


```
drkirkby@hawk:~$ elfdump -d 64/sage-4.5.3.alpha2/local/lib/libcliquer.so  | grep TEXTREL
      [17]  TEXTREL           0                   
      [25]  FLAGS             0x4                 [ TEXTREL ]
drkirkby@hawk:~$ 
```


If this flag is found, then the link-editor thinks this file contains non-pic code. 

Looking at the way the shared library is built on Solaris, it is different from other platforms. 


```
# Flags for building a dynamically linked shared object.
SAGESOFLAGS=" "
if [ "$UNAME" = "Linux" ] || [ "$UNAME" = "FreeBSD" ]; then
    SAGESOFLAGS="-shared -Wl,-soname,libcliquer.so"
    export SAGESOFLAGS
elif [ "$UNAME" = "Darwin" ]; then
    MACOSX_DEPLOYMENT_TARGET="10.3"
    export MACOSX_DEPLOYMENT_TARGET
    SAGESOFLAGS="-dynamiclib -single_module -flat_namespace -undefined dynamic_l
ookup"
    export SAGESOFLAGS
elif [ "$UNAME" = "SunOS" ]; then
    SAGESOFLAGS="-G -Bdynamic"
    export SAGESOFLAGS
elif [ "$UNAME" = "CYGWIN" ]; then
    SAGESOFLAGS="-shared -Wl,-soname,libcliquer.so"
```


Using just


```
elif [ "$UNAME" = "SunOS" ]; then
   SAGESOFLAGS="-shared"
```


was sufficient to produce a shared library which did not exhibit this problem. When Sage was started, Sage no longer produced the libcliquer error message, though it did fail to run properly. 

There are in fact several other libraries in Sage that show show output using the `elfdump` command above. 


```
 * libcliquer.so
 * libecl.so
 * libgroebner-0.6.4.so
 * libpboriCudd-0.6.4.so
 * libpolybori-0.6.4.so 
```

(These were observed on OpenSolaris x64. I've confirmed the same is true of libcliquer.so on 64-bit SPARC using `t2.math`, but I've not verified if all the other libraries show this problem. )

I doubt whether these are the only issues preventing Sage running properly on 64-bit Solaris, but these should be resolved. 

Since 
 * The current version of Cliquer in Sage 1.2 is not the latest.
 * Cliquer 1.2.1 is a bug-fix only release, so should be safe. 
 * The Cliquer test suite can't be run as there's no `spkg-check` file - see #9767

it makes sense to update Cliquer and sort out the Solaris and `spkg-check` issues at the same time. 

Dave 


---

Comment by leif created at 2010-09-08 20:02:25

This is a general error in how Cliquer is adapted to/built for Sage.

It is intended as a stand-alone program, and therefore contains `main()`.

You *must* (or should)  *not* build [shared] libraries containing a `main()` function.

Instead, use `#ifdef ...` and `-D...` depending on what you build. I think Sage should build and install both, the program and a library. (If you remove/omit `main()` for the shared library, the loader problems should vanish.)


```diff
--- cliquer-1.2.p6/src/Makefile	2010-02-16 05:26:57.000000000 +0100
+++ cliquer-1.2.p6/patch/Makefile	2010-02-16 05:26:55.000000000 +0100
@@ -1,14 +1,29 @@
 
 ##### Configurable options:
 
+# Don't need to set any of these compiler variables. They have already been
+# set when running SAGE_ROOT/local/bin/sage-env as part of installing a
+# package.
 ## Compiler:
-CC=gcc
+# CC=gcc
 #CC=cc
 
 ## Compiler flags:
 
 # GCC:  (also -march=pentium etc, for machine-dependent optimizing)
-CFLAGS=-Wall -O3 -fomit-frame-pointer -funroll-loops
+# Build in 64-bit mode on Mac OS X with an Intel processor.
+
+# Flags for building a dynamically linked shared object.
+# SAGESOFLAGS=""
+# ifeq (`uname`, Linux)
+# 	SAGESOFLAGS=-shared -Wl,-soname,libcliquer.so
+# endif
+# ifeq (`uname`, Darwin)
+# 	SAGESOFLAGS=-shared -dynamiclib
+# endif
+# ifeq (`uname`, SunOS)
+# 	SAGESOFLAGS=-G -Bdynamic
+# endif
 
 # GCC w/ debugging:
 #CFLAGS=-Wall -g -DINLINE=
@@ -36,8 +51,7 @@
 	$(CC) $(LDFLAGS) -o $@ testcases.o cliquer.o graph.o reorder.o
 
 cl: cl.o cliquer.o graph.o reorder.o
-	$(CC) $(LDFLAGS) -o $@ cl.o cliquer.o graph.o reorder.o
-
+	$(CC) $(LDFLAGS) $(SAGESOFLAGS) -o libcliquer.so cl.o cliquer.o graph.o reorder.o
 
 cl.o testcases.o cliquer.o graph.o reorder.o: cliquer.h set.h graph.h misc.h reorder.h Makefile cliquerconf.h
 
```

Note the changes made to the `cl` target (which is [the name of] the stand-alone program).

This package really needs work (but there's - besides others - already a ticket (#9871) for an upstream update as well). The files in `src/` are not even vanilla, but contain weird changes in order to use Cliquer as a library from within Sage.


---

Comment by drkirkby created at 2010-09-13 21:57:00

This can be closed when #9871 is closed. 

Another relevant ticket is #9870, which should sort out many of the issues with Cliquer. 

Dave


---

Comment by drkirkby created at 2010-09-16 08:54:53

Minh, 
this ticket can be effectively ignored now. Since #9871 is merged in sage-4.6.alpha1, one might assume it will get to sage-4.6. With hindsight the issue resolved on this ticket should have been resolved here, but I intending updating the source, so created a wider ticket to do that, only to find that was not going to be possible. 

Leif intended resolving #9870. 

I'm not sure what the procedure his here, and whether this should be closed now (since it's merged in sage-4.6.alpha1, or wait until it's merged in sage-4.6. I believe the latter is probably more appropriate, as it could potentially be found to be problematic and not get merged in 4.6 at all. 

Dave


---

Comment by mpatel created at 2010-09-16 21:54:05

I'm closing this ticket as a "duplicate" of #9871.  Please reopen it, if the Cliquer relocation error remains or reappears.


---

Comment by mpatel created at 2010-09-16 21:54:05

Resolution: duplicate
