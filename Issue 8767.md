# Issue 8767: libpng -- sage-4.4 fails to build on itanium with GCC-4.5.0

archive/issues_008767.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nWhen building Sage using GCC 4.5.0 on iras, a SUSE 10 Itanium, libpng fails to build due to:\n\n```\nlibpng.vers:2: syntax error in VERSION script\n```\n\n\nMore context:\n\n\n```\n...\nbin/sh ./libtool --tag=CC   --mode=link gcc  -fPIC -g -I/home/wstein/screen/iras/sage-4.4/local/include -no-undefined -export-dynamic -version-number 0:35:0 -Wl,--version-script=libpng.vers   -o libpng12.la -rpath\niras/sage-4.4/local/lib libpng12_la-png.lo libpng12_la-pngset.lo libpng12_la-pngget.lo libpng12_la-pngrutil.lo libpng12_la-pngtrans.lo libpng12_la-pngwutil.lo libpng12_la-pngread.lo libpng12_la-pngrio.lo libpng12_l\nla-pngwrite.lo libpng12_la-pngrtran.lo libpng12_la-pngwtran.lo libpng12_la-pngmem.lo libpng12_la-pngerror.lo libpng12_la-pngpread.lo  -lz -lm\nlibtool: compile:  gcc -DHAVE_CONFIG_H -I. -DPNG_CONFIGURE_LIBPNG -fPIC -g -I/home/wstein/screen/iras/sage-4.4/local/include -MT libpng_la-pngwtran.lo -MD -MP -MF .deps/libpng_la-pngwtran.Tpo -c pngwtran.c -o libpn\n/null 2>&1\nlibtool: compile:  gcc -DHAVE_CONFIG_H -I. -DPNG_CONFIGURE_LIBPNG -fPIC -g -I/home/wstein/screen/iras/sage-4.4/local/include -MT libpng_la-pngmem.lo -MD -MP -MF .deps/libpng_la-pngmem.Tpo -c pngmem.c -o libpng_la-p\n&1\nlibtool: link: gcc -shared  .libs/libpng12_la-png.o .libs/libpng12_la-pngset.o .libs/libpng12_la-pngget.o .libs/libpng12_la-pngrutil.o .libs/libpng12_la-pngtrans.o .libs/libpng12_la-pngwutil.o .libs/libpng12_la-png\n_la-pngrio.o .libs/libpng12_la-pngwio.o .libs/libpng12_la-pngwrite.o .libs/libpng12_la-pngrtran.o .libs/libpng12_la-pngwtran.o .libs/libpng12_la-pngmem.o .libs/libpng12_la-pngerror.o .libs/libpng12_la-pngpread.o\nn-script=libpng.vers   -Wl,-soname -Wl,libpng12.so.0 -o .libs/libpng12.so.0.35.0\n/usr/local/binutils-2.20.1/ia64-Linux-suse-gcc-4.4.3/bin/ld:libpng.vers:2: syntax error in VERSION script\ncollect2: ld returned 1 exit status\nmake[3]: *** [libpng12.la] Error 1\n```\n\n\nMore machine info:\n\n```\ngcc version 4.5.0 (GCC)\nwstein@iras:~/screen/iras> uname -a\nLinux iras 2.6.16.46-0.12-default #1 SMP Thu May 17 14:00:09 UTC 2007 ia64 ia64 ia64 GNU/Linux\nwstein@iras:~/screen/iras> cat /etc/issue\n\nWelcome to SUSE Linux Enterprise Server 10 SP1 (ia64) - Kernel \\r (\\l).\n```\n\n\nThe crappy libpng SPKG.txt endslike this:\n\n```\n### libpng-1.2.35.p0 (Jaap Spies, Feb 1th, 2010)\n *\n\n### libpng-1.2.35 (Michael Abshoff, April 10th, 2009)\n * update to latest upstream due to security issue in libpng (#5696)\n\n```\n\n\nThe hg log ends\n\n```\nchangeset:   13:ae01944f408c\ntag:         tip\nuser:        Jaap Spies <jaapspies@gmail.com>\ndate:        Thu Feb 04 19:32:51 2010 +0100\nsummary:     Corrected stupid typo I thought I had corrected earlier.\n\n```\n\n\nThus this is likely a compiler/toolchain issue, since it looks like libpng used to work fine with GCC-4.4x.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/8767\n\n",
    "created_at": "2010-04-26T17:40:50Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "libpng -- sage-4.4 fails to build on itanium with GCC-4.5.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8767",
    "user": "https://github.com/williamstein"
}
```
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
wstein@iras:~/screen/iras> uname -a
Linux iras 2.6.16.46-0.12-default #1 SMP Thu May 17 14:00:09 UTC 2007 ia64 ia64 ia64 GNU/Linux
wstein@iras:~/screen/iras> cat /etc/issue

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
user:        Jaap Spies <jaapspies@gmail.com>
date:        Thu Feb 04 19:32:51 2010 +0100
summary:     Corrected stupid typo I thought I had corrected earlier.

```


Thus this is likely a compiler/toolchain issue, since it looks like libpng used to work fine with GCC-4.4x.  

Issue created by migration from https://trac.sagemath.org/ticket/8767





---

archive/issue_comments_080100.json:
```json
{
    "body": "Same problem on x86_64 linux:\n\n```\nwstein@menas:~/screen/menas> uname -a\nLinux menas 2.6.27.39-0.2-default #1 SMP 2009-11-23 12:57:38 +0100 x86_64 x86_64 x86_64 GNU/Linux\nwstein@menas:~/screen/menas> cat /etc/issue\nWelcome to openSUSE 11.1 - Kernel \\r (\\l).\n```\n",
    "created_at": "2010-04-26T17:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8767#issuecomment-80100",
    "user": "https://github.com/williamstein"
}
```

Same problem on x86_64 linux:

```
wstein@menas:~/screen/menas> uname -a
Linux menas 2.6.27.39-0.2-default #1 SMP 2009-11-23 12:57:38 +0100 x86_64 x86_64 x86_64 GNU/Linux
wstein@menas:~/screen/menas> cat /etc/issue
Welcome to openSUSE 11.1 - Kernel \r (\l).
```




---

archive/issue_comments_080101.json:
```json
{
    "body": "\n```\nspkg-install} was passing include paths in CFLAGS instead of in CPPFLAGS, which caused some preprocessor magic to fail that libpng was doing to create a symbol version script.\n\nNew spkg at:\n\nhttp://www.math.leidenuniv.nl/~wpalenst/sage/libpng-1.2.35.p1.spkg\n\n(The .p0 spkg also contained a duplicate copy of itself, which I removed.)",
    "created_at": "2010-04-26T22:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8767#issuecomment-80101",
    "user": "https://github.com/wjp"
}
```


```
spkg-install} was passing include paths in CFLAGS instead of in CPPFLAGS, which caused some preprocessor magic to fail that libpng was doing to create a symbol version script.

New spkg at:

http://www.math.leidenuniv.nl/~wpalenst/sage/libpng-1.2.35.p1.spkg

(The .p0 spkg also contained a duplicate copy of itself, which I removed.)



---

archive/issue_comments_080102.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-26T22:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8767#issuecomment-80102",
    "user": "https://github.com/wjp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080103.json:
```json
{
    "body": "Positive review!",
    "created_at": "2010-04-26T23:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8767#issuecomment-80103",
    "user": "https://github.com/williamstein"
}
```

Positive review!



---

archive/issue_comments_080104.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-26T23:00:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8767#issuecomment-80104",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_008935.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2010-04-28T19:19:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8767",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8767#event-8935"
}
```



---

archive/issue_comments_080105.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-28T19:19:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8767",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8767#issuecomment-80105",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
