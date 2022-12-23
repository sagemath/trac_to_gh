# Issue 7067: cddlib 094f fails to build with Sun Studio - fabs() unresolved. Probably needs -lm

Issue created by migration from https://trac.sagemath.org/ticket/7067

Original creator: drkirkby

Original creation time: 2009-09-29 12:54:27

Assignee: tbd

Using

    * Solaris 10 update 7 on SPARC
    * sage-4.1.2.alpha2
    * Sun Studio 12.1
    * An updated configure script to allow the Sun compiler to be used. 

I find that cddlib. This looks like fabs() is an unresolved external, which is not surprising given the maths library libm is not linked in.  This should be easy to fix. 


```
cddlib-094f/.hg/00changelog.i
cddlib-094f/patches/
cddlib-094f/patches/allfaces.c.diff
cddlib-094f/patches/allfaces.c
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v
usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
checking for a BSD-compatible install... /usr/local/bin/ginstall -c
checking whether build environment is sane... yes
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking for gcc... /opt/xxxsunstudio12.1/bin/cc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables...
checking for suffix of object files... o
checking whether we are using the GNU C compiler... no
checking whether /opt/xxxsunstudio12.1/bin/cc accepts -g... yes
checking for /opt/xxxsunstudio12.1/bin/cc option to accept ISO C89... none needed
checking for style of include used by make... GNU
checking dependency style of /opt/xxxsunstudio12.1/bin/cc... none
checking for a BSD-compatible install... /usr/local/bin/ginstall -c
checking for ranlib... ranlib
checking for main in -lgmp... yes
checking how to run the C preprocessor... /opt/xxxsunstudio12.1/bin/cc -E
checking for grep that handles long lines and -e... /usr/sfw/bin/ggrep
checking for egrep... /usr/sfw/bin/ggrep -E
checking for ANSI C header files... yes
checking for an ANSI C-conforming const... yes
configure: creating ./config.status
config.status: creating lib-src/Makefile
config.status: WARNING:  lib-src/Makefile.in seems to ignore the --datarootdir setting
config.status: creating src/Makefile
config.status: WARNING:  src/Makefile.in seems to ignore the --datarootdir setting
config.status: creating lib-src-gmp/Makefile
config.status: WARNING:  lib-src-gmp/Makefile.in seems to ignore the --datarootdir setting
config.status: creating src-gmp/Makefile
config.status: WARNING:  src-gmp/Makefile.in seems to ignore the --datarootdir setting
config.status: creating Makefile
config.status: WARNING:  Makefile.in seems to ignore the --datarootdir setting
config.status: executing depfiles commands
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/cddlib-094f/src'
Making all in lib-src
make[3]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/cddlib-094f/src/lib-src'
source='cddcore.c' object='cddcore.o' libtool=no \
depfile='.deps/cddcore.Po' tmpdepfile='.deps/cddcore.TPo' \
depmode=none /bin/bash ../depcomp \
/opt/xxxsunstudio12.1/bin/cc -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"cddlib\" -DVERSION=\"0.94\" -DHAVE_LIBGMP=1 -DSTDC_HEADERS=1 -I. -I.  -UGMPRATIONAL   -I /export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib  -c `test -f 'cddcore.c' || echo './'`cddcore.c
source='cddlp.c' object='cddlp.o' libtool=no \
depfile='.deps/cddlp.Po' tmpdepfile='.deps/cddlp.TPo' \
depmode=none /bin/bash ../depcomp \
/opt/xxxsunstudio12.1/bin/cc -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"cddlib\" -DVERSION=\"0.94\" -DHAVE_LIBGMP=1 -DSTDC_HEADERS=1 -I. -I.  -UGMPRATIONAL   -I /export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib  -c `test -f 'cddlp.c' || echo './'`cddlp.c
source='cddmp.c' object='cddmp.o' libtool=no \
depfile='.deps/cddmp.Po' tmpdepfile='.deps/cddmp.TPo' \
depmode=none /bin/bash ../depcomp \
/opt/xxxsunstudio12.1/bin/cc -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"cddlib\" -DVERSION=\"0.94\" -DHAVE_LIBGMP=1 -DSTDC_HEADERS=1 -I. -I.  -UGMPRATIONAL   -I /export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib  -c `test -f 'cddmp.c' || echo './'`cddmp.c
source='cddio.c' object='cddio.o' libtool=no \
depfile='.deps/cddio.Po' tmpdepfile='.deps/cddio.TPo' \
depmode=none /bin/bash ../depcomp \
/opt/xxxsunstudio12.1/bin/cc -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"cddlib\" -DVERSION=\"0.94\" -DHAVE_LIBGMP=1 -DSTDC_HEADERS=1 -I. -I.  -UGMPRATIONAL   -I /export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib  -c `test -f 'cddio.c' || echo './'`cddio.c
source='cddlib.c' object='cddlib.o' libtool=no \
depfile='.deps/cddlib.Po' tmpdepfile='.deps/cddlib.TPo' \
depmode=none /bin/bash ../depcomp \
/opt/xxxsunstudio12.1/bin/cc -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"cddlib\" -DVERSION=\"0.94\" -DHAVE_LIBGMP=1 -DSTDC_HEADERS=1 -I. -I.  -UGMPRATIONAL   -I /export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib  -c `test -f 'cddlib.c' || echo './'`cddlib.c
source='cddproj.c' object='cddproj.o' libtool=no \
depfile='.deps/cddproj.Po' tmpdepfile='.deps/cddproj.TPo' \
depmode=none /bin/bash ../depcomp \
/opt/xxxsunstudio12.1/bin/cc -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"cddlib\" -DVERSION=\"0.94\" -DHAVE_LIBGMP=1 -DSTDC_HEADERS=1 -I. -I.  -UGMPRATIONAL   -I /export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib  -c `test -f 'cddproj.c' || echo './'`cddproj.c
source='setoper.c' object='setoper.o' libtool=no \
depfile='.deps/setoper.Po' tmpdepfile='.deps/setoper.TPo' \
depmode=none /bin/bash ../depcomp \
/opt/xxxsunstudio12.1/bin/cc -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"cddlib\" -DVERSION=\"0.94\" -DHAVE_LIBGMP=1 -DSTDC_HEADERS=1 -I. -I.  -UGMPRATIONAL   -I /export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib  -c `test -f 'setoper.c' || echo './'`setoper.c
rm -f libcdd.a
ar cru libcdd.a cddcore.o cddlp.o cddmp.o cddio.o cddlib.o cddproj.o setoper.o
ranlib libcdd.a
make[3]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/cddlib-094f/src/lib-src'
Making all in src
make[3]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/cddlib-094f/src/src'
source='simplecdd.c' object='simplecdd.o' libtool=no \
depfile='.deps/simplecdd.Po' tmpdepfile='.deps/simplecdd.TPo' \
depmode=none /bin/bash ../depcomp \
/opt/xxxsunstudio12.1/bin/cc -DPACKAGE_NAME=\"\" -DPACKAGE_TARNAME=\"\" -DPACKAGE_VERSION=\"\" -DPACKAGE_STRING=\"\" -DPACKAGE_BUGREPORT=\"\" -DPACKAGE=\"cddlib\" -DVERSION=\"0.94\" -DHAVE_LIBGMP=1 -DSTDC_HEADERS=1 -I. -I. -I../lib-src -UGMPRATIONAL   -I /export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib  -c `test -f 'simplecdd.c' || echo './'`simplecdd.c
/opt/xxxsunstudio12.1/bin/cc  -I /export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib    -o scdd  simplecdd.o ../lib-src/libcdd.a -lgmp
Undefined                       first referenced
 symbol                             in file
fabs                                ../lib-src/libcdd.a(cddio.o)
ld: fatal: Symbol referencing errors. No output written to scdd
make[3]: *** [scdd] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/cddlib-094f/src/src'
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/cddlib-094f/src'
Error building cddlib

real    0m13.117s
user    0m3.318s
sys     0m4.640s
sage: An error occurred while installing cddlib-094f
```



---

Comment by drkirkby created at 2009-11-09 14:06:54

Changing component from algebra to solaris.


---

Comment by drkirkby created at 2009-11-27 16:09:48

I'm not sure who yo report this to.


---

Comment by drkirkby created at 2009-12-31 01:02:47

Reported it today to

fukuda AT 
ifor.math.ethz.ch

It would be easy to fix. 

Dave


---

Comment by drkirkby created at 2009-12-31 03:54:43

Changing status from new to needs_review.


---

Comment by drkirkby created at 2009-12-31 03:54:43

I've reported it, but fixed it too. All I needed to add was:

AC_CHECK_LIB(m, fabs)

to configure.in

and then remake the .spkg The revised .spkg can be found here. 

http://boxen.math.washington.edu/home/kirkby/portability/cddlib-094f.p0/


---

Comment by ddrake created at 2010-01-05 07:31:45

On 64-bit Linux (Ubuntu) this works perfectly well, and I do see that it checks for fabs in libm. It passes all doctests. Is there a convenient way that I could test this on, say, t2.math?


---

Comment by drkirkby created at 2010-01-05 12:18:26

Hi Dan. Thank you for taking a look at this. 

Given Sage takes a long time to build on t2 (a couple of days), I suggest you use an install of mine on 't2'. I've made all files world writable under the directory /rootpool2/local/kirkby/ world writable. 

 * Log into 't2'
 * $ cd /rootpool2/local/kirkby/sage-4.3
 * $ export PATH=/usr/local/gcc-4.4.1-sun-linker/bin:/usr/local/bin2:/usr/bin:/usr/ccs/bin:/usr/local/bin:/usr/sfw/bin:/bin:/usr/sbin
 * $ export  CC=/opt/SUNWspro/bin/cc
 * $ export  CXX=/opt/SUNWspro/bin/CC

Then try /rootpool2/local/kirkby/sage-4.3/sage -f cddlib-094f.p0

Also try cddlib-094f if you wish, and you will find it fails. 

Both packages are in spkg/installed/standard 

Dave


---

Comment by drkirkby created at 2010-01-05 12:21:35

Ooops, I mean both packages are in the directory 


```
/rootpool2/local/kirkby/sage-4.3/spkg/standard
```



---

Comment by ddrake created at 2010-01-06 00:56:44

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-01-06 00:56:44

Your new spkg does build correctly on t2.math, and the old one does fail. Positive review.


---

Comment by rlm created at 2010-01-13 05:56:05

Resolution: fixed
