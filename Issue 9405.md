# Issue 9405: iconv fails to build on OpenSolaris 2008.11 x64  (disk.math)

Issue created by migration from https://trac.sagemath.org/ticket/9405

Original creator: drkirkby

Original creation time: 2010-07-02 01:54:54

Assignee: drkirkby

CC:  was jhpalmieri dimpase

An error occurs when building sage-4.5.alpha1 (with some patches) on disk.math, an OpenSolaris machine running !openSolaros 2008.11 (snv_101b_rc2)

The exact same source builds fine on OpenSolaris 2009.06 which has been updated to build 134. Singular also failed to build on this machine (#9404) as did ATLAS. 

*I suspect some of the tools on this system need updating.*

## Hardware
 * disk.math.washington.edu x64 hardware of some sort. 
 * OpenSolaris 2008.11 (snv_101b)
 * 32 GB RAM
 * 2 x quad core 2.3 GHz CPUs

## GCC Configuration
The configuration of gcc on OpenSolaris is quite critical. This is the GCC included with OpenSolaris 11.2008. 

```
-bash-3.2$ gcc -v
Reading specs from /opt/sfw/lib/gcc/i386-pc-solaris2.11/4.3.2/specs
Target: i386-pc-solaris2.11
Configured with: ./configure --prefix=/opt/sfw --enable-shared --with-gmp=/opt/sfw --with-mpfr=/opt/sfw --with-gnu-as --with-as=/usr/sfw/bin/gas --without-gnu-ld --with-ld=/usr/ccs/bin/ld --enable-stage1-languages=c,c++ --enable-languages=c,c++,objc,fortran
Thread model: posix
gcc driver version 4.3.2 (GCC) executing gcc version 4.2.3
```


GCC is configured to use a rather old version (version 2.15 from 2002) version of the GNU assembler /usr/sfw/bin/gas. I suspect an upgrade of gcc and/or the assembler might cure this. 

## The error message

```
/bin/sh ../libtool --mode=compile gcc -I. -I. -I../include -I./../include -I.. -I./..  -m64 -fvisibility=hidden -DLIBDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\" -DBUILDING_LIBICONV -DBUILDING_DLL -DENABLE_RELOCATABLE=1 -DIN_LIBRARY -DINSTALLDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\" -DNO_XMALLOC -Dset_relocation_prefix=libiconv_set_relocation_prefix -Drelocate=libiconv_relocate -DHAVE_CONFIG_H -c ./iconv.c
/bin/sh ../libtool --mode=compile gcc -I. -I. -I../include -I./../include -I.. -I./..  -m64 -fvisibility=hidden -DLIBDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\" -DBUILDING_LIBICONV -DBUILDING_DLL -DENABLE_RELOCATABLE=1 -DIN_LIBRARY -DINSTALLDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\" -DNO_XMALLOC -Dset_relocation_prefix=libiconv_set_relocation_prefix -Drelocate=libiconv_relocate -DHAVE_CONFIG_H -c ./../libcharset/lib/localcharset.c
/bin/sh ../libtool --mode=compile gcc -I. -I. -I../include -I./../include -I.. -I./..  -m64 -fvisibility=hidden -DLIBDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\" -DBUILDING_LIBICONV -DBUILDING_DLL -DENABLE_RELOCATABLE=1 -DIN_LIBRARY -DINSTALLDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\" -DNO_XMALLOC -Dset_relocation_prefix=libiconv_set_relocation_prefix -Drelocate=libiconv_relocate -DHAVE_CONFIG_H -c ./relocatable.c
libtool: compile:  gcc -I. -I. -I../include -I./../include -I.. -I./.. -m64 -fvisibility=hidden "-DLIBDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\"" -DBUILDING_LIBICONV -DBUILDING_DLL -DENABLE_RELOCATABLE=1 -DIN_LIBRARY "-DINSTALLDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\"" -DNO_XMALLOC -Dset_relocation_prefix=libiconv_set_relocation_prefix -Drelocate=libiconv_relocate -DHAVE_CONFIG_H -c ./iconv.c  -fPIC -DPIC -o .libs/iconv.o
libtool: compile:  gcc -I. -I. -I../include -I./../include -I.. -I./.. -m64 -fvisibility=hidden "-DLIBDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\"" -DBUILDING_LIBICONV -DBUILDING_DLL -DENABLE_RELOCATABLE=1 -DIN_LIBRARY "-DINSTALLDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\"" -DNO_XMALLOC -Dset_relocation_prefix=libiconv_set_relocation_prefix -Drelocate=libiconv_relocate -DHAVE_CONFIG_H -c ./relocatable.c  -fPIC -DPIC -o .libs/relocatable.o
libtool: compile:  gcc -I. -I. -I../include -I./../include -I.. -I./.. -m64 -fvisibility=hidden "-DLIBDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\"" -DBUILDING_LIBICONV -DBUILDING_DLL -DENABLE_RELOCATABLE=1 -DIN_LIBRARY "-DINSTALLDIR=\"/export/home/kirkby/sage-4.5.alpha1/local/lib\"" -DNO_XMALLOC -Dset_relocation_prefix=libiconv_set_relocation_prefix -Drelocate=libiconv_relocate -DHAVE_CONFIG_H -c ./../libcharset/lib/localcharset.c  -fPIC -DPIC -o .libs/localcharset.o
./relocatable.c: In function ‘libiconv_relocate’:
./relocatable.c:466: warning: visibility attribute not supported in this configuration; ignored
./../libcharset/lib/localcharset.c: In function ‘locale_charset’:
./../libcharset/lib/localcharset.c:500: warning: visibility attribute not supported in this configuration; ignored
In file included from ./iconv.c:148:
lib/aliases_syssolaris.gperf: In function ‘aliases_lookup’:
lib/aliases_syssolaris.gperf:389: warning: visibility attribute not supported in this configuration; ignored
/bin/sh ../libtool --mode=link gcc  -m64 -fvisibility=hidden -o libiconv.la -rpath /export/home/kirkby/sage-4.5.alpha1/local/lib -version-info 7:0:5 -no-undefined iconv.lo localcharset.lo relocatable.lo  
libtool: link: gcc -shared -Wl,-z -Wl,text -Wl,-h -Wl,libiconv.so.2 -o .libs/libiconv.so.2.5.0  .libs/iconv.o .libs/localcharset.o .libs/relocatable.o   -lc  -m64  
Text relocation remains                         referenced
    against symbol                  offset      in file
aliases_lookup                      0x1b81b     .libs/iconv.o
aliases_lookup                      0x1b9c1     .libs/iconv.o
aliases_lookup                      0x1beca     .libs/iconv.o
aliases_lookup                      0x1c070     .libs/iconv.o
aliases_lookup                      0x1c935     .libs/iconv.o
ld: fatal: relocations remain against allocatable but non-writable sections
collect2: ld returned 1 exit status
make[3]: *** [libiconv.la] Error 1
make[3]: Leaving directory `/export/home/kirkby/sage-4.5.alpha1/spkg/build/iconv-1.13.1.p2/src/lib'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/kirkby/sage-4.5.alpha1/spkg/build/iconv-1.13.1.p2/src'
Error making iconv

real    1m34.539s
user    0m8.805s
sys     0m11.161s
sage: An error occurred while installing iconv-1.13.1.p2
```



---

Comment by drkirkby created at 2010-08-10 21:41:33

Note, the same problem occurs on OpenSolaris 11/2008 - see #9718


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Outdated, should be closed


---

Comment by mkoeppe created at 2020-07-08 16:51:35

Changing status from new to needs_review.


---

Comment by mjo created at 2020-07-12 20:00:36

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.


---

Comment by mjo created at 2020-07-12 20:00:36

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-07-15 07:18:41

Resolution: invalid


---

Comment by chapoton created at 2020-07-15 07:18:41

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.
