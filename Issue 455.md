# Issue 455: scipy picks /usr/local/lib/libfftw3.a instead of $SAGE_LIB/libfftw3.a

archive/issues_000455.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jasongrout mvngu\n\nReported by JMD:\n\nsystem : AMD64 X2 4200\n             Slamd64  (Slackware 11.0 for x86-64)\n             gcc 3.4.6\n\nHere it seems that /usr/local/lib/libfftw3.a on my system is used,\nmaybe instead of something inside sage-2.8/\n\nlog :   gcc: build/src.linux-x86_64-2.5/Lib/fftpack/_fftpackmodule.c\nsage_fortran -shared -shared build/temp.linux-x86_64-2.5/build/\nsrc.linux-x86_64-2.5/Lib/fftpack/_fftpackmodule.o build/temp.linux-\nx86_64-2.5/Lib/fftpack/src/zfft.o build/temp.linux-x86_64-2.5/Lib/\nfftpack/src/drfft.o build/temp.linux-x86_64-2.5/Lib/fftpack/src/\nzrfft.o build/temp.linux-x86_64-2.5/Lib/fftpack/src/zfftnd.o build/\ntemp.linux-x86_64-2.5/build/src.linux-x86_64-2.5/fortranobject.o -L/\nusr/local/lib -Lbuild/temp.linux-x86_64-2.5 -ldfftpack -lfftw3 -o\nbuild/lib.linux-x86_64-2.5/scipy/fftpack/_fftpack.so\nld: /usr/local/lib/libfftw3.a(mapflags.o): relocation R_X86_64_32\nagainst `a local symbol' can not be used when making a shared object;\nrecompile with -fPIC\n/usr/local/lib/libfftw3.a: ne peut lire les symboles: Mauvaise valeur\nld: /usr/local/lib/libfftw3.a(mapflags.o): relocation R_X86_64_32\nagainst `a local symbol' can not be used when making a shared object;\nrecompile with -fPIC\n/usr/local/lib/libfftw3.a: ne peut lire les symboles: Mauvaise valeur\nerror: Command \"sage_fortran -shared -shared build/temp.linux-\nx86_64-2.5/build/src.linux-x86_64-2.5/Lib/fftpack/_fftpackmodule.o\nbuild/temp.linux-x86_64-2.5/Lib/fftpack/src/zfft.o build/temp.linux-\nx86_64-2.5/Lib/fftpack/src/drfft.o build/temp.linux-x86_64-2.5/Lib/\nfftpack/src/zrfft.o build/temp.linux-x86_64-2.5/Lib/fftpack/src/\nzfftnd.o build/temp.linux-x86_64-2.5/build/src.linux-x86_64-2.5/\nfortranobject.o -L/usr/local/lib -Lbuild/temp.linux-x86_64-2.5 -\nldfftpack -lfftw3 -o build/lib.linux-x86_64-2.5/scipy/fftpack/\n_fftpack.so\" failed with exit status 1\nError building scipy. \n\nThe problem goes away when /usr/local/lib/libfftw3.a is moved.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/455\n\n",
    "created_at": "2007-08-19T08:56:19Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "scipy picks /usr/local/lib/libfftw3.a instead of $SAGE_LIB/libfftw3.a",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/455",
    "user": "mabshoff"
}
```
Assignee: @williamstein

CC:  @jasongrout mvngu

Reported by JMD:

system : AMD64 X2 4200
             Slamd64  (Slackware 11.0 for x86-64)
             gcc 3.4.6

Here it seems that /usr/local/lib/libfftw3.a on my system is used,
maybe instead of something inside sage-2.8/

log :   gcc: build/src.linux-x86_64-2.5/Lib/fftpack/_fftpackmodule.c
sage_fortran -shared -shared build/temp.linux-x86_64-2.5/build/
src.linux-x86_64-2.5/Lib/fftpack/_fftpackmodule.o build/temp.linux-
x86_64-2.5/Lib/fftpack/src/zfft.o build/temp.linux-x86_64-2.5/Lib/
fftpack/src/drfft.o build/temp.linux-x86_64-2.5/Lib/fftpack/src/
zrfft.o build/temp.linux-x86_64-2.5/Lib/fftpack/src/zfftnd.o build/
temp.linux-x86_64-2.5/build/src.linux-x86_64-2.5/fortranobject.o -L/
usr/local/lib -Lbuild/temp.linux-x86_64-2.5 -ldfftpack -lfftw3 -o
build/lib.linux-x86_64-2.5/scipy/fftpack/_fftpack.so
ld: /usr/local/lib/libfftw3.a(mapflags.o): relocation R_X86_64_32
against `a local symbol' can not be used when making a shared object;
recompile with -fPIC
/usr/local/lib/libfftw3.a: ne peut lire les symboles: Mauvaise valeur
ld: /usr/local/lib/libfftw3.a(mapflags.o): relocation R_X86_64_32
against `a local symbol' can not be used when making a shared object;
recompile with -fPIC
/usr/local/lib/libfftw3.a: ne peut lire les symboles: Mauvaise valeur
error: Command "sage_fortran -shared -shared build/temp.linux-
x86_64-2.5/build/src.linux-x86_64-2.5/Lib/fftpack/_fftpackmodule.o
build/temp.linux-x86_64-2.5/Lib/fftpack/src/zfft.o build/temp.linux-
x86_64-2.5/Lib/fftpack/src/drfft.o build/temp.linux-x86_64-2.5/Lib/
fftpack/src/zrfft.o build/temp.linux-x86_64-2.5/Lib/fftpack/src/
zfftnd.o build/temp.linux-x86_64-2.5/build/src.linux-x86_64-2.5/
fortranobject.o -L/usr/local/lib -Lbuild/temp.linux-x86_64-2.5 -
ldfftpack -lfftw3 -o build/lib.linux-x86_64-2.5/scipy/fftpack/
_fftpack.so" failed with exit status 1
Error building scipy. 

The problem goes away when /usr/local/lib/libfftw3.a is moved.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/455





---

archive/issue_comments_002274.json:
```json
{
    "body": "This problem can be fixed by patching the default locations the build system looks for libraries. We should disallow /usr and /usr/local and on OSX the various places for Fink and MacPorts since more than likely some random crap will be pulled in that way.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-12T08:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/455#issuecomment-2274",
    "user": "mabshoff"
}
```

This problem can be fixed by patching the default locations the build system looks for libraries. We should disallow /usr and /usr/local and on OSX the various places for Fink and MacPorts since more than likely some random crap will be pulled in that way.

Cheers,

Michael



---

archive/issue_comments_002275.json:
```json
{
    "body": "IIRC, fftw is stripped out of the scipy 0.7 release, so this problem may go away, right?\n\nOn the other hand, we'll probably miss fftw, since I understand that in at least some cases, it is faster than the default scipy fftpack.",
    "created_at": "2009-02-12T10:02:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/455#issuecomment-2275",
    "user": "@jasongrout"
}
```

IIRC, fftw is stripped out of the scipy 0.7 release, so this problem may go away, right?

On the other hand, we'll probably miss fftw, since I understand that in at least some cases, it is faster than the default scipy fftpack.



---

archive/issue_comments_002276.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> IIRC, fftw is stripped out of the scipy 0.7 release, so this problem may go away, right?\n\nIIRC there is still some fft support, but the point is that we should not pick up random crap. \n\n> On the other hand, we'll probably miss fftw, since I understand that in at least some cases, it is faster than the default scipy fftpack.\n\nYes, we need to figure out what to do about that. \n\nI have changed the ticket summary to reflect the intention. I know how to do this, so we can do it during the scipy 0.7 update.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-12T10:10:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/455#issuecomment-2276",
    "user": "mabshoff"
}
```

Replying to [comment:4 jason]:
> IIRC, fftw is stripped out of the scipy 0.7 release, so this problem may go away, right?

IIRC there is still some fft support, but the point is that we should not pick up random crap. 

> On the other hand, we'll probably miss fftw, since I understand that in at least some cases, it is faster than the default scipy fftpack.

Yes, we need to figure out what to do about that. 

I have changed the ticket summary to reflect the intention. I know how to do this, so we can do it during the scipy 0.7 update.

Cheers,

Michael



---

archive/issue_comments_002277.json:
```json
{
    "body": "Scipy is now in version 0.7.0 in Sage.  Has this been done elsewhere in the meantime?  (Perhaps not, since I still need to remove /sw from my own PATH on Mac).",
    "created_at": "2009-12-30T04:39:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/455#issuecomment-2277",
    "user": "@kcrisman"
}
```

Scipy is now in version 0.7.0 in Sage.  Has this been done elsewhere in the meantime?  (Perhaps not, since I still need to remove /sw from my own PATH on Mac).



---

archive/issue_comments_002278.json:
```json
{
    "body": "I wonder if #9208 and #9210 make it so that you don't need to remove /sw from your path anymore.\n\nI don't believe that fftw3 is used anymore in scipy:\n\n\n```\n~/sage% grep \"lfftw3\" install.log\n~/sage%  \n```\n\n\nSo I think this ticket can safely be closed.",
    "created_at": "2010-06-11T06:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/455#issuecomment-2278",
    "user": "@jasongrout"
}
```

I wonder if #9208 and #9210 make it so that you don't need to remove /sw from your path anymore.

I don't believe that fftw3 is used anymore in scipy:


```
~/sage% grep "lfftw3" install.log
~/sage%  
```


So I think this ticket can safely be closed.



---

archive/issue_comments_002279.json:
```json
{
    "body": "(there might be other /usr/local/ libs that are picked up, but fftw won't be since it's not used)",
    "created_at": "2010-06-11T06:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/455#issuecomment-2279",
    "user": "@jasongrout"
}
```

(there might be other /usr/local/ libs that are picked up, but fftw won't be since it's not used)



---

archive/issue_comments_002280.json:
```json
{
    "body": "> I wonder if #9208 and #9210 make it so that you don't need to remove /sw from your path anymore.\nThat might be dangerous.\n> So I think this ticket can safely be closed.\nSo... positive review, sage-invalid?  I'll let you make the call.",
    "created_at": "2012-07-07T04:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/455#issuecomment-2280",
    "user": "@kcrisman"
}
```

> I wonder if #9208 and #9210 make it so that you don't need to remove /sw from your path anymore.
That might be dangerous.
> So I think this ticket can safely be closed.
So... positive review, sage-invalid?  I'll let you make the call.



---

archive/issue_comments_002281.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-22T15:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/455#issuecomment-2281",
    "user": "@mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_002282.json:
```json
{
    "body": "I think we should mark it as invalid.",
    "created_at": "2013-07-22T15:37:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/455#issuecomment-2282",
    "user": "@mwhansen"
}
```

I think we should mark it as invalid.
