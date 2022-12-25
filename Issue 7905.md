# Issue 7905: Sun Studio 12 64-bit mode on Solaris.  libgpg-error creates 32-bit binaries.

archive/issues_007905.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @jaapspies @dimpase\n\n## Build environment\n* Sun Blade 2000. 2 x UltraSPARC III+ CPUs at 1.2 GHz. 8 GB RAM\n* Solaris 10 update 7 (05/2009)\n* Sage 4.3 with numerous modifications, including updated sage-env to hopefully handle 64-bit builds properly. \n* Sun Studio 12.1 \n* 64-bit build. SAGE64 was set to yes. \n\n```\nCC=/opt/sunstudio12.1/bin/cc\nCXX=/opt/sunstudio12.1/bin/CC\nSAGE64=yes\nSAGE_FORTRAN_LIB=/usr/local/gcc-4.4.1-sun-linker/lib/libgfortran.so\nSAGE_FORTRAN=/opt/sunstudio12.1/bin/f95\n```\n\nI'm not sure why I set SAGE_FORTRAN_LIB there, but I doubt it was doing anything. The build breaks with:\n\n```\n /opt/sunstudio12.1/bin/cc -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sun-64/sage-4.3/local/include -I/export/home/drkirkby/sun-64/sage-4.3/local/include -g -O2 -m64 -g -c ath.c  -KPIC -DPIC -o .libs/libgcrypt_la-ath.o\n /opt/sunstudio12.1/bin/cc -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sun-64/sage-4.3/local/include -I/export/home/drkirkby/sun-64/sage-4.3/local/include -g -O2 -m64 -g -c ath.c -o libgcrypt_la-ath.o >/dev/null 2>&1\n/bin/bash ../libtool --tag=CC   --mode=link /opt/sunstudio12.1/bin/cc -I/export/home/drkirkby/sun-64/sage-4.3/local/include -g  -O2  -m64  -g      -version-info 16:2:5 -m64  -o libgcrypt.la -rpath /export/home/drkirkby/sun-64/sage-4.3/local/lib libgcrypt_la-visibility.lo libgcrypt_la-misc.lo libgcrypt_la-global.lo libgcrypt_la-sexp.lo libgcrypt_la-hwfeatures.lo libgcrypt_la-stdmem.lo libgcrypt_la-secmem.lo libgcrypt_la-missing-string.lo libgcrypt_la-module.lo libgcrypt_la-fips.lo libgcrypt_la-hmac256.lo libgcrypt_la-ath.lo ../cipher/libcipher.la ../random/librandom.la ../mpi/libmpi.la -L/export/home/drkirkby/sun-64/sage-4.3/local/lib -lgpg-error -lsocket -lsocket \nld -G -h libgcrypt.so.11 -o .libs/libgcrypt.so.11.5.2  .libs/libgcrypt_la-visibility.o .libs/libgcrypt_la-misc.o .libs/libgcrypt_la-global.o .libs/libgcrypt_la-sexp.o .libs/libgcrypt_la-hwfeatures.o .libs/libgcrypt_la-stdmem.o .libs/libgcrypt_la-secmem.o .libs/libgcrypt_la-missing-string.o .libs/libgcrypt_la-module.o .libs/libgcrypt_la-fips.o .libs/libgcrypt_la-hmac256.o .libs/libgcrypt_la-ath.o -z allextract ../cipher/.libs/libcipher.a ../random/.libs/librandom.a ../mpi/.libs/libmpi.a -z defaultextract  -R/export/home/drkirkby/sun-64/sage-4.3/local/lib -R/export/home/drkirkby/sun-64/sage-4.3/local/lib -L/export/home/drkirkby/sun-64/sage-4.3/local/lib /export/home/drkirkby/sun-64/sage-4.3/local/lib/libgpg-error.so -lsocket -lc \nld: fatal: file /export/home/drkirkby/sun-64/sage-4.3/local/lib/libgpg-error.so: wrong ELF class: ELFCLASS32\nld: fatal: File processing errors. No output written to .libs/libgcrypt.so.11.5.2\nmake[4]: *** [libgcrypt.la] Error 1\nmake[4]: Leaving directory `/export/home/drkirkby/sun-64/sage-4.3/spkg/build/libgcrypt-1.4.4.p1/src/src'\nmake[3]: *** [all-recursive] Error 1\nmake[3]: Leaving directory `/export/home/drkirkby/sun-64/sage-4.3/spkg/build/libgcrypt-1.4.4.p1/src'\nmake[2]: *** [all] Error 2\nmake[2]: Leaving directory `/export/home/drkirkby/sun-64/sage-4.3/spkg/build/libgcrypt-1.4.4.p1/src'\nfailed to build libgcrypt\n\nreal    8m30.831s\nuser    2m9.479s\nsys     1m35.707s\nsage: An error occurred while installing libgcrypt-1.4.4.p1\n```\n\nHence I need to resolve why 32-bit binaries are being built, when they should be 64-bit. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7905\n\n",
    "created_at": "2010-01-12T08:26:27Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sun Studio 12 64-bit mode on Solaris.  libgpg-error creates 32-bit binaries.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7905",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  @jaapspies @dimpase

## Build environment
* Sun Blade 2000. 2 x UltraSPARC III+ CPUs at 1.2 GHz. 8 GB RAM
* Solaris 10 update 7 (05/2009)
* Sage 4.3 with numerous modifications, including updated sage-env to hopefully handle 64-bit builds properly. 
* Sun Studio 12.1 
* 64-bit build. SAGE64 was set to yes. 

```
CC=/opt/sunstudio12.1/bin/cc
CXX=/opt/sunstudio12.1/bin/CC
SAGE64=yes
SAGE_FORTRAN_LIB=/usr/local/gcc-4.4.1-sun-linker/lib/libgfortran.so
SAGE_FORTRAN=/opt/sunstudio12.1/bin/f95
```

I'm not sure why I set SAGE_FORTRAN_LIB there, but I doubt it was doing anything. The build breaks with:

```
 /opt/sunstudio12.1/bin/cc -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sun-64/sage-4.3/local/include -I/export/home/drkirkby/sun-64/sage-4.3/local/include -g -O2 -m64 -g -c ath.c  -KPIC -DPIC -o .libs/libgcrypt_la-ath.o
 /opt/sunstudio12.1/bin/cc -DHAVE_CONFIG_H -I. -I.. -I/export/home/drkirkby/sun-64/sage-4.3/local/include -I/export/home/drkirkby/sun-64/sage-4.3/local/include -g -O2 -m64 -g -c ath.c -o libgcrypt_la-ath.o >/dev/null 2>&1
/bin/bash ../libtool --tag=CC   --mode=link /opt/sunstudio12.1/bin/cc -I/export/home/drkirkby/sun-64/sage-4.3/local/include -g  -O2  -m64  -g      -version-info 16:2:5 -m64  -o libgcrypt.la -rpath /export/home/drkirkby/sun-64/sage-4.3/local/lib libgcrypt_la-visibility.lo libgcrypt_la-misc.lo libgcrypt_la-global.lo libgcrypt_la-sexp.lo libgcrypt_la-hwfeatures.lo libgcrypt_la-stdmem.lo libgcrypt_la-secmem.lo libgcrypt_la-missing-string.lo libgcrypt_la-module.lo libgcrypt_la-fips.lo libgcrypt_la-hmac256.lo libgcrypt_la-ath.lo ../cipher/libcipher.la ../random/librandom.la ../mpi/libmpi.la -L/export/home/drkirkby/sun-64/sage-4.3/local/lib -lgpg-error -lsocket -lsocket 
ld -G -h libgcrypt.so.11 -o .libs/libgcrypt.so.11.5.2  .libs/libgcrypt_la-visibility.o .libs/libgcrypt_la-misc.o .libs/libgcrypt_la-global.o .libs/libgcrypt_la-sexp.o .libs/libgcrypt_la-hwfeatures.o .libs/libgcrypt_la-stdmem.o .libs/libgcrypt_la-secmem.o .libs/libgcrypt_la-missing-string.o .libs/libgcrypt_la-module.o .libs/libgcrypt_la-fips.o .libs/libgcrypt_la-hmac256.o .libs/libgcrypt_la-ath.o -z allextract ../cipher/.libs/libcipher.a ../random/.libs/librandom.a ../mpi/.libs/libmpi.a -z defaultextract  -R/export/home/drkirkby/sun-64/sage-4.3/local/lib -R/export/home/drkirkby/sun-64/sage-4.3/local/lib -L/export/home/drkirkby/sun-64/sage-4.3/local/lib /export/home/drkirkby/sun-64/sage-4.3/local/lib/libgpg-error.so -lsocket -lc 
ld: fatal: file /export/home/drkirkby/sun-64/sage-4.3/local/lib/libgpg-error.so: wrong ELF class: ELFCLASS32
ld: fatal: File processing errors. No output written to .libs/libgcrypt.so.11.5.2
make[4]: *** [libgcrypt.la] Error 1
make[4]: Leaving directory `/export/home/drkirkby/sun-64/sage-4.3/spkg/build/libgcrypt-1.4.4.p1/src/src'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sun-64/sage-4.3/spkg/build/libgcrypt-1.4.4.p1/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sun-64/sage-4.3/spkg/build/libgcrypt-1.4.4.p1/src'
failed to build libgcrypt

real    8m30.831s
user    2m9.479s
sys     1m35.707s
sage: An error occurred while installing libgcrypt-1.4.4.p1
```

Hence I need to resolve why 32-bit binaries are being built, when they should be 64-bit. 


Issue created by migration from https://trac.sagemath.org/ticket/7905





---

archive/issue_events_018901.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7905#event-18901"
}
```



---

archive/issue_events_018902.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7905#event-18902"
}
```



---

archive/issue_events_018903.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7905#event-18903"
}
```



---

archive/issue_events_018904.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7905#event-18904"
}
```



---

archive/issue_events_018905.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7905#event-18905"
}
```



---

archive/issue_events_018906.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7905#event-18906"
}
```



---

archive/issue_events_018907.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7905#event-18907"
}
```



---

archive/issue_comments_068615.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7905#issuecomment-68615",
    "user": "https://github.com/mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_events_018908.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-07-08T16:51:35Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7905#event-18908"
}
```



---

archive/issue_events_018909.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-07-08T16:51:35Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7905#event-18909"
}
```



---

archive/issue_comments_068616.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7905#issuecomment-68616",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_068617.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-07-12T20:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7905#issuecomment-68617",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_068618.json:
```json
{
    "body": "The goal of these tickets is laudable, but:\n\n* We need at least one user who is able to test.\n* The package/OS information on this ticket is outdated beyond usefulness.\n* Upstream is a better place to report portability issues these days.",
    "created_at": "2020-07-12T20:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7905#issuecomment-68618",
    "user": "https://github.com/orlitzky"
}
```

The goal of these tickets is laudable, but:

* We need at least one user who is able to test.
* The package/OS information on this ticket is outdated beyond usefulness.
* Upstream is a better place to report portability issues these days.



---

archive/issue_comments_068619.json:
```json
{
    "body": "Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7905#issuecomment-68619",
    "user": "https://github.com/fchapoton"
}
```

Closing very old sun/solaris tickets. Any tentative for this OS should start afresh.



---

archive/issue_events_018910.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-07-15T07:18:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7905#event-18910"
}
```



---

archive/issue_comments_068620.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-15T07:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7905",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7905#issuecomment-68620",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
