# Issue 8806: update the README.txt in sage-4.4.1 to reflect improved platform and compiler support

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-28 18:02:08

Assignee: mvngu


```
With that in mind, you should probably change README.txt.  It is
woefully out of date, and not tracked by HG as far as I can tell.
E.g.,

NOT OFFICIALLY SUPPORTED, BUT NEARLY WORKS
------------------------------------------

PROCESSOR  OPERATING SYSTEM
SPARC      Solaris 10 -- nearly works
x86        Apple Mac OS X 10.6.x (64-bit) -- see trac #7095.
x86_64     Solaris 10 -- does not work
x86_64     Apple Mac OS X 10.5.x (64-bit) -- needs 64-bit gFortran
          instead of g95

It should also say something about removing /sw from your PATH on Mac.

Karl-Dieter
```



---

Comment by was created at 2010-05-03 03:46:14

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-05-03 07:25:42

Here's the diff between the README.txt in Sage 4.4 and the one in Sage 4.4.1:


```diff
--- README-4.4.txt	2010-05-03 00:08:47.229709868 -0700
+++ README-4.4.1.txt	2010-05-03 00:07:29.129236453 -0700
`@``@` -5,8 +5,8 `@``@`
 
     ./sage
 
-from the command line and you are good to go. If you downloaded the sources,
-please read below on how to build Sage and work around common issues.
+from the command line. If you downloaded the sources, please read
+below on how to build Sage and work around common issues.
 
 
 ---------------------------------------------------------------------------
`@``@` -17,7 +17,7 `@``@`
           Magma, Maple, Mathematica, and Matlab"
 
     Copyright (C) 2005, 2006, 2007, 2008, 2009, 2010
-    William Stein and The Sage Development Team
+    William Stein and the Sage Development Team
 
     Distributed under the terms of the GNU General Public License (GPL)
 
`@``@` -27,7 +27,7 `@``@`
 
          http://groups.google.com/group/sage-support
 
-    AUTHORS: Over 150 people have contributed code to Sage. Please see
+    AUTHORS: Over 200 people have contributed code to Sage. Please see
     one of the websites above for a list. In many cases, documentation
     for modules and functions list the authors.
 
`@``@` -40,7 +40,7 `@``@`
 The following steps briefly outline the process of building Sage from
 source. See below for more detailed instructions.
 
-1. Make sure you have the dependencies and 2 GB of free disk space.
+1. Make sure you have the dependencies and 2.5 GB of free disk space.
 
    Linux (install these using your package manager):
 
`@``@` -89,41 +89,38 `@``@`
 Building of Sage from source is regularly tested on (minimal installs
 of) the following platforms:
 
-PROCESSOR        OPERATING SYSTEM
-x86              32-bit Linux -- Debian, Ubuntu, CentOS (=Red Hat),
-                                 Fedora, openSUSE, Mandriva
-x86_64           64-bit Linux -- Debian, Ubuntu, CentOS (=Red Hat),
-                                 Fedora, openSUSE, Mandriva
-IA-64 Itanium 2  64-bit Linux -- Red Hat, SUSE
-x86              Apple Mac OS X 10.5.x
-PPC              Apple Mac OS X 10.5.x
+  PROCESSOR        OPERATING SYSTEM
+  x86              32-bit Linux -- Debian, Ubuntu, CentOS (=Red Hat),
+                                   Fedora, openSUSE, Mandriva, Arch
+  x86_64           64-bit Linux -- Debian, Ubuntu, CentOS (=Red Hat),
+                                   Fedora, openSUSE, Mandriva, Arch
+  IA-64 Itanium 2  64-bit Linux -- Red Hat, SUSE
+  x86              Apple Mac OS X 10.5.x, 10.6.x
+  PPC              Apple Mac OS X 10.5.x, 10.6.x
+  Sparc            Solaris 10
 
-Use Sage on Microsoft Windows via VirtualBox. We do not always test on
-OS X 10.4, but Sage should work there fine.
+Use Sage on Microsoft Windows via VMware.  Active work to port Sage to
+Cygwin (Windows) is in progress.
 
+NOTE: Sage-4.4 worked on OS X 10.4, but Sage-4.4.1 doesn't. 
 
 NOT OFFICIALLY SUPPORTED, BUT NEARLY WORKS
 ------------------------------------------
 
-PROCESSOR  OPERATING SYSTEM
-SPARC      Solaris 10 -- nearly works
-x86        Apple Mac OS X 10.6.x (64-bit) -- see trac #7095.
-x86_64     Solaris 10 -- does not work
-x86_64     Apple Mac OS X 10.5.x (64-bit) -- needs 64-bit gFortran
-           instead of g95
+  PROCESSOR  OPERATING SYSTEM
+  x86_64     Solaris 10 -- does not work yet
 
 
 NOT SUPPORTED
 -------------
 
-* AIX
-* Arch Linux
-* FreeBSD
-* Gentoo Linux
-* HP-UX
-* Microsoft Windows (via Cygwin)
-* Microsoft Windows (via Visual Studio C++)
-* OpenSolaris (aka Solaris 11). A port will be completed in 2010.
+  * AIX
+  * FreeBSD
+  * Gentoo Linux -- though Sage will probably work fine
+  * HP-UX
+  * Microsoft Windows (via Cygwin) -- active port in progress
+  * Microsoft Windows (via Visual Studio C++)
+  * OpenSolaris
 
 There is some effort to port Sage to FreeBSD and HP-UX. We like all of
 the above operating systems, but just haven't had the time to make
`@``@` -138,11 +135,10 `@``@`
 FORTRAN
 -------
 
-If you are using Fortran on a platform for which Sage does not include
-g95 binaries, you must use a system-wide gFortran. For example, Solaris
-10 does not ship with any Fortran binaries. You need to explicitly
-tell the Sage build process about the Fortran compiler and library
-location. Do this by typing
+To build Sage on any platform except OS X, you must use a system-wide
+gfortran compiler.  Sometimes you need to explicitly tell the Sage
+build process about the Fortran compiler and library location. Do this
+by typing
 
     export SAGE_FORTRAN=/exact/path/to/gfortran
     export SAGE_FORTRAN_LIB=/path/to/fortran/libs/libgfortran.so
`@``@` -163,15 +159,15 `@``@`
 --------------
 
 Sage has significant components written in the following languages:
-C/C++, Python, Lisp, and Fortran. Lisp and Python are built as part of
-Sage and Fortran (g95) is included (x86 Linux and OS X only), so you
-do not need them in order to build Sage.
+C/C++, Python, Cython, Lisp, and Fortran. Lisp (ECL) and Python are
+built as part of Sage and a GNU Fortran (gfortran) binary is included
+(OS X only), so you do not need them in order to build Sage.
 
 
 MORE DETAILED INSTRUCTIONS TO BUILD FROM SOURCE
 -----------------------------------------------
 
-1. Make sure you have about 2 GB of free disk space.
+1. Make sure you have about 2.5 GB of free disk space.
 
 2. Linux: Install GCC, g++, m4, ranlib, and make. The build should
    work fine on openSUSE, Fedora, Ubuntu, etc. If it doesn't, we want
`@``@` -256,22 +252,10 `@``@`
 SUPPORTED COMPILERS
 -------------------
 
-* Sage builds with GCC >= 3.x, GCC >= 4.0.1, and GCC >= 4.1.x.
-* Sage will not build with GCC 2.9.x.
-* WARNING: Don't build with GCC 4.0.0, which is very buggy.
-* Sage has never been built without using GCC compiler.
-
-
-RUNNING SAGE
-------------
-
-1. Try running Sage:
-
-       ./sage
-
-2. Try running an example Sage script:
-
-       ./sage example.sage
+ * Sage builds with GCC >= 3.x, GCC >= 4.0.1, and GCC >= 4.1.x.
+ * Sage will not build with GCC 2.9.x.
+ * WARNING: Don't build with GCC 4.0.0, which is very buggy.
+ * Sage has never been built without using the GCC compiler.
 
 
 RELOCATION
`@``@` -308,10 +292,9 `@``@`
    installed by typing "sage -bdist x.y.z". The result is placed in
    the SAGE_ROOT/dist directory.
 
-3. Fat Binaries: This *does not* work at all yet (as of Nov 14, 2009).
-   To make a binary that will run on the widest range of target
-   machines, set the SAGE_FAT_BINARY environment variable to "yes"
-   before building Sage:
+3. Fat Binaries: To make a binary that will run on the widest range of
+   target machines, set the SAGE_FAT_BINARY environment variable to
+   "yes" before building Sage:
 
        export SAGE_FAT_BINARY="yes"
        make
`@``@` -322,10 +305,8 `@``@`
 ----------------------------
 
 All software included with Sage is copyright by the respective authors
-and released under an open source license that is GPL compatible. See
-the file COPYING.txt for more details. (NOTE: jsMath is licensed
-under the Apache license. Apache claim their license is GPL
-compatible, but Stallman disagrees.)
+and released under an open source license that is "GPL version 3 or
+later"q compatible. See the file COPYING.txt for more details.
 
 Each spkg in SAGE_ROOT/spkg/standard/ is a bzip'd tarball. You can
 extract it with
```


The changes are OK. But I don't understand why there's a "q" appended to the word "later". That is, this line:


```
+later"q compatible. See the file COPYING.txt for more details.
```


If it's a typo, it is a trivial typo that can be fixed in Sage 4.4.2. Anyway, the updated README.txt fixes many issues at #7484.


---

Comment by mvngu created at 2010-05-03 07:25:42

Resolution: fixed


---

Comment by kcrisman created at 2010-05-03 14:56:36

Just a very minor point to go along with Minh's potential followup ticket for the "q":

```
PPC              Apple Mac OS X 10.5.x, 10.6.x 
```

is wrong as well, since of course Apple intentionally removed PPC support from OS X 10.6.
