# Issue 8767: libpng -- sage-4.4 fails to build on itanium with GCC-4.5.0

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-26 17:40:50

Assignee: GeorgSWeber

When building Sage using GCC 4.5.0 on iras, a SUSE 10 Itanium, libpng fails to build due to:

```
libpng.vers:2: syntax error in VERSION script
```


More context:


```
...
bin/sh ./libtool --tag=CC   --mode=link gcc  -fPIC -g -I/home/wstein/screen/iras/sage-4.4/local/include -no-undefined -export-dynamic -version-number 0:35:0 -Wl,--version-script=libpng.vers   -o libpng12.la -rpath
iras/sage-4.4/local/lib libpng12_la-png.lo libpng12_la-pngset.lo libpng12_la-pngget.lo libpng12_la-pngrutil.lo libpng12_la-pngtrans.lo libpng12_la-pngwutil.lo libpng12_la-pngread.lo libpng12_la-pngrio.lo libpng12_l
la-pngwrite.lo libpng12_la-pngrtran.lo libpng12_la-pngwtran.lo libpng12_la-pngmem.lo libpng12_la-pngerror.lo libpng12_la-pngpread.lo  -lz -lm
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -DPNG_CONFIGURE_LIBPNG -fPIC -g -I/home/wstein/screen/iras/sage-4.4/local/include -MT libpng_la-pngwtran.lo -MD -MP -MF .deps/libpng_la-pngwtran.Tpo -c pngwtran.c -o libpn
/null 2>&1
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -DPNG_CONFIGURE_LIBPNG -fPIC -g -I/home/wstein/screen/iras/sage-4.4/local/include -MT libpng_la-pngmem.lo -MD -MP -MF .deps/libpng_la-pngmem.Tpo -c pngmem.c -o libpng_la-p
&1
libtool: link: gcc -shared  .libs/libpng12_la-png.o .libs/libpng12_la-pngset.o .libs/libpng12_la-pngget.o .libs/libpng12_la-pngrutil.o .libs/libpng12_la-pngtrans.o .libs/libpng12_la-pngwutil.o .libs/libpng12_la-png
_la-pngrio.o .libs/libpng12_la-pngwio.o .libs/libpng12_la-pngwrite.o .libs/libpng12_la-pngrtran.o .libs/libpng12_la-pngwtran.o .libs/libpng12_la-pngmem.o .libs/libpng12_la-pngerror.o .libs/libpng12_la-pngpread.o
n-script=libpng.vers   -Wl,-soname -Wl,libpng12.so.0 -o .libs/libpng12.so.0.35.0
/usr/local/binutils-2.20.1/ia64-Linux-suse-gcc-4.4.3/bin/ld:libpng.vers:2: syntax error in VERSION script
collect2: ld returned 1 exit status
make[3]: *** [libpng12.la] Error 1
```


More machine info:

```
gcc version 4.5.0 (GCC)
wstein`@`iras:~/screen/iras> uname -a
Linux iras 2.6.16.46-0.12-default #1 SMP Thu May 17 14:00:09 UTC 2007 ia64 ia64 ia64 GNU/Linux
wstein`@`iras:~/screen/iras> cat /etc/issue

Welcome to SUSE Linux Enterprise Server 10 SP1 (ia64) - Kernel \r (\l).
```


The crappy libpng SPKG.txt endslike this:

```
### libpng-1.2.35.p0 (Jaap Spies, Feb 1th, 2010)
 *

### libpng-1.2.35 (Michael Abshoff, April 10th, 2009)
 * update to latest upstream due to security issue in libpng (#5696)

```


The hg log ends

```
changeset:   13:ae01944f408c
tag:         tip
user:        Jaap Spies <jaapspies`@`gmail.com>
date:        Thu Feb 04 19:32:51 2010 +0100
summary:     Corrected stupid typo I thought I had corrected earlier.

```


Thus this is likely a compiler/toolchain issue, since it looks like libpng used to work fine with GCC-4.4x.  


---

Comment by was created at 2010-04-26 17:44:39

Same problem on x86_64 linux:

```
wstein`@`menas:~/screen/menas> uname -a
Linux menas 2.6.27.39-0.2-default #1 SMP 2009-11-23 12:57:38 +0100 x86_64 x86_64 x86_64 GNU/Linux
wstein`@`menas:~/screen/menas> cat /etc/issue
Welcome to openSUSE 11.1 - Kernel \r (\l).
```



---

Comment by wjp created at 2010-04-26 22:43:55


```
spkg-install} was passing include paths in CFLAGS instead of in CPPFLAGS, which caused some preprocessor magic to fail that libpng was doing to create a symbol version script.

New spkg at:

http://www.math.leidenuniv.nl/~wpalenst/sage/libpng-1.2.35.p1.spkg

(The .p0 spkg also contained a duplicate copy of itself, which I removed.)


---

Comment by wjp created at 2010-04-26 22:43:55

Changing status from new to needs_review.


---

Comment by was created at 2010-04-26 23:00:29

Positive review!


---

Comment by was created at 2010-04-26 23:00:29

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-28 19:19:53

Resolution: fixed
