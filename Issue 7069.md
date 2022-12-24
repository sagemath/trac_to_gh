# Issue 7069: tachyon-0.98beta.p9 ignores CC and uses gcc, so can't build with Sun Studio.

archive/issues_007069.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @orlitzky @dimpase\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used #7021 \n\n\n```\ntachyon-0.98beta.p9/patches/\ntachyon-0.98beta.p9/patches/Make-arch.patch\ntachyon-0.98beta.p9/patches/Make-arch\ntachyon-0.98beta.p9/spkg-install\ntachyon-0.98beta.p9/.hgignore\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nmake[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'\nmake all \\\n\"ARCH = solaris-pthreads-gcc\" \\\n\"CC = gcc\" \\\n\"CFLAGS = -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS\" \\\n\"AR = ar\" \\\n\"ARFLAGS = r\" \\\n\"STRIP = strip\" \\\n\"LIBS = -L. -ltachyon  -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib -lpng12 -lz  -lm -lpthread\"\nmake[3]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'\nBuilding Tachyon Parallel Ray Tracing library\nCopyright 1994-2007, John E. Stone\nAll Rights Reserveed\nMaking architecture directory ../compile/solaris-pthreads-gcc\nMaking library directory ../compile/solaris-pthreads-gcc/libtachyon\nmake ../compile ../compile/solaris-pthreads-gcc ../compile/solaris-pthreads-gcc/libtachyon  ../compile/solaris-pthreads-gcc/libtachyon.a  ../compile/solaris-pthreads-gcc/tachyon\nmake[4]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'\nmake[4]: Nothing to be done for `../compile'.\nmake[4]: Nothing to be done for `../compile/solaris-pthreads-gcc'.\nmake[4]: Nothing to be done for `../compile/solaris-pthreads-gcc/libtachyon'.\ngcc -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS -c ../src/api.c -o ../compile/solaris-pthreads-gcc/libtachyon/api.o\ngcc -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS -c ../src/apigeom.c -o ../compile/solaris-pthreads-gcc/libtachyon/apigeom.o\ngcc -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS -c ../src/box.c -o ../compile/solaris-pthreads-gcc/libtachyon/box.o\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7069\n\n",
    "created_at": "2009-09-29T13:06:53Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "tachyon-0.98beta.p9 ignores CC and uses gcc, so can't build with Sun Studio.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7069",
    "user": "drkirkby"
}
```
Assignee: tbd

CC:  @orlitzky @dimpase

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used #7021 


```
tachyon-0.98beta.p9/patches/
tachyon-0.98beta.p9/patches/Make-arch.patch
tachyon-0.98beta.p9/patches/Make-arch
tachyon-0.98beta.p9/spkg-install
tachyon-0.98beta.p9/.hgignore
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
make[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'
make all \
"ARCH = solaris-pthreads-gcc" \
"CC = gcc" \
"CFLAGS = -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS" \
"AR = ar" \
"ARFLAGS = r" \
"STRIP = strip" \
"LIBS = -L. -ltachyon  -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib -lpng12 -lz  -lm -lpthread"
make[3]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'
Building Tachyon Parallel Ray Tracing library
Copyright 1994-2007, John E. Stone
All Rights Reserveed
Making architecture directory ../compile/solaris-pthreads-gcc
Making library directory ../compile/solaris-pthreads-gcc/libtachyon
make ../compile ../compile/solaris-pthreads-gcc ../compile/solaris-pthreads-gcc/libtachyon  ../compile/solaris-pthreads-gcc/libtachyon.a  ../compile/solaris-pthreads-gcc/tachyon
make[4]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'
make[4]: Nothing to be done for `../compile'.
make[4]: Nothing to be done for `../compile/solaris-pthreads-gcc'.
make[4]: Nothing to be done for `../compile/solaris-pthreads-gcc/libtachyon'.
gcc -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS -c ../src/api.c -o ../compile/solaris-pthreads-gcc/libtachyon/api.o
gcc -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS -c ../src/apigeom.c -o ../compile/solaris-pthreads-gcc/libtachyon/apigeom.o
gcc -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS -c ../src/box.c -o ../compile/solaris-pthreads-gcc/libtachyon/box.o
```


Issue created by migration from https://trac.sagemath.org/ticket/7069





---

archive/issue_comments_058474.json:
```json
{
    "body": "Changing component from algebra to solaris.",
    "created_at": "2009-11-09T14:05:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7069#issuecomment-58474",
    "user": "drkirkby"
}
```

Changing component from algebra to solaris.



---

archive/issue_comments_058475.json:
```json
{
    "body": "I think all `$CC` issues were fixed by #9379 and #10681. Can you test on Solaris?",
    "created_at": "2012-02-25T22:43:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7069#issuecomment-58475",
    "user": "@orlitzky"
}
```

I think all `$CC` issues were fixed by #9379 and #10681. Can you test on Solaris?



---

archive/issue_comments_058476.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7069#issuecomment-58476",
    "user": "@mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058477.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-07-08T16:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7069#issuecomment-58477",
    "user": "@mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_058478.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-07-14T16:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7069",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7069#issuecomment-58478",
    "user": "@fchapoton"
}
```

Resolution: invalid
