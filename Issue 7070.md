# Issue 7070: tachyon 0.98beta.p9 ignores CC and uses gcc. Also uses -O6 which might be dangerous.

archive/issues_007070.json:
```json
{
    "body": "Assignee: tbd\n\nUsing\n\n* Solaris 10 update 7 on SPARC\n* sage-4.1.2.alpha2\n* Sun Studio 12.1\n* An updated configure script to allow the Sun compiler to be used #7021 \n\n```\ntachyon-0.98beta.p9/spkg-install\ntachyon-0.98beta.p9/.hgignore\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000\n****************************************************\n****************************************************\nCC Version\n/opt/xxxsunstudio12.1/bin/cc -v\nusage: cc [ options] files.  Use 'cc -flags' for details\n****************************************************\nmake[2]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'\nmake all \\\n\"ARCH = solaris-pthreads-gcc\" \\\n\"CC = gcc\" \\\n\"CFLAGS = -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS\" \\\n\"AR = ar\" \\\n\"ARFLAGS = r\" \\\n\"STRIP = strip\" \\\n\"LIBS = -L. -ltachyon  -L/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/lib -lpng12 -lz  -lm -lpthread\"\nmake[3]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'\nBuilding Tachyon Parallel Ray Tracing library\nCopyright 1994-2007, John E. Stone\nAll Rights Reserveed\nMaking architecture directory ../compile/solaris-pthreads-gcc\nMaking library directory ../compile/solaris-pthreads-gcc/libtachyon\nmake ../compile ../compile/solaris-pthreads-gcc ../compile/solaris-pthreads-gcc/libtachyon  ../compile/solaris-pthreads-gcc/libtachyon.a  ../compile/solaris-pthreads-gcc/tachyon\nmake[4]: Entering directory `/export/home/drkirkby/sage/sage-4.1.2.alpha4/spkg/build/tachyon-0.98beta.p9/src/unix'\nmake[4]: Nothing to be done for `../compile'.\nmake[4]: Nothing to be done for `../compile/solaris-pthreads-gcc'.\nmake[4]: Nothing to be done for `../compile/solaris-pthreads-gcc/libtachyon'.\ngcc -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS -c ../src/api.c -o ../compile/solaris-pthreads-gcc/libtachyon/api.o\ngcc -Wall -O6 -fomit-frame-pointer -ffast-math -D_REENTRANT -DSunOS  -DUSEPNG    -I/export/home/drkirkby/sage/sage-4.1.2.alpha4/local/include  -DTHR -DUSEPOSIXTHREADS -c ../src/apigeom.c -o ../compile/solaris-pthreads-gcc/libtachyon/apigeom.o\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7070\n\n",
    "created_at": "2009-09-29T13:14:33Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "tachyon 0.98beta.p9 ignores CC and uses gcc. Also uses -O6 which might be dangerous.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7070",
    "user": "drkirkby"
}
```
Assignee: tbd

Using

* Solaris 10 update 7 on SPARC
* sage-4.1.2.alpha2
* Sun Studio 12.1
* An updated configure script to allow the Sun compiler to be used #7021 

```
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
```


Issue created by migration from https://trac.sagemath.org/ticket/7070





---

archive/issue_comments_058479.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-09-29T13:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7070#issuecomment-58479",
    "user": "mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_058480.json:
```json
{
    "body": "Closing this ticket as a duplicate of #7069.",
    "created_at": "2009-09-29T13:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7070#issuecomment-58480",
    "user": "mvngu"
}
```

Closing this ticket as a duplicate of #7069.
