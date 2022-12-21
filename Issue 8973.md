# Issue 8973: surf does not build (gcc 4.4.4)

Issue created by migration from Trac.

Original creator: mmezzarobba

Original creation time: 2010-05-15 16:01:44

Assignee: tbd

CC:  benjaminfjones dimpase

The experimental spkg "surf-1.1" does not build with gcc-4.4.4. The following patch works for me.


```
diff -ru a/surf/draw/SurfaceCalc.cc b/surf-1.1/surf/draw/SurfaceCalc.cc
--- a/surf/draw/SurfaceCalc.cc  2004-11-08 11:00:43.000000000 +0100
+++ b/surf-1.1/surf/draw/SurfaceCalc.cc 2010-05-15 17:48:38.663596876 +0200
`@``@` -38,6 +38,7 `@``@`
 #include <IO.h>
 
 #include <math.h>
+#include <cstring>
 
 extern double Y_AXIS_LR_ROTATE;
 
diff -ru a/surf/image-formats/ByExtension.cc b/surf-1.1/surf/image-formats/ByExtension.cc
--- a/surf/image-formats/ByExtension.cc 2003-04-14 17:12:37.000000000 +0200
+++ b/surf-1.1/surf/image-formats/ByExtension.cc        2010-05-15 17:47:47.707096842 +0200
`@``@` -26,7 +26,8 `@``@`
 
 #include <AvailableImageFormats.h>
 
-#include<iostream>
+#include <iostream>
+#include <cstring>
 
 namespace ImageFormats {
 
`@``@` -87,7 +88,7 `@``@`
                }
 
                // just look for "*.extension"
-               char* ext = strrchr(filename, '.');
+               const char* ext = strrchr(filename, '.');
                if (ext == 0) {
                        return 0;
                }
diff -ru a/surf/misc/IO.cc b/surf-1.1/surf/misc/IO.cc
--- a/surf/misc/IO.cc   2006-02-12 14:36:26.000000000 +0100
+++ b/surf-1.1/surf/misc/IO.cc  2010-05-15 17:49:12.939096803 +0200
`@``@` -27,6 +27,8 `@``@`
 
 #include <errno.h>
 
+#include <cstdlib>
+
 #ifdef HAVE_UNISTD_H
 #  include <unistd.h>
 #endif
diff -ru a/surf/src/init_parser.cc b/surf-1.1/surf/src/init_parser.cc
--- a/surf/src/init_parser.cc   2002-06-09 15:29:17.000000000 +0200
+++ b/surf-1.1/surf/src/init_parser.cc  2010-05-15 17:45:32.318586702 +0200
`@``@` -32,8 +32,8 `@``@`
 #include <monomarith.h>
 #include <AvailableImageFormats.h>
 
-#include<cstdio>
-#include<string>
+#include <cstdio>
+#include <cstring>
 
 using namespace ScriptVar;
```



---

Comment by benjaminfjones created at 2012-05-27 18:39:56

Changing keywords from "" to "sd40.5".


---

Comment by benjaminfjones created at 2012-05-29 04:10:00

I've produced a new spkg for surf-1.1 called surf-1.1.p0. 

http://sage.math.washington.edu/home/bjones/surf-1.1.p0.spkg

This the first spkg I've "packaged", but I followed the developer's guide so I think it's close to being proper. The existing surf-1.1.spkg was produced in 2006 and doesn't conform at all to the current standards (including not having any hg repo, no SPKG.txt, etc..) I've checked that it builds successfully on Mac OS X, sage-5.1.beta0. 

On debian linux, there is a problem during `./configure`. I don't have much experience with autotools, so need some help there.

```
configure: error: cannot find install-sh or install.sh in "." "./.." "./../.."
```


Please test and report back.


---

Comment by kcrisman created at 2012-05-29 04:19:57

I'm wondering whether we might as well use [surf 1.0.6](http://sourceforge.net/projects/surf/files/surf/1.0.6/), since apparently 1.1 never appeared.

Testing nonetheless...


---

Comment by kcrisman created at 2012-05-29 04:33:25

On sage.math:

```
Making all in docs
make[2]: Entering directory `/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/spkg/build/surf-1.1.p0/src/docs'
Updating ./version.texi
restore=: && backupdir=".am$$" && \
	am__cwd=`pwd` && cd . && \
	rm -rf $backupdir && mkdir $backupdir && \
	if (/bin/bash /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/spkg/build/surf-1.1.p0/src/missing --run makeinfo --version) >/dev/null 2>&1; then \
	  for f in surf.info surf.info-[0-9] surf.info-[0-9][0-9] surf.i[0-9] surf.i[0-9][0-9]; do \
	    if test -f $f; then mv $f $backupdir; restore=mv; else :; fi; \
	  done; \
	else :; fi && \
	cd "$am__cwd"; \
	if /bin/bash /home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/spkg/build/surf-1.1.p0/src/missing --run makeinfo   -I . \
	 -o surf.info surf.texi; \
	then \
	  rc=0; \
	  cd .; \
	else \
	  rc=$?; \
	  cd . && \
	  $restore $backupdir/* `echo "./surf.info" | sed 's|[^/]*$||'`; \
	fi; \
	rm -rf $backupdir; exit $rc
/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/spkg/build/surf-1.1.p0/src/missing: line 54: makeinfo: command not found
WARNING: `makeinfo' is missing on your system.  You should only need it if
         you modified a `.texi' or `.texinfo' file, or any other file
         indirectly affecting the aspect of the manual.  The spurious
         call might also be the consequence of using a buggy `make' (AIX,
         DU, IRIX).  You might want to install the `Texinfo' package or
         the `GNU make' package.  Grab either from any GNU archive site.
make[2]: *** [surf.info] Error 1
make[2]: Leaving directory `/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/spkg/build/surf-1.1.p0/src/docs'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/kcrisman/sage-5.1.beta1-boxen-x86_64-Linux/spkg/build/surf-1.1.p0/src'
make: *** [all] Error 2
Error building PACKAGE_NAME.

real	0m33.030s
user	0m19.410s
sys	0m8.280s
************************************************************************
Error installing package surf-1.1.p0
************************************************************************
```

But the package itself built.


---

Comment by kcrisman created at 2012-05-29 04:36:35

Successful build all the way on Mac OS X 10.6 - it ignored a warning about help2man, otherwise seems fine.


---

Comment by benjaminfjones created at 2012-05-29 14:47:48

Repackaged version at http://sage.math.washington.edu/home/bjones/surf-1.1.p0.spkg now passes `./configure` on debian squeeze with autoconf installed. Still working on getting it to build.


---

Comment by kcrisman created at 2012-06-01 19:03:27

See also #6316.  Apparently Surf has become slightly higher priority since then, given that this was a "high priority" bug at Sage Days 40.5.

Also, "surfer" and even more recent post-surf things building on it might be more useful in any case.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by mmezzarobba created at 2020-10-31 07:24:34

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-11-01 10:02:58

Resolution: invalid
