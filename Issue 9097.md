# Issue 9097: c_lib in Sage library fails to build on OpenSolaris x64

archive/issues_009097.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies f.r.bissey@massey.ac.nz\n\n## Build environment\n* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM\n* OpenSolaris 2009.06 snv_111b X86\n* Sage 4.4.2\n* gcc 4.4.4\n\n## How gcc 4.4.4 was configured\nSince the configuration of gcc is fairly critical on OpenSolaris, here's how it was built. \n\n\n```\ndrkirkby@hawk:~/sage-4.4.2$ gcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.4.4 (GCC) \n```\n\n\ngcc 4.3.4 was failing to build iconv. \n\n## The problem\n\n\n```\n#error \"LONG_BIT definition appears wrong for platform (bad gcc/glibc config?).\"\nscons: *** [src/interrupt.pic.o] Error 1\n*** TOUCHING ALL CYTHON (.pyx) FILES ***\ngcc -o src/interrupt.pic.o -c -fPIC -I/export/home/drkirkby/sage-4.4.2/local/include -I/export/home/drkirkby/sage-4.4.2/local/include/python2.6 -I/export/home/drkirkby/sage-4.4.2/local/include/NTL -Iinclude src/interrupt.c\nIn file included from /export/home/drkirkby/sage-4.4.2/local/include/python2.6/Python.h:58,\n                 from include/stdsage.h:35,\n                 from src/interrupt.c:12:\n/export/home/drkirkby/sage-4.4.2/local/include/python2.6/pyport.h:685:2: error: #error \"LONG_BIT definition appears wrong for platform (bad gcc/glibc config?).\"\nscons: *** [src/interrupt.pic.o] Error 1\nBuilding Sage on Solaris in 64-bit mode\nCreating SAGE_LOCAL/lib/sage-64.txt since it does not exist\nDetected SAGE64 flag\nBuilding Sage on Solaris in 64-bit mode\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\ngcc -o src/interrupt.pic.o -c -fPIC -I/export/home/drkirkby/sage-4.4.2/local/include -I/export/home/drkirkby/sage-4.4.2/local/include/python2.6 -I/export/home/drkirkby/sage-4.4.2/local/include/NTL -Iinclude src/interrupt.c\nIn file included from /export/home/drkirkby/sage-4.4.2/local/include/python2.6/Python.h:58,\n                 from include/stdsage.h:35,\n                 from src/interrupt.c:12:\n/export/home/drkirkby/sage-4.4.2/local/include/python2.6/pyport.h:685:2: error: #error \"LONG_BIT definition appears wrong for platform (bad gcc/glibc config?).\"\nscons: *** [src/interrupt.pic.o] Error 1\nERROR: There was an error building c_lib.\n\nERROR installing SAGE\n\nreal\t0m4.020s\nuser\t0m1.014s\nsys\t0m2.138s\nsage: An error occurred while installing sage-4.4.2\n```\n\n\n## Likely cause\nIt looks as though the -m64 option is not getting through to the library. Since that uses SCons to build, and I don't understand SCons (and very few people seem to), this could be a pig to fix. \n\nIssue created by migration from https://trac.sagemath.org/ticket/9097\n\n",
    "created_at": "2010-05-31T00:49:01Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "c_lib in Sage library fails to build on OpenSolaris x64",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9097",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies f.r.bissey@massey.ac.nz

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

Issue created by migration from https://trac.sagemath.org/ticket/9097





---

archive/issue_comments_084383.json:
```json
{
    "body": "Mercurial patch which adds -m64 when building c_lib.",
    "created_at": "2010-06-14T17:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84383",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Mercurial patch which adds -m64 when building c_lib.



---

archive/issue_comments_084384.json:
```json
{
    "body": "Attachment [c_lib.patch](tarball://root/attachments/some-uuid/ticket9097/c_lib.patch) by drkirkby created at 2010-06-14 17:30:05\n\nThis is not a complete fix which enables the library to build, but it adds the flag -m64 on all platforms except OS X. (On OS X the flag is already added, but along with some other flags which I don't understand, and for now are best left). \n\nDave",
    "created_at": "2010-06-14T17:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84384",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [c_lib.patch](tarball://root/attachments/some-uuid/ticket9097/c_lib.patch) by drkirkby created at 2010-06-14 17:30:05

This is not a complete fix which enables the library to build, but it adds the flag -m64 on all platforms except OS X. (On OS X the flag is already added, but along with some other flags which I don't understand, and for now are best left). 

Dave



---

archive/issue_comments_084385.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-14T17:30:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84385",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084386.json:
```json
{
    "body": "Log file of building on OpenSolaris x64. The section where files are extracted from the tar file have been removed to save space.",
    "created_at": "2010-07-01T00:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84386",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Log file of building on OpenSolaris x64. The section where files are extracted from the tar file have been removed to save space.



---

archive/issue_comments_084387.json:
```json
{
    "body": "Attachment [sage-4.5.alpha1.log](tarball://root/attachments/some-uuid/ticket9097/sage-4.5.alpha1.log) by drkirkby created at 2010-07-01 00:09:43\n\nI'm attaching a log file which shows that this patch allows the build progress to go a long way. The log file for the build of the library `spkg/logs/sage-4.5.alpha1.log` is 958 KB in size, so clearly this gets a long way, where without the 4 lines\n\n\n```\nif env['PLATFORM'] != \"darwin\" and os.environ['SAGE64']==\"yes\": \n    env.Append( CFLAGS=\"-O2 -g -m64\" ) \n    env.Append( CXXFLAGS=\"-O2 -g -m64\" ) \n    env.Append( LINKFLAGS=\"-m64\" ) \n```\n\n\nthe build fails after only 40 lines or so. \n\nThere are some remaining issues to resolve, but this patch, which is only implemented if SAGE64 is set to yes and the operating system is **not** OS X, goes a long way towards helping a 64-bit port to OpenSolaris. \n\nDave",
    "created_at": "2010-07-01T00:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84387",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [sage-4.5.alpha1.log](tarball://root/attachments/some-uuid/ticket9097/sage-4.5.alpha1.log) by drkirkby created at 2010-07-01 00:09:43

I'm attaching a log file which shows that this patch allows the build progress to go a long way. The log file for the build of the library `spkg/logs/sage-4.5.alpha1.log` is 958 KB in size, so clearly this gets a long way, where without the 4 lines


```
if env['PLATFORM'] != "darwin" and os.environ['SAGE64']=="yes": 
    env.Append( CFLAGS="-O2 -g -m64" ) 
    env.Append( CXXFLAGS="-O2 -g -m64" ) 
    env.Append( LINKFLAGS="-m64" ) 
```


the build fails after only 40 lines or so. 

There are some remaining issues to resolve, but this patch, which is only implemented if SAGE64 is set to yes and the operating system is **not** OS X, goes a long way towards helping a 64-bit port to OpenSolaris. 

Dave



---

archive/issue_comments_084388.json:
```json
{
    "body": "I think the patch does the job. But I want to suggest the following patch (sorry I\nhave broken browsers right now because of a messy libpng update and I cannot use the\nattachment form):\n\n\n```\n--- SConstruct.orig\t2010-05-26 12:13:50.000000000 +1200\n+++ SConstruct\t2010-07-01 13:28:53.605754354 +1200\n@@ -105,15 +105,15 @@\n ## The other two options control the way the linker creates a namespace\n ## for the dynamic library; check the man page for ld on a mac to see\n ## the details.\n+if os.environ['SAGE64']==\"yes\":\n+    # We want the debug and optimization flags, since debug symbols are so useful, etc.\n+    print \"MacIntel in 64 bit mode\"\n+    env.Append( CFLAGS=\"-O2 -g -m64\" )\n+    env.Append( CXXFLAGS=\"-O2 -g -m64\" )\n+    env.Append( LINKFLAGS=\"-m64\" )\n+\n if env['PLATFORM']==\"darwin\":\n-    if os.environ['SAGE64']==\"yes\":\n-        # We want the debug and optimization flags, since debug symbols are so useful, etc.\n-        print \"MacIntel in 64 bit mode\"\n-        env.Append( CFLAGS=\"-O2 -g -m64\" )\n-        env.Append( CXXFLAGS=\"-O2 -g -m64\" )\n-        env.Append( LINKFLAGS=\"-m64 -single_module -flat_namespace -undefined dynamic_lookup\" )\n-    else:\n-        env.Append( LINKFLAGS=\"-single_module -flat_namespace -undefined dynamic_lookup\" )\n+    env.Append( LINKFLAGS=\"-single_module -flat_namespace -undefined dynamic_lookup\" )\n \n # SCons doesn't automatically pull in system environment variables\n # However, we only need SAGE_LOCAL, so that's easy.\n```\n\nI think this simplify the logic. The building of extension afterwards is separate.",
    "created_at": "2010-07-01T01:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84388",
    "user": "https://github.com/kiwifb"
}
```

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

archive/issue_comments_084389.json:
```json
{
    "body": "Changing assignee from drkirkby to @kiwifb.",
    "created_at": "2010-07-01T01:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84389",
    "user": "https://github.com/kiwifb"
}
```

Changing assignee from drkirkby to @kiwifb.



---

archive/issue_comments_084390.json:
```json
{
    "body": "Cleaner and proper patch with the same ideas previously shown",
    "created_at": "2010-07-01T09:37:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84390",
    "user": "https://github.com/kiwifb"
}
```

Cleaner and proper patch with the same ideas previously shown



---

archive/issue_comments_084391.json:
```json
{
    "body": "Attachment [sage_clib64.patch](tarball://root/attachments/some-uuid/ticket9097/sage_clib64.patch) by @kiwifb created at 2010-07-01 09:41:01\n\nNote that the space in\n\n```\nLINKFLAGS=\" -single_module -flat_namespace -undefined dynamic_lookup\"\n```\n\nis on purpose as scons concatenate strings. We don't want to end\nup with \"-m64-single_module\".",
    "created_at": "2010-07-01T09:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84391",
    "user": "https://github.com/kiwifb"
}
```

Attachment [sage_clib64.patch](tarball://root/attachments/some-uuid/ticket9097/sage_clib64.patch) by @kiwifb created at 2010-07-01 09:41:01

Note that the space in

```
LINKFLAGS=" -single_module -flat_namespace -undefined dynamic_lookup"
```

is on purpose as scons concatenate strings. We don't want to end
up with "-m64-single_module".



---

archive/issue_comments_084392.json:
```json
{
    "body": "Thank you. \n\nI've put us both as reviews and both as authors. I understand this is OK. I know I initially asked you to remove me. That looks good. I am just about to test.",
    "created_at": "2010-07-04T21:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84392",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thank you. 

I've put us both as reviews and both as authors. I understand this is OK. I know I initially asked you to remove me. That looks good. I am just about to test.



---

archive/issue_comments_084393.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-05T09:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84393",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084394.json:
```json
{
    "body": "Thank you very much. With this, patch applied, along with \n\n* Applying #9399\n* Faking the install of maxima by touching spkg/installed/maxima-$version\n* Faking the install of R by touching /spkg/installed/R-$version\n\nI'm able to get a 64-bit build on OpenSolaris. It does however crash at startup, so the port is not complete! But it is getting pretty close I think. \n\nDave",
    "created_at": "2010-07-05T09:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84394",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Thank you very much. With this, patch applied, along with 

* Applying #9399
* Faking the install of maxima by touching spkg/installed/maxima-$version
* Faking the install of R by touching /spkg/installed/R-$version

I'm able to get a 64-bit build on OpenSolaris. It does however crash at startup, so the port is not complete! But it is getting pretty close I think. 

Dave



---

archive/issue_comments_084395.json:
```json
{
    "body": "Since this touch the OSX build as well do we have a tester for OSX \nthat could try it? 32/64 bit should be irrelevant.",
    "created_at": "2010-07-05T10:04:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84395",
    "user": "https://github.com/kiwifb"
}
```

Since this touch the OSX build as well do we have a tester for OSX 
that could try it? 32/64 bit should be irrelevant.



---

archive/issue_comments_084396.json:
```json
{
    "body": "Replying to [comment:8 fbissey]:\n> Since this touch the OSX build as well do we have a tester for OSX \n> that could try it? 32/64 bit should be irrelevant.\n\nI've tested this on OS X, and it works fine:\n\n\n```\n[kirkby@bsd sage-4.5.alpha1]$ uname -a \nDarwin bsd.local 10.4.0 Darwin Kernel Version 10.4.0: Fri Apr 23 18:28:53 PDT 2010; root:xnu-1504.7.4~1/RELEASE_I386 i386 i386 MacPro1,1 Darwin\n[kirkby@bsd sage-4.5.alpha1]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: 1+1\n2\nsage: Quit\nExiting Sage (CPU time 0m0.04s, Wall time 0m4.44s).\n[kirkby@bsd sage-4.5.alpha1]$ \n```\n\n| Sage Version 4.5.alpha1, Release Date: 2010-06-29                  |\n| Type notebook() for the GUI, and license() for information.        |\nI agree your solution was cleaner than mine, but the reason I wrote it the way I did, was to guarantee that it could have no effect on OS X. \n\nI've also tested it on Linux (sage.math). \n\nDave",
    "created_at": "2010-07-05T15:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84396",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

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

archive/issue_comments_084397.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-08T19:06:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9097#issuecomment-84397",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_009254.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-07-08T19:06:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9097",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9097#event-9254"
}
```
