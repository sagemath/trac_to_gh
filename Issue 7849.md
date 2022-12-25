# Issue 7849: MPRI issue with Sun Studio and --enable-cxx

archive/issues_007849.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  wbhart @jaapspies\n\nSun's recent compilers for Solaris (and I assume Linux too), ship with two standard C++ libraries:\n\nhttp://developers.sun.com/solaris/articles/cmp_stlport_libCstd.html\n\n* libCstd for backward compatibility with the old C+++ standard\n* libstlport for almost 100% compatibility with the latest C++ standard. (If Wikipedia is to be believe, there is no C++ compiler in existence which is 100% compatible). \n\nPolyBoRi will not build without the newer library. Since libraries can't be mixed and backward compatibility to a library released before Sage was released is not important. It therefore makes sensce to use the latest library on Solaris. That means adding the option\n\n\n```\n-library=stlport4.\n```\n\n\nto CXXFLAGS. \n\nSomething like the following show allow a 64-bit build of Sage (though many bits do not work yet). \n\n\n```\n$ export CC=/opt/sunstudio12.1/bin/cc\n$ export CXX=/opt/sunstudio12.1/bin/CC\n$ export CFLAGS=-m64\n$ export CXXFLAGS=-m64 \n$ export ABI=64\n$ configure --enable-cxx\n$ make\n$ make check\n```\n\n\nMPIR is one such package. Bill Hart suggested a fix:\n\n-----\nTry #including stddef.h and stdarg.h in gmp-h.in.\n\nProbably that won't be the end of the problems....\n\nBill Hart\n-----\nI will simply added this temporary fix to the stop of the file. It did fix the problem. but Bill notes it needs more extensive testing on other platforms. \n\nI'll probably add a patch in Sage, which only includes the fix for the Sun Studio compilers. There's nothing in that web page from Sun to indicate the problem is specific to Solaris (Sun also ships Sun Studio for Linux), so I'll **not** make it Solaris specific, but only Sun Studio specific. That's easy using the script \n\n\n```\n$SAGE_LOCAL/bin/testcxx.sh\n```\n\n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/7849\n\n",
    "created_at": "2010-01-05T13:39:03Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "MPRI issue with Sun Studio and --enable-cxx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7849",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  wbhart @jaapspies

Sun's recent compilers for Solaris (and I assume Linux too), ship with two standard C++ libraries:

http://developers.sun.com/solaris/articles/cmp_stlport_libCstd.html

* libCstd for backward compatibility with the old C+++ standard
* libstlport for almost 100% compatibility with the latest C++ standard. (If Wikipedia is to be believe, there is no C++ compiler in existence which is 100% compatible). 

PolyBoRi will not build without the newer library. Since libraries can't be mixed and backward compatibility to a library released before Sage was released is not important. It therefore makes sensce to use the latest library on Solaris. That means adding the option


```
-library=stlport4.
```


to CXXFLAGS. 

Something like the following show allow a 64-bit build of Sage (though many bits do not work yet). 


```
$ export CC=/opt/sunstudio12.1/bin/cc
$ export CXX=/opt/sunstudio12.1/bin/CC
$ export CFLAGS=-m64
$ export CXXFLAGS=-m64 
$ export ABI=64
$ configure --enable-cxx
$ make
$ make check
```


MPIR is one such package. Bill Hart suggested a fix:

-----
Try #including stddef.h and stdarg.h in gmp-h.in.

Probably that won't be the end of the problems....

Bill Hart
-----
I will simply added this temporary fix to the stop of the file. It did fix the problem. but Bill notes it needs more extensive testing on other platforms. 

I'll probably add a patch in Sage, which only includes the fix for the Sun Studio compilers. There's nothing in that web page from Sun to indicate the problem is specific to Solaris (Sun also ships Sun Studio for Linux), so I'll **not** make it Solaris specific, but only Sun Studio specific. That's easy using the script 


```
$SAGE_LOCAL/bin/testcxx.sh
```


Dave 

Issue created by migration from https://trac.sagemath.org/ticket/7849





---

archive/issue_comments_067869.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-05T21:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7849#issuecomment-67869",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067870.json:
```json
{
    "body": "I added \n\n\n```\nif [ \"x`uname`\" = \"xSunOS\" ] ; then\n   echo \"Copying a version of gmp-h.in which is patched for Sun Studio\"\n   cp patches/gmp-h.in src/\n   if ! [ $? -eq 0 ]; then\n      echo \"Failed to patch for Sun Studio\"\n      exit 1\n   fi\nfi\n```\n\n\nto spkg-install, so the file is only copied over on Solaris. The actual changes to the file gmp-h.in are the addition of these few lines\n\n\n```\n#ifdef __SUNPRO_CC    /* See: http://trac.sagemath.org/sage_trac/ticket/7849 */\n#include <stddef.h>   /* This is Bill Hart's fix, but I've applied it only */\n#include <stdarg.h>   /* on Sun Studio */\n#endif \n```\n\n\nWhether this patch should be applied on Linux or not is unknown - in any case, Linux systems running Sun Studio are very rare. Currently the patch is applied on all Solaris systems, but is only seen by the Sun C++ compiler, not by g++. \n\nhttp://boxen.math.washington.edu/home/kirkby/portability/mpir-1.2.2.p0/\n\n**Here's the errors before the fix** \n\n```\n\ndrkirkby@hawk:~/sage-4.3.1.alpha0$ ./sage -f mpir-1.2.2\n\n<SNIP> \n\n /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c isfuns.cc  -KPIC -DPIC -o .libs/isfuns.o\n/bin/sh ../libtool --tag=CXX --mode=compile /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I..    -m64 -library=stlport4 -c -o ismpf.lo ismpf.cc\n /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c ismpf.cc  -KPIC -DPIC -o .libs/ismpf.o\n/bin/sh ../libtool --tag=CXX --mode=compile /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I..    -m64 -library=stlport4 -c -o ismpq.lo ismpq.cc\n /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c ismpq.cc  -KPIC -DPIC -o .libs/ismpq.o\n/bin/sh ../libtool --tag=CXX --mode=compile /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I..    -m64 -library=stlport4 -c -o ismpz.lo ismpz.cc\n /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c ismpz.cc  -KPIC -DPIC -o .libs/ismpz.o\n/bin/sh ../libtool --tag=CXX --mode=compile /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I..    -m64 -library=stlport4 -c -o ismpznw.lo ismpznw.cc\n /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c ismpznw.cc  -KPIC -DPIC -o .libs/ismpznw.o\n/bin/sh ../libtool --tag=CXX --mode=compile /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I..    -m64 -library=stlport4 -c -o osdoprnti.lo osdoprnti.cc\n /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c osdoprnti.cc  -KPIC -DPIC -o .libs/osdoprnti.o\n\"../mpir.h\", line 629: Error: va_list is not defined.\n\"../mpir.h\", line 634: Error: va_list is not defined.\n\"../mpir.h\", line 639: Error: va_list is not defined.\n\"../mpir.h\", line 644: Error: va_list is not defined.\n\"../mpir.h\", line 649: Error: va_list is not defined.\n\"../mpir.h\", line 668: Error: va_list is not defined.\n\"../mpir.h\", line 673: Error: va_list is not defined.\n\"../mpir.h\", line 678: Error: va_list is not defined.\n\"../gmp-impl.h\", line 3682: Error: va_list is not defined.\n\"../gmp-impl.h\", line 3785: Error: va_list is not defined.\n\"../gmp-impl.h\", line 3791: Error: va_list is not defined.\n\"../gmp-impl.h\", line 3811: Error: va_list is not defined.\n12 Error(s) detected.\nmake[2]: *** [osdoprnti.lo] Error 1\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2/src/cxx'\nmake[1]: *** [all-recursive] Error 1\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2/src'\nmake: *** [all] Error 2\nError building MPIR.\n```\n\n\n\n**Here's the result ofter the fix**\n\n```\ndrkirkby@hawk:~/sage-4.3.1.alpha0$ ./sage -f mpir-1.2.2.p0\n<SNIP>\n+-------------------------------------------------------------+\n+-------------------------------------------------------------+\n| CAUTION:                                                    |\n|                                                             |\n| If you have not already run \"make check\", then we strongly  |\n| recommend you do so.                                        |\n|                                                             |\n| MPIR has been carefully tested by its authors, but compilers|\n| are all too often released with serious bugs.  MPIR tends to|\n| explore interesting corners in compilers and has hit bugs   |\n| on quite a few occasions.                                   |\n|                                                             |\nmake[4]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2.p0/src'\nmake[3]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2.p0/src'\nmake[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2.p0/src'\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2.p0/src'\n\nreal\t0m56.690s\nuser\t0m27.805s\nsys\t0m30.550s\nSuccessfully installed mpir-1.2.2.p0\n```\n\nAnd when 'make check' was run outside of Sage, all tests passed. \n\n\nDave",
    "created_at": "2010-01-05T21:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7849#issuecomment-67870",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I added 


```
if [ "x`uname`" = "xSunOS" ] ; then
   echo "Copying a version of gmp-h.in which is patched for Sun Studio"
   cp patches/gmp-h.in src/
   if ! [ $? -eq 0 ]; then
      echo "Failed to patch for Sun Studio"
      exit 1
   fi
fi
```


to spkg-install, so the file is only copied over on Solaris. The actual changes to the file gmp-h.in are the addition of these few lines


```
#ifdef __SUNPRO_CC    /* See: http://trac.sagemath.org/sage_trac/ticket/7849 */
#include <stddef.h>   /* This is Bill Hart's fix, but I've applied it only */
#include <stdarg.h>   /* on Sun Studio */
#endif 
```


Whether this patch should be applied on Linux or not is unknown - in any case, Linux systems running Sun Studio are very rare. Currently the patch is applied on all Solaris systems, but is only seen by the Sun C++ compiler, not by g++. 

http://boxen.math.washington.edu/home/kirkby/portability/mpir-1.2.2.p0/

**Here's the errors before the fix** 

```

drkirkby@hawk:~/sage-4.3.1.alpha0$ ./sage -f mpir-1.2.2

<SNIP> 

 /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c isfuns.cc  -KPIC -DPIC -o .libs/isfuns.o
/bin/sh ../libtool --tag=CXX --mode=compile /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I..    -m64 -library=stlport4 -c -o ismpf.lo ismpf.cc
 /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c ismpf.cc  -KPIC -DPIC -o .libs/ismpf.o
/bin/sh ../libtool --tag=CXX --mode=compile /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I..    -m64 -library=stlport4 -c -o ismpq.lo ismpq.cc
 /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c ismpq.cc  -KPIC -DPIC -o .libs/ismpq.o
/bin/sh ../libtool --tag=CXX --mode=compile /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I..    -m64 -library=stlport4 -c -o ismpz.lo ismpz.cc
 /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c ismpz.cc  -KPIC -DPIC -o .libs/ismpz.o
/bin/sh ../libtool --tag=CXX --mode=compile /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I..    -m64 -library=stlport4 -c -o ismpznw.lo ismpznw.cc
 /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c ismpznw.cc  -KPIC -DPIC -o .libs/ismpznw.o
/bin/sh ../libtool --tag=CXX --mode=compile /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I..    -m64 -library=stlport4 -c -o osdoprnti.lo osdoprnti.cc
 /opt/sunstudio12.1/bin/CC -DHAVE_CONFIG_H -I. -I. -I.. -D__GMP_WITHIN_GMPXX -I.. -m64 -library=stlport4 -c osdoprnti.cc  -KPIC -DPIC -o .libs/osdoprnti.o
"../mpir.h", line 629: Error: va_list is not defined.
"../mpir.h", line 634: Error: va_list is not defined.
"../mpir.h", line 639: Error: va_list is not defined.
"../mpir.h", line 644: Error: va_list is not defined.
"../mpir.h", line 649: Error: va_list is not defined.
"../mpir.h", line 668: Error: va_list is not defined.
"../mpir.h", line 673: Error: va_list is not defined.
"../mpir.h", line 678: Error: va_list is not defined.
"../gmp-impl.h", line 3682: Error: va_list is not defined.
"../gmp-impl.h", line 3785: Error: va_list is not defined.
"../gmp-impl.h", line 3791: Error: va_list is not defined.
"../gmp-impl.h", line 3811: Error: va_list is not defined.
12 Error(s) detected.
make[2]: *** [osdoprnti.lo] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2/src/cxx'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2/src'
make: *** [all] Error 2
Error building MPIR.
```



**Here's the result ofter the fix**

```
drkirkby@hawk:~/sage-4.3.1.alpha0$ ./sage -f mpir-1.2.2.p0
<SNIP>
+-------------------------------------------------------------+
+-------------------------------------------------------------+
| CAUTION:                                                    |
|                                                             |
| If you have not already run "make check", then we strongly  |
| recommend you do so.                                        |
|                                                             |
| MPIR has been carefully tested by its authors, but compilers|
| are all too often released with serious bugs.  MPIR tends to|
| explore interesting corners in compilers and has hit bugs   |
| on quite a few occasions.                                   |
|                                                             |
make[4]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2.p0/src'
make[3]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2.p0/src'
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2.p0/src'
make[1]: Leaving directory `/export/home/drkirkby/sage-4.3.1.alpha0/spkg/build/mpir-1.2.2.p0/src'

real	0m56.690s
user	0m27.805s
sys	0m30.550s
Successfully installed mpir-1.2.2.p0
```

And when 'make check' was run outside of Sage, all tests passed. 


Dave



---

archive/issue_comments_067871.json:
```json
{
    "body": "Changing component from porting to solaris.",
    "created_at": "2010-01-05T21:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7849#issuecomment-67871",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from porting to solaris.



---

archive/issue_comments_067872.json:
```json
{
    "body": "This does not work when Sun Studio is not installed (or not the favorite compiler!).\n\n\n\n```\nHost system\nuname -a:\nSunOS opensolaris 5.11 snv_111b i86pc i386 i86pc Solaris\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.3.2/configure --prefix=/usr --program-suffix=-4.3.2 --infodir=/usr/share/info --mandir=/usr/share/man --libexecdir=/usr/lib --enable-shared --disable-static --disable-libtool-lock --target= --enable-objc-gc --enable-concept-checks --disable-libada --enable-libssp --enable-languages=c,c++,objc,fortran --enable-threads=posix --enable-tls=yes --with-system-zlib --without-gnu-ld --with-ld=/usr/ccs/bin/ld --with-gnu-as --with-as=/usr/sfw/bin/gas --with-gmp-include=/usr/include/gmp --with-gmp-lib=/usr/lib --with-mpfr-include=/usr/include/mpfr --with-mpfr-lib=/usr/lib --enable-c99 --enable-nls --enable-wchar_t --enable-libstdcxx-allocator=mt --with-pic\nThread model: posix\ngcc version 4.3.2 (GCC) \n****************************************************\nCopying a version of gmp-h.in which is patched for Sun Studio\nBuilding 64 bit Solaris version\nchecking build system type... i486-pc-solaris2.11\nchecking host system type... i486-pc-solaris2.11\nchecking for a BSD-compatible install... /usr/bin/ginstall -c\nchecking whether build environment is sane... yes\nchecking for gawk... gawk\nchecking whether make sets $(MAKE)... yes\nchecking whether to enable maintainer-specific portions of Makefiles... no\nconfigure: error: ABI=64 is not among the following valid choices: 32\nFailed to configure.\n\nreal\t0m1.593s\nuser\t0m0.175s\nsys\t0m0.430s\nsage: An error occurred while installing mpir-1.2.2.p0\n\n```\n\n\nI think there is more work to do.\n\nJaap",
    "created_at": "2010-01-07T16:12:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7849#issuecomment-67872",
    "user": "https://github.com/jaapspies"
}
```

This does not work when Sun Studio is not installed (or not the favorite compiler!).



```
Host system
uname -a:
SunOS opensolaris 5.11 snv_111b i86pc i386 i86pc Solaris
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.3.2/configure --prefix=/usr --program-suffix=-4.3.2 --infodir=/usr/share/info --mandir=/usr/share/man --libexecdir=/usr/lib --enable-shared --disable-static --disable-libtool-lock --target= --enable-objc-gc --enable-concept-checks --disable-libada --enable-libssp --enable-languages=c,c++,objc,fortran --enable-threads=posix --enable-tls=yes --with-system-zlib --without-gnu-ld --with-ld=/usr/ccs/bin/ld --with-gnu-as --with-as=/usr/sfw/bin/gas --with-gmp-include=/usr/include/gmp --with-gmp-lib=/usr/lib --with-mpfr-include=/usr/include/mpfr --with-mpfr-lib=/usr/lib --enable-c99 --enable-nls --enable-wchar_t --enable-libstdcxx-allocator=mt --with-pic
Thread model: posix
gcc version 4.3.2 (GCC) 
****************************************************
Copying a version of gmp-h.in which is patched for Sun Studio
Building 64 bit Solaris version
checking build system type... i486-pc-solaris2.11
checking host system type... i486-pc-solaris2.11
checking for a BSD-compatible install... /usr/bin/ginstall -c
checking whether build environment is sane... yes
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether to enable maintainer-specific portions of Makefiles... no
configure: error: ABI=64 is not among the following valid choices: 32
Failed to configure.

real	0m1.593s
user	0m0.175s
sys	0m0.430s
sage: An error occurred while installing mpir-1.2.2.p0

```


I think there is more work to do.

Jaap



---

archive/issue_comments_067873.json:
```json
{
    "body": "Hi Jaap, \n\nI believe the MPIR error message you show:\n\n\n```\nconfigure: error: ABI=64 is not among the following valid choices: 32\n```\n\n\nis related to 32/64-bit issues you have, and are **totally unrelated** to this fix which is very specific for Sun Studio. The two extra include files, which are only included with Sun Studio\n\n\n```\n#ifdef __SUNPRO_CC    /* See: http://trac.sagemath.org/sage_trac/ticket/7849 */\n#include <stddef.h>   /* This is Bill Hart's fix, but I've applied it only */\n#include <stdarg.h>   /* on Sun Studio */\n#endif\n```\n\n\ncan't change any issues with the ABI. That looks like an issue with compiler flags or a broken set of build tools. \n\nI've just created a copy my gcc 4.3.4 and bintils 2.20 binaries, and are in the process of uploading them to a server at the University of Washington. I'll give you a link later by email. It might eliminate the possibility your compiler is broken in some way. \n\nThis particular fix is not a high priority one, but it would be nice to get it in at some point. I think Bill's two header files are totally safe, as I've put them inside compiler directives which are only defined with the Sun C++ compiler - not even the Sun C compiler will see them.  \n\nDave",
    "created_at": "2010-01-07T18:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7849#issuecomment-67873",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Hi Jaap, 

I believe the MPIR error message you show:


```
configure: error: ABI=64 is not among the following valid choices: 32
```


is related to 32/64-bit issues you have, and are **totally unrelated** to this fix which is very specific for Sun Studio. The two extra include files, which are only included with Sun Studio


```
#ifdef __SUNPRO_CC    /* See: http://trac.sagemath.org/sage_trac/ticket/7849 */
#include <stddef.h>   /* This is Bill Hart's fix, but I've applied it only */
#include <stdarg.h>   /* on Sun Studio */
#endif
```


can't change any issues with the ABI. That looks like an issue with compiler flags or a broken set of build tools. 

I've just created a copy my gcc 4.3.4 and bintils 2.20 binaries, and are in the process of uploading them to a server at the University of Washington. I'll give you a link later by email. It might eliminate the possibility your compiler is broken in some way. 

This particular fix is not a high priority one, but it would be nice to get it in at some point. I think Bill's two header files are totally safe, as I've put them inside compiler directives which are only defined with the Sun C++ compiler - not even the Sun C compiler will see them.  

Dave



---

archive/issue_comments_067874.json:
```json
{
    "body": "Note that the reason for Jaap only getting the offer an ABI of 32 is that his processor is incorrectly identified as a 486. \n\n\n```\nchecking build system type... i486-pc-solaris2.11\nchecking host system type... i486-pc-solaris2.11 \n```\n\n\nHence the fix here, which adds a couple of files only with the Sun C++ compiler, is unrelated to the fact the configure script incorrectly determines the CPU to be a 486, and so therefore only 32-bit. \n\nDave",
    "created_at": "2010-01-13T05:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7849#issuecomment-67874",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Note that the reason for Jaap only getting the offer an ABI of 32 is that his processor is incorrectly identified as a 486. 


```
checking build system type... i486-pc-solaris2.11
checking host system type... i486-pc-solaris2.11 
```


Hence the fix here, which adds a couple of files only with the Sun C++ compiler, is unrelated to the fact the configure script incorrectly determines the CPU to be a 486, and so therefore only 32-bit. 

Dave



---

archive/issue_comments_067875.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-13T22:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7849#issuecomment-67875",
    "user": "https://github.com/peterjeremy"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067876.json:
```json
{
    "body": "The actual code change only affects Sun Studio compilers so I'll accept that David Kirby knows what he is doing here.",
    "created_at": "2010-01-13T22:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7849#issuecomment-67876",
    "user": "https://github.com/peterjeremy"
}
```

The actual code change only affects Sun Studio compilers so I'll accept that David Kirby knows what he is doing here.



---

archive/issue_comments_067877.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T01:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7849#issuecomment-67877",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
